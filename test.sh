#!/bin/sh
blender --background --python synth.py -o //out.png -f 1 cube.blend
iceweasel out.png*
