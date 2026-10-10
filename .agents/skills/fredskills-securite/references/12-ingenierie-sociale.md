# 12 — Ingénierie sociale et identité

**Couverture :** 13 types d’attaque numérotés 188 à 200. Cet inventaire identifie des familles, variantes et scénarios ; certains termes se recoupent.

**Utilisation :** lire les profils liés à la surface attaquée. Les risques sont indicatifs et se recalculent selon exposition, impact, contrôle existant et vraisemblance. Ne pas effectuer de tests actifs sur des systèmes non autorisés.

## 188 — Phishing

1. **Description / fonctionnement :** Incite une personne à révéler ses accès dans une fausse interface.
2. **Causes techniques :** Identité sociale ou tiers non vérifiés ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** emails, comptes, consoles d’administration, OAuth, SSO et navigateur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Contrôler parcours de consentement, processus de support, alertes de connexion et signalements. Rechercher spécialement : identité sociale ou tiers non vérifiés.
5. **Prévention :** MFA résistante au phishing lorsque disponible, contrôles hors bande, DMARC/SPF/DKIM et sensibilisation. **Point spécifique :** Procédures hors bande, sécurité du support, MFA résistant au phishing et approbation des intégrations.
6. **Correction sécurisée :** Renforcer les procédures de récupération/validation d’identité et retirer les consentements anormaux. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Les procédures de récupération nécessitent une preuve indépendante d’identité. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : prise de contrôle de comptes ou fraude par interaction humaine.
9. **Prévention de réapparition :** Surveiller anomalies et entraîner les équipes régulièrement. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 189 — Spear Phishing

1. **Description / fonctionnement :** Phishing personnalisé sur une victime ou équipe.
2. **Causes techniques :** Identité sociale ou tiers non vérifiés ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** emails, comptes, consoles d’administration, OAuth, SSO et navigateur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Contrôler parcours de consentement, processus de support, alertes de connexion et signalements. Rechercher spécialement : identité sociale ou tiers non vérifiés.
5. **Prévention :** MFA résistante au phishing lorsque disponible, contrôles hors bande, DMARC/SPF/DKIM et sensibilisation. **Point spécifique :** Procédures hors bande, sécurité du support, MFA résistant au phishing et approbation des intégrations.
6. **Correction sécurisée :** Renforcer les procédures de récupération/validation d’identité et retirer les consentements anormaux. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Les procédures de récupération nécessitent une preuve indépendante d’identité. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : prise de contrôle de comptes ou fraude par interaction humaine.
9. **Prévention de réapparition :** Surveiller anomalies et entraîner les équipes régulièrement. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 190 — Clone Phishing

1. **Description / fonctionnement :** Reproduit un message légitime pour tromper le destinataire.
2. **Causes techniques :** Identité sociale ou tiers non vérifiés ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** emails, comptes, consoles d’administration, OAuth, SSO et navigateur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Contrôler parcours de consentement, processus de support, alertes de connexion et signalements. Rechercher spécialement : identité sociale ou tiers non vérifiés.
5. **Prévention :** MFA résistante au phishing lorsque disponible, contrôles hors bande, DMARC/SPF/DKIM et sensibilisation. **Point spécifique :** Procédures hors bande, sécurité du support, MFA résistant au phishing et approbation des intégrations.
6. **Correction sécurisée :** Renforcer les procédures de récupération/validation d’identité et retirer les consentements anormaux. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Les procédures de récupération nécessitent une preuve indépendante d’identité. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : prise de contrôle de comptes ou fraude par interaction humaine.
9. **Prévention de réapparition :** Surveiller anomalies et entraîner les équipes régulièrement. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 191 — Adversary-in-the-Middle Phishing

1. **Description / fonctionnement :** Intercepte le parcours de connexion via une interface relais.
2. **Causes techniques :** Identité sociale ou tiers non vérifiés ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** emails, comptes, consoles d’administration, OAuth, SSO et navigateur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Contrôler parcours de consentement, processus de support, alertes de connexion et signalements. Rechercher spécialement : identité sociale ou tiers non vérifiés.
5. **Prévention :** MFA résistante au phishing lorsque disponible, contrôles hors bande, DMARC/SPF/DKIM et sensibilisation. **Point spécifique :** Procédures hors bande, sécurité du support, MFA résistant au phishing et approbation des intégrations.
6. **Correction sécurisée :** Renforcer les procédures de récupération/validation d’identité et retirer les consentements anormaux. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Les procédures de récupération nécessitent une preuve indépendante d’identité. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : prise de contrôle de comptes ou fraude par interaction humaine.
9. **Prévention de réapparition :** Surveiller anomalies et entraîner les équipes régulièrement. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 192 — Social Engineering

1. **Description / fonctionnement :** Manipule l'utilisateur ou un agent support.
2. **Causes techniques :** Identité sociale ou tiers non vérifiés ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** emails, comptes, consoles d’administration, OAuth, SSO et navigateur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Contrôler parcours de consentement, processus de support, alertes de connexion et signalements. Rechercher spécialement : identité sociale ou tiers non vérifiés.
5. **Prévention :** MFA résistante au phishing lorsque disponible, contrôles hors bande, DMARC/SPF/DKIM et sensibilisation. **Point spécifique :** Procédures hors bande, sécurité du support, MFA résistant au phishing et approbation des intégrations.
6. **Correction sécurisée :** Renforcer les procédures de récupération/validation d’identité et retirer les consentements anormaux. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Les procédures de récupération nécessitent une preuve indépendante d’identité. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : prise de contrôle de comptes ou fraude par interaction humaine.
9. **Prévention de réapparition :** Surveiller anomalies et entraîner les équipes régulièrement. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 193 — Pretexting

1. **Description / fonctionnement :** Utilise un scénario mensonger pour obtenir une action.
2. **Causes techniques :** Identité sociale ou tiers non vérifiés ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** emails, comptes, consoles d’administration, OAuth, SSO et navigateur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Contrôler parcours de consentement, processus de support, alertes de connexion et signalements. Rechercher spécialement : identité sociale ou tiers non vérifiés.
5. **Prévention :** MFA résistante au phishing lorsque disponible, contrôles hors bande, DMARC/SPF/DKIM et sensibilisation. **Point spécifique :** Procédures hors bande, sécurité du support, MFA résistant au phishing et approbation des intégrations.
6. **Correction sécurisée :** Renforcer les procédures de récupération/validation d’identité et retirer les consentements anormaux. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Les procédures de récupération nécessitent une preuve indépendante d’identité. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : prise de contrôle de comptes ou fraude par interaction humaine.
9. **Prévention de réapparition :** Surveiller anomalies et entraîner les équipes régulièrement. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 194 — Helpdesk Impersonation

1. **Description / fonctionnement :** Se fait passer pour le support d'un service.
2. **Causes techniques :** Identité sociale ou tiers non vérifiés ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** emails, comptes, consoles d’administration, OAuth, SSO et navigateur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Contrôler parcours de consentement, processus de support, alertes de connexion et signalements. Rechercher spécialement : identité sociale ou tiers non vérifiés.
5. **Prévention :** MFA résistante au phishing lorsque disponible, contrôles hors bande, DMARC/SPF/DKIM et sensibilisation. **Point spécifique :** Procédures hors bande, sécurité du support, MFA résistant au phishing et approbation des intégrations.
6. **Correction sécurisée :** Renforcer les procédures de récupération/validation d’identité et retirer les consentements anormaux. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Les procédures de récupération nécessitent une preuve indépendante d’identité. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : prise de contrôle de comptes ou fraude par interaction humaine.
9. **Prévention de réapparition :** Surveiller anomalies et entraîner les équipes régulièrement. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 195 — Fake Login Page

1. **Description / fonctionnement :** Reproduit un formulaire de connexion dans une page frauduleuse.
2. **Causes techniques :** Identité sociale ou tiers non vérifiés ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** emails, comptes, consoles d’administration, OAuth, SSO et navigateur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Contrôler parcours de consentement, processus de support, alertes de connexion et signalements. Rechercher spécialement : identité sociale ou tiers non vérifiés.
5. **Prévention :** MFA résistante au phishing lorsque disponible, contrôles hors bande, DMARC/SPF/DKIM et sensibilisation. **Point spécifique :** Procédures hors bande, sécurité du support, MFA résistant au phishing et approbation des intégrations.
6. **Correction sécurisée :** Renforcer les procédures de récupération/validation d’identité et retirer les consentements anormaux. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Les procédures de récupération nécessitent une preuve indépendante d’identité. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : prise de contrôle de comptes ou fraude par interaction humaine.
9. **Prévention de réapparition :** Surveiller anomalies et entraîner les équipes régulièrement. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 196 — Session Token Phishing

1. **Description / fonctionnement :** Trompe la victime pour obtenir un artefact de session.
2. **Causes techniques :** Identité sociale ou tiers non vérifiés ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** emails, comptes, consoles d’administration, OAuth, SSO et navigateur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Contrôler parcours de consentement, processus de support, alertes de connexion et signalements. Rechercher spécialement : identité sociale ou tiers non vérifiés.
5. **Prévention :** MFA résistante au phishing lorsque disponible, contrôles hors bande, DMARC/SPF/DKIM et sensibilisation. **Point spécifique :** Procédures hors bande, sécurité du support, MFA résistant au phishing et approbation des intégrations.
6. **Correction sécurisée :** Renforcer les procédures de récupération/validation d’identité et retirer les consentements anormaux. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Les procédures de récupération nécessitent une preuve indépendante d’identité. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : prise de contrôle de comptes ou fraude par interaction humaine.
9. **Prévention de réapparition :** Surveiller anomalies et entraîner les équipes régulièrement. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 197 — QR Code Phishing

1. **Description / fonctionnement :** Oriente une personne vers une destination frauduleuse via QR code.
2. **Causes techniques :** Identité sociale ou tiers non vérifiés ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** emails, comptes, consoles d’administration, OAuth, SSO et navigateur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Contrôler parcours de consentement, processus de support, alertes de connexion et signalements. Rechercher spécialement : identité sociale ou tiers non vérifiés.
5. **Prévention :** MFA résistante au phishing lorsque disponible, contrôles hors bande, DMARC/SPF/DKIM et sensibilisation. **Point spécifique :** Procédures hors bande, sécurité du support, MFA résistant au phishing et approbation des intégrations.
6. **Correction sécurisée :** Renforcer les procédures de récupération/validation d’identité et retirer les consentements anormaux. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Les procédures de récupération nécessitent une preuve indépendante d’identité. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : prise de contrôle de comptes ou fraude par interaction humaine.
9. **Prévention de réapparition :** Surveiller anomalies et entraîner les équipes régulièrement. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 198 — Malicious Browser Extension

1. **Description / fonctionnement :** Utilise une extension pour accéder au contexte du navigateur.
2. **Causes techniques :** Identité sociale ou tiers non vérifiés ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** emails, comptes, consoles d’administration, OAuth, SSO et navigateur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Contrôler parcours de consentement, processus de support, alertes de connexion et signalements. Rechercher spécialement : identité sociale ou tiers non vérifiés.
5. **Prévention :** MFA résistante au phishing lorsque disponible, contrôles hors bande, DMARC/SPF/DKIM et sensibilisation. **Point spécifique :** Procédures hors bande, sécurité du support, MFA résistant au phishing et approbation des intégrations.
6. **Correction sécurisée :** Renforcer les procédures de récupération/validation d’identité et retirer les consentements anormaux. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Les procédures de récupération nécessitent une preuve indépendante d’identité. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : prise de contrôle de comptes ou fraude par interaction humaine.
9. **Prévention de réapparition :** Surveiller anomalies et entraîner les équipes régulièrement. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 199 — OAuth Consent Phishing

1. **Description / fonctionnement :** Fait autoriser une application OAuth malveillante.
2. **Causes techniques :** Identité sociale ou tiers non vérifiés ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** emails, comptes, consoles d’administration, OAuth, SSO et navigateur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Contrôler parcours de consentement, processus de support, alertes de connexion et signalements. Rechercher spécialement : identité sociale ou tiers non vérifiés.
5. **Prévention :** MFA résistante au phishing lorsque disponible, contrôles hors bande, DMARC/SPF/DKIM et sensibilisation. **Point spécifique :** Procédures hors bande, sécurité du support, MFA résistant au phishing et approbation des intégrations.
6. **Correction sécurisée :** Renforcer les procédures de récupération/validation d’identité et retirer les consentements anormaux. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Les procédures de récupération nécessitent une preuve indépendante d’identité. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : prise de contrôle de comptes ou fraude par interaction humaine.
9. **Prévention de réapparition :** Surveiller anomalies et entraîner les équipes régulièrement. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 200 — Business Email Compromise

1. **Description / fonctionnement :** Usurpe la messagerie d'une entreprise pour frauder.
2. **Causes techniques :** Identité sociale ou tiers non vérifiés ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** emails, comptes, consoles d’administration, OAuth, SSO et navigateur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Contrôler parcours de consentement, processus de support, alertes de connexion et signalements. Rechercher spécialement : identité sociale ou tiers non vérifiés.
5. **Prévention :** MFA résistante au phishing lorsque disponible, contrôles hors bande, DMARC/SPF/DKIM et sensibilisation. **Point spécifique :** Procédures hors bande, sécurité du support, MFA résistant au phishing et approbation des intégrations.
6. **Correction sécurisée :** Renforcer les procédures de récupération/validation d’identité et retirer les consentements anormaux. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Les procédures de récupération nécessitent une preuve indépendante d’identité. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : prise de contrôle de comptes ou fraude par interaction humaine.
9. **Prévention de réapparition :** Surveiller anomalies et entraîner les équipes régulièrement. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».
