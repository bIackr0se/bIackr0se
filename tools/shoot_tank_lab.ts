import { spawn } from "node:child_process";
import { mkdtempSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os"; import { join } from "node:path";
import { createServer, type AddressInfo } from "node:net";
const PORT = await new Promise<number>((r) => { const s = createServer(); s.listen(0, "127.0.0.1", () => { const p = (s.address() as AddressInfo).port; s.close(() => r(p)); }); });
const chrome = spawn("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", ["--headless=new", "--enable-unsafe-swiftshader", "--use-angle=swiftshader", "--hide-scrollbars", `--remote-debugging-port=${PORT}`, `--user-data-dir=${mkdtempSync(join(tmpdir(), "tl-"))}`, "about:blank"], { stdio: "ignore" });
const sleep = (ms: number) => new Promise((r) => setTimeout(r, ms));
let list: any; for (let i = 0; i < 80 && !list; i++) { try { list = await (await fetch(`http://127.0.0.1:${PORT}/json/list`)).json(); } catch { await sleep(250); } }
const ws = new WebSocket(list.find((t: any) => t.type === "page").webSocketDebuggerUrl);
await new Promise((r) => (ws.onopen = r));
let id = 0; const w = new Map<number, (v: any) => void>();
ws.onmessage = (e) => { const m = JSON.parse(String(e.data)); if (m.id && w.has(m.id)) { w.get(m.id)!(m); w.delete(m.id); } };
const send = (method: string, params: any = {}) => new Promise<any>((r) => { const n = ++id; w.set(n, r); ws.send(JSON.stringify({ id: n, method, params })); });
const ev = async (e: string) => (await send("Runtime.evaluate", { expression: e, returnByValue: true, awaitPromise: true })).result?.result?.value;
try {
  await send("Emulation.setDeviceMetricsOverride", { width: 1280, height: 800, deviceScaleFactor: 2, mobile: false });
  await send("Page.enable"); await send("Page.navigate", { url: "https://biackr0se.github.io/tank-lab/" }); await sleep(6000);
  const press = async (sel: string) => {
    const pt = await ev(`(() => { const el = ${sel}; if (!el) return null; const r = el.getBoundingClientRect(); return { x: r.x + r.width / 2, y: r.y + r.height / 2 }; })()`);
    if (!pt) return false;
    for (const type of ["mouseMoved", "mousePressed", "mouseReleased"]) await send("Input.dispatchMouseEvent", { type, x: pt.x, y: pt.y, button: "left", clickCount: 1 });
    await sleep(300); return true;
  };
  const byText = (t: string) => `[...document.querySelectorAll('button')].find(b => b.textContent.trim() === ${JSON.stringify(t)})`;
  console.log("stealthy", await press(byText("Stealthy")), "speed", await press(byText("120×")), "switch", await press(`document.querySelector('[role=switch]')`));
  console.log("checked", await ev(`document.querySelector('[role=switch]')?.getAttribute('aria-checked')`), await ev(`document.body.innerText.slice(0, 200)`));
  let head = "";
  for (let i = 0; i < 240; i++) { head = await ev(`document.body.innerText.includes('tripped the pump') ? 'tripped' : ''`); if (head) break; await sleep(1000); }
  console.log("state", head || "never tripped");
  await sleep(6000); // let the trip settle into the charts, as in the pane
  const shot = await send("Page.captureScreenshot", { format: "png" });
  writeFileSync(process.argv[2], Buffer.from(shot.result.data, "base64"));
  console.log("saved", process.argv[2]);
} finally { chrome.kill(); }
process.exit(0);
