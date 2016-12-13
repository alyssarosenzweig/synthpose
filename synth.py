import bpy, bpy_extras, json, random, os

# modify these as needed
OUTPUT_DIR = os.environ.get("SYNTHPOSE_OUTPUT_DIR") or "samples/"
COUNT      = int(os.environ.get("SYNTHPOSE_COUNT")  or 1)

def camera_rotate():
    # TODO: rotate camera randomly, according to paper
    camera = bpy.data.objects["Camera"]
    camera.rotation_mode = 'XYZ'
    camera.rotation_euler = [3.14/3, 0, 0]
    camera.location = [0.0, -4.0, 3.0]

def model_translate(model):
    model.location[2] = random.gauss(-2, -0.25)

def model_rotate(model):
    model.rotation_mode = 'XYZ'
    model.rotation_euler = [0, 0, random.gauss(0, 3.14/8)]

def model_scale(model):
    coefficient = random.gauss(1.5, 0.5)
    model.scale[0] = random.gauss(coefficient, 0.15) # random weight
    model.scale[1] = random.gauss(coefficient, 0.15) # random, uh, depth
    model.scale[2] = random.gauss(coefficient, 0.15) # random height

def random_skeleton(model):
    for bone in model.pose.bones:
        if bone.name.split(".")[0] in ["Upperarm", "Lowerarm", "Thigh", "Shin"]:
            bone_random_rotate(bone, bone.name)

def bone_random_rotate(bone, name):
    bone.rotation_mode = 'XYZ'
    bone.rotation_euler = [
            random.uniform(-1, 1),
            0,
            random.uniform(-1, 1)]

def set_mode(mode):
    mat = bpy.data.materials["MaleSkin"]

    if mode == "depth":
        mat.use_textures[0] = False
        mat.use_textures[1] = True
        mat.use_textures[2] = False
        bpy.data.worlds[0].mist_settings.use_mist = True
    elif mode == "parts":
        mat.use_textures[0] = True
        mat.use_textures[1] = False
        mat.use_textures[2] = False
        bpy.data.worlds[0].mist_settings.use_mist = False
    elif mode == "rgb":
        mat.use_textures[0] = False
        mat.use_textures[1] = False
        mat.use_textures[2] = True
        bpy.data.worlds[0].mist_settings.use_mist = False

def render_mode(mode, prefix, count):
    set_mode(mode)
    path = prefix + 'render_' + str(count) + "_" + mode + '.png'
    bpy.ops.render.render()
    bpy.data.images["Render Result"].save_render(filepath=path)

# see https://blender.stackexchange.com/questions/882/how-to-find-image-coordinates-of-the-rendered-vertex
def space_convert(mat):
    coord = mat.to_translation()
    print(coord)

    projected = bpy_extras.object_utils.world_to_camera_view(bpy.context.scene, bpy.data.objects["Camera"], coord)

    s = bpy.context.scene.render.resolution_percentage / 100
    return [projected.x * bpy.context.scene.render.resolution_x * s, projected.y * bpy.context.scene.render.resolution_y * s]

def project(j):
    mat = bpy.data.objects["MaleArm"].matrix_world
    bone = bpy.data.objects["MaleArm"].pose.bones[j]
    return space_convert(mat * bone.matrix)

def export_json(prefix, count):
    f = open(prefix + "render_" + str(count) + "_skeleton.json", "w")
    
    skeleton = {
            "head": "Head",

            "lhand": "Hand.Left",
            "rhand": "Hand.Right",
            "lshoulder": "Upperarm.Left",
            "rshoulder": "Upperarm.Right",
            "lelbow": "Forearm.Left",
            "relbow": "Forearm.Right",

            "hip": "Hip",

            "lpelvis": "Thigh.Left",
            "rpelvis": "Thigh.Right",
            "lknee": "Shin.Left",
            "rknee": "Shin.Right",
            "lfoot": "Foot.Left",
            "rfoot": "Foot.Right"
    }

    f.write(json.dumps({k: project(v) for k, v in skeleton.items()}))
    f.close()

def render_frame(count):
    camera_rotate()

    # TODO: generalize to other models
    model = bpy.data.objects["MaleArm"]

    model_translate(model)
    model_rotate(model)
    model_scale(model)
    random_skeleton(model)

    render_mode("parts", OUTPUT_DIR, count)
    render_mode("depth", OUTPUT_DIR, count)
    render_mode("rgb",   OUTPUT_DIR, count)
    export_json(OUTPUT_DIR, count)

for i in range(0, COUNT):
    render_frame(i)
