#!/bin/sh
blender human_1.blend --python synth.py -b
iceweasel /tmp/.png
