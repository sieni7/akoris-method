# Décision 042 — CLI — Adapters

- **Statut :** V2 / non implémentée
- **Date :** 2026-10-28
- **Contexte :** Bloc 8d (process)

---

## Décision

Le CLI communique avec les outils externes (opencode, Manus, Cursor) via des **adapters** interchangeables. Un fallback clipboard est toujours disponible.

## Règles

### Interface

```typescript
interface Adapter {
  send(command: string): Promise<void>;
}
```

### Adapters V2.0

| Adapter | Méthode | Priorité |
|---------|---------|----------|
| `OpencodeAdapter` | Clipboard + notification | 1 |
| `ManusAdapter` | Clipboard + notification | 1 |
| `CursorAdapter` | API (si dispo) | 2 |
| `ClipboardAdapter` | Copie dans le presse-papiers | Fallback |

### Fallback

- Si l'adapter principal échoue, le CLI bascule sur `ClipboardAdapter`.
- L'humain colle manuellement dans l'onglet.
- Le CLI notifie : « `go` copié dans le presse-papiers. Colle-le dans l'onglet A. »

### V2.1

- Si opencode/Manus exposent une API, les adapters deviennent **API-first**.
- L'humain n'a plus à coller manuellement.

## Justification

- **Interchangeabilité** : on peut changer d'outil sans changer le CLI.
- **Fallback** : le clipboard fonctionne toujours.
- **Progression** : V2.0 (clipboard) → V2.1 (API).

## Alternatives écartées

- **Adapter unique** : dépendance à un outil.
- **Pas de fallback** : le CLI casse si l'API est down.
- **API uniquement** : impossible tant qu'opencode n'expose pas d'API.
