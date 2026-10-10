# Procédure de modélisation des menaces

1. Identifier actifs : comptes, secrets, données privées, paiements, fichiers, disponibilité, configurations et identité tenant.
2. Identifier acteurs légitimes : visiteur, utilisateur, support, administrateur d'organisation, superadmin, API, webhook, agent IA.
3. Cartographier flux : navigateur→app→DB ; app→paiement ; app→email ; WebSocket ; uploads ; jobs ; RAG→LLM→outils.
4. Dessiner frontières : internet, réseau privé, session, organisation SaaS, permissions de service, source de documents IA.
5. Lister chaque point d'entrée et donnée non fiable. Classer les risques selon familles 01–13.
6. Donner pour chaque risque : actif, impact, vraisemblance, contrôles existants, test, propriétaire et état.
7. Définir mesures dès conception : RBAC/ABAC, scoping tenant, quotas, validation, secrets, logs, plan de restauration.
8. Revoir le modèle lors d'une nouvelle route, d'un fournisseur, d'un changement d'authentification ou d'un changement de rôles.

Documenter les inconnues sans inventer les composants absents.
