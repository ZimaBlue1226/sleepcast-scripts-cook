---
name: sleepcast-scripts-cook
description: Generate an English adult-sleep SleepCast script (sleep-audio narration / sleep story / sleep podcast) for VelaSleep. Use when the user wants to create, write, or draft a SleepCast script, or asks for sleep-audio narration topics. The skill first proposes 10 original lookalike topic candidates by extracting the transferable topic formula, story architecture, presentation style, and sleep value from the user's reference material and the maintained audience profile; after the user picks one, it writes a full TTS-ready English script. It does NOT do TTS, mixing, BGM production, or audio post.
---

# SleepCast Script Generator

Generate English SleepCast scripts for VelaSleep adult-sleep audio, in two stages:
**(1) propose 10 topic candidates → (2) the user picks one → write the full script.**

This skill ONLY produces the script text. TTS, mixing, BGM file production, and audio post are handled by a separate engineering backend and are out of scope.

## Files in this skill package

- `script_rules.md` — **the core of this skill.** The single source of truth for how scripts are written: the audio markup system, the 6 PARTs (0–5), the rhythm arc, sentence-length and pause rules, and the content red lines. This is not "reference material" — it *is* the generation engine. Follow it exactly in Stage 2.
- `user_profile.md` — the target audience and content-preference profile. Always consult it. The user may edit it freely.
- `examples/script_example.md` — a reference example showing the desired finished-script shape.

Read these from this package, not from elsewhere.

---

## Stage 0 · Gather input and confirm

1. Read `script_rules.md`, `user_profile.md`, and `examples/script_example.md` from this package.
2. Collect this run's material. The user may paste a block of text, give one or more local file paths, point at reference scripts/videos or competitor material, or say there's nothing extra (in which case `user_profile.md` plus the project background carry the run). This material is **ad-hoc and per-run — it never needs to be added to the skill package**; `examples/` holds only the bundled sample and is not a dropbox for user material.
3. If file paths are given, read them. **Parse the material deeply** — especially verbatim transcripts (逐字稿) and topic/theme analyses (题材分析). Treat reference scripts, competitor material, and theme analyses primarily as **model samples**: extract the transferable topic type, story architecture, presentation style, sensory strategy, sleep value, and differentiation constraints. (How those become candidates — and why specific imagery is evidence, not material to copy — is governed by Stage 1.)
4. **Confirm before proceeding.** Briefly tell the user what you took in and how you read it — which files/text, and the key imagery or direction you extracted. Then stop and wait for the user to confirm; only move on to Stage 1 once they say to continue. This gate keeps you from generating off a misread.

---

## Stage 1 · Propose 10 topic candidates

Synthesize `user_profile.md` + this run's material into **exactly 10** original lookalike topic candidates: the same content formula as the reference (topic type, story architecture, presentation style, sensory density, sleep value), but a different setting, object system, and memorable motif.

Before listing the candidates, briefly summarize the extracted reference model in Chinese:

- `选题类型`: e.g. night-open daily refuge / slow wandering scene / low-stimulation care space.
- `故事架构`: the transferable arc, such as entrance boundary → wind down → arrival → safe environment → 3-5 attention anchors → fade-out.
- `呈现风格`: pacing, social pressure level, plot intensity, character use, and narration posture.
- `感官公式`: dominant sound / light / scent / touch / temperature patterns.
- `用户价值`: why this formula helps VelaSleep's target audience downshift before sleep.

Topic abstraction rule:

- Inherit the reference's **safety-and-downshift mechanism**, not its surface props. (A flower-market reference does not make glass walls, canals, flowers, or warm lamps mandatory — those are evidence of the mechanism, not required ingredients.)
- Each candidate must be a **credible low-defensiveness space**: a believable place the listener can enter, remain in, and slowly observe without having to explain themselves, buy anything, perform, hurry, or respond socially.
- Anchor every candidate in one of three scene types, and be ready to say why the place is believable: `现实存在` (a real, widely-known place), `现实改造` (a real place put into a low-stimulation state), or `幻想自洽` (an unreal place whose objects, sounds, and access logic stay internally coherent).
- Night is only one possible low-stimulation state; a candidate's quiet may instead come from rain, early morning, off-season stillness, a travel pause, or a permitted after-hours visit.
- Before writing a candidate, test it against this formula:

```text
credible place + low-stimulation state + slow stay/wandering path + natural object system + source of safety
```

It should answer, at least implicitly: What is this place? Why is it quiet now? How may the listener enter or stay? Why do these objects belong together? What makes the space feel safe?

Present them as a numbered list. Use **English titles + Chinese explanations** so a Chinese-speaking operator can quickly pick 1 of 10.

Each candidate card uses these fields:


| 字段       | 语言  | 说明                                                                                                                                                                     |
| -------- | --- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `No.`    | —   | 1–10                                                                                                                                                                   |
| `Title`  | EN  | English working title (the content title itself). Keep it short — at most four short words, or two short words plus one longer word; avoid long prepositional phrases. |
| `Hook`   | EN  | One-line hook that sets the mood                                                                                                                                       |
| `场景成立方式` | 中   | `现实存在` / `现实改造` / `幻想自洽`；用一句话说明该场景为什么可信                                                                                                                                |
| `场景概述`   | 中   | 空间 / 时间 / 天气；为何低刺激、无任务                                                                                                                                                 |
| `感官调色板`  | 中   | 主导感官锚点：声 / 光 / 嗅 / 触 / 温                                                                                                                                               |
| `适配理由`   | 中   | 为何对北美高唤起睡前人群有效（降唤醒机制）                                                                                                                                                  |
| `参考继承点`  | 中   | 继承参考样本的哪种选题类型 / 故事架构 / 呈现风格 / 感官机制                                                                                                                                     |
| `差异化`    | 中   | 与已知竞品（如 Headspace *Rainday Antiques*）的区别或新鲜度                                                                                                                           |


Rules:

- Produce **10** distinct candidates with varied settings and sensory palettes — avoid clustering on one motif (e.g. if the reference is a night flower market, do not return ten flower-market corners).
- **Do not** build candidates by zooming into the reference's isolated props/corners, or by recombining its surface elements into a place that isn't credible. If a candidate can't explain why its place, time/state, entry path, object system, and safety source belong together, replace it — and never force soft elements together just because each is soothing.
- Keep the lookalike relationship visible: every candidate shares the reference's downshift mechanism but uses a clearly different setting, object system, and signature image.
- The current version requires the 10-choose-1 flow. **Do not let the user skip topic selection and name a theme directly.** If they try, still present 10 candidates (you may seed them with the user's direction).
- After presenting, **stop and wait** for the user to choose one.

---

## Stage 2 · Generate the full script

Triggered only after the user confirms 1 of the 10 candidates.

### 2.1 Resolve parameters

- 脚本参考时长 (reference duration): if the user did not specify, default `**30min`**.
- 开头 BGM 单独铺底时长 (opening BGM solo lead-in): if the user did not specify, default `**8s**`.

### 2.2 Assemble the generation brief

Build a structured brief that becomes the direct input to script generation:

1. **All fields of the chosen topic card** — 场景概述 / 感官调色板 / 参考继承点 / 差异化 become seed material for PART 2 / 3 / 4, so the script never starts from zero.
2. **Resolved parameters** — reference duration and opening BGM lead-in.
3. **Relevant audience constraints** pulled from `user_profile.md`.
4. **Reference-model notes and detail-density cues** from this run's material. Use them to match the reference's type, story architecture, sensory granularity, and low-stimulation presentation style. Do not transplant distinctive reference details unless the user explicitly asks for a direct adaptation.
5. **The Wind Down technique** for this script: randomly and uniquely pick **one** of — noting / body scan / breath counting / gravity body / weighted breath — and record it in the brief. Vary it across runs; do not default to the same one.

### 2.3 Write the script

- Follow **every** rule in `script_rules.md` exactly: the audio markup system, the 6 PARTs (0–5), the rhythm arc, sentence-length limits, pause rules, and the forbidden-element list.
- Match the finished-script shape of `examples/script_example.md`.
- Honor the opening-audio rule: emit `[BGM_START:…]` and `[BGM_DURATION:…]`, then a line-of-its-own `<break time="8s"/>` (use the resolved BGM lead-in value), then `[PART 0: Opening]` and the narration.
- The Wind Down technique named in PART 0 must match the actual practice in PART 1, and must be the one chosen in the brief.

### 2.4 Output

- Output the script as **English plain text** (NOT JSON), containing only the audio/BGM/PART tags and narration — no explanations, commentary, creator notes, Chinese annotations, or Markdown headings inside the script (per the prompt's output constraints).
- Write the script to `output/<YYYY-MM-DD>-<slug>.md` relative to the current working directory (`<slug>` derived from the chosen English title). Create `output/` if needed.
- In the chat, give a brief confirmation: file path, chosen topic, resolved duration / BGM lead-in, and the Wind Down technique used. Keep this confirmation OUTSIDE the script file.

---

## Scope boundary

This skill goes from background material → 10 candidates → full SleepCast script, and nothing further. TTS, mixing, BGM file production, audio export, and QA are handled by a separate engineering backend.