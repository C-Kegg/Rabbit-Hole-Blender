import google.generativeai as palm

palm.configure(api_key="AIzaSyCe09OtTktAXVyuBbX3ZMxSaO5c_EzJ7iQ")

database = ""

defaults = {
  'model': 'models/chat-bison-001',
  'temperature': 0.35,
  'candidate_count': 1,
  'top_k': 40,
  'top_p': 0.95,
}
context = f"Provide information regarding the user's query based on information from the following database and any additional information that may be deemed necessary:\n{database}"
examples = []
messages = []
def run(input):
    if input == "Terminate(\"program\")":
        print("Terminating program.")
        exit()
    global context, examples, messages
    global response
    messages.append(input)
    response = palm.chat(
        **defaults,
        context=context,
        examples=examples,
        messages=messages
    )
    return response

if __name__ == "__main__":
    run("Hello.")
    while True:
        print("\n", response.last, "\n") # Response of the AI to your most recent request
        run(input())
