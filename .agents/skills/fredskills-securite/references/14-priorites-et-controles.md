# 14 — Contrôles prioritaires et critères de preuve

Ce chapitre correspond à la section 14 de la liste initiale : il ne décrit pas de nouvelles attaques. L'adapter à l'exposition et à la criticité réelles.

| Contrôle | Exigence concrète | Preuve vérifiable |
|---|---|---|
| Injections SQL/NoSQL | Paramètres liés, filtres typés, permissions minimales | Revue des accès DB + tests de valeurs atypiques |
| XSS | Encodage en fonction du contexte ; HTML riche sanitisé ; CSP complémentaire | Tests de rendu, DOM, CSP navigateur |
| CSRF | Requêtes modifiant l'état protégées (tokens, Origin/Referer selon modèle, SameSite en défense complémentaire) | Requête sans jeton rejetée dans cas applicable |
| SSRF | Destinations autorisées, blocage des IP privées/link-local, vérification après résolutions et redirections | Essais locaux de destinations interdites, aucune requête réseau effectuée |
| IDOR/BOLA | Contrôle objet pour lecture/écriture/suppression/export | Matrice compte A / compte B / tenant A / tenant B |
| Authentification | Hachage adapté, MFA selon menace, rate limiting et récupération forte | Codes expirés/refusés, récupération non rejouable |
| Sessions | Cookie Secure/HttpOnly/SameSite, renouvellement login et révocation serveur | Ancien cookie inutilisable après logout/changement de sécurité |
| Rôles/permissions | Vérification serveur deny-by-default par fonction | Admin-only inaccessible à utilisateur standard |
| Isolation SaaS | tenant_id issu du contexte vérifié, filtres au niveau DB et objets | Test croisé sur 2 tenants / fichiers / cache / exports |
| Uploads | Type+taille, noms aléatoires, stockage privé non exécutable, antivirus selon risques | Exécutable de test non servi/exécuté |
| API | Autorisation champ/objet, validation schéma, limitation et inventaire | Requêtes invalides 4xx et quotas vérifiés |
| Dépendances | SBOM, lockfile, versions corrigées, vérification de provenance | Rapport SCA daté + corrections suivies |
| Config serveur | HTTPS, CSP/HSTS appropriés, CORS stricte, erreurs non bavardes | Valeurs de config et réponses réelles en pré-production |
| Secret management | Secrets hors dépôt et hors logs ; rotation/révocation | Inventaire secrets (identifiants masqués) et tests de révocation |
| Logs / sauvegardes | Audit événements critiques, alertes et restauration testée | Test de restauration daté et alerte démontrée |
| Disponibilité | Limites CPU/requêtes/timeout/quotas, WAF/CDN si exposition | Charge contrôlée et métriques d'effet |

## Priorisation

- **P0** : exfiltration inter-tenant, compromission d'administration, RCE, fuite de secrets actifs, paiement non authentifié : isoler/mitiger immédiatement et gérer l'incident.
- **P1** : injection confirmée, XSS persistant à impact fort, autorisation manquante sur données sensibles, vulnérabilité critique exploitable dans dépendance.
- **P2** : durcissement utile et risque contextualisé modéré.
- **P3** : amélioration mineure, dette de maintenance ou observation non prouvée.

Le niveau final dépend de l'exposition, des données, de l'exploitabilité et des protections déjà en place. Ne pas confondre les classes ci-dessus avec un score CVSS officiel.
