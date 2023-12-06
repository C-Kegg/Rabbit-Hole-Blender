# Before running this code, the following must be done. This code is made to be used in VS Code (https://code.visualstudio.com/Download):
# 0: Download VS Code and Blender (https://www.blender.org/download/). Configure VS Code to use Python (Install extensions `Pylance` and `Python` by Microsoft).
# 1.1: Run `pip install fake-bpy-module-latest`. This enables the code completion. 
# 1.2: Run `pip install google-generativeai`.
# 1.3: Restart VS Code.
# 2: Install the `Blender Development` extension by Jacques Lucke. This allows VS Code and Blender to interface.
# 3: Press `Command + Shift + P` on Mac or `Control + Shift + P` on others. Type `Blender`.
# 4: Select `Blender: Start`. In the file picker, select the Blender app.
# 5: Run the code by pressing `Command + Shift + P` on Mac or `Control + Shift + P` on others, typing `Blender`, and selecting `Blender: Run Script`.

import bpy
from random import random
import googlegenai as genai
from prompt import prompt as p


def create_obj(request: str):
    """Queries the Google Generatove A.I. engine with the prompt to create a JSON version of a 3D model, then constructs the model in Blender.
    
    Arguments:

        request: The object you want to create.

    Returns:

        A list containing the objects unique identification number
    """
    ai = genai.run(request, prompt=p)
    r = eval(ai)
    obj = None # Will be defined later
    w = str(random() * random() * random())
    if r["create_type"] == "predef":

        t = r["obj_type"]
        
        if t == "cuboid":

            mesh = bpy.ops.mesh.primitive_cube_add(size=r["size"], enter_editmode=False, align='WORLD', location=r["location"], scale=r["scale"])

            obj = bpy.context.objects.new(w, mesh)
        elif t == "sphere":
            
            mesh = bpy.ops.mesh.primitive_uv_sphere_add(size=r["size"], enter_editmode=False, align='WORLD', location=r['location'])

            obj = bpy.context.objects.new(w, mesh)
        elif t == "cone":

            mesh = bpy.ops.mesh.primitive_cone_add(size=r["size"], enter_editmode=False, align="WORLD", location=r["location"])

            obj = bpy.context.objects.new(w, mesh)
        elif t == "pyramid":
            
            mesh = bpy.data.meshes.new(w)
            object = bpy.data.objects.new(w, mesh)
    
            bpy.context.collection.objects.link(object)

            verts = [(1 + r["scale"][0], 1 + r["scale"][1], 0  + r["scale"][2]), (-1 - r["scale"][0], 1  + r["scale"][1], 0  + r["scale"][2]), (-1 - r["scale"][0], -1  - r["scale"][1], 0  + r["scale"][2]), (1  + r["scale"][0], -1  - r["scale"][1], 0  + r["scale"][2]), (0  + r["scale"][0], 0  + r["scale"][1], 1  + r["scale"][2])]
            faces = [(0, 1, 2, 3), (0, 1, 4), (1, 2, 4), (2, 3, 4), (3, 0, 4)]

            mesh.from_pydata(verts, [], faces)

            obj = bpy.context.active_object
        elif t == "plane":

            mesh = bpy.ops.mesh.primitive_plane_add(size=r["size"], enter_editmode=False, align="WORLD", location=r["location"])

            obj = bpy.context.objects.new(w, mesh)
        elif t == "torus":

            mesh = bpy.ops.mesh.primitive_torus_add(size=r["size"], enter_editmode=False, align='WORLD', location=r["location"])

            obj = bpy.context.objects.new(w, mesh)
        else:
            raise TypeError("`obj_type` is not an accepted type")
        
    elif r["create_type"] == "customdef":
        
        mesh = bpy.data.meshes.new(w)
        object = bpy.data.objects.new(w, mesh)
    
        bpy.context.collection.objects.link(object)
    
        mesh.from_pydata(r["verts"], [], r["faces"])
    obj.location = r["location"]
     # Add a new material
    mat = bpy.data.materials.new(name=("Material" + str(random())))
    obj.data.materials.append(mat)

    # Set material properties for gold
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    principled = nodes.get("Principled BSDF")

    # Set gold color and roughness
    principled.inputs["Base Color"].default_value = (255,95,88,0.01)  # Gold color
    principled.inputs["Roughness"].default_value = 1  # Adjust roughness

     # Optional: Render settings
    bpy.context.scene.render.engine = 'CYCLES'  # Set render engine to Cycles

    return """Object # `{w}` created"""

if __name__ == "__main__":
    create_obj("A cube")