#!/usr/bin/env python3
"""
HTML 转 PNG 截图脚本
使用 Chrome headless 对 HTML 文件中的每个 slide section 截图。

支持两种 HTML 结构：
1. 每个 <section class="slide"> 或 <div class="slide"> 为一页
2. 用 <hr class="page-break"> 分隔的页面

用法:
    python html2img.py <input.html> [output_dir]

如不指定 output_dir，则在 input.html 同目录下创建 slides/ 目录。
"""

import sys
import os
import re
import subprocess
import tempfile
import shutil
from pathlib import Path


def find_chrome():
    """查找 Chrome/Chromium 可执行文件"""
    candidates = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        "/usr/bin/google-chrome",
        "/usr/bin/chromium-browser",
        "/usr/bin/chromium",
        "/usr/local/bin/google-chrome",
    ]
    for c in candidates:
        if os.path.exists(c):
            return c
    # 尝试 which
    for name in ["google-chrome", "chromium-browser", "chromium", "chrome"]:
        path = shutil.which(name)
        if path:
            return path
    return None


def extract_slides_from_html(html_path):
    """
    从 HTML 中提取 slide 信息。
    返回 [(slide_id_or_selector, slide_index), ...]
    
    策略：
    1. 如果有 .slide 类的元素，按其分页
    2. 如果有 hr.page-break，按其分页
    3. 否则整页截图
    """
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 检查是否有 .slide 类
    if re.search(r'class="[^"]*slide[^"]*"', content):
        return "slide_class"
    
    # 检查是否有 page-break
    if 'page-break' in content or 'page_break' in content:
        return "page_break"
    
    return "full_page"


def generate_screenshot_js(html_path, output_dir, slide_mode):
    """
    生成 JavaScript 文件，用 Chrome 的 Puppeteer-like 方式截图。
    但我们用纯 Chrome headless --screenshot 方式，更简单。
    """
    # 对于 .slide 类分页的情况，我们需要注入 JS 来逐个截图
    # Chrome headless 的 --screenshot 只能截整页
    # 所以我们用另一种方式：为每个 slide 创建一个临时 HTML
    
    slides_info = []
    
    if slide_mode == "slide_class":
        # 读取 HTML，按 .slide 分割
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 提取 head 部分
        head_match = re.search(r'<head>(.*?)</head>', content, re.DOTALL)
        head_content = head_match.group(1) if head_match else ""
        
        # 提取所有 .slide 元素
        slide_pattern = r'<(?:section|div)[^>]*class="[^"]*slide[^"]*"[^>]*>(.*?)</(?:section|div)>'
        slides = re.findall(slide_pattern, content, re.DOTALL)
        
        if not slides:
            # 尝试更宽松的匹配
            slide_pattern = r'<(?:section|div)[^>]*class="slide"[^>]*>(.*?)</(?:section|div)>'
            slides = re.findall(slide_pattern, content, re.DOTALL)
        
        if not slides:
            slide_mode = "full_page"
        else:
            for i, slide_content in enumerate(slides):
                tmp_html = os.path.join(output_dir, f"_slide_{i:03d}.html")
                with open(tmp_html, 'w', encoding='utf-8') as f:
                    f.write(f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
{head_content}
<style>
body {{ margin: 0; padding: 0; display: flex; justify-content: center; align-items: center; min-height: 100vh; }}
.slide {{ width: 1280px; height: 720px; overflow: hidden; }}
</style>
</head>
<body>
<div class="slide">
{slide_content}
</div>
</body>
</html>""")
                slides_info.append((tmp_html, f"slide_{i:03d}.png"))
    
    if slide_mode == "full_page":
        slides_info.append((html_path, "slide_000.png"))
    
    return slides_info


def screenshot_with_chrome(chrome_path, html_path, output_png, width=1280, height=720):
    """使用 Chrome headless 截图"""
    file_url = f"file://{os.path.abspath(html_path)}"
    cmd = [
        chrome_path,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        "--hide-scrollbars",
        f"--window-size={width},{height}",
        f"--screenshot={os.path.abspath(output_png)}",
        file_url,
    ]
    result = subprocess.run(cmd, capture_output=True, timeout=30)
    return result.returncode == 0


def html_to_images(html_path, output_dir=None, width=1280, height=720):
    """
    将 HTML 文件转为 PNG 图片序列。
    
    参数:
        html_path: HTML 文件路径
        output_dir: 输出目录（默认为 HTML 同目录下的 slides/）
        width: 截图宽度（默认 1280，对应 16:9）
        height: 截图高度（默认 720）
    
    返回:
        list of PNG 文件路径
    """
    html_path = os.path.abspath(html_path)
    
    if output_dir is None:
        output_dir = os.path.join(os.path.dirname(html_path), "slides")
    
    os.makedirs(output_dir, exist_ok=True)
    
    chrome_path = find_chrome()
    if not chrome_path:
        print("错误: 未找到 Chrome/Chromium，请安装 Google Chrome。", file=sys.stderr)
        sys.exit(1)
    
    print(f"Chrome 路径: {chrome_path}")
    print(f"HTML 文件: {html_path}")
    print(f"输出目录: {output_dir}")
    print(f"截图尺寸: {width}x{height}")
    
    # 检测 slide 模式
    slide_mode = extract_slides_from_html(html_path)
    print(f"检测到模式: {slide_mode}")
    
    # 生成截图任务
    slides_info = generate_screenshot_js(html_path, output_dir, slide_mode)
    
    print(f"\n共 {len(slides_info)} 页，开始截图...")
    
    png_files = []
    for i, (src_html, out_png) in enumerate(slides_info):
        out_path = os.path.join(output_dir, out_png)
        print(f"  [{i+1}/{len(slides_info)}] {out_png}...", end=" ", flush=True)
        
        if screenshot_with_chrome(chrome_path, src_html, out_path, width, height):
            print("✓")
            png_files.append(out_path)
        else:
            print("✗ 失败")
        
        # 清理临时 HTML
        if src_html != html_path and os.path.exists(src_html):
            os.remove(src_html)
    
    print(f"\n完成！共生成 {len(png_files)} 张图片:")
    for f in png_files:
        print(f"  {f}")
    
    return png_files


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python html2img.py <input.html> [output_dir] [width] [height]")
        print("示例: python html2img.py slides.html slides/ 1280 720")
        sys.exit(1)
    
    html_path = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None
    width = int(sys.argv[3]) if len(sys.argv) > 3 else 1280
    height = int(sys.argv[4]) if len(sys.argv) > 4 else 720
    
    html_to_images(html_path, output_dir, width, height)
