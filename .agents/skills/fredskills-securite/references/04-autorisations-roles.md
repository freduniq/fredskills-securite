# 04 — Autorisations et rôles

**Couverture :** 15 types d’attaque numérotés 56 à 70. Cet inventaire identifie des familles, variantes et scénarios ; certains termes se recoupent.

**Utilisation :** lire les profils liés à la surface attaquée. Les risques sont indicatifs et se recalculent selon exposition, impact, contrôle existant et vraisemblance. Ne pas effectuer de tests actifs sur des systèmes non autorisés.

## 056 — IDOR

1. **Description / fonctionnement :** Accède à un objet par un identifiant sans vérifier son propriétaire.
2. **Causes techniques :** Identifiant d’objet utilisé sans contrôle d’appartenance ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** routes, contrôleurs, services, modèles, fichiers, espace administrateur et tenant_id ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Tracer chaque action jusqu’à la vérification d’autorisation serveur et simuler des accès entre comptes de test. Rechercher spécialement : identifiant d’objet utilisé sans contrôle d’appartenance.
5. **Prévention :** Deny-by-default, contrôles objet et fonction côté serveur, scoping par utilisateur/tenant. **Point spécifique :** Récupérer les objets avec filtre tenant/propriétaire et autorisation serveur à chaque opération.
6. **Correction sécurisée :** Ajouter policy/guard serveur pour chaque action ; contraindre les requêtes par propriétaire et organisation. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Changer seulement l’ID vers un objet du second compte renvoie 403 ou 404. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Matrice d’autorisations et tests négatifs pour toute nouvelle route. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 057 — BOLA

1. **Description / fonctionnement :** Accède à un objet API sans contrôle d'autorisation par objet.
2. **Causes techniques :** Identifiant d’objet utilisé sans contrôle d’appartenance ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** routes, contrôleurs, services, modèles, fichiers, espace administrateur et tenant_id ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Tracer chaque action jusqu’à la vérification d’autorisation serveur et simuler des accès entre comptes de test. Rechercher spécialement : identifiant d’objet utilisé sans contrôle d’appartenance.
5. **Prévention :** Deny-by-default, contrôles objet et fonction côté serveur, scoping par utilisateur/tenant. **Point spécifique :** Récupérer les objets avec filtre tenant/propriétaire et autorisation serveur à chaque opération.
6. **Correction sécurisée :** Ajouter policy/guard serveur pour chaque action ; contraindre les requêtes par propriétaire et organisation. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Changer seulement l’ID vers un objet du second compte renvoie 403 ou 404. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Matrice d’autorisations et tests négatifs pour toute nouvelle route. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 058 — BFLA

1. **Description / fonctionnement :** Accède à une opération API non autorisée pour le rôle.
2. **Causes techniques :** Champs ou fonctions d’autorisation déduits du client ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** routes, contrôleurs, services, modèles, fichiers, espace administrateur et tenant_id ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Tracer chaque action jusqu’à la vérification d’autorisation serveur et simuler des accès entre comptes de test. Rechercher spécialement : champs ou fonctions d’autorisation déduits du client.
5. **Prévention :** Deny-by-default, contrôles objet et fonction côté serveur, scoping par utilisateur/tenant. **Point spécifique :** Autoriser explicitement les champs modifiables et imposer des policies serveur par rôle/fonction.
6. **Correction sécurisée :** Ajouter policy/guard serveur pour chaque action ; contraindre les requêtes par propriétaire et organisation. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un utilisateur standard ne peut pas passer role=admin ni modifier une propriété cachée. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Matrice d’autorisations et tests négatifs pour toute nouvelle route. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 059 — Broken Access Control

1. **Description / fonctionnement :** Contourne les règles de visibilité et de modification.
2. **Causes techniques :** confiance dans un identifiant ou rôle fourni par le client ; vérification d’autorisation manquante ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** routes, contrôleurs, services, modèles, fichiers, espace administrateur et tenant_id ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Tracer chaque action jusqu’à la vérification d’autorisation serveur et simuler des accès entre comptes de test. Rechercher spécialement : confiance dans un identifiant ou rôle fourni par le client ; vérification d’autorisation manquante.
5. **Prévention :** Deny-by-default, contrôles objet et fonction côté serveur, scoping par utilisateur/tenant. **Point spécifique :** ajouter policy/guard serveur pour chaque action ; contraindre les requêtes par propriétaire et organisation
6. **Correction sécurisée :** Ajouter policy/guard serveur pour chaque action ; contraindre les requêtes par propriétaire et organisation. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** tester refus 403/404 pour utilisateur voisin, rôle inférieur, tenant différent et ressource supprimée Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Matrice d’autorisations et tests négatifs pour toute nouvelle route. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 060 — Privilege Escalation

1. **Description / fonctionnement :** Obtient des privilèges supérieurs à ceux attribués.
2. **Causes techniques :** Champs ou fonctions d’autorisation déduits du client ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** routes, contrôleurs, services, modèles, fichiers, espace administrateur et tenant_id ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Tracer chaque action jusqu’à la vérification d’autorisation serveur et simuler des accès entre comptes de test. Rechercher spécialement : champs ou fonctions d’autorisation déduits du client.
5. **Prévention :** Deny-by-default, contrôles objet et fonction côté serveur, scoping par utilisateur/tenant. **Point spécifique :** Autoriser explicitement les champs modifiables et imposer des policies serveur par rôle/fonction.
6. **Correction sécurisée :** Ajouter policy/guard serveur pour chaque action ; contraindre les requêtes par propriétaire et organisation. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un utilisateur standard ne peut pas passer role=admin ni modifier une propriété cachée. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Matrice d’autorisations et tests négatifs pour toute nouvelle route. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 061 — Horizontal Privilege Escalation

1. **Description / fonctionnement :** Accède aux ressources d'un autre utilisateur de même rôle.
2. **Causes techniques :** Champs ou fonctions d’autorisation déduits du client ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** routes, contrôleurs, services, modèles, fichiers, espace administrateur et tenant_id ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Tracer chaque action jusqu’à la vérification d’autorisation serveur et simuler des accès entre comptes de test. Rechercher spécialement : champs ou fonctions d’autorisation déduits du client.
5. **Prévention :** Deny-by-default, contrôles objet et fonction côté serveur, scoping par utilisateur/tenant. **Point spécifique :** Autoriser explicitement les champs modifiables et imposer des policies serveur par rôle/fonction.
6. **Correction sécurisée :** Ajouter policy/guard serveur pour chaque action ; contraindre les requêtes par propriétaire et organisation. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un utilisateur standard ne peut pas passer role=admin ni modifier une propriété cachée. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Matrice d’autorisations et tests négatifs pour toute nouvelle route. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 062 — Vertical Privilege Escalation

1. **Description / fonctionnement :** Obtient les capacités d'un rôle privilégié.
2. **Causes techniques :** Champs ou fonctions d’autorisation déduits du client ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** routes, contrôleurs, services, modèles, fichiers, espace administrateur et tenant_id ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Tracer chaque action jusqu’à la vérification d’autorisation serveur et simuler des accès entre comptes de test. Rechercher spécialement : champs ou fonctions d’autorisation déduits du client.
5. **Prévention :** Deny-by-default, contrôles objet et fonction côté serveur, scoping par utilisateur/tenant. **Point spécifique :** Autoriser explicitement les champs modifiables et imposer des policies serveur par rôle/fonction.
6. **Correction sécurisée :** Ajouter policy/guard serveur pour chaque action ; contraindre les requêtes par propriétaire et organisation. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un utilisateur standard ne peut pas passer role=admin ni modifier une propriété cachée. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Matrice d’autorisations et tests négatifs pour toute nouvelle route. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 063 — Forced Browsing

1. **Description / fonctionnement :** Utilise directement une URL non protégée.
2. **Causes techniques :** Entrée transmise à un interpréteur ou exécuteur ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** routes, contrôleurs, services, modèles, fichiers, espace administrateur et tenant_id ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Tracer chaque action jusqu’à la vérification d’autorisation serveur et simuler des accès entre comptes de test. Rechercher spécialement : entrée transmise à un interpréteur ou exécuteur.
5. **Prévention :** Deny-by-default, contrôles objet et fonction côté serveur, scoping par utilisateur/tenant. **Point spécifique :** Éviter l’interpréteur ; employer des API dédiées, arguments séparés et listes autorisées.
6. **Correction sécurisée :** Ajouter policy/guard serveur pour chaque action ; contraindre les requêtes par propriétaire et organisation. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un nom de fichier avec caractères spéciaux ne doit jamais déclencher de commande. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Matrice d’autorisations et tests négatifs pour toute nouvelle route. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 064 — Mass Assignment

1. **Description / fonctionnement :** Associe automatiquement des champs sensibles fournis par le client.
2. **Causes techniques :** Champs ou fonctions d’autorisation déduits du client ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** routes, contrôleurs, services, modèles, fichiers, espace administrateur et tenant_id ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Tracer chaque action jusqu’à la vérification d’autorisation serveur et simuler des accès entre comptes de test. Rechercher spécialement : champs ou fonctions d’autorisation déduits du client.
5. **Prévention :** Deny-by-default, contrôles objet et fonction côté serveur, scoping par utilisateur/tenant. **Point spécifique :** Autoriser explicitement les champs modifiables et imposer des policies serveur par rôle/fonction.
6. **Correction sécurisée :** Ajouter policy/guard serveur pour chaque action ; contraindre les requêtes par propriétaire et organisation. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un utilisateur standard ne peut pas passer role=admin ni modifier une propriété cachée. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Matrice d’autorisations et tests négatifs pour toute nouvelle route. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 065 — Parameter Tampering

1. **Description / fonctionnement :** Modifie des paramètres métier ou d'accès côté client.
2. **Causes techniques :** Champs ou fonctions d’autorisation déduits du client ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** routes, contrôleurs, services, modèles, fichiers, espace administrateur et tenant_id ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Tracer chaque action jusqu’à la vérification d’autorisation serveur et simuler des accès entre comptes de test. Rechercher spécialement : champs ou fonctions d’autorisation déduits du client.
5. **Prévention :** Deny-by-default, contrôles objet et fonction côté serveur, scoping par utilisateur/tenant. **Point spécifique :** Autoriser explicitement les champs modifiables et imposer des policies serveur par rôle/fonction.
6. **Correction sécurisée :** Ajouter policy/guard serveur pour chaque action ; contraindre les requêtes par propriétaire et organisation. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un utilisateur standard ne peut pas passer role=admin ni modifier une propriété cachée. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Matrice d’autorisations et tests négatifs pour toute nouvelle route. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 066 — Role Manipulation

1. **Description / fonctionnement :** Modifie frauduleusement des rôles ou attributions.
2. **Causes techniques :** Champs ou fonctions d’autorisation déduits du client ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** routes, contrôleurs, services, modèles, fichiers, espace administrateur et tenant_id ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Tracer chaque action jusqu’à la vérification d’autorisation serveur et simuler des accès entre comptes de test. Rechercher spécialement : champs ou fonctions d’autorisation déduits du client.
5. **Prévention :** Deny-by-default, contrôles objet et fonction côté serveur, scoping par utilisateur/tenant. **Point spécifique :** Autoriser explicitement les champs modifiables et imposer des policies serveur par rôle/fonction.
6. **Correction sécurisée :** Ajouter policy/guard serveur pour chaque action ; contraindre les requêtes par propriétaire et organisation. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un utilisateur standard ne peut pas passer role=admin ni modifier une propriété cachée. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Matrice d’autorisations et tests négatifs pour toute nouvelle route. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 067 — Tenant Isolation Bypass

1. **Description / fonctionnement :** Traverse la frontière entre organisations SaaS.
2. **Causes techniques :** Identifiant d’objet utilisé sans contrôle d’appartenance ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** routes, contrôleurs, services, modèles, fichiers, espace administrateur et tenant_id ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Tracer chaque action jusqu’à la vérification d’autorisation serveur et simuler des accès entre comptes de test. Rechercher spécialement : identifiant d’objet utilisé sans contrôle d’appartenance.
5. **Prévention :** Deny-by-default, contrôles objet et fonction côté serveur, scoping par utilisateur/tenant. **Point spécifique :** Récupérer les objets avec filtre tenant/propriétaire et autorisation serveur à chaque opération.
6. **Correction sécurisée :** Ajouter policy/guard serveur pour chaque action ; contraindre les requêtes par propriétaire et organisation. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Changer seulement l’ID vers un objet du second compte renvoie 403 ou 404. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Matrice d’autorisations et tests négatifs pour toute nouvelle route. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 068 — Insecure Direct File Access

1. **Description / fonctionnement :** Accède à une ressource privée via son URL directe.
2. **Causes techniques :** Chemins dérivés d’entrées non fiables ou fichiers servis trop librement ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** routes, contrôleurs, services, modèles, fichiers, espace administrateur et tenant_id ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Tracer chaque action jusqu’à la vérification d’autorisation serveur et simuler des accès entre comptes de test. Rechercher spécialement : chemins dérivés d’entrées non fiables ou fichiers servis trop librement.
5. **Prévention :** Deny-by-default, contrôles objet et fonction côté serveur, scoping par utilisateur/tenant. **Point spécifique :** Chemins canoniques, stockage privé hors webroot, streaming sous autorisation et contrôle type/taille.
6. **Correction sécurisée :** Ajouter policy/guard serveur pour chaque action ; contraindre les requêtes par propriétaire et organisation. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un chemin parent ou téléchargement d’un autre compte est refusé ; upload non exécutable. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Matrice d’autorisations et tests négatifs pour toute nouvelle route. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 069 — Missing Function-Level Authorization

1. **Description / fonctionnement :** Appelle une fonction sans contrôle de rôle.
2. **Causes techniques :** Champs ou fonctions d’autorisation déduits du client ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** routes, contrôleurs, services, modèles, fichiers, espace administrateur et tenant_id ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Tracer chaque action jusqu’à la vérification d’autorisation serveur et simuler des accès entre comptes de test. Rechercher spécialement : champs ou fonctions d’autorisation déduits du client.
5. **Prévention :** Deny-by-default, contrôles objet et fonction côté serveur, scoping par utilisateur/tenant. **Point spécifique :** Autoriser explicitement les champs modifiables et imposer des policies serveur par rôle/fonction.
6. **Correction sécurisée :** Ajouter policy/guard serveur pour chaque action ; contraindre les requêtes par propriétaire et organisation. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un utilisateur standard ne peut pas passer role=admin ni modifier une propriété cachée. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Matrice d’autorisations et tests négatifs pour toute nouvelle route. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 070 — Workflow Authorization Bypass

1. **Description / fonctionnement :** Saute une approbation ou vérification d'autorisation intermédiaire.
2. **Causes techniques :** Valeurs métier et transitions influencées par le client ou état concurrent ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** routes, contrôleurs, services, modèles, fichiers, espace administrateur et tenant_id ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Tracer chaque action jusqu’à la vérification d’autorisation serveur et simuler des accès entre comptes de test. Rechercher spécialement : valeurs métier et transitions influencées par le client ou état concurrent.
5. **Prévention :** Deny-by-default, contrôles objet et fonction côté serveur, scoping par utilisateur/tenant. **Point spécifique :** Recalcul serveur, contraintes SQL, transaction atomique, idempotency keys et machine à états.
6. **Correction sécurisée :** Ajouter policy/guard serveur pour chaque action ; contraindre les requêtes par propriétaire et organisation. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une opération répétée, négative ou concurrente ne modifie pas illégalement le solde/stock. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : compromission de comptes, divulgation de données ou actions non autorisées.
9. **Prévention de réapparition :** Matrice d’autorisations et tests négatifs pour toute nouvelle route. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».
