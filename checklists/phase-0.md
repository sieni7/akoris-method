# CHECKLIST — PHASE 0 : INITIALISATION DES ONGLETS

> **Public :** Validator (humain)
> **Quand :** Avant le bootstrap, une seule fois par projet
> **Durée :** 5-10 minutes
> **Référence :** `.akoris/contexte.md` §18

---

## Prérequis

- [ ] `akoris-method/` accessible (repo cloné ou à côté)
- [ ] 3 onglets ouverts (A, B, C) sur le même LLM (ou 3 LLM différents)
- [ ] Un terminal ouvert

---

## Étape 0.1 — Scaffold (terminal)

- [ ] `cd <chemin-parent>`
- [ ] `./akoris-method/scripts/init-project.sh <nom-du-projet>`
  - **OU** manuellement : `mkdir <nom-du-projet> && cd <nom-du-projet>`
    puis `mkdir -p app doc .akoris`
    puis `cp -r akoris-method/templates/.akoris .`
- [ ] `cd <nom-du-projet>`
- [ ] Vérifier : `ls -la` → `app/`, `doc/`, `.akoris/`
- [ ] Adapter `.akoris/projet.md` P1 (nom du projet, stack, public)

---

## Étape 0.2 — Onglet A (Orchestrator)

- [ ] Copier le contenu de `.akoris/config/agents/orchestrator.md`
- [ ] Coller dans l'onglet A
- [ ] Envoyer
- [ ] Vérifier la réponse : `ORCHESTRATOR prêt. En attente du prompt bootstrap.`
- [ ] ❌ **Ne PAS taper `go`**

---

## Étape 0.3 — Onglet B (Builder)

- [ ] Copier le contenu de `.akoris/config/agents/builder.md`
- [ ] Coller dans l'onglet B
- [ ] Envoyer
- [ ] Vérifier la réponse : `BUILDER prêt. En attente.`
- [ ] ❌ **Ne PAS taper `go`**

---

## Étape 0.4 — Onglet C (Auditor)

- [ ] Copier le contenu de `.akoris/config/agents/auditor.md`
- [ ] Coller dans l'onglet C
- [ ] Envoyer
- [ ] Vérifier la réponse : `AUDITOR prêt. En attente.`
- [ ] ❌ **Ne PAS taper `go`**

---

## Étape 0.5 — Lancer le bootstrap (onglet A)

- [ ] Copier le contenu de `.akoris/config/bootstrap.md`
- [ ] Coller dans l'onglet A (à la suite du prompt d'identité)
- [ ] Envoyer
- [ ] L'Orchestrator répond avec la Phase 1
- [ ] Lire sa réponse
- [ ] Taper `go` dans A → Phase 2

---

## Validation finale

- [ ] Les 3 onglets ont répondu "prêt"
- [ ] Aucun `go` tapé en phase 0
- [ ] Le bootstrap est lancé (Phase 1)
- [ ] `.akoris/projet.md` P1 adapté au projet

**✅ Phase 0 terminée. Passer à `checklists/bootstrap.md`.**
