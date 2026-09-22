"""Run core data-quality checks and produce traceable exception outputs."""
from pathlib import Path
import pandas as pd
root=Path(__file__).resolve().parents[1]
base=root/"data"/"generated"
ep=base/"eligibility.csv"; cp=base/"claims.csv"
if not ep.exists(): ep=root/"data"/"sample_eligibility.csv"; cp=root/"data"/"sample_claims.csv"
elig=pd.read_csv(ep,parse_dates=["coverage_start","coverage_end"])
claims=pd.read_csv(cp,parse_dates=["service_date"])
exceptions=[]
def flag(mask,rule,severity,reason):
    for i in elig.index[mask]:
        exceptions.append({"rule_id":rule,"severity":severity,"record_index":int(i),"member_id":elig.at[i,"member_id"],"reason":reason})
flag(elig.member_id.isna(),"ELG001","Critical","Missing member identifier")
flag(elig.plan_id.isna(),"ELG002","Critical","Missing plan identifier")
flag(elig.coverage_start.isna(),"ELG003","Critical","Missing coverage start")
flag(elig.coverage_end.isna(),"ELG004","Critical","Missing coverage end")
flag(elig.coverage_end<elig.coverage_start,"ELG005","Critical","Coverage end precedes start")
flag(elig.duplicated(["member_id","plan_id","coverage_start","coverage_end"],keep=False),"ELG006","High","Duplicate eligibility span")
flag(~elig.status.isin(["Active","Terminated"]),"ELG007","Medium","Invalid status")
flag(~elig.plan_id.isin(["PLAN_A","PLAN_B","PLAN_C"]),"ELG008","High","Unknown plan")
valid=set(elig.member_id.dropna())
orphans=claims.loc[~claims.member_id.isin(valid)].copy()
orphans["rule_id"]="CLM001"; orphans["severity"]="Critical"; orphans["reason"]="Claim member not found in eligibility"
exc=pd.DataFrame(exceptions)
out=root/"outputs"; out.mkdir(exist_ok=True)
exc.to_csv(out/"eligibility_exceptions.csv",index=False); orphans.to_csv(out/"orphan_claims.csv",index=False)
critical=int((exc.severity=="Critical").sum()) if not exc.empty else 0
validity=100*(1-critical/len(elig)) if len(elig) else 0
print(f"Eligibility rows evaluated: {len(elig):,}")
print(f"Eligibility exceptions: {len(exc):,}")
print(f"Orphan claims: {len(orphans):,}")
print(f"Critical-field validity proxy: {validity:.2f}%")
