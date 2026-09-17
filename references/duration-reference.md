# Empirical narration-duration reference

The target remains approximately thirty minutes of narration within forty-five minutes of finished audio. The earlier finished episode below provides an estimate, not a replacement target or a TTS speed setting.

## Finished reference

The user identified The Ship at Twilight as the reference. Its audio production record gives:

| Item | Female voice | Male voice |
|---|---|---|
| Narration duration | About 25 minutes | About 26 minutes |
| Voice | Lora | Spuds Oxley |
| Model | eleven_multilingual_v2 | eleven_multilingual_v2 |
| Speed / Stability / Similarity | 1 / 65% / 75% | 1 / 85% / 60% |

The bundled English example contains 1,860 English words and 638 seconds of explicit pauses, including the four-second opening and inter-Part pauses. Count contractions and hyphenated words as one word and exclude engineering markup.

Assuming the bundled script corresponds to the recorded audio and all marked pauses were rendered:

`net words per minute = 1860 / (recorded narration minutes - 638 / 60)`

- Female voice: approximately 129.5 net words per minute.
- Male voice: approximately 121 net words per minute.

## Application and limits

Without newer voice calibration, estimate over approximately 121–129.5 net words per minute. Use 125 as a common planning value within the range, explicitly labeled as an empirical estimate. Use the current script's word count and pauses, not the reference's 638 seconds.

`estimated narration minutes = current English words / net words per minute + current explicit pause seconds / 60`

The production record gives approximate durations, not waveform measurements of the narration endpoint. It does not specify whether the opening four seconds are included. Prosody, punctuation, sentence structure, and backend pause handling may change the result. Decimal calculations do not imply measurement precision. Recalibrate for another voice or model.

This reference works locally without network access. If the user edits the bundled example or provides updated finished-audio measurements, recount and update the empirical data. Do not infer new production rules from unrelated historical scripts.
