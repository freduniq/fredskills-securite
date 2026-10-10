# 16 — Sources, versions et correspondances

Cette section est une référence documentaire, pas une catégorie d'attaque.

- **OWASP Top 10:2025** — https://top10.owasp.org/2025/ ; catégories A01 Broken Access Control, A02 Security Misconfiguration, A03 Software Supply Chain Failures, A04 Cryptographic Failures, A05 Injection, A06 Insecure Design, A07 Authentication Failures, A08 Software or Data Integrity Failures, A09 Security Logging and Alerting Failures, A10 Mishandling of Exceptional Conditions.
- **OWASP ASVS v5.0.0 (2025)** — https://github.com/OWASP/ASVS ; utiliser les exigences de vérification pour définir des critères de recette. Les identifiants précis doivent être vérifiés dans la version consultée, ne pas les inventer.
- **OWASP API Security Top 10:2023** — https://api-security.owasp.org/editions/2023/en/0x11-t10/ ; API1 BOLA, API2 Broken Authentication, API3 Broken Object Property Level Authorization, API4 Unrestricted Resource Consumption, API5 Broken Function Level Authorization, API6 Sensitive Business Flows, API7 SSRF, API8 Misconfiguration, API9 Inventory Management, API10 Unsafe Consumption of APIs.
- **MITRE CWE** — https://cwe.mitre.org/ ; typologie de faiblesses techniques et détails des défauts.
- **OWASP WSTG** — https://owasp.org/www-project-web-security-testing-guide/ ; tests manuels et dynamiques.
- **OWASP Cheat Sheet Series** — https://cheatsheetseries.owasp.org/ ; recommandations d'implémentation.

## Aide de mapping (non exhaustive)

| Menace | OWASP Top 10 2025 | CWE utile | API 2023 |
|---|---|---|---|
| SQL injection | A05 | CWE-89 | API8 (selon scénario) |
| XSS | A05 | CWE-79 | API8 (selon scénario) |
| IDOR/BOLA | A01 | CWE-639 / CWE-862 | API1 |
| Authentification | A07 | CWE-287 | API2 |
| CSRF | A01 / A06 (contexte) | CWE-352 | selon scénario |
| Path traversal | A01 / A05 (contexte) | CWE-22 | selon scénario |
| SSRF | A05 / A06 (contexte) | CWE-918 | API7 |
| Upload non restreint | A06 / A02 (contexte) | CWE-434 | selon scénario |
| Secrets codés en dur | A04 / A02 (contexte) | CWE-798 | API8 |
| Épuisement ressources | A06 | CWE-400 | API4 |
| Dépendances vulnérables | A03 | CWE-1104 | API10 (selon scénario) |
| Logging/alerting absents | A09 | CWE-778 | selon scénario |

Les mappings sont des **aides d'analyse**, pas des équivalences officielles un-à-un. Contrôler les versions des normes et les avis de vulnérabilité avant d'émettre une conclusion à date.
