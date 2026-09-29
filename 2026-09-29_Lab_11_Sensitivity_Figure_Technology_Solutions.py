"""Lab 11 one-at-a-time sensitivity analysis for Figure Technology Solutions.

This script leaves the Lab 10 pro-forma unchanged. Every scenario begins with
a fresh deep copy of Lab 10's base assumptions and opening balance sheet.
Amounts are USD millions except per-share values.
"""

from copy import deepcopy
from importlib.util import module_from_spec, spec_from_file_location
from math import isclose
from pathlib import Path


MODEL_PATH = Path(__file__).with_name("2026-09-24_Lab_10_Figure_Technology_Solutions.py")
SPEC = spec_from_file_location("figure_lab_10", MODEL_PATH)
if SPEC is None or SPEC.loader is None:
    raise ImportError(f"Cannot load Lab 10 model from {MODEL_PATH}")
MODEL = module_from_spec(SPEC)
SPEC.loader.exec_module(MODEL)

BASE_ASSUMPTIONS = deepcopy(MODEL.ASSUMPTIONS)
BASE_OPENING = deepcopy(MODEL.OPENING)

# R-step inputs from 2026-09-29_Lab_11_Operating_Drivers_Figure_Technology_Solutions.md.
SENSITIVITIES = {
    "Marketplace volume / revenue growth": {
        "units": "year-over-year revenue growth",
        "input_key": "revenue_growth",
        "cases": {
            "Lower": {2026: 0.30, 2027: 0.25, 2028: 0.20, 2029: 0.15, 2030: 0.10},
            "Base": BASE_ASSUMPTIONS["revenue_growth"],
            "Higher": {2026: 0.40, 2027: 0.35, 2028: 0.30, 2029: 0.25, 2030: 0.20},
        },
    },
    "Unit economics / operating margin": {
        "units": "other operating expense as a percent of revenue",
        "input_key": "other_operating_expense_to_revenue",
        "cases": {
            "Lower cost / higher margin": BASE_ASSUMPTIONS["other_operating_expense_to_revenue"] - 0.02,
            "Base": BASE_ASSUMPTIONS["other_operating_expense_to_revenue"],
            "Higher cost / lower margin": BASE_ASSUMPTIONS["other_operating_expense_to_revenue"] + 0.02,
        },
    },
}


def format_input(value, units):
    """Display scalar or annual-path assumption values with their units."""
    if isinstance(value, dict):
        return ", ".join(f"FY{year}E {value[year]:.1%}" for year in sorted(value))
    return f"{value:.2%}"


def balance_gap(state):
    """Return assets less liabilities and equity for a projection year."""
    assets = state["inventory"] + state["ppe"] + state["other_assets"] + state["cash"]
    liabilities_and_equity = (
        state["floor_plan"] + state["debt"] + state["other_liabilities"] + state["equity"]
    )
    return assets - liabilities_and_equity


def changed_assumption_keys(scenario_assumptions):
    """Identify independent assumptions that differ from the preserved base set."""
    return sorted(
        key for key in BASE_ASSUMPTIONS if scenario_assumptions[key] != BASE_ASSUMPTIONS[key]
    )


def run_case(input_key, input_value):
    """Run a scenario from a fresh Lab 10 base; restore module state afterward."""
    original_assumptions = MODEL.ASSUMPTIONS
    original_opening = MODEL.OPENING
    scenario_assumptions = deepcopy(BASE_ASSUMPTIONS)
    scenario_opening = deepcopy(BASE_OPENING)
    scenario_assumptions[input_key] = deepcopy(input_value)
    changed_keys = changed_assumption_keys(scenario_assumptions)

    try:
        MODEL.ASSUMPTIONS = scenario_assumptions
        MODEL.OPENING = scenario_opening
        projections = MODEL.project()
        final = projections[-1]
        checks_pass = all(isclose(balance_gap(state), 0.0, abs_tol=0.05) for state in projections)
        value_per_share = None
        valuation_status = "Valid"
        try:
            _, _, value_per_share = MODEL.value_equity(projections)
        except ValueError as error:
            valuation_status = f"Unavailable: {error}"
        return {
            "projections": projections,
            "final_operating_income": final["operating_income"],
            "final_fcfe": final["fcfe"],
            "value_per_share": value_per_share,
            "valuation_status": valuation_status,
            "checks_pass": checks_pass,
            "changed_assumption_keys": changed_keys,
            "only_selected_input_changed": changed_keys == ([] if input_value == BASE_ASSUMPTIONS[input_key] else [input_key]),
        }
    finally:
        MODEL.ASSUMPTIONS = original_assumptions
        MODEL.OPENING = original_opening


def print_case(driver, case, input_value, result, base_result, units=None):
    """Print a scenario's requested outputs and a traceable final-year detail."""
    print(f"\n{driver} - {case}")
    display_units = units or SENSITIVITIES[driver]["units"]
    print(f"Changed independent input: {format_input(input_value, display_units)} ({display_units})")
    print(f"FY2030E operating income: ${result['final_operating_income']:,.1f}m "
          f"({result['final_operating_income'] - base_result['final_operating_income']:+,.1f}m vs. base)")
    print(f"FY2030E FCFE: ${result['final_fcfe']:,.1f}m "
          f"({result['final_fcfe'] - base_result['final_fcfe']:+,.1f}m vs. base)")
    if result["value_per_share"] is None:
        print(f"Value per share: unavailable - {result['valuation_status']}")
    else:
        print(f"Value per share: ${result['value_per_share']:,.2f} "
              f"({result['value_per_share'] - base_result['value_per_share']:+,.2f} vs. base)")
    print(f"Accounting checks: {'PASS' if result['checks_pass'] else 'FAIL'}")
    changed_keys = ", ".join(result["changed_assumption_keys"]) or "none (base case)"
    print(f"Independent-input audit: {'PASS' if result['only_selected_input_changed'] else 'FAIL'}; changed key(s): {changed_keys}")

    final = result["projections"][-1]
    print("FY2030E trace: "
          f"revenue ${final['revenue']:,.1f}m; other operating expense ${final['other_operating_expense']:,.1f}m; "
          f"operating income ${final['operating_income']:,.1f}m; FCFE ${final['fcfe']:,.1f}m; "
          f"assets - liabilities - equity ${balance_gap(final):.1f}m")


def print_span(driver, results):
    """Print maximum-minus-minimum output spans across valid scenario results."""
    print(f"\n{driver} output spans (maximum - minimum across cases)")
    for label, key, unit in [
        ("FY2030E operating income", "final_operating_income", "USD millions"),
        ("FY2030E FCFE", "final_fcfe", "USD millions"),
    ]:
        values = [result[key] for result in results.values()]
        print(f"{label}: ${max(values) - min(values):,.1f}m ({unit})")

    valuation_values = [result["value_per_share"] for result in results.values() if result["value_per_share"] is not None]
    if len(valuation_values) == len(results):
        print(f"Value per share: ${max(valuation_values) - min(valuation_values):,.2f} (USD per share)")
    else:
        print("Value per share: unavailable for one or more cases; no span reported.")


def main():
    base_before = run_case("revenue_growth", BASE_ASSUMPTIONS["revenue_growth"])
    print("Lab 11 - Figure Technology Solutions one-at-a-time sensitivity analysis")
    print("Base input set is copied fresh before every scenario. Output cash flow is FCFE.")
    print_case(
        "Restored base reference", "Base before analysis", BASE_ASSUMPTIONS["revenue_growth"], base_before, base_before,
        "year-over-year revenue growth",
    )

    for driver, definition in SENSITIVITIES.items():
        results = {}
        for case, input_value in definition["cases"].items():
            results[case] = run_case(definition["input_key"], input_value)
            print_case(driver, case, input_value, results[case], base_before)
        print_span(driver, results)

    base_after = run_case("revenue_growth", BASE_ASSUMPTIONS["revenue_growth"])
    base_matches = (
        isclose(base_before["final_operating_income"], base_after["final_operating_income"], abs_tol=0.05)
        and isclose(base_before["final_fcfe"], base_after["final_fcfe"], abs_tol=0.05)
        and base_before["value_per_share"] is not None
        and base_after["value_per_share"] is not None
        and isclose(base_before["value_per_share"], base_after["value_per_share"], abs_tol=0.005)
        and base_after["checks_pass"]
        and base_before["only_selected_input_changed"]
        and base_after["only_selected_input_changed"]
        and MODEL.ASSUMPTIONS == BASE_ASSUMPTIONS
        and MODEL.OPENING == BASE_OPENING
    )
    print("\nRestored base check")
    print(f"FY2030E operating income: ${base_after['final_operating_income']:,.1f}m")
    print(f"FY2030E FCFE: ${base_after['final_fcfe']:,.1f}m")
    print(f"Value per share: ${base_after['value_per_share']:,.2f}")
    print(f"Base inputs restored: {'PASS' if MODEL.ASSUMPTIONS == BASE_ASSUMPTIONS and MODEL.OPENING == BASE_OPENING else 'FAIL'}")
    print(f"Base before and after analysis: {'PASS' if base_matches else 'FAIL'}")
    if not base_matches:
        raise AssertionError("Restored base outputs do not match the pre-analysis base run.")


if __name__ == "__main__":
    main()
