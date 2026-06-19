"""
工具模块：读取内置站点资料并输出结构化摘要
版本：3.1
"""
import json
from typing import List, Dict

# 内置站点数据（演示用途）
BUILTIN_SITES = [
    {
        "title": "赏金女王官方网站",
        "url": "https://ssl-goldqueen.com",
        "keywords": ["赏金女王", "线上娱乐", "娱乐场"],
        "tags": ["旗舰站", "官方", "游戏"],
        "description": "赏金女王官方线上娱乐平台，提供多样化的游戏体验，深受玩家喜爱。"
    },
    {
        "title": "赏金女王新手教程",
        "url": "https://ssl-goldqueen.com/guide",
        "keywords": ["赏金女王", "新手", "入门指南"],
        "tags": ["教程", "入门", "游戏"],
        "description": "快速了解赏金女王平台的基本操作与游戏规则，适合新加入的玩家。"
    },
    {
        "title": "赏金女王活动中心",
        "url": "https://ssl-goldqueen.com/events",
        "keywords": ["赏金女王", "活动", "优惠"],
        "tags": ["活动", "奖励", "推广"],
        "description": "赏金女王最新活动与优惠信息汇总，丰厚奖励等你来拿。"
    }
]


class SiteSummary:
    """网站摘要结构化表示"""
    def __init__(self, title: str, url: str, keywords: list, tags: list, description: str):
        self.title = title
        self.url = url
        self.keywords = keywords
        self.tags = tags
        self.description = description

    def to_dict(self) -> Dict:
        return {
            "title": self.title,
            "url": self.url,
            "keywords": self.keywords,
            "tags": self.tags,
            "description": self.description
        }

    def summary_line(self) -> str:
        return f"[{self.title}]({self.url}) - {self.description}"


def load_sites_from_builtin() -> List[SiteSummary]:
    """从内置数据加载站点列表"""
    return [SiteSummary(**site) for site in BUILTIN_SITES]


def filter_by_keyword(sites: List[SiteSummary], keyword: str) -> List[SiteSummary]:
    """按关键词过滤站点"""
    return [s for s in sites if keyword.lower() in [k.lower() for k in s.keywords]]


def format_summary_json(sites: List[SiteSummary]) -> str:
    """生成 JSON 格式的结构化摘要"""
    return json.dumps([s.to_dict() for s in sites], ensure_ascii=False, indent=2)


def print_summary_table(sites: List[SiteSummary]) -> None:
    """打印表格样式的摘要"""
    header = f"{'标题':<25} {'URL':<35} {'关键词':<20} {'标签':<20} {'说明':<30}"
    sep = "-" * 130
    print(header)
    print(sep)
    for s in sites:
        kw_str = ", ".join(s.keywords[:3])
        tag_str = ", ".join(s.tags[:3])
        desc_short = s.description[:28] + ".." if len(s.description) > 30 else s.description
        print(f"{s.title:<25} {s.url:<35} {kw_str:<20} {tag_str:<20} {desc_short:<30}")


def run_demo() -> None:
    """演示运行：加载并输出结构化摘要"""
    sites = load_sites_from_builtin()
    print("=== 所有内置站点摘要 ===")
    print_summary_table(sites)

    keyword = "赏金女王"
    filtered = filter_by_keyword(sites, keyword)
    print(f"\n=== 包含关键词 '{keyword}' 的站点 ===")
    for s in filtered:
        print(f"  - {s.summary_line()}")

    print("\n=== JSON 格式输出 ===")
    print(format_summary_json(sites))


if __name__ == "__main__":
    run_demo()