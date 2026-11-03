# Flatiron Cars — Flask Routes Lab

A small Flask app that serves two routes for a car company.

## Routes

- **`GET /`** — returns `Welcome to Flatiron Cars`
- **`GET /<model>`** — checks the given `model` against the fleet's
  `existing_models` list:
  - If the model is in the fleet: `Flatiron {model} is in our fleet!`
  - If it isn't: `No models called {model} exists in our catalog`

## Running locally

```bash
pip install flask
python app.py
```

The app runs at `http://127.0.0.1:5000`.

## Example

```
GET /Civic      -> "Flatiron Civic is in our fleet!"
GET /Tesla      -> "No models called Tesla exists in our catalog"
```

<!-- Add a screenshot of the running app / a terminal curl example here -->