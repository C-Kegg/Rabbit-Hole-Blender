# ** WARNING **
# This code is not in use. Please use the `blender_code_with_genai` file.
# Put this code into the `Scripting` section of Blender
# The `verts` and `faces` variables must be coppied dirtectly from the response of the A.I. at the momment, as web requests currently do not work properly.

import bpy, json
from random import random



def create_obj(data:str, name="New_" + str(random())):
    """Creates an object with the given name, vertices, and faces.
    
    Arguments:
        data = The JSON data of the object to create.

        name = The name of the object to create. By default is "Name" + a random float between 0 and 1.
    Returns:
        Name of object created
    """
    data_proc = json.loads(data)
    if data_proc[""]:
        mesh = bpy.data.meshes.new(name)
        object = bpy.data.objects.new(name, mesh)
    
        bpy.context.collection.objects.link(object)
    
        mesh.from_pydata(verts, [], faces)
    elif data_proc:
        return name


if __name__ == "__main__": 
    # Change the values of these variables depepending on what you want. It's like a 3D connect-the-dots,
    # with the tuples in `verts` being the points and the tuples in `faces` being the lines connecting them
    verts = [(4, -4, 0), (4, 4, 0), (-2, -4, 0), (-2, 4, 0), (4, -4, 2), (4, 4, 2), (-2, -4, 2), (-2, 4, 2)]
    faces = [(0, 1, 3, 2), (4, 5, 7, 6), (1, 3, 7, 5), (0, 2, 6, 4)]
    
    create_obj(verts, faces)