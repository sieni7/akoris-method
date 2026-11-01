# Décision 051 — Catalogue des spécialisations et déclinaisons Standard / Lite

- **Statut :** décision humaine validée pour formalisation ; contrats détaillés en cours de conception
- **Date :** 2026-11-01
- **Contexte :** Cycles 1, 2 et 3.1 de structuration des spécialisations AKORIS
- **Portée :** orientation de conception et gouvernance du catalogue ; ne vaut pas implémentation technique

---

## 1. Décisions validées

### 1.1 Catalogue des spécialisations

Le catalogue conserve **29 spécialisations opérationnelles** issues de l'analyse des 33 profils initiaux.

- CORE-06 et GOV-03 sont fusionnés en une seule spécialisation : **Documentation & Capitalisation des connaissances**.
- CORE-01, GOV-01 et GOV-02 sont écartés comme modules autonomes, leurs responsabilités ne devant pas créer de rôles ou d'autorités parallèles aux fondations AKORIS.
- CORE-08 est conservé comme expertise d'analyse et de préparation qualité, sans autorité sur les Quality Gates, les décisions GO / NO GO / BLOCKED ou les transitions.
- Les 29 spécialisations restent dans le catalogue ; leur activation est conditionnelle au besoin réel du projet.

### 1.2 Compatibilité A / B / C

La matrice de compatibilité ci-dessous a été validée au Cycle 2.

Légende :
- **P** : rôle principal pour mobiliser la spécialisation.
- **S** : rôle de support.
- **V** : vérification indépendante.
- **—** : aucune attribution opérationnelle.

| Spécialisation | A | B | C |
|---|:---:|:---:|:---:|
| CORE-02 — Solution Architect | P | S | V |
| CORE-03 — Product Owner | P | S | V |
| CORE-04 — Database Architect | S | P | V |
| CORE-05 — Security Officer | P | S | V |
| CORE-06/GOV-03 — Documentation & Knowledge Capitalization | S | P | V |
| CORE-07 — DevOps Engineer | S | P | V |
| CORE-08 — Quality Analysis & Preparation | P | S | V |
| DEV-01 — Frontend Architect | S | P | V |
| DEV-02 — Backend Architect | S | P | V |
| DEV-03 — API Designer | S | P | V |
| DEV-04 — Domain Modeler | P | S | V |
| DEV-05 — UX Engineer | S | P | V |
| DEV-06 — PWA Engineer | S | P | V |
| DEV-07 — Performance Engineer | S | P | V |
| DEV-08 — Integration Engineer | S | P | V |
| EXP-01 — AI Interaction Optimization | P | S | V |
| EXP-02 — SaaS Specialist | S | P | V |
| EXP-03 — Mobile Specialist | S | P | V |
| EXP-04 — Data Engineer | S | P | V |
| EXP-05 — Compliance Analysis | P | S | V |
| EXP-06 — Operations Specialist | S | P | V |
| EXP-07 — Replication & Reproducibility Specialist | P | S | V |
| QA-01 — Code Reviewer | S | — | P |
| QA-02 — Test Automation Engineer | S | P | V |
| QA-03 — Security Auditor | S | — | P |
| QA-04 — Performance Auditor | S | — | P |
| QA-05 — Accessibility Auditor | S | — | P |
| QA-06 — Documentation Auditor | S | — | P |
| QA-07 — Technical Debt Analyst | P | S | V |

Cette matrice ne modifie pas les responsabilités constitutionnelles des rôles. L'ordre **A → B → C** demeure obligatoire. C intervient après le travail de B pour vérifier indépendamment ; son constat ou sa recommandation ne constitue pas, à lui seul, une autorisation de fusion, de déploiement ou une décision humaine.

Règles particulières validées :
- QA-01, QA-03, QA-04, QA-05 et QA-06 sont mobilisées par C pour un audit indépendant ; B ne peut pas auditer son propre travail.
- QA-02 est principalement mobilisée par B pour construire les tests, puis vérifiée par C.
- QA-07 aide A à analyser et prioriser la dette ; B réalise les corrections et C en vérifie les résultats.
- Les spécialisations conditionnelles ne sont activées que si le contexte du projet le justifie.

### 1.3 Contrat opérationnel commun

Le contrat commun des spécialisations, version de travail **0.1**, a été validé au Cycle 3.1.

Il fixe notamment :
- l'identité et le statut d'une spécialisation ;
- le respect des rôles et de l'ordre A → B → C ;
- les conditions d'activation et la définition de mission ;
- les entrées, sources, activités et livrables ;
- les preuves et vérifications ;
- les limites, interdictions et procédures de blocage ;
- la sécurité, la traçabilité, la clôture et le versionnement.

Chaque spécialisation disposera d'une fiche métier dérivée de ce contrat commun. Les contrats détaillés des 29 spécialisations restent à élaborer et à examiner ; leur validation n'est pas présumée par la présente décision.

## 2. Décision de conception : deux déclinaisons

Le principe d'une approche progressive comprenant deux déclinaisons est validé :

### AKORIS Standard

Déclinaison complète de référence, portant l'ensemble du cadre, du catalogue, des contrats, des exigences de traçabilité et des modalités de vérification adaptées aux projets structurés.

### AKORIS Lite

Déclinaison simplifiée destinée notamment aux jeunes développeurs, aux débutants et aux projets de petite taille.

Lite doit être conçue comme une simplification d'usage et d'apprentissage à partir du socle Standard, et non comme une méthode concurrente ou une gouvernance dégradée.

Le principe validé autorise notamment à étudier :
- des fiches et instructions plus courtes ;
- un nombre réduit de spécialisations activées ;
- des livrables et checklists plus légers ;
- une progression pédagogique graduelle.

Lite ne peut pas supprimer ou contourner les garanties fondamentales :
- les rôles permanents A, B et C ;
- l'ordre A → B → C ;
- la séparation entre construction et audit indépendant ;
- la traçabilité minimale des décisions et des preuves ;
- la distinction entre recommandation, vérification et décision humaine.

**Important :** le principe des deux déclinaisons est validé ; leurs spécifications détaillées, leur périmètre exact, leurs critères de conformité et leur implémentation restent à définir.

## 3. Suite des travaux

La progression retenue est la suivante :

1. Finaliser et stabiliser le contrat opérationnel commun.
2. Définir et examiner les 29 fiches de spécialisation, famille par famille.
3. Vérifier la cohérence de l'ensemble des fiches avec la matrice A/B/C et les règles d'indépendance.
4. Construire la spécification AKORIS Lite à partir du socle Standard.
5. Préparer seulement ensuite l'intégration normative et technique dans le dépôt.

## 4. Limites de cette décision

Cette décision consigne les arbitrages humains exprimés au cours des cycles de conception. Elle ne signifie pas que les spécialisations, les contrats détaillés, AKORIS Lite ou les mécanismes d'activation sont déjà implémentés dans le dépôt ou dans les templates.

Toute évolution de la constitution, des rôles ou des règles normatives doit suivre la gouvernance de décision AKORIS et rester cohérente avec les documents fondateurs.
