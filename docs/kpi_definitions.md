# KPI Definitions

- **Completeness rate:** populated required fields / required fields evaluated × 100.
- **Critical-field validity:** records without critical validation exception / records evaluated × 100.
- **Exception rate:** records triggering a QA rule / records evaluated × 100.
- **Duplicate rate:** duplicate eligibility records / eligibility records evaluated × 100.
- **Orphan-claim rate:** claims with no matching eligibility member / claims evaluated × 100.
- **Coverage mismatch rate:** claims outside a matching coverage span / claims evaluated × 100.
- **Source volume variance:** (received − expected) / expected × 100.

Portfolio scenario validity: 94.1% → 99.2% = **+5.1 percentage points**.

Portfolio scenario validation turnaround: 8.0h → 2.1h; (8.0−2.1)/8.0 = **73.75% (~74%) reduction**.

Live exception KPIs should always be calculated from the generated/loaded dataset, not hard-coded.
