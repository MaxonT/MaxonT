<p align="center"><img src="assets/banner-ming-yang2.svg" alt="Ming Yang，正在做 Guli：让 agent 把事情真正做完，Vanderbilt 计算机系" width="100%"></p>

<div align="center">

# Ming (Tiger) Yang | 正在做 Guli

创业者 · AI Agent 运营 · Vanderbilt 计算机系

[English](README.md) · 简体中文

![Focus](https://img.shields.io/badge/%E6%96%B9%E5%90%91-AI%20Agent%20%E8%BF%90%E8%90%A5-7C3AED?style=for-the-badge&logo=openai&logoColor=white)
![Status](https://img.shields.io/badge/%E7%8A%B6%E6%80%81-%E6%AD%A3%E5%9C%A8%E5%81%9A%20Guli-22C55E?style=for-the-badge)
![School](https://img.shields.io/badge/CS-Vanderbilt%20University-866D4B?style=for-the-badge)

<img src="assets/divider.svg" width="100%" alt="">

</div>

我正在做 Guli，一家创业公司，探索 AI agent 如何从回答问题，走向可靠地把真实的工作做完。

我现在关注一个很简单的问题：把任务交给 AI agent 之后，怎么知道它真的做完了？

我写软件，研究 agent 系统，把想法做成实用的工具。

## 🧭 我在做什么

Guli 在做一个 AI agent 的运营平台。目标是让人可以把真实的工作交给 AI 系统，并且能可靠地知道这些工作有没有完成。

agent 说一句「做完了」，只是它告诉了你一件事。难的是确认这是真的，以及不是真的时该怎么办。这个缺口就是我在意的问题。

我们最初的重点：

| 方向 | 背后的问题 |
|:--|:--|
| 任务完成 | agent 做的是不是被要求的那件事？ |
| 验证 | 有什么证据能说明工作确实完成了？ |
| 可靠性 | 它能一次又一次稳定做到，而不只是一次吗？ |
| 恢复 | 任务失败后，工作怎样回到正轨？ |

安全是我们做事的基础原则，但它只是工作的一部分，不是全部。

## 🧪 精选的工程与开源项目

<sub>围绕同一批问题做的个人开源实验，不是 Guli 的产品。点卡片进入仓库。</sub>

<table>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/MaxonT/TRACES.md"><img src="assets/lab-traces.zh.svg" width="100%" alt="TRACES.md：记录 agent 做了什么"></a>
<p align="center"><a href="https://github.com/MaxonT/TRACES.md"><img src="https://img.shields.io/github/stars/MaxonT/TRACES.md?style=social" alt="TRACES.md stars"></a> · <a href="https://github.com/MaxonT/TRACES.md">打开 TRACES.md →</a></p>
</td>
<td width="50%" valign="top">
<a href="https://github.com/MaxonT/aisync"><img src="assets/lab-aisync.zh.svg" width="100%" alt="aisync：让所有 AI 编程工具开同一个站会"></a>
<p align="center"><a href="https://github.com/MaxonT/aisync"><img src="https://img.shields.io/github/stars/MaxonT/aisync?style=social" alt="aisync stars"></a> · <a href="https://github.com/MaxonT/aisync">打开 aisync →</a></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/MaxonT/existence-trace"><img src="assets/lab-etrace.zh.svg" width="100%" alt="existence-trace：日记进去，反馈变成规则"></a>
<p align="center"><a href="https://github.com/MaxonT/existence-trace"><img src="https://img.shields.io/github/stars/MaxonT/existence-trace?style=social" alt="existence-trace stars"></a> · <a href="https://github.com/MaxonT/existence-trace">打开 existence-trace →</a></p>
</td>
<td width="50%" valign="middle" align="center">
<sub>三个小实验，对着同一个问题：<br>怎么知道 agent 到底做了什么？<br><br>把它记下来（TRACES.md）。<br>让它们互相协调（aisync）。<br>证明它真的用了（existence-trace）。</sub>
</td>
</tr>
</table>

| 项目 | 解决的问题 | 它展示了什么 | 目前能做什么 |
|:--|:--|:--|:--|
| [TRACES.md](https://github.com/MaxonT/TRACES.md) | agent 做完之后，没有可靠的记录说明它做了什么，失败也容易丢。 | 一个带校验器的开放规范，不必相信 agent 自己的总结，也能检查它的工作。 | 纯文本格式加 Python 命令行（只用标准库）。每个任务一个只追加的文件，每次工具调用一行，失败也如实记录。校验器会拒绝隐瞒失败的记录。 |
| [aisync](https://github.com/MaxonT/aisync) | 好几个 AI 编程工具在同一个代码库里改东西，却不知道彼此在做什么。 | agent 之间的协调与冲突处理。 | 本地中枢：共享规则，防止两个 agent 同时改同一文件的文件认领，记录决策和提交的哈希链日志，以及把其他工具刚做的事告诉正在运行的会话的钩子。支持 macOS 和 Linux 上的 Claude Code、Codex 和 Cursor。 |
| [existence-trace](https://github.com/MaxonT/existence-trace) | AI 可以读遍你的代码，却对你这个人没有可核查的记忆。 | 一个必须证明自己用了所知内容的 AI。 | 读取你自己文件夹里的每日日记，不确定时发问，把你的回答变成规则，每次规则改变报告时留下凭证。它是自我反思的辅助工具，不是临床工具。 |

## 🧰 技术栈

<p align="center">
  <img src="https://skillicons.dev/icons?i=py,js,ts,react,nodejs,express,mongodb,java,cpp,html,css,git,github,vscode,linux,docker&perline=8" alt="Skill icons">
</p>

<p align="center"><img src="assets/workflow-sketch.svg" width="100%" alt="拆解，系统设计，AI 构建，评估，发布，学习"></p>

## 📊 GitHub 动态与项目

<p align="center">
  <img height="180" src="https://github-readme-stats-liard-ten-90.vercel.app/api?username=MaxonT&show_icons=true&theme=radical" alt="GitHub stats">
  <img height="180" src="https://github-readme-stats-liard-ten-90.vercel.app/api/top-langs/?username=MaxonT&layout=compact&theme=radical" alt="Top languages">
</p>
<p align="center">
  <img src="assets/activity.svg" width="100%" alt="最近 30 天的贡献活动">
</p>

### 最近的公开仓库

每小时自动刷新一次，星数实时显示。自动维护的、按 star 排序的参考清单集中在[这里](https://github.com/MaxonT?tab=repositories&q=top-&type=source)。

<!-- LATEST:START -->
| 项目 | ⭐ | 更新 | 做什么 |
|:--|:-:|:-:|:--|
| [awesome-agent-workflows](https://github.com/MaxonT/awesome-agent-workflows) | ![](https://img.shields.io/github/stars/MaxonT/awesome-agent-workflows?style=flat-square&label=&color=F5C518) | 2026-11-02 | Curated, star-ranked catalog of AI agent frameworks, coding-agent harnesses and workflow platform... |
| [reeta](https://github.com/MaxonT/reeta) | ![](https://img.shields.io/github/stars/MaxonT/reeta?style=flat-square&label=&color=F5C518) | 2026-10-20 | Reeta: teach the AI student. HackTN26, Challenge #3 |
| [prompt-mirror](https://github.com/MaxonT/prompt-mirror) | ![](https://img.shields.io/github/stars/MaxonT/prompt-mirror?style=flat-square&label=&color=F5C518) | 2026-10-12 | ai interations analysis statistic tool, see your interations with ai |
| [tweeter_prototype](https://github.com/MaxonT/tweeter_prototype) | ![](https://img.shields.io/github/stars/MaxonT/tweeter_prototype?style=flat-square&label=&color=F5C518) | 2026-10-12 | 🚀 A sleek UI demo for SocialMax, prototype social app interface built to explore design, layout a... |
| [learn_html_workshop](https://github.com/MaxonT/learn_html_workshop) | ![](https://img.shields.io/github/stars/MaxonT/learn_html_workshop?style=flat-square&label=&color=F5C518) | 2026-01-06 | 🔥This hands-on session will teach you how to build a beautiful, modern portfolio website using on... |
<!-- LATEST:END -->

<details>
<summary>🔬 我在研究什么（点击展开）</summary>

<br>

- 🎯 Agent 可靠性：知道交出去的任务是否真的完成，没完成时怎么恢复
- 🤖 Agent 可观测性：agent 做了什么，以及怎样从它的失败里学到东西
- 🧠 先做评估：用小型测试集判断一个 AI 工具是不是真的更好
- 🎓 把学习科学用在测验、间隔复习和学习计划上
- 🌐 中英双语的文档和工具作为默认，而不是事后补上

</details>

<img src="assets/divider.svg" width="100%" alt="">

<details>
<summary>🎮 下班时间：游戏与恐怖（点击展开）</summary>

<br>

![FNAF](https://img.shields.io/badge/%E6%81%90%E6%80%96%E6%B8%B8%E6%88%8F-FNAF-f59e0b?style=for-the-badge)

<sub><i>凌晨三点，走廊在嗡嗡响。一分钟前还关着的门开了，光漏出来，像赶着去哪里。有人站在光里，或者站着的是我，动的是走廊。画面从不解释自己，我也是。不过构建还是绿的。</i></sub>

<p align="center"><img src="assets/corridor-sketch.svg" width="100%" alt="走廊尽头门光中的人影"></p>

凌晨三点调 bug 就像在熬 FNAF 的夜班，所以画了一张夜班保安室：

<p align="center"><img src="assets/fnaf-sketch.svg" width="100%" alt="深夜保安室"></p>

</details>

<p align="center"><img src="assets/footer.svg" width="100%" alt=""></p>

<p align="center"><sub>这里的仓库是我个人的开源作品。Guli 是我的创业项目。</sub></p>
