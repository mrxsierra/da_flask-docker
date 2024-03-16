# scripts/analyze_data.py
import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

def analyze_data():
    """
    Analyzes a dataset and returns summary statistics, a correlation matrix, and a scatter plot.

    Returns:
        dict: A dictionary containing the analysis results.
              - 'summary_stats': HTML representation of summary statistics.
              - 'correlation_matrix': HTML representation of the correlation matrix.
              - 'plot_path': Path to the saved scatter plot image.
    """
    dataset_filename = "kc_house_data.csv"

    # Get the directory of the current script
    script_directory = os.path.dirname(os.path.realpath(__file__))

    # Construct the full path to the dataset file
    dataset_path = os.path.join(script_directory, '..', 'data', dataset_filename)

    print(f"Attempting to load file from: {dataset_path}")

    # Check if the file exists
    if not os.path.isfile(dataset_path):
        print(f"Error: The file {dataset_filename} was not found at {dataset_path}.")
        return None

    # Load the dataset
    data = pd.read_csv(dataset_path)
    
    # Remove the 'date' column from the dataset
    data.drop("date", axis=1, inplace=True)

    # Perform analysis (replace this with your actual analysis)
    summary_stats = data.describe().round(2)
    correlation_matrix = data.corr().round(2)

    # Visualize data without triggering Matplotlib GUI
    fig, ax = plt.subplots()
    ax.scatter(data['sqft_living'], data['price'])
    ax.set_title('Scatter Plot')
    ax.set_xlabel('X-axis')
    ax.set_ylabel('Y-axis')

    # Save the plot as a static file
    plot_path = os.path.join(script_directory, '..', 'static', 'scatter_plot.png')
    fig.savefig(plot_path)
    plt.close(fig)  # Close the figure to avoid displaying it in Flask

    # Return analysis results
    return {
        'summary_stats': summary_stats.to_html(),
        'correlation_matrix': correlation_matrix.to_html(),
        'plot_path': plot_path
    }

if __name__ == "__main__":
    # If the script is run directly, perform the analysis
    analyze_data()
