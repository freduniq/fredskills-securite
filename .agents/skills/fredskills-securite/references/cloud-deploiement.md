# Cloud, hébergement mutualisé, VPS et déploiement

- Documenter hébergeur, hostname, reverse proxy, CDN/WAF, TLS, DNS, ports, sauvegardes, sources de secrets et responsabilités.
- Déployer sur HTTPS avec redirection et certificat valide ; HSTS seulement après vérification de tout le périmètre ; désactiver TRACE, listings et diagnostics publics.
- VPS : utilisateur sans privilège excessif, SSH par clé, mises à jour, firewall et protections anti-brute-force ; minimiser les ports.
- Hébergement PHP : document root séparé du code métier si possible, protéger fichiers `.env`, `.git`, `.sql`, `.bak`, config et logs ; interdire exécution dans stockage uploads.
- Conteneurs : images minimales, utilisateur non-root, filesystem read-only si compatible, secrets non embarqués dans images, socket Docker non exposé.
- Cloud : buckets privés par défaut, rôles IAM minimaux, métadonnées non accessibles aux fonctions SSRF, surveillance des journaux administratifs.
- CI/CD : permissions minimales des tokens, validations PR, lockfiles, scans de dépendances, provenance des artefacts et séparation staging/production.
- Sauvegardes : chiffrement, copies hors site et **test de restauration** ; politique de rétention conforme aux exigences.
- Journalisation : pas de mots de passe, tokens, cookies ou données bancaires brutes ; alertes opérationnelles sur abus et erreurs.
- DDoS : limites applicatives et protection réseau/CDN selon disponibilité et budget ; pas de garantie d'absorption totale.
- Déploiement : contrôler migrations avant prod, possibilité de rollback, état des secrets et monitoring post-deploy.
