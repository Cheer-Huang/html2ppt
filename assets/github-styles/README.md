# GitHub 高质量网站/幻灯片风格模板收集

> 以下模板均来自 GitHub 开源项目，采用 MIT 许可证，允许商用和二次开发。
> 使用时请在最终产物中保留原始版权声明。

## 幻灯片模板

### 1. beautiful-html-templates

| 项目 | 信息 |
|------|------|
| 仓库 | https://github.com/zarazhangrui/beautiful-html-templates |
| 许可证 | MIT |
| Stars | 3.1k+ |
| 模板数 | 34 套 |
| 特点 | 专为 AI Agent 设计，每套模板独立可用，风格多样 |

**风格预览：**
- 极简白底、编辑风衬线、柔和粉彩、等宽字体
- 北欧冷色、日落暖色、Catppuccin、Dracula、Tokyo Night
- 新粗野主义、玻璃拟态、包豪斯、瑞士网格
- 赛博朋克霓虹、蒸汽波、复古电视、日式极简
- 企业商务、学术论文、新闻播报、VC 路演

**使用方式：**
```bash
git clone https://github.com/zarazhangrui/beautiful-html-templates.git
# 浏览 templates/ 目录，选择合适风格
# 将模板 HTML 结构融入你的幻灯片
```

### 2. html-ppt-skill (HTML PPT Studio)

| 项目 | 信息 |
|------|------|
| 仓库 | https://github.com/lewislulu/html-ppt-skill |
| 许可证 | MIT |
| Stars | 6.4k+ |
| 主题数 | 36 主题 |
| 布局数 | 31 种页面布局 |
| 动画数 | 47 种（27 CSS + 20 Canvas FX） |
| 特点 | 含演示者模式、演讲稿、计时器，功能最全 |

**使用方式：**
```bash
git clone https://github.com/lewislulu/html-ppt-skill.git
# 参考 themes/ 目录中的主题样式
# 参考 layouts/ 目录中的页面布局
```

### 3. frontend-slides

| 项目 | 信息 |
|------|------|
| 仓库 | https://github.com/zarazhangrui/frontend-slides |
| 许可证 | MIT |
| 版本 | v2.1.0 |
| 特点 | 零依赖单 HTML 文件，反 AI 通用美学，支持 PPT→网页转换 |

**使用方式：**
```bash
git clone https://github.com/zarazhangrui/frontend-slides.git
# 参考 SKILL.md 中的设计理念
# 使用其 34 种大胆设计模板
```

## 配色/渐变资源

### 4. WebGradients

| 项目 | 信息 |
|------|------|
| 网站 | https://webgradients.com |
| 许可证 | MIT |
| 渐变数 | 180 种 |
| 特点 | 一键复制 CSS，含 .sketch/.PSD 文件 |

### 5. uiGradients

| 项目 | 信息 |
|------|------|
| 网站 | https://uigradients.com |
| 特点 | 手选渐变色集合，适合做幻灯片背景 |

### 6. Grabient

| 项目 | 信息 |
|------|------|
| 网站 | https://grabient.com |
| 特点 | 可视化渐变编辑器，导出 CSS/SVG |

## UI 组件资源

### 7. Uiverse

| 项目 | 信息 |
|------|------|
| 网站 | https://uiverse.io |
| 特点 | 最大开源 UI 组件库，复制 HTML/CSS/Tailwind/React |

## 如何在 html2ppt 中使用这些模板

1. **选择风格**：浏览上述模板库，找到适合你场景的视觉风格
2. **提取 CSS**：将模板中的配色、字体、布局样式提取到你的 HTML `<style>` 块中
3. **适配 slide 结构**：将样式适配到 `<section class="slide">` 结构中
4. **保持内联**：所有样式内联在 HTML 中，不依赖外部文件（截图需要）
5. **保留版权**：在 HTML 注释中保留模板来源和许可证声明

```html
<!-- 
  风格来源: beautiful-html-templates (MIT License)
  https://github.com/zarazhangrui/beautiful-html-templates
-->
<style>
/* 从模板提取的样式 */
.slide { ... }
</style>
```

## 贡献新模板

欢迎通过 PR 贡献新的高质量模板。要求：
1. 必须有明确的开源许可证（MIT / Apache 2.0 / BSD 等）
2. 在本索引中标注许可证和来源链接
3. 提供截图预览或在线 Demo 链接
