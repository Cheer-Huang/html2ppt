# html2ppt

> AI 生成 HTML 幻灯片，一键转为高保真 PowerPoint

## 为什么需要这个工具

用 AI 生成 PPT 时，直接用 python-pptx 写代码生成幻灯片，排版能力有限——字体、渐变、布局很难精确控制。

**html2ppt** 换了个思路：让 AI 发挥 HTML/CSS 的排版能力生成幻灯片页面，再用 Chrome headless 截图后组装为 PPT。100% 还原 HTML 渲染效果，所见即所得。

## 工作流程

```
1. AI 生成 HTML（可反复迭代，浏览器预览）
2. Chrome headless 逐页截图为 PNG
3. python-pptx 组装为 PPTX
```

步骤 1 是 AI 的创意工作，步骤 2-3 是确定性脚本。

## 两种使用方式

### 方式一：作为 AI Agent Skill（推荐）

本项目是一个标准 Skill 包，可安装到各类 AI 编程助手中。安装后，直接对 Agent 说"帮我做一个答辩PPT"即可自动触发完整流程。

#### 安装指南

**CodeBuddy：**

```bash
git clone https://github.com/Cheer-Huang/html2ppt.git ~/.codebuddy/skills/html2ppt
```

**Claude Code：**

```bash
git clone https://github.com/Cheer-Huang/html2ppt.git ~/.claude/skills/html2ppt
```

在项目根目录的 `CLAUDE.md` 中添加引用：
```markdown
## Skills
- HTML转PPT: ~/.claude/skills/html2ppt/SKILL.md
```

**Trae / 其他 Agent：**

```bash
git clone https://github.com/Cheer-Huang/html2ppt.git ~/skills/html2ppt
```

在 Agent 配置中添加：
```
当用户提到"PPT"、"slides"、"演示文稿"、"答辩"等关键词时，
参考 ~/skills/html2ppt/SKILL.md 中的指引完成 HTML 生成和 PPT 转换。
```

### 方式二：命令行工具

```bash
pip install python-pptx
python scripts/html2ppt.py slides.html output.pptx
```

## 快速开始

### 安装依赖

```bash
pip install python-pptx
```

需要系统已安装 Google Chrome 或 Chromium。

### 一键转换

```bash
python scripts/html2ppt.py slides.html output.pptx
```

### 分步执行

```bash
# Step 1: HTML → PNG 截图
python scripts/html2img.py slides.html slides/

# Step 2: PNG → PPTX 组装
python scripts/img2ppt.py slides/ output.pptx
```

### 高清模式

```bash
python scripts/html2ppt.py slides.html output.pptx --width 1920 --height 1080
```

## HTML 幻灯片模板

每页用 `<section class="slide">` 包裹，固定 1280x720px：

```html
<section class="slide">
  <h1>页面标题</h1>
  <ul>
    <li>要点一</li>
    <li>要点二</li>
  </ul>
</section>
```

完整模板见 [references/html_slide_template.md](references/html_slide_template.md)，包含标题页、内容页、两栏页、表格页、代码页等样式。

## 功能一览

| 功能 | 说明 |
|------|------|
| HTML 分页解析 | 自动识别 `<section class="slide">` 分页 |
| Chrome headless 截图 | 逐页截图，支持自定义分辨率 |
| PPTX 组装 | 图片填满幻灯片，保持原始比例 |
| 一键转换 | `html2ppt.py` 一步到位 |
| 高清支持 | 支持 1920x1080 输出 |
| 模板参考 | 提供完整 HTML/CSS 模板 |

## 推荐工作流

```
1. AI 生成 HTML 幻灯片（可反复修改，浏览器预览效果）
2. 确认 HTML 效果满意
3. 运行 html2ppt.py 一键转换
4. 在 PowerPoint 中打开检查
```

> **重要**：HTML 生成是可迭代的——先在浏览器中预览调整到满意，再运行转换脚本。截图会 100% 还原浏览器渲染效果。

## 输出说明

- PPTX 中的每页是全幅图片（非可编辑文本/形状）
- 优点：100% 还原 HTML 设计，不会出现排版错乱
- 缺点：图片不可编辑，文件体积较大
- 适合场景：答辩、演示、汇报（这些场景不需要编辑 PPT 内容）

## 技术细节

| 组件 | 技术 |
|------|------|
| HTML 解析 | Python 正则，提取 `<section class="slide">` |
| 截图 | Chrome headless `--screenshot` |
| PPTX 生成 | python-pptx，空白布局 + 全幅图片 |
| 分辨率 | 默认 1280x720 (16:9)，可选 1920x1080 |

## 与 thesis-format-cn 的配合

```
AI 生成 HTML 报告
    ↓
thesis-format-cn → 格式化 DOCX（提交版报告）
    ↓
html2ppt → 截图转 PPT（答辩演示）
```

## 免责声明

本项目为独立开源工具。Chrome 和 PowerPoint 是各自公司的产品，本项目不与之关联。

## License

MIT License - 详见 [LICENSE](LICENSE)
