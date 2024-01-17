FROM ubuntu

RUN apt update
RUN apt install -y python3-pip
RUN pip3 install flask
RUN pip3 install pytz
RUN pip3 install geopy
RUN pip3 install requests

WORKDIR /app

COPY . .

CMD ["python3","-m","flask","run","--host=0.0.0.0"]