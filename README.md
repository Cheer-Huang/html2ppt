# html2ppt

> AI 生成 HTML 幻灯片，截图转为高保真 PowerPoint (.pptx)

## 使用场景

你遇到过这些情况吗？

- **老师/会议要求提交 .pptx 文件**，但你用 AI 生成 PPT 时，直接用 python-pptx 写代码排版能力有限——字体、渐变、布局很难精确控制
- **AI 直接生成 PPT 效果不理想**：默认蓝色标题、丑陋的列表样式、表格没有设计感，和你在网页上看到的精美幻灯片差距很大
- **用 AI 写 HTML/CSS 做幻灯片效果很好**，但 HTML 没法直接当 PPT 提交，手动截图再粘贴到 PPT 里太繁琐
- **答辩/汇报场景需要 .pptx 文件**，但又想保持网页级的设计质量

## 解决方案

**html2ppt** 的思路：让 AI 发挥 HTML/CSS 的排版能力生成幻灯片页面，再用 Chrome headless 截图后组装为 PPTX。100% 还原 HTML 渲染效果，所见即所得。

```
AI 生成 HTML 幻灯片（可反复迭代，浏览器预览效果）
        ↓
Chrome headless 逐页截图为 PNG
        ↓
python-pptx 组装为 .pptx 文件
```

**第一步是 AI 的创意工作**——可以反复修改 HTML 直到浏览器中预览满意为止。
**后两步是确定性脚本**——一键运行，不依赖 AI，结果稳定可靠。

## 与其他方案的对比

| 方案 | 排版能力 | 输出格式 | 可迭代 | 保真度 |
|------|---------|---------|--------|--------|
| python-pptx 直接生成 | 弱（代码控制布局） | .pptx | 差 | 低 |
| AI 生成 HTML 浏览器演示 | 强（CSS/HTML） | .html | 好 | — |
| html-ppt-skill 等纯 HTML 方案 | 强（CSS/动画） | .html | 好 | — |
| **html2ppt（本工具）** | **强（CSS/HTML）** | **.pptx** | **好** | **100%** |

> 如果你不需要提交 .pptx 文件，纯 HTML 方案（如 [html-ppt-skill](https://github.com/lewislulu/html-ppt-skill)）已经够用。当你**必须交 .pptx** 时，html2ppt 是最佳选择。

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

### 高质量风格模板

不想从零写 CSS？[assets/github-styles/](assets/github-styles/) 收集了 GitHub 上高质量开源幻灯片模板（均 MIT 许可），涵盖极简、赛博朋克、学术论文、玻璃拟态等 36+ 种风格，可直接提取样式使用。

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
