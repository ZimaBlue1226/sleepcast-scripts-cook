---
name: sleepcast-scripts-cook
description: Generate an English adult-sleep SleepCast script (sleep-audio narration / sleep story / sleep podcast) for VelaSleep. Use when the user wants to create, write, or draft a SleepCast script, or asks for sleep-audio narration topics. The skill first proposes 10 topic candidates from the user's background material and a maintained audience profile, then — after the user picks one — writes a full TTS-ready English script. It does NOT do TTS, mixing, BGM/SFX production, or audio post.
---

# SleepCast Script Generator

Generate English SleepCast scripts for VelaSleep adult-sleep audio, in two stages:
**(1) propose 10 topic candidates → (2) the user picks one → write the full script.**

This skill ONLY produces the script text. TTS, mixing, BGM/SFX file production, and audio post are handled by a separate engineering backend and are out of scope.

## Files in this skill package

- `user_profile.md` — the target audience and content-preference profile. Always consult it. The user may edit it freely.
- `references/sleepcast_script_prompt.md` — the **single source of truth** for script rules (markup, PART structure, rhythm, content red lines). Always follow it exactly in Stage 2.
- `references/script_example.md` — the reference for the desired finished-script shape.

Read these from this package, not from elsewhere.

---

## Stage 0 · Prepare

1. Read `user_profile.md`, `references/sleepcast_script_prompt.md`, and `references/script_example.md` from this package.
2. Gather the user's input for this run. It may include: free-text direction typed in the client, local file paths, reference videos/scripts, competitor material, audience comments, or a content direction note.
3. **Parse the provided material deeply** — including verbatim transcripts (逐字稿) and topic/theme analyses (题材分析). These are a primary source for both topic selection and concrete script detail. Do not ignore them; mine them for specific imagery, settings, sensory cues, and differentiation angles.

If the user gave no material at all, ask once for the background/direction before proceeding.

---

## Stage 1 · Propose 10 topic candidates

Synthesize `user_profile.md` + this run's material into **exactly 10** candidate topics. Each candidate is a *distillation* of the material, and every field exists to feed later script detail.

Present them as a numbered list. Use **English titles + Chinese explanations** so a Chinese-speaking operator can quickly pick 1 of 10.

Each candidate card uses these fields:

| 字段 | 语言 | 说明 |
|---|---|---|
| `No.` | — | 1–10 |
| `Title` | EN | English working title (this is the content title itself) |
| `Hook` | EN | One-line hook that sets the mood |
| `场景概述` | 中 | 空间 / 时间 / 天气；为何低刺激、无任务 |
| `感官调色板` | 中 | 主导感官锚点：声 / 光 / 嗅 / 触 / 温 |
| `适配理由` | 中 | 为何对北美高唤起睡前人群有效（降唤醒机制） |
| `差异化` | 中 | 与已知竞品（如 Headspace *Rainday Antiques*）的区别或新鲜度 |

Rules:
- Produce **10** distinct candidates with varied settings/sensory palettes — avoid clustering on one motif.
- The current version requires the 10-choose-1 flow. **Do not let the user skip topic selection and name a theme directly.** If they try, still present 10 candidates (you may seed them with the user's direction).
- After presenting, **stop and wait** for the user to choose one.

---

## Stage 2 · Generate the full script

Triggered only after the user confirms 1 of the 10 candidates.

### 2.1 Resolve parameters

- 脚本参考时长 (reference duration): if the user did not specify, default **`30min`**.
- 开头 BGM 单独铺底时长 (opening BGM solo lead-in): if the user did not specify, default **`8s`**.

### 2.2 Assemble the generation brief

Build a structured brief that becomes the direct input to script generation:

1. **All fields of the chosen topic card** — 场景概述 / 感官调色板 / 差异化 become seed material for PART 2 / 3 / 4, so the script never starts from zero.
2. **Resolved parameters** — reference duration and opening BGM lead-in.
3. **Relevant audience constraints** pulled from `user_profile.md`.
4. **Specific detail excerpts** from this run's material that fit this topic (e.g. concrete imagery from a transcript).
5. **The Wind Down technique** for this script: randomly and uniquely pick **one** of — noting / body scan / breath counting / gravity body / weighted breath — and record it in the brief. Vary it across runs; do not default to the same one.

### 2.3 Write the script

- Follow **every** rule in `references/sleepcast_script_prompt.md` exactly: the audio markup system, the 6 PARTs (0–5), the rhythm arc, sentence-length limits, pause rules, and the forbidden-element list.
- Match the finished-script shape of `references/script_example.md`.
- Honor the opening-audio rule: emit `[BGM_START:…]` and `[BGM_DURATION:…]`, then a line-of-its-own `<break time="8s"/>` (use the resolved BGM lead-in value), then `[PART 0: Opening]` and the narration.
- The Wind Down technique named in PART 0 must match the actual practice in PART 1, and must be the one chosen in the brief.

### 2.4 Output

- Output the script as **English plain text** (NOT JSON), containing only the audio/BGM/SFX/PART tags and narration — no explanations, commentary, creator notes, Chinese annotations, or Markdown headings inside the script (per the prompt's output constraints).
- Write the script to `output/<YYYY-MM-DD>-<slug>.md` relative to the current working directory (`<slug>` derived from the chosen English title). Create `output/` if needed.
- In the chat, give a brief confirmation: file path, chosen topic, resolved duration / BGM lead-in, and the Wind Down technique used. Keep this confirmation OUTSIDE the script file.

---

## Scope boundary

This skill goes from background material → 10 candidates → full SleepCast script, and nothing further. TTS, mixing, BGM/SFX file production, audio export, and QA are handled by a separate engineering backend.
