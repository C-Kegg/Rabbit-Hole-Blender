"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai

apikey = "API_KEY" # Use your key here

genai.configure(api_key=apikey)

defaults = {
  'model': 'models/text-bison-001',
  'temperature': 0.7, # This is how creative the model is. It has a maximum value of 1 and a minimum of 0
  'candidate_count': 1, # This is how many responses the model gives
  'top_k': 40, # Don't mess with this
  'top_p': 0.95, # Or this
  'max_output_tokens': 32768, # Maximum number of characters in response. Make this number larger for more complex requests/responses
  'stop_sequences': [],
  'safety_settings': [{"category":"HARM_CATEGORY_DEROGATORY","threshold":"BLOCK_LOW_AND_ABOVE"},{"category":"HARM_CATEGORY_TOXICITY","threshold":"BLOCK_LOW_AND_ABOVE"},{"category":"HARM_CATEGORY_VIOLENCE","threshold":"BLOCK_MEDIUM_AND_ABOVE"},{"category":"HARM_CATEGORY_SEXUAL","threshold":"BLOCK_MEDIUM_AND_ABOVE"},{"category":"HARM_CATEGORY_MEDICAL","threshold":"BLOCK_MEDIUM_AND_ABOVE"},{"category":"HARM_CATEGORY_DANGEROUS","threshold":"BLOCK_MEDIUM_AND_ABOVE"}],
}

def run(input, prompt="default"):

    if input == "Terminate(\"program\")":
        print("Terminating program.")
        exit()
    if prompt == "default":
        prompt = """Create a JSON object containing a "verts" object and a "faces" object, each of which is composed of a list of tuples. Each integer in each "faces" tuple corresponds to an index of a tuple in the "verts" object. Each tuple in the "verts" object represents a point in a 3D model, with (x, y, z) (0, 0 ,0) being the center of the model. y is back, x is right, and z is up. Combined and processed, the "verts" and "faces" form a 3D model. Consider it a 3D connect-the-dots, in which each tuple in the "verts" variable being a point in space, and each face connecting the "verts" based on the index. The "color" variable is a tuple representing an RGB value + an alpha value, default (0, 0, 0, 0.5), with (RED, GREEN, BLUE, ALPHA). "sphere" is a varible specifically used for spheres. If the object is not a sphere, then the value is false. If the object is a sphere, the values of "verts" and "faces" are false, and the value of "sphere" is an integer representing the radius of the sphere.
input: A cube 2 units cubed
output: {
    verts: [(0,0,0), (0,2,0), (2,2,0),(2,0,0),(0,0,2),(0,2,2),(2,2,2),(2,0,2)],
    faces: [(0,1,2,3),(7,6,5,4),(0,4,5,1),(1,5,6,2),(2,6,7,3),(3,7,4,9)],
    color: (0, 0, 0, 1.0),
    sphere: false
}

input: An upside-down pyramid with height 2
output: {
    verts: [(0,0,0),(0,1,2),(-1,0,2),(1,0,2),(0,-1,2)],
    faces: [(0,1,2),(0,3,1),(0,3,4),(2,4,0),(1,2,4,3)],
    color: (0, 0, 0, 1.0),
    sphere: false
}

input: A cube 3 cubic units in size
output: {
    verts: [(0,0,0), (0,3,0), (3,3,0),(3,0,0),(0,0,3),(0,3,3),(3,3,3),(3,0,3)],
    faces: [(0,1,2,3),(7,6,5,4),(0,4,5,1),(1,5,6,2),(2,6,7,3),(3,7,4,9)]
    color: (0, 0, 0, 1.0),
    sphere: false
}
input: Create a four-sided pyramid with a base 9 units squared and a height of 2 units
output: {
    verts: [(0, 0, 0), (1.5, 1.5, 2), (3, 3, 0), (3, 0, 0), (0, 3, 0)],
    faces: [(0, 1, 3), (0, 1, 4), (1, 2, 3), (1, 2, 4), (0, 2, 3, 4)],
    run_cmd: false
}

input: Create a house with a door and a slanted roof

output: {
    verts:[(4, -4, 0), (4, 4, 0), (-2, -4, 0), (-2, 4, 0), (4, -4, 2), (4, 4, 2), (-2, -4, 2), (-2, 4, 2), (-2, -3, 0), (-2, -2, 0), (-2, -3, 2), (-2, -2, 2), (1, -4, 3), (1, 4, 3)],
    faces: [(0, 1, 3, 2), (4, 5, 7, 6), (1, 3, 7, 5), (0, 2, 6, 4), (0, 1, 5, 4), (3, 7, 11, 9), (2, 6, 10, 8), (4, 5, 13, 12), (6, 7, 13, 12), (6, 4, 12), (7, 5, 13)],
    run_cmd: false
}

input: Create a sphere 2 units wide

output: {
    verts: false,
    faces: false,
    color: (0, 0, 0, 1.0),
    sphere: 1
}
input: """ + input + """
output:""""""
""" # This essentially trains the model
    else:
        prompt += "input: " + input + "\noutput:"""""""

    response = genai.generate_text(
        **defaults,
        prompt=prompt
    )
    t = response.result
    while t[0] != "{":
        t.replace(t[0], "", 1)
    
    return t

if __name__ == "__main__":
    while True:
        run(input("What do you want built?\n"))
