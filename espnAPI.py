import json

# Function that shows headlines
def show_headlines(headlines):
    if len(headlines) == 0:
        print("No headlines available!")
    else:
        print("Here are the latest headlines:")
        for headline in headlines:
            print("-", headline)

# Function that shows teams
def show_teams(nicknames):
    if len(nicknames) == 0:
        print("No nicknames available!")
    else:
        print("Here are the nicknames:")
        for nickname in nicknames:
            print(nickname)

# Function that shows dates
def show_dates(dates):
    if len(dates) == 0:
        print("No Dates available!")
    else:
        print("Here are the Dates:")
        for date in dates:
            print(date)    


command = input("What would you like to look at? (News, Teams, Dates): ").lower()

if command == "news":
    with open('nflnews.json') as file: # Opens file and makes it a variable. Learned from geeksforgeeks https://www.geeksforgeeks.org/read-json-file-using-python/
        content = file.read() # Reads file
        if content.strip() == '': # Removes all leading and trailing whitespace (spaces, tabs, newlines) from the file content. Learned from W3Schools https://www.w3schools.com/python/ref_string_strip.asp
            print("News file is empty!")
        else:   
            news_headlines = [] # List of headlines

            data = json.loads(content)  # The json.loads() method of JSON module is used to parse a valid JSON string and convert it into a Python dictionary. https://www.geeksforgeeks.org/json-loads-in-python/
            for item in data['articles']: # Loops through each article in JSON article list
                news_headlines.append(item['headline']) # Takes each headline from every article and adds it to news_headlines list
            show_headlines(news_headlines) # Prints headlines

elif command == "teams":
    with open('nflteams.json') as file:# Opens file and makes it a variable. Learned from geeksforgeeks https://www.geeksforgeeks.org/read-json-file-using-python/
        content = file.read()
        if content.strip() == '': # Removes all leading and trailing whitespace (spaces, tabs, newlines) from the file content. Learned from W3Schools https://www.w3schools.com/python/ref_string_strip.asp
            print("Teams file is empty!")
        else:
            team_info = [] # List of teams

            data = json.loads(content) # The json.loads() method of JSON module is used to parse a valid JSON string and convert it into a Python dictionary. https://www.geeksforgeeks.org/json-loads-in-python/
            for sport in data['sports']:
                for league in sport['leagues']:
                    for teams in league['teams']:
                        team = teams['team']
                        team_info.append(team['location'] + " " + team['nickname'])
            show_teams(team_info)

elif command == "dates":
    with open('nfldates.json') as file: # Opens file and makes it a variable. Learned from geeksforgeeks https://www.geeksforgeeks.org/read-json-file-using-python/
        content = file.read()
        if content.strip() == '': # Removes all leading and trailing whitespace (spaces, tabs, newlines) from the file content. Learned from W3Schools https://www.w3schools.com/python/ref_string_strip.asp
            print("Dates file is empty!")
        else:
            weeks = [] # List of dates

            data = json.loads(content)  # The json.loads() method of JSON module is used to parse a valid JSON string and convert it into a Python dictionary. https://www.geeksforgeeks.org/json-loads-in-python/
            for league in data['leagues']:
                for calender in league['calenders']:
                    for entry in calender['entries']:
                        weeks.append(entry['label'] + " " + entry['detail'])
            show_dates(weeks)

else:
    print("Something went wrong! Make sure you choose one of News, Teams or Dates.")
