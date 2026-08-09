# -*- coding: utf-8 -*-
import json, sqlite3, os, datetime

BASE = os.path.dirname(os.path.abspath(__file__))
P1 = "https://x.com/mertmetindev/status/2086123249016983903"
P2 = "https://x.com/xiaoying_eth/status/2085920007360524724"
P3 = "https://x.com/0xkkai/status/2085838657068347401"

def t(name, category, url, desc, P=(1,0,0,0), pricing="free", access="web",
      repo="", tags=None, source=P1, notes=""):
    return dict(name=name, category=category, url=url, repo_url=repo, description=desc,
                value_productive=P[0], value_monetizable=P[1], value_development=P[2],
                value_analytical=P[3], access_method=access, pricing=pricing,
                tags=tags or [], source_post=source, notes=notes)

tools = []
# ---- POST 1: 50 sites (mertmetindev) ----
p1 = [
 ("12ft.io","Leitura/Produtividade","https://12ft.io","Contorna paywalls de qualquer site",(1,0,0,0)),
 ("libgen.is","Conhecimento","https://libgen.is","Milhões de livros e didáticos grátis",(1,0,0,0)),
 ("sci-hub.se","Pesquisa","https://sci-hub.se","Artigos acadêmicos grátis",(1,0,0,1)),
 ("alternativeto.net","Descoberta","https://alternativeto.net","Encontra alternativas gratuitas de apps",(1,0,0,1)),
 ("justwatch.com","Entretenimento","https://justwatch.com","Descobre onde um conteúdo está sendo transmitido",(1,0,0,0)),
 ("archive.org","Pesquisa","https://archive.org","Acessa qualquer página antiga da web",(1,0,0,1)),
 ("gutenberg.org","Conhecimento","https://gutenberg.org","70 mil livros clássicos grátis",(1,0,0,0)),
 ("pdfdrive.com","Conhecimento","https://pdfdrive.com","Download gratuito de PDFs",(1,0,0,0)),
 ("openculture.com","Educação","https://openculture.com","Cursos grátis das melhores universidades",(1,0,0,0)),
 ("wolframalpha.com","Analítico","https://wolframalpha.com","Resolve qualquer problema de matemática na hora",(1,0,1,1)),
 ("photopea.com","Design","https://photopea.com","Photoshop grátis dentro do navegador",(1,0,1,0)),
 ("squoosh.app","Design/Dev","https://squoosh.app","Comprime qualquer imagem gratuitamente",(1,0,1,0)),
 ("remove.bg","Design","https://remove.bg","Remove o fundo de imagens gratuitamente",(1,1,0,0)),
 ("cleanup.pictures","Design","https://cleanup.pictures","Apaga objetos de fotos",(1,1,0,0)),
 ("unscreen.com","Design/Vídeo","https://unscreen.com","Remove o fundo de vídeos",(1,1,0,0)),
 ("carbon.now.sh","Dev","https://carbon.now.sh","Transforma código em arte/imagem",(1,0,1,0)),
 ("ray.so","Dev","https://ray.so","Screenshots de código elegantes",(1,0,1,0)),
 ("shots.so","Design","https://shots.so","Mockups de produto grátis",(1,1,1,0)),
 ("smartmockups.com","Design","https://smartmockups.com","Cria mockups sem Photoshop",(1,1,0,0)),
 ("haveibeenpwned.com","Segurança","https://haveibeenpwned.com","Verifica se você foi hackeado",(1,0,1,1)),
 ("virustotal.com","Segurança","https://virustotal.com","Escaneia arquivos contra malware",(1,0,1,1)),
 ("privnote.com","Privacidade","https://privnote.com","Envia mensagens autodestrutivas",(1,0,0,0)),
 ("temp-mail.org","Privacidade","https://temp-mail.org","E-mail descartável instantâneo",(1,0,1,0)),
 ("file.io","Utilitário","https://file.io","Compartilhamento de arquivos autodeletados",(1,0,1,0)),
 ("archive.ph","Pesquisa","https://archive.ph","Salva qualquer página permanentemente",(1,0,0,1)),
 ("similarsites.com","Descoberta","https://similarsites.com","Encontra alternativas de qualquer site",(1,0,0,1)),
 ("radio.garden","Entretenimento","https://radio.garden","Ouve rádios de qualquer lugar do mundo",(0,0,0,0)),
 ("everynoise.com","Descoberta","https://everynoise.com","Explora todos os gêneros musicais",(0,0,0,1)),
 ("tunefind.com","Entretenimento","https://tunefind.com","Acha músicas de qualquer série/filme",(0,0,0,1)),
 ("musicforprogramming.net","Produtividade","https://musicforprogramming.net","Música para foco/programação",(1,0,0,0)),
 ("mynoise.net","Produtividade","https://mynoise.net","Ambientes sonoros personalizados de foco",(1,0,0,0)),
 ("coffitivity.com","Produtividade","https://coffitivity.com","Sons de café que aumentam a produtividade",(1,0,0,0)),
 ("elicit.org","Pesquisa/IA","https://elicit.org","Assistente de IA para artigos acadêmicos",(1,1,0,1)),
 ("consensus.app","Pesquisa/IA","https://consensus.app","Busca de consenso científico",(1,1,0,1)),
 ("connectedpapers.com","Pesquisa","https://connectedpapers.com","Visualiza mapas de artigos acadêmicos",(1,0,0,1)),
 ("semanticscholar.org","Pesquisa","https://semanticscholar.org","Busca acadêmica gratuita",(1,0,0,1)),
 ("scispace.com","Pesquisa/IA","https://scispace.com","Entende qualquer artigo acadêmico",(1,1,0,1)),
 ("summarize.tech","Produtividade/IA","https://summarize.tech","Resume qualquer vídeo do YouTube",(1,0,0,1)),
 ("phind.com","Dev/IA","https://phind.com","Buscador de IA para desenvolvedores",(1,0,1,0)),
 ("regex101.com","Dev","https://regex101.com","Testa qualquer regex na hora",(1,0,1,0)),
 ("codebeautify.org","Dev","https://codebeautify.org","Formata código de forma limpa",(1,0,1,0)),
 ("jsonformatter.org","Dev","https://jsonformatter.org","Lê JSON de forma humana",(1,0,1,0)),
 ("explainshell.com","Dev","https://explainshell.com","Explica comandos de terminal",(1,0,1,0)),
 ("raindrop.io","Produtividade","https://raindrop.io","Gerenciador de bookmarks eficiente",(1,0,0,0)),
 ("downdetector.com","Analítico","https://downdetector.com","Verifica se um site está fora do ar",(1,0,1,1)),
 ("tineye.com","Analítico","https://tineye.com","Busca reversa de imagens",(1,0,0,1)),
 ("fast.com","Utilitário","https://fast.com","Testa a velocidade da internet",(1,0,0,1)),
 ("smallpdf.com","Produtividade","https://smallpdf.com","Edição de PDF grátis",(1,1,0,0)),
 ("ilovepdf.com","Produtividade","https://ilovepdf.com","Junta e divide PDFs",(1,1,0,0)),
 ("10minutemail.com","Privacidade","https://10minutemail.com","E-mail temporário de segundos",(1,0,1,0)),
]
for name,cat,url,desc,P in p1:
    pricing = "freemium" if P[1]==1 else "free"
    tools.append(t(name,cat,url,desc,P,pricing=pricing,tags=[cat.split('/')[0].lower()],source=P1))

# ---- POST 2: 10 repos de scraping (xiaoying_eth) ----
p2 = [
 ("Firecrawl","firecrawl/firecrawl","Aponta para qualquer site, renderiza JS e devolve dados estruturados prontos pra IA. ~130k estrelas.",(1,1,1,1)),
 ("Crawl4AI","unclecode/crawl4ai","Transforma qualquer página em markdown, sem API key nem custo por página. Open-source (Apache 2.0).",(1,1,1,1)),
 ("Browser-Use","browser-use/browser-use","Agente de IA que opera o navegador como humano: clica, rola, loga, preenche e extrai. MIT.",(1,1,1,1)),
 ("Crawlee","apify/crawlee","Framework profissional: rotação de proxy, retry, fingerprint e fila. Kit completo grátis.",(1,1,1,0)),
 ("Scrapy","scrapy/scrapy","Scraper industrial, testado há mais de 10 anos. Escala pra milhões de páginas.",(1,1,1,1)),
 ("MarkItDown","microsoft/markitdown","Converte arquivos, web, PDF, Office e imagens em markdown pra IA ler. Da Microsoft.",(1,0,1,1)),
 ("Scrapling","D4Vinci/Scrapling","Scraper furtivo que se adapta a mudanças do site e evita detecção anti-bot.",(1,1,1,1)),
 ("scrcpy","Genymobile/scrcpy","Controla e extrai dados de Android remotamente pelo PC. ~130k estrelas. Apache 2.0.",(1,0,1,0)),
 ("AutoScraper","alirezamika/autoscraper","Scraper inteligente e leve que aprende os padrões da página automaticamente.",(1,1,1,1)),
 ("curl-impersonate","lwthiker/curl-impersonate","curl que imita navegadores reais para driblar bloqueios de TLS/fingerprint.",(1,0,1,0)),
]
for name,repo,desc,P in p2:
    tools.append(t(name,"Scraping/Dev","https://github.com/"+repo,desc,P,pricing="open-source",
                   access="self-host",repo="https://github.com/"+repo,
                   tags=["scraping","github","open-source"],source=P2))

# ---- POST 3: 10 repos Segundo Cérebro Claude+Obsidian (0xkkai) ----
p3 = [
 ("claude-obsidian","AgriciDaniel/claude-obsidian","Padrão Karpathy Wiki (implementação mais pura). Ingere um arquivo uma vez e compila 8-15 páginas wiki linkadas. Melhor pra começar.",(1,0,1,1)),
 ("obsidian-second-brain","eugeniughelbur/obsidian-second-brain","MCP read-write + Skills. 45 comandos, busca híbrida (BM25+embeddings), notas auto-reescritas e agentes agendados que mantêm o vault sozinho.",(1,1,1,1)),
 ("obsidian-skills (kepano)","kepano/obsidian-skills","Skills prontas do criador do Obsidian. Clona na pasta de skills e registra sozinho. Aposta mais segura.",(1,0,1,0)),
 ("obsidian-skills (qhuang20)","qhuang20/obsidian-skills","Plugin Claude Code com skill llm-wiki (padrão Karpathy) + utilidades. Rápido pra quem vive no Claude Code.",(1,0,1,1)),
 ("llm-wiki","ekadetov/llm-wiki","Padrão Karpathy puro, 6 comandos. Setup em menos de 5 min. Mínimo viável.",(1,0,1,1)),
 ("obsidian-claude-code-mcp","iansinnott/obsidian-claude-code-mcp","MCP read-write via API do Obsidian (respeita plugins Dataview/Templater/Excalidraw).",(1,0,1,1)),
 ("second-brain-mcp (noesskeetit)","noesskeetit/second-brain-mcp","MCP read-only offline com busca semântica. Funciona em Claude Code, Cursor, Zed.",(1,0,1,1)),
 ("second-brain-mcp (CoMfUcIoS)","CoMfUcIoS/second-brain-mcp","MCP estritamente read-only. Ideal pra quem não quer risco de escrita automática.",(1,0,1,1)),
 ("obsidian-plugin-skills","sunnyhasija/obsidian-plugin-skills","Expande as skills do Kepano com adições da comunidade (journal, meeting-notes, book-highlight, spaced-review).",(1,0,1,0)),
 ("MegaMem","C-Bjorn/MegaMem","MCP + grafo de conhecimento temporal (Graphiti). Rastreia como conceitos mudam ao longo do tempo. 12 graph tools + 11 vault tools.",(1,1,1,1)),
]
for name,repo,desc,P in p3:
    tools.append(t(name,"Segundo Cérebro/Dev","https://github.com/"+repo,desc,P,pricing="open-source",
                   access="mcp",repo="https://github.com/"+repo,
                   tags=["obsidian","claude","second-brain","github"],source=P3))

# ---- write catalog.json ----
cat = {
 "_meta": {
   "descricao": "Catalogo de ferramentas de valor extraidas de 3 threads do X.",
   "fontes": {"post1_50_sites": P1, "post2_10_scrapers": P2, "post3_10_segundo_cerebro": P3},
   "gerado_em": datetime.date.today().isoformat(),
   "total": len(tools)
 },
 "tools": tools
}
with open(os.path.join(BASE,"web","catalog.json"),"w",encoding="utf-8") as f:
    json.dump(cat,f,ensure_ascii=False,indent=1)

# ---- build SQLite db ----
db = os.path.join(BASE,"db","toolkit.db")
if os.path.exists(db): os.remove(db)
con = sqlite3.connect(db)
con.executescript(open(os.path.join(BASE,"db","schema.sql"),encoding="utf-8").read())
for x in tools:
    con.execute("""INSERT INTO tools(name,category,url,repo_url,description,
      value_productive,value_monetizable,value_development,value_analytical,
      access_method,pricing,tags,source_post) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)""",
      (x["name"],x["category"],x["url"],x["repo_url"],x["description"],
       x["value_productive"],x["value_monetizable"],x["value_development"],x["value_analytical"],
       x["access_method"],x["pricing"],",".join(x["tags"]),x["source_post"]))
con.commit()
n = con.execute("SELECT COUNT(*) FROM tools").fetchone()[0]
mon = con.execute("SELECT COUNT(*) FROM tools WHERE value_monetizable=1").fetchone()[0]
dev = con.execute("SELECT COUNT(*) FROM tools WHERE value_development=1").fetchone()[0]
ana = con.execute("SELECT COUNT(*) FROM tools WHERE value_analytical=1").fetchone()[0]
con.close()
print(f"OK: {n} ferramentas | monetizaveis={mon} dev={dev} analiticas={ana}")
