## Loading the package

After installation helixvis can be loaded as follows:

```python
# load pyplot
import matplotlib.pyplot as plt

# load helixvis
import helixvis
```

## Background

The helixvis R package allows users to construct 2-dimensional visualizations of 3-dimensional &alpha;-helical oligopeptides in a programmatic, reproducible manner.
Currently, helixvis implements visualization of helical wheels, introduced by @wheeldiag, and wenxiang diagrams, introduced by @wenxiangdiag.

A prototypical &alpha;-helix has approximately 3.6 residues per turn [@helixorig], implying a 100&deg; rotation between consecutive residues.
After 18 rotations, the 19th residue returns to the same angle as the 1st residue.
Since helical wheels place all residues at an equal radius away from the center, having the same angle of rotation would cause complete overlap of the 1st and 19th residues.
As such, helical wheels are limited to plotting 18 residues in a single turn, although some tools do allow for plotting of more than 1 turn [@heliquest].
For consistency, we also limit wenxiang diagrams to 18 residues.

## Helical wheels

Helical wheels provide a bird's eye view of an &alpha;-helical peptides and are particularly helpful at highlighting prominent hydrophobic faces to explain a large hydrophobic moment [@eisenberg1982; @dathe1997] and design antimicrobial peptides [@chen2005; @jiang2011].

With helixvis, generating helical wheels takes a single line of code, as follows.

```python
# draw helical wheel
helixvis.draw_wheel("GLLGPLLKIAAKVGSNLL")
plt.show()
```

By default: nonpolar residues (e.g. glycine, tryptophan) will be colored grey; polar residues (e.g. serine, threonine) will be colored yellow; acidic residues with a negative charge at physiologic pH (e.g. aspartic acid, glutamic acid) will be colored red; and basic residues with a positive charge at physiologic pH (e.g. lysine, arginine) will be colored blue.
This color scheme can be modified using the `colors` parameter, which accepts a character vector with 4 elements, each of which must be an element of `matplotlib.colors.cnames`.
The one-letter code for each residue can also be overlaid on each residue by setting the `labels` parameter to `True`.

```python
# draw helical wheel with custom color scheme
helixvis.draw_wheel("GLLGPLLKIAAKVGSNLL", colors = ["pink", "orange", "white", "black"],
       labels = True, labelcolor = "blue")
plt.show()
```

## Wenxiang diagrams

Wenxiang diagrams are quite similar to helical wheels, with the exception that distance from the first residue is denoted by distance from the center of the spiral.
Thus, wenxiang diagrams visually provide the order of amino acids in the sequence.
The code used to generate wenxiang diagrams is analogous to that for generation of helical wheels.

The following code blocks and figures reproduce the figures from the Helical Wheel section, redrawn as wenxiang diagrams.

```python

# draw wenxiang diagram
helixvis.draw_wenxiang("GLLGPLLKIAAKVGSNLL")
plt.show()

# draw wenxiang diagram with custom color scheme
draw_wenxiang("GLLGPLLKIAAKVGSNLL", colors = ["pink", "orange", "white", "black"],
       labels = True, labelcolor = "blue")
plt.show()
```
