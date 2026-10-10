# 08 — Disponibilité et DDoS

**Couverture :** 15 types d’attaque numérotés 123 à 137. Cet inventaire identifie des familles, variantes et scénarios ; certains termes se recoupent.

**Utilisation :** lire les profils liés à la surface attaquée. Les risques sont indicatifs et se recalculent selon exposition, impact, contrôle existant et vraisemblance. Ne pas effectuer de tests actifs sur des systèmes non autorisés.

## 123 — DoS

1. **Description / fonctionnement :** Rend un service indisponible en épuisant ses ressources.
2. **Causes techniques :** Absence de limites de coûts par requête ou de protection périmétrique ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** load balancer, application, API, base, connexions et authentification ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Mesurer temps de réponse et files en charge contrôlée ; analyser limites de taille et de débit. Rechercher spécialement : absence de limites de coûts par requête ou de protection périmétrique.
5. **Prévention :** Rate limiting multi-niveaux, quotas, timeouts, files, autoscaling et protection DDoS en périphérie. **Point spécifique :** Limiter délais, corps, requêtes et connexions ; WAF/CDN/anti-DDoS selon l’exposition.
6. **Correction sécurisée :** Placer des limites par IP/utilisateur/tenant et sur les opérations coûteuses ; isoler les dépendances. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Charge de test bornée : plafonds activés, métriques et service toujours réactif. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : indisponibilité et dégradation du service, surcoûts et effet domino.
9. **Prévention de réapparition :** Superviser capacité et prévoir reprise, caches et circuit breakers. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 124 — DDoS

1. **Description / fonctionnement :** Sature un service depuis de multiples sources.
2. **Causes techniques :** Absence de limites de coûts par requête ou de protection périmétrique ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** load balancer, application, API, base, connexions et authentification ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Mesurer temps de réponse et files en charge contrôlée ; analyser limites de taille et de débit. Rechercher spécialement : absence de limites de coûts par requête ou de protection périmétrique.
5. **Prévention :** Rate limiting multi-niveaux, quotas, timeouts, files, autoscaling et protection DDoS en périphérie. **Point spécifique :** Limiter délais, corps, requêtes et connexions ; WAF/CDN/anti-DDoS selon l’exposition.
6. **Correction sécurisée :** Placer des limites par IP/utilisateur/tenant et sur les opérations coûteuses ; isoler les dépendances. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Charge de test bornée : plafonds activés, métriques et service toujours réactif. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : indisponibilité et dégradation du service, surcoûts et effet domino.
9. **Prévention de réapparition :** Superviser capacité et prévoir reprise, caches et circuit breakers. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 125 — HTTP Flood

1. **Description / fonctionnement :** Sature le traitement des requêtes HTTP.
2. **Causes techniques :** Absence de limites de coûts par requête ou de protection périmétrique ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** load balancer, application, API, base, connexions et authentification ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Mesurer temps de réponse et files en charge contrôlée ; analyser limites de taille et de débit. Rechercher spécialement : absence de limites de coûts par requête ou de protection périmétrique.
5. **Prévention :** Rate limiting multi-niveaux, quotas, timeouts, files, autoscaling et protection DDoS en périphérie. **Point spécifique :** Limiter délais, corps, requêtes et connexions ; WAF/CDN/anti-DDoS selon l’exposition.
6. **Correction sécurisée :** Placer des limites par IP/utilisateur/tenant et sur les opérations coûteuses ; isoler les dépendances. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Charge de test bornée : plafonds activés, métriques et service toujours réactif. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : indisponibilité et dégradation du service, surcoûts et effet domino.
9. **Prévention de réapparition :** Superviser capacité et prévoir reprise, caches et circuit breakers. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 126 — SYN Flood

1. **Description / fonctionnement :** Épuise le traitement des connexions TCP initiales.
2. **Causes techniques :** Absence de limites de coûts par requête ou de protection périmétrique ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** load balancer, application, API, base, connexions et authentification ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Mesurer temps de réponse et files en charge contrôlée ; analyser limites de taille et de débit. Rechercher spécialement : absence de limites de coûts par requête ou de protection périmétrique.
5. **Prévention :** Rate limiting multi-niveaux, quotas, timeouts, files, autoscaling et protection DDoS en périphérie. **Point spécifique :** Limiter délais, corps, requêtes et connexions ; WAF/CDN/anti-DDoS selon l’exposition.
6. **Correction sécurisée :** Placer des limites par IP/utilisateur/tenant et sur les opérations coûteuses ; isoler les dépendances. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Charge de test bornée : plafonds activés, métriques et service toujours réactif. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : indisponibilité et dégradation du service, surcoûts et effet domino.
9. **Prévention de réapparition :** Superviser capacité et prévoir reprise, caches et circuit breakers. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 127 — UDP Flood

1. **Description / fonctionnement :** Sature réseau ou serveur par trafic UDP.
2. **Causes techniques :** Absence de limites de coûts par requête ou de protection périmétrique ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** load balancer, application, API, base, connexions et authentification ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Mesurer temps de réponse et files en charge contrôlée ; analyser limites de taille et de débit. Rechercher spécialement : absence de limites de coûts par requête ou de protection périmétrique.
5. **Prévention :** Rate limiting multi-niveaux, quotas, timeouts, files, autoscaling et protection DDoS en périphérie. **Point spécifique :** Limiter délais, corps, requêtes et connexions ; WAF/CDN/anti-DDoS selon l’exposition.
6. **Correction sécurisée :** Placer des limites par IP/utilisateur/tenant et sur les opérations coûteuses ; isoler les dépendances. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Charge de test bornée : plafonds activés, métriques et service toujours réactif. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : indisponibilité et dégradation du service, surcoûts et effet domino.
9. **Prévention de réapparition :** Superviser capacité et prévoir reprise, caches et circuit breakers. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 128 — Slowloris

1. **Description / fonctionnement :** Maintient longtemps des connexions HTTP incomplètes.
2. **Causes techniques :** Absence de limites de coûts par requête ou de protection périmétrique ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** load balancer, application, API, base, connexions et authentification ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Mesurer temps de réponse et files en charge contrôlée ; analyser limites de taille et de débit. Rechercher spécialement : absence de limites de coûts par requête ou de protection périmétrique.
5. **Prévention :** Rate limiting multi-niveaux, quotas, timeouts, files, autoscaling et protection DDoS en périphérie. **Point spécifique :** Limiter délais, corps, requêtes et connexions ; WAF/CDN/anti-DDoS selon l’exposition.
6. **Correction sécurisée :** Placer des limites par IP/utilisateur/tenant et sur les opérations coûteuses ; isoler les dépendances. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Charge de test bornée : plafonds activés, métriques et service toujours réactif. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : indisponibilité et dégradation du service, surcoûts et effet domino.
9. **Prévention de réapparition :** Superviser capacité et prévoir reprise, caches et circuit breakers. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 129 — Slow POST

1. **Description / fonctionnement :** Envoie un corps de requête excessivement lent.
2. **Causes techniques :** Absence de limites de coûts par requête ou de protection périmétrique ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** load balancer, application, API, base, connexions et authentification ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Mesurer temps de réponse et files en charge contrôlée ; analyser limites de taille et de débit. Rechercher spécialement : absence de limites de coûts par requête ou de protection périmétrique.
5. **Prévention :** Rate limiting multi-niveaux, quotas, timeouts, files, autoscaling et protection DDoS en périphérie. **Point spécifique :** Limiter délais, corps, requêtes et connexions ; WAF/CDN/anti-DDoS selon l’exposition.
6. **Correction sécurisée :** Placer des limites par IP/utilisateur/tenant et sur les opérations coûteuses ; isoler les dépendances. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Charge de test bornée : plafonds activés, métriques et service toujours réactif. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : indisponibilité et dégradation du service, surcoûts et effet domino.
9. **Prévention de réapparition :** Superviser capacité et prévoir reprise, caches et circuit breakers. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 130 — Application Layer DDoS

1. **Description / fonctionnement :** Surcharge des opérations métier coûteuses.
2. **Causes techniques :** Absence de limites de coûts par requête ou de protection périmétrique ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** load balancer, application, API, base, connexions et authentification ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Mesurer temps de réponse et files en charge contrôlée ; analyser limites de taille et de débit. Rechercher spécialement : absence de limites de coûts par requête ou de protection périmétrique.
5. **Prévention :** Rate limiting multi-niveaux, quotas, timeouts, files, autoscaling et protection DDoS en périphérie. **Point spécifique :** Limiter délais, corps, requêtes et connexions ; WAF/CDN/anti-DDoS selon l’exposition.
6. **Correction sécurisée :** Placer des limites par IP/utilisateur/tenant et sur les opérations coûteuses ; isoler les dépendances. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Charge de test bornée : plafonds activés, métriques et service toujours réactif. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : indisponibilité et dégradation du service, surcoûts et effet domino.
9. **Prévention de réapparition :** Superviser capacité et prévoir reprise, caches et circuit breakers. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 131 — DNS Amplification

1. **Description / fonctionnement :** Utilise des réponses DNS disproportionnées comme vecteur de trafic.
2. **Causes techniques :** Absence de limites de coûts par requête ou de protection périmétrique ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** load balancer, application, API, base, connexions et authentification ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Mesurer temps de réponse et files en charge contrôlée ; analyser limites de taille et de débit. Rechercher spécialement : absence de limites de coûts par requête ou de protection périmétrique.
5. **Prévention :** Rate limiting multi-niveaux, quotas, timeouts, files, autoscaling et protection DDoS en périphérie. **Point spécifique :** Limiter délais, corps, requêtes et connexions ; WAF/CDN/anti-DDoS selon l’exposition.
6. **Correction sécurisée :** Placer des limites par IP/utilisateur/tenant et sur les opérations coûteuses ; isoler les dépendances. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Charge de test bornée : plafonds activés, métriques et service toujours réactif. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : indisponibilité et dégradation du service, surcoûts et effet domino.
9. **Prévention de réapparition :** Superviser capacité et prévoir reprise, caches et circuit breakers. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 132 — NTP Amplification

1. **Description / fonctionnement :** Utilise des réponses NTP disproportionnées comme vecteur de trafic.
2. **Causes techniques :** Absence de limites de coûts par requête ou de protection périmétrique ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** load balancer, application, API, base, connexions et authentification ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Mesurer temps de réponse et files en charge contrôlée ; analyser limites de taille et de débit. Rechercher spécialement : absence de limites de coûts par requête ou de protection périmétrique.
5. **Prévention :** Rate limiting multi-niveaux, quotas, timeouts, files, autoscaling et protection DDoS en périphérie. **Point spécifique :** Limiter délais, corps, requêtes et connexions ; WAF/CDN/anti-DDoS selon l’exposition.
6. **Correction sécurisée :** Placer des limites par IP/utilisateur/tenant et sur les opérations coûteuses ; isoler les dépendances. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Charge de test bornée : plafonds activés, métriques et service toujours réactif. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : indisponibilité et dégradation du service, surcoûts et effet domino.
9. **Prévention de réapparition :** Superviser capacité et prévoir reprise, caches et circuit breakers. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 133 — Resource Exhaustion

1. **Description / fonctionnement :** Épuise CPU, RAM, file d'attente ou espace disque.
2. **Causes techniques :** Absence de limites de coûts par requête ou de protection périmétrique ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** load balancer, application, API, base, connexions et authentification ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Mesurer temps de réponse et files en charge contrôlée ; analyser limites de taille et de débit. Rechercher spécialement : absence de limites de coûts par requête ou de protection périmétrique.
5. **Prévention :** Rate limiting multi-niveaux, quotas, timeouts, files, autoscaling et protection DDoS en périphérie. **Point spécifique :** Limiter délais, corps, requêtes et connexions ; WAF/CDN/anti-DDoS selon l’exposition.
6. **Correction sécurisée :** Placer des limites par IP/utilisateur/tenant et sur les opérations coûteuses ; isoler les dépendances. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Charge de test bornée : plafonds activés, métriques et service toujours réactif. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : indisponibilité et dégradation du service, surcoûts et effet domino.
9. **Prévention de réapparition :** Superviser capacité et prévoir reprise, caches et circuit breakers. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 134 — Connection Exhaustion

1. **Description / fonctionnement :** Consomme le nombre maximal de connexions.
2. **Causes techniques :** Absence de limites de coûts par requête ou de protection périmétrique ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** load balancer, application, API, base, connexions et authentification ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Mesurer temps de réponse et files en charge contrôlée ; analyser limites de taille et de débit. Rechercher spécialement : absence de limites de coûts par requête ou de protection périmétrique.
5. **Prévention :** Rate limiting multi-niveaux, quotas, timeouts, files, autoscaling et protection DDoS en périphérie. **Point spécifique :** Limiter délais, corps, requêtes et connexions ; WAF/CDN/anti-DDoS selon l’exposition.
6. **Correction sécurisée :** Placer des limites par IP/utilisateur/tenant et sur les opérations coûteuses ; isoler les dépendances. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Charge de test bornée : plafonds activés, métriques et service toujours réactif. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : indisponibilité et dégradation du service, surcoûts et effet domino.
9. **Prévention de réapparition :** Superviser capacité et prévoir reprise, caches et circuit breakers. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 135 — API Flooding

1. **Description / fonctionnement :** Sature un service via ses endpoints API.
2. **Causes techniques :** Absence de limites de coûts par requête ou de protection périmétrique ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** load balancer, application, API, base, connexions et authentification ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Mesurer temps de réponse et files en charge contrôlée ; analyser limites de taille et de débit. Rechercher spécialement : absence de limites de coûts par requête ou de protection périmétrique.
5. **Prévention :** Rate limiting multi-niveaux, quotas, timeouts, files, autoscaling et protection DDoS en périphérie. **Point spécifique :** Limiter délais, corps, requêtes et connexions ; WAF/CDN/anti-DDoS selon l’exposition.
6. **Correction sécurisée :** Placer des limites par IP/utilisateur/tenant et sur les opérations coûteuses ; isoler les dépendances. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Charge de test bornée : plafonds activés, métriques et service toujours réactif. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : indisponibilité et dégradation du service, surcoûts et effet domino.
9. **Prévention de réapparition :** Superviser capacité et prévoir reprise, caches et circuit breakers. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 136 — Database Query Exhaustion

1. **Description / fonctionnement :** Provoque des requêtes SQL ou NoSQL disproportionnellement coûteuses.
2. **Causes techniques :** Absence de limites de coûts par requête ou de protection périmétrique ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** load balancer, application, API, base, connexions et authentification ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Mesurer temps de réponse et files en charge contrôlée ; analyser limites de taille et de débit. Rechercher spécialement : absence de limites de coûts par requête ou de protection périmétrique.
5. **Prévention :** Rate limiting multi-niveaux, quotas, timeouts, files, autoscaling et protection DDoS en périphérie. **Point spécifique :** Limiter délais, corps, requêtes et connexions ; WAF/CDN/anti-DDoS selon l’exposition.
6. **Correction sécurisée :** Placer des limites par IP/utilisateur/tenant et sur les opérations coûteuses ; isoler les dépendances. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Charge de test bornée : plafonds activés, métriques et service toujours réactif. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : indisponibilité et dégradation du service, surcoûts et effet domino.
9. **Prévention de réapparition :** Superviser capacité et prévoir reprise, caches et circuit breakers. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 137 — Login Flooding

1. **Description / fonctionnement :** Sature le traitement des connexions utilisateur.
2. **Causes techniques :** Absence de limites de coûts par requête ou de protection périmétrique ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** load balancer, application, API, base, connexions et authentification ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Mesurer temps de réponse et files en charge contrôlée ; analyser limites de taille et de débit. Rechercher spécialement : absence de limites de coûts par requête ou de protection périmétrique.
5. **Prévention :** Rate limiting multi-niveaux, quotas, timeouts, files, autoscaling et protection DDoS en périphérie. **Point spécifique :** Limiter délais, corps, requêtes et connexions ; WAF/CDN/anti-DDoS selon l’exposition.
6. **Correction sécurisée :** Placer des limites par IP/utilisateur/tenant et sur les opérations coûteuses ; isoler les dépendances. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Charge de test bornée : plafonds activés, métriques et service toujours réactif. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : indisponibilité et dégradation du service, surcoûts et effet domino.
9. **Prévention de réapparition :** Superviser capacité et prévoir reprise, caches et circuit breakers. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».
