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
    aws_access_key_id='ASIAX4I3MXBHGKQXT5PP',
    aws_secret_access_key='Wz7MmeByb2K/N+ChwgLSq3mLp8a6CKZf2VSc2xGU',
    aws_session_token='FwoGZXIvYXdzEDcaDG+Mbp9oUTV32gBUrSK5AQ8CZyBkLlHoYSl9bTz+d+BnLPM8RbzQzs7KMGi36Qf//QmhwLwdWQEzzziDSi0UVhHfAxZHK5dkLZhbMs9/7TizI5jn78mLAi+09/NhUxyrPLPFxFGD6agB2Dl8BmEovxOCCg/kmOIjmiXP3rqjZz3IaFoPLZUdgIr7tarRiQxHX5BA6wymgH0bq3xjhSPEKYlWMXs6eBl1Xzv62uJUekeB+gpZQhfNTg32PtcnKLr1vmKo3I6DE+LaKLmvj6cGMi3QrpVmQfBhtITSbAPygEVhwWjNVesQb3nJch2elGEW6s9udgV1thatvtcX0oU='
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
