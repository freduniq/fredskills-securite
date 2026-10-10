#!/usr/bin/env python3
"""Scanner local de triage heuristique : lecture seule, sans réseau, sortie sans extraits de code."""
from __future__ import annotations
import argparse
import json
import re
from collections import Counter
from dataclasses import dataclass, asdict
from pathlib import Path

EXCLUDED={'.git','.svn','.hg','node_modules','vendor','.next','dist','build','coverage','.venv','venv','__pycache__','.idea','.tox','.mypy_cache','storage','tmp','logs','site-packages'}
SUFFIXES={'.php','.phtml','.js','.jsx','.ts','.tsx','.mjs','.cjs','.py','.java','.cs','.go','.rb','.html','.htm','.vue','.svelte','.conf','.ini','.yml','.yaml','.toml','.sql','.tf','.sh','.xml','.properties'}
LOCKS={'package-lock.json','pnpm-lock.yaml','yarn.lock','bun.lock','bun.lockb','poetry.lock','uv.lock','pdm.lock','composer.lock','gemfile.lock','cargo.lock','go.sum'}
LIMIT_FILES=5000
LIMIT_FINDINGS=250
LIMIT_SIZE=1000000

@dataclass(frozen=True)
class Finding:
    rule: str
    severity: str
    confidence: str
    path: str
    line: int
    message: str
    recommendation: str
    status: str = 'suspect (à vérifier manuellement)'

RULES=[
('R001','élevé','moyenne',r'\b(?:eval|assert)\s*\(\s*(?![\"\x27])','Interpréteur de code potentiellement dynamique','Remplacer par une opération structurée sans évaluation de code.'),
('R002','élevé','moyenne',r'\b(?:unserialize|pickle\.loads|yaml\.unsafe_load|yaml\.load)\s*\(','Désérialisation à risque à examiner','Accepter des objets typés ou JSON validé plutôt que des objets arbitraires.'),
('R003','élevé','faible',r'\b(?:shell_exec|passthru|proc_open|popen|os\.system|subprocess\.Popen)\s*\(','Appel de processus à analyser','Éviter le shell et vérifier l’origine des arguments.'),
('R004','élevé','moyenne',r'(?:NODE_TLS_REJECT_UNAUTHORIZED\s*=\s*[\"\x27]?0|verify\s*=\s*False|CURLOPT_SSL_VERIFYPEER\s*,\s*false)','Vérification TLS possiblement désactivée','Réactiver TLS et valider les certificats.'),
('R005','modéré','faible',r'(?:innerHTML\s*=|dangerouslySetInnerHTML|document\.write\s*\()','Point de rendu HTML à examiner','Préférer textContent et sanitation HTML si nécessaire.'),
('R006','élevé','faible',r'(?:PDO::ATTR_EMULATE_PREPARES\s*=>\s*true|mysqli_multi_query\s*\()','Paramétrage SQL potentiellement dangereux','Vérifier la paramétrisation des requêtes.'),
('R007','modéré','faible',r'(?:\bDEBUG\s*=\s*True\b|\bAPP_DEBUG\s*=\s*true\b|display_errors\s*[,=]\s*(?:1|On|true))','Debug possiblement exposé','Désactiver les erreurs visibles en production, conserver les logs serveur.'),
('R008','élevé','faible',r'(?:allow_origins\s*=\s*\[\s*[\"\x27]\*[\"\x27]|Access-Control-Allow-Origin\s*[:=]\s*[\"\x27]?\*)','CORS wildcard à vérifier','Restreindre les origines aux besoins réels.'),
('R009','modéré','faible',r'(?:allow_credentials\s*=\s*True|credentials\s*:\s*true)','Credentials CORS : vérifier origines associées','S’assurer de l’allowlist effective d’origines.'),
('R010','élevé','faible',r'(?:password|passwd|api[_-]?key|secret|access[_-]?token)\s*[:=]\s*[\"\x27][^\"\x27]{8,}[\"\x27]','Possible secret codé en dur','Déplacer vers un fournisseur de secrets et renouveler si exposé.'),
('R011','modéré','faible',r'(?:LIBXML_NOENT|resolve_entities\s*=\s*True|load_dtd\s*=\s*True)','Options XML dangereuses possibles','Désactiver DTD et entités externes sur données non fiables.'),
('R012','élevé','faible',r'\b(?:SELECT|INSERT|UPDATE|DELETE)\b.*(?:\$_(?:GET|POST|REQUEST)\b|\+\s*\w+|\{\w+\})','Construction de requête potentiellement dynamique','Vérifier le flux et utiliser des paramètres liés.')]
PATTERNS=[(*r[:3],re.compile(r[3],re.I),*r[4:]) for r in RULES]


def scan(root:Path)->tuple[list[Finding],dict]:
    if not root.is_dir():
        raise ValueError('Le chemin doit être un répertoire local existant.')
    root=root.resolve()
    findings=[]
    stats={'fichiers_examines':0,'fichiers_ignores':0,'limite_atteinte':False}
    package=False; lock=False
    for p in sorted(root.rglob('*')):
        if len(findings)>=LIMIT_FINDINGS or stats['fichiers_examines']>=LIMIT_FILES:
            stats['limite_atteinte']=True;break
        try:
            relative=p.relative_to(root)
            if p.is_symlink() or any(x in EXCLUDED for x in relative.parts[:-1]) or not p.is_file():
                continue
            name=p.name.lower()
            location=relative.as_posix()
            if name in LOCKS: lock=True
            if name=='package.json': package=True
            if name=='.env' or (name.startswith('.env.') and not name.endswith(('.example','.sample','.template'))):
                findings.append(Finding('R013','élevé','faible',location,0,'Fichier environnement : exposition à examiner (jamais lu)','Vérifier exclusion Git, accès serveur et présence de secrets.'))
                stats['fichiers_ignores']+=1
                continue
            if name.endswith(('.bak','.backup','.sql.gz','.old')):
                findings.append(Finding('R014','modéré','faible',location,0,'Sauvegarde locale : exposition à examiner','Protéger stockage et interdire exposition HTTP.'))
                continue
            if p.suffix.lower() not in SUFFIXES and name not in {'.htaccess','dockerfile'}:
                continue
            if p.stat().st_size>LIMIT_SIZE:
                stats['fichiers_ignores']+=1;continue
            content=p.read_text(encoding='utf-8',errors='replace')
            stats['fichiers_examines']+=1
            for line_no,line in enumerate(content.splitlines(),1):
                if len(line)>10000 or line.lstrip().startswith(('#','//','*','<!--')):continue
                for rid,sev,conf,rx,msg,fix in PATTERNS:
                    if rx.search(line):
                        findings.append(Finding(rid,sev,conf,location,line_no,msg,fix))
                        if len(findings)>=LIMIT_FINDINGS:break
                if len(findings)>=LIMIT_FINDINGS:break
        except (OSError,UnicodeError,PermissionError):
            stats['fichiers_ignores']+=1
    if package and not lock and len(findings)<LIMIT_FINDINGS:
        findings.append(Finding('R015','modéré','faible','package.json',0,'Lockfile JS non trouvé dans le périmètre','Vérifier que le workspace utilise un lockfile maintenu.'))
    stats['alertes_heuristiques']=len(findings)
    stats['par_gravite']=dict(Counter(f.severity for f in findings))
    return findings,stats


def markdown(findings:list[Finding],stats:dict,root:Path)->str:
    out=['# Triage statique local — fredskills sécurité','',f"Répertoire : `{root.name}` (nom uniquement).",
        f"Fichiers examinés : {stats['fichiers_examines']} ; ignorés : {stats['fichiers_ignores']} ; alertes : {len(findings)} ; limite : {'oui' if stats['limite_atteinte'] else 'non'}.",'',
        '**Résultats heuristiques, non confirmés. Aucun réseau, DAST ou test de droits réellement exécuté. Pas de secrets ni extraits de code affichés.**','',
        '| Règle | Gravité | Confiance | Fichier:ligne | Observation |','|---|---|---|---|---|']
    for f in findings:
        loc=(f'{f.path}:{f.line}' if f.line else f.path).replace('|','\\|').replace('`',"'")
        out.append(f'| {f.rule} | {f.severity} | {f.confidence} | `{loc}` | {f.message} |')
    out.extend(['','## Recommandations'])
    for f in {x.rule:x for x in findings}.values():out.append(f'- {f.rule} : {f.recommendation}')
    if not findings:out.append('- Aucune alerte de cette liste. Cela **ne démontre pas** l’absence de vulnérabilité.')
    return '\n'.join(out)+'\n'


def main()->int:
    parser=argparse.ArgumentParser(description='Triage local heuristique en lecture seule.')
    parser.add_argument('--root',required=True,type=Path)
    parser.add_argument('--format',choices=('markdown','json'),default='markdown')
    args=parser.parse_args()
    try: findings,stats=scan(args.root)
    except ValueError as err:parser.error(str(err))
    if args.format=='json':print(json.dumps({'type':'heuristique_non_confirmee','stats':stats,'findings':[asdict(f) for f in findings]},ensure_ascii=False,indent=2))
    else:print(markdown(findings,stats,args.root),end='')
    return 0

if __name__=='__main__':
    raise SystemExit(main())
