# Lab 11 — Pro-Forma Sensitivity Inputs: Figure Technology Solutions

All dollar figures are USD millions. This is the **R — choose the inputs and the comparison** record for the existing Lab 10 Figure pro-forma. The model forecasts **FCFE**, not FCFF, and the valuation is an FCFE equity-value model.

## Model scope and driver mapping

Figure's business value is driven principally by (1) consumer-loan marketplace volume and (2) the fee/margin earned on that volume. The Lab 10 model does not yet forecast separate loan-volume or take-rate lines. To use only existing independent assumptions, I use the following reproducible proxies:

- **Marketplace volume / revenue growth:** the existing `revenue_growth` path. It is a revenue-growth proxy for loan-marketplace volume and adoption; it is not a claim that revenue and volume are identical.
- **Unit economics / operating margin:** the existing `other_operating_expense_to_revenue` input. Reducing this cost ratio raises operating margin and is the model's available proxy for better take rate, pricing, or operating efficiency. The displayed operating margin is calculated, so it is not changed directly.

This preserves the Lab 10 model's assumption structure rather than adding unsourced standalone volume or take-rate assumptions.

## Driver 1 — Marketplace volume / revenue growth

| Case | FY2026E | FY2027E | FY2028E | FY2029E | FY2030E | Units |
|---|---:|---:|---:|---:|---:|---|
| Lower | 30% | 25% | 20% | 15% | 10% | Year-over-year revenue growth |
| Base | 35% | 30% | 25% | 20% | 15% | Year-over-year revenue growth |
| Higher | 40% | 35% | 30% | 25% | 20% | Year-over-year revenue growth |

**Affected forecast years:** FY2026E–FY2030E.

**Range design:** lower and higher each apply a **5 percentage-point** shift to every forecast year. This is a percentage-point change, not a 5% proportional change. Figure's reported revenue growth was 62.7% in FY2024 and 48.7% in FY2025. The base path already steps down below that history; the lower case tests a faster deceleration, while the higher case tests stronger loan-marketplace growth and partner adoption. This is a labelled judgment, not company guidance.

## Driver 2 — Unit economics / operating margin

| Case | Independent input: other operating expense / revenue | Implied operating margin* | Units | Affected forecast years |
|---|---:|---:|---|---|
| Lower cost / higher margin | 48.78% | 25.19% | Percent of revenue | FY2026E–FY2030E |
| Base | 50.78% | 23.19% | Percent of revenue | FY2026E–FY2030E |
| Higher cost / lower margin | 52.78% | 21.19% | Percent of revenue | FY2026E–FY2030E |

\*Implied operating margin = 1 − SG&A / revenue − other operating expense / revenue. The model holds SG&A / revenue at its existing base assumption of 26.04%.

**Range design:** the independent cost-ratio input moves by **2 percentage points** from base in each direction in every forecast year. The base 50.78% equals FY2025 total operating expenses excluding G&A divided by FY2025 revenue. A two-point range is a labelled judgment that tests whether Figure can retain more of each revenue dollar through better marketplace pricing/take rate or operating efficiency, versus a weaker funding and loan-sale environment that raises variable operating costs. It does not change revenue growth, SG&A / revenue, taxes, balance-sheet ratios, discount rate, or any other base input.

## Common outputs for every run

Every lower, base, and higher run will report the same outputs from the fully linked model:

| Output | Definition | Units |
|---|---|---|
| Final-year operating profit | FY2030E operating income | USD millions |
| Final-year free cash flow | FY2030E free cash flow to equity (**FCFE**) | USD millions |
| Value per share | FCFE equity value divided by 141.802 million diluted shares, only if the model's FCFE valuation remains valid | USD per share |

## Base-case reference run

The Lab 10 model was run on September 29, 2026 at 17:23:27 ET before sensitivity work.

| Output | Base result |
|---|---:|
| FY2030E operating income | $355.8m |
| FY2030E FCFE | $256.4m |
| Equity value | $1,814.9m |
| Value per share | $12.80 |
| FY2025A and FY2026E–FY2030E balance checks | Passed; each displayed assets − liabilities − equity = $0.0m |

## Locked Changed-Input Record — prediction before running

**Timestamp:** September 29, 2026, 17:23:27 ET

| Planned one-at-a-time run | Input change | Expected output direction and rough size | Why |
|---|---|---|---|
| Volume / growth — lower | Revenue growth: base path to lower path above | FY2030E operating income, FCFE, and value per share should all decline materially. | Compounding a lower revenue path reduces revenue in every forecast year; fixed revenue ratios then flow through to operating income and FCFE. |
| Volume / growth — higher | Revenue growth: base path to higher path above | FY2030E operating income, FCFE, and value per share should all increase materially. | Compounding a higher revenue path increases the revenue base that earns the model's existing margins. |
| Unit economics — lower cost / higher margin | Other operating expense / revenue: 50.78% to 48.78% in every forecast year | Operating income, FCFE, and value per share should increase; the direct operating-profit effect should be approximately 2% of revenue before taxes. | Each revenue dollar carries two cents less other operating expense while all other independent inputs stay at base. |
| Unit economics — higher cost / lower margin | Other operating expense / revenue: 50.78% to 52.78% in every forecast year | Operating income, FCFE, and value per share should decrease; the direct operating-profit effect should be approximately 2% of revenue before taxes. | Each revenue dollar carries two cents more other operating expense while all other independent inputs stay at base. |

## Source and interpretation note

The historical revenue figures and FY2025 expense ratios are from Figure's FY2025 Form 10-K. Figure identifies consumer-loan marketplace volume as a key scale measure and defines net take rate from marketplace and loan economics, but this Lab 10 model does not separately model those metrics. The sensitivity therefore uses existing revenue-growth and operating-expense-ratio inputs as transparent proxies. [Figure FY2025 Form 10-K](https://www.sec.gov/Archives/edgar/data/2064124/000206412426000009/figr-20251231.htm)

## I — one-at-a-time sensitivity results

Each scenario began with a fresh copy of the Lab 10 base inputs. Only the named independent input changed; linked statements, balance-sheet amounts, FCFE, and valuation recalculated. All output cash flow figures below are **FCFE**.

### Marketplace volume / revenue growth

| Case | Actual input path (FY2026E–FY2030E) | FY2030E operating income | Change vs. base | FY2030E FCFE | Change vs. base | Value per share | Change vs. base | Accounting checks |
|---|---|---:|---:|---:|---:|---:|---:|---|
| Lower | 30%, 25%, 20%, 15%, 10% | $289.9m | $(65.9)m | $212.8m | $(43.7)m | $10.90 | $(1.90) | Pass |
| Base | 35%, 30%, 25%, 20%, 15% | $355.8m | $0.0m | $256.4m | $0.0m | $12.80 | $0.00 | Pass |
| Higher | 40%, 35%, 30%, 25%, 20% | $433.1m | +$77.3m | $307.0m | +$50.5m | $14.98 | +$2.18 | Pass |
| **Output span** | Maximum minus minimum | **$143.2m** | — | **$94.2m** | — | **$4.08** | — | All valid |

### Unit economics / operating margin

| Case | Actual independent input: other operating expense / revenue | FY2030E operating income | Change vs. base | FY2030E FCFE | Change vs. base | Value per share | Change vs. base | Accounting checks |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Lower cost / higher margin | 48.78% | $386.5m | +$30.7m | $280.7m | +$24.2m | $14.02 | +$1.22 | Pass |
| Base | 50.78% | $355.8m | $0.0m | $256.4m | $0.0m | $12.80 | $0.00 | Pass |
| Higher cost / lower margin | 52.78% | $325.1m | $(30.7)m | $232.2m | $(24.2)m | $11.58 | $(1.22) | Pass |
| **Output span** | Maximum minus minimum | **$61.4m** | — | **$48.5m** | — | **$2.44** | — | All valid |

### Traceable selected result: higher revenue-growth case

| FY2030E linked line | Result | Units |
|---|---:|---|
| Revenue | $1,868.1m | USD millions |
| Other operating expense | $948.5m | USD millions |
| Operating income | $433.1m | USD millions |
| FCFE | $307.0m | USD millions |
| Assets − liabilities − equity | $0.0m | USD millions; balance check passed |

### Restored-base check

After all scenarios, the script re-ran the original base revenue-growth path. FY2030E operating income was **$355.8m**, FY2030E FCFE was **$256.4m**, value per share was **$12.80**, and all accounting checks passed. The before-and-after base check passed.

## V — result check

Dollar-million outputs are displayed to one decimal place and per-share values to two decimal places. Signed changes are calculated from the underlying unrounded model output; a reader recomputing from displayed values should use a rounding tolerance of **$0.1m** for dollar-million outputs and **$0.01** per share.

| Check | Evidence from the run | Result |
|---|---|---|
| Base before and after the analysis | Base before: FY2030E operating income $355.8m, FCFE $256.4m, and value/share $12.80. Restored base: the same displayed inputs and outputs. | Pass |
| Lower or higher run | The independent-input audit reported only `revenue_growth` changed in each non-base revenue case and only `other_operating_expense_to_revenue` changed in each non-base unit-economics case. Each run started from a fresh base copy. | Pass |
| Accounting checks | Every usable case printed `PASS`; FY2030E assets − liabilities − equity was $0.0m in each trace. No runs were invalid. | Pass |
| Change from base | Each signed change is calculated in the script as changed unrounded output minus base unrounded output; the displayed tables reconcile within the stated rounding tolerance. | Pass |

The code also reports `Base inputs restored: PASS` after the final base rerun.

## Locked prediction reconciliation

**Selected locked prediction:** Marketplace volume / revenue growth — higher case. The pre-run record predicted that moving the revenue-growth path from 35%, 30%, 25%, 20%, and 15% to 40%, 35%, 30%, 25%, and 20% would increase FY2030E operating income, FCFE, and value per share materially because the larger revenue base would compound through the model.

| Output | Base | Higher-growth actual | Actual change from base | Reconciliation |
|---|---:|---:|---:|---|
| FY2030E operating income | $355.8m | $433.1m | +$77.3m | Increase as predicted |
| FY2030E FCFE | $256.4m | $307.0m | +$50.5m | Increase as predicted |
| Value per share | $12.80 | $14.98 | +$2.18 | Increase as predicted |

The prediction was correct in direction and described the size only as “materially,” so there is no numerical prediction-error claim to reconcile beyond the actual signed changes above. The source of the effect is traceable in the higher-growth run: FY2030E revenue increased to $1,868.1m, and the model recalculated operating expense, operating income, FCFE, and valuation from that higher revenue base.

## E — find the driver

Over the stated sensitivity ranges, **marketplace volume / revenue growth** is the larger driver for every reported output.

| Output | Marketplace volume / revenue-growth span | Unit-economics / operating-margin span | Larger driver over these ranges |
|---|---:|---:|---|
| FY2030E operating income | $143.2m | $61.4m | Marketplace volume / revenue growth |
| FY2030E FCFE | $94.2m | $48.5m | Marketplace volume / revenue growth |
| Value per share | $4.08 | $2.44 | Marketplace volume / revenue growth |

The causal link is that the revenue-growth path compounds into a different FY2030E revenue base: $1,250.3m in the lower case, $1,534.5m in the base case, and $1,868.1m in the higher case. With the model's other revenue-linked assumptions recalculating, that larger or smaller revenue base flows through to operating income, FCFE, and the FCFE valuation. The unit-economics driver changes the cost retained on each dollar of revenue, but it does so on the same base-case revenue path.

This ranking applies **only over these stated ranges**: a ±5-percentage-point shift to each annual revenue-growth assumption versus a ±2-percentage-point shift to other operating expense as a percentage of revenue. The larger revenue-growth span can partly reflect its wider selected range and compounding effect; it does not establish that revenue growth is always more important than unit economics, nor does it assign a probability to either case.

## Partner exchange 3 — to complete in class

Add your partner's question about this ranking, your answer, and the question/check you performed on your partner's result. These notes require your actual partner exchange and are intentionally not generated here.
