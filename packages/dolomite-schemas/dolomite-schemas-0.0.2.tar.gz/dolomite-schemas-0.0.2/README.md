<!-- These are examples of badges you might want to add to your README:
     please update the URLs accordingly

[![Built Status](https://api.cirrus-ci.com/github/<USER>/dolomite-schemas.svg?branch=main)](https://cirrus-ci.com/github/<USER>/dolomite-schemas)
[![ReadTheDocs](https://readthedocs.org/projects/dolomite-schemas/badge/?version=latest)](https://dolomite-schemas.readthedocs.io/en/stable/)
[![Coveralls](https://img.shields.io/coveralls/github/<USER>/dolomite-schemas/main.svg)](https://coveralls.io/r/<USER>/dolomite-schemas)
[![PyPI-Server](https://img.shields.io/pypi/v/dolomite-schemas.svg)](https://pypi.org/project/dolomite-schemas/)
[![Conda-Forge](https://img.shields.io/conda/vn/conda-forge/dolomite-schemas.svg)](https://anaconda.org/conda-forge/dolomite-schemas)
[![Monthly Downloads](https://pepy.tech/badge/dolomite-schemas/month)](https://pepy.tech/project/dolomite-schemas)
[![Twitter](https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter)](https://twitter.com/dolomite-schemas)
-->

[![Project generated with PyScaffold](https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold)](https://pyscaffold.org/)

# dolomite-schemas

This package provides access to the [JSON schemas](https://github.com/ArtifactDB/BiocObjectSchemas) for bioconductor objects, for use in downstream packages. It is primarily intended for the various dolomite-* python packages in the artifactdb organization.

## Installation

Developers can install the package through pip.

```sh
pip install dolomite-schemas
```

## Usage

The default assumption across all dolomite-derivatives is the package will contain a directory `schemas` to access the JSON schemas.

```python
os.path.join(os.dirname(schema_pkg.__file__), "schemas")
```

<!-- pyscaffold-notes -->

## Note

This project has been set up using PyScaffold 4.5. For details and usage
information on PyScaffold see https://pyscaffold.org/.

```sh
putup dolomite-schemas --package schemas --namespace dolomite --markdown
```
