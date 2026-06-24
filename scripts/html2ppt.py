#!/usr/bin/env python3
"""
HTML 转 PPT 一键脚本
将 HTML 文件截图后组装为 PowerPoint 演示文稿。

用法:
    python html2ppt.py <input.html> [output.pptx] [--width 1280] [--height 720]

流程:
    1. 解析 HTML 中的 slide 分页
    2. Chrome headless 逐页截图为 PNG
    3. python-pptx 组装为 PPTX

依赖:
    - Google Chrome / Chromium
    - python-pptx (pip install python-pptx)
"""

import sys
import os
import argparse
import tempfile

# 导入同目录下的模块
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from html2img import html_to_images
from img2ppt import images_to_pptx


def html_to_pptx(html_path, output_pptx=None, width=1280, height=720):
    """
    一键将 HTML 转为 PPTX。
    
    参数:
        html_path: HTML 文件路径
        output_pptx: 输出 PPTX 路径（默认为同名 .pptx）
        width: 截图宽度像素
        height: 截图高度像素
    """
    html_path = os.path.abspath(html_path)
    
    if output_pptx is None:
        base = os.path.splitext(html_path)[0]
        output_pptx = base + ".pptx"
    
    print("=" * 60)
    print("HTML → PPT 一键转换")
    print("=" * 60)
    print(f"输入: {html_path}")
    print(f"输出: {output_pptx}")
    print(f"尺寸: {width}x{height}px")
    print()
    
    # Step 1: HTML → PNG
    print("-" * 40)
    print("Step 1: HTML → PNG 截图")
    print("-" * 40)
    
    with tempfile.TemporaryDirectory() as tmp_dir:
        png_files = html_to_images(html_path, tmp_dir, width, height)
        
        if not png_files:
            print("错误: 截图失败，未生成任何图片", file=sys.stderr)
            sys.exit(1)
        
        # Step 2: PNG → PPTX
        print()
        print("-" * 40)
        print("Step 2: PNG → PPTX 组装")
        print("-" * 40)
        
        images_to_pptx(png_files, output_pptx, width, height)
    
    print()
    print("=" * 60)
    print(f"全部完成！")
    print(f"PPTX 文件: {output_pptx}")
    print(f"文件大小: {os.path.getsize(output_pptx) / 1024 / 1024:.1f} MB")
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="HTML 转 PPT 一键脚本",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
    python html2ppt.py slides.html
    python html2ppt.py slides.html output.pptx
    python html2ppt.py slides.html output.pptx --width 1920 --height 1080
        """,
    )
    parser.add_argument("input", help="HTML 文件路径")
    parser.add_argument("output", nargs="?", help="输出 PPTX 路径（默认同名.pptx）")
    parser.add_argument("--width", type=int, default=1280, help="截图宽度像素（默认1280）")
    parser.add_argument("--height", type=int, default=720, help="截图高度像素（默认720）")
    
    args = parser.parse_args()
    html_to_pptx(args.input, args.output, args.width, args.height)


if __name__ == "__main__":
    main()
