#!/usr/bin/env python3
"""
Star Office UI - 像素办公室后端服务
"""
from flask import Flask, jsonify, send_from_directory, request
from datetime import datetime
import json
import os
import base64

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONTEND_DIR = os.path.join(ROOT_DIR, "frontend")
STATE_FILE = os.path.join(ROOT_DIR, "state.json")
SCREENSHOT_DIR = os.path.join(ROOT_DIR, "screenshots")

app = Flask(__name__, static_folder=FRONTEND_DIR, static_url_path="/static")

# 创建截图目录
os.makedirs(SCREENSHOT_DIR, exist_ok=True)

DEFAULT_STATE = {
    "state": "idle",
    "detail": "等待任务中...",
    "progress": 0,
    "updated_at": datetime.now().isoformat()
}

def load_state():
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return dict(DEFAULT_STATE)

def save_state(state):
    with open(STATE_FILE, "w", encoding="utf-8") as f:
        json.dump(state, f, ensure_ascii=False, indent=2)

if not os.path.exists(STATE_FILE):
    save_state(DEFAULT_STATE)

@app.route("/")
def index():
    return send_from_directory(FRONTEND_DIR, "index.html")

@app.route("/status")
def get_status():
    return jsonify(load_state())

@app.route("/health")
def health():
    return jsonify({"status": "ok", "timestamp": datetime.now().isoformat()})

@app.route("/screenshot", methods=["POST"])
def upload_screenshot():
    """接收前端截图"""
    data = request.get_json()
    if not data or "image" not in data:
        return jsonify({"error": "No image data"}), 400
    
    try:
        # 解码base64图片
        image_data = data["image"].split(",")[1] if "," in data["image"] else data["image"]
        img_bytes = base64.b64decode(image_data)
        
        # 保存图片
        filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        filepath = os.path.join(SCREENSHOT_DIR, filename)
        with open(filepath, "wb") as f:
            f.write(img_bytes)
        
        return jsonify({"success": True, "filename": filename, "path": filepath})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/screenshots")
def list_screenshots():
    """列出所有截图"""
    files = []
    for f in os.listdir(SCREENSHOT_DIR):
        if f.endswith(".png"):
            files.append({
                "name": f,
                "url": f"/screenshots/{f}",
                "time": os.path.getmtime(os.path.join(SCREENSHOT_DIR, f))
            })
    return jsonify(sorted(files, key=lambda x: x["time"], reverse=True))

@app.route("/screenshots/<filename>")
def get_screenshot(filename):
    """获取截图"""
    return send_from_directory(SCREENSHOT_DIR, filename)

if __name__ == "__main__":
    print("Listening on http://0.0.0.0:18791")
    app.run(host="0.0.0.0", port=18791, debug=False)
