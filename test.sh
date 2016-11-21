#!/bin/sh
blender human-old.blend --python synth.py -b
iceweasel /tmp/.png
