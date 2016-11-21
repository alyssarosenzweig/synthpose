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
        obj.rotation_mode = 'XYZ'
        obj.rotation_euler = [3.14/3, 0, 0]
        obj.location = [0.0, -4.0, 3.0]
        pass
    
    # TODO: generalize to other models
    if obj.name == 'MaleArm':
        # random rotation of person
        obj.rotation_mode = 'XYZ'
        obj.rotation_euler = [0, 0, random.gauss(0, 3.14/8)]

        obj.scale[0] = random.gauss(1, 0.15) # random weight
        obj.scale[1] = random.gauss(1, 0.15) # random, uh, depth
        obj.scale[2] = random.gauss(1, 0.15) # random height

        bpy.data.materials["MaleSkin"].use_textures[0] = True
        bpy.data.materials["MaleSkin"].use_textures[1] = False

        for bone in obj.pose.bones:
            print(bone.name)

            if bone.name.split(".")[0] in ["Upperarm", "Lowerarm", "Thigh", "Shin", "Hand", "Fingers1", "Fingers2"]:
                euler_rotate(bone)

# depth implemented by hacking mist
bpy.data.worlds[0].mist_settings.use_mist = False

bpy.ops.render.render(write_still=True)

print("Scene ready for render!")
