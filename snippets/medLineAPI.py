import requests
import json

def getData(ncode):
  # Define the base URL for the openFDA API
  base_url = "https://connect.medlineplus.gov/service?"
  # Define the search parameters
  search_params = {
    "mainSearchCriteria.v.cs": "2.16.840.1.113883.6.69",
     "knowledgeResponseType": "application/json",  # Limit the number of results to 1
    "mainSearchCriteria.v.c":str(ncode)#"00456140530"
  }
  # Send the GET request to the openFDA API
  response = requests.get(base_url, params=search_params)
  
  # Check if the request was successful
  if response.status_code == 200:
    # Extract the data from the response
    data = response.json()
    if(data['feed']['entry']): 
    # Print out the first result's summary:
      # print("First article: ",data['feed']['entry'][0]['summary']['_value'])
      
      # Save the data to a local JSON file
      with open("data.json", "w") as file:
        # Inputs the data of the first entry including the name and the summary
        json.dump(data['feed']['entry'][0], file)
    else:
      print("Nothing found")
  
  else:
    print("Error: Failed to retrieve data from the MedLine Connect Plus API")

# Use code in the botom to test it
# ncodeValue = input("Enter the ndc Code you want to see data for: ")
# getData(ncodeValue)
