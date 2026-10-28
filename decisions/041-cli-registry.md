# Décision 041 — CLI — Registry des onglets virtuels

- **Statut :** figée
- **Date :** 2026-10-28
- **Contexte :** Bloc 8d (process)

---

## Décision

Le CLI AKORIS implémente les onglets A, B, C comme des **entités virtuelles** dans un registry (core), préservant la philosophie d'opencode (UI en onglets + dossier partagé).

## Règles

### Structure du registry

```typescript
interface Tab {
  id: 'A' | 'B' | 'C';
  agent: 'orchestrator' | 'builder' | 'auditor';
  adapter: Adapter;
}

class Registry {
  private tabs: Map<string, Tab>;
  getTab(id: string): Tab;
  async sendGo(tabId: string): Promise<void>;
}
```

### Philosophie préservée

| opencode (V1) | Registry (V2) |
|---------------|---------------|
| UI en onglets | `Tab { id, agent, adapter }` |
| Dossier local partagé | Core lit/écrit `.akoris/` |
| Chat par onglet | `akoris go A` → adapter A |

### V1 vs V2

- V1 : opencode impose ses onglets (UI réelle).
- V2 : le registry reproduit la philosophie, indépendamment de l'outil.

## Justification

- **Indépendance** : le CLI ne dépend plus d'opencode.
- **Philosophie préservée** : onglets + dossier partagé restent les piliers.
- **Extensibilité** : ajouter un 4e onglet (D) devient trivial.

## Alternatives écartées

- **Pas de registry** : le CLI dépend d'opencode.
- **Registry dans opencode** : dépendance à l'outil.
- **UI en onglets recréée from scratch** : coût énorme, risque de régression.
