#!/bin/bash

# from https://github.com/ArtifactDB/alabaster.schemas/blob/master/inst/source.sh

curl -L https://artifactdb.github.io/BiocObjectSchemas/bundle.tar.gz > bundle.tar.gz # for testing the latest.
rm -rf schemas
tar -xvf bundle.tar.gz

dest=../src/dolomite_schemas/schemas
rm -rf ${dest}
mv resolved ${dest}
