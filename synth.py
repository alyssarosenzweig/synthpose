import bpy, random

random.seed(None) # seed RNG with time

rad2deg = 360 / 6.28

def euler_rotate(bone):
    bone.rotation_mode = 'XYZ'
    bone.rotation_euler = [
            random.uniform(-2.5, +2.5),
            random.uniform(-2.5, +2.5),
            random.uniform(-2.5, +2.5)]

# randomize camera location a bit
for obj in bpy.data.objects:
    if obj.type == 'CAMERA':
        #obj.rotation_euler[0] += random.uniform(-1, 1)
        #obj.rotation_euler[1] += random.uniform(-1, 1)
        #obj.rotation_euler[2] += random.uniform(-1, 1)
        pass
    if obj.name == 'MaleArm':
        obj.rotation_mode = 'XYZ'
        obj.rotation_euler = [-30 / rad2deg, 0 / rad2deg, 45 / rad2deg]

        if bpy.ops.object.mode_set.poll():
            bpy.ops.object.mode_set(mode='POSE')

        for bone in obj.pose.bones:
            print(bone.name)

            if bone.name.split(".")[0] in ["Upperarm", "Lowerarm", "Thigh", "Shin", "Hand", "Fingers1", "Fingers2"]:
                euler_rotate(bone)

        print(obj)

bpy.ops.render.render(write_still=True)

print("Scene ready for render!")
