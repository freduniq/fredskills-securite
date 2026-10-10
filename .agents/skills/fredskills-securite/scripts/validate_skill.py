#!/usr/bin/env python3
"""Validateur autonome du paquet de skill, sans réseau."""
from pathlib import Path
import json
import re
ROOT=Path(__file__).resolve().parents[1]

def validate()->list[str]:
    errors=[]
    text=(ROOT/'SKILL.md').read_text(encoding='utf-8')
    if not re.match(r'\A---\nname: fredskills-securite\ndescription: .+?\n---\n',text):
        errors.append('Frontmatter invalide')
    data=json.loads((ROOT/'references/catalogue.json').read_text(encoding='utf-8'))
    groups=data['groups']
    numbers=[i['id'] for g in groups for i in g['items']]
    if len(groups)!=13 or numbers!=list(range(1,211)) or data['count']!=210:
        errors.append('Catalogue 13 groupes / 210 cas non conforme')
    for group in groups:
        path=ROOT/group['path']
        if not path.is_file():errors.append('Fichier absent : '+str(path));continue
        text=path.read_text(encoding='utf-8')
        for item in group['items']:
            if not re.search(rf'^## {item["id"]:03d} — ',text,re.M):
                errors.append('Fiche manquante : '+str(item['id']))
    for i in range(14,17):
        if not list((ROOT/'references').glob(f'{i:02d}-*.md')):errors.append(f'Chapitre {i} absent')
    for p in ('procedures/audit.md','procedures/correction.md','procedures/modele-de-menaces.md','checklists/avant-production.md','assets/modele-rapport.md','agents/openai.yaml','scripts/security_audit.py','README.md'):
        if not (ROOT/p).is_file():errors.append('Ressource absente : '+p)
    return errors

if __name__=='__main__':
    errors=validate()
    for e in errors:print('ERREUR : '+e)
    if errors:raise SystemExit(1)
    print('OK : SKILL.md, 13 familles, 210 fiches, 3 chapitres transversaux et ressources.')
