import requests

class ObsidianFlow:
    def __init__(self, api_key, namespace):
        self.api_key = api_key
        self.namespace = namespace

    def ingest():
        print('to be implemented')
    
    def chat(self, messages, include_sources=True):
        # Define the API endpoint URL
        api_url = "https://public-api-seven.vercel.app/api/v1.0/chat"

        # Define the headers, including the API key if required
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",  # Replace with your API key
        }

        # Create the request payload
        payload = {
            "messages": messages,
            "namespaceId": self.namespace,
            "includeSources": include_sources,
        }

        # Send the POST request
        try:
            response = requests.post(api_url, json=payload, headers=headers)

            # Check if the request was successful (HTTP status code 200)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Request failed with status code {response.status_code}: {response.text}")
                return None

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None


