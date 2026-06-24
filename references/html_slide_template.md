# HTML 幻灯片模板规范

## 基本结构

每页幻灯片用 `<section class="slide">` 包裹，脚本会自动按此分页截图。

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<title>演示文稿标题</title>
<style>
/* 全局样式 */
body {
  margin: 0; padding: 0;
  font-family: "PingFang SC", "Microsoft YaHei", sans-serif;
  background: #fff;
}

/* 每页幻灯片：固定 1280x720 (16:9) */
.slide {
  width: 1280px;
  height: 720px;
  padding: 60px 80px;
  box-sizing: border-box;
  page-break-after: always;
  position: relative;
  overflow: hidden;
}

/* 标题页样式 */
.slide.title {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}

/* 内容页标题 */
.slide h1 {
  font-size: 36px;
  color: #1a1a1a;
  border-bottom: 3px solid #2d6cdf;
  padding-bottom: 12px;
  margin-bottom: 30px;
}

/* 正文 */
.slide p, .slide li {
  font-size: 22px;
  line-height: 1.8;
  color: #333;
}

/* 要点列表 */
.slide ul {
  padding-left: 40px;
}
.slide li {
  margin-bottom: 12px;
}

/* 两栏布局 */
.slide.two-col {
  display: flex;
  gap: 40px;
}
.slide.two-col > div {
  flex: 1;
}

/* 表格 */
.slide table {
  width: 100%;
  border-collapse: collapse;
  font-size: 20px;
}
.slide th, .slide td {
  padding: 10px 16px;
  text-align: left;
  border-bottom: 1px solid #ddd;
}
.slide th {
  background: #f5f7fa;
  font-weight: bold;
}

/* 代码块 */
.slide pre {
  background: #1e1e1e;
  color: #d4d4d4;
  padding: 20px;
  border-radius: 8px;
  font-size: 16px;
  line-height: 1.5;
  overflow-x: auto;
}

/* 页码 */
.slide .page-num {
  position: absolute;
  bottom: 20px;
  right: 40px;
  font-size: 14px;
  color: #999;
}

/* 强调色 */
.highlight { color: #2d6cdf; font-weight: bold; }
.success { color: #52c41a; font-weight: bold; }
.warning { color: #faad14; font-weight: bold; }
.danger { color: #ff4d4f; font-weight: bold; }
</style>
</head>
<body>

<!-- 标题页 -->
<section class="slide title">
  <h1 style="font-size:48px;border:none">演示文稿标题</h1>
  <p style="font-size:24px;color:#666">副标题 / 作者 / 日期</p>
</section>

<!-- 内容页 -->
<section class="slide">
  <h1>页面标题</h1>
  <ul>
    <li>要点一</li>
    <li>要点二</li>
    <li>要点三</li>
  </ul>
  <div class="page-num">2</div>
</section>

<!-- 两栏页 -->
<section class="slide two-col">
  <div>
    <h1>左侧标题</h1>
    <p>左侧内容</p>
  </div>
  <div>
    <h1>右侧标题</h1>
    <p>右侧内容</p>
  </div>
  <div class="page-num">3</div>
</section>

</body>
</html>
```

## 设计要点

1. **固定尺寸**：每页 `.slide` 必须是 `1280x720px`（16:9）或 `1920x1080px`（高清16:9）
2. **分页标记**：用 `<section class="slide">` 包裹每页内容，脚本自动识别
3. **内联样式优先**：截图方式不加载外部 CSS 文件，关键样式用 `<style>` 内联
4. **图片用绝对路径**：`<img src="file:///absolute/path/to/image.png">`，避免相对路径丢失
5. **字体选择**：用系统自带字体（PingFang SC / Microsoft YaHei / SimHei），避免截图时字体缺失
6. **避免动画**：截图是静态的，CSS 动画和 JS 交互不会生效
7. **overflow: hidden**：每页设置溢出隐藏，防止内容超出被截断

## 常见页面类型

| 类型 | class | 用途 |
|------|-------|------|
| 标题页 | `.slide.title` | 封面，居中大标题 |
| 内容页 | `.slide` | 标题+正文/列表 |
| 两栏页 | `.slide.two-col` | 左右对比 |
| 图片页 | `.slide` + `<img>` | 全图或图文混排 |
| 表格页 | `.slide` + `<table>` | 数据展示 |
| 代码页 | `.slide` + `<pre>` | 代码展示 |
| 结尾页 | `.slide.title` | 致谢/Q&A |

## 学术风格模板

适用于学术答辩、论文汇报等场景。设计灵感来自 LaTeX 论文排版和
[html-ppt-skill](https://github.com/lewislulu/html-ppt-skill) 的 academic-paper 主题。

### 配色方案

| 变量 | 颜色 | 用途 |
|------|------|------|
| `--bg` | `#fdfcf8` | 主背景（暖白/米白，模拟纸张） |
| `--surface` | `#ffffff` | 卡片表面（纯白） |
| `--text-1` | `#0a0a0a` | 主文字（近黑） |
| `--text-2` | `#333333` | 次级文字 |
| `--text-3` | `#707070` | 辅助文字 |
| `--accent` | `#1a3a7a` | 主强调色（学术深蓝） |
| `--accent-3` | `#8a1a1a` | 第三强调色（深红，用于关键数据） |
| `--good` | `#1a5a2a` | 正面/提升（深绿） |
| `--bad` | `#8a1a1a` | 负面/下降（深红） |

### 字体栈

```css
--font-serif: 'Noto Serif SC', 'Source Han Serif SC', Georgia, 'Times New Roman', serif;
--font-mono: 'SF Mono', 'Fira Code', 'Menlo', 'Courier New', monospace;
```

统一使用衬线字体，还原学术论文质感。中文用 Noto Serif SC（思源宋体），英文用 Georgia。

### 完整 CSS

```css
:root {
  --bg:#fdfcf8; --bg-soft:#f7f5ed; --surface:#ffffff; --surface-2:#f5f3ea;
  --border:rgba(20,20,20,.14); --border-strong:rgba(20,20,20,.35);
  --text-1:#0a0a0a; --text-2:#333333; --text-3:#707070;
  --accent:#1a3a7a; --accent-3:#8a1a1a;
  --good:#1a5a2a; --bad:#8a1a1a;
  --font-serif:'Noto Serif SC','Source Han Serif SC',Georgia,'Times New Roman',serif;
  --font-mono:'SF Mono','Fira Code','Menlo','Courier New',monospace;
}
body { margin:0; padding:0; background:#2a2230; font-family:var(--font-serif); }

/* 幻灯片：全直角、无阴影、米白底 */
.slide {
  width:1280px; height:720px; margin:0 auto 34px;
  background:var(--bg); overflow:hidden; position:relative;
  display:flex; flex-direction:column;
  border-radius:0; box-shadow:0 8px 40px rgba(0,0,0,.3);
}
.slide-body { flex:1; padding:30px 70px 50px; display:flex; flex-direction:column; }

/* 标题：衬线粗体，下方黑色实线 */
.kicker { font-family:var(--font-mono); font-size:13px; color:var(--accent);
  font-style:italic; font-weight:400; margin-bottom:8px; }
h1.title { font-family:var(--font-serif); font-size:36px; font-weight:700;
  color:var(--text-1); line-height:1.2; }
.rule { height:2px; background:var(--text-1); width:100%; margin:12px 0 24px; }

/* 正文 */
p.lead { font-size:18px; color:var(--text-2); line-height:1.8; }
ul.bul { list-style:none; margin-top:8px; }
ul.bul > li { position:relative; padding-left:22px; font-size:17px;
  color:var(--text-2); line-height:1.7; margin-bottom:12px; }
ul.bul > li::before { content:""; position:absolute; left:0; top:10px;
  width:6px; height:6px; background:var(--accent); }

/* 表格：极简底边框，表头弱化 */
table.t { width:100%; border-collapse:collapse; font-size:16px; }
table.t th, table.t td { padding:12px 16px; text-align:left;
  border-bottom:1px solid var(--border); }
table.t th { font-size:12px; text-transform:uppercase; letter-spacing:.1em;
  color:var(--text-3); font-weight:600; }
table.t td.num { font-variant-numeric:tabular-nums; text-align:right; }
.up { color:var(--good); font-weight:700; }
.dn { color:var(--bad); font-weight:700; }

/* 代码块 */
pre { background:#1e1e1e; color:#d4d4d4; padding:16px 20px;
  border-radius:0; font-family:var(--font-mono); font-size:14px; line-height:1.5;
  overflow-x:auto; }

/* 卡片：直角边框，无阴影 */
.card { border:1px solid var(--border); background:var(--surface);
  padding:20px; border-radius:0; }

/* 页脚 */
.foot { position:absolute; bottom:16px; left:70px; right:70px;
  display:flex; justify-content:space-between;
  font-family:var(--font-mono); font-size:11px; color:var(--text-3);
  border-top:1px solid var(--border); padding-top:8px; }

/* 强调色 */
.hl { color:var(--accent); font-weight:700; }
.hl-red { color:var(--accent-3); font-weight:700; }
.hl-green { color:var(--good); font-weight:700; }
```

### 学术页面类型

| 类型 | 适用场景 | 设计要点 |
|------|---------|---------|
| 封面页 | 论文标题/作者/日期 | 居中衬线大标题，下方黑色实线 |
| 研究问题 | 问题陈述 | kicker 斜体引语 + 编号列表 |
| 方法架构 | 模型/系统架构图 | 左图右文或全图，图下方 caption |
| 实验结果 | 数据表格 | 极简底边框表格，数字列右对齐 `tabular-nums` |
| 消融对比 | 对比表格 | 用 `.up`/`.dn` 标注涨跌 |
| 结论页 | 总结要点 | 编号列表 + 强调色高亮关键发现 |
| 致谢页 | Q&A | 居中衬线大字 |
