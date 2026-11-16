"""Snapshot every note that git is not tracking.

Held notes (the review queue, un-published notes, source transcriptions) are
git-ignored, and git treats ignored files as disposable: switching to a branch
or commit where one of them was tracked overwrites it, and switching back
deletes it. This script copies them into one archive that git never touches.

    python tools/backup_held.py            # write .workspace/backups/held-<time>.tar.gz
    python tools/backup_held.py --list     # show what would be saved

Run it before un-publishing notes, before `git checkout`/`git switch`/`git merge`
/`git pull`, and whenever a batch of held notes has been written. The newest
ten archives are kept. To restore: `tar -xzf <archive> -C <vault root>`.
"""
from __future__ import annotations

import subprocess
import sys
import tarfile
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / ".workspace" / "backups"
AREAS = ("academic", "self-study", "archive")
SUFFIXES = {".md", ".tex", ".ipynb", ".desmos", ".svg", ".py", ".txt", ".csv"}
MAX_BYTES = 2_000_000
KEEP = 10


def held_files() -> list[Path]:
    out = subprocess.run(["git", "ls-files", "--others", "-z", "--", *AREAS],
                         cwd=ROOT, capture_output=True, check=True).stdout.decode("utf-8")
    files = []
    for rel in filter(None, out.split("\0")):
        p = ROOT / rel
        skip = {"venv", ".venv", "node_modules", "__pycache__"} & set(Path(rel).parts)
        if not skip and p.is_file() and p.suffix in SUFFIXES and p.stat().st_size <= MAX_BYTES:
            files.append(Path(rel))
    return sorted(files)


def main() -> int:
    files = held_files()
    if "--list" in sys.argv:
        print("\n".join(f.as_posix() for f in files))
        print(f"{len(files)} held file(s)")
        return 0
    DEST.mkdir(parents=True, exist_ok=True)
    archive = DEST / f"held-{time.strftime('%Y%m%d-%H%M%S')}.tar.gz"
    with tarfile.open(archive, "w:gz") as tar:
        for rel in files:
            tar.add(ROOT / rel, arcname=rel.as_posix())
    for old in sorted(DEST.glob("held-*.tar.gz"))[:-KEEP]:
        old.unlink()
    print(f"saved {len(files)} held file(s) to {archive.relative_to(ROOT)} ({archive.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
