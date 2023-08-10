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
    hotels = dynamodb.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'name',
            'AttributeType': 'S'
        }
    ],
    TableName='hotels',
    KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'name',
            'KeyType': 'RANGE'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
    )

    # Wait until the table exists.
    hotels.wait_until_exists()
    
    return hotels.item_count

@app.get("/hotels")
def read_hotel():
    table = dynamodb.Table('hotels')

    response = table.get_item(
        Key={
            'id': 1,
            'name': 'La Facha Hostal Restaurant Surf'
        }
    )
    item = response['Item']
    return item

@app.get("/categories")
def read_categories():
    table = dynamodb.Table('hotels')
    response = table.get_item(
        Key={
            'id': 1,
            'name': 'La Facha Hostal Restaurant Surf'
        }
    )
    item = response['Item']
    return item

@app.get("/surroundings")
def read_surroundings():
    table = dynamodb.Table('hotels')
    response = table.get_item(
        Key={
            'id': 1,
            'name': 'La Facha Hostal Restaurant Surf'
        }
    )
    item = response['Item']
    return item
