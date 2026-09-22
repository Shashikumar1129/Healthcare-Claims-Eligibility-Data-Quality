# Data Quality Workflow

1. **Intake:** capture source, batch, record count and load context.
2. **Profile:** measure counts, nulls, duplicates, dates and categorical distributions.
3. **Validate:** run completeness, validity, uniqueness, consistency and reconciliation controls.
4. **Log exceptions:** retain rule ID, severity, record and reason for traceability.
5. **Reconcile:** compare expected/received volumes and claims-adjacent records to eligibility.
6. **Investigate root cause:** group failures by rule, source, plan and batch.
7. **Validate remediation:** rerun identical controls after fixes and compare results.
8. **Report:** publish curated KPIs for Power BI and stakeholder review.

The workflow separates detection from remediation; QA controls do not silently modify source data.
