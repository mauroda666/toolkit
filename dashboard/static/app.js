let DATA = { tools: [], agents: [], skills: [], stats: {} };
let TAB = "tools", Q = "", FILTER = "";
let TEAM = []; // {type,id,name}
let CUR = null; // detalhe aberto {type,id,name,prefix}
const $ = (s) => document.querySelector(s);
const grid = $("#grid"), empty = $("#empty"), countEl = $("#count");
const vlabels = { value_productive: "Prod", value_monetizable: "💰Mon", value_development: "Dev", value_analytical: "Anal" };

fetch("/api/data").then(r => r.json()).then(d => { DATA = d; renderStats(); syncFilter(); render(); })
  .catch(() => { countEl.textContent = "Falha ao carregar /api/data"; });

function renderStats() {
  const s = DATA.stats || {};
  $("#stats").innerHTML =
    `<div class="stat"><b>${s.tools||0}</b> ferramentas</div>` +
    `<div class="stat"><b>${s.agents||0}</b> agentes</div>` +
    `<div class="stat"><b>${s.skills||0}</b> skills</div>`;
}

document.querySelectorAll(".tab").forEach(t => t.addEventListener("click", () => {
  document.querySelectorAll(".tab").forEach(x => x.classList.remove("on"));
  t.classList.add("on"); TAB = t.dataset.t; FILTER = ""; syncFilter(); render();
}));
$("#q").addEventListener("input", e => { Q = e.target.value.toLowerCase(); render(); });
$("#filter").addEventListener("change", e => { FILTER = e.target.value; render(); });

function syncFilter() {
  const sel = $("#filter"); let opts = [];
  if (TAB === "tools") opts = [...new Set(DATA.tools.map(x => x.category).filter(Boolean))].sort();
  else if (TAB === "agents") opts = [...new Set(DATA.agents.map(x => x.division).filter(Boolean))].sort();
  const label = TAB === "tools" ? "categorias" : TAB === "agents" ? "divisões" : "";
  sel.style.display = opts.length ? "" : "none";
  sel.innerHTML = `<option value="">Todas ${label}</option>` + opts.map(o => `<option value="${o}">${o}</option>`).join("");
}
const matches = (h) => !Q || h.toLowerCase().includes(Q);
const esc = (s) => (s||"").replace(/[&<>"]/g, c => ({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));

function render() {
  let rows = [];
  if (TAB === "tools") {
    rows = DATA.tools.filter(t => matches((t.name||"")+" "+(t.description||"")+" "+(t.category||"")+" "+(t.tags||[]).join(" ")) && (!FILTER||t.category===FILTER));
    grid.innerHTML = rows.map(toolCard).join("");
  } else if (TAB === "agents") {
    rows = DATA.agents.filter(a => matches((a.name||"")+" "+(a.description||"")+" "+(a.division||"")) && (!FILTER||a.division===FILTER));
    grid.innerHTML = rows.map(a => itemCard("agent", a, a.division, a.emoji, a.vibe)).join("");
  } else {
    rows = DATA.skills.filter(s => matches((s.name||"")+" "+(s.description||"")));
    grid.innerHTML = rows.map(s => itemCard("skill", s, "skill", "", "")).join("");
  }
  empty.style.display = rows.length ? "none" : "block";
  countEl.textContent = rows.length + " itens";
}

function toolCard(t) {
  const vals = Object.keys(vlabels).map(k => `<span class="v ${t[k]?"on":""}">${vlabels[k]}</span>`).join("");
  const tags = (t.tags||[]).slice(0,4).map(x => `<span class="tag">${esc(x)}</span>`).join("");
  return `<div class="card"><h3>${esc(t.name)}</h3>
    <div class="row"><span class="tag">${esc(t.category||"—")}</span><span class="tag">${esc(t.pricing||"")}</span></div>
    <p>${esc(t.description||"")}</p><div class="row">${vals}</div><div class="row">${tags}</div>
    ${t.url?`<a class="open" href="${esc(t.url)}" target="_blank" rel="noopener">Abrir →</a>`:""}</div>`;
}
function itemCard(type, x, badge, emoji, vibe) {
  return `<div class="card click" data-type="${type}" data-id="${esc(x.id)}">
    <h3>${emoji?esc(emoji)+" ":""}${esc(x.name)}</h3>
    <div class="row"><span class="tag">${esc(badge)}</span></div>
    <p>${esc(x.description||"")}</p>
    ${vibe?`<p style="color:#c792ea">${esc(vibe)}</p>`:""}
    <button class="add" data-add="1" data-type="${type}" data-id="${esc(x.id)}" data-name="${esc(x.name)}">+ time</button>
  </div>`;
}

grid.addEventListener("click", (e) => {
  const add = e.target.closest("[data-add]");
  if (add) { e.stopPropagation(); addToTeam(add.dataset.type, add.dataset.id, add.dataset.name); return; }
  const card = e.target.closest(".card.click");
  if (card) openDetail(card.dataset.type, card.dataset.id);
});

function openDetail(type, id) {
  fetch(`/api/${type}/${encodeURIComponent(id)}`).then(r => r.json()).then(d => {
    if (d.error) return;
    CUR = { type, id, name: d.name, prefix: d.prompt };
    $("#mTitle").textContent = d.name;
    $("#mSub").textContent = type === "agent" ? `agente · ${d.division||""}` : "skill";
    $("#mDesc").textContent = d.description || "";
    $("#mTask").value = "";
    $("#mPrompt").value = d.prompt;
    $("#mSrc").textContent = d.source || "";
    $("#modal").classList.add("on");
  });
}
$("#mTask").addEventListener("input", () => { if (CUR) $("#mPrompt").value = CUR.prefix + $("#mTask").value; });
$("#mCopy").addEventListener("click", () => copyText($("#mPrompt").value));
$("#mAdd").addEventListener("click", () => { if (CUR) { addToTeam(CUR.type, CUR.id, CUR.name); } });
$("#mClose").addEventListener("click", () => $("#modal").classList.remove("on"));
$("#modal").addEventListener("click", e => { if (e.target.id === "modal") $("#modal").classList.remove("on"); });

function addToTeam(type, id, name) {
  if (!TEAM.some(m => m.type === type && m.id === id)) TEAM.push({ type, id, name });
  updateTray(); toast(`Adicionado ao time: ${name}`);
}
function updateTray() {
  const b = $("#trayBtn"); b.textContent = `🧩 Time (${TEAM.length})`;
  b.classList.toggle("on", TEAM.length > 0);
}
$("#trayBtn").addEventListener("click", openTeam);
function openTeam() {
  $("#teamList").innerHTML = TEAM.length ? TEAM.map(m => `${m.type==="agent"?"🧠":"⚙️"} ${esc(m.name)}`).join(" · ") : "Time vazio.";
  buildTeamPrompt();
  $("#teamModal").classList.add("on");
}
$("#teamTask").addEventListener("input", buildTeamPrompt);
function buildTeamPrompt() {
  const task = $("#teamTask").value || "<descreva a tarefa>";
  const lines = TEAM.map(m => `- ${esc(m.name)} (${m.type === "agent" ? "agente" : "skill"})`).join("\n");
  $("#teamPrompt").value = `Monte um time e acione cada um no seu papel para a tarefa abaixo.\n\nTarefa: ${task}\n\nTime:\n${lines}`;
}
$("#teamCopy").addEventListener("click", () => copyText($("#teamPrompt").value));
$("#teamClear").addEventListener("click", () => { TEAM = []; updateTray(); openTeam(); });
$("#teamClose").addEventListener("click", () => $("#teamModal").classList.remove("on"));
$("#teamModal").addEventListener("click", e => { if (e.target.id === "teamModal") $("#teamModal").classList.remove("on"); });

function copyText(text) {
  const done = () => toast("Copiado ✓");
  if (navigator.clipboard && window.isSecureContext) {
    navigator.clipboard.writeText(text).then(done).catch(() => fallbackCopy(text, done));
  } else fallbackCopy(text, done);
}
function fallbackCopy(text, done) {
  const ta = document.createElement("textarea");
  ta.value = text; ta.style.position = "fixed"; ta.style.opacity = "0";
  document.body.appendChild(ta); ta.focus(); ta.select();
  try { document.execCommand("copy"); done(); } catch (e) { toast("Selecione e copie manual"); }
  document.body.removeChild(ta);
}
let toastT;
function toast(msg) {
  const t = $("#toast"); t.textContent = msg; t.classList.add("on");
  clearTimeout(toastT); toastT = setTimeout(() => t.classList.remove("on"), 1600);
}
