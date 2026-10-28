---
id: DT-NNN
titre: <titre court de la dette>
priorite: P0 | P1 | P2 | P3
statut: ouverte | en_cours | resorbee | acceptee_definitivement
sprint_origine: <NN>
decision_origine: go_with_reserve
adr_lie: ADR-NNNN
risque: "<description du risque>"
impact: faible | moyen | eleve | critique
sprint_resorption_prevu: <NN>
cree_le: <YYYY-MM-DD>
---

# DT-NNN — <titre court>

## Contexte

<pourquoi cette dette a été acceptée, dans quel contexte, quelles contraintes>

## Risque

<ce qui peut mal tourner si la dette n'est pas résorbée>

## Plan de résorption

<étapes prévues pour résorber la dette, critères de sortie>

## Preuves de résorption

<commits, tests, PR qui prouvent la résorption>

## Historique

- <YYYY-MM-DD> : ouverte (sprint NN, verdict go_with_reserve)
- <YYYY-MM-DD> : en_cours (sprint NN)
- <YYYY-MM-DD> : resorbee (commit <hash>)
