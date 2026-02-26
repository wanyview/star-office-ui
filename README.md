# Star Office UI

> 为 AI 助手创建的"像素办公室"可视化界面 🏢

## 效果预览

- 俯视像素办公室背景
- 像素小人代表助手：根据 `state` 在不同区域移动
- 眨眼/气泡/打字机等动态效果
- 手机可通过 Cloudflare Tunnel 公网访问

## 快速开始

### 1. 安装依赖

```bash
cd star-office-ui/backend
pip install flask
```

### 2. 启动后端

```bash
python app.py
```

服务将在 http://0.0.0.0:18791 启动

### 3. 公网访问（可选）

```bash
# 下载 cloudflared
brew install cloudflared

# 启动 quick tunnel
cloudflared tunnel --url http://127.0.0.1:18791
```

## 状态更新

```bash
# 更新状态
python set_state.py writing "正在写报告"

# 可用状态
idle, writing, researching, executing, syncing, error
```

## 状态说明

| 状态 | 区域 | 说明 |
|------|------|------|
| idle | 休息区 | 等待任务 |
| writing | 办公桌 | 写作中 |
| researching | 办公桌 | 研究中 |
| executing | 办公桌 | 执行中 |
| syncing | 休息区 | 同步中 |
| error | 休息区 | 出错 |

## API

- `GET /` - 前端页面
- `GET /status` - 获取当前状态
- `GET /health` - 健康检查
