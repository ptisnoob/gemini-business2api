"""测试静默模式浏览器"""
import time
from core.gemini_automation import GeminiAutomation

def test_silent_mode():
    print("🧪 测试静默模式...")

    automation = GeminiAutomation(
        browser_mode="silent",
        timeout=30,
        log_callback=lambda level, msg: print(f"[{level}] {msg}")
    )

    try:
        page = automation._create_page()
        print("✅ 浏览器已启动（静默模式）")
        print("⏳ 等待 10 秒，请检查任务栏是否有最小化的浏览器窗口...")

        page.get("https://www.google.com")
        print("✅ 已导航到 Google")

        time.sleep(10)

        page.quit()
        print("✅ 测试完成")

    except Exception as e:
        print(f"❌ 测试失败: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_silent_mode()
