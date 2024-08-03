import pandas as pd
import requests
import json

# Load the dataset
dataset = pd.read_excel('Store Sales.xlsx')

# Replace NaN values with 0
dataset = dataset.fillna(0)

# Convert any Timestamp objects to strings
dataset = dataset.applymap(lambda x: x.isoformat() if isinstance(x, pd.Timestamp) else x)

# Extract column names (fields) and values
input_fields = dataset.columns.tolist()
input_values = dataset.values.tolist()

API_KEY = "3dite7RgTKdjvSlnJgLDo8a8aVfA-GcgeLgTWLwJHzgw"  # Replace with your actual API key
token_response = requests.post(
    'https://iam.cloud.ibm.com/identity/token',
    data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'}
)
if token_response.status_code == 200:
    mltoken = token_response.json()["access_token"]
else:
    print("Failed to get token:", token_response.text)
    exit()

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

payload_scoring = {
    "input_data": [
        {
            "fields": input_fields,
            "values": input_values
        }
    ]
}

# Use the public endpoint
response_scoring = requests.post(
    'https://us-south.ml.cloud.ibm.com/ml/v4/deployments/febf3af9-db65-4a8b-a91e-d465b6defd45/predictions?version=2021-05-01',
    json=payload_scoring,
    headers=header
)

if response_scoring.status_code == 200:
    results = response_scoring.json()["predictions"][0]["values"]
    print("Scoring response")
    print(results)

    # Convert results to DataFrame and save as CSV
    results_df = pd.DataFrame(results, columns=["Predictions"])
    results_df.to_csv('Scoring_Results.csv', index=False)
    print("Results saved to Scoring_Results.csv")
else:
    print("Failed to get prediction:", response_scoring.text)
