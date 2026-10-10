# 13 — IA et agents

**Couverture :** 10 types d’attaque numérotés 201 à 210. Cet inventaire identifie des familles, variantes et scénarios ; certains termes se recoupent.

**Utilisation :** lire les profils liés à la surface attaquée. Les risques sont indicatifs et se recalculent selon exposition, impact, contrôle existant et vraisemblance. Ne pas effectuer de tests actifs sur des systèmes non autorisés.

## 201 — Prompt Injection

1. **Description / fonctionnement :** Place des instructions non fiables dans les contenus traités par un modèle.
2. **Causes techniques :** Données externes traitées comme directives ou actions ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** LLM, RAG, prompts, outils, vector DB, fonctions d’agents et APIs tierces ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier frontières de confiance, entrées rag et droits d’action ; évaluer avec documents de test. Rechercher spécialement : données externes traitées comme directives ou actions.
5. **Prévention :** Séparer instructions et données, permissionner les outils, validation des sorties, filtre tenant. **Point spécifique :** Outils à droits minimaux ; séparer contenu externe et instructions ; validation et approbation des actions sensibles.
6. **Correction sécurisée :** Réduire l’accès et les actions des agents ; valider chaque commande/URL/paramètre avant exécution. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une instruction hostile de test intégrée à un document n’entraîne aucune action privilégiée. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : divulgation de données ou actions non autorisées par un agent.
9. **Prévention de réapparition :** Revues de prompts/outils, journalisation des appels et jeux d’évaluation non offensifs. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 202 — Indirect Prompt Injection

1. **Description / fonctionnement :** Camoufle une instruction dans une page ou un document récupéré.
2. **Causes techniques :** Données externes traitées comme directives ou actions ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** LLM, RAG, prompts, outils, vector DB, fonctions d’agents et APIs tierces ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier frontières de confiance, entrées rag et droits d’action ; évaluer avec documents de test. Rechercher spécialement : données externes traitées comme directives ou actions.
5. **Prévention :** Séparer instructions et données, permissionner les outils, validation des sorties, filtre tenant. **Point spécifique :** Outils à droits minimaux ; séparer contenu externe et instructions ; validation et approbation des actions sensibles.
6. **Correction sécurisée :** Réduire l’accès et les actions des agents ; valider chaque commande/URL/paramètre avant exécution. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une instruction hostile de test intégrée à un document n’entraîne aucune action privilégiée. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : divulgation de données ou actions non autorisées par un agent.
9. **Prévention de réapparition :** Revues de prompts/outils, journalisation des appels et jeux d’évaluation non offensifs. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 203 — Tool Output Manipulation

1. **Description / fonctionnement :** Falsifie la réponse d'un outil ou service pour orienter l'agent.
2. **Causes techniques :** Données externes traitées comme directives ou actions ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** LLM, RAG, prompts, outils, vector DB, fonctions d’agents et APIs tierces ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier frontières de confiance, entrées rag et droits d’action ; évaluer avec documents de test. Rechercher spécialement : données externes traitées comme directives ou actions.
5. **Prévention :** Séparer instructions et données, permissionner les outils, validation des sorties, filtre tenant. **Point spécifique :** Outils à droits minimaux ; séparer contenu externe et instructions ; validation et approbation des actions sensibles.
6. **Correction sécurisée :** Réduire l’accès et les actions des agents ; valider chaque commande/URL/paramètre avant exécution. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une instruction hostile de test intégrée à un document n’entraîne aucune action privilégiée. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : divulgation de données ou actions non autorisées par un agent.
9. **Prévention de réapparition :** Revues de prompts/outils, journalisation des appels et jeux d’évaluation non offensifs. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 204 — AI Agent Tool Abuse

1. **Description / fonctionnement :** Détourne les capacités d'action accordées à un agent IA.
2. **Causes techniques :** Données externes traitées comme directives ou actions ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** LLM, RAG, prompts, outils, vector DB, fonctions d’agents et APIs tierces ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier frontières de confiance, entrées rag et droits d’action ; évaluer avec documents de test. Rechercher spécialement : données externes traitées comme directives ou actions.
5. **Prévention :** Séparer instructions et données, permissionner les outils, validation des sorties, filtre tenant. **Point spécifique :** Outils à droits minimaux ; séparer contenu externe et instructions ; validation et approbation des actions sensibles.
6. **Correction sécurisée :** Réduire l’accès et les actions des agents ; valider chaque commande/URL/paramètre avant exécution. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une instruction hostile de test intégrée à un document n’entraîne aucune action privilégiée. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : divulgation de données ou actions non autorisées par un agent.
9. **Prévention de réapparition :** Revues de prompts/outils, journalisation des appels et jeux d’évaluation non offensifs. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 205 — Sensitive Data Disclosure via LLM

1. **Description / fonctionnement :** Obtient la restitution non autorisée d'informations par un modèle.
2. **Causes techniques :** Données externes traitées comme directives ou actions ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** LLM, RAG, prompts, outils, vector DB, fonctions d’agents et APIs tierces ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier frontières de confiance, entrées rag et droits d’action ; évaluer avec documents de test. Rechercher spécialement : données externes traitées comme directives ou actions.
5. **Prévention :** Séparer instructions et données, permissionner les outils, validation des sorties, filtre tenant. **Point spécifique :** Outils à droits minimaux ; séparer contenu externe et instructions ; validation et approbation des actions sensibles.
6. **Correction sécurisée :** Réduire l’accès et les actions des agents ; valider chaque commande/URL/paramètre avant exécution. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une instruction hostile de test intégrée à un document n’entraîne aucune action privilégiée. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : divulgation de données ou actions non autorisées par un agent.
9. **Prévention de réapparition :** Revues de prompts/outils, journalisation des appels et jeux d’évaluation non offensifs. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 206 — RAG Data Poisoning

1. **Description / fonctionnement :** Intègre de fausses données dans un corpus utilisé pour la génération.
2. **Causes techniques :** Données externes traitées comme directives ou actions ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** LLM, RAG, prompts, outils, vector DB, fonctions d’agents et APIs tierces ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier frontières de confiance, entrées rag et droits d’action ; évaluer avec documents de test. Rechercher spécialement : données externes traitées comme directives ou actions.
5. **Prévention :** Séparer instructions et données, permissionner les outils, validation des sorties, filtre tenant. **Point spécifique :** Outils à droits minimaux ; séparer contenu externe et instructions ; validation et approbation des actions sensibles.
6. **Correction sécurisée :** Réduire l’accès et les actions des agents ; valider chaque commande/URL/paramètre avant exécution. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une instruction hostile de test intégrée à un document n’entraîne aucune action privilégiée. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : divulgation de données ou actions non autorisées par un agent.
9. **Prévention de réapparition :** Revues de prompts/outils, journalisation des appels et jeux d’évaluation non offensifs. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 207 — Vector Database Access Abuse

1. **Description / fonctionnement :** Explore des embeddings ou documents en dehors de son périmètre.
2. **Causes techniques :** Données externes traitées comme directives ou actions ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** LLM, RAG, prompts, outils, vector DB, fonctions d’agents et APIs tierces ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier frontières de confiance, entrées rag et droits d’action ; évaluer avec documents de test. Rechercher spécialement : données externes traitées comme directives ou actions.
5. **Prévention :** Séparer instructions et données, permissionner les outils, validation des sorties, filtre tenant. **Point spécifique :** Outils à droits minimaux ; séparer contenu externe et instructions ; validation et approbation des actions sensibles.
6. **Correction sécurisée :** Réduire l’accès et les actions des agents ; valider chaque commande/URL/paramètre avant exécution. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une instruction hostile de test intégrée à un document n’entraîne aucune action privilégiée. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : divulgation de données ou actions non autorisées par un agent.
9. **Prévention de réapparition :** Revues de prompts/outils, journalisation des appels et jeux d’évaluation non offensifs. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 208 — LLM Resource Exhaustion

1. **Description / fonctionnement :** Épuise coûts et quotas liés aux modèles.
2. **Causes techniques :** Données externes traitées comme directives ou actions ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** LLM, RAG, prompts, outils, vector DB, fonctions d’agents et APIs tierces ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier frontières de confiance, entrées rag et droits d’action ; évaluer avec documents de test. Rechercher spécialement : données externes traitées comme directives ou actions.
5. **Prévention :** Séparer instructions et données, permissionner les outils, validation des sorties, filtre tenant. **Point spécifique :** Outils à droits minimaux ; séparer contenu externe et instructions ; validation et approbation des actions sensibles.
6. **Correction sécurisée :** Réduire l’accès et les actions des agents ; valider chaque commande/URL/paramètre avant exécution. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une instruction hostile de test intégrée à un document n’entraîne aucune action privilégiée. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : divulgation de données ou actions non autorisées par un agent.
9. **Prévention de réapparition :** Revues de prompts/outils, journalisation des appels et jeux d’évaluation non offensifs. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 209 — Insecure LLM Output Handling

1. **Description / fonctionnement :** Traite une sortie IA comme une commande ou donnée de confiance.
2. **Causes techniques :** Données externes traitées comme directives ou actions ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** LLM, RAG, prompts, outils, vector DB, fonctions d’agents et APIs tierces ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier frontières de confiance, entrées rag et droits d’action ; évaluer avec documents de test. Rechercher spécialement : données externes traitées comme directives ou actions.
5. **Prévention :** Séparer instructions et données, permissionner les outils, validation des sorties, filtre tenant. **Point spécifique :** Outils à droits minimaux ; séparer contenu externe et instructions ; validation et approbation des actions sensibles.
6. **Correction sécurisée :** Réduire l’accès et les actions des agents ; valider chaque commande/URL/paramètre avant exécution. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une instruction hostile de test intégrée à un document n’entraîne aucune action privilégiée. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : divulgation de données ou actions non autorisées par un agent.
9. **Prévention de réapparition :** Revues de prompts/outils, journalisation des appels et jeux d’évaluation non offensifs. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».

## 210 — Excessive Agency

1. **Description / fonctionnement :** Confère à l'agent plus de permissions ou autonomie que nécessaire.
2. **Causes techniques :** Données externes traitées comme directives ou actions ; risque accru si l’entrée traverse la frontière de confiance sans validation côté serveur.
3. **Composants concernés :** LLM, RAG, prompts, outils, vector DB, fonctions d’agents et APIs tierces ; identifier précisément les routes, fichiers et dépendances utilisés dans ce projet.
4. **Détection / analyse :** Cartographier frontières de confiance, entrées rag et droits d’action ; évaluer avec documents de test. Rechercher spécialement : données externes traitées comme directives ou actions.
5. **Prévention :** Séparer instructions et données, permissionner les outils, validation des sorties, filtre tenant. **Point spécifique :** Outils à droits minimaux ; séparer contenu externe et instructions ; validation et approbation des actions sensibles.
6. **Correction sécurisée :** Réduire l’accès et les actions des agents ; valider chaque commande/URL/paramètre avant exécution. Vérifier que la modification conserve les règles métier et les interfaces existantes.
7. **Validation :** Une instruction hostile de test intégrée à un document n’entraîne aucune action privilégiée. Compléter par les tests de non-régression du module et un test négatif d’autorisation.
8. **Risque / conséquences :** base **élevé** (à contextualiser : vraisemblance × impact) ; impacts possibles : divulgation de données ou actions non autorisées par un agent.
9. **Prévention de réapparition :** Revues de prompts/outils, journalisation des appels et jeux d’évaluation non offensifs. Documenter les tests dans la CI.
10. **Preuve attendue :** route/fichier:ligne + contrôle observé + test exécuté/résultat + limites ; sinon déclarer « à vérifier », pas « protégé ».
