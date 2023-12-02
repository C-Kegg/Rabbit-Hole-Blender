# Put this code intyo ther `Scripting` section of Blender
# The `verts` and `faces` variables must be coppied dirtectly from the response of the A.I., as web requests currently do not work.

import bpy # Blender interface library -- can only be used in Blender
from random import random


def create_obj(verts, faces, name="New_" + str(random())):
    """Creates an object with the given name, vertices, and faces.
    
    Arguments:
        verts = The vertices of the object to create, given as a list of tuples representing points in space.
        
        faces = The faces of the object to create, given as a list of tuples representing indexes of vertices. **Note**: For 3-point faces, the order of the numbers does not matter.
        
        name = The name of the object to create. By default is "Name" + a random number between 0 and 1.
    Returns:
        Name of object created
        """
    mesh = bpy.data.meshes.new(name)
    object = bpy.data.objects.new(name, mesh)
    
    bpy.context.collection.objects.link(object)
    
    mesh.from_pydata(verts, [], faces)
    
    return name


if __name__ == "__main__": 
    # Change the values of these variables depepending on what you want. It's like a 3D connect-the-dots,
    # with the tuples in `verts` being the points and the tuples in `faces` being the lines connecting them
    verts = [(4, -4, 0), (4, 4, 0), (-2, -4, 0), (-2, 4, 0), (4, -4, 2), (4, 4, 2), (-2, -4, 2), (-2, 4, 2)]
    faces = [(0, 1, 3, 2), (4, 5, 7, 6), (1, 3, 7, 5), (0, 2, 6, 4)]
    
    create_obj(verts, faces)