# sleepcast-script

*[English](#english) · [中文](#中文)*

A self-contained Claude Code / Agent skill that generates **English adult-sleep SleepCast scripts** for VelaSleep — TTS-ready narration in the style of a native sleep story / sleep podcast.

---

## Who reads what / 文件分工

This package mixes **human-facing docs** and **agent-facing instructions**. Don't confuse them:

| 文件 | 读者 / Audience | 作用 / Purpose |
|---|---|---|
| `README.md` (this file) | **人 / Humans** | 安装、用法、自定义说明。Agent 运行时不读它。 |
| `SKILL.md` | **Agent** | Skill 的执行指令与触发元数据。**人一般不用看**，除非要修改 skill 的行为。 |
| `user_profile.md` | **人维护，Agent 读取** | 目标听众与内容偏好。人编辑，agent 每次运行参考。 |
| `references/sleepcast_script_prompt.md` | **人维护，Agent 读取** | 脚本规则唯一真源（标记/结构/节奏/禁区）。改脚本行为就改这里。 |
| `references/script_example.md` | **人维护，Agent 读取** | 成品脚本形态参考。 |

> 一句话：**README 给人看，SKILL.md 给 agent 看**；`user_profile.md` 和 `references/` 是两者共享的数据，由人维护、由 agent 读取。

---

## English

### What it does

The skill works in two stages:

1. **Propose 10 topic candidates** distilled from your background material (transcripts, theme analyses, competitor notes, content direction) plus a maintained audience profile.
2. **Write the full script** for the one you pick.

It produces only the script text. TTS, mixing, BGM/SFX file production, and audio post are handled by a separate engineering backend and are out of scope.

### Contents

```
sleepcast-script/
  README.md                             # human docs (this file)
  SKILL.md                              # agent instructions: trigger metadata + two-stage workflow
  user_profile.md                       # editable target-audience / content-preference profile
  references/
    sleepcast_script_prompt.md          # single source of truth for script rules
    script_example.md                   # reference for the finished-script shape
```

The skill reads its own bundled `references/` copies, so the package is portable — no dependency on files elsewhere in the repo.

### Install

A standard self-contained skill folder. Install it into any agent that supports skills.

**Claude Code** — copy or symlink into a discovered skills directory:

```bash
# personal (all projects)
cp -r sleepcast-script ~/.claude/skills/

# or project-level
cp -r sleepcast-script <your-project>/.claude/skills/
```

**Cross-agent installer** (Claude Code, Codex, etc.):

```bash
npx skills add <github-repo-url>
```

> This is a private repo. Only collaborators with git auth configured can clone/install it.

### Usage

Invoke the skill and provide this run's background material — free text, local file paths, reference scripts/videos, competitor material, audience comments, or a content direction.

1. The skill presents **10 topic candidates** (English titles + Chinese explanations). Pick one.
2. Optionally specify:
   - script reference duration (default **`30min`**)
   - opening BGM solo lead-in (default **`8s`**)
3. The skill writes the full English script to `output/<YYYY-MM-DD>-<slug>.md`.

> The current version requires the 10-choose-1 flow; you cannot skip topic selection and name a theme directly.

### Customizing

Edit `user_profile.md` to adjust the target audience and content preferences — the skill consults it on every run, so you don't re-enter this each time.

Script style, structure, markup rules, and content red lines live in `references/sleepcast_script_prompt.md`. To change how scripts are written, edit that file — it is the single source of truth.

---

## 中文

### 它做什么

这是一个自包含的 Claude Code / Agent skill，为 VelaSleep 生成**英文成人助眠 SleepCast 脚本**——可直接用于 TTS 的、像 native sleep story / sleep podcast 的旁白。

工作流分两阶段：

1. **生成 10 个候选选题**：综合你提供的背景材料（逐字稿、题材分析、竞品笔记、内容方向）和维护好的听众画像后蒸馏而来。
2. **生成完整脚本**：针对你选定的那一条。

它只产出脚本文本。TTS、混音、BGM/SFX 文件制作、音频后期由独立工程后台处理，不在本 skill 范围内。

### 目录结构

```
sleepcast-script/
  README.md                             # 给人看的说明（本文件）
  SKILL.md                              # 给 agent 看的执行指令：触发元数据 + 两阶段工作流
  user_profile.md                       # 可编辑的目标听众 / 内容偏好画像
  references/
    sleepcast_script_prompt.md          # 脚本规则唯一真源
    script_example.md                   # 成品脚本形态参考
```

Skill 读取的是自身 `references/` 内的副本，所以这个包是可移植的——不依赖仓库里其他位置的文件。

### 安装

这是一个标准的自包含 skill 文件夹，可装进任何支持 skill 的 agent。

**Claude Code** —— 复制或软链到可被发现的 skills 目录：

```bash
# 个人级（所有项目可用）
cp -r sleepcast-script ~/.claude/skills/

# 或项目级
cp -r sleepcast-script <你的项目>/.claude/skills/
```

**跨 agent 安装器**（Claude Code、Codex 等）：

```bash
npx skills add <github-repo-url>
```

> 这是私密仓库，只有被加为协作者、且本机配好 git 认证的人才能 clone/安装。

### 用法

调用 skill，并提供本次任务的背景材料——文字说明、本地文件路径、参考脚本/视频、竞品素材、评论反馈或内容方向均可。

1. Skill 给出 **10 个候选选题**（英文标题 + 中文说明），你选一个。
2. 可选指定：
   - 脚本参考时长（默认 **`30min`**）
   - 开头 BGM 单独铺底时长（默认 **`8s`**）
3. Skill 把完整英文脚本写入 `output/<YYYY-MM-DD>-<slug>.md`。

> 当前版本强制走 10 选 1 流程，不支持跳过选题、直接指定主题。

### 自定义

编辑 `user_profile.md` 调整目标听众与内容偏好——skill 每次运行都会参考它，无需每次重复输入。

脚本风格、结构、标记规则和内容禁区都在 `references/sleepcast_script_prompt.md` 里。要改脚本怎么写，就改这个文件——它是唯一真源。
