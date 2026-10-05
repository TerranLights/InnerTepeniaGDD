"""Re-render the whole Tepenia map series. Run after ANY change to data/*.csv.

  python3 render_all.py            # archive the previous out/ (if any), then render all five maps
Safety: the previous outputs are moved into archive/<timestamp>/ first - never overwritten in place
(lesson from the Russia map series: always archive before overwriting).
"""
import shutil, subprocess, sys, time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = ROOT / 'out'
if not (ROOT / 'data' / 'base' / 'land.geojson').exists():
    subprocess.check_call(['bash', str(HERE / 'fetch_base_data.sh')]); subprocess.check_call([sys.executable, str(HERE / 'prepare_base_data.py')])
if not (ROOT / 'data' / 'highway_geometry.csv').exists():
    subprocess.check_call([sys.executable, str(HERE / 'build_geometry.py'), '--rebuild'])
if OUT.exists() and any(OUT.iterdir()):
    arch = ROOT / 'archive' / time.strftime('%Y-%m-%d_%H%M'); arch.mkdir(parents=True, exist_ok=True)
    for f in OUT.iterdir(): shutil.move(str(f), str(arch / f.name))
    print('archived previous outputs to', arch)
for s in sorted(HERE.glob('render_[0-9]*.py')):
    print('->', s.name); subprocess.check_call([sys.executable, str(s)], cwd=HERE)
