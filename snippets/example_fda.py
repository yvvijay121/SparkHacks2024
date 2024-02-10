import requests
import json

# Define the base URL for the openFDA API
base_url = "http://api.fda.gov/drug/label.json"

# Define the search parameters
search_params = {
  "search": "openfda.unii:786Z46389E",
  "limit": 1  # Limit the number of results to 1
}

# Send the GET request to the openFDA API
response = requests.get(base_url, params=search_params)

# Check if the request was successful
if response.status_code == 200:
  # Extract the data from the response
  data = response.json()

  # Process the data as needed
  # ...

  # Save the data to a local JSON file
  with open("data.json", "w") as file:
    json.dump(data, file)

else:
  print("Error: Failed to retrieve data from the openFDA API")