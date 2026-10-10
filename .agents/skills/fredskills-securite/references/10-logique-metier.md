# 10 — Transactions et logique métier

**Couverture :** 16 types d’attaque numérotés 155 à 170. Cet inventaire identifie des familles, variantes et scénarios ; certains termes se recoupent.

**Utilisation :** lire les profils liés à la surface attaquée. Les risques sont indicatifs et se recalculent selon exposition, impact, contrôle existant et vraisemblance. Ne pas effectuer de tests actifs sur des systèmes non autorisés.

## 155 — Business Logic Abuse

1. **Description / fonctionnement :** Exploite des règles métier incohérentes ou incomplètes.
2. **Causes techniques :** confiance dans état métier envoyé par le client, incohérence transactionnelle ou concurrence non gérée ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** commandes, prix, paiements, coupons, stock, validations et remboursements ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Modéliser états et transitions ; inspecter transactions, verrous et sources de vérité. Rechercher spécialement : confiance dans état métier envoyé par le client, incohérence transactionnelle ou concurrence non gérée.
5. **Prévention :** Recalculer côté serveur, transactions atomiques, idempotence et validation des transitions. **Point spécifique :** déplacer vérification de prix/état côté serveur et imposer contraintes transactionnelles en base
6. **Correction sécurisée :** Déplacer vérification de prix/état côté serveur et imposer contraintes transactionnelles en base. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** tester actions répétées, ordres inversés, valeurs limites et concurrence bornée sur données de test Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : pertes financières, incohérences comptables et abus des transactions.
9. **Prévention de réapparition :** Mettre invariants métier et tests de concurrence dans CI. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 156 — Race Condition

1. **Description / fonctionnement :** Profite de deux opérations concurrentes non synchronisées.
2. **Causes techniques :** Valeurs métier et transitions influencées par le client ou état concurrent ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** commandes, prix, paiements, coupons, stock, validations et remboursements ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Modéliser états et transitions ; inspecter transactions, verrous et sources de vérité. Rechercher spécialement : valeurs métier et transitions influencées par le client ou état concurrent.
5. **Prévention :** Recalculer côté serveur, transactions atomiques, idempotence et validation des transitions. **Point spécifique :** Recalcul serveur, contraintes SQL, transaction atomique, idempotency keys et machine à états.
6. **Correction sécurisée :** Déplacer vérification de prix/état côté serveur et imposer contraintes transactionnelles en base. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une opération répétée, négative ou concurrente ne modifie pas illégalement le solde/stock. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : pertes financières, incohérences comptables et abus des transactions.
9. **Prévention de réapparition :** Mettre invariants métier et tests de concurrence dans CI. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 157 — TOCTOU

1. **Description / fonctionnement :** Change l'état entre la vérification et l'utilisation.
2. **Causes techniques :** Valeurs métier et transitions influencées par le client ou état concurrent ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** commandes, prix, paiements, coupons, stock, validations et remboursements ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Modéliser états et transitions ; inspecter transactions, verrous et sources de vérité. Rechercher spécialement : valeurs métier et transitions influencées par le client ou état concurrent.
5. **Prévention :** Recalculer côté serveur, transactions atomiques, idempotence et validation des transitions. **Point spécifique :** Recalcul serveur, contraintes SQL, transaction atomique, idempotency keys et machine à états.
6. **Correction sécurisée :** Déplacer vérification de prix/état côté serveur et imposer contraintes transactionnelles en base. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une opération répétée, négative ou concurrente ne modifie pas illégalement le solde/stock. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : pertes financières, incohérences comptables et abus des transactions.
9. **Prévention de réapparition :** Mettre invariants métier et tests de concurrence dans CI. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 158 — Price Manipulation

1. **Description / fonctionnement :** Modifie un prix calculé ou transmis depuis le client.
2. **Causes techniques :** Valeurs métier et transitions influencées par le client ou état concurrent ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** commandes, prix, paiements, coupons, stock, validations et remboursements ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Modéliser états et transitions ; inspecter transactions, verrous et sources de vérité. Rechercher spécialement : valeurs métier et transitions influencées par le client ou état concurrent.
5. **Prévention :** Recalculer côté serveur, transactions atomiques, idempotence et validation des transitions. **Point spécifique :** Recalcul serveur, contraintes SQL, transaction atomique, idempotency keys et machine à états.
6. **Correction sécurisée :** Déplacer vérification de prix/état côté serveur et imposer contraintes transactionnelles en base. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une opération répétée, négative ou concurrente ne modifie pas illégalement le solde/stock. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : pertes financières, incohérences comptables et abus des transactions.
9. **Prévention de réapparition :** Mettre invariants métier et tests de concurrence dans CI. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 159 — Payment Bypass

1. **Description / fonctionnement :** Marque une transaction payée sans preuve serveur suffisante.
2. **Causes techniques :** Valeurs métier et transitions influencées par le client ou état concurrent ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** commandes, prix, paiements, coupons, stock, validations et remboursements ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Modéliser états et transitions ; inspecter transactions, verrous et sources de vérité. Rechercher spécialement : valeurs métier et transitions influencées par le client ou état concurrent.
5. **Prévention :** Recalculer côté serveur, transactions atomiques, idempotence et validation des transitions. **Point spécifique :** Recalcul serveur, contraintes SQL, transaction atomique, idempotency keys et machine à états.
6. **Correction sécurisée :** Déplacer vérification de prix/état côté serveur et imposer contraintes transactionnelles en base. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une opération répétée, négative ou concurrente ne modifie pas illégalement le solde/stock. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : pertes financières, incohérences comptables et abus des transactions.
9. **Prévention de réapparition :** Mettre invariants métier et tests de concurrence dans CI. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 160 — Coupon Abuse

1. **Description / fonctionnement :** Réutilise ou combine abusivement des réductions.
2. **Causes techniques :** Valeurs métier et transitions influencées par le client ou état concurrent ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** commandes, prix, paiements, coupons, stock, validations et remboursements ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Modéliser états et transitions ; inspecter transactions, verrous et sources de vérité. Rechercher spécialement : valeurs métier et transitions influencées par le client ou état concurrent.
5. **Prévention :** Recalculer côté serveur, transactions atomiques, idempotence et validation des transitions. **Point spécifique :** Recalcul serveur, contraintes SQL, transaction atomique, idempotency keys et machine à états.
6. **Correction sécurisée :** Déplacer vérification de prix/état côté serveur et imposer contraintes transactionnelles en base. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une opération répétée, négative ou concurrente ne modifie pas illégalement le solde/stock. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : pertes financières, incohérences comptables et abus des transactions.
9. **Prévention de réapparition :** Mettre invariants métier et tests de concurrence dans CI. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 161 — Refund Fraud

1. **Description / fonctionnement :** Contourne les règles et étapes du remboursement.
2. **Causes techniques :** Valeurs métier et transitions influencées par le client ou état concurrent ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** commandes, prix, paiements, coupons, stock, validations et remboursements ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Modéliser états et transitions ; inspecter transactions, verrous et sources de vérité. Rechercher spécialement : valeurs métier et transitions influencées par le client ou état concurrent.
5. **Prévention :** Recalculer côté serveur, transactions atomiques, idempotence et validation des transitions. **Point spécifique :** Recalcul serveur, contraintes SQL, transaction atomique, idempotency keys et machine à états.
6. **Correction sécurisée :** Déplacer vérification de prix/état côté serveur et imposer contraintes transactionnelles en base. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une opération répétée, négative ou concurrente ne modifie pas illégalement le solde/stock. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : pertes financières, incohérences comptables et abus des transactions.
9. **Prévention de réapparition :** Mettre invariants métier et tests de concurrence dans CI. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 162 — Inventory Manipulation

1. **Description / fonctionnement :** Modifie des stocks hors des règles métiers.
2. **Causes techniques :** Valeurs métier et transitions influencées par le client ou état concurrent ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** commandes, prix, paiements, coupons, stock, validations et remboursements ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Modéliser états et transitions ; inspecter transactions, verrous et sources de vérité. Rechercher spécialement : valeurs métier et transitions influencées par le client ou état concurrent.
5. **Prévention :** Recalculer côté serveur, transactions atomiques, idempotence et validation des transitions. **Point spécifique :** Recalcul serveur, contraintes SQL, transaction atomique, idempotency keys et machine à états.
6. **Correction sécurisée :** Déplacer vérification de prix/état côté serveur et imposer contraintes transactionnelles en base. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une opération répétée, négative ou concurrente ne modifie pas illégalement le solde/stock. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : pertes financières, incohérences comptables et abus des transactions.
9. **Prévention de réapparition :** Mettre invariants métier et tests de concurrence dans CI. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 163 — Transaction Replay

1. **Description / fonctionnement :** Réexécute une transaction autorisée une première fois.
2. **Causes techniques :** Valeurs métier et transitions influencées par le client ou état concurrent ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** commandes, prix, paiements, coupons, stock, validations et remboursements ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Modéliser états et transitions ; inspecter transactions, verrous et sources de vérité. Rechercher spécialement : valeurs métier et transitions influencées par le client ou état concurrent.
5. **Prévention :** Recalculer côté serveur, transactions atomiques, idempotence et validation des transitions. **Point spécifique :** Recalcul serveur, contraintes SQL, transaction atomique, idempotency keys et machine à états.
6. **Correction sécurisée :** Déplacer vérification de prix/état côté serveur et imposer contraintes transactionnelles en base. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une opération répétée, négative ou concurrente ne modifie pas illégalement le solde/stock. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : pertes financières, incohérences comptables et abus des transactions.
9. **Prévention de réapparition :** Mettre invariants métier et tests de concurrence dans CI. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 164 — Double Spending

1. **Description / fonctionnement :** Consomme deux fois le même solde ou crédit.
2. **Causes techniques :** Valeurs métier et transitions influencées par le client ou état concurrent ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** commandes, prix, paiements, coupons, stock, validations et remboursements ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Modéliser états et transitions ; inspecter transactions, verrous et sources de vérité. Rechercher spécialement : valeurs métier et transitions influencées par le client ou état concurrent.
5. **Prévention :** Recalculer côté serveur, transactions atomiques, idempotence et validation des transitions. **Point spécifique :** Recalcul serveur, contraintes SQL, transaction atomique, idempotency keys et machine à états.
6. **Correction sécurisée :** Déplacer vérification de prix/état côté serveur et imposer contraintes transactionnelles en base. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une opération répétée, négative ou concurrente ne modifie pas illégalement le solde/stock. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : pertes financières, incohérences comptables et abus des transactions.
9. **Prévention de réapparition :** Mettre invariants métier et tests de concurrence dans CI. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 165 — Workflow Bypass

1. **Description / fonctionnement :** Contourne une étape obligatoire d'une opération.
2. **Causes techniques :** Valeurs métier et transitions influencées par le client ou état concurrent ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** commandes, prix, paiements, coupons, stock, validations et remboursements ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Modéliser états et transitions ; inspecter transactions, verrous et sources de vérité. Rechercher spécialement : valeurs métier et transitions influencées par le client ou état concurrent.
5. **Prévention :** Recalculer côté serveur, transactions atomiques, idempotence et validation des transitions. **Point spécifique :** Recalcul serveur, contraintes SQL, transaction atomique, idempotency keys et machine à états.
6. **Correction sécurisée :** Déplacer vérification de prix/état côté serveur et imposer contraintes transactionnelles en base. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une opération répétée, négative ou concurrente ne modifie pas illégalement le solde/stock. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : pertes financières, incohérences comptables et abus des transactions.
9. **Prévention de réapparition :** Mettre invariants métier et tests de concurrence dans CI. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 166 — Negative Quantity Abuse

1. **Description / fonctionnement :** Exploite des valeurs négatives inattendues.
2. **Causes techniques :** Valeurs métier et transitions influencées par le client ou état concurrent ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** commandes, prix, paiements, coupons, stock, validations et remboursements ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Modéliser états et transitions ; inspecter transactions, verrous et sources de vérité. Rechercher spécialement : valeurs métier et transitions influencées par le client ou état concurrent.
5. **Prévention :** Recalculer côté serveur, transactions atomiques, idempotence et validation des transitions. **Point spécifique :** Recalcul serveur, contraintes SQL, transaction atomique, idempotency keys et machine à états.
6. **Correction sécurisée :** Déplacer vérification de prix/état côté serveur et imposer contraintes transactionnelles en base. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une opération répétée, négative ou concurrente ne modifie pas illégalement le solde/stock. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : pertes financières, incohérences comptables et abus des transactions.
9. **Prévention de réapparition :** Mettre invariants métier et tests de concurrence dans CI. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 167 — Parameter Price Tampering

1. **Description / fonctionnement :** Falsifie la valeur de prix fournie au serveur.
2. **Causes techniques :** Valeurs métier et transitions influencées par le client ou état concurrent ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** commandes, prix, paiements, coupons, stock, validations et remboursements ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Modéliser états et transitions ; inspecter transactions, verrous et sources de vérité. Rechercher spécialement : valeurs métier et transitions influencées par le client ou état concurrent.
5. **Prévention :** Recalculer côté serveur, transactions atomiques, idempotence et validation des transitions. **Point spécifique :** Recalcul serveur, contraintes SQL, transaction atomique, idempotency keys et machine à états.
6. **Correction sécurisée :** Déplacer vérification de prix/état côté serveur et imposer contraintes transactionnelles en base. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une opération répétée, négative ou concurrente ne modifie pas illégalement le solde/stock. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : pertes financières, incohérences comptables et abus des transactions.
9. **Prévention de réapparition :** Mettre invariants métier et tests de concurrence dans CI. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 168 — Order Status Manipulation

1. **Description / fonctionnement :** Modifie un état de commande hors du workflow.
2. **Causes techniques :** Valeurs métier et transitions influencées par le client ou état concurrent ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** commandes, prix, paiements, coupons, stock, validations et remboursements ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Modéliser états et transitions ; inspecter transactions, verrous et sources de vérité. Rechercher spécialement : valeurs métier et transitions influencées par le client ou état concurrent.
5. **Prévention :** Recalculer côté serveur, transactions atomiques, idempotence et validation des transitions. **Point spécifique :** Recalcul serveur, contraintes SQL, transaction atomique, idempotency keys et machine à états.
6. **Correction sécurisée :** Déplacer vérification de prix/état côté serveur et imposer contraintes transactionnelles en base. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une opération répétée, négative ou concurrente ne modifie pas illégalement le solde/stock. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : pertes financières, incohérences comptables et abus des transactions.
9. **Prévention de réapparition :** Mettre invariants métier et tests de concurrence dans CI. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 169 — Approval Workflow Bypass

1. **Description / fonctionnement :** Valide une action sans approbation requise.
2. **Causes techniques :** Valeurs métier et transitions influencées par le client ou état concurrent ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** commandes, prix, paiements, coupons, stock, validations et remboursements ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Modéliser états et transitions ; inspecter transactions, verrous et sources de vérité. Rechercher spécialement : valeurs métier et transitions influencées par le client ou état concurrent.
5. **Prévention :** Recalculer côté serveur, transactions atomiques, idempotence et validation des transitions. **Point spécifique :** Recalcul serveur, contraintes SQL, transaction atomique, idempotency keys et machine à états.
6. **Correction sécurisée :** Déplacer vérification de prix/état côté serveur et imposer contraintes transactionnelles en base. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une opération répétée, négative ou concurrente ne modifie pas illégalement le solde/stock. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : pertes financières, incohérences comptables et abus des transactions.
9. **Prévention de réapparition :** Mettre invariants métier et tests de concurrence dans CI. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 170 — Insecure Payment Callback

1. **Description / fonctionnement :** Accepte une confirmation de paiement insuffisamment authentifiée.
2. **Causes techniques :** Valeurs métier et transitions influencées par le client ou état concurrent ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** commandes, prix, paiements, coupons, stock, validations et remboursements ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Modéliser états et transitions ; inspecter transactions, verrous et sources de vérité. Rechercher spécialement : valeurs métier et transitions influencées par le client ou état concurrent.
5. **Prévention :** Recalculer côté serveur, transactions atomiques, idempotence et validation des transitions. **Point spécifique :** Recalcul serveur, contraintes SQL, transaction atomique, idempotency keys et machine à états.
6. **Correction sécurisée :** Déplacer vérification de prix/état côté serveur et imposer contraintes transactionnelles en base. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une opération répétée, négative ou concurrente ne modifie pas illégalement le solde/stock. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **critique** (à contextualiser : vraisemblance × impact) ; impacts possibles : pertes financières, incohérences comptables et abus des transactions.
9. **Prévention de réapparition :** Mettre invariants métier et tests de concurrence dans CI. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».
