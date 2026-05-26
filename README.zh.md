# Sleepcast-Scripts-Cook

[中文版](./README.zh.md) | [English](./README.md)

一个自包含的 Claude Code / Agent skill，为 VelaSleep 生成**英文成人助眠 SleepCast 脚本**——可直接用于 TTS 的、像 native sleep story / sleep podcast 的旁白。

---

## 文件分工

本包同时包含**给人看的文档**和**给 agent 看的指令**，不要混淆：

| 文件 | 读者 | 作用 |
|---|---|---|
| `README.md` / `README.zh.md` | **人** | 安装、用法、自定义说明。Agent 运行时不读它们。 |
| `SKILL.md` | **Agent** | Skill 的执行指令与触发元数据。除非要修改 skill 行为，否则人一般不用看。 |
| `user_profile.md` | **人维护，Agent 读取** | 目标听众与内容偏好。人编辑，agent 每次运行参考。 |
| `references/sleepcast_script_prompt.md` | **人维护，Agent 读取** | 脚本规则唯一真源（标记/结构/节奏/禁区）。改脚本行为就改这里。 |
| `references/script_example.md` | **人维护，Agent 读取** | 成品脚本形态参考。 |

> 一句话：**README 给人看，`SKILL.md` 给 agent 看**；`user_profile.md` 和 `references/` 是两者共享的数据，由人维护、由 agent 读取。

---

## 它做什么

工作流分两阶段：

1. **生成 10 个候选选题**：综合你提供的背景材料（逐字稿、题材分析、竞品笔记、内容方向）和维护好的听众画像后蒸馏而来。
2. **生成完整脚本**：针对你选定的那一条。

它只产出脚本文本。TTS、混音、BGM/SFX 文件制作、音频后期由独立工程后台处理，不在本 skill 范围内。

---

## 目录结构

本仓库的**根目录就是 skill 包本身**——`SKILL.md` 在仓库顶层，而不是套在某个子文件夹里。clone 仓库后你得到的是一个以仓库命名的文件夹（`Sleepcast-Scripts-Cook/`）；而 skill 自身的名字（安装器使用的名字）是 `sleepcast-script`，取自 `SKILL.md` 里的 `name` 字段。

```
<仓库根目录>/                            # skill 包本身（clone 出来的目录：Sleepcast-Scripts-Cook/）
  README.md                             # 给人看的文档，英文
  README.zh.md                          # 给人看的文档，中文（本文件）
  SKILL.md                              # 给 agent 看的执行指令：触发元数据 + 两阶段工作流
  user_profile.md                       # 可编辑的目标听众 / 内容偏好画像
  references/
    sleepcast_script_prompt.md          # 脚本规则唯一真源
    script_example.md                   # 成品脚本形态参考
```

Skill 通过相对路径读取自身的 `references/` 和 `user_profile.md`，所以这个包是可移植的——不依赖仓库里其他位置的文件。

---

## 安装

> 这是**私密**仓库。先配好 git 认证（被加为协作者 + `gh auth login` / SSH key / PAT），否则 clone 和 `npx skills add` 都会失败。

Skill 最终必须以一个名为 `sleepcast-script` 的文件夹存在于可被发现的 skills 目录中。下面两条路径面向不同的安装者。

### A. 人工安装 —— 给人看

clone 仓库后，把它复制进 skills 目录、并**重命名为 `sleepcast-script`**（clone 出来的文件夹叫 `Sleepcast-Scripts-Cook`，不是 `sleepcast-script`）：

```bash
git clone https://github.com/ZimaBlue1226/Sleepcast-Scripts-Cook.git

# 个人级（所有项目可用）
cp -r Sleepcast-Scripts-Cook ~/.claude/skills/sleepcast-script

# 或项目级
cp -r Sleepcast-Scripts-Cook <你的项目>/.claude/skills/sleepcast-script
```

（如果希望在 clone 里改动能实时生效，可用软链代替复制。）

### B. 自动安装 —— 给 agent 看

跨 agent 安装器会识别根目录的 `SKILL.md`，并按其 frontmatter `name`（`sleepcast-script`）安装，与仓库名/clone 文件夹名无关：

```bash
npx skills add https://github.com/ZimaBlue1226/Sleepcast-Scripts-Cook
```

> 同样有私库限制：`npx skills add` 依赖本地 git 凭证，你必须已对该私密仓库完成认证。

如果你是正在**手动**安装本 skill 的 agent，请遵循以下指令：

- 这是一个**自包含 skill**，且**仓库根目录即 skill**——把仓库内容放进目标 agent skills 目录下的 `sleepcast-script/` 文件夹（Claude Code：`~/.claude/skills/` 或 `<项目>/.claude/skills/`）。
- 入口文件是 `SKILL.md`。**无需构建步骤**，运行时除读取本地文件外无其他依赖。
- `SKILL.md`、`user_profile.md`、`references/` 必须**保持在一起**，不可拆分；skill 通过相对路径读取 `references/` 和 `user_profile.md`。
- **不要**靠读 `README.md` / `README.zh.md` 来运行 skill——它们是给人看的文档。运行只依据 `SKILL.md`。

---

## 用法

调用 skill，并提供本次任务的背景材料——文字说明、本地文件路径、参考脚本/视频、竞品素材、评论反馈或内容方向均可。

1. Skill 给出 **10 个候选选题**（英文标题 + 中文说明），你选一个。
2. 可选指定：
   - 脚本参考时长（默认 **`30min`**）
   - 开头 BGM 单独铺底时长（默认 **`8s`**）
3. Skill 把完整英文脚本写入 `output/<YYYY-MM-DD>-<slug>.md`。

> 当前版本强制走 10 选 1 流程，不支持跳过选题、直接指定主题。

---

## 自定义

编辑 `user_profile.md` 调整目标听众与内容偏好——skill 每次运行都会参考它，无需每次重复输入。

脚本风格、结构、标记规则和内容禁区都在 `references/sleepcast_script_prompt.md` 里。要改脚本怎么写，就改这个文件——它是唯一真源。改完任何文件后记得重新 push 仓库，保持安装同步。
