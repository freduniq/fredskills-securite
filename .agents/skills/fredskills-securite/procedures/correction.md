# Procédure de correction sécurisée et non régressive

1. Reproduire de manière non destructive dans un environnement isolé et **autorisé** ; sinon marquer « suspect » ou « à confirmer ».
2. Créer ou relever un test de comportement fonctionnel existant. Noter fichiers et interfaces affectés.
3. Identifier cause racine : frontière de confiance, permission, interpolation, configuration, état métier.
4. Choisir **le plus petit changement** : paramétrisation, validation typée, policy serveur, filtrage tenant, protection CSRF, refus de destination SSRF, etc.
5. Ne pas supprimer de fonctionnalité métier, renommer références produits/clients, changer logique de caisse, modifier migration ou refondre UI sans nécessité justifiée et périmètre approuvé.
6. Ajouter au moins un test négatif contre la vulnérabilité et un test positif préservant le parcours légitime.
7. Vérifier permissions inverse (comptes A/B), rôle standard/admin, organisation A/B si applicable, sessions invalides, erreurs sans divulgation.
8. Lire le diff : pas de secret, pas de debug, pas de dépendance non revue, pas de désactivation de contrôle.
9. Lancer les tests disponibles, signaler chaque échec et les tests non exécutés.
10. Fournir changement fichier:ligne, justification, résultat avant/après et risques résiduels ; ne jamais prétendre une correction validée sans son test.

Si une correction nécessiterait un changement métier incompatible : arrêter cette modification, expliquer le compromis, demander décision pour ce seul changement, continuer les corrections indépendantes.
