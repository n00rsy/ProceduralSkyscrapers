import bpy
from bpy.props import (
        BoolProperty,
        EnumProperty,
        FloatProperty,
        IntProperty,
        FloatVectorProperty,
        StringProperty,
        )
import bmesh
import random
from mathutils import Vector

def generate_skyscraper(props, context):
    random.seed(props.seed)
    bm = bmesh.new()
    bmesh.ops.create_cube(bm, size=1)
    
    for face in bm.faces[:]:
        if(face.normal.z ==1):
            height = props.height-random.random()*(props.random_height)
            bmesh.ops.translate(bm,
            verts=face.verts,
            vec=height * face.normal)
    
    # generate base shape
        # random x y z scale
        # maybe extrude random faces
        # maybe make random edge loops
        # maybe move edges along normals - check for overlap
        # maybe move edges in random directions - check for overlap
        # maybe bevel random edges

    # generate actual structure
        # select random top faces and extrude up OR extrude, scale in, extrude move up
        # maybe select random horizontal face and extrude out
        # maybe make horizontal loops and scale in
        # repeat

    #finishing touches
        # maybe select random outer edges paralell to inner ones and move up or down
        # maybe add antenna
        # maybe bevel?

    # write bmesh into new mesh
    me = bpy.data.meshes.new('Mesh')
    bm.to_mesh(me)
    bm.free()

    # Add mesh to the scene
    obj = bpy.data.objects.new('Skyscraper', me)
    bpy.context.collection.objects.link(obj)

class GenerateSkyscraper(bpy.types.Operator):
    """Construct a skyscraper """      # Use this as a tooltip for menu items and buttons.
    bl_idname = "mesh.add_skyscraper"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Add Skyscraper"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    #properties
    seed: bpy.props.IntProperty(name="Seed", default=0)
    height: bpy.props.IntProperty(name="Height", default=5, min=1, max=10)
    complexity: bpy.props.IntProperty(name="Complexity", default=5, min=1, max=10)
    random_height : bpy.props.FloatProperty(name="Random Height", default=0, min=0, max=5)
    random_complexity : bpy.props.FloatProperty(name="Random Complexity", default=0, min=0, max=1)
    detail: bpy.props.IntProperty(name="Detail", default=5, min=1, max=10)

    def execute(self, context):        # execute() is called when running the operator.
        #make a skyscraper lmaoooo
        generate_skyscraper(self, context)
        return {'FINISHED'}            # Lets Blender know the operator finished successfully.


