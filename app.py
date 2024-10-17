from flask import Flask, request, jsonify
import autogen
from autogen import AssistantAgent

app = Flask(__name__)

# Load patient persona from the file
with open("patient_1.txt", "r") as file:
    john_w_persona = file.read()

# Configuration for LLMs (ensure you have your LLM config here)
config_list = autogen.config_list_from_json("OAI_CONFIG_LIST")

# Function to detect termination messages
def termination_msg(x):
    return isinstance(x, dict) and "TERMINATE" == str(x.get("content", ""))[-9:].upper()

# Define the assistant agent with the loaded persona
llm_config = {"config_list": config_list, "timeout": 60, "temperature": 0.8, "seed": 1234}

assistant = AssistantAgent(
    name="Patient",
    system_message=john_w_persona,  # Use the persona from patient_1.txt
    llm_config=llm_config,
    description="Patient agent who answers student questions as John W."
)

# Flask route for chat interaction
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    
    # Generate a response directly from the persona-based assistant
    response = assistant.message_generator(user_input)
    
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
