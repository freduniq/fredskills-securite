# 02 — XSS et navigateur

**Couverture :** 12 types d’attaque numérotés 21 à 32. Cet inventaire identifie des familles, variantes et scénarios ; certains termes se recoupent.

**Utilisation :** lire les profils liés à la surface attaquée. Les risques sont indicatifs et se recalculent selon exposition, impact, contrôle existant et vraisemblance. Ne pas effectuer de tests actifs sur des systèmes non autorisés.

## 021 — Reflected XSS

1. **Description / fonctionnement :** Script renvoyé dans une réponse puis exécuté dans le navigateur.
2. **Causes techniques :** Source non fiable injectée dans un contexte navigateur actif ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** templates, JavaScript frontend, HTML, styles, cookies, iframe et WebSocket ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Examiner les puits dom et moteurs de rendu, l’encodage contextuel et les en-têtes ; exécuter des tests de rendu sur environnement autorisé. Rechercher spécialement : source non fiable injectée dans un contexte navigateur actif.
5. **Prévention :** Encoder selon le contexte, utiliser des APIs DOM sûres, sanitizer éprouvé si HTML nécessaire, CSP et anti-framing. **Point spécifique :** Employer échappement contextuel, DOM textContent, clés d’objet sûres et sanitizer maintenu si HTML requis.
6. **Correction sécurisée :** Supprimer les affectations dangereuses à innerHTML lorsque textContent suffit ; utiliser CSP en défense complémentaire. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Les caractères HTML/JS de test restent inertes ; les propriétés de prototype ne changent pas. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Adopter des composants sûrs et une revue des sorties utilisateur. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 022 — Stored XSS

1. **Description / fonctionnement :** Charge du code depuis une donnée persistée dans l'application.
2. **Causes techniques :** Source non fiable injectée dans un contexte navigateur actif ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** templates, JavaScript frontend, HTML, styles, cookies, iframe et WebSocket ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Examiner les puits dom et moteurs de rendu, l’encodage contextuel et les en-têtes ; exécuter des tests de rendu sur environnement autorisé. Rechercher spécialement : source non fiable injectée dans un contexte navigateur actif.
5. **Prévention :** Encoder selon le contexte, utiliser des APIs DOM sûres, sanitizer éprouvé si HTML nécessaire, CSP et anti-framing. **Point spécifique :** Employer échappement contextuel, DOM textContent, clés d’objet sûres et sanitizer maintenu si HTML requis.
6. **Correction sécurisée :** Supprimer les affectations dangereuses à innerHTML lorsque textContent suffit ; utiliser CSP en défense complémentaire. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Les caractères HTML/JS de test restent inertes ; les propriétés de prototype ne changent pas. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Adopter des composants sûrs et une revue des sorties utilisateur. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 023 — DOM-Based XSS

1. **Description / fonctionnement :** Injecte des données dans un puits DOM dangereux.
2. **Causes techniques :** Source non fiable injectée dans un contexte navigateur actif ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** templates, JavaScript frontend, HTML, styles, cookies, iframe et WebSocket ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Examiner les puits dom et moteurs de rendu, l’encodage contextuel et les en-têtes ; exécuter des tests de rendu sur environnement autorisé. Rechercher spécialement : source non fiable injectée dans un contexte navigateur actif.
5. **Prévention :** Encoder selon le contexte, utiliser des APIs DOM sûres, sanitizer éprouvé si HTML nécessaire, CSP et anti-framing. **Point spécifique :** Employer échappement contextuel, DOM textContent, clés d’objet sûres et sanitizer maintenu si HTML requis.
6. **Correction sécurisée :** Supprimer les affectations dangereuses à innerHTML lorsque textContent suffit ; utiliser CSP en défense complémentaire. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Les caractères HTML/JS de test restent inertes ; les propriétés de prototype ne changent pas. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Adopter des composants sûrs et une revue des sorties utilisateur. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 024 — Blind XSS

1. **Description / fonctionnement :** Charge utile XSS déclenchée dans un autre parcours utilisateur.
2. **Causes techniques :** Source non fiable injectée dans un contexte navigateur actif ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** templates, JavaScript frontend, HTML, styles, cookies, iframe et WebSocket ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Examiner les puits dom et moteurs de rendu, l’encodage contextuel et les en-têtes ; exécuter des tests de rendu sur environnement autorisé. Rechercher spécialement : source non fiable injectée dans un contexte navigateur actif.
5. **Prévention :** Encoder selon le contexte, utiliser des APIs DOM sûres, sanitizer éprouvé si HTML nécessaire, CSP et anti-framing. **Point spécifique :** Employer échappement contextuel, DOM textContent, clés d’objet sûres et sanitizer maintenu si HTML requis.
6. **Correction sécurisée :** Supprimer les affectations dangereuses à innerHTML lorsque textContent suffit ; utiliser CSP en défense complémentaire. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Les caractères HTML/JS de test restent inertes ; les propriétés de prototype ne changent pas. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Adopter des composants sûrs et une revue des sorties utilisateur. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 025 — Mutation XSS

1. **Description / fonctionnement :** Exploit des transformations du DOM après sanitation insuffisante.
2. **Causes techniques :** Source non fiable injectée dans un contexte navigateur actif ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** templates, JavaScript frontend, HTML, styles, cookies, iframe et WebSocket ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Examiner les puits dom et moteurs de rendu, l’encodage contextuel et les en-têtes ; exécuter des tests de rendu sur environnement autorisé. Rechercher spécialement : source non fiable injectée dans un contexte navigateur actif.
5. **Prévention :** Encoder selon le contexte, utiliser des APIs DOM sûres, sanitizer éprouvé si HTML nécessaire, CSP et anti-framing. **Point spécifique :** Employer échappement contextuel, DOM textContent, clés d’objet sûres et sanitizer maintenu si HTML requis.
6. **Correction sécurisée :** Supprimer les affectations dangereuses à innerHTML lorsque textContent suffit ; utiliser CSP en défense complémentaire. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Les caractères HTML/JS de test restent inertes ; les propriétés de prototype ne changent pas. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Adopter des composants sûrs et une revue des sorties utilisateur. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 026 — Self-XSS

1. **Description / fonctionnement :** Incite une personne à exécuter du code dans son navigateur.
2. **Causes techniques :** Source non fiable injectée dans un contexte navigateur actif ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** templates, JavaScript frontend, HTML, styles, cookies, iframe et WebSocket ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Examiner les puits dom et moteurs de rendu, l’encodage contextuel et les en-têtes ; exécuter des tests de rendu sur environnement autorisé. Rechercher spécialement : source non fiable injectée dans un contexte navigateur actif.
5. **Prévention :** Encoder selon le contexte, utiliser des APIs DOM sûres, sanitizer éprouvé si HTML nécessaire, CSP et anti-framing. **Point spécifique :** Employer échappement contextuel, DOM textContent, clés d’objet sûres et sanitizer maintenu si HTML requis.
6. **Correction sécurisée :** Supprimer les affectations dangereuses à innerHTML lorsque textContent suffit ; utiliser CSP en défense complémentaire. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Les caractères HTML/JS de test restent inertes ; les propriétés de prototype ne changent pas. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **modéré** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Adopter des composants sûrs et une revue des sorties utilisateur. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 027 — Cross-Site Script Inclusion

1. **Description / fonctionnement :** Expose des données ou fonctionnalités via l'inclusion de script inter-origines.
2. **Causes techniques :** insertion non maîtrisée de contenu dans une sortie du navigateur ou contrôle d’origine insuffisant ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** templates, JavaScript frontend, HTML, styles, cookies, iframe et WebSocket ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Examiner les puits dom et moteurs de rendu, l’encodage contextuel et les en-têtes ; exécuter des tests de rendu sur environnement autorisé. Rechercher spécialement : insertion non maîtrisée de contenu dans une sortie du navigateur ou contrôle d’origine insuffisant.
5. **Prévention :** Encoder selon le contexte, utiliser des APIs DOM sûres, sanitizer éprouvé si HTML nécessaire, CSP et anti-framing. **Point spécifique :** supprimer les affectations dangereuses à innerHTML lorsque textContent suffit ; utiliser CSP en défense complémentaire
6. **Correction sécurisée :** Supprimer les affectations dangereuses à innerHTML lorsque textContent suffit ; utiliser CSP en défense complémentaire. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** vérifier qu’un texte contenant balises et caractères spéciaux reste du texte ; contrôler l’origine et les politiques navigateur Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Adopter des composants sûrs et une revue des sorties utilisateur. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 028 — DOM Clobbering

1. **Description / fonctionnement :** Utilise des éléments HTML pour écraser des variables ou références DOM.
2. **Causes techniques :** Source non fiable injectée dans un contexte navigateur actif ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** templates, JavaScript frontend, HTML, styles, cookies, iframe et WebSocket ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Examiner les puits dom et moteurs de rendu, l’encodage contextuel et les en-têtes ; exécuter des tests de rendu sur environnement autorisé. Rechercher spécialement : source non fiable injectée dans un contexte navigateur actif.
5. **Prévention :** Encoder selon le contexte, utiliser des APIs DOM sûres, sanitizer éprouvé si HTML nécessaire, CSP et anti-framing. **Point spécifique :** Employer échappement contextuel, DOM textContent, clés d’objet sûres et sanitizer maintenu si HTML requis.
6. **Correction sécurisée :** Supprimer les affectations dangereuses à innerHTML lorsque textContent suffit ; utiliser CSP en défense complémentaire. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Les caractères HTML/JS de test restent inertes ; les propriétés de prototype ne changent pas. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Adopter des composants sûrs et une revue des sorties utilisateur. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 029 — Clickjacking

1. **Description / fonctionnement :** Superpose des interfaces pour provoquer un clic involontaire.
2. **Causes techniques :** Page sensible intégrable dans une frame externe ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** templates, JavaScript frontend, HTML, styles, cookies, iframe et WebSocket ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Examiner les puits dom et moteurs de rendu, l’encodage contextuel et les en-têtes ; exécuter des tests de rendu sur environnement autorisé. Rechercher spécialement : page sensible intégrable dans une frame externe.
5. **Prévention :** Encoder selon le contexte, utiliser des APIs DOM sûres, sanitizer éprouvé si HTML nécessaire, CSP et anti-framing. **Point spécifique :** Utiliser CSP frame-ancestors adaptée ; X-Frame-Options en compatibilité.
6. **Correction sécurisée :** Supprimer les affectations dangereuses à innerHTML lorsque textContent suffit ; utiliser CSP en défense complémentaire. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une page de validation ne peut pas être affichée dans une iframe d’origine tierce. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Adopter des composants sûrs et une revue des sorties utilisateur. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 030 — UI Redressing

1. **Description / fonctionnement :** Présente une interface trompeuse pour détourner une action.
2. **Causes techniques :** Page sensible intégrable dans une frame externe ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** templates, JavaScript frontend, HTML, styles, cookies, iframe et WebSocket ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Examiner les puits dom et moteurs de rendu, l’encodage contextuel et les en-têtes ; exécuter des tests de rendu sur environnement autorisé. Rechercher spécialement : page sensible intégrable dans une frame externe.
5. **Prévention :** Encoder selon le contexte, utiliser des APIs DOM sûres, sanitizer éprouvé si HTML nécessaire, CSP et anti-framing. **Point spécifique :** Utiliser CSP frame-ancestors adaptée ; X-Frame-Options en compatibilité.
6. **Correction sécurisée :** Supprimer les affectations dangereuses à innerHTML lorsque textContent suffit ; utiliser CSP en défense complémentaire. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une page de validation ne peut pas être affichée dans une iframe d’origine tierce. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Adopter des composants sûrs et une revue des sorties utilisateur. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 031 — Cross-Site WebSocket Hijacking

1. **Description / fonctionnement :** Abuse d'une connexion WebSocket fondée sur des cookies sans contrôle d'origine.
2. **Causes techniques :** Connexion ou message WS non authentifié/autorisé ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** templates, JavaScript frontend, HTML, styles, cookies, iframe et WebSocket ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Examiner les puits dom et moteurs de rendu, l’encodage contextuel et les en-têtes ; exécuter des tests de rendu sur environnement autorisé. Rechercher spécialement : connexion ou message ws non authentifié/autorisé.
5. **Prévention :** Encoder selon le contexte, utiliser des APIs DOM sûres, sanitizer éprouvé si HTML nécessaire, CSP et anti-framing. **Point spécifique :** Vérifier Origin attendu, authentifier la connexion et autoriser chaque message côté serveur.
6. **Correction sécurisée :** Supprimer les affectations dangereuses à innerHTML lorsque textContent suffit ; utiliser CSP en défense complémentaire. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un client d’une autre origine ou d’un autre rôle ne peut pas exécuter un message sensible. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Adopter des composants sûrs et une revue des sorties utilisateur. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 032 — Client-Side Prototype Pollution

1. **Description / fonctionnement :** Modifie des propriétés de prototype JavaScript depuis des données non fiables.
2. **Causes techniques :** Source non fiable injectée dans un contexte navigateur actif ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** templates, JavaScript frontend, HTML, styles, cookies, iframe et WebSocket ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Examiner les puits dom et moteurs de rendu, l’encodage contextuel et les en-têtes ; exécuter des tests de rendu sur environnement autorisé. Rechercher spécialement : source non fiable injectée dans un contexte navigateur actif.
5. **Prévention :** Encoder selon le contexte, utiliser des APIs DOM sûres, sanitizer éprouvé si HTML nécessaire, CSP et anti-framing. **Point spécifique :** Employer échappement contextuel, DOM textContent, clés d’objet sûres et sanitizer maintenu si HTML requis.
6. **Correction sécurisée :** Supprimer les affectations dangereuses à innerHTML lorsque textContent suffit ; utiliser CSP en défense complémentaire. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Les caractères HTML/JS de test restent inertes ; les propriétés de prototype ne changent pas. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Adopter des composants sûrs et une revue des sorties utilisateur. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».
