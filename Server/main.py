#!/usr/bin/env python

"""
main.py

Python API
"""

import boto3
from typing import Union
from fastapi import FastAPI

app = FastAPI()

# dynamodb = boto3.resource('dynamodb')

dynamodb = boto3.resource(
    service_name='dynamodb',
    region_name='us-east-1',
    aws_access_key_id='ASIAZZ5DBKWW7CM3L7WC',
    aws_secret_access_key='0h8i5jLlsLMjQ8SoSIa1+kPLgv8FDUZz3HqJ8VIJ',
    aws_session_token='FwoGZXIvYXdzEFIaDNbUq0+sIyqCGiG1YyK5AVK4QdM1ES3CDeeNtvtJV8IhbzBG5rZHAuv4ylHBvtNeKqoplNJiWEzm49pEe4VP5tDN9AaV1J6/Sp48j28q9WP1naVPQEiX6CU/bvrp1nPTWyT7DLvre10IEv3NlSGFppShk9Nq6i0xfO7D1qtT8wwPORY26pw2kYrPmpzHRvG2Bi+eG07LQzBq64G6DUNbLeF8xO0BKcAprmtFGKqhSX9ZUjInPnG4bmEVnA1uqd/GerrOHAvcwDy8KN+elacGMi2dtY9gHWqqPNUXtvoP/wMuZ9MzKOEgVr7LPLWsQ9G7em2LL8BUzeJwGFNZXJY='
)

@app.get("/")
def read_root():    
    return {
        "hotels": "/hotels",
        "categories": "/categories",
        "surroundings": "/surroundings",
    }

@app.get("/hotels")
def read_hotel():
    hotels = dynamodb.Table('hotels')
    response = hotels.scan()
    data = response['Items']
    return data

@app.get("/categories")
def read_categories():
    categories = dynamodb.Table('categories')
    response = categories.scan()
    data = response['Items']
    return data

@app.get("/surroundings")
def read_surroundings():
    surroundings = dynamodb.Table('surroundings')
    response = surroundings.scan()
    data = response['Items']
    return data
