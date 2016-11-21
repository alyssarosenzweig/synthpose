import bpy, random

def euler_rotate(bone):
    bone.rotation_mode = 'XYZ'
    bone.rotation_euler = [
            random.gauss(0, 0.25),
            random.gauss(0, 0.25),
            random.gauss(0, 0.1)]

def set_mode(mode):
    mat = bpy.data.materials["MaleSkin"]

    if mode == "depth":
        mat.use_textures[0] = False
        mat.use_textures[1] = True
        bpy.data.worlds[0].mist_settings.use_mist = True
    elif mode == "parts":
        mat.use_textures[0] = True
        mat.use_textures[1] = False
        bpy.data.worlds[0].mist_settings.use_mist = False

# TODO: rotate camera randomly, according to paper
camera = bpy.data.objects["Camera"]
camera.rotation_mode = 'XYZ'
camera.rotation_euler = [3.14/3, 0, 0]
camera.location = [0.0, -4.0, 3.0]
    
# TODO: generalize to other models
model = bpy.data.objects["MaleArm"]

# random rotation of person
model.rotation_mode = 'XYZ'
model.rotation_euler = [0, 0, random.gauss(0, 3.14/8)]

model.scale[0] = random.gauss(1, 0.15) # random weight
model.scale[1] = random.gauss(1, 0.15) # random, uh, depth
model.scale[2] = random.gauss(1, 0.15) # random height

for bone in model.pose.bones:
    print(bone.name)

    if bone.name.split(".")[0] in ["Upperarm", "Lowerarm", "Thigh", "Shin", "Hand", "Fingers1", "Fingers2"]:
        euler_rotate(bone)

set_mode("parts")
bpy.ops.render.render(write_still=True)

print("Scene ready for render!")
