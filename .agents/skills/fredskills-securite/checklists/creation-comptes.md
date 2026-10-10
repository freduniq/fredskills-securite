# Checklist inscription, login et administration

- [ ] Email/identité normalisé sans confusion de compte.
- [ ] Hachage de mot de passe (Argon2id ou équivalent maintenu) et politique adaptée.
- [ ] Aucune donnée d'authentification sensible dans logs, URL ou réponses.
- [ ] Lutte contre credential stuffing, spraying et énumération.
- [ ] MFA pour admin et autres opérations sensibles selon risque.
- [ ] Jetons de récupération à usage unique, expiration, invalidation.
- [ ] Renouvellement de session après login ; logout révoque session et jetons concernés.
- [ ] Cookies HttpOnly/Secure/SameSite et protections CSRF pertinentes.
- [ ] Admin isolé par vérifications serveur et journalisé.
- [ ] Limites rôles/organisations vérifiées sur chaque objet/API/fichier.
- [ ] Tests de comptes fictifs à deux rôles et deux tenants.
- [ ] Conservation, suppression, export et minimisation des données documentées.
