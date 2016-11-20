import bpy, random

random.seed(None) # seed RNG with time

for obj in bpy.data.objects:
    if obj.type == 'CAMERA':
        print(obj.rotation_euler)
        # obj.rotation_euler = [0, 0, 0]
#bpy.context.camera.shift_x = random.uniform(-10, 10)
#bpy.context.scene.render()

bpy.ops.render.render(write_still=True)

print("Scene ready for render!")
