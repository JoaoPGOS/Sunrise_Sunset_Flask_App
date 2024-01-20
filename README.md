# What is the app

This app will receive information from a form:
* latitude
* longitude
* timezone
* if it's sunrise or sunset

Then will call an API to get the exact datetime of the next sunrise or sunset, the exact requested datetime and the remaining time.

Container: Docker

# Dependencies

To run the app it's necessary to install python and the following libraries
* flask
* pytz
* geopy
* requests

Using pip3 install librarie_name or pip install librarie_name

# Docker build
The Dockerfile it's already configured

To build the flask image need to install Docker(Docker 4.26.1 used)

Then in the terminal type "docker build -t sunrise_sunset_app" can be any name but this was the used

To run it type in terminal "docker run -d -p 5000:5000 sunrise_sunset_app"

C: