import requests

def main():
    # Specify the URL you want to connect to
    url = 'https://vistadev.itch.io/'

    try:
        # Send a GET request to the specified URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Print the response content
            print("Response from", url)
            print(response.content.decode('utf-8'))  # Decode the content to a string
        else:
            print("Failed to retrieve data. Status code:", response.status_code)

    except requests.exceptions.RequestException as e:
        # Handle any errors that occur during the request
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
