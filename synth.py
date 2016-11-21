import bpy, random

random.seed(None) # seed RNG with time

rad2deg = 360 / 6.28

def euler_rotate(bone):
    bone.rotation_mode = 'XYZ'
    bone.rotation_euler = [
            random.gauss(0, 0.5),
            random.gauss(0, 0.5),
            random.gauss(0, 0.5)]

def set_mode(mode):
    if bpy.ops.object.mode_set.poll():
        bpy.ops.object.mode_set(mode=mode)

# randomize camera location a bit
for obj in bpy.data.objects:
    if obj.type == 'CAMERA':
        # TODO: rotate camera according
        pass
    
    # TODO: generalize to other models
    if obj.name == 'MaleArm':
        obj.rotation_mode = 'XYZ'
        obj.rotation_euler = [-30 / rad2deg, 0 / rad2deg, 45 / rad2deg]

#        set_mode("POSE")

        for bone in obj.pose.bones:
            print(bone.name)

            if bone.name.split(".")[0] in ["Upperarm", "Lowerarm", "Thigh", "Shin", "Hand", "Fingers1", "Fingers2"]:
                euler_rotate(bone)

#        mat = bpy.data.materials.new("RED")
#        mat.diffuse_intensity = 1.0
#        mat.diffuse_shader = 'LAMBERT'
#        mat.diffuse_color = [1.0, 0.0, 0.0]
#        obj.active_material = mat

# fix some rendering issues

bpy.data.worlds[0].light_settings.use_indirect_light = True

bpy.ops.render.render(write_still=True)

print("Scene ready for render!")
