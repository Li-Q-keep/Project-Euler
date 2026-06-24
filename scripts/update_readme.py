#!/usr/bin/env python3
"""
自动更新 README.md 脚本
扫描 solutions/ 和 notes/ 目录，生成进度统计和题目索引
"""

import os
from urllib.parse import quote
import re
from pathlib import Path
from datetime import datetime, timezone

# ============ 配置 ============
SOLUTIONS_DIR = Path("solutions")
NOTES_DIR = Path("notes")
README_PATH = Path("README.md")

BATCH_SIZE = 100
MAX_PROBLEM = 997

STATUS_DONE = "✅"
STATUS_TODO = "❌"
STATUS_FEATURED = "⭐"




def md_link(text: str, path: str) -> str:
    """生成 Markdown 链接，自动编码路径中的特殊字符"""
    encoded = quote(path, safe='/:#?=&')
    return f"[{text}]({encoded})"

def get_problem_number(filename: str) -> int | None:
    """从文件名提取题号"""
    match = re.match(r'p(\d+)(?:[_-].*)?\.(py|md)', filename, re.IGNORECASE)
    if match:
        return int(match.group(1))
    return None


def get_solution_title(filepath: Path) -> str:
    """从 solutions/p00x.py 提取题目标题"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        in_docstring = False
        for line in lines:
            stripped = line.strip()
            
            if stripped.startswith("'''") or stripped.startswith('"""'):
                if not in_docstring:
                    in_docstring = True
                    quote = stripped[:3]
                    content = stripped[3:]
                    if content.endswith(quote):
                        content = content[:-3].strip()
                    if content:
                        return content.strip("'\"")
                else:
                    break
            elif in_docstring:
                if stripped:
                    return stripped
    
    except Exception as e:
        print(f"Warning: 无法读取 {filepath}: {e}")
    
    return "Unknown"


def get_note_title(filepath: Path) -> str:
    """从 notes/p00x-xxx.md 提取标题，去掉 [P9] 前缀"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        for line in lines:
            stripped = line.strip()
            if stripped.startswith('# '):
                title = stripped[2:].strip()
                title = re.sub(r'^\[P\d+\]\s*', '', title)
                return title
            elif stripped.startswith('## '):
                title = stripped[3:].strip()
                title = re.sub(r'^\[P\d+\]\s*', '', title)
                return title
    
    except Exception as e:
        print(f"Warning: 无法读取 {filepath}: {e}")
    
    return "Unknown"


def scan_solutions() -> dict[int, dict]:
    """扫描 solutions/ 目录"""
    problems = {}
    
    if not SOLUTIONS_DIR.exists():
        print(f"Warning: {SOLUTIONS_DIR} 不存在")
        return problems
    
    for filepath in sorted(SOLUTIONS_DIR.iterdir()):
        if filepath.suffix != '.py' or filepath.is_dir():
            continue
        
        num = get_problem_number(filepath.name)
        if num is None:
            continue
        
        if num in problems:
            problems[num]['solution_files'].append(filepath.name)
            continue
        
        title = get_solution_title(filepath)
        problems[num] = {
            'number': num,
            'title': title,
            'solution_files': [filepath.name],
            'has_note': False,
            'note_title': None,
            'note_file': None,
        }
    
    return problems


def scan_notes(problems: dict[int, dict]) -> None:
    """扫描 notes/ 目录，匹配题号"""
    if not NOTES_DIR.exists():
        print(f"Warning: {NOTES_DIR} 不存在")
        return
    
    for filepath in sorted(NOTES_DIR.iterdir()):
        if filepath.suffix != '.md':
            continue
        
        num = get_problem_number(filepath.name)
        if num is None:
            continue
        
        if num not in problems:
            continue
        
        problems[num]['has_note'] = True
        problems[num]['note_file'] = filepath.name
        problems[num]['note_title'] = get_note_title(filepath)


def generate_progress_bar(current: int, total: int, width: int = 20) -> str:
    """生成 ASCII 进度条"""
    if total == 0:
        return "`░░░░░░░░░░░░░░░░░░░░` 0%"
    filled = int(width * current / total)
    bar = "█" * filled + "░" * (width - filled)
    percent = current / total * 100
    return f"`{bar}` {percent:.1f}%"


def generate_progress_section(problems: dict[int, dict]) -> str:
    """生成总进度统计"""
    total_solved = len(problems)
    total_with_notes = sum(1 for p in problems.values() if p['has_note'])
    
    lines = [
        f"### 总体进度",
        f"",
        f"- **已解题**: {total_solved} / {MAX_PROBLEM} {generate_progress_bar(total_solved, MAX_PROBLEM)}",
        # f"- **附题解**: {total_with_notes} / {total_solved} {generate_progress_bar(total_with_notes, total_solved) if total_solved > 0 else generate_progress_bar(0, 1)}",
        f"",
        "### 区间概览",
        "",
        "| 区间 | 完成 | 进度 | 状态 |",
        "|------|------|------|------|",
    ]
    
    for start in range(1, MAX_PROBLEM + 1, BATCH_SIZE):
        end = min(start + BATCH_SIZE - 1, MAX_PROBLEM)
        solved = sum(1 for n in range(start, end + 1) if n in problems)
        
        if solved == BATCH_SIZE:
            status = "🟢 已完成"
        elif solved >= BATCH_SIZE * 0.6:
            status = "🟡 推进中"
        elif solved > 0:
            status = "🔴 缓慢"
        else:
            status = "⚪ 未开始"
        
        progress_bar = generate_progress_bar(solved, BATCH_SIZE)
        anchor = f"#{start:03d}-{end:03d}"
        lines.append(f"| [{start:03d}-{end:03d}]({anchor}) | {solved}/{BATCH_SIZE} | {progress_bar} | {status} |")
    
    return "\n".join(lines)


def generate_featured_section(problems: dict[int, dict]) -> str:
    """生成重点题解表格（有 notes/ 的题目）"""
    featured = {n: p for n, p in problems.items() if p['has_note']}
    
    if not featured:
        return "_暂无重点题解，在 notes/ 目录添加 Markdown 文件即可自动收录。_"
    
    lines = [
        "| 题号 | 标题 | 代码 | 题解 |",
        "|------|------|------|------|",
    ]
    
    for num in sorted(featured.keys()):
        p = featured[num]
        main_file = p['solution_files'][0] if p['solution_files'] else f'p{num:03d}.py'
        code_link = md_link(main_file, f"solutions/{main_file}")
        note_link = md_link('📖 原理详解', f"notes/{p['note_file']}")
        display_title = p['note_title'] or p['title']
        lines.append(f"| {STATUS_FEATURED} **{num:03d}** | {display_title} | {code_link} | {note_link} |")
    
    return "\n".join(lines)


def generate_index_section(problems: dict[int, dict]) -> str:
    """生成按区间折叠的题目索引"""
    lines = []
    
    for start in range(1, MAX_PROBLEM + 1, BATCH_SIZE):
        end = min(start + BATCH_SIZE - 1, MAX_PROBLEM)
        solved = sum(1 for n in range(start, end + 1) if n in problems)
        
        open_attr = " open" if start == 1 else ""
        anchor = f"{start:03d}-{end:03d}"
        
        lines.append(f'<details{open_attr}>')
        lines.append(f'<summary><b>{start:03d}-{end:03d}</b> — {solved}/{BATCH_SIZE} {generate_progress_bar(solved, BATCH_SIZE)}</summary>')
        lines.append("")
        lines.append("| 题号 | 标题 | 状态 | 代码 |")
        lines.append("|------|------|------|------|")
        
        for num in range(start, end + 1):
            if num in problems:
                p = problems[num]
                status = STATUS_DONE
                main_file = p['solution_files'][0] if p['solution_files'] else f'p{num:03d}.py'
                code_link = md_link('代码', f"solutions/{main_file}")
                # note_link = md_link('📖', f"notes/{p['note_file']}") + ' ⭐' if p['has_note'] else '—'
                title = p['title']
            else:
                status = STATUS_TODO
                code_link = '—'
                # note_link = '—'
                title = '—'
            
            lines.append(f"| {num:03d} | {title} | {status} | {code_link} |")
        
        lines.append("")
        lines.append("</details>")
        lines.append("")
    
    return "\n".join(lines)


def replace_chunk(content: str, marker: str, chunk: str) -> str:
    """替换 README 中标记区块的内容"""
    pattern = re.compile(
        rf'<!-- {marker} starts -->.*?<!-- {marker} ends -->',
        re.DOTALL
    )
    replacement = f"<!-- {marker} starts -->\n{chunk}\n<!-- {marker} ends -->"
    return pattern.sub(replacement, content)


def main():
    print("🔍 扫描 solutions/ 和 notes/ 目录...")
    
    problems = scan_solutions()
    scan_notes(problems)
    
    print(f"📊 发现 {len(problems)} 道已解题，{sum(1 for p in problems.values() if p['has_note'])} 道附详细题解")
    
    progress = generate_progress_section(problems)
    featured = generate_featured_section(problems)
    index = generate_index_section(problems)
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    
    if README_PATH.exists():
        with open(README_PATH, 'r', encoding='utf-8') as f:
            content = f.read()
    else:
        content = ""
        print("Warning: README.md 不存在，将创建新文件")
    
    content = replace_chunk(content, "progress", progress)
    content = replace_chunk(content, "featured", featured)
    content = replace_chunk(content, "index", index)
    content = content.replace("<!-- timestamp -->", timestamp)
    
    with open(README_PATH, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✅ README.md 已更新 ({timestamp})")


if __name__ == '__main__':
    main()