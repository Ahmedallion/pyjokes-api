# Pyjokes API

[![Pyjokes Logo](images/pyjokes.png)](https://github.com/pyjokes/pyjokes)

This is a simple Flask application that provides a random joke through an API using the Pyjokes library. The application includes routes for documentation and fetching a joke, with proper error handling.

## Features

- **Redirects**:
  - `/` redirects to `/docs/`.
  - `/joke/` redirects to `/joke`.
- **Documentation**:
  - `/docs` and `/docs/` provide information about the available routes.
- **Random Joke**:
  - `/joke` returns a random joke in JSON format using the `pyjokes` library. It accepts an optional `lang` parameter to specify the language of the joke.

## Requirements

- Python 3.x
- Flask
- pyjokes

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Ahmedallion/pyjokes-api.git
   cd pyjokes-api
   ```

2. **Create a virtual environment and activate it**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```bash
   pip install flask pyjokes
   ```

## Running the Application

1. **Start the Flask server**:
   ```bash
   python app.py
   ```

2. **Access the application**:
   - Open a web browser and navigate to `http://127.0.0.1:5000/`.

## API Endpoints

- **Root**: `/`
  - Redirects to the documentation page.
- **Documentation**: `/docs` or `/docs/`
  - Provides information about the available routes.
- **Joke**: `/joke`
  - Returns a random joke in JSON format. Accepts an optional `lang` parameter to specify the language of the joke.
- **Joke Redirect**: `/joke/`
  - Redirects to `/joke`.

## Example Responses

- **Documentation** (`GET /docs`):
  ```json
  {
      "routes": {
          "/": {
              "description": "Redirects to the docs page."
          },
          "/docs": {
              "description": "Shows the routes for this API."
          },
          "/joke": {
              "description": "Tells a random joke.",
              "parameters": {
                  "lang": {
                      "description": "Specifies the language of the joke.",
                      "valid_options": "'en', 'de', 'es', 'gl', 'eu'', 'it'"
                  }
              }
          }
      }
  }
  ```

- **Random Joke** (`GET /joke`):
  ```json
  {
      "joke": "Ubuntu users are apt to get this joke."
  }
  ```
