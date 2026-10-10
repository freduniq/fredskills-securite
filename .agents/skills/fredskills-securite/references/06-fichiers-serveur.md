# 06 — Fichiers et serveur

**Couverture :** 20 types d’attaque numérotés 86 à 105. Cet inventaire identifie des familles, variantes et scénarios ; certains termes se recoupent.

**Utilisation :** lire les profils liés à la surface attaquée. Les risques sont indicatifs et se recalculent selon exposition, impact, contrôle existant et vraisemblance. Ne pas effectuer de tests actifs sur des systèmes non autorisés.

## 086 — LFI

1. **Description / fonctionnement :** Charge un fichier local sous le contrôle d'un paramètre.
2. **Causes techniques :** Chemins dérivés d’entrées non fiables ou fichiers servis trop librement ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** téléversement, téléchargements, répertoires publics, sérialisation et serveur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Inspecter le chemin de stockage/exécution, résolution de chemins, mime, extensions et droits du serveur. Rechercher spécialement : chemins dérivés d’entrées non fiables ou fichiers servis trop librement.
5. **Prévention :** Stockage hors webroot, noms aléatoires, allowlists, permissions OS minimales, désérialisation sûre. **Point spécifique :** Chemins canoniques, stockage privé hors webroot, streaming sous autorisation et contrôle type/taille.
6. **Correction sécurisée :** Séparer upload et exécution ; contrôler chemin canonique et appartenances avant chaque accès. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un chemin parent ou téléchargement d’un autre compte est refusé ; upload non exécutable. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Mettre à jour les bibliothèques et auditer permissions et fichiers publiés. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 087 — RFI

1. **Description / fonctionnement :** Charge un fichier distant en tant que ressource exécutable.
2. **Causes techniques :** Chemins dérivés d’entrées non fiables ou fichiers servis trop librement ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** téléversement, téléchargements, répertoires publics, sérialisation et serveur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Inspecter le chemin de stockage/exécution, résolution de chemins, mime, extensions et droits du serveur. Rechercher spécialement : chemins dérivés d’entrées non fiables ou fichiers servis trop librement.
5. **Prévention :** Stockage hors webroot, noms aléatoires, allowlists, permissions OS minimales, désérialisation sûre. **Point spécifique :** Chemins canoniques, stockage privé hors webroot, streaming sous autorisation et contrôle type/taille.
6. **Correction sécurisée :** Séparer upload et exécution ; contrôler chemin canonique et appartenances avant chaque accès. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un chemin parent ou téléchargement d’un autre compte est refusé ; upload non exécutable. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Mettre à jour les bibliothèques et auditer permissions et fichiers publiés. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 088 — Path Traversal

1. **Description / fonctionnement :** Remonte hors du répertoire autorisé pour accéder à des fichiers.
2. **Causes techniques :** Chemins dérivés d’entrées non fiables ou fichiers servis trop librement ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** téléversement, téléchargements, répertoires publics, sérialisation et serveur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Inspecter le chemin de stockage/exécution, résolution de chemins, mime, extensions et droits du serveur. Rechercher spécialement : chemins dérivés d’entrées non fiables ou fichiers servis trop librement.
5. **Prévention :** Stockage hors webroot, noms aléatoires, allowlists, permissions OS minimales, désérialisation sûre. **Point spécifique :** Chemins canoniques, stockage privé hors webroot, streaming sous autorisation et contrôle type/taille.
6. **Correction sécurisée :** Séparer upload et exécution ; contrôler chemin canonique et appartenances avant chaque accès. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un chemin parent ou téléchargement d’un autre compte est refusé ; upload non exécutable. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Mettre à jour les bibliothèques et auditer permissions et fichiers publiés. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 089 — Arbitrary File Upload

1. **Description / fonctionnement :** Dépose un fichier dangereux qui peut être interprété ou servi.
2. **Causes techniques :** Chemins dérivés d’entrées non fiables ou fichiers servis trop librement ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** téléversement, téléchargements, répertoires publics, sérialisation et serveur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Inspecter le chemin de stockage/exécution, résolution de chemins, mime, extensions et droits du serveur. Rechercher spécialement : chemins dérivés d’entrées non fiables ou fichiers servis trop librement.
5. **Prévention :** Stockage hors webroot, noms aléatoires, allowlists, permissions OS minimales, désérialisation sûre. **Point spécifique :** Chemins canoniques, stockage privé hors webroot, streaming sous autorisation et contrôle type/taille.
6. **Correction sécurisée :** Séparer upload et exécution ; contrôler chemin canonique et appartenances avant chaque accès. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un chemin parent ou téléchargement d’un autre compte est refusé ; upload non exécutable. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Mettre à jour les bibliothèques et auditer permissions et fichiers publiés. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 090 — Unrestricted File Upload

1. **Description / fonctionnement :** Téléverse des fichiers sans limites de type, taille ou destination.
2. **Causes techniques :** Chemins dérivés d’entrées non fiables ou fichiers servis trop librement ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** téléversement, téléchargements, répertoires publics, sérialisation et serveur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Inspecter le chemin de stockage/exécution, résolution de chemins, mime, extensions et droits du serveur. Rechercher spécialement : chemins dérivés d’entrées non fiables ou fichiers servis trop librement.
5. **Prévention :** Stockage hors webroot, noms aléatoires, allowlists, permissions OS minimales, désérialisation sûre. **Point spécifique :** Chemins canoniques, stockage privé hors webroot, streaming sous autorisation et contrôle type/taille.
6. **Correction sécurisée :** Séparer upload et exécution ; contrôler chemin canonique et appartenances avant chaque accès. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un chemin parent ou téléchargement d’un autre compte est refusé ; upload non exécutable. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Mettre à jour les bibliothèques et auditer permissions et fichiers publiés. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 091 — File Overwrite

1. **Description / fonctionnement :** Remplace des fichiers existants via une destination non maîtrisée.
2. **Causes techniques :** Chemins dérivés d’entrées non fiables ou fichiers servis trop librement ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** téléversement, téléchargements, répertoires publics, sérialisation et serveur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Inspecter le chemin de stockage/exécution, résolution de chemins, mime, extensions et droits du serveur. Rechercher spécialement : chemins dérivés d’entrées non fiables ou fichiers servis trop librement.
5. **Prévention :** Stockage hors webroot, noms aléatoires, allowlists, permissions OS minimales, désérialisation sûre. **Point spécifique :** Chemins canoniques, stockage privé hors webroot, streaming sous autorisation et contrôle type/taille.
6. **Correction sécurisée :** Séparer upload et exécution ; contrôler chemin canonique et appartenances avant chaque accès. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un chemin parent ou téléchargement d’un autre compte est refusé ; upload non exécutable. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Mettre à jour les bibliothèques et auditer permissions et fichiers publiés. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 092 — Arbitrary File Read

1. **Description / fonctionnement :** Lit des fichiers hors du périmètre autorisé.
2. **Causes techniques :** Chemins dérivés d’entrées non fiables ou fichiers servis trop librement ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** téléversement, téléchargements, répertoires publics, sérialisation et serveur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Inspecter le chemin de stockage/exécution, résolution de chemins, mime, extensions et droits du serveur. Rechercher spécialement : chemins dérivés d’entrées non fiables ou fichiers servis trop librement.
5. **Prévention :** Stockage hors webroot, noms aléatoires, allowlists, permissions OS minimales, désérialisation sûre. **Point spécifique :** Chemins canoniques, stockage privé hors webroot, streaming sous autorisation et contrôle type/taille.
6. **Correction sécurisée :** Séparer upload et exécution ; contrôler chemin canonique et appartenances avant chaque accès. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un chemin parent ou téléchargement d’un autre compte est refusé ; upload non exécutable. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Mettre à jour les bibliothèques et auditer permissions et fichiers publiés. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 093 — Arbitrary File Deletion

1. **Description / fonctionnement :** Supprime des fichiers hors du périmètre autorisé.
2. **Causes techniques :** Chemins dérivés d’entrées non fiables ou fichiers servis trop librement ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** téléversement, téléchargements, répertoires publics, sérialisation et serveur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Inspecter le chemin de stockage/exécution, résolution de chemins, mime, extensions et droits du serveur. Rechercher spécialement : chemins dérivés d’entrées non fiables ou fichiers servis trop librement.
5. **Prévention :** Stockage hors webroot, noms aléatoires, allowlists, permissions OS minimales, désérialisation sûre. **Point spécifique :** Chemins canoniques, stockage privé hors webroot, streaming sous autorisation et contrôle type/taille.
6. **Correction sécurisée :** Séparer upload et exécution ; contrôler chemin canonique et appartenances avant chaque accès. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un chemin parent ou téléchargement d’un autre compte est refusé ; upload non exécutable. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Mettre à jour les bibliothèques et auditer permissions et fichiers publiés. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 094 — Remote Code Execution (RCE)

1. **Description / fonctionnement :** Exécute des instructions sur le serveur à distance.
2. **Causes techniques :** Entrée transmise à un interpréteur ou exécuteur ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** téléversement, téléchargements, répertoires publics, sérialisation et serveur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Inspecter le chemin de stockage/exécution, résolution de chemins, mime, extensions et droits du serveur. Rechercher spécialement : entrée transmise à un interpréteur ou exécuteur.
5. **Prévention :** Stockage hors webroot, noms aléatoires, allowlists, permissions OS minimales, désérialisation sûre. **Point spécifique :** Éviter l’interpréteur ; employer des API dédiées, arguments séparés et listes autorisées.
6. **Correction sécurisée :** Séparer upload et exécution ; contrôler chemin canonique et appartenances avant chaque accès. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un nom de fichier avec caractères spéciaux ne doit jamais déclencher de commande. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Mettre à jour les bibliothèques et auditer permissions et fichiers publiés. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 095 — Local Privilege Escalation

1. **Description / fonctionnement :** Gagne plus de privilèges après un accès serveur initial.
2. **Causes techniques :** Champs ou fonctions d’autorisation déduits du client ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** téléversement, téléchargements, répertoires publics, sérialisation et serveur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Inspecter le chemin de stockage/exécution, résolution de chemins, mime, extensions et droits du serveur. Rechercher spécialement : champs ou fonctions d’autorisation déduits du client.
5. **Prévention :** Stockage hors webroot, noms aléatoires, allowlists, permissions OS minimales, désérialisation sûre. **Point spécifique :** Autoriser explicitement les champs modifiables et imposer des policies serveur par rôle/fonction.
6. **Correction sécurisée :** Séparer upload et exécution ; contrôler chemin canonique et appartenances avant chaque accès. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un utilisateur standard ne peut pas passer role=admin ni modifier une propriété cachée. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Mettre à jour les bibliothèques et auditer permissions et fichiers publiés. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 096 — Insecure Deserialization

1. **Description / fonctionnement :** Restaure des objets non fiables pouvant déclencher des effets indésirables.
2. **Causes techniques :** Désérialisation d’objets arbitraires non fiables ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** téléversement, téléchargements, répertoires publics, sérialisation et serveur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Inspecter le chemin de stockage/exécution, résolution de chemins, mime, extensions et droits du serveur. Rechercher spécialement : désérialisation d’objets arbitraires non fiables.
5. **Prévention :** Stockage hors webroot, noms aléatoires, allowlists, permissions OS minimales, désérialisation sûre. **Point spécifique :** Éviter la désérialisation d’objets ; utiliser JSON typé et validations de schéma.
6. **Correction sécurisée :** Séparer upload et exécution ; contrôler chemin canonique et appartenances avant chaque accès. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une structure de classe inattendue est refusée sans appel de méthode spéciale. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Mettre à jour les bibliothèques et auditer permissions et fichiers publiés. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 097 — PHP Object Injection

1. **Description / fonctionnement :** Provoque des appels de méthodes magiques à la désérialisation PHP.
2. **Causes techniques :** Désérialisation d’objets arbitraires non fiables ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** téléversement, téléchargements, répertoires publics, sérialisation et serveur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Inspecter le chemin de stockage/exécution, résolution de chemins, mime, extensions et droits du serveur. Rechercher spécialement : désérialisation d’objets arbitraires non fiables.
5. **Prévention :** Stockage hors webroot, noms aléatoires, allowlists, permissions OS minimales, désérialisation sûre. **Point spécifique :** Éviter la désérialisation d’objets ; utiliser JSON typé et validations de schéma.
6. **Correction sécurisée :** Séparer upload et exécution ; contrôler chemin canonique et appartenances avant chaque accès. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une structure de classe inattendue est refusée sans appel de méthode spéciale. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Mettre à jour les bibliothèques et auditer permissions et fichiers publiés. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 098 — Insecure Temporary Files

1. **Description / fonctionnement :** Abuse de fichiers temporaires accessibles ou prédictibles.
2. **Causes techniques :** Chemins dérivés d’entrées non fiables ou fichiers servis trop librement ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** téléversement, téléchargements, répertoires publics, sérialisation et serveur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Inspecter le chemin de stockage/exécution, résolution de chemins, mime, extensions et droits du serveur. Rechercher spécialement : chemins dérivés d’entrées non fiables ou fichiers servis trop librement.
5. **Prévention :** Stockage hors webroot, noms aléatoires, allowlists, permissions OS minimales, désérialisation sûre. **Point spécifique :** Chemins canoniques, stockage privé hors webroot, streaming sous autorisation et contrôle type/taille.
6. **Correction sécurisée :** Séparer upload et exécution ; contrôler chemin canonique et appartenances avant chaque accès. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un chemin parent ou téléchargement d’un autre compte est refusé ; upload non exécutable. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Mettre à jour les bibliothèques et auditer permissions et fichiers publiés. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 099 — Exposed Backup Files

1. **Description / fonctionnement :** Récupère des sauvegardes publiées par erreur.
2. **Causes techniques :** Chemins dérivés d’entrées non fiables ou fichiers servis trop librement ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** téléversement, téléchargements, répertoires publics, sérialisation et serveur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Inspecter le chemin de stockage/exécution, résolution de chemins, mime, extensions et droits du serveur. Rechercher spécialement : chemins dérivés d’entrées non fiables ou fichiers servis trop librement.
5. **Prévention :** Stockage hors webroot, noms aléatoires, allowlists, permissions OS minimales, désérialisation sûre. **Point spécifique :** Chemins canoniques, stockage privé hors webroot, streaming sous autorisation et contrôle type/taille.
6. **Correction sécurisée :** Séparer upload et exécution ; contrôler chemin canonique et appartenances avant chaque accès. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un chemin parent ou téléchargement d’un autre compte est refusé ; upload non exécutable. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Mettre à jour les bibliothèques et auditer permissions et fichiers publiés. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 100 — Exposed Environment Files

1. **Description / fonctionnement :** Récupère des fichiers .env contenant des secrets.
2. **Causes techniques :** Chemins dérivés d’entrées non fiables ou fichiers servis trop librement ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** téléversement, téléchargements, répertoires publics, sérialisation et serveur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Inspecter le chemin de stockage/exécution, résolution de chemins, mime, extensions et droits du serveur. Rechercher spécialement : chemins dérivés d’entrées non fiables ou fichiers servis trop librement.
5. **Prévention :** Stockage hors webroot, noms aléatoires, allowlists, permissions OS minimales, désérialisation sûre. **Point spécifique :** Chemins canoniques, stockage privé hors webroot, streaming sous autorisation et contrôle type/taille.
6. **Correction sécurisée :** Séparer upload et exécution ; contrôler chemin canonique et appartenances avant chaque accès. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un chemin parent ou téléchargement d’un autre compte est refusé ; upload non exécutable. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Mettre à jour les bibliothèques et auditer permissions et fichiers publiés. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 101 — Directory Listing Exposure

1. **Description / fonctionnement :** Explore un répertoire faute de page index et de restriction.
2. **Causes techniques :** Chemins dérivés d’entrées non fiables ou fichiers servis trop librement ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** téléversement, téléchargements, répertoires publics, sérialisation et serveur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Inspecter le chemin de stockage/exécution, résolution de chemins, mime, extensions et droits du serveur. Rechercher spécialement : chemins dérivés d’entrées non fiables ou fichiers servis trop librement.
5. **Prévention :** Stockage hors webroot, noms aléatoires, allowlists, permissions OS minimales, désérialisation sûre. **Point spécifique :** Chemins canoniques, stockage privé hors webroot, streaming sous autorisation et contrôle type/taille.
6. **Correction sécurisée :** Séparer upload et exécution ; contrôler chemin canonique et appartenances avant chaque accès. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un chemin parent ou téléchargement d’un autre compte est refusé ; upload non exécutable. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Mettre à jour les bibliothèques et auditer permissions et fichiers publiés. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 102 — Server Misconfiguration

1. **Description / fonctionnement :** Abuse d'une configuration serveur permissive.
2. **Causes techniques :** traitement de chemins, fichiers, objets ou configurations comme sources de confiance ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** téléversement, téléchargements, répertoires publics, sérialisation et serveur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Inspecter le chemin de stockage/exécution, résolution de chemins, mime, extensions et droits du serveur. Rechercher spécialement : traitement de chemins, fichiers, objets ou configurations comme sources de confiance.
5. **Prévention :** Stockage hors webroot, noms aléatoires, allowlists, permissions OS minimales, désérialisation sûre. **Point spécifique :** séparer upload et exécution ; contrôler chemin canonique et appartenances avant chaque accès
6. **Correction sécurisée :** Séparer upload et exécution ; contrôler chemin canonique et appartenances avant chaque accès. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** tester fichiers inoffensifs avec extensions trompeuses et tentatives de parcours normalisées ; refus attendu Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Mettre à jour les bibliothèques et auditer permissions et fichiers publiés. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 103 — Web Shell Installation

1. **Description / fonctionnement :** Déploie un script permettant des commandes persistantes.
2. **Causes techniques :** Entrée transmise à un interpréteur ou exécuteur ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** téléversement, téléchargements, répertoires publics, sérialisation et serveur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Inspecter le chemin de stockage/exécution, résolution de chemins, mime, extensions et droits du serveur. Rechercher spécialement : entrée transmise à un interpréteur ou exécuteur.
5. **Prévention :** Stockage hors webroot, noms aléatoires, allowlists, permissions OS minimales, désérialisation sûre. **Point spécifique :** Éviter l’interpréteur ; employer des API dédiées, arguments séparés et listes autorisées.
6. **Correction sécurisée :** Séparer upload et exécution ; contrôler chemin canonique et appartenances avant chaque accès. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un nom de fichier avec caractères spéciaux ne doit jamais déclencher de commande. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Mettre à jour les bibliothèques et auditer permissions et fichiers publiés. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 104 — Dependency Exploitation

1. **Description / fonctionnement :** Exploite une bibliothèque vulnérable installée.
2. **Causes techniques :** Infrastructure ou chaîne de compilation trop permissive ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** téléversement, téléchargements, répertoires publics, sérialisation et serveur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Inspecter le chemin de stockage/exécution, résolution de chemins, mime, extensions et droits du serveur. Rechercher spécialement : infrastructure ou chaîne de compilation trop permissive.
5. **Prévention :** Stockage hors webroot, noms aléatoires, allowlists, permissions OS minimales, désérialisation sûre. **Point spécifique :** Appliquer least privilege, pinning, SBOM, scans, signatures et réseau privé.
6. **Correction sécurisée :** Séparer upload et exécution ; contrôler chemin canonique et appartenances avant chaque accès. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un rôle de test ne peut pas lire hors de sa portée ; une dépendance non approuvée est bloquée. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Mettre à jour les bibliothèques et auditer permissions et fichiers publiés. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 105 — Configuration File Disclosure

1. **Description / fonctionnement :** Obtient des paramètres internes exposés.
2. **Causes techniques :** Chemins dérivés d’entrées non fiables ou fichiers servis trop librement ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** téléversement, téléchargements, répertoires publics, sérialisation et serveur ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Inspecter le chemin de stockage/exécution, résolution de chemins, mime, extensions et droits du serveur. Rechercher spécialement : chemins dérivés d’entrées non fiables ou fichiers servis trop librement.
5. **Prévention :** Stockage hors webroot, noms aléatoires, allowlists, permissions OS minimales, désérialisation sûre. **Point spécifique :** Chemins canoniques, stockage privé hors webroot, streaming sous autorisation et contrôle type/taille.
6. **Correction sécurisée :** Séparer upload et exécution ; contrôler chemin canonique et appartenances avant chaque accès. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un chemin parent ou téléchargement d’un autre compte est refusé ; upload non exécutable. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Mettre à jour les bibliothèques et auditer permissions et fichiers publiés. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».
