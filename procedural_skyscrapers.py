import bpy
from bpy.props import (
        BoolProperty,
        EnumProperty,
        FloatProperty,
        IntProperty,
        FloatVectorProperty,
        StringProperty,
        )
class GenerateSkyscraper(bpy.types.Operator):
    """Construct a skyscraper """      # Use this as a tooltip for menu items and buttons.
    bl_idname = "mesh.add_skyscraper"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Add Skyscraper"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    #properties
    seed: bpy.props.IntProperty(name="Seed", default=0)
    height: bpy.props.IntProperty(name="Height", default=5, min=1, max=10)
    complexity: bpy.props.IntProperty(name="Complexity", default=5, min=1, max=10)
    random_height : bpy.props.FloatProperty(name="Random Height", default=0, min=0, max=1)
    random_complexity : bpy.props.FloatProperty(name="Random Complexity", default=0, min=0, max=1)
    detail: bpy.props.IntProperty(name="Detail", default=5, min=1, max=10)

    def execute(self, context):        # execute() is called when running the operator.
        #make a skyscraper lmaoooo
        bpy.ops.mesh.primitive_cube_add()
        return {'FINISHED'}            # Lets Blender know the operator finished successfully.

