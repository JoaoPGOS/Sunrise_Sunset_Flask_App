const latitudeInput = document.getElementById('latitude');// Reference to latitude input
const longitudeInput = document.getElementById('longitude');// Reference to longitude input
const regexDecimal = /^-?\d{1,2}\.\d+$/;// Regular Expression to decimal latitude and longitude

function validate_latitude() 
{

    if (!regexDecimal.test(latitudeInput.value))// Testing the value inside of the input to see if it's on the same format as the Regular Expression require
    { 
        // If it's not tested as true the input will have a red border and will be the focus to the person type again the latitude
        latitudeInput.style.border = '1px red solid';
        latitudeInput.focus(); 
        return false;
    }

    latitudeInput.style.border = '1px green solid';//if it's tested as true the input will have a green border
    return true;
}

function validate_longitude()
{
    if (!regexDecimal.test(longitudeInput.value)) 
    {
        longitudeInput.style.border = '1px red solid';
        longitudeInput.focus();
        return false;
    }

    longitudeInput.style.border = '1px green solid';
    return true;
    
}

const city = document.getElementById('city'); // Reference to the city input

function get_lat_and_lgn()
{
    // Create an XMLHttpRequest object
    var xhr = new XMLHttpRequest();

    // Configure the POST request to the "/getlatandlng" endpoint
    xhr.open("POST", "/getlatandlng", true);

    // Set up the callback function for when the response is received
    xhr.onreadystatechange = function () {
        if (xhr.readyState == 4 && xhr.status == 200) {
            // When the response is successfully received as json, insert the response values from the function inside of latitude input and the longitude input and then run the validation of the latitude and longitude
            lat = JSON.parse(xhr.responseText)['lat']
            lng = JSON.parse(xhr.responseText)['lng']

            latitudeInput.value = lat
            longitudeInput.value = lng
            validate_latitude()
            validate_longitude()
        }
    };

    // Adding necessary headers for a POST request to send data in a json type
    xhr.setRequestHeader("Content-Type", "application/json");

    // Adding data to send 
    var data = JSON.stringify(city.value);

    // Sending the request with the data
    xhr.send(data);
}


