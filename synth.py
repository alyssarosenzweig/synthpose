import bpy, random

def euler_rotate(bone):
    bone.rotation_mode = 'XYZ'
    bone.rotation_euler = [
            random.gauss(0, 0.25),
            random.gauss(0, 0.25),
            random.gauss(0, 0.1)]

for obj in bpy.data.objects:
    if obj.type == 'CAMERA':
        # TODO: rotate camera randomly, according to paper
        pass
    
    # TODO: generalize to other models
    if obj.name == 'MaleArm':
        obj.rotation_mode = 'XYZ'
        obj.rotation_euler = [0, 0, random.gauss(3.14/4, 3.14/8)]

        for bone in obj.pose.bones:
            print(bone.name)

            if bone.name.split(".")[0] in ["Upperarm", "Lowerarm", "Thigh", "Shin", "Hand", "Fingers1", "Fingers2"]:
                euler_rotate(bone)

bpy.ops.render.render(write_still=True)

print("Scene ready for render!")
