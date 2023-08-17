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
    aws_access_key_id='ASIAX4I3MXBHPWWIXZ7T',
    aws_secret_access_key='lwPLg0N/HDF0W7Tthq2D2X8cXxPmSh/j2fpaquYg',
    aws_session_token='FwoGZXIvYXdzEL7//////////wEaDNrsgN6njeXKKvAREiK5AVWhX0mC67Y8iGGop3Anp2sUsaqFqXrld5MOGyLW12J21PGRCeSghf5QrS2o+95l9OqOxdvK+FySQlD/qpVv1bobCYt3gDKfvgXJTpYxRPd4fYPrlJjWQvm5SvbsmEC2aSifroIWuUUkLydMOZLu8V30tJzQp76VtpiDfCzFY4H+wuqib9XhVApfD+GjHfG6G25PM96KdZS9tvDwC/4vzGRl292TppaXSenF9kG7rcp+kilO/G4CuEihKKLx9KYGMi1tWoAxnUhWPiLFVloKSngPzyYpR5KXpwYuTbT70Y/ZfVfZ6nVWdHsUNV0KYIk='
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
