-- Representative ANSI-style healthcare data-quality checks.
-- Adjust date/data types for your SQL platform.

-- Missing critical eligibility fields
SELECT *
FROM eligibility
WHERE member_id IS NULL OR plan_id IS NULL
   OR coverage_start IS NULL OR coverage_end IS NULL;

-- Duplicate eligibility spans
SELECT member_id, plan_id, coverage_start, coverage_end, COUNT(*) AS row_count
FROM eligibility
GROUP BY member_id, plan_id, coverage_start, coverage_end
HAVING COUNT(*) > 1;

-- Invalid coverage sequencing
SELECT *
FROM eligibility
WHERE coverage_end < coverage_start;

-- Unsupported status / plan
SELECT *
FROM eligibility
WHERE status NOT IN ('Active','Terminated')
   OR plan_id NOT IN ('PLAN_A','PLAN_B','PLAN_C');

-- Claims with no eligibility member match
SELECT c.*
FROM claims c
LEFT JOIN eligibility e ON c.member_id=e.member_id
WHERE e.member_id IS NULL;

-- Claims whose service date is outside all matching coverage spans
SELECT c.*
FROM claims c
LEFT JOIN eligibility e
  ON c.member_id=e.member_id
 AND c.service_date BETWEEN e.coverage_start AND e.coverage_end
WHERE e.member_id IS NULL;
