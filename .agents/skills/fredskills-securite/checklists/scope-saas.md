# Checklist multi-tenant et SaaS

- [ ] Contexte tenant issu de l'authentification vérifiée, pas d'un simple champ POST.
- [ ] Propriétaire et tenant contraignent toutes lectures/écritures/deletions côté serveur.
- [ ] Permissions identiques pour l'API, l'interface, les exports, les fichiers et les jobs.
- [ ] Cache, recherche plein texte, queues, analytics et métriques isolés entre tenants.
- [ ] Invitations à durée courte, usage unique et rôles limités.
- [ ] Changement d'organisation contrôlé et journalisé.
- [ ] Facturation, abonnement, quota et flags décidés côté serveur.
- [ ] Webhooks signés, horodatés et idempotents.
- [ ] Support « impersonation » à consentement/autorisation robuste, traçabilité et expiration.
- [ ] Essais négatifs tenant A/B et admin tenant A vs B effectués.
