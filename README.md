Store Sales Prediction Scoring Script

This repository includes a Python script called 2.py that automates the scoring of store sales data using IBM Watson Machine Learning. The script reads data from an Excel file, cleans and formats it, sends it to an IBM Cloud Machine Learning endpoint to generate predictions, and finally saves those predictions in a CSV file.

The project directory contains three key files:

1. 2.py: The Python script responsible for data loading, preprocessing, authentication, sending scoring requests, and saving the output.
2. Store Sales.xlsx: The input dataset with historical or current store sales information used for prediction.
3. Scoring\_Results.csv: The output file where the model’s predicted sales values are stored.

Before running the script, you will need:

• Python version 3.7 or later installed on your machine.
• An IBM Cloud account with the Watson Machine Learning service enabled.
• The following Python packages installed: pandas, requests, and openpyxl.

To set up the project:

1. Clone the repository to your local machine and change into the project directory.
2. (Optional) Create and activate a virtual environment for Python dependencies.
3. Install the required packages by running pip install pandas requests openpyxl.

Next, configure the script:

1. Obtain an API key from your IBM Cloud account for Watson Machine Learning.
2. Open 2.py and replace the placeholder API\_KEY value with your actual IBM Cloud API key.
3. Ensure that the URL in the script references your specific deployment ID and version number for the Watson ML deployment.

To run the script, simply execute python 2.py from the command line. The script will:

1. Load and preprocess the data from Store Sales.xlsx by replacing missing values with zeros and converting timestamps to strings.
2. Authenticate against IBM Cloud to obtain an access token using your API key.
3. Send the prepared data to the Watson ML scoring endpoint associated with your deployment.
4. Receive the prediction results and display them in the console.
5. Save the predictions to a file named Scoring\_Results.csv, with a single column labeled “Predictions.”

If any errors occur during execution, check the following:

• Failed to get token: Make sure your API key is valid and you have an active internet connection.
• Failed to get prediction: Verify your deployment ID, version number, and ensure that your Watson ML deployment is active and accessible.

This project is released under the MIT License. For more information, see the LICENSE file in the repository.

Created by Sugam Nema.

