# Texte facultatif à intégrer MANUELLEMENT dans l'AGENTS.md d'un projet

Pour chaque création/modification de route, formulaire, système de session, autorisation, API, fichier, paiement, intégration ou configuration de déploiement, appliquer le Skill `$fredskills-securite` s'il est disponible. Préserver toutes les règles métier et les protections existantes ; vérifier les autorisations côté serveur et les effets inter-tenant ; ajouter tests positifs et négatifs ; signaler les contrôles non vérifiés. En audit seul, rester en lecture seule. Ne jamais afficher secrets, clés ou tokens dans les résultats.

Ce texte est une instruction de dépôt : elle favorise la cohérence, mais **ne garantit pas techniquement** qu'un skill se déclenche systématiquement. Vérifier via CI et revue humaine.
