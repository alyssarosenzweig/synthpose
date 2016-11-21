import bpy, random, os

def camera_rotate():
    # TODO: rotate camera randomly, according to paper
    camera = bpy.data.objects["Camera"]
    camera.rotation_mode = 'XYZ'
    camera.rotation_euler = [3.14/3, 0, 0]
    camera.location = [0.0, -4.0, 3.0]

def model_rotate(model):
    model.rotation_mode = 'XYZ'
    model.rotation_euler = [0, 0, random.gauss(0, 3.14/8)]

def model_scale(model):
    model.scale[0] = random.gauss(1, 0.15) # random weight
    model.scale[1] = random.gauss(1, 0.15) # random, uh, depth
    model.scale[2] = random.gauss(1, 0.15) # random height

def random_skeleton(model):
    for bone in model.pose.bones:
        if bone.name.split(".")[0] in ["Upperarm", "Lowerarm", "Thigh", "Shin", "Hand", "Fingers1", "Fingers2"]:
            bone_random_rotate(bone)

def bone_random_rotate(bone):
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

def render_mode(mode):
    set_mode(mode)
    bpy.ops.render.render(write_still=True)
    os.system("iceweasel /tmp/.png")

def render_frame():
    camera_rotate()

    # TODO: generalize to other models
    model = bpy.data.objects["MaleArm"]

    model_rotate(model)
    model_scale(model)
    random_skeleton(model)

    render_mode("parts")
    render_mode("depth")

render_frame()
