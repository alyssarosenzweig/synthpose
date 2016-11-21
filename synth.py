import bpy, random

rad2deg = 360 / 6.28

def euler_rotate(bone):
    bone.rotation_mode = 'XYZ'
    bone.rotation_euler = [
            random.gauss(0, 0.5),
            random.gauss(0, 0.5),
            random.gauss(0, 0.5)]

for obj in bpy.data.objects:
    if obj.type == 'CAMERA':
        # TODO: rotate camera randomly, according to paper
        pass
    
    # TODO: generalize to other models
    if obj.name == 'MaleArm':
        obj.rotation_mode = 'XYZ'
        obj.rotation_euler = [-30 / rad2deg, 0 / rad2deg, 45 / rad2deg]

        for bone in obj.pose.bones:
            print(bone.name)

            if bone.name.split(".")[0] in ["Upperarm", "Lowerarm", "Thigh", "Shin", "Hand", "Fingers1", "Fingers2"]:
                euler_rotate(bone)

bpy.ops.render.render(write_still=True)

print("Scene ready for render!")
