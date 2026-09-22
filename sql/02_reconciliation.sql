-- Reconciliation examples

-- Eligibility population and distinct members
SELECT COUNT(*) AS eligibility_rows,
       COUNT(DISTINCT member_id) AS distinct_members
FROM eligibility;

-- Claims reconciliation status
SELECT c.claim_id, c.member_id, c.service_date, c.claim_amount,
       CASE WHEN e.member_id IS NULL THEN 'NO_VALID_COVERAGE'
            ELSE 'MATCHED' END AS reconciliation_status
FROM claims c
LEFT JOIN eligibility e
  ON c.member_id=e.member_id
 AND c.service_date BETWEEN e.coverage_start AND e.coverage_end;

-- Source-level volume monitoring
SELECT source_file,
       COUNT(*) AS received_rows,
       COUNT(DISTINCT member_id) AS distinct_members
FROM eligibility
GROUP BY source_file;
