import subprocess, time, json
from playwright.sync_api import sync_playwright
srv=subprocess.Popen(['python3','-m','http.server','8774','-d','www'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL); time.sleep(1)
MOCK={"brands":{},"templates":{
 "t-discoid-lupus-erythematosus":{"name":"DLE old","rx":[{"drug":"Tab HCQ","freq":"BD"}],"updatedAt":1791035262768},
 "t-oral-candidiasis-thrush":{"name":"Thrush EDITED BY OWNER","rx":[],"updatedAt":1791099999999}}}
try:
  with sync_playwright() as p:
    b=p.chromium.launch(); ctx=b.new_context(viewport={'width':390,'height':860},service_workers='block')
    errs=[]
    # ---- part A: seed mode UI tests
    ctx.route('**/config.js', lambda r: r.fulfill(body='window.DRX_CONFIG={}', content_type='application/javascript'))
    pg=ctx.new_page(); pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('http://localhost:8774/'); pg.wait_for_timeout(1500)
    # More -> Dose by weight
    pg.click('[data-tab=more]'); pg.wait_for_timeout(200); pg.click('[data-act=wtcalc]'); pg.wait_for_timeout(300)
    pg.fill('#wtQ','griseo'); pg.wait_for_timeout(100)
    pg.select_option('#wtSel', label=pg.locator('#wtSel option').first.inner_text())
    pg.fill('#wtW','20'); pg.fill('#wtA','7'); pg.wait_for_timeout(150)
    print('A1 griseofulvin 20kg:', pg.locator('#wtOut').inner_text().replace('\n',' | ')[:300])
    pg.fill('#wtQ','rituximab'); pg.wait_for_timeout(100)
    opts=pg.locator('#wtSel option').all_inner_texts(); print('   rituximab opts', opts)
    pg.select_option('#wtSel', index=[i for i,o in enumerate(opts) if 'lymphoma' in o.lower() or 'm²' in o][0] if any('lymph' in o.lower() for o in opts) else 0)
    pg.fill('#wtW','60'); pg.fill('#wtA','40'); pg.fill('#wtH','160'); pg.wait_for_timeout(150)
    print('A2 rituximab m2:', pg.locator('#wtOut').inner_text().replace('\n',' | ')[:250])
    pg.keyboard.press('Escape'); pg.goto('http://localhost:8774/'); pg.wait_for_timeout(1200)
    # patient page: dose by weight button
    pg.click('[data-tab=patients]'); pg.wait_for_timeout(300); pg.click('[data-act=newpatient]'); pg.wait_for_timeout(400)
    pg.fill('#ppName','Wt Kid'); pg.fill('#ppAge','8'); pg.fill('#ppWt','25')
    pg.click('#ppWtc'); pg.wait_for_timeout(300)
    pg.fill('#wtQ','ivermectin'); pg.wait_for_timeout(100)
    print('B1 ivermectin kid 25kg:', pg.locator('#wtOut').inner_text().replace('\n',' | ')[:250])
    pg.click('#wtUse'); pg.wait_for_timeout(300)
    print('   rx:', pg.locator('#ppRx').inner_text().replace('\n',' | ')[:200])
    # med picker -> Itratuf -> details calc
    pg.click('#ppAdd'); pg.wait_for_timeout(300); pg.fill('#mpQ','Itratuf'); pg.wait_for_timeout(300)
    pg.locator('[data-mpb]').first.click(); pg.wait_for_timeout(300)
    print('C1 details has calc?', pg.locator('#ddWtD').count()==1)
    pg.click('#ddWtD summary'); pg.wait_for_timeout(300)
    print('   options:', pg.locator('#ddWt #wtSel option').all_inner_texts())
    print('   out:', pg.locator('#ddWt #wtOut').inner_text().replace('\n',' | ')[:220])
    pg.click('#ddWt #wtUse'); pg.wait_for_timeout(200)
    print('   dose field:', pg.input_value('#ddDose'), '| freq', pg.input_value('#ddFreq'), '| dur', pg.input_value('#ddDur'))
    pg.screenshot(path='wt_details.png')
    pg.click('#ddSave'); pg.wait_for_timeout(300)
    pg.locator('#ppRx').scroll_into_view_if_needed(); pg.screenshot(path='wt_rx.png')
    # topical should not get calculator
    pg.click('#ppAdd'); pg.wait_for_timeout(300); pg.fill('#mpQ','Lilituf'); pg.wait_for_timeout(300); pg.locator('[data-mpb]').first.click(); pg.wait_for_timeout(300)
    print('C2 topical has calc? (expect False)', pg.locator('#ddWtD').count()==1)
    pg.keyboard.press('Escape')
    # drug safety detail shows Wolverton
    pg.goto('http://localhost:8774/'); pg.wait_for_timeout(1200)
    pg.click('[data-tab=more]'); pg.wait_for_timeout(200)
    # templates count
    pg.click('[data-tab=templates]') if pg.locator('[data-tab=templates]').count() else None; pg.wait_for_timeout(400)
    print('D1 templates text has Chancroid?', 'Chancroid' in pg.locator('#main').inner_text())
    pg.close()
    # ---- part B: publish logic with mock firebase (owner)
    ctx2=b.new_context(viewport={'width':390,'height':860},service_workers='block')
    ctx2.add_init_script("if(!localStorage.getItem('__mockstore')) localStorage.setItem('__mockstore', %s)" % json.dumps(json.dumps(MOCK)))
    ctx2.route('**/config.js', lambda r: r.fulfill(body='window.DRX_CONFIG={adminEmail:"dhirajnisha804@gmail.com",firebase:{apiKey:"k",projectId:"p"}}', content_type='application/javascript'))
    ctx2.route('**/vendor/firebase-app-compat.js', lambda r: r.fulfill(body=open('mockfb2.js').read(), content_type='application/javascript'))
    for f in ['auth','firestore']: ctx2.route(f'**/vendor/firebase-{f}-compat.js', lambda r: r.fulfill(body='', content_type='application/javascript'))
    q=ctx2.new_page(); q.on('pageerror',lambda e:errs.append(str(e)))
    q.goto('http://localhost:8774/'); q.wait_for_timeout(1500)
    q.click('[data-tab=more]'); q.wait_for_timeout(200); q.click('[data-act=sync]'); q.wait_for_timeout(300)
    q.fill('#syEm','dhirajnisha804@gmail.com'); q.fill('#syPw','pw'); q.click('#syIn'); q.wait_for_timeout(1500)
    q.click('#syPub'); q.wait_for_timeout(3000)
    print('E1 msg:', q.locator('#syMsg').inner_text())
    print('   DLE updated (expect OD):', q.evaluate("__store.templates.get('t-discoid-lupus-erythematosus').rx[0].freq"))
    print('   owner-edited thrush kept:', q.evaluate("__store.templates.get('t-oral-candidiasis-thrush').name"))
    print('   templates now', q.evaluate("__store.templates.size"))
    print('errors', errs)
finally: srv.kill()
