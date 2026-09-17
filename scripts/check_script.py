"""Check a bilingual SleepCast Markdown deliverable using only Python's standard library.

Usage: python scripts/check_script.py episode.md [--wpm NET_READING_WORDS_PER_MINUTE]
No TTS or semantic quality claims. Exit 1 means deterministic format errors.
"""
import argparse
import json
import re
from pathlib import Path

PARTS = ['Opening', 'Wind Down', 'Arrival', 'Environmental Immersion', 'Attention Anchors', 'Sleep Descent']
BREAK = r'<break time="(\d+(?:\.\d+)?)s"/>'
WORD = r"[A-Za-z]+(?:['’\-][A-Za-z]+)*"

def inspect(text):
    errors = []
    blocks = re.findall(r'^```(?:text|xml)?\s*\n(.*?)^```\s*$', text, re.M | re.S)
    if len(blocks) != 2:
        return {'errors': ['Deliverable must contain exactly two fenced script blocks: EN then ZH.']}
    en, zh = blocks
    expected = [f'[PART {i}: {title}]' for i, title in enumerate(PARTS)]
    for language, script in [('EN', en), ('ZH', zh)]:
        lines = script.splitlines()
        if len(lines) < 4 or not re.fullmatch(r'\[BGM_START:.+:0\.14\]', lines[0]):
            errors.append(f'{language}: invalid BGM_START.')
        if len(lines) < 4 or lines[1:4] != ['[BGM_DURATION:45MIN]', '', '<break time="4s"/>']:
            errors.append(f'{language}: opening must use 45MIN and 4s on line 4.')
        tags = re.findall(r'^\[PART[^\n]*\]$', script, re.M)
        if tags != expected:
            errors.append(f'{language}: Part labels/order invalid.')
        without_known = re.sub(BREAK, '', script)
        without_known = re.sub(r'^\[(?:BGM_START:.+|BGM_DURATION:45MIN|BGM_FADE:\d+(?:\.\d+)?|PART \d: [^\]]+)\]$', '', without_known, flags=re.M)
        if re.search(r'[<>\[\]]|^\s*#', without_known, re.M):
            errors.append(f'{language}: unknown markup or explanatory heading inside script.')
        values = [float(x) for x in re.findall(BREAK, script)]
        if any(v <= 0 or not (v * 2).is_integer() for v in values):
            errors.append(f'{language}: pauses must be positive multiples of 0.5s.')
        if re.search(BREAK + r'\s*' + BREAK, script):
            errors.append(f'{language}: stacked pauses.')
        fade = re.findall(r'\[BGM_FADE:(\d+(?:\.\d+)?)\]', script)
        if len(fade) != 1 or float(fade[0]) <= 0:
            errors.append(f'{language}: one positive BGM_FADE required.')
        prose = re.sub(BREAK, '', script)
        prose = re.sub(r'^\[.*\]\s*$', '', prose, flags=re.M).strip()
        if not prose.endswith(('...', '…')):
            errors.append(f'{language}: final narration must end in an ellipsis.')
        if language == 'EN' and re.search(r'[\u4e00-\u9fff]', script):
            errors.append('EN: Chinese text inside English script.')
        sections = re.split(r'^\[PART \d: [^\]]+\]\s*\n', script, flags=re.M)[1:]
        for idx, section in enumerate(sections):
            section = re.sub(r'^\[BGM_FADE:[^\]]+\]\s*$', '', section, flags=re.M).strip()
            if idx < 5:
                boundary = re.search(r'\n\s*<break time="([78](?:\.0)?)s"/>\s*$', section)
                if not boundary:
                    errors.append(f'{language} Part {idx}: missing standalone 7–8s boundary.')
                else:
                    section = section[:boundary.start()].rstrip()
            if re.search(BREAK + r'\s*$', section):
                errors.append(f'{language} Part {idx}: final narration has extra trailing pause.')
            if language == 'EN':
                for sentence in re.split(r'[.!?]+', re.sub(BREAK, ' ', section)):
                    count = len(re.findall(WORD, sentence))
                    if count > 18:
                        errors.append(f'EN Part {idx}: sentence has {count} words: {sentence.strip()[:90]}')
    def markup(script):
        normalized = re.sub(r'\[BGM_START:.*\]', '[BGM_START:TRANSLATED:0.14]', script)
        return re.findall(r'\[[^\]]+\]|<break[^>]+>', normalized)
    if markup(en) != markup(zh):
        errors.append('EN/ZH: markup sequence differs.')
    if len(en.splitlines()) != len(zh.splitlines()):
        errors.append('EN/ZH: line structure differs.')
    en_prose = re.sub(r'^\[.*\]\s*$', '', re.sub(BREAK, '', en), flags=re.M)
    words = len(re.findall(WORD, en_prose))
    return {'errors': errors, 'english_words': words, 'english_lines': len(en.splitlines()),
            'explicit_pause_seconds': sum(float(v) for v in re.findall(BREAK, en)),
            'limits': 'Checks format only. Line count is advisory. Content, translation meaning and actual TTS duration require separate verification.'}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('file', type=Path)
    parser.add_argument('--wpm', type=float, help='Assumed net spoken words/minute, excluding explicit pauses')
    args = parser.parse_args()
    if args.wpm is not None and args.wpm <= 0:
        parser.error('--wpm must be positive')
    result = inspect(args.file.read_text(encoding='utf-8-sig'))
    if args.wpm and 'english_words' in result:
        result['duration_estimate'] = {'assumed_net_wpm': args.wpm, 'minutes': round(result['english_words'] / args.wpm + result['explicit_pause_seconds'] / 60, 2), 'actual_tts_verified': False}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(bool(result['errors']))

if __name__ == '__main__':
    main()
