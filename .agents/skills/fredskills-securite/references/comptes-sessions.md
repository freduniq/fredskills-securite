# Comptes utilisateurs, sessions, autorisations et données personnelles

## Conception

- Distinguer identification, authentification, autorisation, consentement et journal d'audit.
- Mots de passe : Argon2id (si disponible), ou algorithme éprouvé du framework avec coût actuel adapté ; ne jamais utiliser MD5/SHA-1 ou chiffrement réversible pour les mots de passe. Pas de mot de passe dans mail ou log.
- Inscription : champs autorisés, normalisation cohérente d'email, prévention d'énumération, confirmation d'adresse lorsque adaptée ; ne jamais accepter rôle/tenant privilégié directement depuis le client.
- Authentification : limite de tentatives par compte et source, MFA surtout pour admins, messages non révélateurs, surveiller appareils et événements anormaux.
- Récupération : jeton cryptographiquement aléatoire (enregistrer un condensat), lié au compte, usage unique, expiration courte, URL à domaine fixé, pas de jeton dans logs ; révocation des anciennes sessions selon politique.
- Cookies : HTTPS, `Secure`, `HttpOnly`, `SameSite=Lax/Strict` selon parcours ; `SameSite` ne remplace pas une protection CSRF quand requise. Éviter localStorage pour jetons persistants lorsque risques XSS élevés ; tenir compte de l'architecture.
- Sessions : nouvel identifiant après connexion/élévation, idle timeout et durée maximale selon risque, logout côté serveur, renouvellement des sessions sensibles.
- CSRF : tokens synchronisés ou double-submit signé selon architecture, contrôle Origin/Referer comme défense complémentaire ; vérifier requêtes GET sans effet secondaire.
- RBAC/ABAC : deny-by-default dans services/routes, matrice par opération et propriété, contrôles aussi sur listes et exports ; tests d'accès croisés.
- SaaS : tenant_id dérivé d'un contexte validé, scoping sur DB, fichiers, recherches, cache, tâches et webhooks ; requêtes avec index et contraintes tenant quand pertinent.
- Admin : MFA renforcé, journal d'actions, confirmation des opérations destructives, sessions plus courtes, séparation des comptes de service.
- Données : minimisation, chiffrement au repos si menace l'exige, TLS, politiques de conservation, suppression et sauvegardes chiffrées.
- Audit logs : qui/quand/quoi/résultat/corrélation sans secrets ; protection contre altération et contrôles d'accès.

## Matrice de tests négatifs recommandée

| Scénario | Attendu |
|---|---|
| Utilisateur A lit un dossier de B | 403/404 ; aucune donnée de B |
| Admin d'organisation A ouvre la facture B | 403/404 ; pas de traversée de tenant |
| Utilisateur normal soumet `role=admin` | Champ rejeté ou ignoré, rôle inchangé |
| Token de reset expiré/réutilisé | Refus, aucun changement de mot de passe |
| Ancienne session après déconnexion | Refus serveur |
| Requête mutation sans protection CSRF | Refus si auth par cookie et protection applicable |
| Ressource privée appelée par API/export/WebSocket | Autorisation identique aux pages web |

## Vérifications manuelles à faire dans le vrai projet

Lister routes, policies, tables users/organizations/memberships, composants frontend, cookies, formulaires de récupération, jobs asynchrones et chemins de téléchargement. Un contrôle visuel du menu **ne vaut jamais preuve d'autorisation**.
