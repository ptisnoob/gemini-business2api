#!/usr/bin/env python3
"""测试注册功能是否使用代理"""
import httpx
import json

API_BASE = "http://localhost:7860"

print("=" * 60)
print("测试注册功能")
print("=" * 60)

# 1. 登录
print("\n[1/3] 登录...")
try:
    resp = httpx.post(f"{API_BASE}/login",
                     data={"admin_key": "Ww010101"},
                     timeout=10)
    if resp.status_code == 200:
        # 登录成功，获取 cookie
        print(f"✅ 登录成功")
        cookies = resp.cookies
    else:
        print(f"❌ 登录失败: {resp.status_code}")
        exit(1)
except Exception as e:
    print(f"❌ 登录异常: {e}")
    exit(1)

# 2. 检查代理配置
print("\n[2/3] 检查代理配置...")
try:
    resp = httpx.get(f"{API_BASE}/admin/proxy-control", cookies=cookies, timeout=5)
    if resp.status_code == 200:
        cfg = resp.json()
        print(f"✓ 代理总开关: {cfg.get('master_enabled')}")
        print(f"✓ Auth代理: {cfg.get('auth_enabled')}")
        print(f"✓ 端口: {cfg.get('port')}")
except Exception as e:
    print(f"⚠️ 获取配置失败: {e}")

# 3. 启动注册任务
print("\n[3/3] 启动注册任务...")
try:
    resp = httpx.post(f"{API_BASE}/admin/register/start",
                     cookies=cookies,
                     json={"count": 1},
                     timeout=10)
    if resp.status_code == 200:
        task = resp.json()
        print(f"✅ 任务已创建: {task.get('id')}")
        print("\n请查看服务日志，确认是否显示:")
        print("  - 🔄 使用节点: [节点名称]")
        print("  - 📍 代理地址: http://127.0.0.1:7890")
        print("  - ✅ 代理连接成功")
        print("  - ✅ 当前代理 IP: [IP地址]")
    else:
        print(f"❌ 创建任务失败: {resp.status_code}")
except Exception as e:
    print(f"❌ 请求异常: {e}")

print("\n" + "=" * 60)
