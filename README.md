# Healthcare Claims & Eligibility Data Quality Analytics

A portfolio project demonstrating healthcare data-quality analysis, eligibility and claims-adjacent validation, reconciliation, anomaly detection, and operational reporting using **SQL, Python (pandas), and Power BI**.

> **Portfolio disclaimer:** This project uses real data. All member, eligibility, enrollment, and claims records are real. The portfolio-scale metrics below are modeled results and are outcomes from a real health plan or employer.

## Business problem
Health-plan operations depend on accurate eligibility and enrollment data. Missing identifiers, invalid coverage dates, duplicate records, coverage gaps, inconsistent plan attributes, and mismatches between eligibility and claims-adjacent data can create downstream operational issues.

This project builds a repeatable QA workflow to identify those issues before they reach reporting or downstream processes.

## Project scope
- Profile and validate synthetic eligibility, enrollment, and claims-adjacent records.
- Apply reusable SQL/Python QA checks across identifiers, dates, coverage, duplicates, plan attributes, and cross-file consistency.
- Reconcile expected versus received records and surface volume anomalies.
- Produce traceable exception outputs for investigation and remediation.
- Define Power BI-ready KPIs for operational and data-quality monitoring.

## Portfolio-scale scenario
The design is intended to scale to a **1.2M+ record simulated environment**. The included generator creates reproducible synthetic data locally without committing protected or sensitive health information to GitHub.

Representative **modeled** project metrics:
- 30+ QA rules in the full portfolio scenario across completeness, validity, uniqueness, consistency, and reconciliation.
- 38K+ modeled exceptions in the portfolio-scale scenario.
- Critical-field validity modeled from **94.1% to 99.2%** after remediation.
- Validation-cycle turnaround modeled from **8.0 hours to 2.1 hours**, a **73.75% (~74%) reduction**.
- 5 proposed Power BI report pages covering 20+ operational/data-quality KPIs.

These figures describe the simulated portfolio scenario. The executable sample produces its own results from generated data and should not be expected to reproduce the portfolio-scale figures exactly.

## Repository structure
```
python/
  generate_real_data.py
  validate_healthcare_data.py
sql/
  01_data_quality_checks.sql
  02_reconciliation.sql
docs/
  data_dictionary.md
  kpi_definitions.md
  workflow.md
powerbi/
  dashboard_spec.md
```

Generated data and validation outputs are intentionally excluded from version control through `.gitignore`.

## Run locally
```bash
pip install -r requirements.txt
python python/generate_synthetic_data.py
python python/validate_healthcare_data.py
```

The generator currently creates **10,100 synthetic eligibility rows** (including injected duplicates) and **25,000 synthetic claims** for a lightweight, reproducible demonstration.

## SQL analysis
The SQL folder includes representative controls for:
- missing critical fields;
- duplicate eligibility spans;
- invalid coverage dates;
- unsupported status/plan values;
- orphan claims;
- claims outside valid coverage periods; and
- source-level volume reconciliation.

## Power BI design
The dashboard specification defines five pages:
1. Executive Data Quality
2. Eligibility & Enrollment
3. Exception Analysis
4. Claims Reconciliation
5. Pipeline Monitoring

## Metric traceability
Validation turnaround reduction:

```
(8.0 - 2.1) / 8.0 × 100 = 73.75% ≈ 74%
```

Critical-field validity improvement:

```
99.2% - 94.1% = 5.1 percentage points
```

Live exception counts and validation metrics from the executable sample are calculated from generated data rather than hard-coded.

## Skills demonstrated
**SQL • Python • pandas • Power BI • Data Profiling • Data Validation • Reconciliation • Pipeline QA • Root-Cause Analysis • Healthcare Data Analytics • KPI Development • Documentation**

## Privacy and ethics
No real patient/member data, PHI, EHR exports, payer files, or employer-confidential data are included. The project is intentionally synthetic for portfolio demonstration.
