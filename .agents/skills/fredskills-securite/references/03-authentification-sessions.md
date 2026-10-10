# 03 — Authentification et sessions

**Couverture :** 23 types d’attaque numérotés 33 à 55. Cet inventaire identifie des familles, variantes et scénarios ; certains termes se recoupent.

**Utilisation :** lire les profils liés à la surface attaquée. Les risques sont indicatifs et se recalculent selon exposition, impact, contrôle existant et vraisemblance. Ne pas effectuer de tests actifs sur des systèmes non autorisés.

## 033 — Brute Force

1. **Description / fonctionnement :** Essais répétés d'authentifiants pour obtenir un accès.
2. **Causes techniques :** Essais illimités et détection d’anomalies absente ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** inscription, connexion, récupération, MFA, OAuth/OIDC, SAML, JWT et cookies ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier tous les parcours de connexion/récupération ; examiner signatures, limites d’essais et états de session. Rechercher spécialement : essais illimités et détection d’anomalies absente.
5. **Prévention :** MFA approprié, vérification cryptographique stricte, ralentissement progressif, secrets robustes et cookies sécurisés. **Point spécifique :** Ajouter limites IP/compte, délai progressif, surveillance et MFA.
6. **Correction sécurisée :** Centraliser l’authentification côté serveur ; invalider anciens jetons et imposer les contrôles à chaque point d’entrée. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Des tentatives de test répétées entraînent une restriction sans bloquer indûment un compte légitime. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Journaliser les événements sensibles sans secrets, faire tourner les jetons et réévaluer les risques. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 034 — Dictionary Attack

1. **Description / fonctionnement :** Essais de mots de passe tirés d'un dictionnaire.
2. **Causes techniques :** Essais illimités et détection d’anomalies absente ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** inscription, connexion, récupération, MFA, OAuth/OIDC, SAML, JWT et cookies ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier tous les parcours de connexion/récupération ; examiner signatures, limites d’essais et états de session. Rechercher spécialement : essais illimités et détection d’anomalies absente.
5. **Prévention :** MFA approprié, vérification cryptographique stricte, ralentissement progressif, secrets robustes et cookies sécurisés. **Point spécifique :** Ajouter limites IP/compte, délai progressif, surveillance et MFA.
6. **Correction sécurisée :** Centraliser l’authentification côté serveur ; invalider anciens jetons et imposer les contrôles à chaque point d’entrée. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Des tentatives de test répétées entraînent une restriction sans bloquer indûment un compte légitime. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Journaliser les événements sensibles sans secrets, faire tourner les jetons et réévaluer les risques. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 035 — Credential Stuffing

1. **Description / fonctionnement :** Réutilise des identifiants compromis sur d'autres services.
2. **Causes techniques :** Essais illimités et détection d’anomalies absente ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** inscription, connexion, récupération, MFA, OAuth/OIDC, SAML, JWT et cookies ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier tous les parcours de connexion/récupération ; examiner signatures, limites d’essais et états de session. Rechercher spécialement : essais illimités et détection d’anomalies absente.
5. **Prévention :** MFA approprié, vérification cryptographique stricte, ralentissement progressif, secrets robustes et cookies sécurisés. **Point spécifique :** Ajouter limites IP/compte, délai progressif, surveillance et MFA.
6. **Correction sécurisée :** Centraliser l’authentification côté serveur ; invalider anciens jetons et imposer les contrôles à chaque point d’entrée. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Des tentatives de test répétées entraînent une restriction sans bloquer indûment un compte légitime. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Journaliser les événements sensibles sans secrets, faire tourner les jetons et réévaluer les risques. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 036 — Password Spraying

1. **Description / fonctionnement :** Teste des secrets fréquents sur de nombreux comptes.
2. **Causes techniques :** Essais illimités et détection d’anomalies absente ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** inscription, connexion, récupération, MFA, OAuth/OIDC, SAML, JWT et cookies ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier tous les parcours de connexion/récupération ; examiner signatures, limites d’essais et états de session. Rechercher spécialement : essais illimités et détection d’anomalies absente.
5. **Prévention :** MFA approprié, vérification cryptographique stricte, ralentissement progressif, secrets robustes et cookies sécurisés. **Point spécifique :** Ajouter limites IP/compte, délai progressif, surveillance et MFA.
6. **Correction sécurisée :** Centraliser l’authentification côté serveur ; invalider anciens jetons et imposer les contrôles à chaque point d’entrée. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Des tentatives de test répétées entraînent une restriction sans bloquer indûment un compte légitime. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Journaliser les événements sensibles sans secrets, faire tourner les jetons et réévaluer les risques. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 037 — Account Enumeration

1. **Description / fonctionnement :** Révèle si un identifiant est enregistré.
2. **Causes techniques :** Réponses distinctes selon existence du compte ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** inscription, connexion, récupération, MFA, OAuth/OIDC, SAML, JWT et cookies ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier tous les parcours de connexion/récupération ; examiner signatures, limites d’essais et états de session. Rechercher spécialement : réponses distinctes selon existence du compte.
5. **Prévention :** MFA approprié, vérification cryptographique stricte, ralentissement progressif, secrets robustes et cookies sécurisés. **Point spécifique :** Utiliser des messages de connexion et récupération équivalents avec temporisation raisonnable.
6. **Correction sécurisée :** Centraliser l’authentification côté serveur ; invalider anciens jetons et imposer les contrôles à chaque point d’entrée. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un compte inexistant et un compte existant produisent des réponses indistinguables. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Journaliser les événements sensibles sans secrets, faire tourner les jetons et réévaluer les risques. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 038 — Authentication Bypass

1. **Description / fonctionnement :** Contourne une vérification d'identité.
2. **Causes techniques :** Récupération ou identité non reliée de façon forte au compte ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** inscription, connexion, récupération, MFA, OAuth/OIDC, SAML, JWT et cookies ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier tous les parcours de connexion/récupération ; examiner signatures, limites d’essais et états de session. Rechercher spécialement : récupération ou identité non reliée de façon forte au compte.
5. **Prévention :** MFA approprié, vérification cryptographique stricte, ralentissement progressif, secrets robustes et cookies sécurisés. **Point spécifique :** Jetons de récupération aléatoires, hachés, uniques, à durée courte ; notification et révocation de session.
6. **Correction sécurisée :** Centraliser l’authentification côté serveur ; invalider anciens jetons et imposer les contrôles à chaque point d’entrée. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un lien expiré, réutilisé ou d’un autre compte ne fonctionne pas. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Journaliser les événements sensibles sans secrets, faire tourner les jetons et réévaluer les risques. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 039 — MFA Bypass

1. **Description / fonctionnement :** Contourne l'étape multifacteur.
2. **Causes techniques :** Facteur insuffisamment lié à une opération, tentatives non limitées ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** inscription, connexion, récupération, MFA, OAuth/OIDC, SAML, JWT et cookies ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier tous les parcours de connexion/récupération ; examiner signatures, limites d’essais et états de session. Rechercher spécialement : facteur insuffisamment lié à une opération, tentatives non limitées.
5. **Prévention :** MFA approprié, vérification cryptographique stricte, ralentissement progressif, secrets robustes et cookies sécurisés. **Point spécifique :** Imposer MFA serveur sur parcours sensibles et codes courts à usage unique, expirants et limités.
6. **Correction sécurisée :** Centraliser l’authentification côté serveur ; invalider anciens jetons et imposer les contrôles à chaque point d’entrée. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un code expiré, déjà utilisé ou hors tentative est rejeté. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Journaliser les événements sensibles sans secrets, faire tourner les jetons et réévaluer les risques. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 040 — MFA Fatigue

1. **Description / fonctionnement :** Déclenche trop de notifications MFA pour obtenir une acceptation.
2. **Causes techniques :** Facteur insuffisamment lié à une opération, tentatives non limitées ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** inscription, connexion, récupération, MFA, OAuth/OIDC, SAML, JWT et cookies ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier tous les parcours de connexion/récupération ; examiner signatures, limites d’essais et états de session. Rechercher spécialement : facteur insuffisamment lié à une opération, tentatives non limitées.
5. **Prévention :** MFA approprié, vérification cryptographique stricte, ralentissement progressif, secrets robustes et cookies sécurisés. **Point spécifique :** Imposer MFA serveur sur parcours sensibles et codes courts à usage unique, expirants et limités.
6. **Correction sécurisée :** Centraliser l’authentification côté serveur ; invalider anciens jetons et imposer les contrôles à chaque point d’entrée. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un code expiré, déjà utilisé ou hors tentative est rejeté. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Journaliser les événements sensibles sans secrets, faire tourner les jetons et réévaluer les risques. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 041 — OTP Brute Force

1. **Description / fonctionnement :** Devine des codes à usage unique par essais.
2. **Causes techniques :** Facteur insuffisamment lié à une opération, tentatives non limitées ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** inscription, connexion, récupération, MFA, OAuth/OIDC, SAML, JWT et cookies ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier tous les parcours de connexion/récupération ; examiner signatures, limites d’essais et états de session. Rechercher spécialement : facteur insuffisamment lié à une opération, tentatives non limitées.
5. **Prévention :** MFA approprié, vérification cryptographique stricte, ralentissement progressif, secrets robustes et cookies sécurisés. **Point spécifique :** Imposer MFA serveur sur parcours sensibles et codes courts à usage unique, expirants et limités.
6. **Correction sécurisée :** Centraliser l’authentification côté serveur ; invalider anciens jetons et imposer les contrôles à chaque point d’entrée. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un code expiré, déjà utilisé ou hors tentative est rejeté. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Journaliser les événements sensibles sans secrets, faire tourner les jetons et réévaluer les risques. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 042 — Password Reset Poisoning

1. **Description / fonctionnement :** Modifie le lien ou destinataire d'une récupération de compte.
2. **Causes techniques :** Récupération ou identité non reliée de façon forte au compte ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** inscription, connexion, récupération, MFA, OAuth/OIDC, SAML, JWT et cookies ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier tous les parcours de connexion/récupération ; examiner signatures, limites d’essais et états de session. Rechercher spécialement : récupération ou identité non reliée de façon forte au compte.
5. **Prévention :** MFA approprié, vérification cryptographique stricte, ralentissement progressif, secrets robustes et cookies sécurisés. **Point spécifique :** Jetons de récupération aléatoires, hachés, uniques, à durée courte ; notification et révocation de session.
6. **Correction sécurisée :** Centraliser l’authentification côté serveur ; invalider anciens jetons et imposer les contrôles à chaque point d’entrée. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un lien expiré, réutilisé ou d’un autre compte ne fonctionne pas. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Journaliser les événements sensibles sans secrets, faire tourner les jetons et réévaluer les risques. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 043 — Password Reset Token Theft

1. **Description / fonctionnement :** Soustrait un jeton de récupération valide.
2. **Causes techniques :** Secrets persistants ou transmis à un mauvais destinataire ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** inscription, connexion, récupération, MFA, OAuth/OIDC, SAML, JWT et cookies ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier tous les parcours de connexion/récupération ; examiner signatures, limites d’essais et états de session. Rechercher spécialement : secrets persistants ou transmis à un mauvais destinataire.
5. **Prévention :** MFA approprié, vérification cryptographique stricte, ralentissement progressif, secrets robustes et cookies sécurisés. **Point spécifique :** Stocker en gestionnaire de secrets, réduire la portée et effectuer rotation et révocation.
6. **Correction sécurisée :** Centraliser l’authentification côté serveur ; invalider anciens jetons et imposer les contrôles à chaque point d’entrée. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Clés invalides ou retirées ne fonctionnent plus ; aucun secret dans logs et réponses. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Journaliser les événements sensibles sans secrets, faire tourner les jetons et réévaluer les risques. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 044 — Account Takeover (ATO)

1. **Description / fonctionnement :** Obtient le contrôle du compte d'un utilisateur.
2. **Causes techniques :** Récupération ou identité non reliée de façon forte au compte ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** inscription, connexion, récupération, MFA, OAuth/OIDC, SAML, JWT et cookies ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier tous les parcours de connexion/récupération ; examiner signatures, limites d’essais et états de session. Rechercher spécialement : récupération ou identité non reliée de façon forte au compte.
5. **Prévention :** MFA approprié, vérification cryptographique stricte, ralentissement progressif, secrets robustes et cookies sécurisés. **Point spécifique :** Jetons de récupération aléatoires, hachés, uniques, à durée courte ; notification et révocation de session.
6. **Correction sécurisée :** Centraliser l’authentification côté serveur ; invalider anciens jetons et imposer les contrôles à chaque point d’entrée. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un lien expiré, réutilisé ou d’un autre compte ne fonctionne pas. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Journaliser les événements sensibles sans secrets, faire tourner les jetons et réévaluer les risques. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 045 — Session Fixation

1. **Description / fonctionnement :** Impose un identifiant de session avant connexion.
2. **Causes techniques :** Session réutilisable ou cookie sans attributs adaptés ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** inscription, connexion, récupération, MFA, OAuth/OIDC, SAML, JWT et cookies ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier tous les parcours de connexion/récupération ; examiner signatures, limites d’essais et états de session. Rechercher spécialement : session réutilisable ou cookie sans attributs adaptés.
5. **Prévention :** MFA approprié, vérification cryptographique stricte, ralentissement progressif, secrets robustes et cookies sécurisés. **Point spécifique :** Renouveler ID après login, expirer/révoquer côté serveur, cookies Secure/HttpOnly/SameSite, TLS.
6. **Correction sécurisée :** Centraliser l’authentification côté serveur ; invalider anciens jetons et imposer les contrôles à chaque point d’entrée. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Après logout et renouvellement, une ancienne session ne permet plus d’accès. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Journaliser les événements sensibles sans secrets, faire tourner les jetons et réévaluer les risques. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 046 — Session Hijacking

1. **Description / fonctionnement :** Détourne une session active.
2. **Causes techniques :** Session réutilisable ou cookie sans attributs adaptés ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** inscription, connexion, récupération, MFA, OAuth/OIDC, SAML, JWT et cookies ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier tous les parcours de connexion/récupération ; examiner signatures, limites d’essais et états de session. Rechercher spécialement : session réutilisable ou cookie sans attributs adaptés.
5. **Prévention :** MFA approprié, vérification cryptographique stricte, ralentissement progressif, secrets robustes et cookies sécurisés. **Point spécifique :** Renouveler ID après login, expirer/révoquer côté serveur, cookies Secure/HttpOnly/SameSite, TLS.
6. **Correction sécurisée :** Centraliser l’authentification côté serveur ; invalider anciens jetons et imposer les contrôles à chaque point d’entrée. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Après logout et renouvellement, une ancienne session ne permet plus d’accès. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Journaliser les événements sensibles sans secrets, faire tourner les jetons et réévaluer les risques. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 047 — Session Replay

1. **Description / fonctionnement :** Réutilise un artefact d'authentification intercepté.
2. **Causes techniques :** Session réutilisable ou cookie sans attributs adaptés ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** inscription, connexion, récupération, MFA, OAuth/OIDC, SAML, JWT et cookies ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier tous les parcours de connexion/récupération ; examiner signatures, limites d’essais et états de session. Rechercher spécialement : session réutilisable ou cookie sans attributs adaptés.
5. **Prévention :** MFA approprié, vérification cryptographique stricte, ralentissement progressif, secrets robustes et cookies sécurisés. **Point spécifique :** Renouveler ID après login, expirer/révoquer côté serveur, cookies Secure/HttpOnly/SameSite, TLS.
6. **Correction sécurisée :** Centraliser l’authentification côté serveur ; invalider anciens jetons et imposer les contrôles à chaque point d’entrée. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Après logout et renouvellement, une ancienne session ne permet plus d’accès. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Journaliser les événements sensibles sans secrets, faire tourner les jetons et réévaluer les risques. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 048 — Cookie Theft

1. **Description / fonctionnement :** Extrait et réutilise un cookie sensible.
2. **Causes techniques :** Session réutilisable ou cookie sans attributs adaptés ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** inscription, connexion, récupération, MFA, OAuth/OIDC, SAML, JWT et cookies ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier tous les parcours de connexion/récupération ; examiner signatures, limites d’essais et états de session. Rechercher spécialement : session réutilisable ou cookie sans attributs adaptés.
5. **Prévention :** MFA approprié, vérification cryptographique stricte, ralentissement progressif, secrets robustes et cookies sécurisés. **Point spécifique :** Renouveler ID après login, expirer/révoquer côté serveur, cookies Secure/HttpOnly/SameSite, TLS.
6. **Correction sécurisée :** Centraliser l’authentification côté serveur ; invalider anciens jetons et imposer les contrôles à chaque point d’entrée. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Après logout et renouvellement, une ancienne session ne permet plus d’accès. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Journaliser les événements sensibles sans secrets, faire tourner les jetons et réévaluer les risques. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 049 — JWT Forgery

1. **Description / fonctionnement :** Exploite une validation de signature JWT défaillante.
2. **Causes techniques :** Claims, algorithme ou signature non vérifiés rigoureusement ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** inscription, connexion, récupération, MFA, OAuth/OIDC, SAML, JWT et cookies ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier tous les parcours de connexion/récupération ; examiner signatures, limites d’essais et états de session. Rechercher spécialement : claims, algorithme ou signature non vérifiés rigoureusement.
5. **Prévention :** MFA approprié, vérification cryptographique stricte, ralentissement progressif, secrets robustes et cookies sécurisés. **Point spécifique :** Imposer algorithme autorisé, signature, issuer, audience, dates et rotation des clés.
6. **Correction sécurisée :** Centraliser l’authentification côté serveur ; invalider anciens jetons et imposer les contrôles à chaque point d’entrée. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un JWT altéré, expiré, mauvaise audience ou mauvais algorithme est rejeté. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Journaliser les événements sensibles sans secrets, faire tourner les jetons et réévaluer les risques. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 050 — JWT Algorithm Confusion

1. **Description / fonctionnement :** Profite d'une confusion entre algorithmes de validation JWT.
2. **Causes techniques :** Claims, algorithme ou signature non vérifiés rigoureusement ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** inscription, connexion, récupération, MFA, OAuth/OIDC, SAML, JWT et cookies ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier tous les parcours de connexion/récupération ; examiner signatures, limites d’essais et états de session. Rechercher spécialement : claims, algorithme ou signature non vérifiés rigoureusement.
5. **Prévention :** MFA approprié, vérification cryptographique stricte, ralentissement progressif, secrets robustes et cookies sécurisés. **Point spécifique :** Imposer algorithme autorisé, signature, issuer, audience, dates et rotation des clés.
6. **Correction sécurisée :** Centraliser l’authentification côté serveur ; invalider anciens jetons et imposer les contrôles à chaque point d’entrée. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un JWT altéré, expiré, mauvaise audience ou mauvais algorithme est rejeté. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Journaliser les événements sensibles sans secrets, faire tourner les jetons et réévaluer les risques. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 051 — OAuth Misconfiguration

1. **Description / fonctionnement :** Exploite un flux OAuth insuffisamment sécurisé.
2. **Causes techniques :** Flux fédéré mal lié à l’état et à l’identité attendus ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** inscription, connexion, récupération, MFA, OAuth/OIDC, SAML, JWT et cookies ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier tous les parcours de connexion/récupération ; examiner signatures, limites d’essais et états de session. Rechercher spécialement : flux fédéré mal lié à l’état et à l’identité attendus.
5. **Prévention :** MFA approprié, vérification cryptographique stricte, ralentissement progressif, secrets robustes et cookies sécurisés. **Point spécifique :** PKCE/state/nonce adaptés, URI redirect exactes et validation cryptographique issuer/audience/signature.
6. **Correction sécurisée :** Centraliser l’authentification côté serveur ; invalider anciens jetons et imposer les contrôles à chaque point d’entrée. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un state erroné, une audience étrangère et un callback modifié sont refusés. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Journaliser les événements sensibles sans secrets, faire tourner les jetons et réévaluer les risques. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 052 — OAuth Account Linking Attack

1. **Description / fonctionnement :** Relie frauduleusement un compte fédéré à un compte local.
2. **Causes techniques :** Flux fédéré mal lié à l’état et à l’identité attendus ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** inscription, connexion, récupération, MFA, OAuth/OIDC, SAML, JWT et cookies ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier tous les parcours de connexion/récupération ; examiner signatures, limites d’essais et états de session. Rechercher spécialement : flux fédéré mal lié à l’état et à l’identité attendus.
5. **Prévention :** MFA approprié, vérification cryptographique stricte, ralentissement progressif, secrets robustes et cookies sécurisés. **Point spécifique :** PKCE/state/nonce adaptés, URI redirect exactes et validation cryptographique issuer/audience/signature.
6. **Correction sécurisée :** Centraliser l’authentification côté serveur ; invalider anciens jetons et imposer les contrôles à chaque point d’entrée. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un state erroné, une audience étrangère et un callback modifié sont refusés. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Journaliser les événements sensibles sans secrets, faire tourner les jetons et réévaluer les risques. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 053 — OpenID Connect Misconfiguration

1. **Description / fonctionnement :** Exploite une validation OIDC incomplète.
2. **Causes techniques :** Flux fédéré mal lié à l’état et à l’identité attendus ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** inscription, connexion, récupération, MFA, OAuth/OIDC, SAML, JWT et cookies ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier tous les parcours de connexion/récupération ; examiner signatures, limites d’essais et états de session. Rechercher spécialement : flux fédéré mal lié à l’état et à l’identité attendus.
5. **Prévention :** MFA approprié, vérification cryptographique stricte, ralentissement progressif, secrets robustes et cookies sécurisés. **Point spécifique :** PKCE/state/nonce adaptés, URI redirect exactes et validation cryptographique issuer/audience/signature.
6. **Correction sécurisée :** Centraliser l’authentification côté serveur ; invalider anciens jetons et imposer les contrôles à chaque point d’entrée. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un state erroné, une audience étrangère et un callback modifié sont refusés. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Journaliser les événements sensibles sans secrets, faire tourner les jetons et réévaluer les risques. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 054 — SAML Signature Wrapping

1. **Description / fonctionnement :** Présente une assertion SAML hors de la zone effectivement signée.
2. **Causes techniques :** Flux fédéré mal lié à l’état et à l’identité attendus ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** inscription, connexion, récupération, MFA, OAuth/OIDC, SAML, JWT et cookies ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier tous les parcours de connexion/récupération ; examiner signatures, limites d’essais et états de session. Rechercher spécialement : flux fédéré mal lié à l’état et à l’identité attendus.
5. **Prévention :** MFA approprié, vérification cryptographique stricte, ralentissement progressif, secrets robustes et cookies sécurisés. **Point spécifique :** PKCE/state/nonce adaptés, URI redirect exactes et validation cryptographique issuer/audience/signature.
6. **Correction sécurisée :** Centraliser l’authentification côté serveur ; invalider anciens jetons et imposer les contrôles à chaque point d’entrée. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un state erroné, une audience étrangère et un callback modifié sont refusés. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Journaliser les événements sensibles sans secrets, faire tourner les jetons et réévaluer les risques. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 055 — Login CSRF

1. **Description / fonctionnement :** Force un navigateur à s'authentifier sur un compte non voulu.
2. **Causes techniques :** absence de validation forte des preuves d’identité et mauvaise gestion du cycle de session ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** inscription, connexion, récupération, MFA, OAuth/OIDC, SAML, JWT et cookies ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier tous les parcours de connexion/récupération ; examiner signatures, limites d’essais et états de session. Rechercher spécialement : absence de validation forte des preuves d’identité et mauvaise gestion du cycle de session.
5. **Prévention :** MFA approprié, vérification cryptographique stricte, ralentissement progressif, secrets robustes et cookies sécurisés. **Point spécifique :** centraliser l’authentification côté serveur ; invalider anciens jetons et imposer les contrôles à chaque point d’entrée
6. **Correction sécurisée :** Centraliser l’authentification côté serveur ; invalider anciens jetons et imposer les contrôles à chaque point d’entrée. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** tester les échecs de connexion, token expiré, MFA absent et session déconnectée avec comptes de test Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Journaliser les événements sensibles sans secrets, faire tourner les jetons et réévaluer les risques. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».
