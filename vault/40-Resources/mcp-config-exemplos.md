# 🔌 Snippets de configuração MCP (Claude Desktop)

Arquivo: `%APPDATA%\Claude\claude_desktop_config.json` (Windows).

## Ponte read-only + busca semântica (noesskeetit/second-brain-mcp)
```json
{
  "mcpServers": {
    "second-brain": {
      "command": "npx",
      "args": ["-y", "second-brain-mcp", "--vault", "C:\\Users\\mauro\\Obsidian\\toolkit-vault"]
    }
  }
}
```

## Ponte read-write (eugeniughelbur/obsidian-second-brain)
```json
{
  "mcpServers": {
    "obsidian-second-brain": {
      "command": "node",
      "args": ["C:\\repos\\obsidian-second-brain\\dist\\server.js"],
      "env": { "VAULT_PATH": "C:\\Users\\mauro\\Obsidian\\toolkit-vault" }
    }
  }
}
```

> Cada repo tem seu README com o comando exato — confira antes de rodar.
> Regra: comece read-only. Migre para read-write só quando confiar no fluxo.
