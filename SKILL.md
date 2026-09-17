---
name: sleepcast-scripts-cook
description: Generate adult English SleepCast topics and bilingual scripts. Select vintage or secondary-world fantasy, develop and confirm a topic through its category-specific workflow, then deliver one Markdown file containing the complete English script and Chinese translation. Use for sleep-podcast topic development and script writing, not independent content review, TTS, or mixing.
---

# SleepCast script generator

This is a self-contained skill. Maintain its bundled instructions directly; no Feishu, MCP, external SOP, or synchronization is required. The user's explicit instructions take precedence over defaults. Examples illustrate writing, but never define or override rules.

Write execution instructions in English. Use Chinese for operator discussion, reference analysis, and topic explanations; use English working titles with Chinese explanations or translations. Final delivery contains both full English narration and its Chinese counterpart. A user-requested language takes precedence.

## 1. Select the category and gather input

- If the user has not selected a category, ask whether they want vintage settings or secondary-world fantasy, then wait before generating topics. Do not ask again when the category is already explicit.
- Treat the operator's labels "复古" and "古典" as vintage, and "第二世界幻想" and "第二幻想世界" as secondary-world fantasy. A vague setting name alone does not establish the category.
- Read [audience guidance](user_profile.md) and [shared production and delivery rules](script_rules.md).
- Vintage: read [topic development](references/classic-topics.md). Before full writing, read [vintage script rules](references/classic-script-rules.md).
- Fantasy: read [the direction definition](references/fantasy-direction.md) and execute [the topic-generation prompt](references/fantasy-topic-prompt.md). Before full writing, read [fantasy script rules](references/fantasy-script-rules.md). Do not load the other category's rules.
- Input may include pasted text, local files, distilled reference notes, an initial direction, or no additional material. Read relevant supplied files. Per-run material does not belong in the skill package.
- For substantial or ambiguous references, briefly explain your interpretation and ask about uncertainty that would change the topics. For clear inputs, summarize the extracted model and proceed without a mandatory extra confirmation turn.

## 2. Develop and confirm the topic

### Vintage

Extract the reference's content formula and follow the vintage topic-development guide. Present ten comparable candidate cards with English titles and Chinese explanations. Wait for the user's choice; discuss and revise when needed.

### Secondary-world fantasy

Execute the bundled topic-generation prompt, rather than improvising from the category name:

- No preset direction: ten complete, clearly different single-episode outlines.
- An initial direction: one complete outline, without forcing ten alternatives.
- Each outline contains a title, core fantasy, core experience, time and environment, key rules, and final resting state. Put the chronological experience development inside the core-experience field, not in a seventh required field.
- At this stage, do not write narration, script Parts, relaxation exercises, pauses, or sound design.
- Ask the user to select or confirm the outline. Your own check does not constitute approval. Apply feedback consistently across related fields.

### Entry into full writing

Write the full script after the user selects and confirms the topic. A complete theme or outline explicitly presented as already confirmed may enter writing directly. An initial idea alone is not confirmation. Do not ask for repeated confirmation or separate proof of Leader approval when the user has already authorized writing.

Keep the theme in the conversation and carry it into writing without discarding key rules or changing its identity. The outline is process data, not a final deliverable.

## 3. Assemble the writing brief and write

Prepare a working brief in context, not an extra deliverable:

1. Carry forward every substantive field of the chosen candidate or confirmed fantasy outline: the setting, experience route, sensory palette, safety basis, world rules, and final state where applicable.
2. Preserve the reference-model notes: topic type, story architecture, presentation style, sensory detail density, and sleep value. Preserve the mechanism while changing distinctive reference imagery.
3. Carry forward the chosen candidate's differentiation and any must-keep details or exclusions agreed with the user.
4. Apply relevant audience circumstances without inventing demographic facts or putting a listener's real-life problems into the story.
5. Resolve the production targets from the shared rules and choose one Wind Down technique under the category rules. Its name in Part 0 must match Part 1.

Use this brief, the shared rules, and the selected category's writing rules to produce the English script. Then translate the final English script faithfully into Chinese and proofread the translation against that English version, preserving events, spatial relationships, characters, paragraphs, narration lines, and pause structure. If the English script changes, update and recheck the corresponding Chinese translation. Do not independently rewrite the plot in translation.

When a fantasy example is useful, use only [The Ship at Twilight in English](examples/the-ship-at-twilight.en.md). Study ordinary sky travel, changing views, and gradual descent in attention. Do not reuse its ship name, core fantasy, or distinctive scenery as a new theme. It contains earlier phrasing, Part-ending pauses, and weak-question differences; it is not a fully compliant reference.

For vintage illustration, [the existing sample](examples/script_example.md) shows sensory development. It does not override current rules or authorize copying distinctive details.

## 4. Check and deliver

Check the completeness and format of this generation. Do not create an independent review report or invoke a review-and-rewrite loop.

1. Compare the script with the confirmed brief: core experience, world rules, listener viewpoint, Part functions, and declining information density. Vintage Part 4 avoids historical or causal questions; fantasy Part 4 develops the core fantasy through three to five connected units.
2. Check markup, sentence length, pauses, and bilingual structure. The optional `scripts/check_script.py FILE` verifies a limited set of deterministic format properties, not semantic quality.
3. Read [the duration reference](references/duration-reference.md). Count current English words and explicit pauses. Use newer measured user data when available; otherwise use the bundled empirical range. For a net reading rate, add explicit pauses; do not add them again to an all-in rate. Compare scripts on the same basis, never by adjusting the assumed rate to force a thirty-minute result. Expand the core experience and sensory depth when clearly short; trim repetition when clearly long. Actual narration duration requires TTS verification. About 380–400 lines is advisory, not a quota; do not add blank lines, fragment sentences, or stretch pauses to reach it.
4. Save one bilingual Markdown file using the shared delivery rules and verify the saved content. Fix clear formatting errors or translation omissions and recheck the affected result.
5. Reply briefly with the file link, category, theme, selected technique, duration estimate, and its unverified TTS limitation. Do not add separate theme, review, or production-note files to the final delivery.
