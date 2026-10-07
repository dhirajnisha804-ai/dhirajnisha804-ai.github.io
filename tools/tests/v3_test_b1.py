import subprocess, time, json
from playwright.sync_api import sync_playwright
srv=subprocess.Popen(['python3','-m','http.server','8770','-d','www'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL); time.sleep(1)
PR=json.dumps({"checkedAt":"2026-10-01","items":{"p-x":{"price":120,"date":"2026-10-01","source":"Apollo Pharmacy, checked 1 Oct 2026"}}})
try:
  with sync_playwright() as p:
    b=p.chromium.launch(); ctx=b.new_context(viewport={'width':390,'height':860},service_workers='block'); ctx.add_init_script("try{localStorage.setItem('drx.tour','1')}catch(e){}"); ctx.add_init_script('if(!localStorage.getItem(\'__mockstore\')){localStorage.setItem(\'__mockstore\',"{\\"brands\\": {\\"p-dabur-femcinol-adp\\": {\\"product\\": \\"Femcinol-ADP gel\\", \\"brand\\": \\"Dabur\\", \\"category\\": \\"Anti-acne (topical)\\", \\"composition\\": \\"Adapalene + Clindamycin\\", \\"price\\": 175, \\"pack\\": \\"15 g\\", \\"mrName\\": \\"Shubham Dubey\\", \\"mrPhone\\": \\"9118079126\\", \\"updatedAt\\": 1}, \\"p-x\\": {\\"product\\": \\"Xcream\\", \\"brand\\": \\"Y\\", \\"category\\": \\"Other\\", \\"composition\\": \\"z\\", \\"price\\": 100, \\"pack\\": \\"10 g\\", \\"updatedAt\\": 1}}, \\"templates\\": {\\"t1\\": {\\"name\\": \\"T1\\", \\"rx\\": [], \\"free\\": true}}, \\"users\\": {\\"u-col\\": {\\"name\\": \\"Col\\", \\"status\\": \\"verified\\"}}, \\"verifications\\": {}, \\"posts\\": {}}");localStorage.setItem(\'__mockaccounts\',"{\\"dhirajnisha804@gmail.com\\": {\\"uid\\": \\"u-admin\\", \\"pw\\": \\"pw\\", \\"verified\\": true}, \\"col@doc.in\\": {\\"uid\\": \\"u-col\\", \\"pw\\": \\"pw\\", \\"verified\\": true}}");localStorage.setItem(\'__mockuser\',"\\"col@doc.in\\"")}')
    ctx.route('**/config.js', lambda r: r.fulfill(body='window.DRX_CONFIG={adminEmail:"dhirajnisha804@gmail.com",firebase:{apiKey:"k",projectId:"p"}}', content_type='application/javascript'))
    ctx.route('**/vendor/firebase-app-compat.js', lambda r: r.fulfill(body=open('mockfb3.js').read(), content_type='application/javascript'))
    for f in ['auth','firestore']: ctx.route(f'**/vendor/firebase-{f}-compat.js', lambda r: r.fulfill(body='', content_type='application/javascript'))
    ctx.route('**/prices.json', lambda r: r.fulfill(body=PR, content_type='application/json'))
    pg=ctx.new_page(); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('http://localhost:8770/'); pg.wait_for_timeout(1500)
    pg.click('[data-tab=meds]'); pg.wait_for_timeout(250); pg.click('[data-dtab=brands]'); pg.wait_for_timeout(250); pg.wait_for_timeout(400)
    txt=pg.locator('#main').inner_text()
    print('1 colleague sees shared MR?', 'Shubham' in txt, '| overridden price 120 shown?', '₹120' in txt, '| Updated date?', 'Updated 1 Oct 2026' in txt)
    # colleague adds own MR to Xcream
    pg.fill('input[type=search]','Xcream'); pg.wait_for_timeout(300)
    pg.locator('[data-br="p-x"]').click(); pg.wait_for_timeout(400)
    print('2 product fields locked for colleague?', pg.locator('#bProduct').is_disabled())
    pg.fill('#bMrName','My MR'); pg.fill('#bMrPhone','9000000000'); pg.click('#bSave'); pg.wait_for_timeout(500)
    print('   toast:', pg.locator('#toast').inner_text())
    print('   shared store untouched?', 'mrName' not in pg.evaluate("JSON.stringify([...__store.brands.get('p-x') ? Object.keys(__store.brands.get('p-x')) : []])"))
    pg.reload(); pg.wait_for_timeout(1500); pg.click('[data-tab=meds]'); pg.wait_for_timeout(250); pg.click('[data-dtab=brands]'); pg.wait_for_timeout(250); pg.fill('input[type=search]','Xcream'); pg.wait_for_timeout(400)
    print('3 own MR persists on phone?', 'My MR' in pg.locator('#main').inner_text())
    # colleague adds own new product
    pg.fill('input[type=search]',''); pg.click('[data-act=newbrand]'); pg.wait_for_timeout(300); pg.fill('#bProduct','MyLocalCream'); pg.click('#bSave'); pg.wait_for_timeout(400)
    pg.fill('input[type=search]','MyLocalCream'); pg.wait_for_timeout(300); print('4 colleague own product saved locally?', 'MyLocalCream' in pg.locator('#main').inner_text(), '| not in shared?', pg.evaluate("!__store.brands.size || ![...__store.brands.values()].some(x=>x.product==='MyLocalCream')"))
    # owner signs in -> migration moves Shubham into owner's phone
    pg.click('#btnMoreTop'); pg.wait_for_timeout(200); pg.click('[data-act=sync]'); pg.wait_for_timeout(300)
    pg.fill('#syEm','dhirajnisha804@gmail.com'); pg.fill('#syPw','pw'); pg.click('#syIn'); pg.wait_for_timeout(1500)
    print('5 migration removed MR from shared?', pg.evaluate("!('mrName' in __store.brands.get('p-dabur-femcinol-adp'))"))
    pg.keyboard.press('Escape'); pg.wait_for_timeout(200); pg.click('[data-tab=meds]'); pg.wait_for_timeout(250); pg.click('[data-dtab=brands]'); pg.wait_for_timeout(250); pg.fill('input[type=search]','Femcinol'); pg.wait_for_timeout(400)
    print('   owner still sees Shubham on her phone?', 'Shubham' in pg.locator('#main').inner_text())
    # owner edits price -> shared updated with priceDate
    pg.locator('[data-br="p-dabur-femcinol-adp"]').click(); pg.wait_for_timeout(300); print('   owner fields editable?', not pg.locator('#bPrice').is_disabled()); pg.fill('#bPrice','180'); pg.click('#bSave'); pg.wait_for_timeout(500)
    print('6 shared price now', pg.evaluate("__store.brands.get('p-dabur-femcinol-adp').price"), pg.evaluate("__store.brands.get('p-dabur-femcinol-adp').priceDate"), '| MR not re-shared?', pg.evaluate("!('mrName' in __store.brands.get('p-dabur-femcinol-adp'))"))
    # follow-up + help
    pg.click('[data-tab=patients]'); pg.wait_for_timeout(300); pg.click('[data-act=newpatient]'); pg.wait_for_timeout(400)
    pg.fill('#ppName','FU Test'); pg.fill('#ppFu','2026-11-15'); print('7 PDF button on new patient?', pg.locator('#ppPdf').count()==1); pg.click('#ppSave'); pg.wait_for_timeout(600)
    fu=pg.evaluate("(async()=>{const db=await window.claude.use('db');const s=await db.collection('visits').get();return s.docs.map(d=>d.data().fu)})()"); print('   saved follow-up', fu)
    pg.click('#btnMoreTop'); pg.wait_for_timeout(200); pg.click('[data-act=help]'); pg.wait_for_timeout(300)
    print('8 help shows email?', 'dhirajnisha804@gmail.com' in pg.locator('#sheet').inner_text()); pg.screenshot(path='b1_help.png')
    print('errors', errs[:5]); b.close()
finally: srv.kill()
