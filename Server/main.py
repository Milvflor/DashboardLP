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
    aws_access_key_id='ASIAX4I3MXBHH3WIKPGX',
    aws_secret_access_key='TCADmLFaG/W33Dwho9seZxyqawB4iBfGVzAMEy+Z',
    aws_session_token='FwoGZXIvYXdzEDkaDKTEig31E4yZDwuSOyK5AXnNu7GprEM5L05QktEU8Sjtu5VruVA6iy8F0TFDfEmvh/otY443915VuAjLqj2FIFYcI5oobZ9XYGvkadLN08XeQF7wJiF3RCsqtVRYBNaC8hQZ2mK7g5YLvwJso85TIc23bndQzAuXiggKDkFH9dg4oe/8PaZC9ZW65h3Wou25tPiuSPjLnea2t9Ighv/nqrIzo1YjQGj5EvzP47kVW5rAN7DJGEQZah8ilcVmr9OqA2nBI3MuBVvfKMDuj6cGMi3ueDSrPYOqAPB/X6rbmcdwwp5NgW9C8o/gfMA/XOCRwszcOlMKxb22N6A5P1Q='
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
