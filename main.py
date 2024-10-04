import requests
import gradio as gr

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mixtral-8x7B-Instruct-v0.1"
headers = {"Authorization": "Bearer hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
def myFunc(message,history):	
    output = query({
        "parameters": {"max_new_tokens": 500},
        "inputs": f"give only sufficient answer nothing extra{message}",
    })

    return (output[0]['generated_text'])

demo = gr.ChatInterface(fn=myFunc, examples=["code linear search", "merge sort in python", "quote of the day"], title="Chatbot")
demo.launch()