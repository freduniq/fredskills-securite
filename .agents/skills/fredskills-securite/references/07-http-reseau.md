# 07 — HTTP et réseau

**Couverture :** 17 types d’attaque numérotés 106 à 122. Cet inventaire identifie des familles, variantes et scénarios ; certains termes se recoupent.

**Utilisation :** lire les profils liés à la surface attaquée. Les risques sont indicatifs et se recalculent selon exposition, impact, contrôle existant et vraisemblance. Ne pas effectuer de tests actifs sur des systèmes non autorisés.

## 106 — HTTP Request Smuggling

1. **Description / fonctionnement :** Exploite des interprétations contradictoires d'une requête par des intermédiaires.
2. **Causes techniques :** Normalisation différente entre proxy, cache et application ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** CDN, DNS, TLS, reverse proxy, CORS, routes HTTP et appels réseau serveur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Comparer les couches proxy/app, inspecter en-têtes, tls, dns et règles cors. Rechercher spécialement : normalisation différente entre proxy, cache et application.
5. **Prévention :** Normalisation cohérente, allowlist d’origines et de destinations, TLS correct, validation réseau. **Point spécifique :** Aligner interprétation du protocole, cache keys, méthodes et en-têtes ; désactiver ambiguïtés.
6. **Correction sécurisée :** Configurer explicitement proxy et application ; rejeter les en-têtes ambigus et destinations interdites. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Des en-têtes ambigus ou doublés sont rejetés de manière cohérente. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Surveiller configuration DNS/TLS/proxy et la maintenir versionnée. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 107 — HTTP Response Splitting

1. **Description / fonctionnement :** Découpe frauduleusement une réponse HTTP.
2. **Causes techniques :** En-têtes composés depuis une entrée non normalisée ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** CDN, DNS, TLS, reverse proxy, CORS, routes HTTP et appels réseau serveur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Comparer les couches proxy/app, inspecter en-têtes, tls, dns et règles cors. Rechercher spécialement : en-têtes composés depuis une entrée non normalisée.
5. **Prévention :** Normalisation cohérente, allowlist d’origines et de destinations, TLS correct, validation réseau. **Point spécifique :** Interdire CR/LF dans les champs d’en-tête, valider les noms d’hôtes et normaliser.
6. **Correction sécurisée :** Configurer explicitement proxy et application ; rejeter les en-têtes ambigus et destinations interdites. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une donnée contenant des retours à la ligne ne crée pas de nouvel en-tête. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Surveiller configuration DNS/TLS/proxy et la maintenir versionnée. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 108 — HTTP Host Header Attack

1. **Description / fonctionnement :** Contrôle des URL ou décisions fondées sur l'en-tête Host.
2. **Causes techniques :** En-têtes composés depuis une entrée non normalisée ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** CDN, DNS, TLS, reverse proxy, CORS, routes HTTP et appels réseau serveur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Comparer les couches proxy/app, inspecter en-têtes, tls, dns et règles cors. Rechercher spécialement : en-têtes composés depuis une entrée non normalisée.
5. **Prévention :** Normalisation cohérente, allowlist d’origines et de destinations, TLS correct, validation réseau. **Point spécifique :** Interdire CR/LF dans les champs d’en-tête, valider les noms d’hôtes et normaliser.
6. **Correction sécurisée :** Configurer explicitement proxy et application ; rejeter les en-têtes ambigus et destinations interdites. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une donnée contenant des retours à la ligne ne crée pas de nouvel en-tête. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Surveiller configuration DNS/TLS/proxy et la maintenir versionnée. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 109 — HTTP Parameter Pollution

1. **Description / fonctionnement :** Exploite la coexistence ambiguë de paramètres portant le même nom.
2. **Causes techniques :** Normalisation différente entre proxy, cache et application ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** CDN, DNS, TLS, reverse proxy, CORS, routes HTTP et appels réseau serveur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Comparer les couches proxy/app, inspecter en-têtes, tls, dns et règles cors. Rechercher spécialement : normalisation différente entre proxy, cache et application.
5. **Prévention :** Normalisation cohérente, allowlist d’origines et de destinations, TLS correct, validation réseau. **Point spécifique :** Aligner interprétation du protocole, cache keys, méthodes et en-têtes ; désactiver ambiguïtés.
6. **Correction sécurisée :** Configurer explicitement proxy et application ; rejeter les en-têtes ambigus et destinations interdites. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Des en-têtes ambigus ou doublés sont rejetés de manière cohérente. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Surveiller configuration DNS/TLS/proxy et la maintenir versionnée. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 110 — Web Cache Poisoning

1. **Description / fonctionnement :** Empoisonne le cache avec une réponse influencée par une entrée non représentée dans la clé.
2. **Causes techniques :** Normalisation différente entre proxy, cache et application ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** CDN, DNS, TLS, reverse proxy, CORS, routes HTTP et appels réseau serveur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Comparer les couches proxy/app, inspecter en-têtes, tls, dns et règles cors. Rechercher spécialement : normalisation différente entre proxy, cache et application.
5. **Prévention :** Normalisation cohérente, allowlist d’origines et de destinations, TLS correct, validation réseau. **Point spécifique :** Aligner interprétation du protocole, cache keys, méthodes et en-têtes ; désactiver ambiguïtés.
6. **Correction sécurisée :** Configurer explicitement proxy et application ; rejeter les en-têtes ambigus et destinations interdites. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Des en-têtes ambigus ou doublés sont rejetés de manière cohérente. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Surveiller configuration DNS/TLS/proxy et la maintenir versionnée. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 111 — Web Cache Deception

1. **Description / fonctionnement :** Amène le cache à stocker une ressource privée sous une URL trompeuse.
2. **Causes techniques :** Normalisation différente entre proxy, cache et application ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** CDN, DNS, TLS, reverse proxy, CORS, routes HTTP et appels réseau serveur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Comparer les couches proxy/app, inspecter en-têtes, tls, dns et règles cors. Rechercher spécialement : normalisation différente entre proxy, cache et application.
5. **Prévention :** Normalisation cohérente, allowlist d’origines et de destinations, TLS correct, validation réseau. **Point spécifique :** Aligner interprétation du protocole, cache keys, méthodes et en-têtes ; désactiver ambiguïtés.
6. **Correction sécurisée :** Configurer explicitement proxy et application ; rejeter les en-têtes ambigus et destinations interdites. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Des en-têtes ambigus ou doublés sont rejetés de manière cohérente. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Surveiller configuration DNS/TLS/proxy et la maintenir versionnée. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 112 — DNS Spoofing

1. **Description / fonctionnement :** Fournit de fausses réponses DNS.
2. **Causes techniques :** contradiction d’interprétation entre composants ou confiance excessive dans les en-têtes/réseaux ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** CDN, DNS, TLS, reverse proxy, CORS, routes HTTP et appels réseau serveur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Comparer les couches proxy/app, inspecter en-têtes, tls, dns et règles cors. Rechercher spécialement : contradiction d’interprétation entre composants ou confiance excessive dans les en-têtes/réseaux.
5. **Prévention :** Normalisation cohérente, allowlist d’origines et de destinations, TLS correct, validation réseau. **Point spécifique :** configurer explicitement proxy et application ; rejeter les en-têtes ambigus et destinations interdites
6. **Correction sécurisée :** Configurer explicitement proxy et application ; rejeter les en-têtes ambigus et destinations interdites. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** tester avec environnements autorisés les origines inattendues, duplications d’en-têtes et chemins de proxy Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Surveiller configuration DNS/TLS/proxy et la maintenir versionnée. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 113 — DNS Cache Poisoning

1. **Description / fonctionnement :** Contamine une résolution DNS mise en cache.
2. **Causes techniques :** Normalisation différente entre proxy, cache et application ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** CDN, DNS, TLS, reverse proxy, CORS, routes HTTP et appels réseau serveur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Comparer les couches proxy/app, inspecter en-têtes, tls, dns et règles cors. Rechercher spécialement : normalisation différente entre proxy, cache et application.
5. **Prévention :** Normalisation cohérente, allowlist d’origines et de destinations, TLS correct, validation réseau. **Point spécifique :** Aligner interprétation du protocole, cache keys, méthodes et en-têtes ; désactiver ambiguïtés.
6. **Correction sécurisée :** Configurer explicitement proxy et application ; rejeter les en-têtes ambigus et destinations interdites. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Des en-têtes ambigus ou doublés sont rejetés de manière cohérente. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Surveiller configuration DNS/TLS/proxy et la maintenir versionnée. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 114 — DNS Hijacking

1. **Description / fonctionnement :** Détourne la configuration ou délégation DNS.
2. **Causes techniques :** contradiction d’interprétation entre composants ou confiance excessive dans les en-têtes/réseaux ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** CDN, DNS, TLS, reverse proxy, CORS, routes HTTP et appels réseau serveur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Comparer les couches proxy/app, inspecter en-têtes, tls, dns et règles cors. Rechercher spécialement : contradiction d’interprétation entre composants ou confiance excessive dans les en-têtes/réseaux.
5. **Prévention :** Normalisation cohérente, allowlist d’origines et de destinations, TLS correct, validation réseau. **Point spécifique :** configurer explicitement proxy et application ; rejeter les en-têtes ambigus et destinations interdites
6. **Correction sécurisée :** Configurer explicitement proxy et application ; rejeter les en-têtes ambigus et destinations interdites. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** tester avec environnements autorisés les origines inattendues, duplications d’en-têtes et chemins de proxy Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Surveiller configuration DNS/TLS/proxy et la maintenir versionnée. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 115 — Man-in-the-Middle (MITM)

1. **Description / fonctionnement :** Intercepte ou modifie une communication.
2. **Causes techniques :** contradiction d’interprétation entre composants ou confiance excessive dans les en-têtes/réseaux ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** CDN, DNS, TLS, reverse proxy, CORS, routes HTTP et appels réseau serveur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Comparer les couches proxy/app, inspecter en-têtes, tls, dns et règles cors. Rechercher spécialement : contradiction d’interprétation entre composants ou confiance excessive dans les en-têtes/réseaux.
5. **Prévention :** Normalisation cohérente, allowlist d’origines et de destinations, TLS correct, validation réseau. **Point spécifique :** configurer explicitement proxy et application ; rejeter les en-têtes ambigus et destinations interdites
6. **Correction sécurisée :** Configurer explicitement proxy et application ; rejeter les en-têtes ambigus et destinations interdites. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** tester avec environnements autorisés les origines inattendues, duplications d’en-têtes et chemins de proxy Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Surveiller configuration DNS/TLS/proxy et la maintenir versionnée. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 116 — TLS Downgrade

1. **Description / fonctionnement :** Force une connexion vers un protocole ou chiffrement plus faible.
2. **Causes techniques :** contradiction d’interprétation entre composants ou confiance excessive dans les en-têtes/réseaux ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** CDN, DNS, TLS, reverse proxy, CORS, routes HTTP et appels réseau serveur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Comparer les couches proxy/app, inspecter en-têtes, tls, dns et règles cors. Rechercher spécialement : contradiction d’interprétation entre composants ou confiance excessive dans les en-têtes/réseaux.
5. **Prévention :** Normalisation cohérente, allowlist d’origines et de destinations, TLS correct, validation réseau. **Point spécifique :** configurer explicitement proxy et application ; rejeter les en-têtes ambigus et destinations interdites
6. **Correction sécurisée :** Configurer explicitement proxy et application ; rejeter les en-têtes ambigus et destinations interdites. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** tester avec environnements autorisés les origines inattendues, duplications d’en-têtes et chemins de proxy Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Surveiller configuration DNS/TLS/proxy et la maintenir versionnée. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 117 — Subdomain Takeover

1. **Description / fonctionnement :** Prend le contrôle d'une ressource externe abandonnée mais référencée en DNS.
2. **Causes techniques :** contradiction d’interprétation entre composants ou confiance excessive dans les en-têtes/réseaux ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** CDN, DNS, TLS, reverse proxy, CORS, routes HTTP et appels réseau serveur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Comparer les couches proxy/app, inspecter en-têtes, tls, dns et règles cors. Rechercher spécialement : contradiction d’interprétation entre composants ou confiance excessive dans les en-têtes/réseaux.
5. **Prévention :** Normalisation cohérente, allowlist d’origines et de destinations, TLS correct, validation réseau. **Point spécifique :** configurer explicitement proxy et application ; rejeter les en-têtes ambigus et destinations interdites
6. **Correction sécurisée :** Configurer explicitement proxy et application ; rejeter les en-têtes ambigus et destinations interdites. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** tester avec environnements autorisés les origines inattendues, duplications d’en-têtes et chemins de proxy Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Surveiller configuration DNS/TLS/proxy et la maintenir versionnée. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 118 — CORS Misconfiguration

1. **Description / fonctionnement :** Exploite une politique d'origines trop permissive.
2. **Causes techniques :** Origines réfléchies et credentials partageables ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** CDN, DNS, TLS, reverse proxy, CORS, routes HTTP et appels réseau serveur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Comparer les couches proxy/app, inspecter en-têtes, tls, dns et règles cors. Rechercher spécialement : origines réfléchies et credentials partageables.
5. **Prévention :** Normalisation cohérente, allowlist d’origines et de destinations, TLS correct, validation réseau. **Point spécifique :** Définir origines exactes autorisées et ne jamais combiner wildcard avec credentials.
6. **Correction sécurisée :** Configurer explicitement proxy et application ; rejeter les en-têtes ambigus et destinations interdites. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une origine inconnue ne reçoit pas les en-têtes permettant l’accès aux données privées. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Surveiller configuration DNS/TLS/proxy et la maintenir versionnée. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 119 — SSRF

1. **Description / fonctionnement :** Fait émettre des requêtes serveur vers des cibles non autorisées.
2. **Causes techniques :** Destination URL fournie par client puis résolue côté serveur ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** CDN, DNS, TLS, reverse proxy, CORS, routes HTTP et appels réseau serveur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Comparer les couches proxy/app, inspecter en-têtes, tls, dns et règles cors. Rechercher spécialement : destination url fournie par client puis résolue côté serveur.
5. **Prévention :** Normalisation cohérente, allowlist d’origines et de destinations, TLS correct, validation réseau. **Point spécifique :** Allowlist destinations, refus IP privées/link-local après résolution et à la connexion ; bloquer redirections.
6. **Correction sécurisée :** Configurer explicitement proxy et application ; rejeter les en-têtes ambigus et destinations interdites. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une URL locale, metadata cloud, redirection privée ou DNS changeant est bloqué. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Surveiller configuration DNS/TLS/proxy et la maintenir versionnée. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 120 — DNS Rebinding

1. **Description / fonctionnement :** Change la résolution DNS pour détourner une politique de confiance.
2. **Causes techniques :** Destination URL fournie par client puis résolue côté serveur ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** CDN, DNS, TLS, reverse proxy, CORS, routes HTTP et appels réseau serveur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Comparer les couches proxy/app, inspecter en-têtes, tls, dns et règles cors. Rechercher spécialement : destination url fournie par client puis résolue côté serveur.
5. **Prévention :** Normalisation cohérente, allowlist d’origines et de destinations, TLS correct, validation réseau. **Point spécifique :** Allowlist destinations, refus IP privées/link-local après résolution et à la connexion ; bloquer redirections.
6. **Correction sécurisée :** Configurer explicitement proxy et application ; rejeter les en-têtes ambigus et destinations interdites. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une URL locale, metadata cloud, redirection privée ou DNS changeant est bloqué. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Surveiller configuration DNS/TLS/proxy et la maintenir versionnée. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 121 — HTTP Method Tampering

1. **Description / fonctionnement :** Utilise une autre méthode HTTP pour contourner un contrôle.
2. **Causes techniques :** Normalisation différente entre proxy, cache et application ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** CDN, DNS, TLS, reverse proxy, CORS, routes HTTP et appels réseau serveur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Comparer les couches proxy/app, inspecter en-têtes, tls, dns et règles cors. Rechercher spécialement : normalisation différente entre proxy, cache et application.
5. **Prévention :** Normalisation cohérente, allowlist d’origines et de destinations, TLS correct, validation réseau. **Point spécifique :** Aligner interprétation du protocole, cache keys, méthodes et en-têtes ; désactiver ambiguïtés.
6. **Correction sécurisée :** Configurer explicitement proxy et application ; rejeter les en-têtes ambigus et destinations interdites. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Des en-têtes ambigus ou doublés sont rejetés de manière cohérente. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Surveiller configuration DNS/TLS/proxy et la maintenir versionnée. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 122 — Reverse Proxy Misconfiguration

1. **Description / fonctionnement :** Abuse de divergences entre proxy et application.
2. **Causes techniques :** Normalisation différente entre proxy, cache et application ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** CDN, DNS, TLS, reverse proxy, CORS, routes HTTP et appels réseau serveur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Comparer les couches proxy/app, inspecter en-têtes, tls, dns et règles cors. Rechercher spécialement : normalisation différente entre proxy, cache et application.
5. **Prévention :** Normalisation cohérente, allowlist d’origines et de destinations, TLS correct, validation réseau. **Point spécifique :** Aligner interprétation du protocole, cache keys, méthodes et en-têtes ; désactiver ambiguïtés.
6. **Correction sécurisée :** Configurer explicitement proxy et application ; rejeter les en-têtes ambigus et destinations interdites. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Des en-têtes ambigus ou doublés sont rejetés de manière cohérente. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Surveiller configuration DNS/TLS/proxy et la maintenir versionnée. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».
