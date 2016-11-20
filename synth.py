import bpy, random

random.seed(None) # seed RNG with time

for obj in bpy.data.objects:
    if obj.type == 'CAMERA':
        obj.rotation_euler[1] += 0.5

print("Scene ready for render!")
