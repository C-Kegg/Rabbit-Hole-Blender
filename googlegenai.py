"""
At the command line, only need to run once to install the package via pip:

$ pip install google-generativeai
"""

import google.generativeai as genai

apikey = "AIzaSyCe09OtTktAXVyuBbX3ZMxSaO5c_EzJ7iQ" # Only use this key for Dragons-related projects

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

input = input("Type what you want built now\n")

prompt = """Create a JSON object containing a "verts" object and a "faces" object, each of which is composed of a list of tuples. Each integer in each "faces" tuple corresponds to an index of a tuple in the "verts" object. Each tuple in the "verts" object represents a point in a 3D model, with (x, y, z) (0, 0 ,0) being the center of the model. y is back, x is right, and z is up. Combined and processed, the "verts" and "faces" form a 3D model. Consider it a 3D connect-the-dots, which each tuple in the "verts" variable being a point in space, and each face connecting the "verts" based on the index.
input: A cube 2 units cubed
output: {
    verts: [(0,0,0), (0,2,0), (2,2,0),(2,0,0),(0,0,2),(0,2,2),(2,2,2),(2,0,2)],
    faces: [(0,1,2,3),(7,6,5,4),(0,4,5,1),(1,5,6,2),(2,6,7,3),(3,7,4,9)]
}

input: An upside-down pyramid with height 2
output: {
    verts: [(0,0,0),(0,1,2),(-1,0,2),(1,0,2),(0,-1,2)],
    faces: [(0,1,2),(0,3,1),(0,3,4),(2,4,0),(1,2,4,3)]
}

input: A cube 3 cubic units in size
output: {
    verts: [(0,0,0), (0,3,0), (3,3,0),(3,0,0),(0,0,3),(0,3,3),(3,3,3),(3,0,3)],
    faces: [(0,1,2,3),(7,6,5,4),(0,4,5,1),(1,5,6,2),(2,6,7,3),(3,7,4,9)]
}
input: Create a four-sided pyramid with a base 9 units squared and a height of 2 units
output: {
    verts: [(0, 0, 0), (1.5, 1.5, 2), (3, 3, 0), (3, 0, 0), (0, 3, 0)],
    faces: [(0, 1, 3), (0, 1, 4), (1, 2, 3), (1, 2, 4), (0, 2, 3, 4)]
}

input: Create a house with a door and a slanted roof

output: {
    verts:[(4, -4, 0), (4, 4, 0), (-2, -4, 0), (-2, 4, 0), (4, -4, 2), (4, 4, 2), (-2, -4, 2), (-2, 4, 2), (-2, -3, 0), (-2, -2, 0), (-2, -3, 2), (-2, -2, 2), (1, -4, 3), (1, 4, 3)],
    faces: [(0, 1, 3, 2), (4, 5, 7, 6), (1, 3, 7, 5), (0, 2, 6, 4), (0, 1, 5, 4), (3, 7, 11, 9), (2, 6, 10, 8), (4, 5, 13, 12), (6, 7, 13, 12), (6, 4, 12), (7, 5, 13)]
}
input: """ + input + """
output:""""""
""" # This essentially trains the model

response = genai.generate_text(
  **defaults,
  prompt=prompt
)

print(response.result)