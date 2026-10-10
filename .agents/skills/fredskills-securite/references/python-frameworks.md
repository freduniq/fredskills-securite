# Guide : Python / Django / Flask / FastAPI

- Django : laisser CSRF middleware actif pour sessions cookies, cookies Secure et HttpOnly, `DEBUG=False` en production, `ALLOWED_HOSTS` exact et contrôles d'autorisation au modèle/vue.
- Flask : secret de session fort en environnement, cookies Secure/HttpOnly/SameSite, CSRF pour formulaires, validation d'identité et autorisations explicitement ajoutées.
- FastAPI : schémas Pydantic, dépendances d'authN/authZ pour chaque route, contrôles propriétaires/tenant dans service/DB ; ne pas confondre OpenAPI public et autorisation.
- SQLAlchemy / Django ORM : utiliser paramètres et constructions ORM ; toute requête SQL brute doit rester paramétrée.
- Sérialisation : ne pas désérialiser `pickle` ou YAML unsafe d'origine non fiable ; employer JSON typé.
- Téléversements : streaming borné, validation extension+signature, stockage privé et autorisation de téléchargement.
- Jobs async : appliquer contexte utilisateur/tenant à l'exécution, éviter tâche « superadmin » cachant un défaut de contrôle.
- Secrets et déploiement : variables d'environnement/gestionnaire secrets, TLS au reverse proxy avec `proxy_headers` sécurisés, journalisation redigée.
