import sys
from playwright.sync_api import sync_playwright
C='/usr/bin/google-chrome';u,pre=sys.argv[1],sys.argv[2]
with sync_playwright() as p:
    b=p.chromium.launch(executable_path=C)
    for n,vw,mob in [("desktop",(1440,900),False),("mobile",(390,844),True)]:
        ctx=b.new_context(viewport={"width":vw[0],"height":vw[1]},is_mobile=mob,has_touch=mob,reduced_motion='reduce' if pre=='after' else 'no-preference')
        pg=ctx.new_page();errs=[];pg.on('pageerror',lambda e:errs.append(str(e)));pg.goto(u,wait_until='networkidle',timeout=60000);pg.wait_for_timeout(2000)
        h=pg.evaluate("document.body.scrollHeight")
        for y in range(0,h,500): pg.evaluate(f"scrollTo(0,{y})");pg.wait_for_timeout(100)
        pg.evaluate("scrollTo(0,0)");pg.wait_for_timeout(800)
        pg.screenshot(path=f"{pre}-{n}.png",full_page=True);print(n,errs);ctx.close()
    b.close()
