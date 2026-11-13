# 北理工通用组会 Beamer 模板

适用于论文精读、专题讲解和阶段进展汇报的 LaTeX Beamer 模板。

采用 16:9、北理工绿色、橙色少量强调和白底正文，提供正式封面、校徽、校园横幅、技术框架、实验表格及总结版式。正文页默认使用轻量白底页眉，也可切换为绿色渐变页眉。所有入口共享一个主题，默认汇报人为“汇报人姓名”。

## 选择起点

| 入口 | 适用场景 | 组织方式 |
|---|---|---|
| `main.tex` / `main.pdf` | 浏览与选取通用版式 | 背景、方法、实验、总结与计划 |
| `paper.tex` / `paper.pdf` | 单篇论文精读 | 问题、贡献、方法、结果、课题联系 |
| `tutorial.tex` / `tutorial.pdf` | Transformer、扩散模型等专题讲解 | 基础概念、计算原理、任务应用 |
| `progress.tex` / `progress.pdf` | 周报、月报、阶段工作 | 目标、实现、结果、问题与计划 |

编译后可查看四个入口的 PDF：版式库 24 页（含一帧的两步展示，共 23 个 frame），论文入口 13 页，专题入口 12 页，进展入口 12 页。PDF 在本地生成，不纳入 Git 备份。

复制整个项目文件夹，选择一个入口，修改 `config.tex`，再填写入口中的正文。版式库的正文位于 `sections/`，可以把需要的 `frame` 复制到所选入口。完整的版式库不意味着每次都要展示所有页面。

## 通用版式

- 学校封面：中文主题、英文主题、机构、汇报场合、姓名与日期。
- 带说明的目录和章节页：短标题下补一句该部分要讲的内容。
- 研究问题与贡献、基础概念与符号表、概念或方法对照。
- 整体框架大图、左图右解释、目标函数和关键推导。
- 训练/推理分栏、两步展示的可编辑计算流程。
- 实验设置与指标、主要结果表、定性对比、消融与参数分析。
- 工作总结、适用范围、阶段进展、问题排查、时间计划与讨论。

所有占位内容都是待填写字段，示意公式标注为通用排版占位。原生表格使用 `booktabs`，公式使用 LaTeX 数学排版，流程图使用 TikZ。校徽与校园横幅位于 `assets/` 目录。

## 配置

`config.tex` 中设置：

```latex
\title[页脚短标题]{封面主标题}
\subtitle{中文主题或论文中文标题}
\setenglishtitle{English Topic / Original Paper Title}
\setpresenter{汇报人姓名}
\setaffiliation{北京理工大学}
\setmeeting{课题组组会}
\date{2026.11.09}
\setpaper{Original Paper Title}{Authors}{Venue, Year}
\setheaderstyle{light}  % 轻量白底页眉，正文空间更大
% \setheaderstyle{band} % 绿色渐变页眉
% \bitsectionpagesfalse % 短汇报关闭章节过渡页
```

日期默认取编译当天。如有固定汇报日期，改为固定值。

## 编译

使用 **XeLaTeX**。不需要上传任何文件到在线服务。

Windows 双击 `build.cmd` 编译版式库，或在终端运行：

```bat
build.cmd
build.cmd paper
build.cmd tutorial
build.cmd progress
build.cmd --all
```

等价的跨平台命令：

```sh
python build.py paper
python build.py --all
python build.py paper --engine /path/to/xelatex
```

脚本先查找 PATH 中的 XeLaTeX，在当前电脑也支持 `F:\texlive\2023\bin\windows\xelatex.exe`，连续编译两次更新目录。PDF 输出到项目根目录，中间文件和日志放在 `.build/`。

也可 `latexmk -xelatex paper.tex`。Overleaf 上传整个项目、设置 XeLaTeX，并把希望编译的入口选作 Main document。Windows 优先使用微软雅黑与 Arial，缺少微软雅黑时回退到 TeX Live 自带 Fandol。

## 常用命令

```latex
\BITtitlepage
\BITcontents
\bitsection{方法与实现}{整体框架、关键机制与运行方式}
\bitcolumns{左栏内容}{右栏内容}
\bitstrong{重点术语}
\bitcallout{本页最重要的结论}
\bitsource{作者、年份、Fig. X / Table X}
\bitexperiment{实验目的}{评估条件}
\bitfigure[.55\textheight]{assets/your-figure.pdf}{图注}
\bitimageplaceholder[.45\textheight]{待插入的图}
\BITthankyou
```

使用 `\bitsection` 可以把章节说明写入目录；普通 `\section` 只适用于不需要说明的情况。默认目录为 3–4 个主要章节，最多建议 5 个；更多章节需拆目录或调整布局。

分步讲解使用 `\uncover<1->`、`\uncover<2->` 保持元素位置稳定。同一帧在 PDF 中会产生两个页面，页脚帧号保持相同。需要静态版本时，将文档类增加 `handout` 选项，或把分步内容合并到一页。

## 内容密度

正文页标题建议不超过约 18 个汉字，正文通常 4–6 条要点。完整框架图可以独占一页，密集图表应分开讲。来源文字使用页底专用区域，长引用放在正文或另附参考页。表格保留指标单位、方向及统计口径，避免直接用论文整页截图代替可读结果。

## Git 备份与后续复用

此目录是可独立复制的模板工程。保留全部 `.tex`、`.sty`、`assets/`、编译脚本及 `latexmkrc`，无需本目录外的论文、视频或旧版模板。

主题支持配置章节号和页码前缀，结束页显示汇报人和日期。

从远程仓库获取模板并编译论文汇报入口：

```sh
git clone https://github.com/Jack-Zhang1101/BIT_latex_beam.git
cd BIT_latex_beam
python build.py paper
```

使用前安装 Python 3 和包含中文支持、Beamer、TikZ 的 TeX Live / MiKTeX，并确保 `xelatex` 可用。`python build.py --all` 可生成全部四种入口的 PDF；编译脚本只使用 Python 标准库。

修改后，在仓库目录中执行以下命令保存版本：

```sh
git add .
git commit -m "Update BIT Beamer template"
git push
```

`git push` 需要当前账号拥有远程仓库的写入权限。

`.gitignore` 排除了 `.build/`、编译日志和四个入口的生成 PDF、预览截图；`assets/` 中的主题图片会随源文件一同备份。制作新汇报时，复制工作目录中的源文件，修改 `config.tex` 并选择 `paper.tex`、`tutorial.tex` 或 `progress.tex`。
