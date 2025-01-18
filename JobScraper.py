import requests

# Your Indeed Publisher API Key
publisher_id = #going to get api key for this

# Indeed API URL
url = 'http://api.indeed.com/ads/apisearch'

# Parameters for the API call
params = {
    'publisher': publisher_id,   # Your Publisher ID
    'q': 'Release Engineer',        # Job search term
    'l': 'Boston',              # Location
    'sort': 'date',               # Sort by date (optional)
    'format': 'json'              # Return JSON data
}

# Send GET request to Indeed API
response = requests.get(url, params=params)

# If the request was successful, process the data
if response.status_code == 200:
    data = response.json()
    jobs = data.get('results', [])
    for job in jobs:
        print(f"Job Title: {job['Release Engineer']}")
        print(f"Company: {job['company']}")
        print(f"Location: {job['formattedLocation']}")
        print(f"Job Link: {job['url']}\n")
else:
    print(f"Error fetching data: {response.status_code}")
