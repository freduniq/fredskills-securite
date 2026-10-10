# 15 — Outils et stratégie d'audit

Cette section reprend les outils de la liste initiale ; aucun n'est intégré ou exécuté automatiquement par le Skill.

| Outil | Type | Limite / précaution |
|---|---|---|
| OWASP ZAP | DAST HTTP | Actif uniquement avec autorisation, privilégier pré-production |
| Burp Suite | Proxy et DAST | L'utilisateur doit disposer des droits et consentements nécessaires |
| Semgrep | SAST | Règles et faux positifs à examiner |
| SonarQube | SAST/qualité | Couverture dépendant des langages et règles |
| Trivy | SCA/images/config | Dépend des bases de vulnérabilités et mises à jour |
| Gitleaks | Détection de secrets | Signaler l'emplacement sans afficher une valeur sensible |
| OWASP Dependency-Check | SCA | Corrélation paquet/CVE nécessite validation manuelle |
| Nuclei | Templates de vérification | Éviter les templates intrusifs ; exécuter uniquement sur cible autorisée |

## Ordre prudent

1. **Code local** : inventaire, grep ciblé, SAST, revue manuelle, comparaison avec la matrice d'accès.
2. **Dépendances** : lire lockfiles, SCA si installé, avis éditeurs et validation des versions ; ne jamais prétendre qu'une CVE a été vérifiée sans sources à jour.
3. **Tests applicatifs locaux** : unitaires, intégration avec comptes factices, autorisations, paiement en sandbox, session et fichiers.
4. **Pré-production dédiée** : DAST autorisé et limité en vitesse, sans vraies données.
5. **Rapport** : preuves, versions, périmètre, faux positifs, risques résiduels et tests non réalisés.

Le scanner livré dans `scripts/security_audit.py` est un **assistant de triage local heuristique**, pas un SAST commercial et encore moins un pentest. Il ne remplace aucune vérification d'autorisation métier.
