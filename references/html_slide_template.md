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
