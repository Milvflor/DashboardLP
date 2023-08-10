#!/usr/bin/env python

"""
main.py

Python API
"""

import boto3
from typing import Union
from fastapi import FastAPI

app = FastAPI()

dynamodb = boto3.resource('dynamodb')

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
