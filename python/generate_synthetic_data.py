"""Generate reproducible synthetic healthcare eligibility and claims-adjacent data."""
from pathlib import Path
import numpy as np
import pandas as pd

SEED = 42
N_MEMBERS = 10000
rng = np.random.default_rng(SEED)
root = Path(__file__).resolve().parents[1]
out = root / "data" / "generated"
out.mkdir(parents=True, exist_ok=True)

member_ids = [f"M{i:07d}" for i in range(1, N_MEMBERS + 1)]
starts = pd.to_datetime("2026-01-01") + pd.to_timedelta(rng.integers(0, 180, N_MEMBERS), unit="D")
ends = starts + pd.to_timedelta(rng.integers(90, 366, N_MEMBERS), unit="D")
elig = pd.DataFrame({"member_id":member_ids,"plan_id":rng.choice(["PLAN_A","PLAN_B","PLAN_C"],N_MEMBERS,p=[.5,.3,.2]),"coverage_start":starts,"coverage_end":ends,"status":rng.choice(["Active","Terminated"],N_MEMBERS,p=[.88,.12]),"source_file":"synthetic_eligibility.csv"})

null_idx=rng.choice(elig.index,size=120,replace=False)
elig.loc[null_idx,"member_id"]=pd.NA
bad_idx=rng.choice(elig.index.difference(null_idx),size=80,replace=False)
elig.loc[bad_idx,"coverage_end"]=elig.loc[bad_idx,"coverage_start"]-pd.Timedelta(days=10)
elig=pd.concat([elig,elig.sample(100,random_state=SEED)],ignore_index=True)

n_claims=25000
claims=pd.DataFrame({"claim_id":[f"C{i:08d}" for i in range(1,n_claims+1)],"member_id":rng.choice(member_ids+["M9999999"],n_claims),"service_date":pd.to_datetime("2026-01-01")+pd.to_timedelta(rng.integers(0,365,n_claims),unit="D"),"claim_amount":np.round(rng.lognormal(5.2,1.0,n_claims),2),"claim_status":rng.choice(["Paid","Pending","Denied"],n_claims,p=[.72,.13,.15])})
elig.to_csv(out/"eligibility.csv",index=False)
claims.to_csv(out/"claims.csv",index=False)
print(f"Generated {len(elig):,} eligibility rows and {len(claims):,} claims rows in {out}")
