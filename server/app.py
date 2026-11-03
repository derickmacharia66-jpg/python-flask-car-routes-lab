from flask import Flask

app = Flask(__name__)

# List of car models currently in the Flatiron Cars fleet.
# The /<model> route checks incoming requests against this list.
existing_models = [
    "Civic",
    "Model 3",
    "Mustang",
    "Corolla",
    "F-150",
    "Crossroads"
]


@app.route('/')
def index():
    """Default route — simple welcome message."""
    return "Welcome to Flatiron Cars"


@app.route('/<model>')
def car_model(model):
    """
    Takes a model name from the URL and checks it against existing_models.
    Returns a confirmation message if the model is in the fleet,
    otherwise returns a not-found style message.
    """
    if model in existing_models:
        return f"Flatiron {model} is in our fleet!"
    else:
        return f"No models called {model} exists in our catalog"


if __name__ == '__main__':
    app.run(debug=True)
