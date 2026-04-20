import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1200, "height": 960})
        await page.goto("file:///C:/Users/Administrator/WorkBuddy/20260420145625/assets/product-arch-diagram.html")
        await asyncio.sleep(1)
        await page.screenshot(
            path="C:/Users/Administrator/WorkBuddy/20260420145625/assets/product-arch-diagram.png",
            full_page=True
        )
        await browser.close()
        print("Screenshot saved!")

asyncio.run(main())
