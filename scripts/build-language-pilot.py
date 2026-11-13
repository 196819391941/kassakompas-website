# Compatibility entry point: the pilot has expanded to the complete website.
from runpy import run_path
from pathlib import Path
run_path(str(Path(__file__).with_name('build-i18n.py')),run_name='__main__')
