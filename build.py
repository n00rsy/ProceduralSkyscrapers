#!/usr/bin/env python

from os.path import abspath, dirname, join as pjoin
import zipfile

SRC_DIR = dirname(abspath(__file__))

with zipfile.ZipFile('add_mesh_SpaceshipGenerator.zip', 'w', zipfile.ZIP_DEFLATED) as arch:
    for filename in [
            '__init__.py',
            'procedural_skyscrapers.py']:
        arch.write(pjoin(SRC_DIR, filename), 'ProceduralSkyscrapers/'+filename)

print('created file: ProceduralSkyscrapers.zip')