# Importing the libraries
import requests
from geopy.geocoders import Nominatim # To request the latitude and longitude from a city name
from datetime import datetime, timedelta # To format dates and get the current datetime
import pytz # To request the timezones


def get_cordinates(city):
    response = [] # Creating the response list
    geolocator = Nominatim(user_agent="get_the_lat_and_long") # Stablishing the unique identifier for the app
    
    try:
        # Get the location (latitude and longitude) of the city
        location = geolocator.geocode(city)
        
        if location: # If the location exists then get the latitude and longitude 
            latitude = location.latitude
            longitude = location.longitude

            # Inserting the latitude and longitude inside of the list
            response.append(latitude)
            response.append(longitude)
        else:
            response.append('')
            response.append('Error - Not Found')
    
        return response # Returning the response
    except Exception as e:
        return f"Error in the request: {e}"


def get_info(sunrise_or_sunset, lat, lng,timezone):
    try:
        if not (is_valid_coordinate(lat) and is_valid_coordinate(lng)):
            response = "Latitude and longitude has to be valid numbers"
            return response
        type = ['sunset','sunrise'] # Stablishing the list that have the values to check if it's sunrise or sunset selected
        response = requests.get(f"https://api.sunrise-sunset.org/json?lat={lat}&lng={lng}&tzid={timezone}")# Calling the API and returning a response from it by passing the parameters latitude, longitude and timezone(set America/Sao_Paulo as default) 
        json_response = response.json()# Getting a json type reponse from that call that I made in the variable response
        sunrise_info = json_response['results']['sunrise']# Using the json response and filtering it by the results and then the sunrise to get the sunrise info from that latitude and longitude
        sunset_info = json_response['results']['sunset']# Using the json response and filtering it by the results and then the sunset to get the sunset info from that latitude and longitude
        if sunrise_or_sunset.lower() == type[1]: # Checking if the value in lower case is equal to "sunrise"
            output = formating_outputs(sunrise_info, timezone) # Receiving a list of the formated outputs from the formating_outputs function
            # Creating a div to be inserted as a response with the values inside of the output list
            return f"""<div class='output'>
            <p>Remaining Time: {output[0]}</p>
            <p>Exact Datetime: {output[1]}</p>
            <p>Request Datetime: {output[2]}</p>
            </div>
            """
        elif sunrise_or_sunset.lower() == type[0]: # Checking if the value in lower case is equal to "sunset"
            output = formating_outputs(sunset_info, timezone)
            return f"""<div class='output'>
            <p>Remaining Time: {output[0]}</p>
            <p>Exact Datetime: {output[1]}</p>
            <p>Request Datetime: {output[2]}</p>
            </div>
            """
        else:
            if response.status_code != 200: # Receiving the status code and returning an error as response if it's not equal to 200
                response = "Error at the request while calling the API"
            return f"{response}"
    except Exception as e:
        print(f"Error in the request: {e}")


def formating_outputs(api_response, timezone):
    timezone = pytz.timezone(f"{timezone}") # Receiving the timezone
    output = []# Creating an output list

    current_datetime = datetime.now(timezone)# Get the current date and time

    # Format the date and time as d/m/y h/m/s
    date_time_format = "%d-%m-%y %H:%M:%S"
    request_datetime = current_datetime.strftime(date_time_format)

    # Formating sunrise_info to remove AM or PM and transform into 24 hours type 
    current_date = current_datetime.strftime("%d-%m-%y")
    exact_time = datetime.strptime(api_response, "%I:%M:%S %p").strftime("%H:%M:%S")

    

    #Returning the remaining time
    current_time = current_datetime.strftime("%H:%M:%S")

    # Creating objects to be able to subtract them
    current_time_obj = datetime.strptime(current_time, "%H:%M:%S") 
    exact_datetime_obj = datetime.strptime(exact_time, "%H:%M:%S")
    remaining_time =  exact_datetime_obj - current_time_obj 


    # Check if the remaining time has a negative day component if yes inserting a day on the current date
    if remaining_time.days < 0:
        current_datetime += timedelta(days=1)  
        current_date = current_datetime.strftime("%d-%m-%y")
        exact_datetime = f"{current_date} {exact_time}"
    else:
        exact_datetime = f"{current_date} {exact_time}"

    # Filtering the remaining time to only the h:m:s and transforming into a string
    remaining_time = str(remaining_time)[8:]

    # Inserting all the values in the output list
    output.append(remaining_time)
    output.append(exact_datetime)
    output.append(request_datetime)

    return output

def get_all_timezones():
    # Getting all the timezones
    all_timezones = pytz.all_timezones
    timezone_options = ''

    # Creating a loop that creates an tag <option> for each timezone and set the America/Sao_Paulo timezone as selected by default
    for tz in all_timezones:
        if tz == 'America/Sao_Paulo':
            timezone_options+= f"<option value='{tz}' selected>{tz}</option>"
        else:
            timezone_options+= f"<option value='{tz}'>{tz}</option>"
    
    return timezone_options

def is_valid_coordinate(coord):
    try:
        # Verifica se o valor pode ser convertido para float
        float_coord = float(coord)

        # Verifica se o valor está dentro dos intervalos válidos
        if -90 <= float_coord <= 90:
            return True
        else:
            return False

    except ValueError:
        return False