-- Toolkit catalog — schema da base de dados de ferramentas
-- Compatível com SQLite e Cloudflare D1
-- Cada ferramenta extraída dos links do thread do X entra aqui.

CREATE TABLE IF NOT EXISTS tools (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    name            TEXT NOT NULL,
    category        TEXT,            -- ex: AI, scraping, dados, dev, automacao, design
    url             TEXT,            -- link oficial / front-end da ferramenta
    repo_url        TEXT,            -- repositório (se houver)
    description     TEXT,
    value_productive   INTEGER DEFAULT 0,
    value_monetizable  INTEGER DEFAULT 0,
    value_development  INTEGER DEFAULT 0,
    value_analytical   INTEGER DEFAULT 0,
    access_method   TEXT,            -- web, cli, api, mcp, desktop, self-host
    pricing         TEXT,            -- free, freemium, paid, open-source
    tags            TEXT,
    notes           TEXT,
    source_post     TEXT,
    created_at      TEXT DEFAULT (datetime('now'))
);
CREATE INDEX IF NOT EXISTS idx_tools_category ON tools(category);
CREATE INDEX IF NOT EXISTS idx_tools_pricing  ON tools(pricing);
CREATE VIEW IF NOT EXISTS monetizable AS
    SELECT name, category, url, pricing FROM tools WHERE value_monetizable = 1;
