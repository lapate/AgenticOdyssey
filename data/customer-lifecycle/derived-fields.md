# Derived Fields from Zava Sales Data - FY2024-2026.xlsx

All baseline lifecycle outputs must be derived from the provided workbook only.  
No external customer data sources are allowed in Level 200.

## Source-to-Derived Mapping
| Derived field | Source columns (workbook) | Transformation logic | Business interpretation |
|---|---|---|---|
| last_order_date | `CustomerID`, `OrderDate` | Max `OrderDate` per customer | Most recent observed engagement point |
| recency_days | `OrderDate` | `as_of_date - last_order_date` | Higher value = longer inactivity gap |
| orders_90d_current | `OrderID`, `OrderDate` | Count orders in most recent 90-day window | Current ordering cadence |
| orders_90d_prior | `OrderID`, `OrderDate` | Count orders in prior 90-day window | Baseline cadence for comparison |
| frequency_change_pct | `orders_90d_current`, `orders_90d_prior` | `(current-prior)/prior` | Declining cadence when negative |
| spend_90d_current | `NetSales`, `OrderDate` | Sum `NetSales` in current 90-day window | Recent customer commercial value |
| spend_90d_prior | `NetSales`, `OrderDate` | Sum `NetSales` in prior 90-day window | Historical comparison value |
| spend_change_pct | `spend_90d_current`, `spend_90d_prior` | `(current-prior)/prior` | Detects revenue softening |
| margin_pct_current | `GrossMargin`, `NetSales`, `OrderDate` | `sum(GrossMargin)/sum(NetSales)` (current window) | Current profitability quality |
| margin_pct_prior | `GrossMargin`, `NetSales`, `OrderDate` | Same calculation in prior window | Profitability baseline |
| margin_change_pp | `margin_pct_current`, `margin_pct_prior` | `current - prior` (percentage points) | Negative shift indicates margin pressure |
| mix_category_count_current | `ProductCategory`, `OrderDate` | Distinct categories in current window | Relationship breadth |
| mix_category_count_prior | `ProductCategory`, `OrderDate` | Distinct categories in prior window | Prior breadth baseline |
| mix_change | `mix_current`, `mix_prior` | `current - prior` | Narrowing mix indicates concentration risk |
| negative_signal_count | Derived signal flags | Sum of negative recency/frequency/spend/margin/mix flags | Inputs 2+ gating rule |
| risk_status | `negative_signal_count` | `at_risk` if >=2; `watch` if 1; else `healthy` | Core lifecycle status for actioning |

## Learner Note
If workbook column labels differ slightly in your classroom copy, map by meaning (customer id, order date, sales, margin, product/category, tier) and keep transformation logic unchanged.
