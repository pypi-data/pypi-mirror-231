import os
from setuptools import setup, find_packages

# Read version
with open(os.path.join(os.path.dirname(__file__), 'VERSION'), 'r') as f:
    version = f.read().strip()

with open(os.path.join(os.path.dirname(__file__), 'README.md'), 'r') as f:
    long_description = f.read().strip()

setup(
    name='scSpectra',
    version=version,
    packages=["Spectra",
              "Spectra.load"],
    author='Russel Z. Kunes',
    author_email='KunesR@mskcc.org',
    maintainer='Tobias Krause',
    maintainer_email='krauset@mskcc.org',
    description="Supervised discovery of interpretable gene programs from single-cell data",
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires = [
        'numpy>=1.20.3',
        'scipy>=1.7.3',
        'scanpy>=1.8.2',
        'torch>=1.10.1',
        'opt-einsum>=3.3.0',
        'pandas>=1.3.5',
        'tqdm>=4.62.3',
        'pyvis>=0.1.9'],
    include_package_data=True,
    package_data={'default_gene_sets': ['Spectra/data/default_gene_sets.json'],
                  'sample_data': ['Spectra/data/sample_data.h5ad']}
)
