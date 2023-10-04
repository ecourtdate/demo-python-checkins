from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import requests
import os

app = Flask(__name__)

# Configuration for the API
API_URL = os.getenv('API_URL')
API_CLIENT = os.getenv('API_CLIENT')
API_SECRET = os.getenv('API_SECRET')

@app.route('/checkin', methods=['POST'])
def checkin():

    # Get an access token
    auth = authenticate()

    if auth.get('access_token') is None:
        return jsonify({"error": "Unable to authenticate with the API"}), 500

    # Extract the search query from the request
    data = request.json

    # Set the authorization headers
    headers = set_headers(auth)

    contact = get_contact(headers, data)

    event = get_event(headers, contact)

    response = checkin_event(headers, data, event)

    if response is None:
        return jsonify({"error": "Unable to check-in the visitor"}), 400

    if response['uuid'] is not None:
        print(response)
        return jsonify({"message": "Visitor checked-in successfully"}), 201


def get_request(path, headers, params):

    # Make a GET request to the ECD API
    response = requests.get(f"{API_URL}v1/{path}", headers=headers, params=params)

    if response.status_code != 200:
        print(response.json())
        return

    results = response.json()

    if len(results) == 0:
        return

    return results[0]

def post_request(path, headers, json):

    # Make a POST request to the ECD API
    response = requests.post(f"{API_URL}v1/{path}", headers=headers, json=json)

    if response.status_code != 201:
        print(response.json())
        return

    return response.json()

def get_contact(headers, data):

    if(data is None):
        return

    if(data.get('search') is None):
        return

    params = set_contact_params(data.get('search'))

    # Search ECD API for known contacts based on a phone or email
    return get_request("contacts", headers, params)

def set_contact_params(search):

    return {
    "contact": search,
    "limit": 1
    }

def get_event(headers, contact):

    if(contact is None):
        return

    # Check the client UUID from the get_contact results
    if(contact['client'] is None):
        return

    params = set_event_params(contact)

    # Search ECD API for events based on the client UUID
    return get_request("events", headers, params)

def set_event_params(contact):

    now = datetime.now()

    return {
        "limit": 1,
        "client": contact['client'],
        "from_date": (now - timedelta(days=1)).strftime("%Y-%m-%d"),
        "to_date": (now + timedelta(days=1)).strftime("%Y-%m-%d")
    }

def checkin_event(headers, data, event):

    # Post request to check-in the visitor
    response = post_request("checkins", headers, set_checkin(data, event))

    return response


def set_checkin(data, event):

    json = {
       "name": data.get('name'),
       "phone": data.get('phone'),
       "email": data.get('email'),
       "location": data.get('location'),
       "language": data.get('language'),
       "service": data.get('service'),
       "department": data.get('department'),
       "notes": data.get('notes'),
       "status": "checked-in"
    }

    if event['uuid'] is not None:
        json['event'] = event['uuid']

    return json

def set_headers(auth):

    # Set the access token in the headers
    return {
        'Authorization': f"Bearer {auth.get('access_token')}",
        'Accept': 'application/json',
    }

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
