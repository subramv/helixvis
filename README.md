# helixvis: Visualize alpha-helical peptide sequences in Python

## Purpose

helixvis can be used to create publication-quality, 2-dimensional visualizations of alpha-helical peptide sequences.
Specifically, this package allows the user to programmatically generate helical wheels and wenxiang diagrams to provide a bird's eye, top-down view of alpha-helical oligopeptides.
Although other tools exist to complete this task, they generally provide a graphical user interface for manual input of peptide sequences, without allowing for programmatic creation and customization of visualizations.
Programmatic generation of helical wheels in open source Python provides multiple benefits, including:

* quick and easy incorporation of wheels into markdown documents
* rapid visualization of many peptides (e.g. all the elements of a peptide database) without manual steps
* programmatic customization of visualizations
* reproducibility: practically zero manual steps required for design and creation of helical wheels and wenxiang diagrams

## Installation and Use

The following Terminal code can be used to take advantage of the current functionality of helixvis.

```
# clone GitHub repo
git clone https://github.com/subramv1/helixvis
cd helixvis

# make helical wheel for "ADEKLGSRTW"
python3 draw_wheel.py ADEKLGSRTW

# make wenxiang diagram for "ADEKLGSRTW"
python3 draw_wenxiang.py ADEKLGSRTW
```

## Contributions


Please report any bugs, suggestions, etc. on the [issues page](https://github.com/subramv1/helixvis/issues) of the [helixvis GitHub repository](https://github.com/subramv1/helixvis).
Contributions (bug fixes, new features, etc.) are welcome via pull requests (generally from forked repositories).
