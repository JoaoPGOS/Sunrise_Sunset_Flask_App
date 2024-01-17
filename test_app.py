import functions

def invalid_latitude_or_longitude():
    invalid_response = functions.get_info('Sunrise','-10','invalid','America/Sao_Paulo')
    expected_response = "Latitude and longitude has to be valid numbers"
    
    if invalid_response == expected_response:
        print("Test Done, an error response was returned correctly to the user \n",invalid_response)
        print('-'*100)

def valid_latitude_or_longitude():
    valid_response = functions.get_info('Sunrise','-10','-10.456700','America/Sao_Paulo')
    invalid_response = "Latitude and longitude has to be valid numbers"
    
    if valid_response != invalid_response:
        print("Test Done, the correct response was returned to the user")
        print(valid_response)
        print('-'*100)

def invalid_get_lng_and_lat():
    invalid_response = functions.get_cordinates('kjsfhkjsdfh')
    expected_response = "Error - Not Found"
    

    if invalid_response[1] == expected_response:
        print("Test Done, an error response was returned correctly to the user \n",invalid_response[1])
        print('-'*100)

def valid_get_lng_and_lat():
    valid_response = functions.get_cordinates('São Paulo')
    invalid_response = "Error - Not Found"
    

    if valid_response != invalid_response:
        print(f"Test Done, the correct response was returned to the user \n lat: {valid_response[0]} and lng: {valid_response[1]}")
        print('-'*100)


def test_all():
    invalid_latitude_or_longitude()
    valid_latitude_or_longitude()
    invalid_get_lng_and_lat()
    valid_get_lng_and_lat()

test_all()