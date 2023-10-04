# Sample Flask Python Check-in App integrated with eCourtDate API

This README provides instructions and information about a sample Flask Check-in application written in Python that demonstrates how to use the [eCourtDate API](https://docs.ecourtdate.com) to check in visitors to a location. Check-ins can be performed by searching for a client based on a phone number or email address or as a guest based on provided information.

Depending on the eCourtDate agency's [Auto Messages](https://staging.ecourtdate.com/auto_messages), the eCourtDate API can be configured to automatically send omnichannel (SMS, MMS, email, voice, chat) and multilingual messages to the client, guest, and staff members. 

The messages can be customized to include the location's name, address, and other information.

To avoid sending live messages when developing, we recommend using the [staging API](https://devs.ecourtdate.com) where all outbound messages are simulated and not sent to the recipient.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [Usage](#usage)
- [API Integration](#api-integration)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you can run the sample app, make sure you have the following prerequisites installed on your system:

- Python (3.7 or higher): [Python Installation Guide](https://www.python.org/downloads/)
- Flask: You can install Flask using pip:

```bash
pip install -r requirements.txt
```

## Getting Started

### Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/ecourtdate/demo-python-checkins.git
```

2. Change to the project directory:

```bash
cd demo-python-checkins
```

3. From there we recommend creating a [virtualenv](https://docs.python.org/3/library/venv.html) and activating it to avoid installing dependencies globally on your computer.

   `virtualenv -p python3 env`
   `source env/bin/activate`

4. Install dependencies:

   `pip install -r requirements.txt`

### Configuration

You need to configure the eCourtDate API endpoints and authentication details. Create a `.env` file in the project directory with the following content:

```ini
ECDAPI_URL=https://staging.api.ecourtdate.com/
ECDAPI_CLIENT=client_id
ECDAPI_SECRET=client_secret`
```

Replace `client_id` and `client_secret` with your API credentials from the [Console APIs](https://console.ecourtdate.com/apis) page.

## Usage

To run the sample app, execute the following command from the project directory:

```bash
python app.py
```

This will start the Flask development server, and you should see output indicating that the server is running. Open the app in an API client like [Postman](https://www.postman.com/) or [Insomnia](https://insomnia.rest/). The app will be accessible at `http://localhost:5000` by default.

## API Integration

The app demonstrates the following endpoints to check in a visitor to a location:

- `/contacts`: Use the [Get Contacts](https://docs.ecourtdate.com/#tag/Contacts/operation/GetContacts) endpoint for a client based on a given phone number or email address.
- `/events`: If a client is found, use the [Get Events](https://docs.ecourtdate.com/#tag/Events/operation/GetEvents) endpoint to search if there are any current events.
- `/checkins`: Use the [Post Checkins](https://docs.ecourtdate.com/#tag/Checkins/operation/PostCheckins) endpoint to create a check in.

You can access these endpoints by making HTTP requests to the Flask app. You can use tools like `curl`, Postman, or create a frontend application to interact with the API endpoints.

## Contributing

If you would like to contribute to this demo app or report issues, please contact our development team at dev@ecourtdate.com.

## License

This demo Flask Python app is open-source and available under the [MIT License](LICENSE). You are free to use, modify, and distribute it as per the terms of the license.
