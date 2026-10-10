# 01 — Injections

**Couverture :** 20 types d’attaque numérotés 1 à 20. Cet inventaire identifie des familles, variantes et scénarios ; certains termes se recoupent.

**Utilisation :** lire les profils liés à la surface attaquée. Les risques sont indicatifs et se recalculent selon exposition, impact, contrôle existant et vraisemblance. Ne pas effectuer de tests actifs sur des systèmes non autorisés.

## 001 — SQL Injection (SQLi)

1. **Description / fonctionnement :** Altère une requête SQL via une donnée contrôlée par un utilisateur.
2. **Causes techniques :** SQL concaténé depuis paramètres HTTP ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** requêtes SQL/NoSQL, shell, templates, sérialisation et exports ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Examiner les sources de paramètres et leur arrivée aux interpréteurs ; rechercher les concaténations et évaluer le comportement avec des données de test inoffensives. Rechercher spécialement : sql concaténé depuis paramètres http.
5. **Prévention :** Utiliser des API paramétrées, une allowlist de syntaxes et un encodage adapté au contexte. **Point spécifique :** Utiliser des requêtes préparées à paramètres liés ; jamais d’interpolation de valeurs SQL.
6. **Correction sécurisée :** Remplacer la construction dynamique risquée par des opérations typées/paramétrées ; réduire les privilèges de l’interpréteur. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Vérifier qu’une apostrophe dans un champ métier est stockée et relue sans modifier la requête. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Installer des règles de revue pour chaque point où une entrée devient une instruction. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 002 — Blind SQL Injection

1. **Description / fonctionnement :** Infère des résultats SQL sans affichage direct des données.
2. **Causes techniques :** SQL concaténé depuis paramètres HTTP ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** requêtes SQL/NoSQL, shell, templates, sérialisation et exports ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Examiner les sources de paramètres et leur arrivée aux interpréteurs ; rechercher les concaténations et évaluer le comportement avec des données de test inoffensives. Rechercher spécialement : sql concaténé depuis paramètres http.
5. **Prévention :** Utiliser des API paramétrées, une allowlist de syntaxes et un encodage adapté au contexte. **Point spécifique :** Utiliser des requêtes préparées à paramètres liés ; jamais d’interpolation de valeurs SQL.
6. **Correction sécurisée :** Remplacer la construction dynamique risquée par des opérations typées/paramétrées ; réduire les privilèges de l’interpréteur. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Vérifier qu’une apostrophe dans un champ métier est stockée et relue sans modifier la requête. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Installer des règles de revue pour chaque point où une entrée devient une instruction. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 003 — Time-Based SQL Injection

1. **Description / fonctionnement :** Infère l'état d'une requête SQL via le délai de réponse.
2. **Causes techniques :** SQL concaténé depuis paramètres HTTP ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** requêtes SQL/NoSQL, shell, templates, sérialisation et exports ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Examiner les sources de paramètres et leur arrivée aux interpréteurs ; rechercher les concaténations et évaluer le comportement avec des données de test inoffensives. Rechercher spécialement : sql concaténé depuis paramètres http.
5. **Prévention :** Utiliser des API paramétrées, une allowlist de syntaxes et un encodage adapté au contexte. **Point spécifique :** Utiliser des requêtes préparées à paramètres liés ; jamais d’interpolation de valeurs SQL.
6. **Correction sécurisée :** Remplacer la construction dynamique risquée par des opérations typées/paramétrées ; réduire les privilèges de l’interpréteur. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Vérifier qu’une apostrophe dans un champ métier est stockée et relue sans modifier la requête. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Installer des règles de revue pour chaque point où une entrée devient une instruction. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 004 — Error-Based SQL Injection

1. **Description / fonctionnement :** Exploite les détails d'erreur SQL exposés.
2. **Causes techniques :** SQL concaténé depuis paramètres HTTP ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** requêtes SQL/NoSQL, shell, templates, sérialisation et exports ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Examiner les sources de paramètres et leur arrivée aux interpréteurs ; rechercher les concaténations et évaluer le comportement avec des données de test inoffensives. Rechercher spécialement : sql concaténé depuis paramètres http.
5. **Prévention :** Utiliser des API paramétrées, une allowlist de syntaxes et un encodage adapté au contexte. **Point spécifique :** Utiliser des requêtes préparées à paramètres liés ; jamais d’interpolation de valeurs SQL.
6. **Correction sécurisée :** Remplacer la construction dynamique risquée par des opérations typées/paramétrées ; réduire les privilèges de l’interpréteur. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Vérifier qu’une apostrophe dans un champ métier est stockée et relue sans modifier la requête. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Installer des règles de revue pour chaque point où une entrée devient une instruction. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 005 — NoSQL Injection

1. **Description / fonctionnement :** Manipule un filtre ou opérateur d'une base NoSQL.
2. **Causes techniques :** Opérateurs BSON contrôlés par le client ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** requêtes SQL/NoSQL, shell, templates, sérialisation et exports ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Examiner les sources de paramètres et leur arrivée aux interpréteurs ; rechercher les concaténations et évaluer le comportement avec des données de test inoffensives. Rechercher spécialement : opérateurs bson contrôlés par le client.
5. **Prévention :** Utiliser des API paramétrées, une allowlist de syntaxes et un encodage adapté au contexte. **Point spécifique :** Accepter des types scalaires validés et construire les filtres côté serveur.
6. **Correction sécurisée :** Remplacer la construction dynamique risquée par des opérations typées/paramétrées ; réduire les privilèges de l’interpréteur. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Rejeter un filtre contenant des opérateurs inattendus, comme un objet à la place d’une chaîne. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Installer des règles de revue pour chaque point où une entrée devient une instruction. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 006 — Command Injection

1. **Description / fonctionnement :** Fait interpréter une entrée comme commande du système.
2. **Causes techniques :** Entrée transmise à un interpréteur ou exécuteur ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** requêtes SQL/NoSQL, shell, templates, sérialisation et exports ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Examiner les sources de paramètres et leur arrivée aux interpréteurs ; rechercher les concaténations et évaluer le comportement avec des données de test inoffensives. Rechercher spécialement : entrée transmise à un interpréteur ou exécuteur.
5. **Prévention :** Utiliser des API paramétrées, une allowlist de syntaxes et un encodage adapté au contexte. **Point spécifique :** Éviter l’interpréteur ; employer des API dédiées, arguments séparés et listes autorisées.
6. **Correction sécurisée :** Remplacer la construction dynamique risquée par des opérations typées/paramétrées ; réduire les privilèges de l’interpréteur. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un nom de fichier avec caractères spéciaux ne doit jamais déclencher de commande. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Installer des règles de revue pour chaque point où une entrée devient une instruction. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 007 — Code Injection

1. **Description / fonctionnement :** Introduit une donnée interprétée comme code exécutable.
2. **Causes techniques :** Entrée transmise à un interpréteur ou exécuteur ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** requêtes SQL/NoSQL, shell, templates, sérialisation et exports ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Examiner les sources de paramètres et leur arrivée aux interpréteurs ; rechercher les concaténations et évaluer le comportement avec des données de test inoffensives. Rechercher spécialement : entrée transmise à un interpréteur ou exécuteur.
5. **Prévention :** Utiliser des API paramétrées, une allowlist de syntaxes et un encodage adapté au contexte. **Point spécifique :** Éviter l’interpréteur ; employer des API dédiées, arguments séparés et listes autorisées.
6. **Correction sécurisée :** Remplacer la construction dynamique risquée par des opérations typées/paramétrées ; réduire les privilèges de l’interpréteur. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un nom de fichier avec caractères spéciaux ne doit jamais déclencher de commande. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Installer des règles de revue pour chaque point où une entrée devient une instruction. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 008 — LDAP Injection

1. **Description / fonctionnement :** Modifie la logique d'un filtre LDAP.
2. **Causes techniques :** Expression de recherche construite par interpolation ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** requêtes SQL/NoSQL, shell, templates, sérialisation et exports ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Examiner les sources de paramètres et leur arrivée aux interpréteurs ; rechercher les concaténations et évaluer le comportement avec des données de test inoffensives. Rechercher spécialement : expression de recherche construite par interpolation.
5. **Prévention :** Utiliser des API paramétrées, une allowlist de syntaxes et un encodage adapté au contexte. **Point spécifique :** Utiliser la construction de filtres sûre, échapper correctement et limiter les expressions.
6. **Correction sécurisée :** Remplacer la construction dynamique risquée par des opérations typées/paramétrées ; réduire les privilèges de l’interpréteur. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une valeur contenant des métacaractères reste une valeur littérale. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Installer des règles de revue pour chaque point où une entrée devient une instruction. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 009 — XPath Injection

1. **Description / fonctionnement :** Détourne une expression XPath construite sans protection.
2. **Causes techniques :** Expression de recherche construite par interpolation ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** requêtes SQL/NoSQL, shell, templates, sérialisation et exports ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Examiner les sources de paramètres et leur arrivée aux interpréteurs ; rechercher les concaténations et évaluer le comportement avec des données de test inoffensives. Rechercher spécialement : expression de recherche construite par interpolation.
5. **Prévention :** Utiliser des API paramétrées, une allowlist de syntaxes et un encodage adapté au contexte. **Point spécifique :** Utiliser la construction de filtres sûre, échapper correctement et limiter les expressions.
6. **Correction sécurisée :** Remplacer la construction dynamique risquée par des opérations typées/paramétrées ; réduire les privilèges de l’interpréteur. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une valeur contenant des métacaractères reste une valeur littérale. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Installer des règles de revue pour chaque point où une entrée devient une instruction. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 010 — XML Injection

1. **Description / fonctionnement :** Injecte une structure XML inattendue dans un traitement.
2. **Causes techniques :** Parseur XML acceptant DTD et entités externes ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** requêtes SQL/NoSQL, shell, templates, sérialisation et exports ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Examiner les sources de paramètres et leur arrivée aux interpréteurs ; rechercher les concaténations et évaluer le comportement avec des données de test inoffensives. Rechercher spécialement : parseur xml acceptant dtd et entités externes.
5. **Prévention :** Utiliser des API paramétrées, une allowlist de syntaxes et un encodage adapté au contexte. **Point spécifique :** Désactiver DTD, entités externes et accès réseau du parseur XML.
6. **Correction sécurisée :** Remplacer la construction dynamique risquée par des opérations typées/paramétrées ; réduire les privilèges de l’interpréteur. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un XML de test avec déclaration d’entité externe est refusé sans requête réseau. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Installer des règles de revue pour chaque point où une entrée devient une instruction. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 011 — XXE Injection

1. **Description / fonctionnement :** Abuse d'entités externes lors du traitement XML.
2. **Causes techniques :** Parseur XML acceptant DTD et entités externes ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** requêtes SQL/NoSQL, shell, templates, sérialisation et exports ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Examiner les sources de paramètres et leur arrivée aux interpréteurs ; rechercher les concaténations et évaluer le comportement avec des données de test inoffensives. Rechercher spécialement : parseur xml acceptant dtd et entités externes.
5. **Prévention :** Utiliser des API paramétrées, une allowlist de syntaxes et un encodage adapté au contexte. **Point spécifique :** Désactiver DTD, entités externes et accès réseau du parseur XML.
6. **Correction sécurisée :** Remplacer la construction dynamique risquée par des opérations typées/paramétrées ; réduire les privilèges de l’interpréteur. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un XML de test avec déclaration d’entité externe est refusé sans requête réseau. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Installer des règles de revue pour chaque point où une entrée devient une instruction. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 012 — SSTI

1. **Description / fonctionnement :** Exécute des expressions non fiables dans un moteur de templates serveur.
2. **Causes techniques :** Chaîne non fiable utilisée comme source de template ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** requêtes SQL/NoSQL, shell, templates, sérialisation et exports ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Examiner les sources de paramètres et leur arrivée aux interpréteurs ; rechercher les concaténations et évaluer le comportement avec des données de test inoffensives. Rechercher spécialement : chaîne non fiable utilisée comme source de template.
5. **Prévention :** Utiliser des API paramétrées, une allowlist de syntaxes et un encodage adapté au contexte. **Point spécifique :** Conserver des templates fixes et ne passer les entrées que comme variables de rendu.
6. **Correction sécurisée :** Remplacer la construction dynamique risquée par des opérations typées/paramétrées ; réduire les privilèges de l’interpréteur. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un texte avec syntaxe de template reste une valeur textuelle. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Installer des règles de revue pour chaque point où une entrée devient une instruction. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 013 — HTML Injection

1. **Description / fonctionnement :** Introduit du balisage actif dans une page.
2. **Causes techniques :** Source non fiable injectée dans un contexte navigateur actif ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** requêtes SQL/NoSQL, shell, templates, sérialisation et exports ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Examiner les sources de paramètres et leur arrivée aux interpréteurs ; rechercher les concaténations et évaluer le comportement avec des données de test inoffensives. Rechercher spécialement : source non fiable injectée dans un contexte navigateur actif.
5. **Prévention :** Utiliser des API paramétrées, une allowlist de syntaxes et un encodage adapté au contexte. **Point spécifique :** Employer échappement contextuel, DOM textContent, clés d’objet sûres et sanitizer maintenu si HTML requis.
6. **Correction sécurisée :** Remplacer la construction dynamique risquée par des opérations typées/paramétrées ; réduire les privilèges de l’interpréteur. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Les caractères HTML/JS de test restent inertes ; les propriétés de prototype ne changent pas. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Installer des règles de revue pour chaque point où une entrée devient une instruction. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 014 — CSS Injection

1. **Description / fonctionnement :** Injecte des règles CSS ou valeurs de style non fiables.
2. **Causes techniques :** Valeur CSS arbitraire non vérifiée ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** requêtes SQL/NoSQL, shell, templates, sérialisation et exports ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Examiner les sources de paramètres et leur arrivée aux interpréteurs ; rechercher les concaténations et évaluer le comportement avec des données de test inoffensives. Rechercher spécialement : valeur css arbitraire non vérifiée.
5. **Prévention :** Utiliser des API paramétrées, une allowlist de syntaxes et un encodage adapté au contexte. **Point spécifique :** Utiliser des classes de style prédéfinies ou une allowlist de valeurs CSS.
6. **Correction sécurisée :** Remplacer la construction dynamique risquée par des opérations typées/paramétrées ; réduire les privilèges de l’interpréteur. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une valeur de style hors allowlist est rejetée sans modification des styles critiques. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Installer des règles de revue pour chaque point où une entrée devient une instruction. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 015 — CRLF Injection

1. **Description / fonctionnement :** Injecte des séparateurs de ligne dans les protocoles texte.
2. **Causes techniques :** En-têtes composés depuis une entrée non normalisée ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** requêtes SQL/NoSQL, shell, templates, sérialisation et exports ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Examiner les sources de paramètres et leur arrivée aux interpréteurs ; rechercher les concaténations et évaluer le comportement avec des données de test inoffensives. Rechercher spécialement : en-têtes composés depuis une entrée non normalisée.
5. **Prévention :** Utiliser des API paramétrées, une allowlist de syntaxes et un encodage adapté au contexte. **Point spécifique :** Interdire CR/LF dans les champs d’en-tête, valider les noms d’hôtes et normaliser.
6. **Correction sécurisée :** Remplacer la construction dynamique risquée par des opérations typées/paramétrées ; réduire les privilèges de l’interpréteur. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une donnée contenant des retours à la ligne ne crée pas de nouvel en-tête. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Installer des règles de revue pour chaque point où une entrée devient une instruction. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 016 — HTTP Header Injection

1. **Description / fonctionnement :** Manipule la composition des en-têtes HTTP.
2. **Causes techniques :** En-têtes composés depuis une entrée non normalisée ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** requêtes SQL/NoSQL, shell, templates, sérialisation et exports ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Examiner les sources de paramètres et leur arrivée aux interpréteurs ; rechercher les concaténations et évaluer le comportement avec des données de test inoffensives. Rechercher spécialement : en-têtes composés depuis une entrée non normalisée.
5. **Prévention :** Utiliser des API paramétrées, une allowlist de syntaxes et un encodage adapté au contexte. **Point spécifique :** Interdire CR/LF dans les champs d’en-tête, valider les noms d’hôtes et normaliser.
6. **Correction sécurisée :** Remplacer la construction dynamique risquée par des opérations typées/paramétrées ; réduire les privilèges de l’interpréteur. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une donnée contenant des retours à la ligne ne crée pas de nouvel en-tête. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Installer des règles de revue pour chaque point où une entrée devient une instruction. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 017 — Email Header Injection

1. **Description / fonctionnement :** Insère de faux champs dans les en-têtes d'e-mail.
2. **Causes techniques :** En-têtes composés depuis une entrée non normalisée ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** requêtes SQL/NoSQL, shell, templates, sérialisation et exports ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Examiner les sources de paramètres et leur arrivée aux interpréteurs ; rechercher les concaténations et évaluer le comportement avec des données de test inoffensives. Rechercher spécialement : en-têtes composés depuis une entrée non normalisée.
5. **Prévention :** Utiliser des API paramétrées, une allowlist de syntaxes et un encodage adapté au contexte. **Point spécifique :** Interdire CR/LF dans les champs d’en-tête, valider les noms d’hôtes et normaliser.
6. **Correction sécurisée :** Remplacer la construction dynamique risquée par des opérations typées/paramétrées ; réduire les privilèges de l’interpréteur. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une donnée contenant des retours à la ligne ne crée pas de nouvel en-tête. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Installer des règles de revue pour chaque point où une entrée devient une instruction. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 018 — CSV / Formula Injection

1. **Description / fonctionnement :** Fait interpréter des cellules exportées comme formules.
2. **Causes techniques :** Export de cellules non échappées vers un tableur ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** requêtes SQL/NoSQL, shell, templates, sérialisation et exports ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Examiner les sources de paramètres et leur arrivée aux interpréteurs ; rechercher les concaténations et évaluer le comportement avec des données de test inoffensives. Rechercher spécialement : export de cellules non échappées vers un tableur.
5. **Prévention :** Utiliser des API paramétrées, une allowlist de syntaxes et un encodage adapté au contexte. **Point spécifique :** Neutraliser les cellules commençant par =, +, -, @ selon format et compatibilité visée.
6. **Correction sécurisée :** Remplacer la construction dynamique risquée par des opérations typées/paramétrées ; réduire les privilèges de l’interpréteur. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une valeur de test commençant par = s’ouvre comme texte et non comme formule. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Installer des règles de revue pour chaque point où une entrée devient une instruction. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 019 — GraphQL Injection

1. **Description / fonctionnement :** Exploit de la construction non fiable des requêtes ou résolveurs GraphQL.
2. **Causes techniques :** Complexité ou schéma API insuffisamment borné ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** requêtes SQL/NoSQL, shell, templates, sérialisation et exports ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Examiner les sources de paramètres et leur arrivée aux interpréteurs ; rechercher les concaténations et évaluer le comportement avec des données de test inoffensives. Rechercher spécialement : complexité ou schéma api insuffisamment borné.
5. **Prévention :** Utiliser des API paramétrées, une allowlist de syntaxes et un encodage adapté au contexte. **Point spécifique :** Limiter profondeur, complexité, taille, pagination et introspection selon menace.
6. **Correction sécurisée :** Remplacer la construction dynamique risquée par des opérations typées/paramétrées ; réduire les privilèges de l’interpréteur. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une requête profonde ou volumineuse dépasse le quota et reçoit un refus contrôlé. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Installer des règles de revue pour chaque point où une entrée devient une instruction. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 020 — Server-Side JavaScript Injection

1. **Description / fonctionnement :** Provoque l'interprétation JavaScript d'une entrée côté serveur.
2. **Causes techniques :** Entrée transmise à un interpréteur ou exécuteur ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** requêtes SQL/NoSQL, shell, templates, sérialisation et exports ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Examiner les sources de paramètres et leur arrivée aux interpréteurs ; rechercher les concaténations et évaluer le comportement avec des données de test inoffensives. Rechercher spécialement : entrée transmise à un interpréteur ou exécuteur.
5. **Prévention :** Utiliser des API paramétrées, une allowlist de syntaxes et un encodage adapté au contexte. **Point spécifique :** Éviter l’interpréteur ; employer des API dédiées, arguments séparés et listes autorisées.
6. **Correction sécurisée :** Remplacer la construction dynamique risquée par des opérations typées/paramétrées ; réduire les privilèges de l’interpréteur. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un nom de fichier avec caractères spéciaux ne doit jamais déclencher de commande. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Installer des règles de revue pour chaque point où une entrée devient une instruction. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».
