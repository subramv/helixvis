name = "helixvis"

# Check for dependencies
dependencies = ("numpy", "pandas", "matplotlib", "dateutil")
missing = []

for mod in dependencies:
    try:
        __import__(mod)
    except ImportError as e:
        missing.append(mod)

if missing:
    raise ImportError(
        "Missing required dependencies {0}".format(missing))
del dependencies, mod, missing

from .draw_wheel import draw_wheel
from .draw_wenxiang import draw_wenxiang

# readme
__doc__ = """
Built by the lab of Regina Stevens-Truss, PhD (Professor & Chair, Department of Chemistry, Kalamazoo College), helixvis can be used to create publication-quality, 2-dimensional visualizations of alpha-helical peptide sequences. Specifically, this package allows the user to programmatically generate helical wheels and wenxiang diagrams to provide a bird's eye, top-down view of alpha-helical oligopeptides. Although other tools exist to complete this task, they generally provide a graphical user interface for manual input of peptide sequences, without allowing for programmatic creation and customization of visualizations. Programmatic generation of helical wheels in open source Python provides multiple benefits, including:

    - quick and easy incorporation of wheels into markdown documents
    - rapid visualization of many peptides (e.g. all the elements of a peptide database) without manual steps
    - programmatic customization of visualizations
    - reproducibility: practically zero manual steps required for design and creation of helical wheels and wenxiang diagrams

This is a port of R package helixvis into Python.

"""

