# 11 — Cloud, DevOps et supply chain

**Couverture :** 17 types d’attaque numérotés 171 à 187. Cet inventaire identifie des familles, variantes et scénarios ; certains termes se recoupent.

**Utilisation :** lire les profils liés à la surface attaquée. Les risques sont indicatifs et se recalculent selon exposition, impact, contrôle existant et vraisemblance. Ne pas effectuer de tests actifs sur des systèmes non autorisés.

## 171 — Cloud Misconfiguration

1. **Description / fonctionnement :** Exposition due aux règles de sécurité cloud non adaptées.
2. **Causes techniques :** Infrastructure ou chaîne de compilation trop permissive ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** cloud IAM, stockage, conteneurs, clusters, paquets, dépôts Git et pipeline CI/CD ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Auditer configurations et inventaire sbom ; scanner secrets sans les afficher ; examiner versions et permissions. Rechercher spécialement : infrastructure ou chaîne de compilation trop permissive.
5. **Prévention :** IAM least-privilege, pinning de dépendances, signatures, secrets manager et réseau privé. **Point spécifique :** Appliquer least privilege, pinning, SBOM, scans, signatures et réseau privé.
6. **Correction sécurisée :** Retirer accès publics inutiles, renouveler secrets compromis et verrouiller les versions. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un rôle de test ne peut pas lire hors de sa portée ; une dépendance non approuvée est bloquée. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Surveiller CVE, mises à jour et provenance des artefacts. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 172 — Exposed Storage Bucket

1. **Description / fonctionnement :** Rend des objets stockés accessibles publiquement.
2. **Causes techniques :** Données externes traitées comme directives ou actions ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** cloud IAM, stockage, conteneurs, clusters, paquets, dépôts Git et pipeline CI/CD ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Auditer configurations et inventaire sbom ; scanner secrets sans les afficher ; examiner versions et permissions. Rechercher spécialement : données externes traitées comme directives ou actions.
5. **Prévention :** IAM least-privilege, pinning de dépendances, signatures, secrets manager et réseau privé. **Point spécifique :** Outils à droits minimaux ; séparer contenu externe et instructions ; validation et approbation des actions sensibles.
6. **Correction sécurisée :** Retirer accès publics inutiles, renouveler secrets compromis et verrouiller les versions. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une instruction hostile de test intégrée à un document n’entraîne aucune action privilégiée. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Surveiller CVE, mises à jour et provenance des artefacts. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 173 — IAM Privilege Escalation

1. **Description / fonctionnement :** Abuse de permissions ou rôles IAM trop larges.
2. **Causes techniques :** Infrastructure ou chaîne de compilation trop permissive ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** cloud IAM, stockage, conteneurs, clusters, paquets, dépôts Git et pipeline CI/CD ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Auditer configurations et inventaire sbom ; scanner secrets sans les afficher ; examiner versions et permissions. Rechercher spécialement : infrastructure ou chaîne de compilation trop permissive.
5. **Prévention :** IAM least-privilege, pinning de dépendances, signatures, secrets manager et réseau privé. **Point spécifique :** Appliquer least privilege, pinning, SBOM, scans, signatures et réseau privé.
6. **Correction sécurisée :** Retirer accès publics inutiles, renouveler secrets compromis et verrouiller les versions. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un rôle de test ne peut pas lire hors de sa portée ; une dépendance non approuvée est bloquée. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Surveiller CVE, mises à jour et provenance des artefacts. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 174 — Cloud Credential Theft

1. **Description / fonctionnement :** Soustrait des identifiants cloud.
2. **Causes techniques :** Infrastructure ou chaîne de compilation trop permissive ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** cloud IAM, stockage, conteneurs, clusters, paquets, dépôts Git et pipeline CI/CD ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Auditer configurations et inventaire sbom ; scanner secrets sans les afficher ; examiner versions et permissions. Rechercher spécialement : infrastructure ou chaîne de compilation trop permissive.
5. **Prévention :** IAM least-privilege, pinning de dépendances, signatures, secrets manager et réseau privé. **Point spécifique :** Appliquer least privilege, pinning, SBOM, scans, signatures et réseau privé.
6. **Correction sécurisée :** Retirer accès publics inutiles, renouveler secrets compromis et verrouiller les versions. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un rôle de test ne peut pas lire hors de sa portée ; une dépendance non approuvée est bloquée. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Surveiller CVE, mises à jour et provenance des artefacts. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 175 — Container Escape

1. **Description / fonctionnement :** Traverse l'isolation d'un conteneur.
2. **Causes techniques :** Infrastructure ou chaîne de compilation trop permissive ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** cloud IAM, stockage, conteneurs, clusters, paquets, dépôts Git et pipeline CI/CD ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Auditer configurations et inventaire sbom ; scanner secrets sans les afficher ; examiner versions et permissions. Rechercher spécialement : infrastructure ou chaîne de compilation trop permissive.
5. **Prévention :** IAM least-privilege, pinning de dépendances, signatures, secrets manager et réseau privé. **Point spécifique :** Appliquer least privilege, pinning, SBOM, scans, signatures et réseau privé.
6. **Correction sécurisée :** Retirer accès publics inutiles, renouveler secrets compromis et verrouiller les versions. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un rôle de test ne peut pas lire hors de sa portée ; une dépendance non approuvée est bloquée. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Surveiller CVE, mises à jour et provenance des artefacts. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 176 — Kubernetes Misconfiguration

1. **Description / fonctionnement :** Abuse d'un cluster et de ressources mal configurés.
2. **Causes techniques :** Infrastructure ou chaîne de compilation trop permissive ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** cloud IAM, stockage, conteneurs, clusters, paquets, dépôts Git et pipeline CI/CD ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Auditer configurations et inventaire sbom ; scanner secrets sans les afficher ; examiner versions et permissions. Rechercher spécialement : infrastructure ou chaîne de compilation trop permissive.
5. **Prévention :** IAM least-privilege, pinning de dépendances, signatures, secrets manager et réseau privé. **Point spécifique :** Appliquer least privilege, pinning, SBOM, scans, signatures et réseau privé.
6. **Correction sécurisée :** Retirer accès publics inutiles, renouveler secrets compromis et verrouiller les versions. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un rôle de test ne peut pas lire hors de sa portée ; une dépendance non approuvée est bloquée. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Surveiller CVE, mises à jour et provenance des artefacts. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 177 — Exposed Kubernetes Dashboard

1. **Description / fonctionnement :** Accède à une console de cluster exposée.
2. **Causes techniques :** Infrastructure ou chaîne de compilation trop permissive ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** cloud IAM, stockage, conteneurs, clusters, paquets, dépôts Git et pipeline CI/CD ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Auditer configurations et inventaire sbom ; scanner secrets sans les afficher ; examiner versions et permissions. Rechercher spécialement : infrastructure ou chaîne de compilation trop permissive.
5. **Prévention :** IAM least-privilege, pinning de dépendances, signatures, secrets manager et réseau privé. **Point spécifique :** Appliquer least privilege, pinning, SBOM, scans, signatures et réseau privé.
6. **Correction sécurisée :** Retirer accès publics inutiles, renouveler secrets compromis et verrouiller les versions. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un rôle de test ne peut pas lire hors de sa portée ; une dépendance non approuvée est bloquée. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Surveiller CVE, mises à jour et provenance des artefacts. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 178 — CI/CD Pipeline Compromise

1. **Description / fonctionnement :** Modifie des étapes d'intégration ou déploiement.
2. **Causes techniques :** Infrastructure ou chaîne de compilation trop permissive ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** cloud IAM, stockage, conteneurs, clusters, paquets, dépôts Git et pipeline CI/CD ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Auditer configurations et inventaire sbom ; scanner secrets sans les afficher ; examiner versions et permissions. Rechercher spécialement : infrastructure ou chaîne de compilation trop permissive.
5. **Prévention :** IAM least-privilege, pinning de dépendances, signatures, secrets manager et réseau privé. **Point spécifique :** Appliquer least privilege, pinning, SBOM, scans, signatures et réseau privé.
6. **Correction sécurisée :** Retirer accès publics inutiles, renouveler secrets compromis et verrouiller les versions. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un rôle de test ne peut pas lire hors de sa portée ; une dépendance non approuvée est bloquée. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Surveiller CVE, mises à jour et provenance des artefacts. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 179 — Dependency Confusion

1. **Description / fonctionnement :** Fait installer une dépendance publique à la place d'une interne.
2. **Causes techniques :** Infrastructure ou chaîne de compilation trop permissive ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** cloud IAM, stockage, conteneurs, clusters, paquets, dépôts Git et pipeline CI/CD ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Auditer configurations et inventaire sbom ; scanner secrets sans les afficher ; examiner versions et permissions. Rechercher spécialement : infrastructure ou chaîne de compilation trop permissive.
5. **Prévention :** IAM least-privilege, pinning de dépendances, signatures, secrets manager et réseau privé. **Point spécifique :** Appliquer least privilege, pinning, SBOM, scans, signatures et réseau privé.
6. **Correction sécurisée :** Retirer accès publics inutiles, renouveler secrets compromis et verrouiller les versions. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un rôle de test ne peut pas lire hors de sa portée ; une dépendance non approuvée est bloquée. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Surveiller CVE, mises à jour et provenance des artefacts. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 180 — Typosquatting Package Attack

1. **Description / fonctionnement :** Introduit un paquet avec un nom trompeusement proche.
2. **Causes techniques :** Infrastructure ou chaîne de compilation trop permissive ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** cloud IAM, stockage, conteneurs, clusters, paquets, dépôts Git et pipeline CI/CD ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Auditer configurations et inventaire sbom ; scanner secrets sans les afficher ; examiner versions et permissions. Rechercher spécialement : infrastructure ou chaîne de compilation trop permissive.
5. **Prévention :** IAM least-privilege, pinning de dépendances, signatures, secrets manager et réseau privé. **Point spécifique :** Appliquer least privilege, pinning, SBOM, scans, signatures et réseau privé.
6. **Correction sécurisée :** Retirer accès publics inutiles, renouveler secrets compromis et verrouiller les versions. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un rôle de test ne peut pas lire hors de sa portée ; une dépendance non approuvée est bloquée. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Surveiller CVE, mises à jour et provenance des artefacts. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 181 — Supply Chain Attack

1. **Description / fonctionnement :** Compromet un fournisseur ou une dépendance de confiance.
2. **Causes techniques :** Infrastructure ou chaîne de compilation trop permissive ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** cloud IAM, stockage, conteneurs, clusters, paquets, dépôts Git et pipeline CI/CD ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Auditer configurations et inventaire sbom ; scanner secrets sans les afficher ; examiner versions et permissions. Rechercher spécialement : infrastructure ou chaîne de compilation trop permissive.
5. **Prévention :** IAM least-privilege, pinning de dépendances, signatures, secrets manager et réseau privé. **Point spécifique :** Appliquer least privilege, pinning, SBOM, scans, signatures et réseau privé.
6. **Correction sécurisée :** Retirer accès publics inutiles, renouveler secrets compromis et verrouiller les versions. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un rôle de test ne peut pas lire hors de sa portée ; une dépendance non approuvée est bloquée. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Surveiller CVE, mises à jour et provenance des artefacts. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 182 — Malicious Package Injection

1. **Description / fonctionnement :** Introduit du code malveillant dans une bibliothèque.
2. **Causes techniques :** Infrastructure ou chaîne de compilation trop permissive ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** cloud IAM, stockage, conteneurs, clusters, paquets, dépôts Git et pipeline CI/CD ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Auditer configurations et inventaire sbom ; scanner secrets sans les afficher ; examiner versions et permissions. Rechercher spécialement : infrastructure ou chaîne de compilation trop permissive.
5. **Prévention :** IAM least-privilege, pinning de dépendances, signatures, secrets manager et réseau privé. **Point spécifique :** Appliquer least privilege, pinning, SBOM, scans, signatures et réseau privé.
6. **Correction sécurisée :** Retirer accès publics inutiles, renouveler secrets compromis et verrouiller les versions. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un rôle de test ne peut pas lire hors de sa portée ; une dépendance non approuvée est bloquée. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Surveiller CVE, mises à jour et provenance des artefacts. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 183 — Secret Leakage

1. **Description / fonctionnement :** Expose des clés, tokens ou mots de passe.
2. **Causes techniques :** Secrets persistants ou transmis à un mauvais destinataire ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** cloud IAM, stockage, conteneurs, clusters, paquets, dépôts Git et pipeline CI/CD ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Auditer configurations et inventaire sbom ; scanner secrets sans les afficher ; examiner versions et permissions. Rechercher spécialement : secrets persistants ou transmis à un mauvais destinataire.
5. **Prévention :** IAM least-privilege, pinning de dépendances, signatures, secrets manager et réseau privé. **Point spécifique :** Stocker en gestionnaire de secrets, réduire la portée et effectuer rotation et révocation.
6. **Correction sécurisée :** Retirer accès publics inutiles, renouveler secrets compromis et verrouiller les versions. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Clés invalides ou retirées ne fonctionnent plus ; aucun secret dans logs et réponses. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Surveiller CVE, mises à jour et provenance des artefacts. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 184 — Git Repository Exposure

1. **Description / fonctionnement :** Expose l'historique et les fichiers Git.
2. **Causes techniques :** Infrastructure ou chaîne de compilation trop permissive ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** cloud IAM, stockage, conteneurs, clusters, paquets, dépôts Git et pipeline CI/CD ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Auditer configurations et inventaire sbom ; scanner secrets sans les afficher ; examiner versions et permissions. Rechercher spécialement : infrastructure ou chaîne de compilation trop permissive.
5. **Prévention :** IAM least-privilege, pinning de dépendances, signatures, secrets manager et réseau privé. **Point spécifique :** Appliquer least privilege, pinning, SBOM, scans, signatures et réseau privé.
6. **Correction sécurisée :** Retirer accès publics inutiles, renouveler secrets compromis et verrouiller les versions. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un rôle de test ne peut pas lire hors de sa portée ; une dépendance non approuvée est bloquée. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Surveiller CVE, mises à jour et provenance des artefacts. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 185 — Docker Socket Exposure

1. **Description / fonctionnement :** Rend accessible le socket de contrôle Docker.
2. **Causes techniques :** Infrastructure ou chaîne de compilation trop permissive ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** cloud IAM, stockage, conteneurs, clusters, paquets, dépôts Git et pipeline CI/CD ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Auditer configurations et inventaire sbom ; scanner secrets sans les afficher ; examiner versions et permissions. Rechercher spécialement : infrastructure ou chaîne de compilation trop permissive.
5. **Prévention :** IAM least-privilege, pinning de dépendances, signatures, secrets manager et réseau privé. **Point spécifique :** Appliquer least privilege, pinning, SBOM, scans, signatures et réseau privé.
6. **Correction sécurisée :** Retirer accès publics inutiles, renouveler secrets compromis et verrouiller les versions. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un rôle de test ne peut pas lire hors de sa portée ; une dépendance non approuvée est bloquée. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Surveiller CVE, mises à jour et provenance des artefacts. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 186 — Infrastructure as Code Misconfiguration

1. **Description / fonctionnement :** Déploie des ressources à partir de paramètres IaC dangereux.
2. **Causes techniques :** Infrastructure ou chaîne de compilation trop permissive ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** cloud IAM, stockage, conteneurs, clusters, paquets, dépôts Git et pipeline CI/CD ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Auditer configurations et inventaire sbom ; scanner secrets sans les afficher ; examiner versions et permissions. Rechercher spécialement : infrastructure ou chaîne de compilation trop permissive.
5. **Prévention :** IAM least-privilege, pinning de dépendances, signatures, secrets manager et réseau privé. **Point spécifique :** Appliquer least privilege, pinning, SBOM, scans, signatures et réseau privé.
6. **Correction sécurisée :** Retirer accès publics inutiles, renouveler secrets compromis et verrouiller les versions. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un rôle de test ne peut pas lire hors de sa portée ; une dépendance non approuvée est bloquée. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Surveiller CVE, mises à jour et provenance des artefacts. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 187 — Build Artifact Tampering

1. **Description / fonctionnement :** Modifie le résultat final d'une compilation ou livraison.
2. **Causes techniques :** Infrastructure ou chaîne de compilation trop permissive ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** cloud IAM, stockage, conteneurs, clusters, paquets, dépôts Git et pipeline CI/CD ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Auditer configurations et inventaire sbom ; scanner secrets sans les afficher ; examiner versions et permissions. Rechercher spécialement : infrastructure ou chaîne de compilation trop permissive.
5. **Prévention :** IAM least-privilege, pinning de dépendances, signatures, secrets manager et réseau privé. **Point spécifique :** Appliquer least privilege, pinning, SBOM, scans, signatures et réseau privé.
6. **Correction sécurisée :** Retirer accès publics inutiles, renouveler secrets compromis et verrouiller les versions. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Un rôle de test ne peut pas lire hors de sa portée ; une dépendance non approuvée est bloquée. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : exfiltration, indisponibilité, compromission ou fraude selon le contexte.
9. **Prévention de réapparition :** Surveiller CVE, mises à jour et provenance des artefacts. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».
