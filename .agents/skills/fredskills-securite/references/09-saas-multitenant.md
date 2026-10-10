# 09 — SaaS multi-tenant

**Couverture :** 17 types d’attaque numérotés 138 à 154. Cet inventaire identifie des familles, variantes et scénarios ; certains termes se recoupent.

**Utilisation :** lire les profils liés à la surface attaquée. Les risques sont indicatifs et se recalculent selon exposition, impact, contrôle existant et vraisemblance. Ne pas effectuer de tests actifs sur des systèmes non autorisés.

## 138 — Cross-Tenant Data Leakage

1. **Description / fonctionnement :** Divulgue des données d'une organisation à une autre.
2. **Causes techniques :** Identifiant d’objet utilisé sans contrôle d’appartenance ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** authentification tenant, DB, cache, stockage, facturation, invitations, webhooks ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier le tenant courant, clés de partition, accès objets et frontières d’organisation. Rechercher spécialement : identifiant d’objet utilisé sans contrôle d’appartenance.
5. **Prévention :** Contexte tenant issu d’une identité vérifiée, autorisation serveur sur chaque objet, espaces logiques isolés. **Point spécifique :** Récupérer les objets avec filtre tenant/propriétaire et autorisation serveur à chaque opération.
6. **Correction sécurisée :** Ajouter filtrage tenant dans accès DB/fichiers/cache et vérifier signatures de webhooks. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Changer seulement l’ID vers un objet du second compte renvoie 403 ou 404. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Contrôles transversaux d’isolation, audit des logs et revues des jobs asynchrones. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 139 — Tenant Impersonation

1. **Description / fonctionnement :** Usurpe le contexte d'une organisation.
2. **Causes techniques :** Identifiant d’objet utilisé sans contrôle d’appartenance ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** authentification tenant, DB, cache, stockage, facturation, invitations, webhooks ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier le tenant courant, clés de partition, accès objets et frontières d’organisation. Rechercher spécialement : identifiant d’objet utilisé sans contrôle d’appartenance.
5. **Prévention :** Contexte tenant issu d’une identité vérifiée, autorisation serveur sur chaque objet, espaces logiques isolés. **Point spécifique :** Récupérer les objets avec filtre tenant/propriétaire et autorisation serveur à chaque opération.
6. **Correction sécurisée :** Ajouter filtrage tenant dans accès DB/fichiers/cache et vérifier signatures de webhooks. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Changer seulement l’ID vers un objet du second compte renvoie 403 ou 404. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Contrôles transversaux d’isolation, audit des logs et revues des jobs asynchrones. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 140 — SaaS Admin Takeover

1. **Description / fonctionnement :** Compromet l'administration de la plateforme SaaS.
2. **Causes techniques :** contexte d’organisation incorrect, permissions croisées ou événement inter-tenant non vérifié ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** authentification tenant, DB, cache, stockage, facturation, invitations, webhooks ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier le tenant courant, clés de partition, accès objets et frontières d’organisation. Rechercher spécialement : contexte d’organisation incorrect, permissions croisées ou événement inter-tenant non vérifié.
5. **Prévention :** Contexte tenant issu d’une identité vérifiée, autorisation serveur sur chaque objet, espaces logiques isolés. **Point spécifique :** ajouter filtrage tenant dans accès DB/fichiers/cache et vérifier signatures de webhooks
6. **Correction sécurisée :** Ajouter filtrage tenant dans accès DB/fichiers/cache et vérifier signatures de webhooks. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** tester deux organisations et deux rôles : aucune lecture, écriture ou notification croisée admise Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Contrôles transversaux d’isolation, audit des logs et revues des jobs asynchrones. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 141 — Subscription Bypass

1. **Description / fonctionnement :** Utilise une fonctionnalité sans l'abonnement requis.
2. **Causes techniques :** contexte d’organisation incorrect, permissions croisées ou événement inter-tenant non vérifié ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** authentification tenant, DB, cache, stockage, facturation, invitations, webhooks ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier le tenant courant, clés de partition, accès objets et frontières d’organisation. Rechercher spécialement : contexte d’organisation incorrect, permissions croisées ou événement inter-tenant non vérifié.
5. **Prévention :** Contexte tenant issu d’une identité vérifiée, autorisation serveur sur chaque objet, espaces logiques isolés. **Point spécifique :** ajouter filtrage tenant dans accès DB/fichiers/cache et vérifier signatures de webhooks
6. **Correction sécurisée :** Ajouter filtrage tenant dans accès DB/fichiers/cache et vérifier signatures de webhooks. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** tester deux organisations et deux rôles : aucune lecture, écriture ou notification croisée admise Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Contrôles transversaux d’isolation, audit des logs et revues des jobs asynchrones. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 142 — Feature Flag Manipulation

1. **Description / fonctionnement :** Modifie des drapeaux de fonctionnalité non autorisés.
2. **Causes techniques :** contexte d’organisation incorrect, permissions croisées ou événement inter-tenant non vérifié ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** authentification tenant, DB, cache, stockage, facturation, invitations, webhooks ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier le tenant courant, clés de partition, accès objets et frontières d’organisation. Rechercher spécialement : contexte d’organisation incorrect, permissions croisées ou événement inter-tenant non vérifié.
5. **Prévention :** Contexte tenant issu d’une identité vérifiée, autorisation serveur sur chaque objet, espaces logiques isolés. **Point spécifique :** ajouter filtrage tenant dans accès DB/fichiers/cache et vérifier signatures de webhooks
6. **Correction sécurisée :** Ajouter filtrage tenant dans accès DB/fichiers/cache et vérifier signatures de webhooks. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** tester deux organisations et deux rôles : aucune lecture, écriture ou notification croisée admise Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Contrôles transversaux d’isolation, audit des logs et revues des jobs asynchrones. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 143 — Billing Manipulation

1. **Description / fonctionnement :** Manipule les données de facturation.
2. **Causes techniques :** Valeurs métier et transitions influencées par le client ou état concurrent ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** authentification tenant, DB, cache, stockage, facturation, invitations, webhooks ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier le tenant courant, clés de partition, accès objets et frontières d’organisation. Rechercher spécialement : valeurs métier et transitions influencées par le client ou état concurrent.
5. **Prévention :** Contexte tenant issu d’une identité vérifiée, autorisation serveur sur chaque objet, espaces logiques isolés. **Point spécifique :** Recalcul serveur, contraintes SQL, transaction atomique, idempotency keys et machine à états.
6. **Correction sécurisée :** Ajouter filtrage tenant dans accès DB/fichiers/cache et vérifier signatures de webhooks. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une opération répétée, négative ou concurrente ne modifie pas illégalement le solde/stock. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Contrôles transversaux d’isolation, audit des logs et revues des jobs asynchrones. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 144 — Usage Limit Bypass

1. **Description / fonctionnement :** Dépasse quotas ou limites de contrat.
2. **Causes techniques :** contexte d’organisation incorrect, permissions croisées ou événement inter-tenant non vérifié ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** authentification tenant, DB, cache, stockage, facturation, invitations, webhooks ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier le tenant courant, clés de partition, accès objets et frontières d’organisation. Rechercher spécialement : contexte d’organisation incorrect, permissions croisées ou événement inter-tenant non vérifié.
5. **Prévention :** Contexte tenant issu d’une identité vérifiée, autorisation serveur sur chaque objet, espaces logiques isolés. **Point spécifique :** ajouter filtrage tenant dans accès DB/fichiers/cache et vérifier signatures de webhooks
6. **Correction sécurisée :** Ajouter filtrage tenant dans accès DB/fichiers/cache et vérifier signatures de webhooks. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** tester deux organisations et deux rôles : aucune lecture, écriture ou notification croisée admise Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Contrôles transversaux d’isolation, audit des logs et revues des jobs asynchrones. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 145 — SaaS API Abuse

1. **Description / fonctionnement :** Abuse des intégrations et API du service.
2. **Causes techniques :** contexte d’organisation incorrect, permissions croisées ou événement inter-tenant non vérifié ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** authentification tenant, DB, cache, stockage, facturation, invitations, webhooks ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier le tenant courant, clés de partition, accès objets et frontières d’organisation. Rechercher spécialement : contexte d’organisation incorrect, permissions croisées ou événement inter-tenant non vérifié.
5. **Prévention :** Contexte tenant issu d’une identité vérifiée, autorisation serveur sur chaque objet, espaces logiques isolés. **Point spécifique :** ajouter filtrage tenant dans accès DB/fichiers/cache et vérifier signatures de webhooks
6. **Correction sécurisée :** Ajouter filtrage tenant dans accès DB/fichiers/cache et vérifier signatures de webhooks. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** tester deux organisations et deux rôles : aucune lecture, écriture ou notification croisée admise Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Contrôles transversaux d’isolation, audit des logs et revues des jobs asynchrones. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 146 — Insecure Tenant Provisioning

1. **Description / fonctionnement :** Crée ou associe une organisation sans validations nécessaires.
2. **Causes techniques :** Identifiant d’objet utilisé sans contrôle d’appartenance ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** authentification tenant, DB, cache, stockage, facturation, invitations, webhooks ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier le tenant courant, clés de partition, accès objets et frontières d’organisation. Rechercher spécialement : identifiant d’objet utilisé sans contrôle d’appartenance.
5. **Prévention :** Contexte tenant issu d’une identité vérifiée, autorisation serveur sur chaque objet, espaces logiques isolés. **Point spécifique :** Récupérer les objets avec filtre tenant/propriétaire et autorisation serveur à chaque opération.
6. **Correction sécurisée :** Ajouter filtrage tenant dans accès DB/fichiers/cache et vérifier signatures de webhooks. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Changer seulement l’ID vers un objet du second compte renvoie 403 ou 404. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Contrôles transversaux d’isolation, audit des logs et revues des jobs asynchrones. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 147 — Cross-Tenant File Access

1. **Description / fonctionnement :** Accède aux documents d'une autre organisation.
2. **Causes techniques :** Chemins dérivés d’entrées non fiables ou fichiers servis trop librement ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** authentification tenant, DB, cache, stockage, facturation, invitations, webhooks ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier le tenant courant, clés de partition, accès objets et frontières d’organisation. Rechercher spécialement : chemins dérivés d’entrées non fiables ou fichiers servis trop librement.
5. **Prévention :** Contexte tenant issu d’une identité vérifiée, autorisation serveur sur chaque objet, espaces logiques isolés. **Point spécifique :** Chemins canoniques, stockage privé hors webroot, streaming sous autorisation et contrôle type/taille.
6. **Correction sécurisée :** Ajouter filtrage tenant dans accès DB/fichiers/cache et vérifier signatures de webhooks. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un chemin parent ou téléchargement d’un autre compte est refusé ; upload non exécutable. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Contrôles transversaux d’isolation, audit des logs et revues des jobs asynchrones. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 148 — Insecure Organization Invitations

1. **Description / fonctionnement :** Profite de jetons d'invitation mal vérifiés.
2. **Causes techniques :** contexte d’organisation incorrect, permissions croisées ou événement inter-tenant non vérifié ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** authentification tenant, DB, cache, stockage, facturation, invitations, webhooks ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier le tenant courant, clés de partition, accès objets et frontières d’organisation. Rechercher spécialement : contexte d’organisation incorrect, permissions croisées ou événement inter-tenant non vérifié.
5. **Prévention :** Contexte tenant issu d’une identité vérifiée, autorisation serveur sur chaque objet, espaces logiques isolés. **Point spécifique :** ajouter filtrage tenant dans accès DB/fichiers/cache et vérifier signatures de webhooks
6. **Correction sécurisée :** Ajouter filtrage tenant dans accès DB/fichiers/cache et vérifier signatures de webhooks. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** tester deux organisations et deux rôles : aucune lecture, écriture ou notification croisée admise Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Contrôles transversaux d’isolation, audit des logs et revues des jobs asynchrones. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 149 — Shared Resource Misconfiguration

1. **Description / fonctionnement :** Partage des caches, files ou objets entre tenants sans isolation.
2. **Causes techniques :** Entrée transmise à un interpréteur ou exécuteur ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** authentification tenant, DB, cache, stockage, facturation, invitations, webhooks ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier le tenant courant, clés de partition, accès objets et frontières d’organisation. Rechercher spécialement : entrée transmise à un interpréteur ou exécuteur.
5. **Prévention :** Contexte tenant issu d’une identité vérifiée, autorisation serveur sur chaque objet, espaces logiques isolés. **Point spécifique :** Éviter l’interpréteur ; employer des API dédiées, arguments séparés et listes autorisées.
6. **Correction sécurisée :** Ajouter filtrage tenant dans accès DB/fichiers/cache et vérifier signatures de webhooks. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un nom de fichier avec caractères spéciaux ne doit jamais déclencher de commande. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Contrôles transversaux d’isolation, audit des logs et revues des jobs asynchrones. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 150 — SaaS Integration Token Theft

1. **Description / fonctionnement :** Vole des identifiants de connecteurs tiers.
2. **Causes techniques :** Secrets persistants ou transmis à un mauvais destinataire ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** authentification tenant, DB, cache, stockage, facturation, invitations, webhooks ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier le tenant courant, clés de partition, accès objets et frontières d’organisation. Rechercher spécialement : secrets persistants ou transmis à un mauvais destinataire.
5. **Prévention :** Contexte tenant issu d’une identité vérifiée, autorisation serveur sur chaque objet, espaces logiques isolés. **Point spécifique :** Stocker en gestionnaire de secrets, réduire la portée et effectuer rotation et révocation.
6. **Correction sécurisée :** Ajouter filtrage tenant dans accès DB/fichiers/cache et vérifier signatures de webhooks. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Clés invalides ou retirées ne fonctionnent plus ; aucun secret dans logs et réponses. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Contrôles transversaux d’isolation, audit des logs et revues des jobs asynchrones. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 151 — Webhook Spoofing

1. **Description / fonctionnement :** Envoie un événement falsifié au système.
2. **Causes techniques :** Notifications entrantes non authentifiées ou rejouables ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** authentification tenant, DB, cache, stockage, facturation, invitations, webhooks ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier le tenant courant, clés de partition, accès objets et frontières d’organisation. Rechercher spécialement : notifications entrantes non authentifiées ou rejouables.
5. **Prévention :** Contexte tenant issu d’une identité vérifiée, autorisation serveur sur chaque objet, espaces logiques isolés. **Point spécifique :** Vérifier signature sur corps brut, horodatage, identifiant événement et déduplication.
6. **Correction sécurisée :** Ajouter filtrage tenant dans accès DB/fichiers/cache et vérifier signatures de webhooks. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Signature modifiée, timestamp périmé et événement réutilisé sont rejetés. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Contrôles transversaux d’isolation, audit des logs et revues des jobs asynchrones. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 152 — Webhook Replay

1. **Description / fonctionnement :** Réutilise un événement webhook pourtant déjà consommé.
2. **Causes techniques :** Notifications entrantes non authentifiées ou rejouables ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** authentification tenant, DB, cache, stockage, facturation, invitations, webhooks ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier le tenant courant, clés de partition, accès objets et frontières d’organisation. Rechercher spécialement : notifications entrantes non authentifiées ou rejouables.
5. **Prévention :** Contexte tenant issu d’une identité vérifiée, autorisation serveur sur chaque objet, espaces logiques isolés. **Point spécifique :** Vérifier signature sur corps brut, horodatage, identifiant événement et déduplication.
6. **Correction sécurisée :** Ajouter filtrage tenant dans accès DB/fichiers/cache et vérifier signatures de webhooks. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Signature modifiée, timestamp périmé et événement réutilisé sont rejetés. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Contrôles transversaux d’isolation, audit des logs et revues des jobs asynchrones. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 153 — Permission Inheritance Abuse

1. **Description / fonctionnement :** Exploite la propagation incorrecte des permissions.
2. **Causes techniques :** contexte d’organisation incorrect, permissions croisées ou événement inter-tenant non vérifié ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** authentification tenant, DB, cache, stockage, facturation, invitations, webhooks ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier le tenant courant, clés de partition, accès objets et frontières d’organisation. Rechercher spécialement : contexte d’organisation incorrect, permissions croisées ou événement inter-tenant non vérifié.
5. **Prévention :** Contexte tenant issu d’une identité vérifiée, autorisation serveur sur chaque objet, espaces logiques isolés. **Point spécifique :** ajouter filtrage tenant dans accès DB/fichiers/cache et vérifier signatures de webhooks
6. **Correction sécurisée :** Ajouter filtrage tenant dans accès DB/fichiers/cache et vérifier signatures de webhooks. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** tester deux organisations et deux rôles : aucune lecture, écriture ou notification croisée admise Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Contrôles transversaux d’isolation, audit des logs et revues des jobs asynchrones. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 154 — Insecure User Impersonation Feature

1. **Description / fonctionnement :** Abuse de la fonction support « agir en tant que ».
2. **Causes techniques :** contexte d’organisation incorrect, permissions croisées ou événement inter-tenant non vérifié ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** authentification tenant, DB, cache, stockage, facturation, invitations, webhooks ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier le tenant courant, clés de partition, accès objets et frontières d’organisation. Rechercher spécialement : contexte d’organisation incorrect, permissions croisées ou événement inter-tenant non vérifié.
5. **Prévention :** Contexte tenant issu d’une identité vérifiée, autorisation serveur sur chaque objet, espaces logiques isolés. **Point spécifique :** ajouter filtrage tenant dans accès DB/fichiers/cache et vérifier signatures de webhooks
6. **Correction sécurisée :** Ajouter filtrage tenant dans accès DB/fichiers/cache et vérifier signatures de webhooks. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** tester deux organisations et deux rôles : aucune lecture, écriture ou notification croisée admise Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Contrôles transversaux d’isolation, audit des logs et revues des jobs asynchrones. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».
