# helixvis: Visualize alpha-helical peptide sequences in Python

## Purpose

Built by the lab of Regina Stevens-Truss, PhD (Professor & Chair, Department of Chemistry, Kalamazoo College), helixvis can be used to create publication-quality, 2-dimensional visualizations of alpha-helical peptide sequences.
Specifically, this package allows the user to programmatically generate helical wheels and wenxiang diagrams to provide a bird's eye, top-down view of alpha-helical oligopeptides.
Although other tools exist to complete this task, they generally provide a graphical user interface for manual input of peptide sequences, without allowing for programmatic creation and customization of visualizations.
Programmatic generation of helical wheels in open source Python provides multiple benefits, including:

* quick and easy incorporation of wheels into markdown documents
* rapid visualization of many peptides (e.g. all the elements of a peptide database) without manual steps
* programmatic customization of visualizations
* reproducibility: practically zero manual steps required for design and creation of helical wheels and wenxiang diagrams

This is a port of R package helixvis into Python.

## Installation

The source code is currently hosted on GitHub at: https://github.com/subramv1/helixvis

helixvis can be found on the Python package index at: https://pypi.org/project/helixvis/

The most up-to-date release can be installed as follows:

```python
python -m pip install -U pip
python -m pip install -U helixvis

```

## Dependencies

* NumPy
* Pandas
* Matplotlib

## Usage

```python   
# load helixvis
import helixvis

# make helical wheel for "ADEKLGSRTW"
helixvis.draw_wheel("ADEKLGSRTW")

# make wenxiang diagram for "ADEKLGSRTW"
helixvis.draw_wenxiang("ADEKLGSRTW")
```

## License

GPL-3

## Contributions


Please report any bugs, suggestions, etc. on the [issues page](https://github.com/subramv1/helixvis/issues) of the [helixvis GitHub repository](https://github.com/subramv1/helixvis).
Contributions (bug fixes, new features, etc.) are welcome via pull requests (generally from forked repositories).
