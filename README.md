# sleepcast-script

[English](./README.md) | [中文版](./README.zh.md)

A self-contained Claude Code / Agent skill that generates **English adult-sleep SleepCast scripts** for VelaSleep — TTS-ready narration in the style of a native sleep story / sleep podcast.

---

## Who reads what

This package mixes **human-facing docs** and **agent-facing instructions**. Don't confuse them:

| File | Audience | Purpose |
|---|---|---|
| `README.md` / `README.zh.md` | **Humans** | Install, usage, customization. The agent does not read these at runtime. |
| `SKILL.md` | **Agent** | The skill's execution instructions and trigger metadata. Humans rarely need it unless changing the skill's behavior. |
| `user_profile.md` | **Human-maintained, agent-read** | Target audience and content preferences. You edit it; the agent consults it every run. |
| `references/sleepcast_script_prompt.md` | **Human-maintained, agent-read** | The single source of truth for script rules (markup / structure / rhythm / red lines). Edit this to change how scripts are written. |
| `references/script_example.md` | **Human-maintained, agent-read** | Reference for the finished-script shape. |

> In one line: **README is for humans, `SKILL.md` is for the agent.** `user_profile.md` and `references/` are shared data — maintained by humans, read by the agent.

---

## What it does

The skill works in two stages:

1. **Propose 10 topic candidates** distilled from your background material (transcripts, theme analyses, competitor notes, content direction) plus a maintained audience profile.
2. **Write the full script** for the one you pick.

It produces only the script text. TTS, mixing, BGM/SFX file production, and audio post are handled by a separate engineering backend and are out of scope.

---

## Contents

This repository's **root is the skill package itself** — `SKILL.md` lives at the top level, not inside a wrapper folder. When you clone the repo you get a folder named after the repo (`Sleepcast-Scripts-Cook/`); the skill's own name (used by installers) is `sleepcast-script`, taken from the `name` field in `SKILL.md`.

```
<repo root>/                            # the skill package (clone dir: Sleepcast-Scripts-Cook/)
  README.md                             # human docs, English (this file)
  README.zh.md                          # human docs, Chinese
  SKILL.md                              # agent instructions: trigger metadata + two-stage workflow
  user_profile.md                       # editable target-audience / content-preference profile
  references/
    sleepcast_script_prompt.md          # single source of truth for script rules
    script_example.md                   # reference for the finished-script shape
```

The skill reads its own bundled `references/` and `user_profile.md` by relative path, so the package is portable — no dependency on files elsewhere.

---

## Install

> This is a **private** repo. Configure git auth first (be a collaborator + `gh auth login` / SSH key / PAT), otherwise both clone and `npx skills add` will fail.

The skill must end up as a folder named `sleepcast-script` inside a discovered skills directory. The two paths below serve different installers.

### A. Manual install — for a human

Clone the repo, then copy it into a skills directory **renamed to `sleepcast-script`** (the clone folder is named `Sleepcast-Scripts-Cook`, not `sleepcast-script`):

```bash
git clone https://github.com/ZimaBlue1226/Sleepcast-Scripts-Cook.git

# personal (all projects)
cp -r Sleepcast-Scripts-Cook ~/.claude/skills/sleepcast-script

# or project-level
cp -r Sleepcast-Scripts-Cook <your-project>/.claude/skills/sleepcast-script
```

(You may symlink instead of copy if you want edits in the clone to take effect live.)

### B. Automated install — for an agent

The cross-agent installer detects the root-level `SKILL.md` and installs the skill under its frontmatter `name` (`sleepcast-script`) regardless of the repo/clone folder name:

```bash
npx skills add https://github.com/ZimaBlue1226/Sleepcast-Scripts-Cook
```

> Same private-repo caveat applies: `npx skills add` relies on your local git credentials, so you must already be authenticated to the private repo.

If you are an agent installing this skill manually instead, follow these directives:

- This is a **self-contained skill** and the **repo root is the skill** — place the repo's contents into a `sleepcast-script/` directory in the target agent's skills directory (Claude Code: `~/.claude/skills/` or `<project>/.claude/skills/`).
- The entry point is `SKILL.md`. There is **no build step** and no runtime dependencies beyond reading local files.
- Keep `SKILL.md`, `user_profile.md`, and `references/` **together** — never split them apart; the skill reads `references/` and `user_profile.md` by relative path.
- Do **not** read `README.md` / `README.zh.md` to operate the skill — they are human documentation. Operate only from `SKILL.md`.

---

## Usage

Invoke the skill and provide this run's background material — free text, local file paths, reference scripts/videos, competitor material, audience comments, or a content direction.

1. The skill presents **10 topic candidates** (English titles + Chinese explanations). Pick one.
2. Optionally specify:
   - script reference duration (default **`30min`**)
   - opening BGM solo lead-in (default **`8s`**)
3. The skill writes the full English script to `output/<YYYY-MM-DD>-<slug>.md`.

> The current version requires the 10-choose-1 flow; you cannot skip topic selection and name a theme directly.

---

## Customizing

Edit `user_profile.md` to adjust the target audience and content preferences — the skill consults it on every run, so you don't re-enter this each time.

Script style, structure, markup rules, and content red lines live in `references/sleepcast_script_prompt.md`. To change how scripts are written, edit that file — it is the single source of truth. After editing any file, re-push the repo so installs stay in sync.
