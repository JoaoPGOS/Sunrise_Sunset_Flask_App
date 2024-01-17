from flask import Flask, render_template, request, jsonify # Importing the Flask library
import functions # Importing the functions inside of the functions.py
import re





app = Flask(__name__,template_folder="template") # Instanciating my app and stablishing the template folder to the folder named "template"
app.config['TESTING'] = True
@app.route('/', methods=['POST','GET']) # Creating a route for the app and stablishing the allowed methods 

def index():
    try:
        # Using request to receive information from the form on the index.html file
        latitude = request.form.get('latitude') 
        longitude  = request.form.get('longitude')
        type = request.form.get('sunrise_and_sunset')
        timezones = request.form.get('timezones')

        # Checking if the method is POST to run the function inside of "functions.py" file that will call the API and return the values
        if request.method == 'POST':
            response = functions.get_info(type, latitude, longitude,timezones) 
        else:
            response = '' # In case of a non valid submit in the form or the first enter in the page it's returning a empty string 
        return render_template('index.html',onpage_response = response, timezones = functions.get_all_timezones()) # Using render template to render the index.html file into our web app and inserting values where it's onpage_response and timezones 
    except Exception as e:
        return render_template('index.html',onpage_response = f'Error: {e}', timezones = functions.get_all_timezones())# In case of an non expected error the try will catch an error and return it on the web page
    

    

@app.route('/getlatandlng', methods=['POST']) # Creating a route for the app  that allows only POST method so the page will not restart when I send a request to it

def get_lat_and_lng():
    try:
        # Get data from the request body as JSON
        data_json = request.get_json()

        # Return a response 
        resp = functions.get_cordinates(data_json)
        if type(resp) == list: # Checking if the response is a list with the latitude and longitude
            response = [resp[0],resp[1]]
            return jsonify({"lat":response[0],"lng":response[1]}), 200 #Returning a json response to the js part so the cordinates can be inserted in the right inputs

        

    except Exception as e:
        # In case of an error, return an error response
        error_message = f"Error processing the data: {str(e)}"
        return jsonify({"error": error_message}), 500
    


#Initializing the app and stablishing the debug to True so the responses can be seen to development purposes
if __name__ == '__main__':
    app.run(debug=True)
