"""Shared helpers for the Real Station Inventory build (name normalization, DMS parsing, distance, loaders)."""
import os, re, json, csv, math, unicodedata
RAW = os.environ.get('RAW', './raw')

def haversine(a, b):
    if None in a or None in b: return None
    R = 6371.0088
    p1, p2 = math.radians(a[0]), math.radians(b[0])
    dp = p2 - p1; dl = math.radians(b[1] - a[1])
    h = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * R * math.asin(min(1, math.sqrt(h)))

def fold(s):
    s = unicodedata.normalize('NFKD', s or '')
    return ''.join(c for c in s if not unicodedata.combining(c))

STOP = set('station stations base bases antarctic antartic antarctica research scientific science camp refuge refugio refuges hut huts laboratory lab the of de del la las los el and y en estacion cientifica polar skiway runway airfield airstrip aerodrome airport aerial airbase field facility summer winter stazione zhan bazo base. naval antartica antartida general capitan capitán teniente comandante presidente profesor professor doctor dr mount cape punta point island isla'.split())
SYN = {'showa': 'syowa', 'molodyozhnaya': 'molodezhnaya', 'molodezhnaja': 'molodezhnaya', 'molodjozhnaja': 'molodezhnaya', 'novolazarevskaja': 'novolazarevskaya', 'novolazarevskaya': 'novolazarevskaya',
       'mirnyj': 'mirny', 'bellingsauzen': 'bellingshausen', 'bellingshausen': 'bellingshausen', 'dumont': 'dumont', 'durville': 'durville', 'changcheng': 'greatwall', 'great': 'greatwall', 'wall': '',
       'jubany': 'carlini', 'decepcion': 'deception', 'camara': 'camara', 'oazis': 'oasis', 'oasis': 'oasis', 'vechernyaya': 'vechernyaya', 'evening': 'vechernyaya', 'mountain': '',
       'ohiggins': 'ohiggins', 'vostok': 'vostok', 'zhongshan': 'zhongshan', 'kunlun': 'kunlun', 'macchu': 'machu', 'ferraz': 'ferraz', 'druzhnaja': 'druzhnaya', 'drushnaya': 'druzhnaya', 'drúzhnaya': 'druzhnaya',
       'roi': 'baudouin', 'koenig': 'baudouin', 'king': 'king', 'neumayer': 'neumayer', 'georg': 'georg', 'esperanza': 'esperanza', 'elichiribehety': 'elichiribehety', 'rupierto': 'elichiribehety', 'ruperto': 'elichiribehety',
       'ohridski': 'ohridski', 'comandante': '', 'ferraz': 'ferraz', 'mario': 'zucchelli', 'zucchelli': 'zucchelli', 'arctowski': 'arctowski', 'henryk': 'arctowski', 'mawson': 'mawson', 'sanae': 'sanae', 'troll': 'troll'}
ROMAN = {'i', 'ii', 'iii', 'iv', 'v', 'vi', 'vii'}

RMAP = {'i': '1', 'ii': '2', 'iii': '3', 'iv': '4', 'v': '5', 'vi': '6', 'vii': '7'}
def tokens(name):
    s = fold(name).lower()
    s = re.sub(r"\(.*?\)", ' ', s)
    s = re.sub(r"/[^/]*/", ' ', s)
    s = re.sub(r"[^a-z0-9]+", ' ', s)
    s = re.sub(r'\b([a-z]) (\d+)\b', r'\1\2', s)
    out = []
    for t in s.split():
        t = SYN.get(t, t)
        if not t or t in STOP: continue
        t = RMAP.get(t, t)
        out.append(t)
    return out

def is_num(t): return t.isdigit() or (len(t) == 1 and t.isalpha())

def name_score(a, b):
    A, B = set(tokens(a)), set(tokens(b))
    if not A or not B: return 0.0
    if A == B: return 1.0
    inter = A & B
    if not {t for t in inter if not is_num(t)}: return 0.0
    na = {t for t in A if is_num(t)}; nb = {t for t in B if is_num(t)}
    if na and nb and na != nb: return 0.0
    sc = len(inter) / min(len(A), len(B))
    if bool(na) != bool(nb): sc *= 0.6
    return sc

DMS_RE = re.compile(r"(\d{1,3})\s*°\s*(?:(\d{1,2}(?:\.\d+)?)\s*['’‘`´′]?)?\s*(?:(\d{1,2}(?:\.\d+)?)\s*(?:['’‘`´′\"”″]\s*)*)?\s*([NSEW])", re.I)
def parse_dms_pair(txt):
    """returns (lat, lon, flags) from strings like 77°52’26’’S 34°37’40’’W"""
    t = txt.replace("''", '"').replace('’’', '"').replace('‘‘', '"').replace('”', '"')
    vals = []
    flags = []
    for m in DMS_RE.finditer(t):
        d = float(m.group(1)); mi = float(m.group(2) or 0); se = float(m.group(3) or 0)
        if mi >= 60 or se >= 60: flags.append('minutes/seconds >=60 in source string')
        v = d + mi / 60 + se / 3600
        if m.group(4).upper() in 'SW': v = -v
        vals.append(v)
    if len(vals) >= 2: return vals[0], vals[1], flags
    return None, None, ['unparsed']

def slug(s):
    s = fold(s).lower()
    s = re.sub(r"[^a-z0-9]+", '-', s).strip('-')
    return s[:60]

def yr(s):
    m = re.search(r'(1[6-9]\d\d|20\d\d)', s or '')
    return m.group(1) if m else ''
