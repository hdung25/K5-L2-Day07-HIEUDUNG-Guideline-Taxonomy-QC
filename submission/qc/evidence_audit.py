"""Read-only checks of lab evidence; writes its own audit and command logs only."""
import csv
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[2]
QC=ROOT/'submission/qc'

def read_json(path):
    return json.loads(path.read_text(encoding='utf-8'))

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    commands=[]
    for name,args in [('validate_labels',['--all']),('check_submission',['--round','1'])]:
        result=subprocess.run([sys.executable,'-X','utf8',str(ROOT/'scripts'/f'{name}.py'),*args],cwd=ROOT,capture_output=True,text=True,encoding='utf-8')
        log=QC/f'{name}_latest.txt'
        log.write_text(result.stdout+result.stderr,encoding='utf-8')
        commands.append({'script':name,'exit_code':result.returncode,'log':log.relative_to(ROOT).as_posix()})
    labels={}
    for member in ('101','102'):
        path=ROOT/f'submission/labels/{member}.json'
        data=read_json(path)
        categories={c['id']:c['name'] for c in data['categories']}
        labels[member]={'images':len(data['images']),'annotations':len(data['annotations']),
            'objects':sum(categories[a['category_id']]!='ignore_region' for a in data['annotations']),
            'can_review':sum(str(a.get('attributes',{}).get('can_review',False)).lower()=='true' for a in data['annotations']),
            'sha256':sha(path)}
    with (QC/'calibration_decisions.csv').open(encoding='utf-8-sig',newline='') as stream:
        decisions=list(csv.DictReader(stream))
    required=['case_id','image','quyet_dinh','quy_tac_ghi_vao_guideline','phien_ban_guideline','nguoi_chot','phieu_sua','kiem_lai','pham_vi']
    complete=sum(all(row.get(k,'').strip() for k in required) for row in decisions)
    summary=read_json(QC/'iaa_summary.json')
    locked_ok=all((ROOT/name).is_file() and sha(ROOT/name)==digest for name,digest in summary['inputs'].items())
    artifact_ok=all(sha(QC/name)==digest for name,digest in summary['artifacts'].items())
    baseline=read_json(ROOT/'submission/taxonomy.json')
    final=read_json(ROOT/'submission/taxonomy_v1.1.json')
    missing=[name for name in ['labels_calibrated.json','labels_calibrated.csv','batch_manifest.json',
        'reviews/round-01/qc_review.csv','reviews/round-01/qc_result.json'] if not (QC/name).is_file()]
    result={'decision':'Hold','labels':labels,'coverage_structural':summary['coverage'],
        'independent_iaa_verified':False,'comparison_only':summary['overall'],
        'cases':len(decisions),'decisions_nonempty_all_fields':complete,'decisions_pending':len(decisions)-complete,
        'flagged_images':summary['n_flagged_images'],'locked_input_hashes_match':locked_ok,
        'generated_artifact_hashes_match':artifact_ok,'taxonomy_rules_preserved':baseline['rules']==final['rules'],
        'v1_1_status':'proposal_pending_calibration','missing_final_evidence':missing,'commands':commands,
        'limitations':'Structural validity and matching hashes do not establish annotation correctness or independent human work.'}
    (QC/'evidence_status.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False,indent=2))

if __name__=='__main__':main()
