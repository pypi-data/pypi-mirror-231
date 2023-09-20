from promptflow import tool
from promptflow.connections import CustomConnection
import json
import requests


@tool
def analyze_conversation(connection: CustomConnection, input_text: str, clu_endpoint: str, project_name: str, deployment_name: str) -> dict:
    # Replace with your tool code.
    # Usually connection contains configs to connect to an API.
    # Use CustomConnection is a dict. You can use it like: connection.api_key, connection.api_base
    # Not all tools need a connection. You can remove it if you don't need it.
    clu_key = connection.LanguageResourceKey
    clu_response = call_clu(input_text, clu_key, clu_endpoint, project_name, deployment_name)
    return clu_response


def call_clu(query: str, clu_key: str, clu_endpoint: str, project_name: str, deployment_name: str) -> dict:
    headers = { "Ocp-Apim-Subscription-Key": clu_key }
    request_body = {
              "kind": "Conversation",
              "analysisInput": {
                  "conversationItem": {
                      "participantId": "1",
                      "id": "1",
                      "modality": "text",
                      "language": "en",
                      "text": query
                  },
                  "isLoggingEnabled": False
              },
              "parameters": {
                  "projectName": project_name,
                  "deploymentName": deployment_name,
                  "verbose": True
              }
          }
    response = requests.post(clu_endpoint, json=request_body, headers=headers, timeout=None)
    response_json = response.json()
    return response_json