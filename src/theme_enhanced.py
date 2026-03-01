"""
star-office-ui 增强模块
功能: 暗色模式+响应式设计+主题定制
来源: UI/UX最佳实践
"""

import json
from typing import Dict, List, Optional

class ThemeManager:
    """主题管理器"""
    
    THEMES = {
        "light": {
            "name": "浅色模式",
            "colors": {
                "primary": "#2563eb",
                "background": "#ffffff",
                "text": "#1f2937",
                "border": "#e5e7eb",
                "accent": "#3b82f6"
            }
        },
        "dark": {
            "name": "暗色模式",
            "colors": {
                "primary": "#60a5fa",
                "background": "#111827",
                "text": "#f9fafb",
                "border": "#374151",
                "accent": "#93c5fd"
            }
        },
        "blue": {
            "name": "海洋蓝",
            "colors": {
                "primary": "#0ea5e9",
                "background": "#f0f9ff",
                "text": "#0c4a6e",
                "border": "#bae6fd",
                "accent": "#38bdf8"
            }
        },
        "green": {
            "name": "森林绿",
            "colors": {
                "primary": "#22c55e",
                "background": "#f0fdf4",
                "text": "#14532d",
                "border": "#bbf7d0",
                "accent": "#4ade80"
            }
        }
    }
    
    def __init__(self):
        self.current_theme = "light"
        
    def set_theme(self, theme_name: str) -> bool:
        """设置主题"""
        if theme_name in self.THEMES:
            self.current_theme = theme_name
            return True
        return False
    
    def get_theme(self) -> Dict:
        """获取当前主题"""
        return self.THEMES.get(self.current_theme, self.THEMES["light"])
    
    def get_css_variables(self) -> str:
        """获取CSS变量"""
        theme = self.get_theme()
        css = ":root {\n"
        for key, value in theme["colors"].items():
            css += f"  --color-{key}: {value};\n"
        css += "}\n"
        return css

class ResponsiveLayout:
    """响应式布局"""
    
    BREAKPOINTS = {
        "mobile": 640,
        "tablet": 768,
        "desktop": 1024,
        "wide": 1280
    }
    
    @staticmethod
    def get_responsive_classes() -> Dict[str, str]:
        """获取响应式类名"""
        return {
            "hidden-mobile": "hidden md:block",
            "hidden-desktop": "block md:hidden",
            "grid-cols-1": "grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4",
            "text-sm": "text-sm md:text-base lg:text-lg"
        }

class AIHelper:
    """AI辅助操作"""
    
    SUGGESTIONS = {
        "input_focus": ["尝试搜索", "热门话题", "最新知识胶囊"],
        "button_hover": ["点击查看详情", "了解更多", "开始使用"],
        "empty_state": ["创建第一个胶囊", "浏览知识库", "参与讨论"]
    }
    
    @staticmethod
    def get_suggestions(context: str) -> List[str]:
        """获取AI建议"""
        return AIHelper.SUGGESTIONS.get(context, [])

# 测试
if __name__ == "__main__":
    manager = ThemeManager()
    
    # 切换主题
    manager.set_theme("dark")
    print("当前主题:", manager.get_theme()["name"])
    print("\nCSS变量:\n", manager.get_css_variables())
    
    # 响应式
    print("\n响应式类:", ResponsiveLayout.get_responsive_classes())
    
    # AI建议
    print("\nAI建议:", AIHelper.get_suggestions("input_focus"))
