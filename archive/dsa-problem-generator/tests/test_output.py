"""The committed output/ folder is current, and every generated document compiles."""

from __future__ import annotations

import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

from problemgen import CANONICAL_TOPICS, CS253ProblemGenerator
from problemgen.cli import CATEGORIES, write_outputs

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "output"
EXTRA_SEEDS = (4, 5)


def compile_error(tex: str) -> str:
    """Compile tex in a throwaway directory; return the first LaTeX error, or '' on success."""
    with tempfile.TemporaryDirectory() as tmp:
        source = Path(tmp) / "problem.tex"
        source.write_text(tex)
        result = subprocess.run(
            ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", source.name],
            cwd=tmp,
            capture_output=True,
            text=True,
            timeout=120,
        )
        if result.returncode == 0 and (Path(tmp) / "problem.pdf").exists():
            return ""
        errors = [line for line in result.stdout.splitlines() if line.startswith("!")]
        return errors[0] if errors else f"pdflatex exited with {result.returncode}"


class OutputFolderTests(unittest.TestCase):
    def test_output_matches_generators(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            fresh = Path(tmp)
            write_outputs(fresh)
            expected = sorted(p.relative_to(fresh) for p in fresh.rglob("*.tex"))
            actual = sorted(p.relative_to(OUTPUT) for p in OUTPUT.rglob("*.tex"))
            self.assertEqual(actual, expected, "run: python3 cs253_problem_generator.py --write-all output")
            for rel in expected:
                self.assertEqual((OUTPUT / rel).read_text(), (fresh / rel).read_text(), str(rel))

    def test_every_topic_is_represented(self) -> None:
        self.assertEqual(sorted(t for topics in CATEGORIES.values() for t in topics), sorted(CANONICAL_TOPICS))
        self.assertEqual(sorted(p.name for p in OUTPUT.iterdir() if p.is_dir()), sorted(CATEGORIES))
        for category, topics in CATEGORIES.items():
            with self.subTest(category=category):
                folders = sorted(p.name for p in (OUTPUT / category).iterdir() if p.is_dir())
                self.assertEqual(folders, sorted(topics))


@unittest.skipUnless(shutil.which("pdflatex"), "pdflatex is not installed")
class CompileTests(unittest.TestCase):
    def test_output_files_compile(self) -> None:
        for path in sorted(OUTPUT.rglob("*.tex")):
            with self.subTest(file=str(path.relative_to(ROOT))):
                self.assertEqual(compile_error(path.read_text()), "")

    def test_more_seeds_compile_with_and_without_solutions(self) -> None:
        for topic in CANONICAL_TOPICS:
            for seed in EXTRA_SEEDS:
                problem = CS253ProblemGenerator(seed=seed).generate(topic)
                for with_solution in (False, True):
                    with self.subTest(topic=topic, seed=seed, with_solution=with_solution):
                        self.assertEqual(compile_error(problem.to_latex(seed, with_solution)), "")


if __name__ == "__main__":
    unittest.main()
