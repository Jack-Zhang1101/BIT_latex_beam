"""Compile a complete, portable BIT Beamer project with XeLaTeX."""
import argparse
from pathlib import Path
import re
import shutil
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
ENTRIES = ('main', 'paper', 'tutorial', 'progress')

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('entry', nargs='?', default='main', choices=ENTRIES)
    parser.add_argument('--all', action='store_true', help='Compile all four entries')
    parser.add_argument('--engine', help='Explicit path to xelatex')
    args = parser.parse_args()
    engine = args.engine or shutil.which('xelatex')
    local_engine = Path('F:/texlive/2023/bin/windows/xelatex.exe')
    if not engine and local_engine.exists():
        engine = str(local_engine)
    if not engine:
        parser.error('XeLaTeX not found. Add TeX Live to PATH or pass --engine PATH.')
    for entry in ENTRIES if args.all else (args.entry,):
        output_dir = ROOT / '.build' / entry
        output_dir.mkdir(parents=True, exist_ok=True)
        command = [engine, '-interaction=nonstopmode', '-halt-on-error',
                   '-file-line-error', '-output-directory=' + str(output_dir),
                   entry + '.tex']
        for run in range(2):
            result = subprocess.run(command, cwd=ROOT, stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
            (output_dir / f'run-{run + 1}.txt').write_bytes(result.stdout)
            if result.returncode:
                print(result.stdout.decode('utf-8', errors='replace')[-7000:])
                return result.returncode
        log = (output_dir / f'{entry}.log').read_text(encoding='utf-8', errors='replace')
        issues = [line for line in log.splitlines()
                  if re.search(r'Overfull|Missing character|Undefined control sequence', line)]
        if issues:
            print('\n'.join(issues))
            return 1
        shutil.copy2(output_dir / f'{entry}.pdf', ROOT / f'{entry}.pdf')
        print(f'OK: {entry}.pdf', flush=True)
    return 0

if __name__ == '__main__':
    sys.exit(main())
