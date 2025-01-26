import requests
import json

def get_gemini_response(inp):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=AIzaSyDyCzxTmxVnTVh9_BVjgeOvfgXwwRx-7ZA"
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        "contents": [{
            "parts": [{"text": inp}]
        }]
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        return response.json()
    else:
        return f"Error: {response.status_code}"
