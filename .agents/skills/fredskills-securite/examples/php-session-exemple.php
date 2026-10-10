<?php
// Exemple minimal pédagogique : ne pas copier aveuglément dans une app existante.
// Exécuter sous HTTPS ; charger ces options avant session_start().
ini_set('session.use_strict_mode', '1');
ini_set('session.use_only_cookies', '1');
session_set_cookie_params([
    'lifetime' => 0,
    'path' => '/',
    'secure' => true,
    'httponly' => true,
    'samesite' => 'Lax',
]);
session_start();
// Après authentification réussie et vérifiée : session_regenerate_id(true);
// Enregistrer côté serveur user_id/tenant_id vérifiés et appliquer un timeout.
// Sur logout : supprimer données et cookie de session, puis session_destroy().
