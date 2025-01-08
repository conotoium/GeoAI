# Modules
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
from geopy.geocoders import Nominatim

# Gemini API
apikey = os.environ.get("GOOGLE_API_KEY")
if not apikey:
    apikey = input("Please enter your API key: ")

genai.configure(api_key=apikey)
model = genai.GenerativeModel("gemini-1.5-flash")


# Geocode Input
geolocator = Nominatim(user_agent="conto_locator")

print("\nGeoAi, a Trip Planning tool by Contonium365.\n")
locat = input("Insert your location here:  ")
ppl = input("How many people will be going to this location?: ")
daycount = input("How many days do you expect to be at this location for?: ")
bugit = input("What do you estimate your maximum budget for this location to be?: ")
location = geolocator.geocode(locat)

print(f"\nLocation: {location.address}\nPeople: {ppl}\nDays: {daycount}\nMax Budget: {bugit}\n")

leave = ["q", "quit"]

chat = model.start_chat()

quest1 = (f"Describe the following location in a general sense, with any costs represented in AUD, including local attractions(include admission cost details), accomodation costs(include hotels, airbnbs, motels, etc) costs, food costs, public transport. Then give estimates for a day's cost, ranging from low to high.\n The Location is {location.address}. The number of people going is {ppl}, The time in days at the location is {daycount}, The estimated maximum budget is {bugit} AUD. Use the github style markdown format and utilise tables and colours, fonts to make it look nice.")

try:
    response = chat.send_message(quest1)
    for chunk in response:
        print(chunk.text, end="")
        with open('conversation.html', 'w') as myFile:
            myFile.write(f"{chunk.text}")
            print(f"\nThat was the summary for {location.address}\n")
except Exception as e:
    print(f"Error: {e}")
