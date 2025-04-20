def select_object(object_name):
    import bpy
    bpy.ops.object.select_all(action='DESELECT')  # Deselect all objects
    obj = bpy.data.objects.get(object_name)
    if obj:
        obj.select_set(True)  # Select the specified object
        bpy.context.view_layer.objects.active = obj  # Set it as the active object
        return obj
    return None

def create_material(material_name):
    import bpy
    material = bpy.data.materials.new(name=material_name)
    material.use_nodes = True  # Enable nodes for the material
    return material

def export_model(filepath, export_format='FBX'):
    import bpy
    if export_format == 'FBX':
        bpy.ops.export_scene.fbx(filepath=filepath)
    elif export_format == 'OBJ':
        bpy.ops.export_scene.obj(filepath=filepath)
    else:
        raise ValueError("Unsupported export format: {}".format(export_format))