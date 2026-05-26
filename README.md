# sleepcast-scripts-cook

[English](./README.md) | [中文版](./README.zh.md)

A self-contained Claude Code / Agent skill that generates **English adult-sleep SleepCast scripts** for VelaSleep — TTS-ready narration in the style of a native sleep story / sleep podcast.

---

## Who reads what

This package mixes **human-facing docs** and **agent-facing instructions**. Don't confuse them:

| File | Audience | Purpose |
|---|---|---|
| `README.md` / `README.zh.md` | **Humans** | Install, usage, customization. The agent does not read these at runtime. |
| `SKILL.md` | **Agent** | The skill's execution instructions and trigger metadata. Humans rarely need it unless changing the skill's behavior. |
| `script_rules.md` | **Core, agent-read** | **The core of the skill** — the single source of truth for how scripts are written (markup / the 6 PARTs / rhythm / red lines). Not "reference material"; it *is* the generation engine. Edit this to change how scripts are written. |
| `user_profile.md` | **Human-maintained, agent-read** | Target audience and content preferences. You edit it; the agent consults it every run. |
| `examples/script_example.md` | **Reference, agent-read** | An example of the desired finished-script shape. |

> In one line: **README is for humans, `SKILL.md` is for the agent.** `script_rules.md` is the core engine; `user_profile.md` and `examples/` are shared data — maintained by humans, read by the agent.

---

## What it does

The skill works in two stages:

1. **Propose 10 topic candidates** distilled from your background material (transcripts, theme analyses, competitor notes, content direction) plus a maintained audience profile.
2. **Write the full script** for the one you pick.

It produces only the script text. TTS, mixing, BGM/SFX file production, and audio post are handled by a separate engineering backend and are out of scope.

---

## Contents

This repository's **root is the skill package itself** — `SKILL.md` lives at the top level, not inside a wrapper folder. The skill name, the repo name, and the clone folder name are all the same: `sleepcast-scripts-cook` (the name comes from the `name` field in `SKILL.md`). So cloning gives a folder that is already named correctly for installation.

```
sleepcast-scripts-cook/                 # repo root = skill package = clone dir
  README.md                             # human docs, English (this file)
  README.zh.md                          # human docs, Chinese
  SKILL.md                              # agent instructions: trigger metadata + two-stage workflow
  script_rules.md                       # CORE: single source of truth for script rules
  user_profile.md                       # editable target-audience / content-preference profile
  examples/
    script_example.md                   # reference example of the finished-script shape
```

The skill reads its own bundled `script_rules.md`, `user_profile.md`, and `examples/` by relative path, so the package is portable — no dependency on files elsewhere.

---

## Install

> This is a **private** repo. Configure git auth first (be a collaborator + `gh auth login` / SSH key / PAT), otherwise both clone and `npx skills add` will fail.

The skill must end up as a folder named `sleepcast-scripts-cook` inside a discovered skills directory. The two paths below serve different installers.

### A. Manual install — for a human

Clone the repo and copy it straight into a skills directory — the clone folder is already named `sleepcast-scripts-cook`, so no rename is needed:

```bash
git clone https://github.com/ZimaBlue1226/sleepcast-scripts-cook.git

# personal (all projects)
cp -r sleepcast-scripts-cook ~/.claude/skills/

# or project-level
cp -r sleepcast-scripts-cook <your-project>/.claude/skills/
```

(You may symlink instead of copy if you want edits in the clone to take effect live.)

### B. Automated install — for an agent

The cross-agent installer detects the root-level `SKILL.md` and installs the skill under its frontmatter `name` (`sleepcast-scripts-cook`):

```bash
npx skills add https://github.com/ZimaBlue1226/sleepcast-scripts-cook
```

> Same private-repo caveat applies: `npx skills add` relies on your local git credentials, so you must already be authenticated to the private repo.

If you are an agent installing this skill manually instead, follow these directives:

- This is a **self-contained skill** and the **repo root is the skill** — place the repo's contents into a `sleepcast-scripts-cook/` directory in the target agent's skills directory (Claude Code: `~/.claude/skills/` or `<project>/.claude/skills/`).
- The entry point is `SKILL.md`. There is **no build step** and no runtime dependencies beyond reading local files.
- Keep `SKILL.md`, `script_rules.md`, `user_profile.md`, and `examples/` **together** — never split them apart; the skill reads them by relative path.
- Do **not** read `README.md` / `README.zh.md` to operate the skill — they are human documentation. Operate only from `SKILL.md`.

---

## Usage

Invoke the skill and provide this run's material — paste free text, give one or more local file paths, point at reference scripts/videos or competitor material, or provide nothing extra (the audience profile carries the run). Material is ad-hoc and per-run; you never need to add it into the skill package.

1. The skill reads your material, **tells you what it understood, and waits for you to confirm** before generating anything.
2. The skill presents **10 topic candidates** (English titles + Chinese explanations). Pick one.
3. Optionally specify:
   - script reference duration (default **`30min`**)
   - opening BGM solo lead-in (default **`8s`**)
4. The skill writes the full English script to `output/<YYYY-MM-DD>-<slug>.md`.

> The current version requires the 10-choose-1 flow; you cannot skip topic selection and name a theme directly.

---

## Customizing

Edit `user_profile.md` to adjust the target audience and content preferences — the skill consults it on every run, so you don't re-enter this each time.

Script style, structure, markup rules, and content red lines live in `script_rules.md` — the core of the skill. To change how scripts are written, edit that file; it is the single source of truth. After editing any file, re-push the repo so installs stay in sync.
