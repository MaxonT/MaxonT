<p align="center"><img src="assets/banner-ming-yang2.svg" alt="Ming Yang, building Guli: agents that finish the work, CS at Vanderbilt" width="100%"></p>

<div align="center">

# Ming (Tiger) Yang | Building Guli

Startup Founder · AI Agent Operations · CS @ Vanderbilt

<a href="https://github.com/MaxonT"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1200&color=22D3EE&center=true&vCenter=true&width=760&lines=Building+Guli;Helping+AI+agents+get+real+work+done;Engineer+and+CS+student+at+Vanderbilt" alt="Building Guli. Helping AI agents get real work done. Engineer and CS student at Vanderbilt."></a>

![Focus](https://img.shields.io/badge/Focus-AI%20Agent%20Operations-7C3AED?style=for-the-badge&logo=openai&logoColor=white)
![Status](https://img.shields.io/badge/Status-Building%20Guli-22C55E?style=for-the-badge)
![School](https://img.shields.io/badge/CS-Vanderbilt%20University-866D4B?style=for-the-badge)
[![中文](https://img.shields.io/badge/%E4%B8%AD%E6%96%87-README-F59E0B?style=for-the-badge)](README.zh-CN.md)

<img src="assets/divider.svg" width="100%" alt="">

</div>

I'm building Guli, a startup exploring how AI agents can move from answering questions to reliably getting real work done.

My current focus is a simple question: when we delegate a task to an AI agent, how do we know it was actually completed?

I build software, explore agent systems, and turn ideas into practical tools.

## 🧭 What I'm building

Guli is building an operating platform for AI agents. The aim is to help people delegate real work to AI systems and then reliably understand whether that work was completed.

An agent that reports "done" has only told you something. The hard part is knowing it is true, and knowing what to do when it is not. That gap is the problem I care about.

Our initial focus:

| Area | The question behind it |
|:--|:--|
| Task fulfillment | Did the agent do the job that was asked? |
| Verification | What evidence shows the work was completed? |
| Reliability | Does it hold up run after run, not only once? |
| Recovery | When a task fails, how does the work get back on track? |

Security and safety are foundational principles in how we build. They are part of the work, not the whole of it.

## 🧪 Selected engineering and open source

<sub>Personal open-source experiments on the same questions. They are not Guli products. Click a card to open the repo.</sub>

<table>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/MaxonT/TRACES.md"><img src="assets/lab-traces.svg" width="100%" alt="TRACES.md: AGENTS.md, but for what agents did"></a>
<p align="center"><a href="https://github.com/MaxonT/TRACES.md"><img src="https://img.shields.io/github/stars/MaxonT/TRACES.md?style=social" alt="TRACES.md stars"></a> · <a href="https://github.com/MaxonT/TRACES.md">Open TRACES.md →</a></p>
</td>
<td width="50%" valign="top">
<a href="https://github.com/MaxonT/aisync"><img src="assets/lab-aisync.svg" width="100%" alt="aisync: one standup for all your AI coding tools"></a>
<p align="center"><a href="https://github.com/MaxonT/aisync"><img src="https://img.shields.io/github/stars/MaxonT/aisync?style=social" alt="aisync stars"></a> · <a href="https://github.com/MaxonT/aisync">Open aisync →</a></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="https://github.com/MaxonT/existence-trace"><img src="assets/lab-etrace.svg" width="100%" alt="existence-trace: journal in, your feedback becomes rules"></a>
<p align="center"><a href="https://github.com/MaxonT/existence-trace"><img src="https://img.shields.io/github/stars/MaxonT/existence-trace?style=social" alt="existence-trace stars"></a> · <a href="https://github.com/MaxonT/existence-trace">Open existence-trace →</a></p>
</td>
<td width="50%" valign="middle" align="center">
<sub>Three small experiments on one question:<br>how do we know what an agent actually did?<br><br>Record it (TRACES.md).<br>Coordinate it (aisync).<br>Prove it was used (existence-trace).</sub>
</td>
</tr>
</table>

| Project | Problem it addresses | What it demonstrates | What it does today |
|:--|:--|:--|:--|
| [TRACES.md](https://github.com/MaxonT/TRACES.md) | After an agent finishes, there is no reliable record of what it did, and failures get lost. | An open spec with validators, so agent work can be checked without trusting the agent's own summary. | A plain-text format and a Python CLI (standard library only). One append-only file per task, one line per tool call, failures included. The validator rejects a trace that hides a failure. |
| [aisync](https://github.com/MaxonT/aisync) | Several AI coding tools edit the same codebase without knowing what the others are doing. | Coordination and conflict handling between agents. | A local hub with shared rules, file claims that stop two agents editing the same file, a hash-chained journal of decisions and commits, and hooks that tell a running session what the others just did. Works with Claude Code, Codex and Cursor on macOS and Linux. |
| [existence-trace](https://github.com/MaxonT/existence-trace) | An AI can read all of your code and still have no checkable memory of you. | An AI that has to prove it used what it knows. | Reads a daily journal in files you own, asks when it is unsure, turns your answers into rules, and keeps a receipt each time a rule changes a report. A reflection aid, not a clinical tool. |

## 🧰 Technical skills

<p align="center">
  <img src="https://skillicons.dev/icons?i=py,js,ts,react,nodejs,express,mongodb,java,cpp,html,css,git,github,vscode,linux,docker&perline=8" alt="Skill icons">
</p>

![Languages](https://img.shields.io/badge/Languages-Python%20%7C%20JavaScript%20%7C%20TypeScript%20%7C%20Java%20%7C%20C%2B%2B-3B82F6?style=flat-square)
![Web](https://img.shields.io/badge/Web-React%20%7C%20Node.js%20%7C%20Express%20%7C%20HTML%20%7C%20CSS-F97316?style=flat-square)
![Data](https://img.shields.io/badge/Data-MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white)
![AI](https://img.shields.io/badge/AI-Agent%20Systems%20%7C%20Evals%20%7C%20Claude%20Code%20%7C%20LangChain%20%7C%20Prompting-8B5CF6?style=flat-square)
![Habits](https://img.shields.io/badge/Habits-Small%20commits%20%7C%20Open%20specs%20%7C%20Stdlib%20first-14B8A6?style=flat-square)

<p align="center"><img src="assets/workflow-sketch.svg" width="100%" alt="Decompose, system design, build with AI, evaluate, ship and learn"></p>

## 📊 GitHub activity and projects

<p align="center">
  <img height="180" src="https://github-readme-stats-liard-ten-90.vercel.app/api?username=MaxonT&show_icons=true&theme=radical" alt="GitHub stats">
  <img height="180" src="https://github-readme-stats-liard-ten-90.vercel.app/api/top-langs/?username=MaxonT&layout=compact&theme=radical" alt="Top languages">
</p>
<p align="center">
  <img src="assets/activity.svg" width="100%" alt="Contribution activity, last 30 days">
</p>

<a id="latest"></a>

### Recent public repositories

Refreshed automatically every hour, star counts are live. The auto-maintained, star-ranked reference lists are collected [here](https://github.com/MaxonT?tab=repositories&q=top-&type=source).

<!-- LATEST:START -->
| Project | ⭐ | Updated | What it is |
|:--|:-:|:-:|:--|
| [awesome-agent-workflows](https://github.com/MaxonT/awesome-agent-workflows) | ![](https://img.shields.io/github/stars/MaxonT/awesome-agent-workflows?style=flat-square&label=&color=F5C518) | 2026-11-02 | Curated, star-ranked catalog of AI agent frameworks, coding-agent harnesses and workflow platform... |
| [reeta](https://github.com/MaxonT/reeta) | ![](https://img.shields.io/github/stars/MaxonT/reeta?style=flat-square&label=&color=F5C518) | 2026-10-20 | Reeta: teach the AI student. HackTN26, Challenge #3 |
| [prompt-mirror](https://github.com/MaxonT/prompt-mirror) | ![](https://img.shields.io/github/stars/MaxonT/prompt-mirror?style=flat-square&label=&color=F5C518) | 2026-10-12 | ai interations analysis statistic tool, see your interations with ai |
| [tweeter_prototype](https://github.com/MaxonT/tweeter_prototype) | ![](https://img.shields.io/github/stars/MaxonT/tweeter_prototype?style=flat-square&label=&color=F5C518) | 2026-10-12 | 🚀 A sleek UI demo for SocialMax, prototype social app interface built to explore design, layout a... |
| [learn_html_workshop](https://github.com/MaxonT/learn_html_workshop) | ![](https://img.shields.io/github/stars/MaxonT/learn_html_workshop?style=flat-square&label=&color=F5C518) | 2026-01-06 | 🔥This hands-on session will teach you how to build a beautiful, modern portfolio website using on... |
<!-- LATEST:END -->

<details>
<summary>🔬 What I am exploring (click to open)</summary>

<br>

- 🎯 Agent reliability: knowing whether a delegated task was actually completed, and recovering when it was not
- 🤖 Agent observability: what an agent did, and how to learn from its failures
- 🧠 Evaluation first: small test sets that tell me whether an AI tool is actually better
- 🎓 Learning science applied to quizzes, spaced review and study plans
- 🌐 Bilingual docs and tools (English and 中文) as a default, not an afterthought

</details>

<img src="assets/divider.svg" width="100%" alt="">

<details>
<summary>🎮 Off duty: games and horror (click to open)</summary>

<br>

![Horror](https://img.shields.io/badge/Horror%20pick-FNAF-f59e0b?style=for-the-badge)
![Night](https://img.shields.io/badge/Night%205-survived-22c55e?style=for-the-badge)

<sub><i>3 AM and the hallway hums. A door that was shut a minute ago is open now, light leaking out like it has somewhere to be. Someone is standing in it, or maybe I am the one standing and the corridor is what moves. Nothing in the footage explains itself. Neither do I. The build is still green though.</i></sub>

<p align="center"><img src="assets/corridor-sketch.svg" width="100%" alt="A figure standing in a lit doorway at the end of a dark corridor"></p>

And because debugging at 3 AM feels exactly like surviving a night shift, here is a night shift scene I drew:

<p align="center"><img src="assets/fnaf-sketch.svg" width="100%" alt="A dim night security office"></p>

</details>

<p align="center"><img src="assets/footer.svg" width="100%" alt=""></p>

<p align="center"><sub>The repositories here are my personal open-source work. Guli is my startup.</sub></p>
