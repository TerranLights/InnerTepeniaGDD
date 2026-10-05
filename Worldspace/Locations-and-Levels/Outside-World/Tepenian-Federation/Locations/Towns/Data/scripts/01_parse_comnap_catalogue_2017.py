#!/usr/bin/env python3
"""Parse the COMNAP Antarctic Station Catalog (Aug 2017 PDF) into JSON.
Input : RAW/comnap_catalogue.pdf  (https://www.comnap.aq/s/COMNAP_Antarctic_Station_Catalogue.pdf)
Output: RAW/comnap_catalogue_parsed.json
One station per PDF page (index 9..84). Station name/operator/DMS coordinates are read from the page itself
(the block holding the coordinate string, and the block just above it).
RAW defaults to the session scratchpad; override with env RAW.
"""
import os, re, json
import pymupdf
RAW = os.environ.get('RAW', './raw')
doc = pymupdf.open(os.path.join(RAW, 'comnap_catalogue.pdf'))

def clean(s): return ' '.join(s.split())

def below(blocks, label, maxgap=30):
    """text of the block directly under the block that starts with `label` (same column)"""
    for b in blocks:
        if b[4].strip().startswith(label):
            body = b[4].strip()[len(label):].strip()
            if body: return clean(body)
            c = [x for x in blocks if abs(x[0]-b[0]) < 10 and x[1] >= b[3]-2 and x[1]-b[3] < maxgap and x is not b]
            if c: return clean(min(c, key=lambda x: x[1])[4])
    return 'unknown'

def num_after(text, label):
    m = re.search(re.escape(label) + r'[^\n]*\n(?:[^\n]*\)\s*\n)?\s*([0-9][0-9,\.]*)\s*\n', text)
    return m.group(1) if m else 'unknown'

out = []
for pg in range(9, 85):
    page = doc[pg]
    blocks = page.get_text('blocks')
    text = '\n'.join(b[4] for b in blocks)
    rec = dict(pdf_index=pg)
    coord = [b for b in blocks if re.match(r'^\s*\d+°', b[4]) and b[0] < 100]
    if coord:
        cb = coord[0]
        rec['coord_dms'] = clean(cb[4])
        above = [b for b in blocks if b[0] < 100 and b[3] <= cb[1]+2 and cb[1]-b[3] < 60 and b is not cb]
        if above:
            nb = max(above, key=lambda b: b[1])
            rec['name_operator_line'] = clean(nb[4])
    m = re.search(r'Type:\s*([^\n]+)', text); rec['type'] = clean(m.group(1)) if m else 'unknown'
    m = re.search(r'Operational period:\s*\n?\s*([^\n]+)', text); rec['operational_period'] = clean(m.group(1)) if m else 'unknown'
    m = re.search(r'\nLocation\s*\n(.*?)\n(?:Biodiversity|History and)', text, re.S)
    rec['location_text'] = clean(m.group(1)) if m else 'unknown'
    rec['history_text'] = below(blocks, 'History and facilities')
    for lab, key in [('Type of surface facility built on', 'surface_type'), ('Altitude of facility (m)', 'altitude_m'),
                     ('Permafrost', 'permafrost'), ('Climate zone', 'climate_zone'), ('Number of beds', 'beds'),
                     ('Number of staff on station (peak/summer season)', 'staff_summer'),
                     ('Number of staff on station (off peak/winter season)', 'staff_winter'),
                     ('Area under roof (m2)', 'area_under_roof_m2'),
                     ('Mean annual temperature (°C)', 'mean_annual_temp_c')]:
        m = re.search(re.escape(lab) + r'[ \t]*\n[ \t]*([^\n]*)', text)
        v = clean(m.group(1)) if m else ''
        if key in ('altitude_m', 'beds', 'staff_summer', 'staff_winter', 'area_under_roof_m2', 'mean_annual_temp_c'):
            v = v if re.fullmatch(r'-?[0-9][0-9,\.]*', v) else 'unknown'
        rec[key] = v if v else 'unknown'
    rec['features'] = below(blocks, 'Features in the facility area')
    rec['disciplines'] = below(blocks, 'Main science disciplines')
    mp = 'unknown'
    for b in blocks:
        if b[4].strip().startswith('Max number of personnel'):
            m2 = re.search(r'\)\s*\n\s*(\d+)', b[4])
            if m2: mp = m2.group(1)
            else:
                c = [x for x in blocks if re.fullmatch(r'\d+\s*', x[4]) and abs(x[1]-b[1]) < 14 and x[0] > b[0]]
                if c: mp = c[0][4].strip()
    rec['max_personnel'] = mp
    out.append(rec)
json.dump(out, open(os.path.join(RAW, 'comnap_catalogue_parsed.json'), 'w'), indent=1, ensure_ascii=False)
for r in out: print(r['pdf_index'], '|', r.get('name_operator_line'), '|', r.get('coord_dms'), '|', r['type'], '|', r['operational_period'], '|', r['surface_type'], '|', r['altitude_m'], r['beds'], r['staff_summer'], r['staff_winter'], r['max_personnel'])
