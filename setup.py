from setuptools import setup

with open("README.MD", 'r') as f:
    long_description = f.read()

setup(
   name='helixvis',
   version='1.0',
   description='Create 2-dimensional visualizations of alpha-helical peptide sequences',
   license="GPL-3",
   long_description=long_description,
   author='Vigneshwar Subramanian, Raoul Wadhwa, Regina Stevens-Truss',
   author_email='vxs294@case.edu',
   url="https://pypi.org/project/helixvis/",
   packages=['helixvis'],  
   install_requires=['numpy', 'pandas', 'matplotlib'], 
)