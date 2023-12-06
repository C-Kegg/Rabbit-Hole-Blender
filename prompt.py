# I have put the prompt for the code in `blender_code_with_genai.py` in this file to minimize individual file size.

prompt = """Please provide a JSON object that represents a 3D model suitable for Blender. The model can either be a predefined or custom defined model. The "create_type" value indicates the type of model, with "predef" indicating a predefined model and "customdef" indicating a custom defined model. Predefined models include basic shapes such as cuboids, pyramids, spheres, cones, planes, and toruses. Custom defined models are more complex, such as text characters, structures, etc. Both types of models possess the following properties:

- "color": a tuple containing an RGBA value in the format (RED, GREEN, BLUE, ALPHA), where each value is a float between 0 and 1.
- "location": a tuple representing the location of the model in space in the format (x, y, z).
- "roughness": a float value between 0 and 1 representing the roughness of the object.

Predefined models have an additional property:

- "size": the base size of the object, given as an integer.
- "scale": a tuple that is a set of multipliers for "size" that changes the height, width, and depth.
- "obj_type": a string indicating the type of object, which is one of the following: cuboid, pyramid, sphere, cone, plane, or torus.

Custom defined models have the following additional properties:

- "verts": a list of tuples representing the vertices of the object, which are points in space that the faces connect. The vertices are given in the format [(x, y, z), (x, y, z), ...].
- "faces": a list of tuples representing the vertices to connect. Each integer in each tuple represents an index of the "verts" value.

input: A house with a door and slanted roof
output: {
"create_type": "customdef",
"verts": [(4, -4, 0), (4, 4, 0), (-2, -4, 0), (-2, 4, 0), (4, -4, 2), (4, 4, 2), (-2, -4, 2), (-2, 4, 2), (-2, -3, 0), (-2, -2, 0), (-2, -3, 2), (-2, -2, 2), (1, -4, 3), (1, 4, 3)],
"faces": [(0, 1, 3, 2), (4, 5, 7, 6), (1, 3, 7, 5), (0, 2, 6, 4), (0, 1, 5, 4), (3, 7, 11, 9), (2, 6, 10, 8), (4, 5, 13, 12), (6, 7, 13, 12), (6, 4, 12), (7, 5, 13)],
"color": (0,0,0,1.0),
"location": (0,0,0),
"roughness": 1.0
}

input: Create a sphere
output: { 
"create_type": "predef", 
"color": (1.0, 0.0, 0.0, 1.0), 
"location": (0.0, 0.0, 0.0), 
"roughness": 1.0, 
"size": 1, 
"scale": (1.0, 1.0, 1.0),
"obj_type": "sphere"
} 

input: A house
output: { 
"create_type": "customdef", 
"verts":[(4, -4, 0), (4, 4, 0), (-2, -4, 0), (-2, 4, 0), (4, -4, 2), (4, 4, 2), (-2, -4, 2), (-2, 4, 2), (-2, -3, 0), (-2, -2, 0), (-2, -3, 2), (-2, -2, 2), (1, -4, 3), (1, 4, 3)], 
"faces": [(0, 1, 3, 2), (4, 5, 7, 6), (1, 3, 7, 5), (0, 2, 6, 4), (0, 1, 5, 4), (3, 7, 11, 9), (2, 6, 10, 8), (4, 5, 13, 12), (6, 7, 13, 12), (6, 4, 12), (7, 5, 13)], 
"color": (0,0,0,1.0), 
"location": (0,0,0), 
"roughness": 1.0 
} 


input: A red cube
output: {
"create_type": "predef",
"color": (1.0, 0.0, 0.0, 1.0),
"location": (0.0, 0.0, 0.0),
"roughness": 1.0,
"size": 1,
"scale": (1.0, 1.0, 1.0),
"obj_type": "cuboid"
}

input: A pyramid
output: {
"create_type": "predef",
"color": (1.0, 0.0, 0.0, 1.0),
"location": (0.0, 0.0, 0.0),
"roughness": 1.0,
"size": 1,
"scale": (1.0, 1.0, 1.0),
"obj_type": "pyramid"
}

input: A plane
output: {
"create_type": "predef",
"color": (0.0, 1.0, 0.0, 1.0),
"location": (0.0, 0.0, 0.0),
"roughness": 0.5,
"size": 1,
"scale": (1.0, 1.0, 1.0),
"obj_type": "plane"
}

input: A 4x4x4 cube
output: {
"create_type": "predef",
"color": (1.0, 0.0, 0.0, 1.0),
"location": (0.0, 0.0, 0.0),
"roughness": 1.0,
"size": 4,
"scale": (1.0, 1.0, 1.0),
"obj_type": "cuboid"
}
"""