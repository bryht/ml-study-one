FROM python:3.9
COPY . /src
WORKDIR /src
EXPOSE 8000:8000
RUN pip3 install fastapi
RUN pip3 install uvicorn
RUN pip3 install typing
RUN pip3 install pymongo
RUN pip3 install python-decouple
CMD [ "uvicorn", "main:app", "--host", "0.0.0.0", "--reload" ]