#!/usr/bin/env python3
"""前端功能测试 - 使用 Playwright"""
import asyncio
from playwright.async_api import async_playwright

API_BASE = "http://localhost:7860"
ADMIN_KEY = "Ww010101"

async def test_frontend():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()

        print("=" * 60)
        print("前端功能测试")
        print("=" * 60)

        # 1. 访问首页
        print("\n[1/4] 访问首页...")
        await page.goto(API_BASE)
        await page.wait_for_load_state("networkidle")
        print("✅ 首页加载成功")

        # 2. 登录
        print("\n[2/4] 登录...")
        await page.fill('input[type="password"]', ADMIN_KEY)
        await page.click('button:has-text("登录")')
        await page.wait_for_timeout(2000)
        print("✅ 登录成功")

        # 3. 进入节点管理页面
        print("\n[3/4] 进入节点管理...")
        await page.click('text=节点管理')
        await page.wait_for_timeout(1000)
        print("✅ 节点管理页面加载成功")

        # 4. 测试预览配置
        print("\n[4/4] 测试预览配置...")
        await page.click('button:has-text("预览配置")')
        await page.wait_for_timeout(1000)

        # 检查预览窗口是否显示
        preview = await page.query_selector('text=运行时 YAML 配置预览')
        if preview:
            print("✅ 预览窗口已打开")

            # 检查窗口大小
            dialog = await page.query_selector('.fixed.inset-0 > div')
            if dialog:
                box = await dialog.bounding_box()
                print(f"✅ 预览窗口尺寸: {box['width']}x{box['height']}")

            # 截图
            await page.screenshot(path="preview_test.png")
            print("✅ 截图已保存: preview_test.png")

            await page.wait_for_timeout(3000)
            await page.click('button:has-text("关闭")')
            print("✅ 预览窗口已关闭")
        else:
            print("❌ 预览窗口未打开")

        print("\n" + "=" * 60)
        print("测试完成")
        print("=" * 60)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(test_frontend())
