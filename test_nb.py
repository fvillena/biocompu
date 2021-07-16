import subprocess
import tempfile


def _exec_notebook(path):
    with tempfile.NamedTemporaryFile(suffix=".ipynb") as fout:
        args = ["jupyter", "nbconvert", "--to", "notebook", "--execute",
                "--ExecutePreprocessor.timeout=1000",
                "--output", fout.name, path]
        subprocess.check_call(args)


def test_1_1():
    _exec_notebook('1.1-clustering.ipynb')

def test_1_2():
    _exec_notebook('1.2-dimensionality_reduction.ipynb')

def test_2():
    _exec_notebook('2-classification.ipynb')

def test_3():
    _exec_notebook('3-regression.ipynb')

def test_4_1():
    _exec_notebook('4.1-balancing.ipynb')