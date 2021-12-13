FROM python:3.9
COPY . /src
WORKDIR /src
RUN pip3 install python-decouple
RUN pip3 install requests
CMD [ "python", "main.py"]