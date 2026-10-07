import subprocess, time, sys
from playwright.sync_api import sync_playwright
W=sys.argv[1]
srv=subprocess.Popen(['python3','-m','http.server','8781','-d',W],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL); time.sleep(1)
try:
  with sync_playwright() as p:
    b=p.chromium.launch(); ctx=b.new_context(viewport={'width':390,'height':844},service_workers='block')
    ctx.route('**/config.js', lambda r: r.fulfill(body='window.DRX_CONFIG={}', content_type='application/javascript'))
    ctx.add_init_script("try{localStorage.setItem('drx.tour','1')}catch(e){}")
    pg=ctx.new_page(); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto('http://localhost:8781/'); pg.wait_for_timeout(2000)
    print('tabs:', pg.locator('nav.tabs').inner_text().replace('\n',' | '))
    print('tagline:', pg.locator('#drline').inner_text(), '| boot gone:', pg.locator('#boot').count()==0)
    pg.screenshot(path='v2_cases.png')
    # case back navigation
    pg.locator('#caseList details summary').first.click(); pg.wait_for_timeout(200)
    pg.locator('#caseList [data-case]').first.click(); pg.wait_for_timeout(300)
    t1=pg.locator('.case-title').inner_text(); pg.locator('[data-casego]').last.click(); pg.wait_for_timeout(300); t2=pg.locator('.case-title').inner_text()
    pg.click('#sheetClose'); pg.wait_for_timeout(300); t3=pg.locator('.case-title').inner_text() if pg.locator('#sheet').is_visible() else 'CLOSED'
    pg.click('#sheetClose'); pg.wait_for_timeout(300)
    print('back nav:', t1,'->',t2,'-> back ->',t3, '| sheet closed:', not pg.locator('#sheet').is_visible(), '| group still open:', pg.locator('#caseList details[open]').count()>0)
    print('csrc removed:', 'original wording' not in pg.content())
    # drugs tab
    pg.click('[data-tab=meds]'); pg.wait_for_timeout(300)
    for d in ['Isotretinoin','Doxycycline','Itraconazole','Simvastatin']:
        pg.fill('#ixQ', d); pg.wait_for_timeout(150); pg.keyboard.press('Enter'); pg.wait_for_timeout(150)
    print('ix:', pg.locator('#ixRes').inner_text().replace('\n',' | ')[:400]); pg.screenshot(path='v2_ix.png')
    pg.click('[data-dtab=dose]'); pg.wait_for_timeout(300); print('dose tab has calc:', pg.locator('#wtSel').count()==1)
    pg.click('[data-dtab=safety]'); pg.wait_for_timeout(300); t=pg.locator('#dsList2').inner_text(); print('safety has upadacitinib:', 'Upadacitinib' in t, '| wolverton text gone:', 'Wolverton' not in pg.locator('#main').inner_text())
    pg.click('[data-dtab=brands]'); pg.wait_for_timeout(300); print('brands list rows:', pg.locator('#medList [data-br]').count())
    # corner
    pg.evaluate('window.DRX && (window.DRX.isAdmin=true)')
    pg.click('[data-tab=corner]'); pg.wait_for_timeout(400); print('corner:', pg.locator('#main').inner_text().replace('\n',' | ')[:300]); pg.screenshot(path='v2_corner.png')
    pg.locator('[data-post]').first.click(); pg.wait_for_timeout(300); print('post:', pg.locator('#sheet .post').inner_text()[:150].replace('\n',' | ')); pg.screenshot(path='v2_post.png'); pg.click('#sheetClose'); pg.wait_for_timeout(200)
    # more via header
    pg.click('#btnMoreTop'); pg.wait_for_timeout(300); print('more view:', pg.locator('.viewhead h2').inner_text())
    # templates review badge
    pg.click('[data-tab=templates]'); pg.wait_for_timeout(300); print('needs review badges:', pg.locator('.rvbadge').count())
    # patient page: interactions + mic
    pg.click('[data-tab=patients]'); pg.wait_for_timeout(300); pg.click('[data-act=newpatient]'); pg.wait_for_timeout(400)
    print('mics:', pg.locator('[data-mic]').count(), '| ix button:', pg.locator('#ppIx').count())
    pg.fill('#ppMeds','Simvastatin'); pg.click('#ppAdd'); pg.wait_for_timeout(300); pg.fill('#mpQ','Itratuf'); pg.wait_for_timeout(300); pg.locator('[data-mpb]').first.click(); pg.wait_for_timeout(300); pg.click('#ddSave'); pg.wait_for_timeout(400)
    print('auto ix on patient:', pg.locator('#ppSafeBody .ixauto').inner_text().replace('\n',' | ')[:200] if pg.locator('#ppSafeBody .ixauto').count() else 'NONE')
    print('errors', errs)
finally: srv.kill()
