# sleepcast-scripts-cook

A self-contained adult SleepCast writing skill with two categories: vintage settings and secondary-world fantasy. It develops topics, waits for the user's selection or confirmation, then delivers one Markdown file containing the full English script and its Chinese counterpart.

No Feishu, MCP, external SOP or synchronization is required. Maintain the bundled files directly. Changes are not automatically committed or pushed.

## Use

Execution instructions are in English. Operator discussion and topic explanations default to Chinese; final scripts remain bilingual. Reference analysis extracts the underlying content formula, vintage candidates use comparable cards, and the selected details carry into a working brief before writing. Audience circumstances are creative guidance, not verified demographic claims.

Invoke the skill with a category and any reference material or initial direction. It asks for the category only when none has been selected.

- Vintage: ten topic candidates, then user selection and writing.
- Fantasy: ten complete outlines without a preset direction, or one outline for a supplied direction; writing begins after confirmation.
- A complete, explicitly confirmed theme can enter writing directly.
- Outlines remain in the conversation. The final file contains only the English and Chinese scripts, each in its own code block.

The default production target is approximately thirty minutes of narration within forty-five minutes of BGM, with a four-second opening. Line count is advisory. Actual narration duration must be verified after synthesis.

## Install and maintain

Place the complete `sleepcast-scripts-cook` folder in your agent's skills directory. Keep all bundled paths together. Existing private-repository distribution can still be used, but local changes do not update the remote repository.

`SKILL.md` controls routing and interaction. `script_rules.md` defines shared production and delivery requirements. `user_profile.md` contains audience guidance. The category-specific topic and writing rules live in `references/`. Examples illustrate writing and never override rules; the fantasy example is The Ship at Twilight.

Optional format validation uses Python 3 with no third-party dependencies:

```sh
python scripts/check_script.py episode.md
python scripts/check_script.py episode.md --wpm 125
```

The optional speed is a net reading rate, excluding pauses. The bundled `references/duration-reference.md` derives an approximate 121–129.5 words/minute range from The Ship at Twilight's recorded narration durations; 125 is a planning value within that range. This check does not validate semantic quality, translation fidelity or the new script's actual TTS duration.

Independent content review, TTS, sound production, mixing and publishing remain outside this skill.
