# 🔎 Auditoria do ecossistema mauroda666 à luz das novas ferramentas

Auditoria fundamentada no código real de `mauroda666/AI` (monorepo, ~30 subprojetos) e nos
repositórios satélite. Cruzamento com as 70 ferramentas dos 3 threads (scrapers, segundo cérebro/MCP, 50 sites).

## Panorama dos repositórios
16 repos. O núcleo é o monorepo **AI** ("all we need") com os subprojetos: equita-webapp/bridge/portal,
openclaw (swarm 18 agentes), mcp-varejonline, quiksilver-hub, mei-facil-ia, conteudo-factory,
radar-marca-ia, reputa-zap, zap-hub, benchmark-pesquisas, capital-invest-br, fidc-agt-tagus, joompro,
loja-brasil, enxame-studio, indice, infra, growth, portfolio, pulso, a2s-ecossistema, norte-fitness,
drones-ucrania-latam. Satélites: bas-motors, BAS-Motors-IREP, sabidinho, criemei/MEI, equita-commons/Tn/equitabiz,
enxame/fabrica, ecoblocks (independente), kepano-obsidian (vault pessoal).

---

## Melhorias por projeto (ferramenta nova → ganho concreto)

### conteudo-factory  (pipeline Trends/RSS → LLM → validador anti-alucinação → fila)
- **Firecrawl / Crawl4AI** como *fonte* além de RSS: puxam a página real em markdown pronto pra o agente escrever **a partir da fonte** — reforça exatamente o seu antialucinação.
- **browser-use** para plataformas sem RSS (X/Threads/Instagram trends, portais com login).
- **MarkItDown** normaliza PDFs/Office/relatórios em markdown antes de alimentar o LLM.
- **Impacto:** mais cobertura de trends, menos alucinação, custo marginal ~zero (tudo OSS).

### reputa-zap  (reputação WhatsApp; roadmap já cita "prospecção via Maps scraping")
- **Crawlee + Scrapling** destravam o incremento de **prospecção via Google Maps** (lista de negócios sem review → lead). É o item que está no seu próprio backlog.
- **browser-use** para ler/publicar no Google Business Profile onde a API é limitada.
- **Impacto:** vira de reativo (pedir review) para ativo (achar quem precisa) — mais MRR.

### radar-marca-ia  (AEO: presença da marca em ChatGPT/Gemini/Perplexity/Claude)
- **browser-use / Firecrawl** para consultar as superfícies de IA e **capturar citações/fontes** em escala, além do OpenRouter.
- Sites analíticos do post 1 (`similarsites`, `connectedpapers`, `semanticscholar`) enriquecem as recomendações de conteúdo.
- **Impacto:** dados de share-of-voice mais ricos e defensáveis.

### benchmark-pesquisas  (surveys; ativo estratégico = o dado/painel)
- Stack de scraping + `AutoScraper` para **aquisição de dados** e monitoramento de concorrentes (Opinion Box, MindMiners, Pollfish).
- **Impacto:** alimenta o lado certo da equação (quem possui o dado), com consentimento LGPD desde o dia 1.

### indice  (índice semântico do monorepo — embeddings Ollama, ~13k trechos)
- **Este é o seu "segundo cérebro" nascente.** Exponha-o como **MCP server** (padrão `noesskeetit/second-brain-mcp` read-only) para o Claude Desktop/Code consultarem **ao vivo**.
- **MegaMem (grafo temporal, Graphiti)** combina com o seu `DECISOES.md`: rastreia *como as decisões mudaram no tempo* — "o que decidimos sobre X em julho vs agora".
- **Impacto:** o split de repos fica seguro (memória cruzada viva) e o Claude para de reescrever o que já foi resolvido.

### openclaw  (swarm de 18 agentes)
- Adicione **browser-use, Crawl4AI e Firecrawl como skills/tools** dos agentes (DevOps/Researcher/Coder) — capacidade de navegação e extração que hoje não têm.
- Ponte MCP de segundo cérebro dá **memória persistente** ao swarm.

### mcp-varejonline  (MCP server ERP, 21 tools — sem README)
- **Ação rápida:** adicionar `README.md` (padrão dos outros subprojetos) e testes de contrato.
- Use os repos MCP de segundo cérebro como referência de arquitetura read-only vs read-write.

### equita-webapp / bridge / portal  (Equità Biz — geração de documentos)
- **MarkItDown** para ingerir modelos/《inputs》 do cliente (PDF/Word/Excel) → contexto do gerador.
- **Firecrawl** para pesquisa de mercado automática dentro do Business Plan/Análise de Viabilidade.

### quiksilver-hub / zap-hub / mei-facil-ia
- **scrcpy** para automações Android onde só há app (WhatsApp/ERP mobile).
- Sites do post 1 (`ilovepdf`, `smallpdf`, `photopea`, `remove.bg`) como utilidades embutidas no MEI Fácil (recibos, logos, PDFs) sem custo de API.

### bas-motors / capital-invest-br / fidc-agt-tagus
- Stack de scraping → **inteligência de precificação de seminovos** e monitoramento de concorrentes (já alinhado ao guia `01-scraping-monetizavel.md`).

---

## Recomendações transversais (maior alavancagem)
1. **Serviço de scraping compartilhado** (`infra/scraper` ou skill do openclaw): Firecrawl+Crawl4AI+Scrapling atrás de uma fila, reusado por conteudo-factory, reputa-zap, radar-marca-ia, bas-motors. Um esforço, cinco projetos.
2. **Camada de memória MCP** sobre o `indice`: expõe o índice semântico + DECISOES.md como MCP (read-only primeiro). Base para o "vault se mantém sozinho".
3. **Vault Obsidian do ecossistema** (o `toolkit/vault` recém-criado + `kepano-obsidian`): usar o padrão Karpathy (compilar `raw/` → `wiki/`) sobre a documentação estratégica (DECISOES, INDEX, A2S).

## Quick wins (ordem de esforço → impacto)
| # | Ação | Onde | Esforço |
|---|---|---|---|
| 1 | README + testes de contrato no `mcp-varejonline` | mcp-varejonline | baixo |
| 2 | Adicionar Firecrawl como fonte no `conteudo-factory` | conteudo-factory | baixo-médio |
| 3 | Expor `indice` como MCP read-only | indice | médio |
| 4 | Prospecção via Maps scraping (Crawlee+Scrapling) | reputa-zap | médio |
| 5 | browser-use como skill do swarm | openclaw | médio |

## Riscos e compliance (atenção)
- **ToS / anti-bot:** `Scrapling` e `curl-impersonate` contornam detecção — avaliar termos de cada alvo (Maps, redes sociais) e LGPD antes de produção. Registrar decisão no `DECISOES.md`.
- **Postura de segredos:** o ecossistema já está bem (`.gitleaks.toml`, espelho sanitizado do openclaw, segredos fora do git). Manter esse padrão ao adicionar chaves de scraping/proxy.
- **Custo de IA:** Model Gateway/embeddings locais já mapeados no `indice` — o scraping reduz tokens ao entregar markdown limpo (menos contexto cru).

---
Fonte da auditoria: leitura de `mauroda666/AI` (README raiz, indice, conteudo-factory, radar-marca-ia, reputa-zap, benchmark-pesquisas, openclaw, mcp-varejonline) + catálogo das 70 ferramentas.
