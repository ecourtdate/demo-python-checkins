from flask import Flask, request, jsonify
import os
import requests

app = Flask(__name__)

# Configuration for the API
API_URL = os.getenv('API_URL')
API_CLIENT = os.getenv('API_CLIENT')
API_SECRET = os.getenv('API_SECRET')

@app.route('/', methods=['POST', 'GET'])
def search_client():
    # Extract the search term from the request JSON
    request_data = request.json
    search = request_data.get('search')

    # Make a request to the API for client search
    response = requests.get(f"v1/{API_URL}search", params={'search': search})

    if response.status_code == 200:
        results = response.json()
        return jsonify(results)
    else:
        return jsonify({"error": "Unable to search for clients"}), 500

def authenticate():

    post = {
       'client_id': API_CLIENT,
       'client_secret': API_SECRET
    }

    # Post request to generate an access token
    response = requests.post(f"{API_URL}oauth/token", json=post)

    if response.status_code == 201:
        return response.json()
    else:
        return response.status_code

if __name__ == '__main__':
    app.run(debug=True)
