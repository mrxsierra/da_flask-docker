# app.py
from flask import Flask, render_template, send_from_directory
import os
import pandas as pd
from scripts.analyze_data import analyze_data  # Import the analyze_data function

app = Flask(__name__)

# Serve static files route
@app.route('/static/<path:filename>')
def serve_static(filename):
    """
    Serve static files from the 'static' directory.

    Args:
        filename (str): The name of the file to be served.

    Returns:
        flask.Response: The response containing the requested static file.
    """
    root_dir = os.path.dirname(os.getcwd())
    return send_from_directory(os.path.join(root_dir, 'static'), filename)

# Main route
@app.route('/')
def index():
    """
    Main route to display the index page with analysis results.

    Returns:
        str: Rendered HTML page.
    """
    # Call analyze_data function to generate analysis results
    analysis_results = analyze_data()

    # Render HTML page with the scatter plot and analysis results
    return render_template('index.html', results=analysis_results)

if __name__ == '__main__':
    # Run the Flask app in debug mode if the script is executed directly
    app.run(debug=True)
