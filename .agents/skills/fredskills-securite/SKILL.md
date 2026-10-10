---
name: fredskills-securite
description: Sécuriser, auditer et corriger des projets web, SaaS, API, ERP, e-commerce ou tableaux de bord pendant la conception, le codage, les modifications et avant déploiement. Vérifier OWASP/ASVS, authentification, sessions, contrôles d’accès, isolation tenant, injections, XSS, CSRF, SSRF, secrets, dépendances et configurations ; produire preuves et tests sans casser le métier.
---

# fredskills sécurité — Skill de cybersécurité pour Codex

## Déclenchement et mission

Activer pour création/modification de sites web, SaaS, ERP/CRM, e-commerce, API et applications avec comptes ; demandes explicites d'audit, hardening, sécurité, vulnérabilités, revue, correctifs ou déploiement. **Ne pas déclencher** pour une tâche purement rédactionnelle sans code ni sécurité. Le Skill conseille et applique des contrôles adaptés ; il n'est pas un dispositif de surveillance permanent et n'exécute rien sans accès au projet.

## Ordre de travail impératif

1. **Périmètre et autorisation.** N'examiner que le code fourni/autorisé. Ne pas scanner de cible internet ou de production sans autorisation écrite et règles de test. Faire une sauvegarde/commit avant tout correctif destructif. Ne jamais exfiltrer de données.
2. **Inventaire.** Identifier stack (PHP/MySQL, Node, Python, Java, .NET…), framework, version, déploiement, dépendances et entrées (formulaires, endpoints, fichiers, jobs, SSO, paiements, webhooks, IA). Déterminer surfaces, utilisateurs et frontières de confiance. Lire `procedures/modele-de-menaces.md`.
3. **Choix de références.** Lire `references/00-index.md`, puis **uniquement** les fichiers 01 à 13 correspondant aux composants inspectés. Lire obligatoirement `references/14-priorites-et-controles.md` et, selon stack, `references/php-mysql.md`, `references/javascript-node.md`, `references/python-frameworks.md`, `references/cloud-deploiement.md`.
4. **Audit ciblé.** Utiliser `procedures/audit.md` ; lire code et config réels, comparer politique d'accès et flux métier ; utiliser outils disponibles de manière **non destructive**. `python3 scripts/security_audit.py --root <répertoire> --format markdown` donne des **indices heuristiques**, pas des vulnérabilités confirmées. Ne pas extrapoler la couverture à 210 attaques.
5. **Prioriser.** Évaluer vraisemblance, exposition et impact sur confidentialité, intégrité et disponibilité. Pour chaque finding : preuve chemin:ligne (sans secret), précondition, scénario non offensif, risque, correction minimale, vérification ; sinon indiquer « à confirmer ».
6. **Corriger au strict nécessaire.** Suivre `procedures/correction.md`. Préserver rôles, recherches par référence, schémas, workflow, structure et UI existants sauf justification validée. Poser vérification serveur, paramétrisation, CSP/CSRF, cookies, protections de paiement, scoping tenant, etc. selon besoin ; ne jamais désactiver une protection pour faire passer un test.
7. **Vérifier.** Exécuter si possible tests unitaires, d'intégration, de permissions inter-comptes, de régression et analyses de dépendances. Commencer par les scénarios négatifs sûrs ; n'utiliser tests actifs que sur environnement de test autorisé. Consulter `checklists/avant-production.md`.
8. **Rapporter.** Produire `Rapport de sécurité` au format `assets/modele-rapport.md` : périmètre, tech, méthode, constats classés, preuve, fichier/ligne, changements, commandes/tests réellement lancés, résultats, tests non exécutés, risques résiduels, prochaines actions. Statuts stricts : **confirmé / suspect / non vérifié / corrigé et testé / corrigé non testé / non applicable**. Pas de « 100 % sécurisé ».

## Modes d'utilisation

- **CREATE** : sécurité dès conception, contrôles des comptes et données avant implémentation, matrice de rôles, modèles d'entrée, tests prévus.
- **CHANGE** : relever comportement actuel, faire diff ciblé, évaluer risques supplémentaires, modifier minimum, tests de non-régression.
- **AUDIT** : mode lecture seule par défaut, preuves classées, aucun correctif sans instruction de modifier.
- **FIX** : proposer correction minimale, implémenter dans périmètre demandé, ajouter tests et reporter les limites.
- **RELEASE** : config HTTPS, secrets, journaux, sauvegardes, CI, exploitation ; vérifier la checklist de sortie.

## Invariants (non négociables)

- Ne pas exposer secrets, données personnelles ou mots de passe en réponse/log/test ; utiliser des valeurs fictives.
- Ne pas faire confiance à une donnée utilisateur, client, webhook, API tierce ou document RAG.
- Vérifier **côté serveur** authN, authZ pour tout objet/fonction/champ, tenant, tarifs, paiements et transitions.
- Par défaut refuser les opérations non autorisées ; jamais valider un droit uniquement par masquer un bouton.
- Préférer paramètres SQL, APIs sûres, encodage par contexte, CSRF pour sessions cookies, politique CORS stricte, contrôle SSRF, sessions robustes, Argon2id ou équivalent selon stack.
- Ne pas installer de dépendances sans justification, analyse de provenance et approbation si requis.
- Ne pas confondre échec du scanner, silence d'un outil ou absence de test avec preuve de sûreté.
- Ne pas ajouter de fonctionnalité, réécrire le site, déplacer des fichiers ou modifier une règle métier sans nécessité justifiée.
- Ne pas utiliser de payloads destructifs, exfiltration, tests de charge agressifs ni d'attaque sur tiers.

## Matrice de ressources

| Situation | Ouvrir en priorité |
|---|---|
| Liste intégrale 210 cas | `references/00-index.md`, puis 01–13 |
| Comptes, sessions et rôles | `references/comptes-sessions.md`, 03, 04, 09 |
| API, intégrations, IA | 05, 07, 09, 13 |
| Correctifs PHP/MySQL | `references/php-mysql.md`, 01, 02, 03, 04, 06 |
| JS/TypeScript/Node | `references/javascript-node.md`, 01, 02, 03, 05 |
| Python web | `references/python-frameworks.md`, 01, 03, 04 |
| Infrastructure / production | `references/cloud-deploiement.md`, 06, 07, 08, 11 |
| Pré-déploiement et politique de tests | `checklists/avant-production.md`, `procedures/audit.md` |
| Cartographie réglementaire / référentiels | `references/16-referentiels.md` |

## Sortie minimale pour toute tâche sécurité

Mentionner toujours les protections **observées dans le code**, les risques **prouvés**, les points **non vérifiés**, les fichiers changés et les tests réellement exécutés. Si le code n'est pas accessible : fournir un plan/checklist, sans prétendre avoir audité l'application.
