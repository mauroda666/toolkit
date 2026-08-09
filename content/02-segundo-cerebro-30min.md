# 🧠 Segundo Cérebro em 30 minutos — Claude + Obsidian

Baseado no thread @0xkkai. Regra de ouro: **você precisa de 2 repos, não de 10** — um *compilador* (padrão Karpathy Wiki) + uma *ponte* (MCP).

## Passo 1 — Vault Obsidian (5 min)
Abra a pasta `vault/` deste projeto no Obsidian (já instalado no seu desktop). Estrutura pronta:
`00-Inbox` → captura · `10-Tools` · `20-Skills` · `30-Projects` (Equita, MEI Fácil, Quiksilver, BAS) · `40-Resources` · `50-Daily` · `99-Templates`.

## Passo 2 — O compilador (padrão Karpathy) (10 min)
Escolha **um**:
- `ekadetov/llm-wiki` — mínimo viável, 6 comandos, setup < 5 min.
- `AgriciDaniel/claude-obsidian` — referência mais limpa (recomendado pra começar).

Ele lê cada fonte **uma vez**, compila em 8–15 páginas wiki linkadas e nunca mais relê o cru — corta 70–90% de tokens em consultas repetidas.

## Passo 3 — A ponte MCP (10 min)
Escolha **um**, conforme seu apetite de risco:
- `noesskeetit/second-brain-mcp` — read-only + busca semântica (seguro, multi-ferramenta: Claude Code, Cursor, Zed).
- `CoMfUcIoS/second-brain-mcp` — estritamente read-only (vault "sagrado").
- `eugeniughelbur/obsidian-second-brain` — read-write + 45 comandos + agentes agendados (o vault se mantém sozinho).

## Passo 4 — Integração desktop / storage (5 min)
- **LLMs no desktop:** Claude Desktop lê o vault via MCP; ChatGPT/Perplexity/Kimi ficam para consultas pontuais.
- **Docs e planilhas:** exporte para `40-Resources`; o compilador ingere.
- **Onde guardar (3 cópias):**
  - Desktop (vault vivo do Obsidian)
  - OneDrive **ou** Google Drive (sync automático da pasta do vault)
  - GitHub `mauroda666/toolkit` (versionado, sob seu controle) → `git push`

## Config MCP (Claude Desktop)
Veja `content/mcp-config-exemplos.md` para o snippet de `claude_desktop_config.json`.
