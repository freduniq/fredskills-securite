# Guide d'implémentation : PHP 8+ / MySQL (adapter au contexte)

- Base de données : PDO avec DSN utf8mb4, `PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION`, `PDO::ATTR_EMULATE_PREPARES => false` selon pilote, `prepare` + paramètres liés. Les noms de tables/colonnes dynamiques demandent une allowlist, jamais un placeholder SQL.
- Sortie HTML : `htmlspecialchars($value, ENT_QUOTES | ENT_SUBSTITUTE, 'UTF-8')` dans les textes/attributs HTML. JavaScript, URL et CSS ont des contextes distincts : ne pas réutiliser aveuglément la fonction HTML.
- CSRF : token cryptographiquement sûr stocké côté session, vérifié avec `hash_equals` sur POST/PATCH/DELETE pour sessions cookies ; traiter la rotation et durée de vie selon parcours.
- Sessions : `session.use_strict_mode=1`, `session.use_only_cookies=1`, cookies sécurisés sous HTTPS, renouveler ID avec `session_regenerate_id(true)` après authentification, expiration logique serveur.
- Mots de passe : `password_hash($password, PASSWORD_ARGON2ID)` si compilé et disponible ; `password_verify` ; migration automatique avec `password_needs_rehash`.
- Upload : valider taille/type réel (finfo), stockage hors docroot, identifiant unique, permissions minimales, vérification de propriété au téléchargement, ne pas accepter un chemin arbitraire du client.
- Erreurs : `display_errors=0` en production, log côté serveur hors webroot sans secrets ni traces sensibles.
- Configuration : credentials par environnement/gestionnaire de secrets, pas de `config.php` public contenant des secrets, `.env` non servi. Ne jamais utiliser l'URL de phpMyAdmin comme hôte MySQL : utiliser le **nom d'hôte DB** fourni par l'hébergeur.
- Contrôle d'accès : toujours au backend, même si l'UI masque menu ou bouton ; vérifier roles/tenant à chaque action.

## Exemples

Lire `examples/php-pdo-exemple.php` et `examples/php-session-exemple.php`. Ce sont des patrons pédagogiques et non un module copié automatiquement : adapter et tester après examen de la structure existante.
