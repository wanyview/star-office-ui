#!/usr/bin/env python3
"""Star Office UI 状态更新工具"""

import requests
import json
import sys
import os

STATE_FILE = "/Users/wanyview/clawd/star-office-ui/state.json"
API_URL = "http://127.0.0.1:18791"

def get_status():
    """获取当前状态"""
    resp = requests.get(f"{API_URL}/status")
    return resp.json()

def set_state(state, detail="", progress=0):
    """设置状态"""
    data = {
        "state": state,
        "detail": detail,
        "progress": progress
    }
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ 状态已更新: {state} - {detail}")

def main():
    if len(sys.argv) < 2:
        # 显示当前状态
        status = get_status()
        print(f"当前状态: {status.get('state', 'unknown')}")
        print(f"详情: {status.get('detail', '')}")
        print(f"进度: {status.get('progress', 0)}%")
        return
    
    state = sys.argv[1]
    detail = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else ""
    
    # 状态映射
    state_map = {
        "idle": "idle",
        "working": "working",
        "writing": "writing",
        "researching": "researching",
        "executing": "executing",
        "syncing": "syncing",
        "error": "error",
        "break": "break"
    }
    
    if state in state_map:
        set_state(state_map[state], detail)
    else:
        print(f"未知状态: {state}")
        print("可用状态: idle, working, writing, researching, executing, syncing, error, break")

if __name__ == "__main__":
    main()
