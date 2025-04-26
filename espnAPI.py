import requests
import json
# Open and read the JSON file

with open('nflteams.json') as file:
    content = file.read()
    print(f"File content: '{content}'")  # Debugging line

    if content.strip() == '':
        print("The file is empty! Can't parse empty JSON.")
    else:
        data = json.load(content)
        print(data)