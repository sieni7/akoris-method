# STATE — <nom-du-projet>
# Machine à états AKORIS. Un seul agent à la fois.
# Écrit par les agents, lu par tous. Commité en clôture de sprint.

sprint: 0
phase: setup
next_agent: null
action: idle
locked_by: null

# Verdicts (remplis en phase review)
verdict: null
verdict_qa: null
verdict_secops: null
verdict_global: null
reserves: []

# Propositions de l'Orchestrator
proposals: []

# Message pour le Validator (lu dans l'UI)
message: ""

# Version cible du sprint (SemVer)
tag_cible: null

# Budget (tokens)
budget_remaining: 0

# Compteurs
tour: 0
sprint_tour_count: 0
total_tour_count: 0
taches_total: 0
taches_done: 0

# Tests (remplis par l'Auditor)
tests_tnr: na
tests_e2e: na
tests_uat: na
tests_secu: na
couverture: 0.0

# Stats par agent
agent_stats:
  orchestrator:
    tours: 0
    sprints_planifies: 0
  builder:
    tours: 0
    commits: 0
    dettes_resorbees: 0
  auditor:
    tours: 0
    audits_qa: 0
    audits_secops: 0
    recommandations_push: 0

# Métadonnées
updated_by: null
updated_at: null
