# sleepcast-script

A self-contained Claude Code / Agent skill that generates **English adult-sleep SleepCast scripts** for [VelaSleep](https://github.com/) — TTS-ready narration in the style of a native sleep story / sleep podcast.

The skill works in two stages:

1. **Propose 10 topic candidates** distilled from your background material (transcripts, theme analyses, competitor notes, content direction) plus a maintained audience profile.
2. **Write the full script** for the one you pick.

It produces only the script text. TTS, mixing, BGM/SFX file production, and audio post are handled by a separate engineering backend and are out of scope.

## Contents

```
sleepcast-script/
  SKILL.md                              # trigger metadata + two-stage workflow
  user_profile.md                       # editable target-audience / content-preference profile
  references/
    sleepcast_script_prompt.md          # single source of truth for script rules
    script_example.md                   # reference for the finished-script shape
```

The skill reads its own bundled `references/` copies, so the package is portable — no dependency on files elsewhere in the repo.

## Install

The skill is a standard self-contained skill folder. Install it into any agent that supports skills.

**Claude Code** — copy or symlink into a discovered skills directory:

```bash
# personal (all projects)
cp -r sleepcast-script ~/.claude/skills/

# or project-level
cp -r sleepcast-script <your-project>/.claude/skills/
```

**Cross-agent installer** (Claude Code, Codex, etc.), once published to GitHub:

```bash
npx skills add <github-repo-url>
```

## Usage

Invoke the skill and provide this run's background material — free text, local file paths, reference scripts/videos, competitor material, audience comments, or a content direction.

1. The skill presents **10 topic candidates** (English titles + Chinese explanations). Pick one.
2. Optionally specify:
   - script reference duration (default **`30min`**)
   - opening BGM solo lead-in (default **`8s`**)
3. The skill writes the full English script to `output/<YYYY-MM-DD>-<slug>.md`.

> The current version requires the 10-choose-1 flow; you cannot skip topic selection and name a theme directly.

## Customizing

Edit `user_profile.md` to adjust the target audience and content preferences — the skill consults it on every run, so you don't re-enter this each time.

Script style, structure, markup rules, and content red lines live in `references/sleepcast_script_prompt.md`. To change how scripts are written, edit that file — it is the single source of truth.
