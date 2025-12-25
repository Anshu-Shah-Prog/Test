import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
TRANSLATIONS_PATH = os.path.join(BASE_DIR, "i18n", "translations.json")

with open(TRANSLATIONS_PATH, "r", encoding="utf-8") as f:
    TRANSLATIONS = json.load(f)


def score_numeric(qkey, option_text, lang='en'):
    if option_text is None:
        return None

    s = str(option_text).strip()

    if s.isdigit():
        return int(s)

    opts = TRANSLATIONS.get(lang, {}).get('Q', {}).get(qkey, {}).get('opts')
    if not opts:
        opts = TRANSLATIONS.get('en', {}).get('Q', {}).get(qkey, {}).get('opts')

    if isinstance(opts, list):
        try:
            return opts.index(s) + 1
        except ValueError:
            return None

    return None


def compute_scores(res, lang='en'):
    num = {k: score_numeric(k, v, lang) for k, v in res.items()}

    for req in ['B6','B7','F4','C1','C2','C3','C4','C5','C6','C7','C8','C9','C10','C12']:
        if num.get(req) is None:
            raise ValueError(f'Missing numeric mapping for {req}')

    refresh_rev = 6 - num['B6']
    difficulty_rev = 6 - num['B7']
    env_rev = 6 - num['F4']
    sleep_quality = refresh_rev + difficulty_rev + env_rev

    who_items = [num['C1'],num['C2'],num['C3'],num['C4'],num['C5']]
    who_rev = [6 - x for x in who_items]
    WHO_total = sum(who_rev) * 4

    distress_total = (
        num['C6'] + num['C7'] + num['C8'] +
        num['C9'] + num['C10'] + num['C12']
    )

    cog_items = [num.get(k, 0) for k in ['D1','D2','D3','D4','D5','D6','D7','D8']]
    cognitive_efficiency = sum(cog_items)

    lifestyle_risk = (
        (num.get('F1') or 0) +
        (num.get('F2') or 0) +
        (5 - (num.get('F3') or 0)) +
        (6 - (num.get('F4') or 0)) +
        (num.get('F5') or 0) +
        (num.get('F6') or 0)
    )

    return {
        'sleep_quality': sleep_quality,
        'WHO_total': WHO_total,
        'distress_total': distress_total,
        'cognitive_efficiency': cognitive_efficiency,
        'lifestyle_risk': lifestyle_risk
    }
