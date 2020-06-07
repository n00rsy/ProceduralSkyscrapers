bl_info = {
    "name" : "ProceduralSkyscrapers",
    "author" : "n00rsy",
    "description" : "Procedurally generate skyscrapers",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Add Mesh"
}

import bpy
from . import procedural_skyscrapers

def menu_func(self, context):
    self.layout.operator(procedural_skyscrapers.GenerateSkyscraper.bl_idname, text="Procedural Skyscrapers", icon='PLUGIN')

classes = (
    procedural_skyscrapers.GenerateSkyscraper,
)
def register():
    for cls in classes:
        bpy.utils.register_class(cls)
    bpy.types.VIEW3D_MT_mesh_add.append(menu_func)


def unregister():
    for cls in reversed( classes):
        bpy.utils.unregister_class(cls)
    bpy.types.VIEW3D_MT_mesh_add.remove(menu_func)