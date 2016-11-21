#!/bin/sh
blender human-fast.blend --python synth.py -b
iceweasel /tmp/.png
