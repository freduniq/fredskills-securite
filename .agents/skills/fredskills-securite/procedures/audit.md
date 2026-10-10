# Audit structuré — lecture seule par défaut

## Avant l'audit

- Définir systèmes explicitement autorisés, branches, fichiers, données de test, horaires et tests permis. Jamais de scan non autorisé sur IP/domaines.
- Recenser langage, routes, services, dépendances, schémas, migrations, configuration, bibliothèques et tests.
- Lire `references/00-index.md` et les modules pertinents. Prioriser comptes, SQL, accès tenant, paiement et fichiers.

## Revue statique et dynamique limitée

1. Examiner les entrées non fiables jusqu'à leur usage dans SQL, shell, HTML, templates et URL distantes.
2. Inspecter authN, session, récupération et restrictions admin ; relever preuves dans le code.
3. Comparer matrice rôle/objet/organisation pour toutes les opérations CRUD et exports.
4. Examiner uploads, webhooks, CORS, CSRF, CSP, cookies et logs de données sensibles.
5. Examiner lockfiles, dépendances, CI/CD, config, environnement et exposition des sauvegardes.
6. Utiliser si pertinent et installé `python3 scripts/security_audit.py --root . --format markdown`; les alertes sont **suspicions**, jamais des failles prouvées automatiquement.
7. Tests sur environnement autorisé : comptes fictifs, ressources réversibles et limites de charge ; aucun test destructif ni déni de service.
8. Classer : confirmé, suspect, non vérifié, non applicable. Ne jamais déduire la sécurité du silence des outils.

## Fiche finding obligatoire

`ID | titre | gravité contextualisée | confiance | preuve chemin:ligne | chemin exploitable sous hypothèses | composant | impact | correction minimale | test/résultat | état`.

Masquer les secrets à l'affichage et dans les rapports. Remettre un rapport même si des outils n'ont pas pu être lancés, en précisant ce qui manque.
