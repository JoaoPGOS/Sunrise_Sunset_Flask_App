# Voxus_test_app
Test to Voxus, assigned to develop an app to receive latitude and longitude and return sunrise/sunset exact hour, remaing time, request hour
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

Then in the terminal type "docker build -t voxus_test_app" can be any name but this was the used

To run it type in terminal "docker run -d -p 5000:5000 voxus_test_app"
