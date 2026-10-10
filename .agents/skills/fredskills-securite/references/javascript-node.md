# Guide : JavaScript / TypeScript / Node / SPA

- Valider types et limites côté serveur (Zod, Joi ou code existant, sans ajouter dépendance sans nécessité). Aucune règle métier critique seulement dans React/Vue/Angular.
- Utiliser des requêtes SQL paramétrées via le driver/ORM ; éviter les fragments SQL construits depuis un utilisateur.
- Éviter `innerHTML`, `dangerouslySetInnerHTML`, `eval` et construction de code depuis les entrées ; encoder par contexte et sanitizer HTML si vraiment indispensable.
- Auth : cookie de session HttpOnly/Secure/SameSite ou OAuth/OIDC robuste ; garder au serveur vérification de droits ; CSRF pour endpoints à cookies.
- CORS : allowlist précise par environnement, Vary Origin si origine variable ; ne jamais réfléchir toute origine avec autorisations cookies.
- SSRF : n'autoriser que destinations prévues ; refuser private/link-local et redirections vers ces plages avec contrôles DNS/connexion.
- API : limites taille, pagination, profondeur GraphQL, idempotence de paiement, validation des schémas, erreurs sans détails internes.
- Supply chain : lockfiles, versions maintenues, `npm audit` ou outil équivalent s'il existe ; inspection des scripts d'installation, secrets hors bundles front.
- Headers : helmet ou paramétrage équivalent si déjà disponible ; politique CSP compatible avec scripts du projet (tester avant durcissement).
- CI : TypeScript typecheck, tests, SAST, SCA si autorisés et disponibles.
