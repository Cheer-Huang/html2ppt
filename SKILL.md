---
name: html2ppt
description: "Generate PowerPoint presentations from HTML. AI generates HTML slides (iterative), then scripts convert HTML to PNG screenshots via Chrome headless, and assemble PNGs into a PPTX file via python-pptx. This skill should be used when users need to create presentations, slides, decks, or PPT files, especially from AI-generated HTML content. Triggers include mentions of PPT, slides, presentation, 演示文稿, 答辩, 幻灯片, html2ppt, or requests to create visual presentations."
---

# HTML to PPT Skill

## Purpose

Generate high-fidelity PowerPoint presentations from HTML content. The workflow
leverages AI's strength in writing HTML/CSS, then uses deterministic scripts for
screenshot capture and PPTX assembly.

## When to Use

- Creating presentation slides from scratch
- Converting HTML content to a PPTX file
- Generating defense/pitch slides
- Any request involving "PPT", "slides", "presentation", "答辩", "演示文稿"

## Prerequisites

- Google Chrome or Chromium installed
- Python 3.8+ with `python-pptx` (`pip install python-pptx`)

## Workflow

### Step 1: Generate HTML Slides (AI Creative Work)

Generate an HTML file where each slide is wrapped in `<section class="slide">`.
Refer to `references/html_slide_template.md` for the template structure and CSS.

Key rules for the HTML:
1. Each slide must be a `<section class="slide">` element
2. Fixed size: `1280x720px` (16:9) per slide
3. Use inline `<style>` block, not external CSS files
4. Images must use absolute `file://` paths
5. Use system fonts (PingFang SC, Microsoft YaHei, SimHei)
6. No CSS animations or JS interactions (screenshots are static)
7. Set `overflow: hidden` on each slide

This step is **iterative** — generate, preview in browser, refine, repeat until
satisfied with the visual result.

### Step 2: HTML to PNG Screenshots

Once the HTML is finalized, convert each slide to a PNG screenshot:

```bash
python scripts/html2img.py <input.html> [output_dir] [width] [height]
```

Default size is 1280x720. For higher quality, use 1920x1080.

The script:
1. Parses `<section class="slide">` elements
2. Creates a temporary HTML file for each slide
3. Uses Chrome headless to screenshot each one
4. Outputs `slide_000.png`, `slide_001.png`, etc.

### Step 3: PNG to PPTX Assembly

Assemble the screenshots into a PowerPoint file:

```bash
python scripts/img2ppt.py <image_dir_or_files> [output.pptx] [--width 1280] [--height 720]
```

The script:
1. Collects PNG files sorted by filename
2. Creates a PPTX with matching slide dimensions
3. Inserts each image as a full-slide picture

### One-Step Shortcut

Run all steps at once:

```bash
python scripts/html2ppt.py <input.html> [output.pptx] [--width 1280] [--height 720]
```

## Critical Workflow Rule

HTML generation (Step 1) is iterative and should be fully completed before
running the conversion scripts. Do NOT run html2ppt until the user confirms the
HTML slides look correct in a browser preview. The screenshots will capture
exactly what the browser renders — any visual issues in HTML will appear in the
PPT.

## Output Notes

- The PPTX contains full-slide images (not editable text/shapes)
- File size depends on image count and resolution
- For editable PPTX, consider using python-pptx directly (not covered by this skill)
- The image-based approach guarantees 100% visual fidelity to the HTML design

## Script API

All scripts can be imported and called programmatically:

```python
from html2img import html_to_images
from img2ppt import images_to_pptx
from html2ppt import html_to_pptx

# One-step
html_to_pptx("slides.html", "output.pptx", width=1280, height=720)

# Or step by step
pngs = html_to_images("slides.html", "slides/", 1280, 720)
images_to_pptx(pngs, "output.pptx", 1280, 720)
```
