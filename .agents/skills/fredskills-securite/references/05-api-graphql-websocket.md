# 05 — API, GraphQL et WebSocket

**Couverture :** 15 types d’attaque numérotés 71 à 85. Cet inventaire identifie des familles, variantes et scénarios ; certains termes se recoupent.

**Utilisation :** lire les profils liés à la surface attaquée. Les risques sont indicatifs et se recalculent selon exposition, impact, contrôle existant et vraisemblance. Ne pas effectuer de tests actifs sur des systèmes non autorisés.

## 071 — API BOLA

1. **Description / fonctionnement :** Accès API à un objet non autorisé.
2. **Causes techniques :** Identifiant d’objet utilisé sans contrôle d’appartenance ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** routes REST/GraphQL, résolveurs, WebSocket, clés et événements API ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Faire inventaire des endpoints et versions ; vérifier permissions par objet/champ, quotas, schémas et messages. Rechercher spécialement : identifiant d’objet utilisé sans contrôle d’appartenance.
5. **Prévention :** Schémas stricts, authentification, autorisation champ/objet, limites de taille/coût et gestion des versions. **Point spécifique :** Récupérer les objets avec filtre tenant/propriétaire et autorisation serveur à chaque opération.
6. **Correction sécurisée :** Ajouter middleware serveur de validation, quotas et contrôle d’accès dans chaque résolveur/handler. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Changer seulement l’ID vers un objet du second compte renvoie 403 ou 404. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Catalogue API à jour, revue d’autorisations et métriques d’abus. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 072 — API Broken Authentication

1. **Description / fonctionnement :** Absence ou défaut de contrôle d'identité dans l'API.
2. **Causes techniques :** API sans limites, contrôles d’identité, validation de schéma ou inventaire suffisant ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** routes REST/GraphQL, résolveurs, WebSocket, clés et événements API ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Faire inventaire des endpoints et versions ; vérifier permissions par objet/champ, quotas, schémas et messages. Rechercher spécialement : api sans limites, contrôles d’identité, validation de schéma ou inventaire suffisant.
5. **Prévention :** Schémas stricts, authentification, autorisation champ/objet, limites de taille/coût et gestion des versions. **Point spécifique :** ajouter middleware serveur de validation, quotas et contrôle d’accès dans chaque résolveur/handler
6. **Correction sécurisée :** Ajouter middleware serveur de validation, quotas et contrôle d’accès dans chaque résolveur/handler. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** tester réponses minimales, ressources appartenant à autrui, payloads surdimensionnés et versions dépréciées Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Catalogue API à jour, revue d’autorisations et métriques d’abus. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 073 — Excessive Data Exposure

1. **Description / fonctionnement :** Réponse API contenant des champs sensibles inutiles.
2. **Causes techniques :** API sans limites, contrôles d’identité, validation de schéma ou inventaire suffisant ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** routes REST/GraphQL, résolveurs, WebSocket, clés et événements API ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Faire inventaire des endpoints et versions ; vérifier permissions par objet/champ, quotas, schémas et messages. Rechercher spécialement : api sans limites, contrôles d’identité, validation de schéma ou inventaire suffisant.
5. **Prévention :** Schémas stricts, authentification, autorisation champ/objet, limites de taille/coût et gestion des versions. **Point spécifique :** ajouter middleware serveur de validation, quotas et contrôle d’accès dans chaque résolveur/handler
6. **Correction sécurisée :** Ajouter middleware serveur de validation, quotas et contrôle d’accès dans chaque résolveur/handler. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** tester réponses minimales, ressources appartenant à autrui, payloads surdimensionnés et versions dépréciées Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Catalogue API à jour, revue d’autorisations et métriques d’abus. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 074 — API Mass Assignment

1. **Description / fonctionnement :** Mise à jour de propriétés non autorisées via une API.
2. **Causes techniques :** Champs ou fonctions d’autorisation déduits du client ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** routes REST/GraphQL, résolveurs, WebSocket, clés et événements API ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Faire inventaire des endpoints et versions ; vérifier permissions par objet/champ, quotas, schémas et messages. Rechercher spécialement : champs ou fonctions d’autorisation déduits du client.
5. **Prévention :** Schémas stricts, authentification, autorisation champ/objet, limites de taille/coût et gestion des versions. **Point spécifique :** Autoriser explicitement les champs modifiables et imposer des policies serveur par rôle/fonction.
6. **Correction sécurisée :** Ajouter middleware serveur de validation, quotas et contrôle d’accès dans chaque résolveur/handler. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un utilisateur standard ne peut pas passer role=admin ni modifier une propriété cachée. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Catalogue API à jour, revue d’autorisations et métriques d’abus. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 075 — API Rate Limit Bypass

1. **Description / fonctionnement :** Contourne le plafonnement des appels API.
2. **Causes techniques :** Absence de limites de coûts par requête ou de protection périmétrique ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** routes REST/GraphQL, résolveurs, WebSocket, clés et événements API ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Faire inventaire des endpoints et versions ; vérifier permissions par objet/champ, quotas, schémas et messages. Rechercher spécialement : absence de limites de coûts par requête ou de protection périmétrique.
5. **Prévention :** Schémas stricts, authentification, autorisation champ/objet, limites de taille/coût et gestion des versions. **Point spécifique :** Limiter délais, corps, requêtes et connexions ; WAF/CDN/anti-DDoS selon l’exposition.
6. **Correction sécurisée :** Ajouter middleware serveur de validation, quotas et contrôle d’accès dans chaque résolveur/handler. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Charge de test bornée : plafonds activés, métriques et service toujours réactif. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Catalogue API à jour, revue d’autorisations et métriques d’abus. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 076 — Unrestricted Resource Consumption

1. **Description / fonctionnement :** Épuise les ressources par des requêtes coûteuses.
2. **Causes techniques :** Absence de limites de coûts par requête ou de protection périmétrique ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** routes REST/GraphQL, résolveurs, WebSocket, clés et événements API ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Faire inventaire des endpoints et versions ; vérifier permissions par objet/champ, quotas, schémas et messages. Rechercher spécialement : absence de limites de coûts par requête ou de protection périmétrique.
5. **Prévention :** Schémas stricts, authentification, autorisation champ/objet, limites de taille/coût et gestion des versions. **Point spécifique :** Limiter délais, corps, requêtes et connexions ; WAF/CDN/anti-DDoS selon l’exposition.
6. **Correction sécurisée :** Ajouter middleware serveur de validation, quotas et contrôle d’accès dans chaque résolveur/handler. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Charge de test bornée : plafonds activés, métriques et service toujours réactif. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Catalogue API à jour, revue d’autorisations et métriques d’abus. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 077 — API Key Leakage

1. **Description / fonctionnement :** Expose une clé d'API dans le code ou les réponses.
2. **Causes techniques :** Secrets persistants ou transmis à un mauvais destinataire ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** routes REST/GraphQL, résolveurs, WebSocket, clés et événements API ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Faire inventaire des endpoints et versions ; vérifier permissions par objet/champ, quotas, schémas et messages. Rechercher spécialement : secrets persistants ou transmis à un mauvais destinataire.
5. **Prévention :** Schémas stricts, authentification, autorisation champ/objet, limites de taille/coût et gestion des versions. **Point spécifique :** Stocker en gestionnaire de secrets, réduire la portée et effectuer rotation et révocation.
6. **Correction sécurisée :** Ajouter middleware serveur de validation, quotas et contrôle d’accès dans chaque résolveur/handler. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Clés invalides ou retirées ne fonctionnent plus ; aucun secret dans logs et réponses. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Catalogue API à jour, revue d’autorisations et métriques d’abus. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 078 — API Key Abuse

1. **Description / fonctionnement :** Réutilise une clé API volée ou trop permissive.
2. **Causes techniques :** Secrets persistants ou transmis à un mauvais destinataire ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** routes REST/GraphQL, résolveurs, WebSocket, clés et événements API ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Faire inventaire des endpoints et versions ; vérifier permissions par objet/champ, quotas, schémas et messages. Rechercher spécialement : secrets persistants ou transmis à un mauvais destinataire.
5. **Prévention :** Schémas stricts, authentification, autorisation champ/objet, limites de taille/coût et gestion des versions. **Point spécifique :** Stocker en gestionnaire de secrets, réduire la portée et effectuer rotation et révocation.
6. **Correction sécurisée :** Ajouter middleware serveur de validation, quotas et contrôle d’accès dans chaque résolveur/handler. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Clés invalides ou retirées ne fonctionnent plus ; aucun secret dans logs et réponses. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Catalogue API à jour, revue d’autorisations et métriques d’abus. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 079 — GraphQL Introspection Exposure

1. **Description / fonctionnement :** Permet de découvrir un schéma GraphQL qui devrait être restreint.
2. **Causes techniques :** Complexité ou schéma API insuffisamment borné ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** routes REST/GraphQL, résolveurs, WebSocket, clés et événements API ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Faire inventaire des endpoints et versions ; vérifier permissions par objet/champ, quotas, schémas et messages. Rechercher spécialement : complexité ou schéma api insuffisamment borné.
5. **Prévention :** Schémas stricts, authentification, autorisation champ/objet, limites de taille/coût et gestion des versions. **Point spécifique :** Limiter profondeur, complexité, taille, pagination et introspection selon menace.
6. **Correction sécurisée :** Ajouter middleware serveur de validation, quotas et contrôle d’accès dans chaque résolveur/handler. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une requête profonde ou volumineuse dépasse le quota et reçoit un refus contrôlé. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Catalogue API à jour, revue d’autorisations et métriques d’abus. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 080 — GraphQL Query Complexity Abuse

1. **Description / fonctionnement :** Exécute des graphes ou requêtes GraphQL trop complexes.
2. **Causes techniques :** Complexité ou schéma API insuffisamment borné ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** routes REST/GraphQL, résolveurs, WebSocket, clés et événements API ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Faire inventaire des endpoints et versions ; vérifier permissions par objet/champ, quotas, schémas et messages. Rechercher spécialement : complexité ou schéma api insuffisamment borné.
5. **Prévention :** Schémas stricts, authentification, autorisation champ/objet, limites de taille/coût et gestion des versions. **Point spécifique :** Limiter profondeur, complexité, taille, pagination et introspection selon menace.
6. **Correction sécurisée :** Ajouter middleware serveur de validation, quotas et contrôle d’accès dans chaque résolveur/handler. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une requête profonde ou volumineuse dépasse le quota et reçoit un refus contrôlé. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Catalogue API à jour, revue d’autorisations et métriques d’abus. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 081 — GraphQL Batching Abuse

1. **Description / fonctionnement :** Abuse des requêtes GraphQL groupées pour contourner des quotas.
2. **Causes techniques :** Complexité ou schéma API insuffisamment borné ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** routes REST/GraphQL, résolveurs, WebSocket, clés et événements API ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Faire inventaire des endpoints et versions ; vérifier permissions par objet/champ, quotas, schémas et messages. Rechercher spécialement : complexité ou schéma api insuffisamment borné.
5. **Prévention :** Schémas stricts, authentification, autorisation champ/objet, limites de taille/coût et gestion des versions. **Point spécifique :** Limiter profondeur, complexité, taille, pagination et introspection selon menace.
6. **Correction sécurisée :** Ajouter middleware serveur de validation, quotas et contrôle d’accès dans chaque résolveur/handler. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une requête profonde ou volumineuse dépasse le quota et reçoit un refus contrôlé. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Catalogue API à jour, revue d’autorisations et métriques d’abus. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 082 — WebSocket Authentication Bypass

1. **Description / fonctionnement :** Utilise un canal WebSocket sans identité vérifiée.
2. **Causes techniques :** Récupération ou identité non reliée de façon forte au compte ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** routes REST/GraphQL, résolveurs, WebSocket, clés et événements API ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Faire inventaire des endpoints et versions ; vérifier permissions par objet/champ, quotas, schémas et messages. Rechercher spécialement : récupération ou identité non reliée de façon forte au compte.
5. **Prévention :** Schémas stricts, authentification, autorisation champ/objet, limites de taille/coût et gestion des versions. **Point spécifique :** Jetons de récupération aléatoires, hachés, uniques, à durée courte ; notification et révocation de session.
6. **Correction sécurisée :** Ajouter middleware serveur de validation, quotas et contrôle d’accès dans chaque résolveur/handler. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un lien expiré, réutilisé ou d’un autre compte ne fonctionne pas. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Catalogue API à jour, revue d’autorisations et métriques d’abus. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 083 — WebSocket Message Tampering

1. **Description / fonctionnement :** Transmet des messages WebSocket non autorisés ou altérés.
2. **Causes techniques :** Connexion ou message WS non authentifié/autorisé ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** routes REST/GraphQL, résolveurs, WebSocket, clés et événements API ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Faire inventaire des endpoints et versions ; vérifier permissions par objet/champ, quotas, schémas et messages. Rechercher spécialement : connexion ou message ws non authentifié/autorisé.
5. **Prévention :** Schémas stricts, authentification, autorisation champ/objet, limites de taille/coût et gestion des versions. **Point spécifique :** Vérifier Origin attendu, authentifier la connexion et autoriser chaque message côté serveur.
6. **Correction sécurisée :** Ajouter middleware serveur de validation, quotas et contrôle d’accès dans chaque résolveur/handler. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un client d’une autre origine ou d’un autre rôle ne peut pas exécuter un message sensible. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Catalogue API à jour, revue d’autorisations et métriques d’abus. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 084 — Shadow API Exploitation

1. **Description / fonctionnement :** Cible des routes API anciennes ou non inventoriées.
2. **Causes techniques :** API sans limites, contrôles d’identité, validation de schéma ou inventaire suffisant ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** routes REST/GraphQL, résolveurs, WebSocket, clés et événements API ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Faire inventaire des endpoints et versions ; vérifier permissions par objet/champ, quotas, schémas et messages. Rechercher spécialement : api sans limites, contrôles d’identité, validation de schéma ou inventaire suffisant.
5. **Prévention :** Schémas stricts, authentification, autorisation champ/objet, limites de taille/coût et gestion des versions. **Point spécifique :** ajouter middleware serveur de validation, quotas et contrôle d’accès dans chaque résolveur/handler
6. **Correction sécurisée :** Ajouter middleware serveur de validation, quotas et contrôle d’accès dans chaque résolveur/handler. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** tester réponses minimales, ressources appartenant à autrui, payloads surdimensionnés et versions dépréciées Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Catalogue API à jour, revue d’autorisations et métriques d’abus. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 085 — Deprecated API Exploitation

1. **Description / fonctionnement :** Profite des anciennes versions d'API non maintenues.
2. **Causes techniques :** API sans limites, contrôles d’identité, validation de schéma ou inventaire suffisant ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** routes REST/GraphQL, résolveurs, WebSocket, clés et événements API ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Faire inventaire des endpoints et versions ; vérifier permissions par objet/champ, quotas, schémas et messages. Rechercher spécialement : api sans limites, contrôles d’identité, validation de schéma ou inventaire suffisant.
5. **Prévention :** Schémas stricts, authentification, autorisation champ/objet, limites de taille/coût et gestion des versions. **Point spécifique :** ajouter middleware serveur de validation, quotas et contrôle d’accès dans chaque résolveur/handler
6. **Correction sécurisée :** Ajouter middleware serveur de validation, quotas et contrôle d’accès dans chaque résolveur/handler. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** tester réponses minimales, ressources appartenant à autrui, payloads surdimensionnés et versions dépréciées Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Catalogue API à jour, revue d’autorisations et métriques d’abus. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».
