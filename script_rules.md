# Shared production and delivery rules

These rules apply to both categories. Category-specific writing lives in `references/*-script-rules.md`; this file defines the shared production specification and final file format. Examples do not override rules.

## Production specification

- Target approximately thirty minutes of English narration within forty-five minutes of BGM, including the subsequent background-only extension.
- Line 1 is `[BGM_START:concrete producible English ambience description:0.14]`. Line 2 is `[BGM_DURATION:45MIN]`. Line 3 is blank. Line 4 is `<break time="4s"/>`. Part 0 follows this opening lead-in.
- Use each label exactly once, on its own line, in this order: `[PART 0: Opening]`, `[PART 1: Wind Down]`, `[PART 2: Arrival]`, `[PART 3: Environmental Immersion]`, `[PART 4: Attention Anchors]`, `[PART 5: Sleep Descent]`.
- Pauses use multiples of half a second. Sentence, paragraph, and Part boundaries follow the selected category's rules. A standalone inter-Part pause is separate from the preceding Part; do not also append a pause to that Part's final sentence.
- Include one BGM fade marker with a positive duration. `[BGM_FADE:25]` is the default from the production structure; the example's twenty seconds is not mandatory. End the final narration with an ellipsis.
- Thirty minutes refers to narration, not a duration inferred from `[BGM_DURATION:45MIN]`. The BGM marker does not prove audio has been produced.
- English sentences have at most eighteen words. Keep short sentences natural and complete, allowing sensory fragments where the category rules permit them. Do not manufacture length through chopped sentences or mechanical repetition.
- Mechanical compliance is insufficient: preserve natural North American adult listening comprehension, the core experience, safety, and coherent world and spatial relationships.

## Final delivery

Deliver only one UTF-8 Markdown file. Use these Chinese section labels for the operator. Each code block contains one complete script with no line numbers, commentary, internal headings, review conclusions, or theme outline:

````markdown
# 英文脚本

```text
[BGM_START:English ambience description:0.14]
[BGM_DURATION:45MIN]

<break time="4s"/>

COMPLETE ENGLISH PARTS 0–5
```

# 中文对照

```text
[BGM_START:Chinese translation of the same ambience description:0.14]
[BGM_DURATION:45MIN]

<break time="4s"/>

COMPLETE CHINESE PARTS 0–5, WITH ENGLISH PART LABELS
```
````

Replace the illustrative placeholders with the full scripts. Translate the BGM description in the Chinese block; preserve all other markup, pause order, and values. Align paragraphs and narration lines one-to-one instead of independently reflowing the Chinese text.

## File placement

Use the user's explicit output file or working directory first, and follow the project's placement rules. If neither specifies placement, use `output/YYYY-MM-DD-english-theme-slug.md` under the current working directory. Use lowercase English and hyphens for the slug.

Do not overwrite an existing draft unless the user requests an in-place update; otherwise choose an unused suffix such as `-v2`. Keep theme discussion in the conversation. If execution needs intermediate files, use the designated working area or an allowed temporary directory, and clean up disposable files after delivery verification.
