# Import the necessary modules
from flask import Flask
from datetime import datetime
import pytz
# Create a new Flask application instance

app = Flask(__name__)

# Define a route for the root URL ("/") that returns "Hello World"

@app.route('/')
def home():
    return "Enter endpoint '/David_Woolston' or '/datetime'"
    
@app.route('/David_Woolston') # The content in ('<content>') is our endpoint.
def hello_world():
    # This function will be called when someone accesses the root URL
    return 'Hello World from David Woolston'

# Run the application if this script is being run directly

@app.route('/datetime')
def get_current_datetime():
    pacific_tz = pytz.timezone('US/Pacific')
    pacific_datetime = datetime.now(pacific_tz)
    return f"{pacific_datetime.strftime('%Y-%m-%d %H:%M:%S')}"

if __name__ == '__main__':
    # The host is set to '0.0.0.0' to make the app accessible from any IP address.
    # The default port is 5000
    app.run(host='0.0.0.0', port=5000)
