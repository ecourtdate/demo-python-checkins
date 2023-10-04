# Sample Flask Python Check-in App integrated with eCourtDate API

This README provides instructions and information about a sample Flask Check-in application written in Python that demonstrates how to integrate with the [eCourtDate API](https://docs.ecourtdate.com). This sample code will showcase how to use the API to perform the following actions:

1. Search for an existing client.
2. Retrieve any scheduled events for the client.
3. Check-in the client for a given event.
4. Update the check-in status for the event.
5. Trigger one-off messages to any recipients.

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

### Configuration

You need to configure the Sample API endpoints and authentication details. Create a `.env` file in the project directory with the following content:

```ini
API_BASE_URL=https://api.sampleapp.com
API_CLIENT=client_id
API_TOKEN=client_token
```

Replace `client_id` and `client_token` with your API credentials from the [Console APIs](https://console.ecourtdate.com/apis) page.

## Usage

To run the sample app, execute the following command from the project directory:

```bash
python app.py
```

This will start the Flask development server, and you should see output indicating that the server is running. By default, the app will be accessible at `http://localhost:5000` in your web browser.

## API Integration

The demo app provides the following endpoints for interacting with the Sample API:

- `/search`: Search for an existing client.
- `/check-in`: Check-in a client.
- `/notify`: Send a one-off message.

You can access these endpoints by making HTTP requests to the Flask app. You can use tools like `curl`, Postman, or create a frontend application to interact with the API endpoints.

## Contributing

If you would like to contribute to this demo app or report issues, please contact our development team at dev@ecourtdate.com.

## License

This demo Flask Python app is open-source and available under the [MIT License](LICENSE). You are free to use, modify, and distribute it as per the terms of the license.
