-- Representative ANSI-style healthcare data-quality checks.
SELECT * FROM eligibility WHERE member_id IS NULL OR TRIM(member_id)='';
SELECT * FROM eligibility WHERE plan_id IS NULL OR TRIM(plan_id)='';
SELECT * FROM eligibility WHERE coverage_end < coverage_start;

SELECT member_id,plan_id,coverage_start,coverage_end,COUNT(*) duplicate_count
FROM eligibility GROUP BY member_id,plan_id,coverage_start,coverage_end HAVING COUNT(*)>1;

SELECT * FROM eligibility WHERE status NOT IN ('Active','Terminated');

SELECT c.* FROM claims c LEFT JOIN eligibility e ON c.member_id=e.member_id
WHERE e.member_id IS NULL;

SELECT c.* FROM claims c LEFT JOIN eligibility e
 ON c.member_id=e.member_id AND c.service_date BETWEEN e.coverage_start AND e.coverage_end
WHERE e.member_id IS NULL;

SELECT source_file,COUNT(*) received_records FROM eligibility GROUP BY source_file;

SELECT plan_id,COUNT(*) member_records,
 ROUND(100.0*COUNT(*)/SUM(COUNT(*)) OVER(),2) pct_of_records
FROM eligibility GROUP BY plan_id;

SELECT EXTRACT(YEAR FROM coverage_start) start_year,
 EXTRACT(MONTH FROM coverage_start) start_month,COUNT(*) enrollment_starts
FROM eligibility
GROUP BY EXTRACT(YEAR FROM coverage_start),EXTRACT(MONTH FROM coverage_start)
ORDER BY start_year,start_month;
