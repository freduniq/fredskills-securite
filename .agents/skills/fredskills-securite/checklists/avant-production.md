# Checklist préproduction (à cocher seulement avec preuve)

- [ ] Périmètre, propriétaire et modèle de menace actualisés.
- [ ] Tests authN/MFA/récupération et rotation de sessions.
- [ ] Matrice de rôles avec refus côté serveur testée.
- [ ] Tests IDOR/BOLA et inter-tenant sur lecture, écriture, recherche, fichiers et exports.
- [ ] Requêtes SQL/NoSQL paramétrées ; aucun interpréteur dangereux exposé.
- [ ] Sorties HTML/JS encodées, traitement HTML riche sécurisé, protections CSRF pertinentes.
- [ ] SSRF, CORS, webhooks, OAuth/OIDC et API audités selon fonctionnalités présentes.
- [ ] Chargement fichiers privé, borné, avec refus des types exécutables.
- [ ] Logique paiements/prix/coupons/stocks vérifiée côté serveur ; idempotence et concurrence.
- [ ] Dépendances/lockfiles analysés avec sources à jour.
- [ ] Secrets absents du dépôt, des bundles, logs et réponses ; rotation prévue.
- [ ] HTTPS/TLS, cookies, CSP et configs d'erreurs vérifiés en staging.
- [ ] Rate limits et plans de dégradation en place selon exposition.
- [ ] Sauvegarde, restauration et rollback testés.
- [ ] Logs sensibles et alertes de sécurité vérifiés (sans fuite de secrets).
- [ ] Tests unitaires/integration/régression passés ; éléments non testés signalés.
- [ ] Rapport final avec preuves, statut par finding et risques résiduels.
