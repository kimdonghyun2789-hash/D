// usage: node shot.js <scene> <out.png> <w> <h> [query]
let chromium; try { ({ chromium } = require('playwright')); } catch (e) { ({ chromium } = require('/opt/node22/lib/node_modules/playwright')); }
const http = require('http'); const fs=require('fs'); const path=require('path');
const root = __dirname;
const mime={'.html':'text/html','.js':'text/javascript','.json':'application/json','.png':'image/png'};
const srv=http.createServer((req,res)=>{let p=decodeURIComponent(req.url.split('?')[0]); let f=path.join(root,p); fs.readFile(f,(e,d)=>{ if(e){res.writeHead(404);res.end();return;} res.writeHead(200,{'Content-Type':mime[path.extname(f)]||'application/octet-stream'}); res.end(d);});});
(async()=>{
  await new Promise(r=>srv.listen(0,r)); const port=srv.address().port;
  const [scene,out,w,h,q] = process.argv.slice(2);
  const browser = await chromium.launch({args:['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
  const page = await browser.newPage({viewport:{width:+w,height:+h},deviceScaleFactor:1});
  page.on('console', m=>console.log('console:', m.text()));
  page.on('pageerror', e=>console.log('pageerror:', e.message));
  await page.goto(`http://localhost:${port}/web/render.html?scene=${scene}&w=${w}&h=${h}&${q||''}`);
  await page.waitForFunction(()=>window.__done===true,{timeout:900000});
  const info = await page.evaluate(()=>window.__info); console.log('info', info); fs.writeFileSync(out.replace(/\.png$/, '.json'), info || '{}');
  const imgs = await page.evaluate(()=>window.__images||null);
  if (imgs) { for (const im of imgs) { const b64 = im.data.split(',')[1]; fs.writeFileSync(out.replace(/\.png$/, '_' + im.name + '.png'), Buffer.from(b64,'base64')); } }
  else await page.screenshot({path:out, omitBackground:true});
  await browser.close(); srv.close();
})();
