# fredskills sécurité — v1.0.0

Skill réutilisable pour Codex, dédié à l'audit, à la prévention et à la correction défensive des projets web.

## Installation

1. Extraire le ZIP ; il contient le dossier `fredskills-securite` avec son fichier `SKILL.md`.
2. Pour tous les projets : copier **le dossier entier** sous `$HOME/.agents/skills/fredskills-securite` (Windows PowerShell : `$HOME\.agents\skills\fredskills-securite`).
3. Pour un dépôt uniquement : copier sous `MON_PROJET/.agents/skills/fredskills-securite`.
4. Ouvrir Codex dans le projet, vérifier la présence via `/skills`, puis utiliser `$fredskills-securite` si souhaité ; Codex peut aussi l'activer lorsque la description correspond. Redémarrer si la découverte ne se met pas à jour.
5. Pour une application systématique dans un dépôt, **adapter** le texte de `examples/AGENTS-snippet.md` à l’`AGENTS.md` existant ; cela ne remplace pas les tests CI et ne garantit pas l'invocation à chaque tour.

Exemple : `Avec $fredskills-securite, audite seulement l'inscription, la connexion, le rôle admin et l'isolation tenant. Lecture seule. Fournis preuves et tests proposés.`

## Vérification locale sans réseau ni dépendance

Depuis le dossier du skill :

```bash
python3 scripts/validate_skill.py
python3 -m unittest discover -s tests -v
python3 scripts/security_audit.py --root /chemin/vers/mon-projet --format markdown
```

Le scanner fourni **ne réalise que des recherches statiques heuristiques** dans les fichiers locaux ; il n'analyse pas toutes les vulnérabilités, ne scanne aucun domaine distant, ne lit pas la base de données et ne doit pas être interprété comme certification de sécurité.

Les 16 chapitres correspondent exactement aux 13 familles d’attaques (210 cas) et aux trois sections transversales (priorités, outillage, référentiels) du catalogue initial.

## Références

OWASP Top 10 2025 : https://top10.owasp.org/2025/
OWASP ASVS 5.0.0 : https://github.com/OWASP/ASVS
OWASP API Security Top 10 2023 : https://api-security.owasp.org/editions/2023/en/0x11-t10/
MITRE CWE : https://cwe.mitre.org/
OpenAI Skills : https://learn.chatgpt.com/docs/build-skills

**Limites :** ne remplace pas un audit indépendant, un pentest contractuellement autorisé ni un programme de maintien en condition de sécurité.
