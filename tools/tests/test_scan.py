import subprocess, time, sys
from playwright.sync_api import sync_playwright
srv=subprocess.Popen(['python3','-m','http.server','8771','-d','www'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL); time.sleep(1)
RX='''<html><body style="margin:0;background:#fff;font-family:Arial;width:800px;padding:40px;color:#111;transform:rotate(-1deg)">
<div style="font-size:26px;font-weight:bold">Skin Care Clinic</div><div style="font-size:16px">Dr. A. Kulkarni, MD (DVL) &nbsp; Reg. No. 12345</div><hr>
<div style="font-size:20px;margin:16px 0">Name: Mrs. Sunita Patil &nbsp;&nbsp; Age: 34 Y / F &nbsp;&nbsp; Date: 12/09/2026</div>
<div style="font-size:20px">Dx: Tinea cruris</div>
<div style="font-size:30px;margin-top:20px">Rx</div>
<div style="font-size:21px;line-height:2">1. Cap Itratuf 200 &nbsp; 1-0-0 after food x 2 weeks<br>2. Lilituf cream &nbsp; BD x 4 weeks<br>3. Tab Levocetirizine 5 mg &nbsp; HS x 10 days</div>
<div style="font-size:18px;margin-top:30px">Review after 2 weeks</div></body></html>'''
try:
  with sync_playwright() as p:
    b=p.chromium.launch(); ctx=b.new_context(viewport={'width':390,'height':860},service_workers=sys.argv[1] if len(sys.argv)>1 else 'block')
    ctx.route('**/config.js', lambda r: r.fulfill(body='window.DRX_CONFIG={}', content_type='application/javascript'))
    im=ctx.new_page(); im.set_viewport_size({'width':900,'height':700}); im.set_content(RX); im.screenshot(path='rx_sample.png'); im.close()
    pg=ctx.new_page(); errs=[]; pg.on('pageerror',lambda e:errs.append(str(e))); pg.on('console',lambda m: m.type=='error' and errs.append(m.text))
    pg.goto('http://localhost:8771/'); pg.wait_for_timeout(1500)
    pg.click('[data-tab=patients]'); pg.wait_for_timeout(300); pg.click('[data-act=newpatient]'); pg.wait_for_timeout(400)
    print('scan box visible?', pg.locator('#ppScGal').count()==1)
    t=time.time(); pg.set_input_files('#ppScGal','rx_sample.png')
    pg.wait_for_selector('#scApply', timeout=120000); print('OCR secs', round(time.time()-t,1))
    print(pg.locator('#sheet2Body').inner_text()[:1500])
    pg.screenshot(path='scan_review.png', full_page=False)
    pg.click('#scApply'); pg.wait_for_timeout(500)
    print('FILLED:', pg.input_value('#ppName'), pg.input_value('#ppAge'), pg.input_value('#ppSex'), pg.input_value('#ppDate'))
    print('RX:', pg.locator('#ppRx').inner_text()[:600])
    pg.screenshot(path='scan_filled.png')
    print('errors', errs)
finally: srv.kill()
