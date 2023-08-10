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
    aws_access_key_id='ASIAX4I3MXBHCXEQ4LNP',
    aws_secret_access_key='q/A7VvLaC9VhQl3T7GjYw14x66f8o9oYYIAE11Wa',
    aws_session_token='FwoGZXIvYXdzECgaDEuqX+tJfqQLI6wH8yK5AVoQn6Z9AEeHC2Sqh4bLEwMpmBoORZ/1GO88MPA/YhNC9uVP9L8uVeRwYl5p6tfKIqBFi/vUNmJbs3/VY2zDPP97T8c3dKuvDqiM+mn4Mo7WA+XlEX6dDpg1Fw3DVIovLLKSMdXyCta8EYMsKXuiUHj+jjMJViqYmg5F2Wm4leN8QVNaxfcBPY1TPgEG4oR7dm259abMEgygiW2Bw8kjgv0jiBqp1KO+w5ktfp7apSb7aOpJ7rBzyzpRKJLy06YGMi2l0rt6t3iGdXj5xW924oadWIeCawW3FHiRpwEb4BNxTVz56OISRXxE3e9zDxc='
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
