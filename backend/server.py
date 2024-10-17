# from flask import Flask, request, jsonify
# import os
# from autogen import AssistantAgent, UserProxyAgent
# import json

# # Load the config_list.json file
# with open('config_list.json') as f:
#     config_list = json.load(f)

# app = Flask(__name__)

# # Load patient persona from the file
# persona_file_path = os.path.join(os.path.dirname(__file__), 'personas', 'patient_1.txt')
# with open(persona_file_path, "r", encoding="utf-8") as file:
#     john_w_persona = file.read()

# llm_config = {
#     "config_list": config_list
# }

# assistant = AssistantAgent(
#     name="John W",
#     llm_config=llm_config,
#     system_message=john_w_persona  # Use the persona loaded from the file
# )

# user_proxy = UserProxyAgent(
#     name="User",
#     code_execution_config=False
# )

# @app.route('/chat', methods=['POST'])
# def chat():
#     user_input = request.json.get("message")
    
#     # Generate response using the AssistantAgent
#     response = user_proxy.initiate_chat(
#         assistant,
#         message=user_input
#     )
    
#     # Send the response back to the frontend
#     return jsonify({"response": response["messages"][-1]["content"]})

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    
    # For testing purposes, return a simple static response
    response_message = f"You said: {user_input}. This is a test response without AutoGen."
    
    # Send the response back to the frontend
    return jsonify({"response": response_message})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
