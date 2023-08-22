#!/usr/bin/env python

"""
main.py

Create a Table and insert rows
"""

import boto3

# dynamodb = boto3.resource('dynamodb')

dynamodb = boto3.resource(
    service_name='dynamodb',
    region_name='us-east-1',
    aws_access_key_id='ASIAX4I3MXBHH3WIKPGX',
    aws_secret_access_key='TCADmLFaG/W33Dwho9seZxyqawB4iBfGVzAMEy+Z',
    aws_session_token='FwoGZXIvYXdzEDkaDKTEig31E4yZDwuSOyK5AXnNu7GprEM5L05QktEU8Sjtu5VruVA6iy8F0TFDfEmvh/otY443915VuAjLqj2FIFYcI5oobZ9XYGvkadLN08XeQF7wJiF3RCsqtVRYBNaC8hQZ2mK7g5YLvwJso85TIc23bndQzAuXiggKDkFH9dg4oe/8PaZC9ZW65h3Wou25tPiuSPjLnea2t9Ighv/nqrIzo1YjQGj5EvzP47kVW5rAN7DJGEQZah8ilcVmr9OqA2nBI3MuBVvfKMDuj6cGMi3ueDSrPYOqAPB/X6rbmcdwwp5NgW9C8o/gfMA/XOCRwszcOlMKxb22N6A5P1Q='
)

"""
Creating the hotels table
"""
hotels = dynamodb.create_table(
    TableName='hotels',
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
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
    )

hotels.wait_until_exists()

if hotels.item_count == 0:
    print("Successfully created hotels", flush = True)

# hotels = dynamodb.Table('hotels')

"""
Creating the categories table
"""
categories = dynamodb.create_table(
    TableName='categories',
    KeySchema=[
    {
        'AttributeName': 'id',
        'KeyType': 'HASH'
    },
    {
        'AttributeName': 'category',
        'KeyType': 'RANGE'
    },
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'category',
            'AttributeType': 'S'
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

categories.wait_until_exists()

if categories.item_count == 0:
    print("Successfully created categories", flush = True)

# categories = dynamodb.Table('categories')

"""
Creating the surroundings table
"""
surroundings = dynamodb.create_table(
    TableName='surroundings',
    AttributeDefinitions=[
        {
            'AttributeName': 'places',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'distance',
            'AttributeType': 'S'
        }
    ],
    KeySchema=[
        {
            'AttributeName': 'places',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'distance',
            'KeyType': 'RANGE'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
    )

surroundings.wait_until_exists()

if surroundings.item_count == 0:
    print("Successfully created surroundings", flush = True)

# surroundings = dynamodb.Table('surroundings')

"""
Inserting records in hotels
"""

with hotels.batch_writer() as batch:
    batch.put_item(
    Item={
      "id": 1,
      "name": "La Facha Hostal Restaurant Surf",
      "price": "62",
      "score": "8.4",
      "link": "https://www.booking.com/hotel/ec/la-facha-hostal-restaurant-surf.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=1&hapos=1&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=107381307_338009137_0_42_0&highlighted_blocks=107381307_338009137_0_42_0&matching_block_id=107381307_338009137_0_42_0&sr_pri_blocks=107381307_338009137_0_42_0__6166&from_sustainable_property_sr=1&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 2,
      "name": "Hotel Casa Arnaldo Esmeraldas",
      "price": "150",
      "score": "8.9",
      "link": "https://www.booking.com/hotel/ec/casa-arnaldo-esmeraldas.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=2&hapos=2&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=476692707_195997650_0_1_0&highlighted_blocks=476692707_195997650_0_1_0&matching_block_id=476692707_195997650_0_1_0&sr_pri_blocks=476692707_195997650_0_1_0__15000&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 3,
      "name": "Hotel la Barca",
      "price": "60",
      "score": "8.8",
      "link": "https://www.booking.com/hotel/ec/la-barca.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=3&hapos=3&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=152433503_362667476_0_2_0&highlighted_blocks=152433503_362667476_0_2_0&matching_block_id=152433503_362667476_0_2_0&sr_pri_blocks=152433503_362667476_0_2_0__6000&from_sustainable_property_sr=1&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 4,
      "name": "Resort Playa Azul Departamentos frente al mar",
      "price": "140",
      "score": "9.3",
      "link": "https://www.booking.com/hotel/ec/resort-playa-azul.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=4&hapos=4&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=208270701_357917003_2_0_0&highlighted_blocks=208270701_357917003_2_0_0&matching_block_id=208270701_357917003_2_0_0&sr_pri_blocks=208270701_357917003_2_0_0__14000&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 5,
      "name": "Escapaditas a la Playa",
      "price": "90",
      "score": "8.8",
      "link": "https://www.booking.com/hotel/ec/escapaditas-a-la-playa.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=5&hapos=5&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=156665701_200511961_3_0_0&highlighted_blocks=156665701_200511961_3_0_0&matching_block_id=156665701_200511961_3_0_0&sr_pri_blocks=156665701_200511961_3_0_0__9000&from_sustainable_property_sr=1&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 6,
      "name": "Hotel Oceanic Lodge",
      "price": "90",
      "score": "8.5",
      "link": "https://www.booking.com/hotel/ec/oceanic-lodge.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=6&hapos=6&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=194908121_237565169_2_2_0&highlighted_blocks=194908121_237565169_2_2_0&matching_block_id=194908121_237565169_2_2_0&sr_pri_blocks=194908121_237565169_2_2_0__9025&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 7,
      "name": "Seaside Garden Ecolodge Mompiche",
      "price": "70",
      "score": "9",
      "link": "https://www.booking.com/hotel/ec/seaside-garden-lodge-mompiche.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=7&hapos=7&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=188825203_272938554_2_42_0&highlighted_blocks=188825203_272938554_2_42_0&matching_block_id=188825203_272938554_2_42_0&sr_pri_blocks=188825203_272938554_2_42_0__7000&from_sustainable_property_sr=1&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 8,
      "name": "Hotel RC Tonsupa",
      "price": "90",
      "score": "8.6",
      "link": "https://www.booking.com/hotel/ec/rc-tonsupa.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=8&hapos=8&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=241659010_193960206_2_42_0&highlighted_blocks=241659010_193960206_2_42_0&matching_block_id=241659010_193960206_2_42_0&sr_pri_blocks=241659010_193960206_2_42_0__8960&from_sustainable_property_sr=1&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 9,
      "name": "Departamento Frente al Mar Diamond Beach",
      "price": "257",
      "score": "9.4",
      "link": "https://www.booking.com/hotel/ec/diamond-beach-tonsupa1234.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=9&hapos=9&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=276037501_362561522_2_0_0&highlighted_blocks=276037501_362561522_2_0_0&matching_block_id=276037501_362561522_2_0_0&sr_pri_blocks=276037501_362561522_2_0_0__25650&from_sustainable_property_sr=1&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 10,
      "name": "Hotel Almond Beach",
      "price": "60",
      "score": "8.7",
      "link": "https://www.booking.com/hotel/ec/almond-beach.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=10&hapos=10&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=206241720_335350452_2_2_0&highlighted_blocks=206241720_335350452_2_2_0&matching_block_id=206241720_335350452_2_2_0&sr_pri_blocks=206241720_335350452_2_2_0__6000&from_sustainable_property_sr=1&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 11,
      "name": "Cabañas Ecologicas Cayapas",
      "price": "100",
      "score": "8.9",
      "link": "https://www.booking.com/hotel/ec/hosteria-cayapas.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=11&hapos=11&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=157901207_176492114_5_0_0&highlighted_blocks=157901207_176492114_5_0_0&matching_block_id=157901207_176492114_5_0_0&sr_pri_blocks=157901207_176492114_5_0_0__10000&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 12,
      "name": "Departamento 4 habitaciones 12 personas vista al mar 8vo piso Playa Almendro",
      "price": "187",
      "score": "7.5",
      "link": "https://www.booking.com/hotel/ec/resort-playa-almendro-tonsupa-4-habitaciones.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=12&hapos=12&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=752831301_361584087_5_0_0&highlighted_blocks=752831301_361584087_5_0_0&matching_block_id=752831301_361584087_5_0_0&sr_pri_blocks=752831301_361584087_5_0_0__18720&from_sustainable_property_sr=1&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 13,
      "name": "Resort Playa Azul Tonsupa Departamento de 2 Habitaciones",
      "price": "258",
      "score": "9.1",
      "link": "https://www.booking.com/hotel/ec/playa-azul-resort-tonsupa-atacames.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=13&hapos=13&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=687622501_365747132_3_0_0&highlighted_blocks=687622501_365747132_3_0_0&matching_block_id=687622501_365747132_3_0_0&sr_pri_blocks=687622501_365747132_3_0_0__25800&from_sustainable_property_sr=1&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 14,
      "name": "Tonsupa Diamond Beach Apart - Hotel",
      "price": "272",
      "score": "8.7",
      "link": "https://www.booking.com/hotel/ec/tonsupa-diamond-beach-apart.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=14&hapos=14&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=305173001_113334619_2_0_0&highlighted_blocks=305173001_113334619_2_0_0&matching_block_id=305173001_113334619_2_0_0&sr_pri_blocks=305173001_113334619_2_0_0__27200&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 15,
      "name": "Aparthotel Oleaje",
      "price": "79",
      "score": "8.9",
      "link": "https://www.booking.com/hotel/ec/cabanas-oleaje.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=15&hapos=15&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=430162108_295543359_2_2_0&highlighted_blocks=430162108_295543359_2_2_0&matching_block_id=430162108_295543359_2_2_0&sr_pri_blocks=430162108_295543359_2_2_0__7920&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 16,
      "name": "Hotel Makana Resort",
      "price": "230",
      "score": "8.4",
      "link": "https://www.booking.com/hotel/ec/makana.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=16&hapos=16&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=88779602_193658734_2_1_0&highlighted_blocks=88779602_193658734_2_1_0&matching_block_id=88779602_193658734_2_1_0&sr_pri_blocks=88779602_193658734_2_1_0__23000&from_sustainable_property_sr=1&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 17,
      "name": "La Bocana",
      "price": "68",
      "score": "8.7",
      "link": "https://www.booking.com/hotel/ec/la-bocana.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=17&hapos=17&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=305038101_288369263_2_0_0&highlighted_blocks=305038101_288369263_2_0_0&matching_block_id=305038101_288369263_2_0_0&sr_pri_blocks=305038101_288369263_2_0_0__6800&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 18,
      "name": "Departamentos frente al mar Resort Playa Azul",
      "price": "228",
      "score": "9.6",
      "link": "https://www.booking.com/hotel/ec/suite-1802b-resort-playa-azul.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=18&hapos=18&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=496852902_358161557_3_0_0&highlighted_blocks=496852902_358161557_3_0_0&matching_block_id=496852902_358161557_3_0_0&sr_pri_blocks=496852902_358161557_3_0_0__22800&from_sustainable_property_sr=1&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 19,
      "name": "Suite Makana #403",
      "price": "150",
      "score": "8.6",
      "link": "https://www.booking.com/hotel/ec/suite-makana-resort-403.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=19&hapos=19&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=198782701_334448564_4_0_0&highlighted_blocks=198782701_334448564_4_0_0&matching_block_id=198782701_334448564_4_0_0&sr_pri_blocks=198782701_334448564_4_0_0__15040&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 20,
      "name": "Dep. Torre Sol Tropical Tonsupa",
      "price": "140",
      "score": "0",
      "link": "https://www.booking.com/hotel/ec/dep-torre-sol-tropical-tonsupa.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=20&hapos=20&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=952097901_367797959_2_0_0&highlighted_blocks=952097901_367797959_2_0_0&matching_block_id=952097901_367797959_2_0_0&sr_pri_blocks=952097901_367797959_2_0_0__14000&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 21,
      "name": "Caramba Hospedaje",
      "price": "108",
      "score": "8.6",
      "link": "https://www.booking.com/hotel/ec/caramba-hospedaje.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=21&hapos=21&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=731985901_341786475_0_41_0&highlighted_blocks=731985901_341786475_0_41_0&matching_block_id=731985901_341786475_0_41_0&sr_pri_blocks=731985901_341786475_0_41_0__10800&from_sustainable_property_sr=1&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 22,
      "name": "Hotel Salduba",
      "price": "60",
      "score": "9.1",
      "link": "https://www.booking.com/hotel/ec/salduba-tonsupa.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=22&hapos=22&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=231040301_109031314_2_0_0&highlighted_blocks=231040301_109031314_2_0_0&matching_block_id=231040301_109031314_2_0_0&sr_pri_blocks=231040301_109031314_2_0_0__6000&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 23,
      "name": "Casa del mar",
      "price": "54",
      "score": "6.7",
      "link": "https://www.booking.com/hotel/ec/casa-del-mar-tonsupa.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=23&hapos=23&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=914957003_362910508_2_0_0&highlighted_blocks=914957003_362910508_2_0_0&matching_block_id=914957003_362910508_2_0_0&sr_pri_blocks=914957003_362910508_2_0_0__5354&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 24,
      "name": "Tus Vacaciones en Tonsupa Ecuador.",
      "price": "114",
      "score": "9.1",
      "link": "https://www.booking.com/hotel/ec/tus-vacaciones-en-tonsupa-ecuador.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=24&hapos=24&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=749184501_331181420_6_0_0&highlighted_blocks=749184501_331181420_6_0_0&matching_block_id=749184501_331181420_6_0_0&sr_pri_blocks=749184501_331181420_6_0_0__11400&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 25,
      "name": "Departamentos frente al mar en Resort Playa Azul-Tonsupa",
      "price": "140",
      "score": "8.6",
      "link": "https://www.booking.com/hotel/ec/edificios-playa-azul-tonsupa.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=25&hapos=25&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=273001001_119199248_4_0_0&highlighted_blocks=273001001_119199248_4_0_0&matching_block_id=273001001_119199248_4_0_0&sr_pri_blocks=273001001_119199248_4_0_0__14000&from_sustainable_property_sr=1&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 26,
      "name": "La Facha Hostal Restaurant Surf",
      "price": "62",
      "score": "8.4",
      "link": "https://www.booking.com/hotel/ec/la-facha-hostal-restaurant-surf.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=1&hapos=1&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=107381307_338009137_0_42_0&highlighted_blocks=107381307_338009137_0_42_0&matching_block_id=107381307_338009137_0_42_0&sr_pri_blocks=107381307_338009137_0_42_0__6166&from_sustainable_property_sr=1&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 27,
      "name": "Hotel Casa Arnaldo Esmeraldas",
      "price": "150",
      "score": "8.9",
      "link": "https://www.booking.com/hotel/ec/casa-arnaldo-esmeraldas.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=2&hapos=2&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=476692707_195997650_0_1_0&highlighted_blocks=476692707_195997650_0_1_0&matching_block_id=476692707_195997650_0_1_0&sr_pri_blocks=476692707_195997650_0_1_0__15000&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 28,
      "name": "Hotel la Barca",
      "price": "60",
      "score": "8.8",
      "link": "https://www.booking.com/hotel/ec/la-barca.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=3&hapos=3&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=152433503_362667476_0_2_0&highlighted_blocks=152433503_362667476_0_2_0&matching_block_id=152433503_362667476_0_2_0&sr_pri_blocks=152433503_362667476_0_2_0__6000&from_sustainable_property_sr=1&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 29,
      "name": "Resort Playa Azul Departamentos frente al mar",
      "price": "140",
      "score": "9.3",
      "link": "https://www.booking.com/hotel/ec/resort-playa-azul.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=4&hapos=4&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=208270701_357917003_2_0_0&highlighted_blocks=208270701_357917003_2_0_0&matching_block_id=208270701_357917003_2_0_0&sr_pri_blocks=208270701_357917003_2_0_0__14000&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 30,
      "name": "Escapaditas a la Playa",
      "price": "90",
      "score": "8.8",
      "link": "https://www.booking.com/hotel/ec/escapaditas-a-la-playa.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=5&hapos=5&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=156665701_200511961_3_0_0&highlighted_blocks=156665701_200511961_3_0_0&matching_block_id=156665701_200511961_3_0_0&sr_pri_blocks=156665701_200511961_3_0_0__9000&from_sustainable_property_sr=1&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 31,
      "name": "Hotel Oceanic Lodge",
      "price": "90",
      "score": "8.5",
      "link": "https://www.booking.com/hotel/ec/oceanic-lodge.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=6&hapos=6&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=194908121_237565169_2_2_0&highlighted_blocks=194908121_237565169_2_2_0&matching_block_id=194908121_237565169_2_2_0&sr_pri_blocks=194908121_237565169_2_2_0__9025&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 32,
      "name": "Seaside Garden Ecolodge Mompiche",
      "price": "70",
      "score": "9",
      "link": "https://www.booking.com/hotel/ec/seaside-garden-lodge-mompiche.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=7&hapos=7&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=188825203_272938554_2_42_0&highlighted_blocks=188825203_272938554_2_42_0&matching_block_id=188825203_272938554_2_42_0&sr_pri_blocks=188825203_272938554_2_42_0__7000&from_sustainable_property_sr=1&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 33,
      "name": "Hotel RC Tonsupa",
      "price": "90",
      "score": "8.6",
      "link": "https://www.booking.com/hotel/ec/rc-tonsupa.en-gb    \}\).html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=8&hapos=8&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=241659010_193960206_2_42_0&highlighted_blocks=241659010_193960206_2_42_0&matching_block_id=241659010_193960206_2_42_0&sr_pri_blocks=241659010_193960206_2_42_0__8960&from_sustainable_property_sr=1&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 34,
      "name": "Departamento Frente al Mar Diamond Beach",
      "price": "257",
      "score": "9.4",
      "link": "https://www.booking.com/hotel/ec/diamond-beach-tonsupa1234.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=9&hapos=9&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=276037501_362561522_2_0_0&highlighted_blocks=276037501_362561522_2_0_0&matching_block_id=276037501_362561522_2_0_0&sr_pri_blocks=276037501_362561522_2_0_0__25650&from_sustainable_property_sr=1&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 35,
      "name": "Hotel Almond Beach",
      "price": "60",
      "score": "8.7",
      "link": "https://www.booking.com/hotel/ec/almond-beach.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=10&hapos=10&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=206241720_335350452_2_2_0&highlighted_blocks=206241720_335350452_2_2_0&matching_block_id=206241720_335350452_2_2_0&sr_pri_blocks=206241720_335350452_2_2_0__6000&from_sustainable_property_sr=1&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 36,
      "name": "Cabañas Ecologicas Cayapas",
      "price": "100",
      "score": "8.9",
      "link": "https://www.booking.com/hotel/ec/hosteria-cayapas.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=11&hapos=11&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=157901207_176492114_5_0_0&highlighted_blocks=157901207_176492114_5_0_0&matching_block_id=157901207_176492114_5_0_0&sr_pri_blocks=157901207_176492114_5_0_0__10000&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 37,
      "name": "Departamento 4 habitaciones 12 personas vista al mar 8vo piso Playa Almendro",
      "price": "187",
      "score": "7.5",
      "link": "https://www.booking.com/hotel/ec/resort-playa-almendro-tonsupa-4-habitaciones.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=12&hapos=12&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=752831301_361584087_5_0_0&highlighted_blocks=752831301_361584087_5_0_0&matching_block_id=752831301_361584087_5_0_0&sr_pri_blocks=752831301_361584087_5_0_0__18720&from_sustainable_property_sr=1&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 38,
      "name": "Resort Playa Azul Tonsupa Departamento de 2 Habitaciones",
      "price": "258",
      "score": "9.1",
      "link": "https://www.booking.com/hotel/ec/playa-azul-resort-tonsupa-atacames.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=13&hapos=13&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=687622501_365747132_3_0_0&highlighted_blocks=687622501_365747132_3_0_0&matching_block_id=687622501_365747132_3_0_0&sr_pri_blocks=687622501_365747132_3_0_0__25800&from_sustainable_property_sr=1&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 39,
      "name": "Tonsupa Diamond Beach Apart - Hotel",
      "price": "272",
      "score": "8.7",
      "link": "https://www.booking.com/hotel/ec/tonsupa-diamond-beach-apart.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=14&hapos=14&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=305173001_113334619_2_0_0&highlighted_blocks=305173001_113334619_2_0_0&matching_block_id=305173001_113334619_2_0_0&sr_pri_blocks=305173001_113334619_2_0_0__27200&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 40,
      "name": "Aparthotel Oleaje",
      "price": "79",
      "score": "8.9",
      "link": "https://www.booking.com/hotel/ec/cabanas-oleaje.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=15&hapos=15&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=430162108_295543359_2_2_0&highlighted_blocks=430162108_295543359_2_2_0&matching_block_id=430162108_295543359_2_2_0&sr_pri_blocks=430162108_295543359_2_2_0__7920&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 41,
      "name": "Hotel Makana Resort",
      "price": "230",
      "score": "8.4",
      "link": "https://www.booking.com/hotel/ec/makana.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=16&hapos=16&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=88779602_193658734_2_1_0&highlighted_blocks=88779602_193658734_2_1_0&matching_block_id=88779602_193658734_2_1_0&sr_pri_blocks=88779602_193658734_2_1_0__23000&from_sustainable_property_sr=1&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 42,
      "name": "La Bocana",
      "price": "68",
      "score": "8.7",
      "link": "https://www.booking.com/hotel/ec/la-bocana.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=17&hapos=17&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=305038101_288369263_2_0_0&highlighted_blocks=305038101_288369263_2_0_0&matching_block_id=305038101_288369263_2_0_0&sr_pri_blocks=305038101_288369263_2_0_0__6800&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 43,
      "name": "Departamentos frente al mar Resort Playa Azul",
      "price": "228",
      "score": "9.6",
      "link": "https://www.booking.com/hotel/ec/suite-1802b-resort-playa-azul.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=18&hapos=18&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=496852902_358161557_3_0_0&highlighted_blocks=496852902_358161557_3_0_0&matching_block_id=496852902_358161557_3_0_0&sr_pri_blocks=496852902_358161557_3_0_0__22800&from_sustainable_property_sr=1&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 44,
      "name": "Suite Makana #403",
      "price": "150",
      "score": "8.6",
      "link": "https://www.booking.com/hotel/ec/suite-makana-resort-403.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=19&hapos=19&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=198782701_334448564_4_0_0&highlighted_blocks=198782701_334448564_4_0_0&matching_block_id=198782701_334448564_4_0_0&sr_pri_blocks=198782701_334448564_4_0_0__15040&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 45,
      "name": "Dep. Torre Sol Tropical Tonsupa",
      "price": "140",
      "score": "0",
      "link": "https://www.booking.com/hotel/ec/dep-torre-sol-tropical-tonsupa.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=20&hapos=20&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=952097901_367797959_2_0_0&highlighted_blocks=952097901_367797959_2_0_0&matching_block_id=952097901_367797959_2_0_0&sr_pri_blocks=952097901_367797959_2_0_0__14000&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 46,
      "name": "Caramba Hospedaje",
      "price": "108",
      "score": "8.6",
      "link": "https://www.booking.com/hotel/ec/caramba-hospedaje.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=21&hapos=21&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=731985901_341786475_0_41_0&highlighted_blocks=731985901_341786475_0_41_0&matching_block_id=731985901_341786475_0_41_0&sr_pri_blocks=731985901_341786475_0_41_0__10800&from_sustainable_property_sr=1&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 47,
      "name": "Hotel Salduba",
      "price": "60",
      "score": "9.1",
      "link": "https://www.booking.com/hotel/ec/salduba-tonsupa.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=22&hapos=22&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=231040301_109031314_2_0_0&highlighted_blocks=231040301_109031314_2_0_0&matching_block_id=231040301_109031314_2_0_0&sr_pri_blocks=231040301_109031314_2_0_0__6000&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 48,
      "name": "Casa del mar",
      "price": "54",
      "score": "6.7",
      "link": "https://www.booking.com/hotel/ec/casa-del-mar-tonsupa.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=23&hapos=23&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=914957003_362910508_2_0_0&highlighted_blocks=914957003_362910508_2_0_0&matching_block_id=914957003_362910508_2_0_0&sr_pri_blocks=914957003_362910508_2_0_0__5354&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 49,
      "name": "Tus Vacaciones en Tonsupa Ecuador.",
      "price": "114",
      "score": "9.1",
      "link": "https://www.booking.com/hotel/ec/tus-vacaciones-en-tonsupa-ecuador.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=24&hapos=24&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=749184501_331181420_6_0_0&highlighted_blocks=749184501_331181420_6_0_0&matching_block_id=749184501_331181420_6_0_0&sr_pri_blocks=749184501_331181420_6_0_0__11400&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 50,
      "name": "Departamentos frente al mar en Resort Playa Azul-Tonsupa",
      "price": "140",
      "score": "8.6",
      "link": "https://www.booking.com/hotel/ec/edificios-playa-azul-tonsupa.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=25&hapos=25&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=273001001_119199248_4_0_0&highlighted_blocks=273001001_119199248_4_0_0&matching_block_id=273001001_119199248_4_0_0&sr_pri_blocks=273001001_119199248_4_0_0__14000&from_sustainable_property_sr=1&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 51,
      "name": "La Facha Hostal Restaurant Surf",
      "price": "62",
      "score": "8.4",
      "link": "https://www.booking.com/hotel/ec/la-facha-hostal-restaurant-surf.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=1&hapos=1&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=107381307_338009137_0_42_0&highlighted_blocks=107381307_338009137_0_42_0&matching_block_id=107381307_338009137_0_42_0&sr_pri_blocks=107381307_338009137_0_42_0__6166&from_sustainable_property_sr=1&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 52,
      "name": "Hotel Casa Arnaldo Esmeraldas",
      "price": "150",
      "score": "8.9",
      "link": "https://www.booking.com/hotel/ec/casa-arnaldo-esmeraldas.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=2&hapos=2&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=476692707_195997650_0_1_0&highlighted_blocks=476692707_195997650_0_1_0&matching_block_id=476692707_195997650_0_1_0&sr_pri_blocks=476692707_195997650_0_1_0__15000&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 53,
      "name": "Hotel la Barca",
      "price": "60",
      "score": "8.8",
      "link": "https://www.booking.com/hotel/ec/la-barca.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=3&hapos=3&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=152433503_362667476_0_2_0&highlighted_blocks=152433503_362667476_0_2_0&matching_block_id=152433503_362667476_0_2_0&sr_pri_blocks=152433503_362667476_0_2_0__6000&from_sustainable_property_sr=1&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 54,
      "name": "Resort Playa Azul Departamentos frente al mar",
      "price": "140",
      "score": "9.3",
      "link": "https://www.booking.com/hotel/ec/resort-playa-azul.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=4&hapos=4&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=208270701_357917003_2_0_0&highlighted_blocks=208270701_357917003_2_0_0&matching_block_id=208270701_357917003_2_0_0&sr_pri_blocks=208270701_357917003_2_0_0__14000&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 55,
      "name": "Escapaditas a la Playa",
      "price": "90",
      "score": "8.8",
      "link": "https://www.booking.com/hotel/ec/escapaditas-a-la-playa.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=5&hapos=5&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=156665701_200511961_3_0_0&highlighted_blocks=156665701_200511961_3_0_0&matching_block_id=156665701_200511961_3_0_0&sr_pri_blocks=156665701_200511961_3_0_0__9000&from_sustainable_property_sr=1&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 56,
      "name": "Hotel Oceanic Lodge",
      "price": "90",
      "score": "8.5",
      "link": "https://www.booking.com/hotel/ec/oceanic-lodge.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=6&hapos=6&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=194908121_237565169_2_2_0&highlighted_blocks=194908121_237565169_2_2_0&matching_block_id=194908121_237565169_2_2_0&sr_pri_blocks=194908121_237565169_2_2_0__9025&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 57,
      "name": "Seaside Garden Ecolodge Mompiche",
      "price": "70",
      "score": "9",
      "link": "https://www.booking.com/hotel/ec/seaside-garden-lodge-mompiche.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=7&hapos=7&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=188825203_272938554_2_42_0&highlighted_blocks=188825203_272938554_2_42_0&matching_block_id=188825203_272938554_2_42_0&sr_pri_blocks=188825203_272938554_2_42_0__7000&from_sustainable_property_sr=1&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 58,
      "name": "Hotel RC Tonsupa",
      "price": "90",
      "score": "8.6",
      "link": "https://www.booking.com/hotel/ec/rc-tonsupa.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=8&hapos=8&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=241659010_193960206_2_42_0&highlighted_blocks=241659010_193960206_2_42_0&matching_block_id=241659010_193960206_2_42_0&sr_pri_blocks=241659010_193960206_2_42_0__8960&from_sustainable_property_sr=1&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 59,
      "name": "Departamento Frente al Mar Diamond Beach",
      "price": "257",
      "score": "9.4",
      "link": "https://www.booking.com/hotel/ec/diamond-beach-tonsupa1234.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=9&hapos=9&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=276037501_362561522_2_0_0&highlighted_blocks=276037501_362561522_2_0_0&matching_block_id=276037501_362561522_2_0_0&sr_pri_blocks=276037501_362561522_2_0_0__25650&from_sustainable_property_sr=1&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 60,
      "name": "Hotel Almond Beach",
      "price": "60",
      "score": "8.7",
      "link": "https://www.booking.com/hotel/ec/almond-beach.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=10&hapos=10&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=206241720_335350452_2_2_0&highlighted_blocks=206241720_335350452_2_2_0&matching_block_id=206241720_335350452_2_2_0&sr_pri_blocks=206241720_335350452_2_2_0__6000&from_sustainable_property_sr=1&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 61,
      "name": "Cabañas Ecologicas Cayapas",
      "price": "100",
      "score": "8.9",
      "link": "https://www.booking.com/hotel/ec/hosteria-cayapas.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=11&hapos=11&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=157901207_176492114_5_0_0&highlighted_blocks=157901207_176492114_5_0_0&matching_block_id=157901207_176492114_5_0_0&sr_pri_blocks=157901207_176492114_5_0_0__10000&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 62,
      "name": "Departamento 4 habitaciones 12 personas vista al mar 8vo piso Playa Almendro",
      "price": "187",
      "score": "7.5",
      "link": "https://www.booking.com/hotel/ec/resort-playa-almendro-tonsupa-4-habitaciones.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=12&hapos=12&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=752831301_361584087_5_0_0&highlighted_blocks=752831301_361584087_5_0_0&matching_block_id=752831301_361584087_5_0_0&sr_pri_blocks=752831301_361584087_5_0_0__18720&from_sustainable_property_sr=1&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 63,
      "name": "Resort Playa Azul Tonsupa Departamento de 2 Habitaciones",
      "price": "258",
      "score": "9.1",
      "link": "https://www.booking.com/hotel/ec/playa-azul-resort-tonsupa-atacames.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=13&hapos=13&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=687622501_365747132_3_0_0&highlighted_blocks=687622501_365747132_3_0_0&matching_block_id=687622501_365747132_3_0_0&sr_pri_blocks=687622501_365747132_3_0_0__25800&from_sustainable_property_sr=1&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 64,
      "name": "Tonsupa Diamond Beach Apart - Hotel",
      "price": "272",
      "score": "8.7",
      "link": "https://www.booking.com/hotel/ec/tonsupa-diamond-beach-apart.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=14&hapos=14&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=305173001_113334619_2_0_0&highlighted_blocks=305173001_113334619_2_0_0&matching_block_id=305173001_113334619_2_0_0&sr_pri_blocks=305173001_113334619_2_0_0__27200&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 65,
      "name": "Aparthotel Oleaje",
      "price": "79",
      "score": "8.9",
      "link": "https://www.booking.com/hotel/ec/cabanas-oleaje.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=15&hapos=15&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=430162108_295543359_2_2_0&highlighted_blocks=430162108_295543359_2_2_0&matching_block_id=430162108_295543359_2_2_0&sr_pri_blocks=430162108_295543359_2_2_0__7920&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 66,
      "name": "Hotel Makana Resort",
      "price": "230",
      "score": "8.4",
      "link": "https://www.booking.com/hotel/ec/makana.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=16&hapos=16&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=88779602_193658734_2_1_0&highlighted_blocks=88779602_193658734_2_1_0&matching_block_id=88779602_193658734_2_1_0&sr_pri_blocks=88779602_193658734_2_1_0__23000&from_sustainable_property_sr=1&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 67,
      "name": "La Bocana",
      "price": "68",
      "score": "8.7",
      "link": "https://www.booking.com/hotel/ec/la-bocana.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=17&hapos=17&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=305038101_288369263_2_0_0&highlighted_blocks=305038101_288369263_2_0_0&matching_block_id=305038101_288369263_2_0_0&sr_pri_blocks=305038101_288369263_2_0_0__6800&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 68,
      "name": "Departamentos frente al mar Resort Playa Azul",
      "price": "228",
      "score": "9.6",
      "link": "https://www.booking.com/hotel/ec/suite-1802b-resort-playa-azul.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=18&hapos=18&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=496852902_358161557_3_0_0&highlighted_blocks=496852902_358161557_3_0_0&matching_block_id=496852902_358161557_3_0_0&sr_pri_blocks=496852902_358161557_3_0_0__22800&from_sustainable_property_sr=1&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 69,
      "name": "Suite Makana #403",
      "price": "150",
      "score": "8.6",
      "link": "https://www.booking.com/hotel/ec/suite-makana-resort-403.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=19&hapos=19&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=198782701_334448564_4_0_0&highlighted_blocks=198782701_334448564_4_0_0&matching_block_id=198782701_334448564_4_0_0&sr_pri_blocks=198782701_334448564_4_0_0__15040&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 70,
      "name": "Dep. Torre Sol Tropical Tonsupa",
      "price": "140",
      "score": "0",
      "link": "https://www.booking.com/hotel/ec/dep-torre-sol-tropical-tonsupa.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=20&hapos=20&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=952097901_367797959_2_0_0&highlighted_blocks=952097901_367797959_2_0_0&matching_block_id=952097901_367797959_2_0_0&sr_pri_blocks=952097901_367797959_2_0_0__14000&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 71,
      "name": "Caramba Hospedaje",
      "price": "108",
      "score": "8.6",
      "link": "https://www.booking.com/hotel/ec/caramba-hospedaje.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=21&hapos=21&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=731985901_341786475_0_41_0&highlighted_blocks=731985901_341786475_0_41_0&matching_block_id=731985901_341786475_0_41_0&sr_pri_blocks=731985901_341786475_0_41_0__10800&from_sustainable_property_sr=1&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 72,
      "name": "Hotel Salduba",
      "price": "60",
      "score": "9.1",
      "link": "https://www.booking.com/hotel/ec/salduba-tonsupa.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=22&hapos=22&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=231040301_109031314_2_0_0&highlighted_blocks=231040301_109031314_2_0_0&matching_block_id=231040301_109031314_2_0_0&sr_pri_blocks=231040301_109031314_2_0_0__6000&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 73,
      "name": "Casa del mar",
      "price": "54",
      "score": "6.7",
      "link": "https://www.booking.com/hotel/ec/casa-del-mar-tonsupa.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=23&hapos=23&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=914957003_362910508_2_0_0&highlighted_blocks=914957003_362910508_2_0_0&matching_block_id=914957003_362910508_2_0_0&sr_pri_blocks=914957003_362910508_2_0_0__5354&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 74,
      "name": "Tus Vacaciones en Tonsupa Ecuador.",
      "price": "114",
      "score": "9.1",
      "link": "https://www.booking.com/hotel/ec/tus-vacaciones-en-tonsupa-ecuador.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=24&hapos=24&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=749184501_331181420_6_0_0&highlighted_blocks=749184501_331181420_6_0_0&matching_block_id=749184501_331181420_6_0_0&sr_pri_blocks=749184501_331181420_6_0_0__11400&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 75,
      "name": "Departamentos frente al mar en Resort Playa Azul-Tonsupa",
      "price": "140",
      "score": "8.6",
      "link": "https://www.booking.com/hotel/ec/edificios-playa-azul-tonsupa.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=13787&dest_type=region&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=25&hapos=25&sr_order=popularity&srpvid=45a501b602ec019e&srepoch=1675124078&all_sr_blocks=273001001_119199248_4_0_0&highlighted_blocks=273001001_119199248_4_0_0&matching_block_id=273001001_119199248_4_0_0&sr_pri_blocks=273001001_119199248_4_0_0__14000&from_sustainable_property_sr=1&from=searchresults&map_fdco=1#hotelTmpl",
      "province": "Esmeraldas"
        }
    )
    batch.put_item(
    Item={
      "id": 1,
      "name": "Hotel Santiago de Compostella Suites",
      "price": "104",
      "score": "8.1",
      "link": "https://www.booking.com/hotel/ec/santiago-de-compostella-suite.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=1&hapos=1&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=168320811_366577311_0_1_0&highlighted_blocks=168320811_366577311_0_1_0&matching_block_id=168320811_366577311_0_1_0&sr_pri_blocks=168320811_366577311_0_1_0__10400&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 2,
      "name": "Floré Hotel Boutique",
      "price": "78",
      "score": "8.9",
      "link": "https://www.booking.com/hotel/ec/flore-boutique.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=2&hapos=2&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=307181819_310108407_2_41_0&highlighted_blocks=307181819_310108407_2_41_0&matching_block_id=307181819_310108407_2_41_0&sr_pri_blocks=307181819_310108407_2_41_0__7800&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 3,
      "name": "Loft NASS Atahualpa",
      "price": "95",
      "score": "8.6",
      "link": "https://www.booking.com/hotel/ec/loft-nass-atahualpa.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=3&hapos=3&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=759828306_347671561_3_1_0&highlighted_blocks=759828306_347671561_3_1_0&matching_block_id=759828306_347671561_3_1_0&sr_pri_blocks=759828306_347671561_3_1_0__9460&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 4,
      "name": "Hostal Posada del Angel",
      "price": "141",
      "score": "9.3",
      "link": "https://www.booking.com/hotel/ec/posadadelangel.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=4&hapos=4&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=9463902_94304056_2_41_0&highlighted_blocks=9463902_94304056_2_41_0&matching_block_id=9463902_94304056_2_41_0&sr_pri_blocks=9463902_94304056_2_41_0__14136&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 5,
      "name": "Hotel La Orquidea",
      "price": "70",
      "score": "8.8",
      "link": "https://www.booking.com/hotel/ec/hostal-la-orquidea.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=5&hapos=5&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=115363602_285349506_2_0_0&highlighted_blocks=115363602_285349506_2_0_0&matching_block_id=115363602_285349506_2_0_0&sr_pri_blocks=115363602_285349506_2_0_0__7000&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 6,
      "name": "Hotel Boutique Castilla de Léon",
      "price": "52",
      "score": "8",
      "link": "https://www.booking.com/hotel/ec/boutique-castilla-de-leon.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=6&hapos=6&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=259100910_104591953_2_2_0&highlighted_blocks=259100910_104591953_2_2_0&matching_block_id=259100910_104591953_2_2_0&sr_pri_blocks=259100910_104591953_2_2_0__5225&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 7,
      "name": "Selina Cuenca",
      "price": "71",
      "score": "8.3",
      "link": "https://www.booking.com/hotel/ec/crespo.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=7&hapos=7&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=27754805_295775667_0_41_0&highlighted_blocks=27754805_295775667_0_41_0&matching_block_id=27754805_295775667_0_41_0&sr_pri_blocks=27754805_295775667_0_41_0__7092&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 8,
      "name": "Hotel Posada del Rey",
      "price": "60",
      "score": "8.8",
      "link": "https://www.booking.com/hotel/ec/posada-del-rey.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=8&hapos=8&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=124028807_348115264_0_2_0&highlighted_blocks=124028807_348115264_0_2_0&matching_block_id=124028807_348115264_0_2_0&sr_pri_blocks=124028807_348115264_0_2_0__5950&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 9,
      "name": "Hotel Azul de la Plaza",
      "price": "97",
      "score": "8.7",
      "link": "https://www.booking.com/hotel/ec/azul-de-la-plaza-san-sebastian-cuenca.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=9&hapos=9&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=599404401_235119628_0_1_0&highlighted_blocks=599404401_235119628_0_1_0&matching_block_id=599404401_235119628_0_1_0&sr_pri_blocks=599404401_235119628_0_1_0__9720&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 10,
      "name": "Pepe's House Cuenca Boutique Hotel l B&B",
      "price": "90",
      "score": "9.3",
      "link": "https://www.booking.com/hotel/ec/casa-sucre-cuenca1.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=10&hapos=10&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=90251117_286816048_2_1_0&highlighted_blocks=90251117_286816048_2_1_0&matching_block_id=90251117_286816048_2_1_0&sr_pri_blocks=90251117_286816048_2_1_0__8958&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 11,
      "name": "Hostal Mariscal Inn & Suite",
      "price": "55",
      "score": "8.4",
      "link": "https://www.booking.com/hotel/ec/hostal-mariscal.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=11&hapos=11&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=775698302_335863330_2_41_0&highlighted_blocks=775698302_335863330_2_41_0&matching_block_id=775698302_335863330_2_41_0&sr_pri_blocks=775698302_335863330_2_41_0__5526&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 12,
      "name": "Villa Emilia Hostal",
      "price": "76",
      "score": "9.4",
      "link": "https://www.booking.com/hotel/ec/villa-emilia-hostal.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=12&hapos=12&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=124840905_266318746_2_1_0&highlighted_blocks=124840905_266318746_2_1_0&matching_block_id=124840905_266318746_2_1_0&sr_pri_blocks=124840905_266318746_2_1_0__7600&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 13,
      "name": "Morenica del Rosario",
      "price": "76",
      "score": "8.5",
      "link": "https://www.booking.com/hotel/ec/morenica-del-rosario.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=13&hapos=13&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=31956008_201931846_0_1_0&highlighted_blocks=31956008_201931846_0_1_0&matching_block_id=31956008_201931846_0_1_0&sr_pri_blocks=31956008_201931846_0_1_0__7600&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 14,
      "name": "Nonno’s House",
      "price": "61",
      "score": "0",
      "link": "https://www.booking.com/hotel/ec/nonnos-house.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=14&hapos=14&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=954998301_367998313_2_0_0&highlighted_blocks=954998301_367998313_2_0_0&matching_block_id=954998301_367998313_2_0_0&sr_pri_blocks=954998301_367998313_2_0_0__6080&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 15,
      "name": "Four Points by Sheraton Cuenca",
      "price": "223",
      "score": "9",
      "link": "https://www.booking.com/hotel/ec/four-points-by-sheraton-cuenca.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=15&hapos=15&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=273410706_246434816_0_41_0&highlighted_blocks=273410706_246434816_0_41_0&matching_block_id=273410706_246434816_0_41_0&sr_pri_blocks=273410706_246434816_0_41_0__22300&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 16,
      "name": "Hotel Nass Pinar del Lago",
      "price": "124",
      "score": "8.4",
      "link": "https://www.booking.com/hotel/ec/pinar-del-lago.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=16&hapos=16&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=50036909_326384576_2_2_0&highlighted_blocks=50036909_326384576_2_2_0&matching_block_id=50036909_326384576_2_2_0&sr_pri_blocks=50036909_326384576_2_2_0__12420&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 17,
      "name": "Hosteria Dos Chorreras",
      "price": "249",
      "score": "8.9",
      "link": "https://www.booking.com/hotel/ec/hosteria-dos-chorreras.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=17&hapos=17&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=38024009_200156838_3_9_0&highlighted_blocks=38024009_200156838_3_9_0&matching_block_id=38024009_200156838_3_9_0&sr_pri_blocks=38024009_200156838_3_9_0__24898&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 18,
      "name": "Guesthouse Bella Vista",
      "price": "24",
      "score": "8.7",
      "link": "https://www.booking.com/hotel/ec/patricio-y-mario-hospedaje.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=18&hapos=18&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=198768511_94042279_0_2_0&highlighted_blocks=198768511_94042279_0_2_0&matching_block_id=198768511_94042279_0_2_0&sr_pri_blocks=198768511_94042279_0_2_0__2400&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 19,
      "name": "Itza Hotel Boutique Internacional",
      "price": "326",
      "score": "9.3",
      "link": "https://www.booking.com/hotel/ec/itza-boutique.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=19&hapos=19&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=828542604_347388427_2_1_0&highlighted_blocks=828542604_347388427_2_1_0&matching_block_id=828542604_347388427_2_1_0&sr_pri_blocks=828542604_347388427_2_1_0__32560&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 20,
      "name": "Hostal Casa de Lidice",
      "price": "71",
      "score": "9.1",
      "link": "https://www.booking.com/hotel/ec/casa-de-lidice-bed-amp-breakfast.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=20&hapos=20&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=103741801_169658527_2_1_0&highlighted_blocks=103741801_169658527_2_1_0&matching_block_id=103741801_169658527_2_1_0&sr_pri_blocks=103741801_169658527_2_1_0__7128&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 21,
      "name": "Apartamentos Otorongo Cuenca Ecuador",
      "price": "136",
      "score": "8.9",
      "link": "https://www.booking.com/hotel/ec/apartamentos-otorongo.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=21&hapos=21&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=46451510_197610807_2_0_0&highlighted_blocks=46451510_197610807_2_0_0&matching_block_id=46451510_197610807_2_0_0&sr_pri_blocks=46451510_197610807_2_0_0__13585&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 22,
      "name": "El Dorado Hotel",
      "price": "157",
      "score": "9",
      "link": "https://www.booking.com/hotel/ec/el-dorado.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=22&hapos=22&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=87487703_201882350_0_2_0&highlighted_blocks=87487703_201882350_0_2_0&matching_block_id=87487703_201882350_0_2_0&sr_pri_blocks=87487703_201882350_0_2_0__15708&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 23,
      "name": "Check Inn Bed and Breakfast",
      "price": "29",
      "score": "7.7",
      "link": "https://www.booking.com/hotel/ec/check-inn-cuenca.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=23&hapos=23&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=87402011_94070276_2_1_0&highlighted_blocks=87402011_94070276_2_1_0&matching_block_id=87402011_94070276_2_1_0&sr_pri_blocks=87402011_94070276_2_1_0__2898&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 24,
      "name": "Hotel Valgus",
      "price": "171",
      "score": "8.7",
      "link": "https://www.booking.com/hotel/ec/valgus.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=24&hapos=24&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=115430901_231843526_2_1_0&highlighted_blocks=115430901_231843526_2_1_0&matching_block_id=115430901_231843526_2_1_0&sr_pri_blocks=115430901_231843526_2_1_0__17100&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 25,
      "name": "Hotel Spa Santa Ana",
      "price": "94",
      "score": "7.5",
      "link": "https://www.booking.com/hotel/ec/suites-y-spa-santa-ana.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=25&hapos=25&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=653952109_266526834_0_2_0&highlighted_blocks=653952109_266526834_0_2_0&matching_block_id=653952109_266526834_0_2_0&sr_pri_blocks=653952109_266526834_0_2_0__9405&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 26,
      "name": "Hotel Santiago de Compostella Suites",
      "price": "104",
      "score": "8.1",
      "link": "https://www.booking.com/hotel/ec/santiago-de-compostella-suite.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=1&hapos=1&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=168320811_366577311_0_1_0&highlighted_blocks=168320811_366577311_0_1_0&matching_block_id=168320811_366577311_0_1_0&sr_pri_blocks=168320811_366577311_0_1_0__10400&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 27,
      "name": "Floré Hotel Boutique",
      "price": "78",
      "score": "8.9",
      "link": "https://www.booking.com/hotel/ec/flore-boutique.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=2&hapos=2&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=307181819_310108407_2_41_0&highlighted_blocks=307181819_310108407_2_41_0&matching_block_id=307181819_310108407_2_41_0&sr_pri_blocks=307181819_310108407_2_41_0__7800&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 28,
      "name": "Loft NASS Atahualpa",
      "price": "95",
      "score": "8.6",
      "link": "https://www.booking.com/hotel/ec/loft-nass-atahualpa.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=3&hapos=3&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=759828306_347671561_3_1_0&highlighted_blocks=759828306_347671561_3_1_0&matching_block_id=759828306_347671561_3_1_0&sr_pri_blocks=759828306_347671561_3_1_0__9460&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 29,
      "name": "Hostal Posada del Angel",
      "price": "141",
      "score": "9.3",
      "link": "https://www.booking.com/hotel/ec/posadadelangel.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=4&hapos=4&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=9463902_94304056_2_41_0&highlighted_blocks=9463902_94304056_2_41_0&matching_block_id=9463902_94304056_2_41_0&sr_pri_blocks=9463902_94304056_2_41_0__14136&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 30,
      "name": "Hotel La Orquidea",
      "price": "70",
      "score": "8.8",
      "link": "https://www.booking.com/hotel/ec/hostal-la-orquidea.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=5&hapos=5&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=115363602_285349506_2_0_0&highlighted_blocks=115363602_285349506_2_0_0&matching_block_id=115363602_285349506_2_0_0&sr_pri_blocks=115363602_285349506_2_0_0__7000&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 31,
      "name": "Hotel Boutique Castilla de Léon",
      "price": "52",
      "score": "8",
      "link": "https://www.booking.com/hotel/ec/boutique-castilla-de-leon.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=6&hapos=6&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=259100910_104591953_2_2_0&highlighted_blocks=259100910_104591953_2_2_0&matching_block_id=259100910_104591953_2_2_0&sr_pri_blocks=259100910_104591953_2_2_0__5225&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 32,
      "name": "Selina Cuenca",
      "price": "71",
      "score": "8.3",
      "link": "https://www.booking.com/hotel/ec/crespo.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=7&hapos=7&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=27754805_295775667_0_41_0&highlighted_blocks=27754805_295775667_0_41_0&matching_block_id=27754805_295775667_0_41_0&sr_pri_blocks=27754805_295775667_0_41_0__7092&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 33,
      "name": "Hotel Posada del Rey",
      "price": "60",
      "score": "8.8",
      "link": "https://www.booking.com/hotel/ec/posada-del-rey.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=8&hapos=8&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=124028807_348115264_0_2_0&highlighted_blocks=124028807_348115264_0_2_0&matching_block_id=124028807_348115264_0_2_0&sr_pri_blocks=124028807_348115264_0_2_0__5950&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 34,
      "name": "Hotel Azul de la Plaza",
      "price": "97",
      "score": "8.7",
      "link": "https://www.booking.com/hotel/ec/azul-de-la-plaza-san-sebastian-cuenca.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=9&hapos=9&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=599404401_235119628_0_1_0&highlighted_blocks=599404401_235119628_0_1_0&matching_block_id=599404401_235119628_0_1_0&sr_pri_blocks=599404401_235119628_0_1_0__9720&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 35,
      "name": "Pepe's House Cuenca Boutique Hotel l B&B",
      "price": "90",
      "score": "9.3",
      "link": "https://www.booking.com/hotel/ec/casa-sucre-cuenca1.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=10&hapos=10&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=90251117_286816048_2_1_0&highlighted_blocks=90251117_286816048_2_1_0&matching_block_id=90251117_286816048_2_1_0&sr_pri_blocks=90251117_286816048_2_1_0__8958&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 36,
      "name": "Hostal Mariscal Inn & Suite",
      "price": "55",
      "score": "8.4",
      "link": "https://www.booking.com/hotel/ec/hostal-mariscal.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=11&hapos=11&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=775698302_335863330_2_41_0&highlighted_blocks=775698302_335863330_2_41_0&matching_block_id=775698302_335863330_2_41_0&sr_pri_blocks=775698302_335863330_2_41_0__5526&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 37,
      "name": "Villa Emilia Hostal",
      "price": "76",
      "score": "9.4",
      "link": "https://www.booking.com/hotel/ec/villa-emilia-hostal.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=12&hapos=12&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=124840905_266318746_2_1_0&highlighted_blocks=124840905_266318746_2_1_0&matching_block_id=124840905_266318746_2_1_0&sr_pri_blocks=124840905_266318746_2_1_0__7600&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 38,
      "name": "Morenica del Rosario",
      "price": "76",
      "score": "8.5",
      "link": "https://www.booking.com/hotel/ec/morenica-del-rosario.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=13&hapos=13&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=31956008_201931846_0_1_0&highlighted_blocks=31956008_201931846_0_1_0&matching_block_id=31956008_201931846_0_1_0&sr_pri_blocks=31956008_201931846_0_1_0__7600&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 39,
      "name": "Nonno’s House",
      "price": "61",
      "score": "0",
      "link": "https://www.booking.com/hotel/ec/nonnos-house.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=14&hapos=14&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=954998301_367998313_2_0_0&highlighted_blocks=954998301_367998313_2_0_0&matching_block_id=954998301_367998313_2_0_0&sr_pri_blocks=954998301_367998313_2_0_0__6080&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 40,
      "name": "Four Points by Sheraton Cuenca",
      "price": "223",
      "score": "9",
      "link": "https://www.booking.com/hotel/ec/four-points-by-sheraton-cuenca.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=15&hapos=15&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=273410706_246434816_0_41_0&highlighted_blocks=273410706_246434816_0_41_0&matching_block_id=273410706_246434816_0_41_0&sr_pri_blocks=273410706_246434816_0_41_0__22300&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 41,
      "name": "Hotel Nass Pinar del Lago",
      "price": "124",
      "score": "8.4",
      "link": "https://www.booking.com/hotel/ec/pinar-del-lago.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=16&hapos=16&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=50036909_326384576_2_2_0&highlighted_blocks=50036909_326384576_2_2_0&matching_block_id=50036909_326384576_2_2_0&sr_pri_blocks=50036909_326384576_2_2_0__12420&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 42,
      "name": "Hosteria Dos Chorreras",
      "price": "249",
      "score": "8.9",
      "link": "https://www.booking.com/hotel/ec/hosteria-dos-chorreras.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=17&hapos=17&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=38024009_200156838_3_9_0&highlighted_blocks=38024009_200156838_3_9_0&matching_block_id=38024009_200156838_3_9_0&sr_pri_blocks=38024009_200156838_3_9_0__24898&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 43,
      "name": "Guesthouse Bella Vista",
      "price": "24",
      "score": "8.7",
      "link": "https://www.booking.com/hotel/ec/patricio-y-mario-hospedaje.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=18&hapos=18&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=198768511_94042279_0_2_0&highlighted_blocks=198768511_94042279_0_2_0&matching_block_id=198768511_94042279_0_2_0&sr_pri_blocks=198768511_94042279_0_2_0__2400&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 44,
      "name": "Itza Hotel Boutique Internacional",
      "price": "326",
      "score": "9.3",
      "link": "https://www.booking.com/hotel/ec/itza-boutique.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=19&hapos=19&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=828542604_347388427_2_1_0&highlighted_blocks=828542604_347388427_2_1_0&matching_block_id=828542604_347388427_2_1_0&sr_pri_blocks=828542604_347388427_2_1_0__32560&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 45,
      "name": "Hostal Casa de Lidice",
      "price": "71",
      "score": "9.1",
      "link": "https://www.booking.com/hotel/ec/casa-de-lidice-bed-amp-breakfast.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=20&hapos=20&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=103741801_169658527_2_1_0&highlighted_blocks=103741801_169658527_2_1_0&matching_block_id=103741801_169658527_2_1_0&sr_pri_blocks=103741801_169658527_2_1_0__7128&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 46,
      "name": "Apartamentos Otorongo Cuenca Ecuador",
      "price": "136",
      "score": "8.9",
      "link": "https://www.booking.com/hotel/ec/apartamentos-otorongo.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=21&hapos=21&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=46451510_197610807_2_0_0&highlighted_blocks=46451510_197610807_2_0_0&matching_block_id=46451510_197610807_2_0_0&sr_pri_blocks=46451510_197610807_2_0_0__13585&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 47,
      "name": "El Dorado Hotel",
      "price": "157",
      "score": "9",
      "link": "https://www.booking.com/hotel/ec/el-dorado.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=22&hapos=22&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=87487703_201882350_0_2_0&highlighted_blocks=87487703_201882350_0_2_0&matching_block_id=87487703_201882350_0_2_0&sr_pri_blocks=87487703_201882350_0_2_0__15708&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 48,
      "name": "Check Inn Bed and Breakfast",
      "price": "29",
      "score": "7.7",
      "link": "https://www.booking.com/hotel/ec/check-inn-cuenca.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=23&hapos=23&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=87402011_94070276_2_1_0&highlighted_blocks=87402011_94070276_2_1_0&matching_block_id=87402011_94070276_2_1_0&sr_pri_blocks=87402011_94070276_2_1_0__2898&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 49,
      "name": "Hotel Valgus",
      "price": "171",
      "score": "8.7",
      "link": "https://www.booking.com/hotel/ec/valgus.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=24&hapos=24&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=115430901_231843526_2_1_0&highlighted_blocks=115430901_231843526_2_1_0&matching_block_id=115430901_231843526_2_1_0&sr_pri_blocks=115430901_231843526_2_1_0__17100&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 50,
      "name": "Hotel Spa Santa Ana",
      "price": "94",
      "score": "7.5",
      "link": "https://www.booking.com/hotel/ec/suites-y-spa-santa-ana.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=25&hapos=25&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=653952109_266526834_0_2_0&highlighted_blocks=653952109_266526834_0_2_0&matching_block_id=653952109_266526834_0_2_0&sr_pri_blocks=653952109_266526834_0_2_0__9405&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 51,
      "name": "Hotel Santiago de Compostella Suites",
      "price": "104",
      "score": "8.1",
      "link": "https://www.booking.com/hotel/ec/santiago-de-compostella-suite.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=1&hapos=1&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=168320811_366577311_0_1_0&highlighted_blocks=168320811_366577311_0_1_0&matching_block_id=168320811_366577311_0_1_0&sr_pri_blocks=168320811_366577311_0_1_0__10400&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 52,
      "name": "Floré Hotel Boutique",
      "price": "78",
      "score": "8.9",
      "link": "https://www.booking.com/hotel/ec/flore-boutique.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=2&hapos=2&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=307181819_310108407_2_41_0&highlighted_blocks=307181819_310108407_2_41_0&matching_block_id=307181819_310108407_2_41_0&sr_pri_blocks=307181819_310108407_2_41_0__7800&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 53,
      "name": "Loft NASS Atahualpa",
      "price": "95",
      "score": "8.6",
      "link": "https://www.booking.com/hotel/ec/loft-nass-atahualpa.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=3&hapos=3&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=759828306_347671561_3_1_0&highlighted_blocks=759828306_347671561_3_1_0&matching_block_id=759828306_347671561_3_1_0&sr_pri_blocks=759828306_347671561_3_1_0__9460&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 54,
      "name": "Hostal Posada del Angel",
      "price": "141",
      "score": "9.3",
      "link": "https://www.booking.com/hotel/ec/posadadelangel.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=4&hapos=4&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=9463902_94304056_2_41_0&highlighted_blocks=9463902_94304056_2_41_0&matching_block_id=9463902_94304056_2_41_0&sr_pri_blocks=9463902_94304056_2_41_0__14136&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 55,
      "name": "Hotel La Orquidea",
      "price": "70",
      "score": "8.8",
      "link": "https://www.booking.com/hotel/ec/hostal-la-orquidea.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=5&hapos=5&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=115363602_285349506_2_0_0&highlighted_blocks=115363602_285349506_2_0_0&matching_block_id=115363602_285349506_2_0_0&sr_pri_blocks=115363602_285349506_2_0_0__7000&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 56,
      "name": "Hotel Boutique Castilla de Léon",
      "price": "52",
      "score": "8",
      "link": "https://www.booking.com/hotel/ec/boutique-castilla-de-leon.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=6&hapos=6&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=259100910_104591953_2_2_0&highlighted_blocks=259100910_104591953_2_2_0&matching_block_id=259100910_104591953_2_2_0&sr_pri_blocks=259100910_104591953_2_2_0__5225&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 57,
      "name": "Selina Cuenca",
      "price": "71",
      "score": "8.3",
      "link": "https://www.booking.com/hotel/ec/crespo.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=7&hapos=7&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=27754805_295775667_0_41_0&highlighted_blocks=27754805_295775667_0_41_0&matching_block_id=27754805_295775667_0_41_0&sr_pri_blocks=27754805_295775667_0_41_0__7092&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 58,
      "name": "Hotel Posada del Rey",
      "price": "60",
      "score": "8.8",
      "link": "https://www.booking.com/hotel/ec/posada-del-rey.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=8&hapos=8&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=124028807_348115264_0_2_0&highlighted_blocks=124028807_348115264_0_2_0&matching_block_id=124028807_348115264_0_2_0&sr_pri_blocks=124028807_348115264_0_2_0__5950&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 59,
      "name": "Hotel Azul de la Plaza",
      "price": "97",
      "score": "8.7",
      "link": "https://www.booking.com/hotel/ec/azul-de-la-plaza-san-sebastian-cuenca.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=9&hapos=9&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=599404401_235119628_0_1_0&highlighted_blocks=599404401_235119628_0_1_0&matching_block_id=599404401_235119628_0_1_0&sr_pri_blocks=599404401_235119628_0_1_0__9720&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 60,
      "name": "Pepe's House Cuenca Boutique Hotel l B&B",
      "price": "90",
      "score": "9.3",
      "link": "https://www.booking.com/hotel/ec/casa-sucre-cuenca1.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=10&hapos=10&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=90251117_286816048_2_1_0&highlighted_blocks=90251117_286816048_2_1_0&matching_block_id=90251117_286816048_2_1_0&sr_pri_blocks=90251117_286816048_2_1_0__8958&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 61,
      "name": "Hostal Mariscal Inn & Suite",
      "price": "55",
      "score": "8.4",
      "link": "https://www.booking.com/hotel/ec/hostal-mariscal.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=11&hapos=11&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=775698302_335863330_2_41_0&highlighted_blocks=775698302_335863330_2_41_0&matching_block_id=775698302_335863330_2_41_0&sr_pri_blocks=775698302_335863330_2_41_0__5526&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 62,
      "name": "Villa Emilia Hostal",
      "price": "76",
      "score": "9.4",
      "link": "https://www.booking.com/hotel/ec/villa-emilia-hostal.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=12&hapos=12&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=124840905_266318746_2_1_0&highlighted_blocks=124840905_266318746_2_1_0&matching_block_id=124840905_266318746_2_1_0&sr_pri_blocks=124840905_266318746_2_1_0__7600&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 63,
      "name": "Morenica del Rosario",
      "price": "76",
      "score": "8.5",
      "link": "https://www.booking.com/hotel/ec/morenica-del-rosario.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=13&hapos=13&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=31956008_201931846_0_1_0&highlighted_blocks=31956008_201931846_0_1_0&matching_block_id=31956008_201931846_0_1_0&sr_pri_blocks=31956008_201931846_0_1_0__7600&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 64,
      "name": "Nonno’s House",
      "price": "61",
      "score": "0",
      "link": "https://www.booking.com/hotel/ec/nonnos-house.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=14&hapos=14&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=954998301_367998313_2_0_0&highlighted_blocks=954998301_367998313_2_0_0&matching_block_id=954998301_367998313_2_0_0&sr_pri_blocks=954998301_367998313_2_0_0__6080&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 65,
      "name": "Four Points by Sheraton Cuenca",
      "price": "223",
      "score": "9",
      "link": "https://www.booking.com/hotel/ec/four-points-by-sheraton-cuenca.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=15&hapos=15&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=273410706_246434816_0_41_0&highlighted_blocks=273410706_246434816_0_41_0&matching_block_id=273410706_246434816_0_41_0&sr_pri_blocks=273410706_246434816_0_41_0__22300&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 66,
      "name": "Hotel Nass Pinar del Lago",
      "price": "124",
      "score": "8.4",
      "link": "https://www.booking.com/hotel/ec/pinar-del-lago.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=16&hapos=16&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=50036909_326384576_2_2_0&highlighted_blocks=50036909_326384576_2_2_0&matching_block_id=50036909_326384576_2_2_0&sr_pri_blocks=50036909_326384576_2_2_0__12420&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 67,
      "name": "Hosteria Dos Chorreras",
      "price": "249",
      "score": "8.9",
      "link": "https://www.booking.com/hotel/ec/hosteria-dos-chorreras.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=17&hapos=17&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=38024009_200156838_3_9_0&highlighted_blocks=38024009_200156838_3_9_0&matching_block_id=38024009_200156838_3_9_0&sr_pri_blocks=38024009_200156838_3_9_0__24898&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 68,
      "name": "Guesthouse Bella Vista",
      "price": "24",
      "score": "8.7",
      "link": "https://www.booking.com/hotel/ec/patricio-y-mario-hospedaje.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=18&hapos=18&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=198768511_94042279_0_2_0&highlighted_blocks=198768511_94042279_0_2_0&matching_block_id=198768511_94042279_0_2_0&sr_pri_blocks=198768511_94042279_0_2_0__2400&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 69,
      "name": "Itza Hotel Boutique Internacional",
      "price": "326",
      "score": "9.3",
      "link": "https://www.booking.com/hotel/ec/itza-boutique.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=19&hapos=19&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=828542604_347388427_2_1_0&highlighted_blocks=828542604_347388427_2_1_0&matching_block_id=828542604_347388427_2_1_0&sr_pri_blocks=828542604_347388427_2_1_0__32560&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 70,
      "name": "Hostal Casa de Lidice",
      "price": "71",
      "score": "9.1",
      "link": "https://www.booking.com/hotel/ec/casa-de-lidice-bed-amp-breakfast.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=20&hapos=20&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=103741801_169658527_2_1_0&highlighted_blocks=103741801_169658527_2_1_0&matching_block_id=103741801_169658527_2_1_0&sr_pri_blocks=103741801_169658527_2_1_0__7128&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 71,
      "name": "Apartamentos Otorongo Cuenca Ecuador",
      "price": "136",
      "score": "8.9",
      "link": "https://www.booking.com/hotel/ec/apartamentos-otorongo.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=21&hapos=21&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=46451510_197610807_2_0_0&highlighted_blocks=46451510_197610807_2_0_0&matching_block_id=46451510_197610807_2_0_0&sr_pri_blocks=46451510_197610807_2_0_0__13585&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 72,
      "name": "El Dorado Hotel",
      "price": "157",
      "score": "9",
      "link": "https://www.booking.com/hotel/ec/el-dorado.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=22&hapos=22&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=87487703_201882350_0_2_0&highlighted_blocks=87487703_201882350_0_2_0&matching_block_id=87487703_201882350_0_2_0&sr_pri_blocks=87487703_201882350_0_2_0__15708&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 73,
      "name": "Check Inn Bed and Breakfast",
      "price": "29",
      "score": "7.7",
      "link": "https://www.booking.com/hotel/ec/check-inn-cuenca.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=23&hapos=23&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=87402011_94070276_2_1_0&highlighted_blocks=87402011_94070276_2_1_0&matching_block_id=87402011_94070276_2_1_0&sr_pri_blocks=87402011_94070276_2_1_0__2898&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 74,
      "name": "Hotel Valgus",
      "price": "171",
      "score": "8.7",
      "link": "https://www.booking.com/hotel/ec/valgus.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=24&hapos=24&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=115430901_231843526_2_1_0&highlighted_blocks=115430901_231843526_2_1_0&matching_block_id=115430901_231843526_2_1_0&sr_pri_blocks=115430901_231843526_2_1_0__17100&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 75,
      "name": "Hotel Spa Santa Ana",
      "price": "94",
      "score": "7.5",
      "link": "https://www.booking.com/hotel/ec/suites-y-spa-santa-ana.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-926345&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=25&hapos=25&sr_order=popularity&srpvid=548702141cac0276&srepoch=1675124267&all_sr_blocks=653952109_266526834_0_2_0&highlighted_blocks=653952109_266526834_0_2_0&matching_block_id=653952109_266526834_0_2_0&sr_pri_blocks=653952109_266526834_0_2_0__9405&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Cuenca"
        }
    )
    batch.put_item(
    Item={
      "id": 1,
      "name": "Hotel David",
      "price": "66",
      "score": "8.7",
      "link": "https://www.booking.com/hotel/ec/david.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=1&hapos=1&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=142038301_264102423_2_1_0&highlighted_blocks=142038301_264102423_2_1_0&matching_block_id=142038301_264102423_2_1_0&sr_pri_blocks=142038301_264102423_2_1_0__6646&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 2,
      "name": "Rincón Familiar Hostel Boutique",
      "price": "94",
      "score": "8.3",
      "link": "https://www.booking.com/hotel/ec/rincon-familiar.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=2&hapos=2&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=113469206_289907624_2_1_0&highlighted_blocks=113469206_289907624_2_1_0&matching_block_id=113469206_289907624_2_1_0&sr_pri_blocks=113469206_289907624_2_1_0__9350&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 3,
      "name": "Adamas House Hotel Boutique",
      "price": "187",
      "score": "9.4",
      "link": "https://www.booking.com/hotel/ec/adamas-house-quito1.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=3&hapos=3&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=549004318_220959955_2_1_0&highlighted_blocks=549004318_220959955_2_1_0&matching_block_id=549004318_220959955_2_1_0&sr_pri_blocks=549004318_220959955_2_1_0__18666&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 4,
      "name": "Boutique Hotel Antinea",
      "price": "112",
      "score": "8.9",
      "link": "https://www.booking.com/hotel/ec/antinea.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=4&hapos=4&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=27202923_367804849_2_1_0&highlighted_blocks=27202923_367804849_2_1_0&matching_block_id=27202923_367804849_2_1_0&sr_pri_blocks=27202923_367804849_2_1_0__11178&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 5,
      "name": "Suite independiente zona financiera",
      "price": "45",
      "score": "0",
      "link": "https://www.booking.com/hotel/ec/suite-independiente-zona-financiera-quito.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=5&hapos=5&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=955057501_368002659_2_2_0&highlighted_blocks=955057501_368002659_2_2_0&matching_block_id=955057501_368002659_2_2_0&sr_pri_blocks=955057501_368002659_2_2_0__4480&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 6,
      "name": "Hotel Bellavista Quito",
      "price": "86",
      "score": "8.1",
      "link": "https://www.booking.com/hotel/ec/ventanal-de-bellavista.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=6&hapos=6&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=155343302_88364357_2_41_0&highlighted_blocks=155343302_88364357_2_41_0&matching_block_id=155343302_88364357_2_41_0&sr_pri_blocks=155343302_88364357_2_41_0__8645&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 7,
      "name": "Hotel Bernys Estrellita",
      "price": "35",
      "score": "7.7",
      "link": "https://www.booking.com/hotel/ec/bernys.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=7&hapos=7&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=915821402_363044384_2_2_0&highlighted_blocks=915821402_363044384_2_2_0&matching_block_id=915821402_363044384_2_2_0&sr_pri_blocks=915821402_363044384_2_2_0__3456&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 8,
      "name": "EL LIMONAL",
      "price": "51",
      "score": "0",
      "link": "https://www.booking.com/hotel/ec/el-limonal.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=8&hapos=8&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=954357601_367955296_2_0_0&highlighted_blocks=954357601_367955296_2_0_0&matching_block_id=954357601_367955296_2_0_0&sr_pri_blocks=954357601_367955296_2_0_0__5100&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 9,
      "name": "Wyndham Garden Quito",
      "price": "160",
      "score": "9",
      "link": "https://www.booking.com/hotel/ec/wyndham-garden-quito.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=9&hapos=9&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=26949713_285737265_2_0_0&highlighted_blocks=26949713_285737265_2_0_0&matching_block_id=26949713_285737265_2_0_0&sr_pri_blocks=26949713_285737265_2_0_0__16020&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 10,
      "name": "ITSA HOME - Torre QL805 202B",
      "price": "75",
      "score": "0",
      "link": "https://www.booking.com/hotel/ec/itsa-home-torre-ql805-202b.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=10&hapos=10&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=955060301_368002905_2_0_0&highlighted_blocks=955060301_368002905_2_0_0&matching_block_id=955060301_368002905_2_0_0&sr_pri_blocks=955060301_368002905_2_0_0__7480&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 11,
      "name": "Posada Tambuca",
      "price": "44",
      "score": "9.4",
      "link": "https://www.booking.com/hotel/ec/posada-tambuca.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=11&hapos=11&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=43707425_190284299_2_1_0&highlighted_blocks=43707425_190284299_2_1_0&matching_block_id=43707425_190284299_2_1_0&sr_pri_blocks=43707425_190284299_2_1_0__4400&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 12,
      "name": "Hostal Yumbo Imperial",
      "price": "23",
      "score": "8.4",
      "link": "https://www.booking.com/hotel/ec/yumbo-imperial.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=12&hapos=12&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=108711204_184422779_0_2_0&highlighted_blocks=108711204_184422779_0_2_0&matching_block_id=108711204_184422779_0_2_0&sr_pri_blocks=108711204_184422779_0_2_0__2340&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 13,
      "name": "Hostal L'Auberge Inn",
      "price": "48",
      "score": "8.7",
      "link": "https://www.booking.com/hotel/ec/hostal-auberge-inn.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=13&hapos=13&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=40177910_213957222_0_2_0&highlighted_blocks=40177910_213957222_0_2_0&matching_block_id=40177910_213957222_0_2_0&sr_pri_blocks=40177910_213957222_0_2_0__4760&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 14,
      "name": "Hotel Reina Isabel",
      "price": "156",
      "score": "8.9",
      "link": "https://www.booking.com/hotel/ec/reina-isabel.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=14&hapos=14&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=34454701_221196700_0_41_0&highlighted_blocks=34454701_221196700_0_41_0&matching_block_id=34454701_221196700_0_41_0&sr_pri_blocks=34454701_221196700_0_41_0__15600&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 15,
      "name": "La Rosario Hostal",
      "price": "27",
      "score": "0",
      "link": "https://www.booking.com/hotel/ec/la-rosario-hostal.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=15&hapos=15&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=955610301_368056857_2_0_0&highlighted_blocks=955610301_368056857_2_0_0&matching_block_id=955610301_368056857_2_0_0&sr_pri_blocks=955610301_368056857_2_0_0__2720&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 16,
      "name": "Hotel Finlandia",
      "price": "300",
      "score": "8.8",
      "link": "https://www.booking.com/hotel/ec/finlandia-quito.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=16&hapos=16&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=32258504_347833927_2_41_0&highlighted_blocks=32258504_347833927_2_41_0&matching_block_id=32258504_347833927_2_41_0&sr_pri_blocks=32258504_347833927_2_41_0__30000&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 17,
      "name": "Hotel Casona 1914",
      "price": "353",
      "score": "9.7",
      "link": "https://www.booking.com/hotel/ec/boutique-casona-d-39-alameda.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=17&hapos=17&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=442331418_330973113_2_1_0&highlighted_blocks=442331418_330973113_2_1_0&matching_block_id=442331418_330973113_2_1_0&sr_pri_blocks=442331418_330973113_2_1_0__35343&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 18,
      "name": "Hostal Juana de Arco",
      "price": "40",
      "score": "8.3",
      "link": "https://www.booking.com/hotel/ec/juana-de-arco.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=18&hapos=18&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=131472904_344326747_2_1_0&highlighted_blocks=131472904_344326747_2_1_0&matching_block_id=131472904_344326747_2_1_0&sr_pri_blocks=131472904_344326747_2_1_0__3990&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 19,
      "name": "Bonito Departamento Sur de Quito",
      "price": "60",
      "score": "0",
      "link": "https://www.booking.com/hotel/ec/bonito-departamento-sur-de-quito.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=19&hapos=19&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=955226601_368014456_2_0_0&highlighted_blocks=955226601_368014456_2_0_0&matching_block_id=955226601_368014456_2_0_0&sr_pri_blocks=955226601_368014456_2_0_0__5950&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 20,
      "name": "ibis Quito",
      "price": "160",
      "score": "8.8",
      "link": "https://www.booking.com/hotel/ec/ibis-quito.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=20&hapos=20&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=432406501_246094429_2_41_0&highlighted_blocks=432406501_246094429_2_41_0&matching_block_id=432406501_246094429_2_41_0&sr_pri_blocks=432406501_246094429_2_41_0__16000&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 21,
      "name": "ArtPlaza",
      "price": "73",
      "score": "8.8",
      "link": "https://www.booking.com/hotel/ec/artplaza.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=21&hapos=21&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=116994001_295810281_0_2_0&highlighted_blocks=116994001_295810281_0_2_0&matching_block_id=116994001_295810281_0_2_0&sr_pri_blocks=116994001_295810281_0_2_0__7344&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 22,
      "name": "ITSAHOME Apartments Torre Seis",
      "price": "116",
      "score": "8.7",
      "link": "https://www.booking.com/hotel/ec/itsahome-apartments.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=22&hapos=22&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=110945713_208105836_2_0_0&highlighted_blocks=110945713_208105836_2_0_0&matching_block_id=110945713_208105836_2_0_0&sr_pri_blocks=110945713_208105836_2_0_0__11600&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 23,
      "name": "Vista del Angel Hotel Boutique",
      "price": "255",
      "score": "9.3",
      "link": "https://www.booking.com/hotel/ec/vista-del-angel-boutique.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=23&hapos=23&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=258612207_339828813_2_33_0&highlighted_blocks=258612207_339828813_2_33_0&matching_block_id=258612207_339828813_2_33_0&sr_pri_blocks=258612207_339828813_2_33_0__25520&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 24,
      "name": "Hotel Huasi Continental",
      "price": "74",
      "score": "8.2",
      "link": "https://www.booking.com/hotel/ec/huasi-continental.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=24&hapos=24&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=33130705_265683207_0_1_0&highlighted_blocks=33130705_265683207_0_1_0&matching_block_id=33130705_265683207_0_1_0&sr_pri_blocks=33130705_265683207_0_1_0__7402&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 25,
      "name": "Dann Carlton Quito",
      "price": "300",
      "score": "8.7",
      "link": "https://www.booking.com/hotel/ec/dann-carlton-quito.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=25&hapos=25&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=30094701_143539561_0_1_0&highlighted_blocks=30094701_143539561_0_1_0&matching_block_id=30094701_143539561_0_1_0&sr_pri_blocks=30094701_143539561_0_1_0__30000&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 26,
      "name": "Hotel David",
      "price": "66",
      "score": "8.7",
      "link": "https://www.booking.com/hotel/ec/david.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=1&hapos=1&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=142038301_264102423_2_1_0&highlighted_blocks=142038301_264102423_2_1_0&matching_block_id=142038301_264102423_2_1_0&sr_pri_blocks=142038301_264102423_2_1_0__6646&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 27,
      "name": "Rincón Familiar Hostel Boutique",
      "price": "94",
      "score": "8.3",
      "link": "https://www.booking.com/hotel/ec/rincon-familiar.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=2&hapos=2&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=113469206_289907624_2_1_0&highlighted_blocks=113469206_289907624_2_1_0&matching_block_id=113469206_289907624_2_1_0&sr_pri_blocks=113469206_289907624_2_1_0__9350&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 28,
      "name": "Adamas House Hotel Boutique",
      "price": "187",
      "score": "9.4",
      "link": "https://www.booking.com/hotel/ec/adamas-house-quito1.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=3&hapos=3&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=549004318_220959955_2_1_0&highlighted_blocks=549004318_220959955_2_1_0&matching_block_id=549004318_220959955_2_1_0&sr_pri_blocks=549004318_220959955_2_1_0__18666&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 29,
      "name": "Boutique Hotel Antinea",
      "price": "112",
      "score": "8.9",
      "link": "https://www.booking.com/hotel/ec/antinea.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=4&hapos=4&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=27202923_367804849_2_1_0&highlighted_blocks=27202923_367804849_2_1_0&matching_block_id=27202923_367804849_2_1_0&sr_pri_blocks=27202923_367804849_2_1_0__11178&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 30,
      "name": "Suite independiente zona financiera",
      "price": "45",
      "score": "0",
      "link": "https://www.booking.com/hotel/ec/suite-independiente-zona-financiera-quito.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=5&hapos=5&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=955057501_368002659_2_2_0&highlighted_blocks=955057501_368002659_2_2_0&matching_block_id=955057501_368002659_2_2_0&sr_pri_blocks=955057501_368002659_2_2_0__4480&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 31,
      "name": "Hotel Bellavista Quito",
      "price": "86",
      "score": "8.1",
      "link": "https://www.booking.com/hotel/ec/ventanal-de-bellavista.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=6&hapos=6&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=155343302_88364357_2_41_0&highlighted_blocks=155343302_88364357_2_41_0&matching_block_id=155343302_88364357_2_41_0&sr_pri_blocks=155343302_88364357_2_41_0__8645&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 32,
      "name": "Hotel Bernys Estrellita",
      "price": "35",
      "score": "7.7",
      "link": "https://www.booking.com/hotel/ec/bernys.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=7&hapos=7&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=915821402_363044384_2_2_0&highlighted_blocks=915821402_363044384_2_2_0&matching_block_id=915821402_363044384_2_2_0&sr_pri_blocks=915821402_363044384_2_2_0__3456&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 33,
      "name": "EL LIMONAL",
      "price": "51",
      "score": "0",
      "link": "https://www.booking.com/hotel/ec/el-limonal.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=8&hapos=8&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=954357601_367955296_2_0_0&highlighted_blocks=954357601_367955296_2_0_0&matching_block_id=954357601_367955296_2_0_0&sr_pri_blocks=954357601_367955296_2_0_0__5100&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 34,
      "name": "Wyndham Garden Quito",
      "price": "160",
      "score": "9",
      "link": "https://www.booking.com/hotel/ec/wyndham-garden-quito.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=9&hapos=9&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=26949713_285737265_2_0_0&highlighted_blocks=26949713_285737265_2_0_0&matching_block_id=26949713_285737265_2_0_0&sr_pri_blocks=26949713_285737265_2_0_0__16020&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 35,
      "name": "ITSA HOME - Torre QL805 202B",
      "price": "75",
      "score": "0",
      "link": "https://www.booking.com/hotel/ec/itsa-home-torre-ql805-202b.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=10&hapos=10&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=955060301_368002905_2_0_0&highlighted_blocks=955060301_368002905_2_0_0&matching_block_id=955060301_368002905_2_0_0&sr_pri_blocks=955060301_368002905_2_0_0__7480&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 36,
      "name": "Posada Tambuca",
      "price": "44",
      "score": "9.4",
      "link": "https://www.booking.com/hotel/ec/posada-tambuca.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=11&hapos=11&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=43707425_190284299_2_1_0&highlighted_blocks=43707425_190284299_2_1_0&matching_block_id=43707425_190284299_2_1_0&sr_pri_blocks=43707425_190284299_2_1_0__4400&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 37,
      "name": "Hostal Yumbo Imperial",
      "price": "23",
      "score": "8.4",
      "link": "https://www.booking.com/hotel/ec/yumbo-imperial.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=12&hapos=12&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=108711204_184422779_0_2_0&highlighted_blocks=108711204_184422779_0_2_0&matching_block_id=108711204_184422779_0_2_0&sr_pri_blocks=108711204_184422779_0_2_0__2340&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 38,
      "name": "Hostal L'Auberge Inn",
      "price": "48",
      "score": "8.7",
      "link": "https://www.booking.com/hotel/ec/hostal-auberge-inn.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=13&hapos=13&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=40177910_213957222_0_2_0&highlighted_blocks=40177910_213957222_0_2_0&matching_block_id=40177910_213957222_0_2_0&sr_pri_blocks=40177910_213957222_0_2_0__4760&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 39,
      "name": "Hotel Reina Isabel",
      "price": "156",
      "score": "8.9",
      "link": "https://www.booking.com/hotel/ec/reina-isabel.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=14&hapos=14&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=34454701_221196700_0_41_0&highlighted_blocks=34454701_221196700_0_41_0&matching_block_id=34454701_221196700_0_41_0&sr_pri_blocks=34454701_221196700_0_41_0__15600&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 40,
      "name": "La Rosario Hostal",
      "price": "27",
      "score": "0",
      "link": "https://www.booking.com/hotel/ec/la-rosario-hostal.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=15&hapos=15&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=955610301_368056857_2_0_0&highlighted_blocks=955610301_368056857_2_0_0&matching_block_id=955610301_368056857_2_0_0&sr_pri_blocks=955610301_368056857_2_0_0__2720&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 41,
      "name": "Hotel Finlandia",
      "price": "300",
      "score": "8.8",
      "link": "https://www.booking.com/hotel/ec/finlandia-quito.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=16&hapos=16&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=32258504_347833927_2_41_0&highlighted_blocks=32258504_347833927_2_41_0&matching_block_id=32258504_347833927_2_41_0&sr_pri_blocks=32258504_347833927_2_41_0__30000&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 42,
      "name": "Hotel Casona 1914",
      "price": "353",
      "score": "9.7",
      "link": "https://www.booking.com/hotel/ec/boutique-casona-d-39-alameda.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=17&hapos=17&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=442331418_330973113_2_1_0&highlighted_blocks=442331418_330973113_2_1_0&matching_block_id=442331418_330973113_2_1_0&sr_pri_blocks=442331418_330973113_2_1_0__35343&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 43,
      "name": "Hostal Juana de Arco",
      "price": "40",
      "score": "8.3",
      "link": "https://www.booking.com/hotel/ec/juana-de-arco.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=18&hapos=18&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=131472904_344326747_2_1_0&highlighted_blocks=131472904_344326747_2_1_0&matching_block_id=131472904_344326747_2_1_0&sr_pri_blocks=131472904_344326747_2_1_0__3990&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 44,
      "name": "Bonito Departamento Sur de Quito",
      "price": "60",
      "score": "0",
      "link": "https://www.booking.com/hotel/ec/bonito-departamento-sur-de-quito.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=19&hapos=19&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=955226601_368014456_2_0_0&highlighted_blocks=955226601_368014456_2_0_0&matching_block_id=955226601_368014456_2_0_0&sr_pri_blocks=955226601_368014456_2_0_0__5950&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 45,
      "name": "ibis Quito",
      "price": "160",
      "score": "8.8",
      "link": "https://www.booking.com/hotel/ec/ibis-quito.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=20&hapos=20&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=432406501_246094429_2_41_0&highlighted_blocks=432406501_246094429_2_41_0&matching_block_id=432406501_246094429_2_41_0&sr_pri_blocks=432406501_246094429_2_41_0__16000&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 46,
      "name": "ArtPlaza",
      "price": "73",
      "score": "8.8",
      "link": "https://www.booking.com/hotel/ec/artplaza.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=21&hapos=21&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=116994001_295810281_0_2_0&highlighted_blocks=116994001_295810281_0_2_0&matching_block_id=116994001_295810281_0_2_0&sr_pri_blocks=116994001_295810281_0_2_0__7344&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 47,
      "name": "ITSAHOME Apartments Torre Seis",
      "price": "116",
      "score": "8.7",
      "link": "https://www.booking.com/hotel/ec/itsahome-apartments.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=22&hapos=22&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=110945713_208105836_2_0_0&highlighted_blocks=110945713_208105836_2_0_0&matching_block_id=110945713_208105836_2_0_0&sr_pri_blocks=110945713_208105836_2_0_0__11600&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 48,
      "name": "Vista del Angel Hotel Boutique",
      "price": "255",
      "score": "9.3",
      "link": "https://www.booking.com/hotel/ec/vista-del-angel-boutique.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=23&hapos=23&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=258612207_339828813_2_33_0&highlighted_blocks=258612207_339828813_2_33_0&matching_block_id=258612207_339828813_2_33_0&sr_pri_blocks=258612207_339828813_2_33_0__25520&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 49,
      "name": "Hotel Huasi Continental",
      "price": "74",
      "score": "8.2",
      "link": "https://www.booking.com/hotel/ec/huasi-continental.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=24&hapos=24&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=33130705_265683207_0_1_0&highlighted_blocks=33130705_265683207_0_1_0&matching_block_id=33130705_265683207_0_1_0&sr_pri_blocks=33130705_265683207_0_1_0__7402&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 50,
      "name": "Dann Carlton Quito",
      "price": "300",
      "score": "8.7",
      "link": "https://www.booking.com/hotel/ec/dann-carlton-quito.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=25&hapos=25&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=30094701_143539561_0_1_0&highlighted_blocks=30094701_143539561_0_1_0&matching_block_id=30094701_143539561_0_1_0&sr_pri_blocks=30094701_143539561_0_1_0__30000&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 51,
      "name": "Hotel David",
      "price": "66",
      "score": "8.7",
      "link": "https://www.booking.com/hotel/ec/david.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=1&hapos=1&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=142038301_264102423_2_1_0&highlighted_blocks=142038301_264102423_2_1_0&matching_block_id=142038301_264102423_2_1_0&sr_pri_blocks=142038301_264102423_2_1_0__6646&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 52,
      "name": "Rincón Familiar Hostel Boutique",
      "price": "94",
      "score": "8.3",
      "link": "https://www.booking.com/hotel/ec/rincon-familiar.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=2&hapos=2&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=113469206_289907624_2_1_0&highlighted_blocks=113469206_289907624_2_1_0&matching_block_id=113469206_289907624_2_1_0&sr_pri_blocks=113469206_289907624_2_1_0__9350&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 53,
      "name": "Adamas House Hotel Boutique",
      "price": "187",
      "score": "9.4",
      "link": "https://www.booking.com/hotel/ec/adamas-house-quito1.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=3&hapos=3&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=549004318_220959955_2_1_0&highlighted_blocks=549004318_220959955_2_1_0&matching_block_id=549004318_220959955_2_1_0&sr_pri_blocks=549004318_220959955_2_1_0__18666&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 54,
      "name": "Boutique Hotel Antinea",
      "price": "112",
      "score": "8.9",
      "link": "https://www.booking.com/hotel/ec/antinea.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=4&hapos=4&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=27202923_367804849_2_1_0&highlighted_blocks=27202923_367804849_2_1_0&matching_block_id=27202923_367804849_2_1_0&sr_pri_blocks=27202923_367804849_2_1_0__11178&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 55,
      "name": "Suite independiente zona financiera",
      "price": "45",
      "score": "0",
      "link": "https://www.booking.com/hotel/ec/suite-independiente-zona-financiera-quito.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=5&hapos=5&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=955057501_368002659_2_2_0&highlighted_blocks=955057501_368002659_2_2_0&matching_block_id=955057501_368002659_2_2_0&sr_pri_blocks=955057501_368002659_2_2_0__4480&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 56,
      "name": "Hotel Bellavista Quito",
      "price": "86",
      "score": "8.1",
      "link": "https://www.booking.com/hotel/ec/ventanal-de-bellavista.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=6&hapos=6&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=155343302_88364357_2_41_0&highlighted_blocks=155343302_88364357_2_41_0&matching_block_id=155343302_88364357_2_41_0&sr_pri_blocks=155343302_88364357_2_41_0__8645&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 57,
      "name": "Hotel Bernys Estrellita",
      "price": "35",
      "score": "7.7",
      "link": "https://www.booking.com/hotel/ec/bernys.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=7&hapos=7&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=915821402_363044384_2_2_0&highlighted_blocks=915821402_363044384_2_2_0&matching_block_id=915821402_363044384_2_2_0&sr_pri_blocks=915821402_363044384_2_2_0__3456&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 58,
      "name": "EL LIMONAL",
      "price": "51",
      "score": "0",
      "link": "https://www.booking.com/hotel/ec/el-limonal.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=8&hapos=8&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=954357601_367955296_2_0_0&highlighted_blocks=954357601_367955296_2_0_0&matching_block_id=954357601_367955296_2_0_0&sr_pri_blocks=954357601_367955296_2_0_0__5100&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 59,
      "name": "Wyndham Garden Quito",
      "price": "160",
      "score": "9",
      "link": "https://www.booking.com/hotel/ec/wyndham-garden-quito.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=9&hapos=9&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=26949713_285737265_2_0_0&highlighted_blocks=26949713_285737265_2_0_0&matching_block_id=26949713_285737265_2_0_0&sr_pri_blocks=26949713_285737265_2_0_0__16020&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 60,
      "name": "ITSA HOME - Torre QL805 202B",
      "price": "75",
      "score": "0",
      "link": "https://www.booking.com/hotel/ec/itsa-home-torre-ql805-202b.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=10&hapos=10&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=955060301_368002905_2_0_0&highlighted_blocks=955060301_368002905_2_0_0&matching_block_id=955060301_368002905_2_0_0&sr_pri_blocks=955060301_368002905_2_0_0__7480&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 61,
      "name": "Posada Tambuca",
      "price": "44",
      "score": "9.4",
      "link": "https://www.booking.com/hotel/ec/posada-tambuca.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=11&hapos=11&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=43707425_190284299_2_1_0&highlighted_blocks=43707425_190284299_2_1_0&matching_block_id=43707425_190284299_2_1_0&sr_pri_blocks=43707425_190284299_2_1_0__4400&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 62,
      "name": "Hostal Yumbo Imperial",
      "price": "23",
      "score": "8.4",
      "link": "https://www.booking.com/hotel/ec/yumbo-imperial.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=12&hapos=12&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=108711204_184422779_0_2_0&highlighted_blocks=108711204_184422779_0_2_0&matching_block_id=108711204_184422779_0_2_0&sr_pri_blocks=108711204_184422779_0_2_0__2340&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 63,
      "name": "Hostal L'Auberge Inn",
      "price": "48",
      "score": "8.7",
      "link": "https://www.booking.com/hotel/ec/hostal-auberge-inn.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=13&hapos=13&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=40177910_213957222_0_2_0&highlighted_blocks=40177910_213957222_0_2_0&matching_block_id=40177910_213957222_0_2_0&sr_pri_blocks=40177910_213957222_0_2_0__4760&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 64,
      "name": "Hotel Reina Isabel",
      "price": "156",
      "score": "8.9",
      "link": "https://www.booking.com/hotel/ec/reina-isabel.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=14&hapos=14&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=34454701_221196700_0_41_0&highlighted_blocks=34454701_221196700_0_41_0&matching_block_id=34454701_221196700_0_41_0&sr_pri_blocks=34454701_221196700_0_41_0__15600&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 65,
      "name": "La Rosario Hostal",
      "price": "27",
      "score": "0",
      "link": "https://www.booking.com/hotel/ec/la-rosario-hostal.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=15&hapos=15&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=955610301_368056857_2_0_0&highlighted_blocks=955610301_368056857_2_0_0&matching_block_id=955610301_368056857_2_0_0&sr_pri_blocks=955610301_368056857_2_0_0__2720&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 66,
      "name": "Hotel Finlandia",
      "price": "300",
      "score": "8.8",
      "link": "https://www.booking.com/hotel/ec/finlandia-quito.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=16&hapos=16&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=32258504_347833927_2_41_0&highlighted_blocks=32258504_347833927_2_41_0&matching_block_id=32258504_347833927_2_41_0&sr_pri_blocks=32258504_347833927_2_41_0__30000&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 67,
      "name": "Hotel Casona 1914",
      "price": "353",
      "score": "9.7",
      "link": "https://www.booking.com/hotel/ec/boutique-casona-d-39-alameda.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=17&hapos=17&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=442331418_330973113_2_1_0&highlighted_blocks=442331418_330973113_2_1_0&matching_block_id=442331418_330973113_2_1_0&sr_pri_blocks=442331418_330973113_2_1_0__35343&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 68,
      "name": "Hostal Juana de Arco",
      "price": "40",
      "score": "8.3",
      "link": "https://www.booking.com/hotel/ec/juana-de-arco.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=18&hapos=18&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=131472904_344326747_2_1_0&highlighted_blocks=131472904_344326747_2_1_0&matching_block_id=131472904_344326747_2_1_0&sr_pri_blocks=131472904_344326747_2_1_0__3990&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 69,
      "name": "Bonito Departamento Sur de Quito",
      "price": "60",
      "score": "0",
      "link": "https://www.booking.com/hotel/ec/bonito-departamento-sur-de-quito.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=19&hapos=19&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=955226601_368014456_2_0_0&highlighted_blocks=955226601_368014456_2_0_0&matching_block_id=955226601_368014456_2_0_0&sr_pri_blocks=955226601_368014456_2_0_0__5950&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 70,
      "name": "ibis Quito",
      "price": "160",
      "score": "8.8",
      "link": "https://www.booking.com/hotel/ec/ibis-quito.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=20&hapos=20&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=432406501_246094429_2_41_0&highlighted_blocks=432406501_246094429_2_41_0&matching_block_id=432406501_246094429_2_41_0&sr_pri_blocks=432406501_246094429_2_41_0__16000&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 71,
      "name": "ArtPlaza",
      "price": "73",
      "score": "8.8",
      "link": "https://www.booking.com/hotel/ec/artplaza.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=21&hapos=21&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=116994001_295810281_0_2_0&highlighted_blocks=116994001_295810281_0_2_0&matching_block_id=116994001_295810281_0_2_0&sr_pri_blocks=116994001_295810281_0_2_0__7344&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 72,
      "name": "ITSAHOME Apartments Torre Seis",
      "price": "116",
      "score": "8.7",
      "link": "https://www.booking.com/hotel/ec/itsahome-apartments.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=22&hapos=22&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=110945713_208105836_2_0_0&highlighted_blocks=110945713_208105836_2_0_0&matching_block_id=110945713_208105836_2_0_0&sr_pri_blocks=110945713_208105836_2_0_0__11600&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 73,
      "name": "Vista del Angel Hotel Boutique",
      "price": "255",
      "score": "9.3",
      "link": "https://www.booking.com/hotel/ec/vista-del-angel-boutique.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=23&hapos=23&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=258612207_339828813_2_33_0&highlighted_blocks=258612207_339828813_2_33_0&matching_block_id=258612207_339828813_2_33_0&sr_pri_blocks=258612207_339828813_2_33_0__25520&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 74,
      "name": "Hotel Huasi Continental",
      "price": "74",
      "score": "8.2",
      "link": "https://www.booking.com/hotel/ec/huasi-continental.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=24&hapos=24&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=33130705_265683207_0_1_0&highlighted_blocks=33130705_265683207_0_1_0&matching_block_id=33130705_265683207_0_1_0&sr_pri_blocks=33130705_265683207_0_1_0__7402&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 75,
      "name": "Dann Carlton Quito",
      "price": "300",
      "score": "8.7",
      "link": "https://www.booking.com/hotel/ec/dann-carlton-quito.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-932573&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=25&hapos=25&sr_order=popularity&srpvid=3c92023f13850163&srepoch=1675124353&all_sr_blocks=30094701_143539561_0_1_0&highlighted_blocks=30094701_143539561_0_1_0&matching_block_id=30094701_143539561_0_1_0&sr_pri_blocks=30094701_143539561_0_1_0__30000&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Quito"
        }
    )
    batch.put_item(
    Item={
      "id": 1,
      "name": "Hotel Air Suites",
      "price": "77",
      "score": "7.5",
      "link": "https://www.booking.com/hotel/ec/air-suites.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=1&hapos=1&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=34877002_89165989_0_41_0&highlighted_blocks=34877002_89165989_0_41_0&matching_block_id=34877002_89165989_0_41_0&sr_pri_blocks=34877002_89165989_0_41_0__7650&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 2,
      "name": "Hotel Perla Central",
      "price": "57",
      "score": "7.9",
      "link": "https://www.booking.com/hotel/ec/nazu-city-hostel.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=2&hapos=2&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=143441603_195349573_0_2_0&highlighted_blocks=143441603_195349573_0_2_0&matching_block_id=143441603_195349573_0_2_0&sr_pri_blocks=143441603_195349573_0_2_0__5670&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 3,
      "name": "Luxva Hotel Boutique",
      "price": "190",
      "score": "8.8",
      "link": "https://www.booking.com/hotel/ec/luxva-boutique.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=3&hapos=3&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=565899903_252878211_2_1_0&highlighted_blocks=565899903_252878211_2_1_0&matching_block_id=565899903_252878211_2_1_0&sr_pri_blocks=565899903_252878211_2_1_0__19000&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 4,
      "name": "Hotel Palace Guayaquil",
      "price": "151",
      "score": "8.9",
      "link": "https://www.booking.com/hotel/ec/palace.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=4&hapos=4&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=25959002_89153636_0_1_0&highlighted_blocks=25959002_89153636_0_1_0&matching_block_id=25959002_89153636_0_1_0&sr_pri_blocks=25959002_89153636_0_1_0__15120&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 5,
      "name": "River Garden Hotel + Suites",
      "price": "207",
      "score": "8.8",
      "link": "https://www.booking.com/hotel/ec/river-garden-suites.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=5&hapos=5&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=634717802_341895313_2_2_0&highlighted_blocks=634717802_341895313_2_2_0&matching_block_id=634717802_341895313_2_2_0&sr_pri_blocks=634717802_341895313_2_2_0__20710&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 6,
      "name": "TRYP by Wyndham Guayaquil",
      "price": "170",
      "score": "8.5",
      "link": "https://www.booking.com/hotel/ec/sonesta-guayaquil.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=6&hapos=6&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=32289809_240942523_3_2_0&highlighted_blocks=32289809_240942523_3_2_0&matching_block_id=32289809_240942523_3_2_0&sr_pri_blocks=32289809_240942523_3_2_0__17000&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 7,
      "name": "Wyndham Garden Guayaquil",
      "price": "193",
      "score": "8.5",
      "link": "https://www.booking.com/hotel/ec/wyndham-garden-guayaquil.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=7&hapos=7&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=26949614_361969860_2_42_0&highlighted_blocks=26949614_361969860_2_42_0&matching_block_id=26949614_361969860_2_42_0&sr_pri_blocks=26949614_361969860_2_42_0__19300&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 8,
      "name": "Unipark by Oro Verde Hotels",
      "price": "174",
      "score": "8.8",
      "link": "https://www.booking.com/hotel/ec/unipark.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=8&hapos=8&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=26996515_209437577_2_1_0&highlighted_blocks=26996515_209437577_2_1_0&matching_block_id=26996515_209437577_2_1_0&sr_pri_blocks=26996515_209437577_2_1_0__17400&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 9,
      "name": "Holiday Inn Guayaquil Airport; an IHG Hotel",
      "price": "270",
      "score": "8.8",
      "link": "https://www.booking.com/hotel/ec/holiday-inn-guayaquil-bolivar-airport.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=9&hapos=9&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=49640918_244367562_2_0_0&highlighted_blocks=49640918_244367562_2_0_0&matching_block_id=49640918_244367562_2_0_0&sr_pri_blocks=49640918_244367562_2_0_0__27000&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 10,
      "name": "YU! Smarthotels",
      "price": "57",
      "score": "8.5",
      "link": "https://www.booking.com/hotel/ec/yu-smarthotels.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=10&hapos=10&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=182386107_344014534_2_0_0&highlighted_blocks=182386107_344014534_2_0_0&matching_block_id=182386107_344014534_2_0_0&sr_pri_blocks=182386107_344014534_2_0_0__5742&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 11,
      "name": "Wyndham Guayaquil; Puerto Santa Ana",
      "price": "288",
      "score": "8.9",
      "link": "https://www.booking.com/hotel/ec/wyndham-guayaquil.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=11&hapos=11&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=57011111_285737300_2_2_0&highlighted_blocks=57011111_285737300_2_2_0&matching_block_id=57011111_285737300_2_2_0&sr_pri_blocks=57011111_285737300_2_2_0__28800&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 12,
      "name": "Hotel de Alborada",
      "price": "64",
      "score": "8.4",
      "link": "https://www.booking.com/hotel/ec/de-alborada.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=12&hapos=12&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=34616101_360914228_0_1_0&highlighted_blocks=34616101_360914228_0_1_0&matching_block_id=34616101_360914228_0_1_0&sr_pri_blocks=34616101_360914228_0_1_0__6370&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 13,
      "name": "The Park Hotel",
      "price": "117",
      "score": "7.9",
      "link": "https://www.booking.com/hotel/ec/the-park-ec.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=13&hapos=13&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=140288811_359820490_2_1_0&highlighted_blocks=140288811_359820490_2_1_0&matching_block_id=140288811_359820490_2_1_0&sr_pri_blocks=140288811_359820490_2_1_0__11680&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 14,
      "name": "Sheraton Guayaquil",
      "price": "245",
      "score": "8.7",
      "link": "https://www.booking.com/hotel/ec/sheraton-guayaquil.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=14&hapos=14&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=26467906_274564200_0_2_0&highlighted_blocks=26467906_274564200_0_2_0&matching_block_id=26467906_274564200_0_2_0&sr_pri_blocks=26467906_274564200_0_2_0__24500&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 15,
      "name": "DC Suites Aeropuerto",
      "price": "84",
      "score": "8.1",
      "link": "https://www.booking.com/hotel/ec/dc.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=15&hapos=15&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=104362714_211324078_2_2_0&highlighted_blocks=104362714_211324078_2_2_0&matching_block_id=104362714_211324078_2_2_0&sr_pri_blocks=104362714_211324078_2_2_0__8400&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 16,
      "name": "Airport Hotel",
      "price": "100",
      "score": "7.8",
      "link": "https://www.booking.com/hotel/ec/airport.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=16&hapos=16&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=133437105_199993723_2_1_0&highlighted_blocks=133437105_199993723_2_1_0&matching_block_id=133437105_199993723_2_1_0&sr_pri_blocks=133437105_199993723_2_1_0__10000&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 17,
      "name": "Hotel Puerto Pacifico Guayaquil Airport",
      "price": "153",
      "score": "8.4",
      "link": "https://www.booking.com/hotel/ec/puerto-pacifico-guayaquil.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=17&hapos=17&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=687825001_279467545_2_10_0&highlighted_blocks=687825001_279467545_2_10_0&matching_block_id=687825001_279467545_2_10_0&sr_pri_blocks=687825001_279467545_2_10_0__15344&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 18,
      "name": "Hilton Colon Guayaquil Hotel",
      "price": "300",
      "score": "8.6",
      "link": "https://www.booking.com/hotel/ec/hilton-colon-guayaquil.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=18&hapos=18&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=26279402_266275887_2_2_0&highlighted_blocks=26279402_266275887_2_2_0&matching_block_id=26279402_266275887_2_2_0&sr_pri_blocks=26279402_266275887_2_2_0__30000&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 19,
      "name": "Pepe's House Guayaquil I Self Check-In MicroHotel",
      "price": "79",
      "score": "8.4",
      "link": "https://www.booking.com/hotel/ec/pepes-house-guayaquil.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=19&hapos=19&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=631704506_246525947_2_1_0&highlighted_blocks=631704506_246525947_2_1_0&matching_block_id=631704506_246525947_2_1_0&sr_pri_blocks=631704506_246525947_2_1_0__7874&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 20,
      "name": "Hotel Ramada",
      "price": "136",
      "score": "7.9",
      "link": "https://www.booking.com/hotel/ec/ramada.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=20&hapos=20&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=27525910_265519618_0_1_0&highlighted_blocks=27525910_265519618_0_1_0&matching_block_id=27525910_265519618_0_1_0&sr_pri_blocks=27525910_265519618_0_1_0__13600&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 21,
      "name": "Hotel Patrimonial by Greenfield",
      "price": "97",
      "score": "8.4",
      "link": "https://www.booking.com/hotel/ec/greenfield-39-s-patrimonial.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=21&hapos=21&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=254800606_362808784_2_1_0&highlighted_blocks=254800606_362808784_2_1_0&matching_block_id=254800606_362808784_2_1_0&sr_pri_blocks=254800606_362808784_2_1_0__9660&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 22,
      "name": "Hotel Marcelius",
      "price": "140",
      "score": "8.3",
      "link": "https://www.booking.com/hotel/ec/marcelius.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=22&hapos=22&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=35828910_112718195_0_41_0&highlighted_blocks=35828910_112718195_0_41_0&matching_block_id=35828910_112718195_0_41_0&sr_pri_blocks=35828910_112718195_0_41_0__14000&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 23,
      "name": "New apartment in Los Ceibos-Guayaquil",
      "price": "122",
      "score": "0",
      "link": "https://www.booking.com/hotel/ec/new-apartment-in-los-ceibos-guayaquil.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=23&hapos=23&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=954911801_367992439_2_0_0&highlighted_blocks=954911801_367992439_2_0_0&matching_block_id=954911801_367992439_2_0_0&sr_pri_blocks=954911801_367992439_2_0_0__12240&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 24,
      "name": "Hotel Boutique Mansion Del Rio",
      "price": "141",
      "score": "8.6",
      "link": "https://www.booking.com/hotel/ec/boutique-mansion-del-rio.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=24&hapos=24&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=34460201_89165403_2_33_0&highlighted_blocks=34460201_89165403_2_33_0&matching_block_id=34460201_89165403_2_33_0&sr_pri_blocks=34460201_89165403_2_33_0__14080&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 25,
      "name": "Manso Boutique Guest House",
      "price": "65",
      "score": "8",
      "link": "https://www.booking.com/hotel/ec/manso-boutique-hostal.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=25&hapos=25&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=27101208_89155227_2_9_0&highlighted_blocks=27101208_89155227_2_9_0&matching_block_id=27101208_89155227_2_9_0&sr_pri_blocks=27101208_89155227_2_9_0__6452&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 26,
      "name": "Hotel Air Suites",
      "price": "77",
      "score": "7.5",
      "link": "https://www.booking.com/hotel/ec/air-suites.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=1&hapos=1&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=34877002_89165989_0_41_0&highlighted_blocks=34877002_89165989_0_41_0&matching_block_id=34877002_89165989_0_41_0&sr_pri_blocks=34877002_89165989_0_41_0__7650&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 27,
      "name": "Hotel Perla Central",
      "price": "57",
      "score": "7.9",
      "link": "https://www.booking.com/hotel/ec/nazu-city-hostel.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=2&hapos=2&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=143441603_195349573_0_2_0&highlighted_blocks=143441603_195349573_0_2_0&matching_block_id=143441603_195349573_0_2_0&sr_pri_blocks=143441603_195349573_0_2_0__5670&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 28,
      "name": "Luxva Hotel Boutique",
      "price": "190",
      "score": "8.8",
      "link": "https://www.booking.com/hotel/ec/luxva-boutique.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=3&hapos=3&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=565899903_252878211_2_1_0&highlighted_blocks=565899903_252878211_2_1_0&matching_block_id=565899903_252878211_2_1_0&sr_pri_blocks=565899903_252878211_2_1_0__19000&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 29,
      "name": "Hotel Palace Guayaquil",
      "price": "151",
      "score": "8.9",
      "link": "https://www.booking.com/hotel/ec/palace.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=4&hapos=4&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=25959002_89153636_0_1_0&highlighted_blocks=25959002_89153636_0_1_0&matching_block_id=25959002_89153636_0_1_0&sr_pri_blocks=25959002_89153636_0_1_0__15120&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 30,
      "name": "River Garden Hotel + Suites",
      "price": "207",
      "score": "8.8",
      "link": "https://www.booking.com/hotel/ec/river-garden-suites.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=5&hapos=5&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=634717802_341895313_2_2_0&highlighted_blocks=634717802_341895313_2_2_0&matching_block_id=634717802_341895313_2_2_0&sr_pri_blocks=634717802_341895313_2_2_0__20710&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 31,
      "name": "TRYP by Wyndham Guayaquil",
      "price": "170",
      "score": "8.5",
      "link": "https://www.booking.com/hotel/ec/sonesta-guayaquil.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=6&hapos=6&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=32289809_240942523_3_2_0&highlighted_blocks=32289809_240942523_3_2_0&matching_block_id=32289809_240942523_3_2_0&sr_pri_blocks=32289809_240942523_3_2_0__17000&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 32,
      "name": "Wyndham Garden Guayaquil",
      "price": "193",
      "score": "8.5",
      "link": "https://www.booking.com/hotel/ec/wyndham-garden-guayaquil.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=7&hapos=7&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=26949614_361969860_2_42_0&highlighted_blocks=26949614_361969860_2_42_0&matching_block_id=26949614_361969860_2_42_0&sr_pri_blocks=26949614_361969860_2_42_0__19300&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 33,
      "name": "Unipark by Oro Verde Hotels",
      "price": "174",
      "score": "8.8",
      "link": "https://www.booking.com/hotel/ec/unipark.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=8&hapos=8&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=26996515_209437577_2_1_0&highlighted_blocks=26996515_209437577_2_1_0&matching_block_id=26996515_209437577_2_1_0&sr_pri_blocks=26996515_209437577_2_1_0__17400&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 34,
      "name": "Holiday Inn Guayaquil Airport; an IHG Hotel",
      "price": "270",
      "score": "8.8",
      "link": "https://www.booking.com/hotel/ec/holiday-inn-guayaquil-bolivar-airport.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=9&hapos=9&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=49640918_244367562_2_0_0&highlighted_blocks=49640918_244367562_2_0_0&matching_block_id=49640918_244367562_2_0_0&sr_pri_blocks=49640918_244367562_2_0_0__27000&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 35,
      "name": "YU! Smarthotels",
      "price": "57",
      "score": "8.5",
      "link": "https://www.booking.com/hotel/ec/yu-smarthotels.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=10&hapos=10&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=182386107_344014534_2_0_0&highlighted_blocks=182386107_344014534_2_0_0&matching_block_id=182386107_344014534_2_0_0&sr_pri_blocks=182386107_344014534_2_0_0__5742&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 36,
      "name": "Wyndham Guayaquil; Puerto Santa Ana",
      "price": "288",
      "score": "8.9",
      "link": "https://www.booking.com/hotel/ec/wyndham-guayaquil.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=11&hapos=11&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=57011111_285737300_2_2_0&highlighted_blocks=57011111_285737300_2_2_0&matching_block_id=57011111_285737300_2_2_0&sr_pri_blocks=57011111_285737300_2_2_0__28800&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 37,
      "name": "Hotel de Alborada",
      "price": "64",
      "score": "8.4",
      "link": "https://www.booking.com/hotel/ec/de-alborada.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=12&hapos=12&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=34616101_360914228_0_1_0&highlighted_blocks=34616101_360914228_0_1_0&matching_block_id=34616101_360914228_0_1_0&sr_pri_blocks=34616101_360914228_0_1_0__6370&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 38,
      "name": "The Park Hotel",
      "price": "117",
      "score": "7.9",
      "link": "https://www.booking.com/hotel/ec/the-park-ec.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=13&hapos=13&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=140288811_359820490_2_1_0&highlighted_blocks=140288811_359820490_2_1_0&matching_block_id=140288811_359820490_2_1_0&sr_pri_blocks=140288811_359820490_2_1_0__11680&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 39,
      "name": "Sheraton Guayaquil",
      "price": "245",
      "score": "8.7",
      "link": "https://www.booking.com/hotel/ec/sheraton-guayaquil.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=14&hapos=14&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=26467906_274564200_0_2_0&highlighted_blocks=26467906_274564200_0_2_0&matching_block_id=26467906_274564200_0_2_0&sr_pri_blocks=26467906_274564200_0_2_0__24500&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 40,
      "name": "DC Suites Aeropuerto",
      "price": "84",
      "score": "8.1",
      "link": "https://www.booking.com/hotel/ec/dc.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=15&hapos=15&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=104362714_211324078_2_2_0&highlighted_blocks=104362714_211324078_2_2_0&matching_block_id=104362714_211324078_2_2_0&sr_pri_blocks=104362714_211324078_2_2_0__8400&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 41,
      "name": "Airport Hotel",
      "price": "100",
      "score": "7.8",
      "link": "https://www.booking.com/hotel/ec/airport.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=16&hapos=16&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=133437105_199993723_2_1_0&highlighted_blocks=133437105_199993723_2_1_0&matching_block_id=133437105_199993723_2_1_0&sr_pri_blocks=133437105_199993723_2_1_0__10000&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 42,
      "name": "Hotel Puerto Pacifico Guayaquil Airport",
      "price": "153",
      "score": "8.4",
      "link": "https://www.booking.com/hotel/ec/puerto-pacifico-guayaquil.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=17&hapos=17&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=687825001_279467545_2_10_0&highlighted_blocks=687825001_279467545_2_10_0&matching_block_id=687825001_279467545_2_10_0&sr_pri_blocks=687825001_279467545_2_10_0__15344&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 43,
      "name": "Hilton Colon Guayaquil Hotel",
      "price": "300",
      "score": "8.6",
      "link": "https://www.booking.com/hotel/ec/hilton-colon-guayaquil.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=18&hapos=18&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=26279402_266275887_2_2_0&highlighted_blocks=26279402_266275887_2_2_0&matching_block_id=26279402_266275887_2_2_0&sr_pri_blocks=26279402_266275887_2_2_0__30000&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 44,
      "name": "Pepe's House Guayaquil I Self Check-In MicroHotel",
      "price": "79",
      "score": "8.4",
      "link": "https://www.booking.com/hotel/ec/pepes-house-guayaquil.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=19&hapos=19&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=631704506_246525947_2_1_0&highlighted_blocks=631704506_246525947_2_1_0&matching_block_id=631704506_246525947_2_1_0&sr_pri_blocks=631704506_246525947_2_1_0__7874&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 45,
      "name": "Hotel Ramada",
      "price": "136",
      "score": "7.9",
      "link": "https://www.booking.com/hotel/ec/ramada.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=20&hapos=20&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=27525910_265519618_0_1_0&highlighted_blocks=27525910_265519618_0_1_0&matching_block_id=27525910_265519618_0_1_0&sr_pri_blocks=27525910_265519618_0_1_0__13600&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 46,
      "name": "Hotel Patrimonial by Greenfield",
      "price": "97",
      "score": "8.4",
      "link": "https://www.booking.com/hotel/ec/greenfield-39-s-patrimonial.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=21&hapos=21&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=254800606_362808784_2_1_0&highlighted_blocks=254800606_362808784_2_1_0&matching_block_id=254800606_362808784_2_1_0&sr_pri_blocks=254800606_362808784_2_1_0__9660&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 47,
      "name": "Hotel Marcelius",
      "price": "140",
      "score": "8.3",
      "link": "https://www.booking.com/hotel/ec/marcelius.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=22&hapos=22&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=35828910_112718195_0_41_0&highlighted_blocks=35828910_112718195_0_41_0&matching_block_id=35828910_112718195_0_41_0&sr_pri_blocks=35828910_112718195_0_41_0__14000&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 48,
      "name": "New apartment in Los Ceibos-Guayaquil",
      "price": "122",
      "score": "0",
      "link": "https://www.booking.com/hotel/ec/new-apartment-in-los-ceibos-guayaquil.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=23&hapos=23&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=954911801_367992439_2_0_0&highlighted_blocks=954911801_367992439_2_0_0&matching_block_id=954911801_367992439_2_0_0&sr_pri_blocks=954911801_367992439_2_0_0__12240&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 49,
      "name": "Hotel Boutique Mansion Del Rio",
      "price": "141",
      "score": "8.6",
      "link": "https://www.booking.com/hotel/ec/boutique-mansion-del-rio.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=24&hapos=24&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=34460201_89165403_2_33_0&highlighted_blocks=34460201_89165403_2_33_0&matching_block_id=34460201_89165403_2_33_0&sr_pri_blocks=34460201_89165403_2_33_0__14080&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 50,
      "name": "Manso Boutique Guest House",
      "price": "65",
      "score": "8",
      "link": "https://www.booking.com/hotel/ec/manso-boutique-hostal.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=25&hapos=25&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=27101208_89155227_2_9_0&highlighted_blocks=27101208_89155227_2_9_0&matching_block_id=27101208_89155227_2_9_0&sr_pri_blocks=27101208_89155227_2_9_0__6452&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 51,
      "name": "Hotel Air Suites",
      "price": "77",
      "score": "7.5",
      "link": "https://www.booking.com/hotel/ec/air-suites.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=1&hapos=1&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=34877002_89165989_0_41_0&highlighted_blocks=34877002_89165989_0_41_0&matching_block_id=34877002_89165989_0_41_0&sr_pri_blocks=34877002_89165989_0_41_0__7650&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 52,
      "name": "Hotel Perla Central",
      "price": "57",
      "score": "7.9",
      "link": "https://www.booking.com/hotel/ec/nazu-city-hostel.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=2&hapos=2&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=143441603_195349573_0_2_0&highlighted_blocks=143441603_195349573_0_2_0&matching_block_id=143441603_195349573_0_2_0&sr_pri_blocks=143441603_195349573_0_2_0__5670&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 53,
      "name": "Luxva Hotel Boutique",
      "price": "190",
      "score": "8.8",
      "link": "https://www.booking.com/hotel/ec/luxva-boutique.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=3&hapos=3&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=565899903_252878211_2_1_0&highlighted_blocks=565899903_252878211_2_1_0&matching_block_id=565899903_252878211_2_1_0&sr_pri_blocks=565899903_252878211_2_1_0__19000&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 54,
      "name": "Hotel Palace Guayaquil",
      "price": "151",
      "score": "8.9",
      "link": "https://www.booking.com/hotel/ec/palace.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=4&hapos=4&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=25959002_89153636_0_1_0&highlighted_blocks=25959002_89153636_0_1_0&matching_block_id=25959002_89153636_0_1_0&sr_pri_blocks=25959002_89153636_0_1_0__15120&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 55,
      "name": "River Garden Hotel + Suites",
      "price": "207",
      "score": "8.8",
      "link": "https://www.booking.com/hotel/ec/river-garden-suites.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=5&hapos=5&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=634717802_341895313_2_2_0&highlighted_blocks=634717802_341895313_2_2_0&matching_block_id=634717802_341895313_2_2_0&sr_pri_blocks=634717802_341895313_2_2_0__20710&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 56,
      "name": "TRYP by Wyndham Guayaquil",
      "price": "170",
      "score": "8.5",
      "link": "https://www.booking.com/hotel/ec/sonesta-guayaquil.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=6&hapos=6&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=32289809_240942523_3_2_0&highlighted_blocks=32289809_240942523_3_2_0&matching_block_id=32289809_240942523_3_2_0&sr_pri_blocks=32289809_240942523_3_2_0__17000&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 57,
      "name": "Wyndham Garden Guayaquil",
      "price": "193",
      "score": "8.5",
      "link": "https://www.booking.com/hotel/ec/wyndham-garden-guayaquil.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=7&hapos=7&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=26949614_361969860_2_42_0&highlighted_blocks=26949614_361969860_2_42_0&matching_block_id=26949614_361969860_2_42_0&sr_pri_blocks=26949614_361969860_2_42_0__19300&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 58,
      "name": "Unipark by Oro Verde Hotels",
      "price": "174",
      "score": "8.8",
      "link": "https://www.booking.com/hotel/ec/unipark.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=8&hapos=8&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=26996515_209437577_2_1_0&highlighted_blocks=26996515_209437577_2_1_0&matching_block_id=26996515_209437577_2_1_0&sr_pri_blocks=26996515_209437577_2_1_0__17400&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 59,
      "name": "Holiday Inn Guayaquil Airport; an IHG Hotel",
      "price": "270",
      "score": "8.8",
      "link": "https://www.booking.com/hotel/ec/holiday-inn-guayaquil-bolivar-airport.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=9&hapos=9&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=49640918_244367562_2_0_0&highlighted_blocks=49640918_244367562_2_0_0&matching_block_id=49640918_244367562_2_0_0&sr_pri_blocks=49640918_244367562_2_0_0__27000&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 60,
      "name": "YU! Smarthotels",
      "price": "57",
      "score": "8.5",
      "link": "https://www.booking.com/hotel/ec/yu-smarthotels.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=10&hapos=10&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=182386107_344014534_2_0_0&highlighted_blocks=182386107_344014534_2_0_0&matching_block_id=182386107_344014534_2_0_0&sr_pri_blocks=182386107_344014534_2_0_0__5742&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 61,
      "name": "Wyndham Guayaquil; Puerto Santa Ana",
      "price": "288",
      "score": "8.9",
      "link": "https://www.booking.com/hotel/ec/wyndham-guayaquil.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=11&hapos=11&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=57011111_285737300_2_2_0&highlighted_blocks=57011111_285737300_2_2_0&matching_block_id=57011111_285737300_2_2_0&sr_pri_blocks=57011111_285737300_2_2_0__28800&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 62,
      "name": "Hotel de Alborada",
      "price": "64",
      "score": "8.4",
      "link": "https://www.booking.com/hotel/ec/de-alborada.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=12&hapos=12&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=34616101_360914228_0_1_0&highlighted_blocks=34616101_360914228_0_1_0&matching_block_id=34616101_360914228_0_1_0&sr_pri_blocks=34616101_360914228_0_1_0__6370&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 63,
      "name": "The Park Hotel",
      "price": "117",
      "score": "7.9",
      "link": "https://www.booking.com/hotel/ec/the-park-ec.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=13&hapos=13&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=140288811_359820490_2_1_0&highlighted_blocks=140288811_359820490_2_1_0&matching_block_id=140288811_359820490_2_1_0&sr_pri_blocks=140288811_359820490_2_1_0__11680&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 64,
      "name": "Sheraton Guayaquil",
      "price": "245",
      "score": "8.7",
      "link": "https://www.booking.com/hotel/ec/sheraton-guayaquil.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=14&hapos=14&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=26467906_274564200_0_2_0&highlighted_blocks=26467906_274564200_0_2_0&matching_block_id=26467906_274564200_0_2_0&sr_pri_blocks=26467906_274564200_0_2_0__24500&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 65,
      "name": "DC Suites Aeropuerto",
      "price": "84",
      "score": "8.1",
      "link": "https://www.booking.com/hotel/ec/dc.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=15&hapos=15&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=104362714_211324078_2_2_0&highlighted_blocks=104362714_211324078_2_2_0&matching_block_id=104362714_211324078_2_2_0&sr_pri_blocks=104362714_211324078_2_2_0__8400&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 66,
      "name": "Airport Hotel",
      "price": "100",
      "score": "7.8",
      "link": "https://www.booking.com/hotel/ec/airport.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=16&hapos=16&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=133437105_199993723_2_1_0&highlighted_blocks=133437105_199993723_2_1_0&matching_block_id=133437105_199993723_2_1_0&sr_pri_blocks=133437105_199993723_2_1_0__10000&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 67,
      "name": "Hotel Puerto Pacifico Guayaquil Airport",
      "price": "153",
      "score": "8.4",
      "link": "https://www.booking.com/hotel/ec/puerto-pacifico-guayaquil.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=17&hapos=17&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=687825001_279467545_2_10_0&highlighted_blocks=687825001_279467545_2_10_0&matching_block_id=687825001_279467545_2_10_0&sr_pri_blocks=687825001_279467545_2_10_0__15344&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 68,
      "name": "Hilton Colon Guayaquil Hotel",
      "price": "300",
      "score": "8.6",
      "link": "https://www.booking.com/hotel/ec/hilton-colon-guayaquil.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=18&hapos=18&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=26279402_266275887_2_2_0&highlighted_blocks=26279402_266275887_2_2_0&matching_block_id=26279402_266275887_2_2_0&sr_pri_blocks=26279402_266275887_2_2_0__30000&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 69,
      "name": "Pepe's House Guayaquil I Self Check-In MicroHotel",
      "price": "79",
      "score": "8.4",
      "link": "https://www.booking.com/hotel/ec/pepes-house-guayaquil.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=19&hapos=19&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=631704506_246525947_2_1_0&highlighted_blocks=631704506_246525947_2_1_0&matching_block_id=631704506_246525947_2_1_0&sr_pri_blocks=631704506_246525947_2_1_0__7874&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 70,
      "name": "Hotel Ramada",
      "price": "136",
      "score": "7.9",
      "link": "https://www.booking.com/hotel/ec/ramada.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=20&hapos=20&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=27525910_265519618_0_1_0&highlighted_blocks=27525910_265519618_0_1_0&matching_block_id=27525910_265519618_0_1_0&sr_pri_blocks=27525910_265519618_0_1_0__13600&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 71,
      "name": "Hotel Patrimonial by Greenfield",
      "price": "97",
      "score": "8.4",
      "link": "https://www.booking.com/hotel/ec/greenfield-39-s-patrimonial.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=21&hapos=21&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=254800606_362808784_2_1_0&highlighted_blocks=254800606_362808784_2_1_0&matching_block_id=254800606_362808784_2_1_0&sr_pri_blocks=254800606_362808784_2_1_0__9660&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 72,
      "name": "Hotel Marcelius",
      "price": "140",
      "score": "8.3",
      "link": "https://www.booking.com/hotel/ec/marcelius.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=22&hapos=22&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=35828910_112718195_0_41_0&highlighted_blocks=35828910_112718195_0_41_0&matching_block_id=35828910_112718195_0_41_0&sr_pri_blocks=35828910_112718195_0_41_0__14000&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 73,
      "name": "New apartment in Los Ceibos-Guayaquil",
      "price": "122",
      "score": "0",
      "link": "https://www.booking.com/hotel/ec/new-apartment-in-los-ceibos-guayaquil.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=23&hapos=23&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=954911801_367992439_2_0_0&highlighted_blocks=954911801_367992439_2_0_0&matching_block_id=954911801_367992439_2_0_0&sr_pri_blocks=954911801_367992439_2_0_0__12240&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 74,
      "name": "Hotel Boutique Mansion Del Rio",
      "price": "141",
      "score": "8.6",
      "link": "https://www.booking.com/hotel/ec/boutique-mansion-del-rio.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=24&hapos=24&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=34460201_89165403_2_33_0&highlighted_blocks=34460201_89165403_2_33_0&matching_block_id=34460201_89165403_2_33_0&sr_pri_blocks=34460201_89165403_2_33_0__14080&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )
    batch.put_item(
    Item={
      "id": 75,
      "name": "Manso Boutique Guest House",
      "price": "65",
      "score": "8",
      "link": "https://www.booking.com/hotel/ec/manso-boutique-hostal.en-gb.html?label=duc511jc-1FCAIoQUICZWNIM1gDaEGIAQGYAQm4AQfIAQzYAQHoAQH4AQ2IAgGoAgO4AqWU7Z0GwAIB0gIkOTNkY2I5NmYtMjRkZS00OGIzLWJkMDYtN2FjMzBhNGE1NDVh2AIG4AIB&sid=d937cab748728b6d0dd262df88420fff&aid=304142&ucfs=1&arphpl=1&checkin=2023-02-01&checkout=2023-02-03&dest_id=-927505&dest_type=city&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=25&hapos=25&sr_order=popularity&srpvid=560c02c2c2820065&srepoch=1675124614&all_sr_blocks=27101208_89155227_2_9_0&highlighted_blocks=27101208_89155227_2_9_0&matching_block_id=27101208_89155227_2_9_0&sr_pri_blocks=27101208_89155227_2_9_0__6452&from_sustainable_property_sr=1&from=searchresults#hotelTmpl",
      "province": "Guayaquil"
        }
    )

print(hotels.get_item(
    Key = {
        "id": 75,
        "name": "Manso Boutique Guest House",
    }
)['Item'], flush = True )

"""
Inserting records in categories
"""

with categories.batch_writer() as batch:
  batch.put_item(
  Item={
    "id": 1,
    "province": " Esmeraldas",
    "category": "Staff",
    "score_category": "9.1",
    "hotel": "La Facha Hostal Restaurant Surf",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 2,
    "province": " Esmeraldas",
    "category": "Facilities",
    "score_category": "8.4",
    "hotel": "La Facha Hostal Restaurant Surf",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 3,
    "province": " Esmeraldas",
    "category": "Cleanliness",
    "score_category": "8.5",
    "hotel": "La Facha Hostal Restaurant Surf",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 4,
    "province": " Esmeraldas",
    "category": "Comfort",
    "score_category": "8.5",
    "hotel": "La Facha Hostal Restaurant Surf",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 5,
    "province": " Esmeraldas",
    "category": "Value for money",
    "score_category": "8.6",
    "hotel": "La Facha Hostal Restaurant Surf",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 6,
    "province": " Esmeraldas",
    "category": "Location",
    "score_category": "9.1",
    "hotel": "La Facha Hostal Restaurant Surf",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 7,
    "province": " Esmeraldas",
    "category": "Free WiFi",
    "score_category": "7.5",
    "hotel": "La Facha Hostal Restaurant Surf",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 8,
    "province": " Esmeraldas",
    "category": "Staff",
    "score_category": "9.4",
    "hotel": "Hotel Casa Arnaldo Esmeraldas",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 9,
    "province": " Esmeraldas",
    "category": "Facilities",
    "score_category": "8.9",
    "hotel": "Hotel Casa Arnaldo Esmeraldas",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 10,
    "province": " Esmeraldas",
    "category": "Cleanliness",
    "score_category": "9.2",
    "hotel": "Hotel Casa Arnaldo Esmeraldas",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 11,
    "province": " Esmeraldas",
    "category": "Comfort",
    "score_category": "9.1",
    "hotel": "Hotel Casa Arnaldo Esmeraldas",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 12,
    "province": " Esmeraldas",
    "category": "Value for money",
    "score_category": "8.6",
    "hotel": "Hotel Casa Arnaldo Esmeraldas",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 13,
    "province": " Esmeraldas",
    "category": "Location",
    "score_category": "9.5",
    "hotel": "Hotel Casa Arnaldo Esmeraldas",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 14,
    "province": " Esmeraldas",
    "category": "Free WiFi",
    "score_category": "7.9",
    "hotel": "Hotel Casa Arnaldo Esmeraldas",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 15,
    "province": " Esmeraldas",
    "category": "Staff",
    "score_category": "9.2",
    "hotel": "Hotel la Barca",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 16,
    "province": " Esmeraldas",
    "category": "Facilities",
    "score_category": "8.5",
    "hotel": "Hotel la Barca",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 17,
    "province": " Esmeraldas",
    "category": "Cleanliness",
    "score_category": "8.9",
    "hotel": "Hotel la Barca",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 18,
    "province": " Esmeraldas",
    "category": "Comfort",
    "score_category": "8.7",
    "hotel": "Hotel la Barca",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 19,
    "province": " Esmeraldas",
    "category": "Value for money",
    "score_category": "8.6",
    "hotel": "Hotel la Barca",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 20,
    "province": " Esmeraldas",
    "category": "Location",
    "score_category": "9.4",
    "hotel": "Hotel la Barca",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 21,
    "province": " Esmeraldas",
    "category": "Free WiFi",
    "score_category": "8.5",
    "hotel": "Hotel la Barca",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 22,
    "province": " Esmeraldas",
    "category": "Staff",
    "score_category": "9",
    "hotel": "Resort Playa Azul Departamentos frente al mar",
    "score_hotel": "9.3",
        }
    )
  batch.put_item(
  Item={
    "id": 23,
    "province": " Esmeraldas",
    "category": "Facilities",
    "score_category": "9.2",
    "hotel": "Resort Playa Azul Departamentos frente al mar",
    "score_hotel": "9.3",
        }
    )
  batch.put_item(
  Item={
    "id": 24,
    "province": " Esmeraldas",
    "category": "Cleanliness",
    "score_category": "9.3",
    "hotel": "Resort Playa Azul Departamentos frente al mar",
    "score_hotel": "9.3",
        }
    )
  batch.put_item(
  Item={
    "id": 25,
    "province": " Esmeraldas",
    "category": "Comfort",
    "score_category": "9.3",
    "hotel": "Resort Playa Azul Departamentos frente al mar",
    "score_hotel": "9.3",
        }
    )
  batch.put_item(
  Item={
    "id": 26,
    "province": " Esmeraldas",
    "category": "Value for money",
    "score_category": "8.9",
    "hotel": "Resort Playa Azul Departamentos frente al mar",
    "score_hotel": "9.3",
        }
    )
  batch.put_item(
  Item={
    "id": 27,
    "province": " Esmeraldas",
    "category": "Location",
    "score_category": "9.4",
    "hotel": "Resort Playa Azul Departamentos frente al mar",
    "score_hotel": "9.3",
        }
    )
  batch.put_item(
  Item={
    "id": 28,
    "province": " Esmeraldas",
    "category": "Free WiFi",
    "score_category": "7.9",
    "hotel": "Resort Playa Azul Departamentos frente al mar",
    "score_hotel": "9.3",
        }
    )
  batch.put_item(
  Item={
    "id": 29,
    "province": " Esmeraldas",
    "category": "Staff",
    "score_category": "8.9",
    "hotel": "Escapaditas a la Playa",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 30,
    "province": " Esmeraldas",
    "category": "Facilities",
    "score_category": "9.1",
    "hotel": "Escapaditas a la Playa",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 31,
    "province": " Esmeraldas",
    "category": "Cleanliness",
    "score_category": "9.3",
    "hotel": "Escapaditas a la Playa",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 32,
    "province": " Esmeraldas",
    "category": "Comfort",
    "score_category": "9.3",
    "hotel": "Escapaditas a la Playa",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 33,
    "province": " Esmeraldas",
    "category": "Value for money",
    "score_category": "9",
    "hotel": "Escapaditas a la Playa",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 34,
    "province": " Esmeraldas",
    "category": "Location",
    "score_category": "8.6",
    "hotel": "Escapaditas a la Playa",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 35,
    "province": " Esmeraldas",
    "category": "Staff",
    "score_category": "8.7",
    "hotel": "Hotel Oceanic Lodge",
    "score_hotel": "8.5",
        }
    )
  batch.put_item(
  Item={
    "id": 36,
    "province": " Esmeraldas",
    "category": "Facilities",
    "score_category": "8.7",
    "hotel": "Hotel Oceanic Lodge",
    "score_hotel": "8.5",
        }
    )
  batch.put_item(
  Item={
    "id": 37,
    "province": " Esmeraldas",
    "category": "Cleanliness",
    "score_category": "8.8",
    "hotel": "Hotel Oceanic Lodge",
    "score_hotel": "8.5",
        }
    )
  batch.put_item(
  Item={
    "id": 38,
    "province": " Esmeraldas",
    "category": "Comfort",
    "score_category": "9",
    "hotel": "Hotel Oceanic Lodge",
    "score_hotel": "8.5",
        }
    )
  batch.put_item(
  Item={
    "id": 39,
    "province": " Esmeraldas",
    "category": "Value for money",
    "score_category": "8.2",
    "hotel": "Hotel Oceanic Lodge",
    "score_hotel": "8.5",
        }
    )
  batch.put_item(
  Item={
    "id": 40,
    "province": " Esmeraldas",
    "category": "Location",
    "score_category": "7.9",
    "hotel": "Hotel Oceanic Lodge",
    "score_hotel": "8.5",
        }
    )
  batch.put_item(
  Item={
    "id": 41,
    "province": " Esmeraldas",
    "category": "Free WiFi",
    "score_category": "7.5",
    "hotel": "Hotel Oceanic Lodge",
    "score_hotel": "8.5",
        }
    )
  batch.put_item(
  Item={
    "id": 42,
    "province": " Esmeraldas",
    "category": "Staff",
    "score_category": "9.5",
    "hotel": "Seaside Garden Ecolodge Mompiche",
    "score_hotel": "9",
        }
    )
  batch.put_item(
  Item={
    "id": 43,
    "province": " Esmeraldas",
    "category": "Facilities",
    "score_category": "8.8",
    "hotel": "Seaside Garden Ecolodge Mompiche",
    "score_hotel": "9",
        }
    )
  batch.put_item(
  Item={
    "id": 44,
    "province": " Esmeraldas",
    "category": "Cleanliness",
    "score_category": "8.9",
    "hotel": "Seaside Garden Ecolodge Mompiche",
    "score_hotel": "9",
        }
    )
  batch.put_item(
  Item={
    "id": 45,
    "province": " Esmeraldas",
    "category": "Comfort",
    "score_category": "9.2",
    "hotel": "Seaside Garden Ecolodge Mompiche",
    "score_hotel": "9",
        }
    )
  batch.put_item(
  Item={
    "id": 46,
    "province": " Esmeraldas",
    "category": "Value for money",
    "score_category": "9.1",
    "hotel": "Seaside Garden Ecolodge Mompiche",
    "score_hotel": "9",
        }
    )
  batch.put_item(
  Item={
    "id": 47,
    "province": " Esmeraldas",
    "category": "Location",
    "score_category": "8.9",
    "hotel": "Seaside Garden Ecolodge Mompiche",
    "score_hotel": "9",
        }
    )
  batch.put_item(
  Item={
    "id": 48,
    "province": " Esmeraldas",
    "category": "Free WiFi",
    "score_category": "6.4",
    "hotel": "Seaside Garden Ecolodge Mompiche",
    "score_hotel": "9",
        }
    )
  batch.put_item(
  Item={
    "id": 49,
    "province": " Esmeraldas",
    "category": "Staff",
    "score_category": "9.2",
    "hotel": "Hotel RC Tonsupa",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 50,
    "province": " Esmeraldas",
    "category": "Facilities",
    "score_category": "8.6",
    "hotel": "Hotel RC Tonsupa",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 51,
    "province": " Esmeraldas",
    "category": "Cleanliness",
    "score_category": "9",
    "hotel": "Hotel RC Tonsupa",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 52,
    "province": " Esmeraldas",
    "category": "Comfort",
    "score_category": "8.8",
    "hotel": "Hotel RC Tonsupa",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 53,
    "province": " Esmeraldas",
    "category": "Value for money",
    "score_category": "8.5",
    "hotel": "Hotel RC Tonsupa",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 54,
    "province": " Esmeraldas",
    "category": "Location",
    "score_category": "7.9",
    "hotel": "Hotel RC Tonsupa",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 55,
    "province": " Esmeraldas",
    "category": "Free WiFi",
    "score_category": "7.2",
    "hotel": "Hotel RC Tonsupa",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 56,
    "province": " Esmeraldas",
    "category": "Staff",
    "score_category": "9.3",
    "hotel": "Departamento Frente al Mar Diamond Beach",
    "score_hotel": "9.4",
        }
    )
  batch.put_item(
  Item={
    "id": 57,
    "province": " Esmeraldas",
    "category": "Facilities",
    "score_category": "9.4",
    "hotel": "Departamento Frente al Mar Diamond Beach",
    "score_hotel": "9.4",
        }
    )
  batch.put_item(
  Item={
    "id": 58,
    "province": " Esmeraldas",
    "category": "Cleanliness",
    "score_category": "9.4",
    "hotel": "Departamento Frente al Mar Diamond Beach",
    "score_hotel": "9.4",
        }
    )
  batch.put_item(
  Item={
    "id": 59,
    "province": " Esmeraldas",
    "category": "Comfort",
    "score_category": "9.5",
    "hotel": "Departamento Frente al Mar Diamond Beach",
    "score_hotel": "9.4",
        }
    )
  batch.put_item(
  Item={
    "id": 60,
    "province": " Esmeraldas",
    "category": "Value for money",
    "score_category": "9.2",
    "hotel": "Departamento Frente al Mar Diamond Beach",
    "score_hotel": "9.4",
        }
    )
  batch.put_item(
  Item={
    "id": 61,
    "province": " Esmeraldas",
    "category": "Location",
    "score_category": "9.8",
    "hotel": "Departamento Frente al Mar Diamond Beach",
    "score_hotel": "9.4",
        }
    )
  batch.put_item(
  Item={
    "id": 62,
    "province": " Esmeraldas",
    "category": "Staff",
    "score_category": "8.7",
    "hotel": "Hotel Almond Beach",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 63,
    "province": " Esmeraldas",
    "category": "Facilities",
    "score_category": "8.7",
    "hotel": "Hotel Almond Beach",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 64,
    "province": " Esmeraldas",
    "category": "Cleanliness",
    "score_category": "8.9",
    "hotel": "Hotel Almond Beach",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 65,
    "province": " Esmeraldas",
    "category": "Comfort",
    "score_category": "8.9",
    "hotel": "Hotel Almond Beach",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 66,
    "province": " Esmeraldas",
    "category": "Value for money",
    "score_category": "8.5",
    "hotel": "Hotel Almond Beach",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 67,
    "province": " Esmeraldas",
    "category": "Location",
    "score_category": "8.6",
    "hotel": "Hotel Almond Beach",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 68,
    "province": " Esmeraldas",
    "category": "Free WiFi",
    "score_category": "7.5",
    "hotel": "Hotel Almond Beach",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 69,
    "province": " Esmeraldas",
    "category": "Staff",
    "score_category": "9.2",
    "hotel": "Cabañas Ecologicas Cayapas",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 70,
    "province": " Esmeraldas",
    "category": "Facilities",
    "score_category": "8.5",
    "hotel": "Cabañas Ecologicas Cayapas",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 71,
    "province": " Esmeraldas",
    "category": "Cleanliness",
    "score_category": "8.9",
    "hotel": "Cabañas Ecologicas Cayapas",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 72,
    "province": " Esmeraldas",
    "category": "Comfort",
    "score_category": "8.9",
    "hotel": "Cabañas Ecologicas Cayapas",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 73,
    "province": " Esmeraldas",
    "category": "Value for money",
    "score_category": "8.7",
    "hotel": "Cabañas Ecologicas Cayapas",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 74,
    "province": " Esmeraldas",
    "category": "Location",
    "score_category": "9.5",
    "hotel": "Cabañas Ecologicas Cayapas",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 75,
    "province": " Esmeraldas",
    "category": "Free WiFi",
    "score_category": "8.2",
    "hotel": "Cabañas Ecologicas Cayapas",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 76,
    "province": " Esmeraldas",
    "category": "Staff",
    "score_category": "8.8",
    "hotel": "Departamento 4 habitaciones 12 personas vista al mar 8vo piso Playa Almendro",
    "score_hotel": "7.5",
        }
    )
  batch.put_item(
  Item={
    "id": 77,
    "province": " Esmeraldas",
    "category": "Facilities",
    "score_category": "7.9",
    "hotel": "Departamento 4 habitaciones 12 personas vista al mar 8vo piso Playa Almendro",
    "score_hotel": "7.5",
        }
    )
  batch.put_item(
  Item={
    "id": 78,
    "province": " Esmeraldas",
    "category": "Cleanliness",
    "score_category": "8.7",
    "hotel": "Departamento 4 habitaciones 12 personas vista al mar 8vo piso Playa Almendro",
    "score_hotel": "7.5",
        }
    )
  batch.put_item(
  Item={
    "id": 79,
    "province": " Esmeraldas",
    "category": "Comfort",
    "score_category": "8.4",
    "hotel": "Departamento 4 habitaciones 12 personas vista al mar 8vo piso Playa Almendro",
    "score_hotel": "7.5",
        }
    )
  batch.put_item(
  Item={
    "id": 80,
    "province": " Esmeraldas",
    "category": "Value for money",
    "score_category": "7.3",
    "hotel": "Departamento 4 habitaciones 12 personas vista al mar 8vo piso Playa Almendro",
    "score_hotel": "7.5",
        }
    )
  batch.put_item(
  Item={
    "id": 81,
    "province": " Esmeraldas",
    "category": "Location",
    "score_category": "8.6",
    "hotel": "Departamento 4 habitaciones 12 personas vista al mar 8vo piso Playa Almendro",
    "score_hotel": "7.5",
        }
    )
  batch.put_item(
  Item={
    "id": 82,
    "province": " Esmeraldas",
    "category": "Staff",
    "score_category": "9.2",
    "hotel": "Resort Playa Azul Tonsupa Departamento de 2 Habitaciones",
    "score_hotel": "9.1",
        }
    )
  batch.put_item(
  Item={
    "id": 83,
    "province": " Esmeraldas",
    "category": "Facilities",
    "score_category": "9.1",
    "hotel": "Resort Playa Azul Tonsupa Departamento de 2 Habitaciones",
    "score_hotel": "9.1",
        }
    )
  batch.put_item(
  Item={
    "id": 84,
    "province": " Esmeraldas",
    "category": "Cleanliness",
    "score_category": "9.5",
    "hotel": "Resort Playa Azul Tonsupa Departamento de 2 Habitaciones",
    "score_hotel": "9.1",
        }
    )
  batch.put_item(
  Item={
    "id": 85,
    "province": " Esmeraldas",
    "category": "Comfort",
    "score_category": "9.5",
    "hotel": "Resort Playa Azul Tonsupa Departamento de 2 Habitaciones",
    "score_hotel": "9.1",
        }
    )
  batch.put_item(
  Item={
    "id": 86,
    "province": " Esmeraldas",
    "category": "Value for money",
    "score_category": "8.9",
    "hotel": "Resort Playa Azul Tonsupa Departamento de 2 Habitaciones",
    "score_hotel": "9.1",
        }
    )
  batch.put_item(
  Item={
    "id": 87,
    "province": " Esmeraldas",
    "category": "Location",
    "score_category": "9.2",
    "hotel": "Resort Playa Azul Tonsupa Departamento de 2 Habitaciones",
    "score_hotel": "9.1",
        }
    )
  batch.put_item(
  Item={
    "id": 88,
    "province": " Esmeraldas",
    "category": "Free WiFi",
    "score_category": "10",
    "hotel": "Resort Playa Azul Tonsupa Departamento de 2 Habitaciones",
    "score_hotel": "9.1",
        }
    )
  batch.put_item(
  Item={
    "id": 89,
    "province": " Esmeraldas",
    "category": "Staff",
    "score_category": "9.2",
    "hotel": "Tonsupa Diamond Beach Apart - Hotel",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 90,
    "province": " Esmeraldas",
    "category": "Facilities",
    "score_category": "8.6",
    "hotel": "Tonsupa Diamond Beach Apart - Hotel",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 91,
    "province": " Esmeraldas",
    "category": "Cleanliness",
    "score_category": "8.9",
    "hotel": "Tonsupa Diamond Beach Apart - Hotel",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 92,
    "province": " Esmeraldas",
    "category": "Comfort",
    "score_category": "9",
    "hotel": "Tonsupa Diamond Beach Apart - Hotel",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 93,
    "province": " Esmeraldas",
    "category": "Value for money",
    "score_category": "8.7",
    "hotel": "Tonsupa Diamond Beach Apart - Hotel",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 94,
    "province": " Esmeraldas",
    "category": "Location",
    "score_category": "9.6",
    "hotel": "Tonsupa Diamond Beach Apart - Hotel",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 95,
    "province": " Esmeraldas",
    "category": "Free WiFi",
    "score_category": "7.5",
    "hotel": "Tonsupa Diamond Beach Apart - Hotel",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 96,
    "province": " Esmeraldas",
    "category": "Staff",
    "score_category": "9.3",
    "hotel": "Aparthotel Oleaje",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 97,
    "province": " Esmeraldas",
    "category": "Facilities",
    "score_category": "8.8",
    "hotel": "Aparthotel Oleaje",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 98,
    "province": " Esmeraldas",
    "category": "Cleanliness",
    "score_category": "9.3",
    "hotel": "Aparthotel Oleaje",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 99,
    "province": " Esmeraldas",
    "category": "Comfort",
    "score_category": "8.9",
    "hotel": "Aparthotel Oleaje",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 100,
    "province": " Esmeraldas",
    "category": "Value for money",
    "score_category": "8.8",
    "hotel": "Aparthotel Oleaje",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 101,
    "province": " Esmeraldas",
    "category": "Location",
    "score_category": "8.7",
    "hotel": "Aparthotel Oleaje",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 102,
    "province": " Esmeraldas",
    "category": "Free WiFi",
    "score_category": "6.3",
    "hotel": "Aparthotel Oleaje",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 103,
    "province": " Esmeraldas",
    "category": "Staff",
    "score_category": "8.7",
    "hotel": "Hotel Makana Resort",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 104,
    "province": " Esmeraldas",
    "category": "Facilities",
    "score_category": "8.4",
    "hotel": "Hotel Makana Resort",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 105,
    "province": " Esmeraldas",
    "category": "Cleanliness",
    "score_category": "9",
    "hotel": "Hotel Makana Resort",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 106,
    "province": " Esmeraldas",
    "category": "Comfort",
    "score_category": "9",
    "hotel": "Hotel Makana Resort",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 107,
    "province": " Esmeraldas",
    "category": "Value for money",
    "score_category": "8",
    "hotel": "Hotel Makana Resort",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 108,
    "province": " Esmeraldas",
    "category": "Location",
    "score_category": "9",
    "hotel": "Hotel Makana Resort",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 109,
    "province": " Esmeraldas",
    "category": "Free WiFi",
    "score_category": "7.2",
    "hotel": "Hotel Makana Resort",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 110,
    "province": " Esmeraldas",
    "category": "Staff",
    "score_category": "9.2",
    "hotel": "La Bocana",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 111,
    "province": " Esmeraldas",
    "category": "Facilities",
    "score_category": "8.6",
    "hotel": "La Bocana",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 112,
    "province": " Esmeraldas",
    "category": "Cleanliness",
    "score_category": "9.1",
    "hotel": "La Bocana",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 113,
    "province": " Esmeraldas",
    "category": "Comfort",
    "score_category": "9",
    "hotel": "La Bocana",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 114,
    "province": " Esmeraldas",
    "category": "Value for money",
    "score_category": "8.7",
    "hotel": "La Bocana",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 115,
    "province": " Esmeraldas",
    "category": "Location",
    "score_category": "9.1",
    "hotel": "La Bocana",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 116,
    "province": " Esmeraldas",
    "category": "Free WiFi",
    "score_category": "7.2",
    "hotel": "La Bocana",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 117,
    "province": " Esmeraldas",
    "category": "Staff",
    "score_category": "10",
    "hotel": "Departamentos frente al mar Resort Playa Azul",
    "score_hotel": "9.6",
        }
    )
  batch.put_item(
  Item={
    "id": 118,
    "province": " Esmeraldas",
    "category": "Facilities",
    "score_category": "9.4",
    "hotel": "Departamentos frente al mar Resort Playa Azul",
    "score_hotel": "9.6",
        }
    )
  batch.put_item(
  Item={
    "id": 119,
    "province": " Esmeraldas",
    "category": "Cleanliness",
    "score_category": "10",
    "hotel": "Departamentos frente al mar Resort Playa Azul",
    "score_hotel": "9.6",
        }
    )
  batch.put_item(
  Item={
    "id": 120,
    "province": " Esmeraldas",
    "category": "Comfort",
    "score_category": "10",
    "hotel": "Departamentos frente al mar Resort Playa Azul",
    "score_hotel": "9.6",
        }
    )
  batch.put_item(
  Item={
    "id": 121,
    "province": " Esmeraldas",
    "category": "Value for money",
    "score_category": "9.7",
    "hotel": "Departamentos frente al mar Resort Playa Azul",
    "score_hotel": "9.6",
        }
    )
  batch.put_item(
  Item={
    "id": 122,
    "province": " Esmeraldas",
    "category": "Location",
    "score_category": "10",
    "hotel": "Departamentos frente al mar Resort Playa Azul",
    "score_hotel": "9.6",
        }
    )
  batch.put_item(
  Item={
    "id": 123,
    "province": " Esmeraldas",
    "category": "Staff",
    "score_category": "8.4",
    "hotel": "Suite Makana #403",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 124,
    "province": " Esmeraldas",
    "category": "Facilities",
    "score_category": "8.2",
    "hotel": "Suite Makana #403",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 125,
    "province": " Esmeraldas",
    "category": "Cleanliness",
    "score_category": "8.6",
    "hotel": "Suite Makana #403",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 126,
    "province": " Esmeraldas",
    "category": "Comfort",
    "score_category": "8.6",
    "hotel": "Suite Makana #403",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 127,
    "province": " Esmeraldas",
    "category": "Value for money",
    "score_category": "8.1",
    "hotel": "Suite Makana #403",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 128,
    "province": " Esmeraldas",
    "category": "Location",
    "score_category": "9.3",
    "hotel": "Suite Makana #403",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 129,
    "province": " Esmeraldas",
    "category": "Free WiFi",
    "score_category": "9.2",
    "hotel": "Suite Makana #403",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 130,
    "province": " Esmeraldas",
    "category": "Staff",
    "score_category": "8.9",
    "hotel": "Caramba Hospedaje",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 131,
    "province": " Esmeraldas",
    "category": "Facilities",
    "score_category": "8.6",
    "hotel": "Caramba Hospedaje",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 132,
    "province": " Esmeraldas",
    "category": "Cleanliness",
    "score_category": "8.8",
    "hotel": "Caramba Hospedaje",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 133,
    "province": " Esmeraldas",
    "category": "Comfort",
    "score_category": "8.6",
    "hotel": "Caramba Hospedaje",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 134,
    "province": " Esmeraldas",
    "category": "Value for money",
    "score_category": "8.3",
    "hotel": "Caramba Hospedaje",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 135,
    "province": " Esmeraldas",
    "category": "Location",
    "score_category": "9.4",
    "hotel": "Caramba Hospedaje",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 136,
    "province": " Esmeraldas",
    "category": "Free WiFi",
    "score_category": "8.8",
    "hotel": "Caramba Hospedaje",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 137,
    "province": " Esmeraldas",
    "category": "Staff",
    "score_category": "9.2",
    "hotel": "Hotel Salduba",
    "score_hotel": "9.1",
        }
    )
  batch.put_item(
  Item={
    "id": 138,
    "province": " Esmeraldas",
    "category": "Facilities",
    "score_category": "8.9",
    "hotel": "Hotel Salduba",
    "score_hotel": "9.1",
        }
    )
  batch.put_item(
  Item={
    "id": 139,
    "province": " Esmeraldas",
    "category": "Cleanliness",
    "score_category": "9.3",
    "hotel": "Hotel Salduba",
    "score_hotel": "9.1",
        }
    )
  batch.put_item(
  Item={
    "id": 140,
    "province": " Esmeraldas",
    "category": "Comfort",
    "score_category": "9.1",
    "hotel": "Hotel Salduba",
    "score_hotel": "9.1",
        }
    )
  batch.put_item(
  Item={
    "id": 141,
    "province": " Esmeraldas",
    "category": "Value for money",
    "score_category": "8.7",
    "hotel": "Hotel Salduba",
    "score_hotel": "9.1",
        }
    )
  batch.put_item(
  Item={
    "id": 142,
    "province": " Esmeraldas",
    "category": "Location",
    "score_category": "8.9",
    "hotel": "Hotel Salduba",
    "score_hotel": "9.1",
        }
    )
  batch.put_item(
  Item={
    "id": 143,
    "province": " Esmeraldas",
    "category": "Free WiFi",
    "score_category": "7.5",
    "hotel": "Hotel Salduba",
    "score_hotel": "9.1",
        }
    )
  batch.put_item(
  Item={
    "id": 144,
    "province": " Esmeraldas",
    "category": "Staff",
    "score_category": "8.6",
    "hotel": "Casa del mar",
    "score_hotel": "6.7",
        }
    )
  batch.put_item(
  Item={
    "id": 145,
    "province": " Esmeraldas",
    "category": "Facilities",
    "score_category": "8.9",
    "hotel": "Casa del mar",
    "score_hotel": "6.7",
        }
    )
  batch.put_item(
  Item={
    "id": 146,
    "province": " Esmeraldas",
    "category": "Cleanliness",
    "score_category": "8.9",
    "hotel": "Casa del mar",
    "score_hotel": "6.7",
        }
    )
  batch.put_item(
  Item={
    "id": 147,
    "province": " Esmeraldas",
    "category": "Comfort",
    "score_category": "8.9",
    "hotel": "Casa del mar",
    "score_hotel": "6.7",
        }
    )
  batch.put_item(
  Item={
    "id": 148,
    "province": " Esmeraldas",
    "category": "Value for money",
    "score_category": "8.9",
    "hotel": "Casa del mar",
    "score_hotel": "6.7",
        }
    )
  batch.put_item(
  Item={
    "id": 149,
    "province": " Esmeraldas",
    "category": "Location",
    "score_category": "6.7",
    "hotel": "Casa del mar",
    "score_hotel": "6.7",
        }
    )
  batch.put_item(
  Item={
    "id": 150,
    "province": " Esmeraldas",
    "category": "Staff",
    "score_category": "9.2",
    "hotel": "Tus Vacaciones en Tonsupa Ecuador.",
    "score_hotel": "9.1",
        }
    )
  batch.put_item(
  Item={
    "id": 151,
    "province": " Esmeraldas",
    "category": "Facilities",
    "score_category": "8.8",
    "hotel": "Tus Vacaciones en Tonsupa Ecuador.",
    "score_hotel": "9.1",
        }
    )
  batch.put_item(
  Item={
    "id": 152,
    "province": " Esmeraldas",
    "category": "Cleanliness",
    "score_category": "8.9",
    "hotel": "Tus Vacaciones en Tonsupa Ecuador.",
    "score_hotel": "9.1",
        }
    )
  batch.put_item(
  Item={
    "id": 153,
    "province": " Esmeraldas",
    "category": "Comfort",
    "score_category": "8.8",
    "hotel": "Tus Vacaciones en Tonsupa Ecuador.",
    "score_hotel": "9.1",
        }
    )
  batch.put_item(
  Item={
    "id": 154,
    "province": " Esmeraldas",
    "category": "Value for money",
    "score_category": "8.8",
    "hotel": "Tus Vacaciones en Tonsupa Ecuador.",
    "score_hotel": "9.1",
        }
    )
  batch.put_item(
  Item={
    "id": 155,
    "province": " Esmeraldas",
    "category": "Location",
    "score_category": "8",
    "hotel": "Tus Vacaciones en Tonsupa Ecuador.",
    "score_hotel": "9.1",
        }
    )
  batch.put_item(
  Item={
    "id": 156,
    "province": " Esmeraldas",
    "category": "Free WiFi",
    "score_category": "10",
    "hotel": "Tus Vacaciones en Tonsupa Ecuador.",
    "score_hotel": "9.1",
        }
    )
  batch.put_item(
  Item={
    "id": 157,
    "province": " Esmeraldas",
    "category": "Staff",
    "score_category": "8.7",
    "hotel": "Departamentos frente al mar en Resort Playa Azul-Tonsupa",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 158,
    "province": " Esmeraldas",
    "category": "Facilities",
    "score_category": "8.7",
    "hotel": "Departamentos frente al mar en Resort Playa Azul-Tonsupa",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 159,
    "province": " Esmeraldas",
    "category": "Cleanliness",
    "score_category": "8.6",
    "hotel": "Departamentos frente al mar en Resort Playa Azul-Tonsupa",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 160,
    "province": " Esmeraldas",
    "category": "Comfort",
    "score_category": "8.8",
    "hotel": "Departamentos frente al mar en Resort Playa Azul-Tonsupa",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 161,
    "province": " Esmeraldas",
    "category": "Value for money",
    "score_category": "8.1",
    "hotel": "Departamentos frente al mar en Resort Playa Azul-Tonsupa",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 162,
    "province": " Esmeraldas",
    "category": "Location",
    "score_category": "9",
    "hotel": "Departamentos frente al mar en Resort Playa Azul-Tonsupa",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 163,
    "province": "Esmeraldas",
    "category": "Free WiFi",
    "score_category": "5.2",
    "hotel": "Departamentos frente al mar en Resort Playa Azul-Tonsupa",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 164,
    "province": "Cuenca",
    "category": "Staff",
    "score_category": "8.8",
    "hotel": "Hotel Santiago de Compostella Suites",
    "score_hotel": "8.1",
        }
    )
  batch.put_item(
  Item={
    "id": 165,
    "province": "Cuenca",
    "category": "Facilities",
    "score_category": "8.2",
    "hotel": "Hotel Santiago de Compostella Suites",
    "score_hotel": "8.1",
        }
    )
  batch.put_item(
  Item={
    "id": 166,
    "province": "Cuenca",
    "category": "Cleanliness",
    "score_category": "8.5",
    "hotel": "Hotel Santiago de Compostella Suites",
    "score_hotel": "8.1",
        }
    )
  batch.put_item(
  Item={
    "id": 167,
    "province": "Cuenca",
    "category": "Comfort",
    "score_category": "8.5",
    "hotel": "Hotel Santiago de Compostella Suites",
    "score_hotel": "8.1",
        }
    )
  batch.put_item(
  Item={
    "id": 168,
    "province": "Cuenca",
    "category": "Value for money",
    "score_category": "8.3",
    "hotel": "Hotel Santiago de Compostella Suites",
    "score_hotel": "8.1",
        }
    )
  batch.put_item(
  Item={
    "id": 169,
    "province": "Cuenca",
    "category": "Location",
    "score_category": "8.9",
    "hotel": "Hotel Santiago de Compostella Suites",
    "score_hotel": "8.1",
        }
    )
  batch.put_item(
  Item={
    "id": 170,
    "province": "Cuenca",
    "category": "Free WiFi",
    "score_category": "7.8",
    "hotel": "Hotel Santiago de Compostella Suites",
    "score_hotel": "8.1",
        }
    )
  batch.put_item(
  Item={
    "id": 171,
    "province": "Cuenca",
    "category": "Staff",
    "score_category": "9.5",
    "hotel": "Floré Hotel Boutique",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 172,
    "province": "Cuenca",
    "category": "Facilities",
    "score_category": "8.8",
    "hotel": "Floré Hotel Boutique",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 173,
    "province": "Cuenca",
    "category": "Cleanliness",
    "score_category": "9",
    "hotel": "Floré Hotel Boutique",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 174,
    "province": "Cuenca",
    "category": "Comfort",
    "score_category": "9",
    "hotel": "Floré Hotel Boutique",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 175,
    "province": "Cuenca",
    "category": "Value for money",
    "score_category": "8.8",
    "hotel": "Floré Hotel Boutique",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 176,
    "province": "Cuenca",
    "category": "Location",
    "score_category": "9.7",
    "hotel": "Floré Hotel Boutique",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 177,
    "province": "Cuenca",
    "category": "Free WiFi",
    "score_category": "8.5",
    "hotel": "Floré Hotel Boutique",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 178,
    "province": "Cuenca",
    "category": "Staff",
    "score_category": "8.9",
    "hotel": "Loft NASS Atahualpa",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 179,
    "province": "Cuenca",
    "category": "Facilities",
    "score_category": "8.6",
    "hotel": "Loft NASS Atahualpa",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 180,
    "province": "Cuenca",
    "category": "Cleanliness",
    "score_category": "9",
    "hotel": "Loft NASS Atahualpa",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 181,
    "province": "Cuenca",
    "category": "Comfort",
    "score_category": "8.9",
    "hotel": "Loft NASS Atahualpa",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 182,
    "province": "Cuenca",
    "category": "Value for money",
    "score_category": "8.8",
    "hotel": "Loft NASS Atahualpa",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 183,
    "province": "Cuenca",
    "category": "Location",
    "score_category": "9.1",
    "hotel": "Loft NASS Atahualpa",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 184,
    "province": "Cuenca",
    "category": "Free WiFi",
    "score_category": "8",
    "hotel": "Loft NASS Atahualpa",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 185,
    "province": "Cuenca",
    "category": "Staff",
    "score_category": "9.7",
    "hotel": "Hostal Posada del Angel",
    "score_hotel": "9.3",
        }
    )
  batch.put_item(
  Item={
    "id": 186,
    "province": "Cuenca",
    "category": "Facilities",
    "score_category": "9.1",
    "hotel": "Hostal Posada del Angel",
    "score_hotel": "9.3",
        }
    )
  batch.put_item(
  Item={
    "id": 187,
    "province": "Cuenca",
    "category": "Cleanliness",
    "score_category": "9.5",
    "hotel": "Hostal Posada del Angel",
    "score_hotel": "9.3",
        }
    )
  batch.put_item(
  Item={
    "id": 188,
    "province": "Cuenca",
    "category": "Comfort",
    "score_category": "9.3",
    "hotel": "Hostal Posada del Angel",
    "score_hotel": "9.3",
        }
    )
  batch.put_item(
  Item={
    "id": 189,
    "province": "Cuenca",
    "category": "Value for money",
    "score_category": "9.5",
    "hotel": "Hostal Posada del Angel",
    "score_hotel": "9.3",
        }
    )
  batch.put_item(
  Item={
    "id": 190,
    "province": "Cuenca",
    "category": "Location",
    "score_category": "9.7",
    "hotel": "Hostal Posada del Angel",
    "score_hotel": "9.3",
        }
    )
  batch.put_item(
  Item={
    "id": 191,
    "province": "Cuenca",
    "category": "Free WiFi",
    "score_category": "8.8",
    "hotel": "Hostal Posada del Angel",
    "score_hotel": "9.3",
        }
    )
  batch.put_item(
  Item={
    "id": 192,
    "province": "Cuenca",
    "category": "Staff",
    "score_category": "9.5",
    "hotel": "Hotel La Orquidea",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 193,
    "province": "Cuenca",
    "category": "Facilities",
    "score_category": "8.7",
    "hotel": "Hotel La Orquidea",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 194,
    "province": "Cuenca",
    "category": "Cleanliness",
    "score_category": "9.1",
    "hotel": "Hotel La Orquidea",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 195,
    "province": "Cuenca",
    "category": "Comfort",
    "score_category": "8.9",
    "hotel": "Hotel La Orquidea",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 196,
    "province": "Cuenca",
    "category": "Value for money",
    "score_category": "9",
    "hotel": "Hotel La Orquidea",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 197,
    "province": "Cuenca",
    "category": "Location",
    "score_category": "9.8",
    "hotel": "Hotel La Orquidea",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 198,
    "province": "Cuenca",
    "category": "Free WiFi",
    "score_category": "8.8",
    "hotel": "Hotel La Orquidea",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 199,
    "province": "Cuenca",
    "category": "Staff",
    "score_category": "8.5",
    "hotel": "Hotel Boutique Castilla de Léon",
    "score_hotel": "8",
        }
    )
  batch.put_item(
  Item={
    "id": 200,
    "province": "Cuenca",
    "category": "Facilities",
    "score_category": "8.1",
    "hotel": "Hotel Boutique Castilla de Léon",
    "score_hotel": "8",
        }
    )
  batch.put_item(
  Item={
    "id": 201,
    "province": "Cuenca",
    "category": "Cleanliness",
    "score_category": "8.4",
    "hotel": "Hotel Boutique Castilla de Léon",
    "score_hotel": "8",
        }
    )
  batch.put_item(
  Item={
    "id": 202,
    "province": "Cuenca",
    "category": "Comfort",
    "score_category": "8.4",
    "hotel": "Hotel Boutique Castilla de Léon",
    "score_hotel": "8",
        }
    )
  batch.put_item(
  Item={
    "id": 203,
    "province": "Cuenca",
    "category": "Value for money",
    "score_category": "8.3",
    "hotel": "Hotel Boutique Castilla de Léon",
    "score_hotel": "8",
        }
    )
  batch.put_item(
  Item={
    "id": 204,
    "province": "Cuenca",
    "category": "Location",
    "score_category": "8.5",
    "hotel": "Hotel Boutique Castilla de Léon",
    "score_hotel": "8",
        }
    )
  batch.put_item(
  Item={
    "id": 205,
    "province": "Cuenca",
    "category": "Free WiFi",
    "score_category": "8.1",
    "hotel": "Hotel Boutique Castilla de Léon",
    "score_hotel": "8",
        }
    )
  batch.put_item(
  Item={
    "id": 206,
    "province": "Cuenca",
    "category": "Staff",
    "score_category": "8.7",
    "hotel": "Selina Cuenca",
    "score_hotel": "8.3",
        }
    )
  batch.put_item(
  Item={
    "id": 207,
    "province": "Cuenca",
    "category": "Facilities",
    "score_category": "8.5",
    "hotel": "Selina Cuenca",
    "score_hotel": "8.3",
        }
    )
  batch.put_item(
  Item={
    "id": 208,
    "province": "Cuenca",
    "category": "Cleanliness",
    "score_category": "8.7",
    "hotel": "Selina Cuenca",
    "score_hotel": "8.3",
        }
    )
  batch.put_item(
  Item={
    "id": 209,
    "province": "Cuenca",
    "category": "Comfort",
    "score_category": "8.6",
    "hotel": "Selina Cuenca",
    "score_hotel": "8.3",
        }
    )
  batch.put_item(
  Item={
    "id": 210,
    "province": "Cuenca",
    "category": "Value for money",
    "score_category": "8.3",
    "hotel": "Selina Cuenca",
    "score_hotel": "8.3",
        }
    )
  batch.put_item(
  Item={
    "id": 211,
    "province": "Cuenca",
    "category": "Location",
    "score_category": "9.4",
    "hotel": "Selina Cuenca",
    "score_hotel": "8.3",
        }
    )
  batch.put_item(
  Item={
    "id": 212,
    "province": "Cuenca",
    "category": "Free WiFi",
    "score_category": "8.8",
    "hotel": "Selina Cuenca",
    "score_hotel": "8.3",
        }
    )
  batch.put_item(
  Item={
    "id": 213,
    "province": "Cuenca",
    "category": "Staff",
    "score_category": "9.5",
    "hotel": "Hotel Posada del Rey",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 214,
    "province": "Cuenca",
    "category": "Facilities",
    "score_category": "8.8",
    "hotel": "Hotel Posada del Rey",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 215,
    "province": "Cuenca",
    "category": "Cleanliness",
    "score_category": "9.2",
    "hotel": "Hotel Posada del Rey",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 216,
    "province": "Cuenca",
    "category": "Comfort",
    "score_category": "9",
    "hotel": "Hotel Posada del Rey",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 217,
    "province": "Cuenca",
    "category": "Value for money",
    "score_category": "8.9",
    "hotel": "Hotel Posada del Rey",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 218,
    "province": "Cuenca",
    "category": "Location",
    "score_category": "9.7",
    "hotel": "Hotel Posada del Rey",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 219,
    "province": "Cuenca",
    "category": "Free WiFi",
    "score_category": "8",
    "hotel": "Hotel Posada del Rey",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 220,
    "province": "Cuenca",
    "category": "Staff",
    "score_category": "9.3",
    "hotel": "Hotel Azul de la Plaza",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 221,
    "province": "Cuenca",
    "category": "Facilities",
    "score_category": "8.8",
    "hotel": "Hotel Azul de la Plaza",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 222,
    "province": "Cuenca",
    "category": "Cleanliness",
    "score_category": "8.9",
    "hotel": "Hotel Azul de la Plaza",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 223,
    "province": "Cuenca",
    "category": "Comfort",
    "score_category": "9.1",
    "hotel": "Hotel Azul de la Plaza",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 224,
    "province": "Cuenca",
    "category": "Value for money",
    "score_category": "8.6",
    "hotel": "Hotel Azul de la Plaza",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 225,
    "province": "Cuenca",
    "category": "Location",
    "score_category": "9.1",
    "hotel": "Hotel Azul de la Plaza",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 226,
    "province": "Cuenca",
    "category": "Free WiFi",
    "score_category": "8.2",
    "hotel": "Hotel Azul de la Plaza",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 227,
    "province": "Cuenca",
    "category": "Staff",
    "score_category": "9.7",
    "hotel": "Pepe's House Cuenca Boutique Hotel l B&B",
    "score_hotel": "9.3",
        }
    )
  batch.put_item(
  Item={
    "id": 228,
    "province": "Cuenca",
    "category": "Facilities",
    "score_category": "9.3",
    "hotel": "Pepe's House Cuenca Boutique Hotel l B&B",
    "score_hotel": "9.3",
        }
    )
  batch.put_item(
  Item={
    "id": 229,
    "province": "Cuenca",
    "category": "Cleanliness",
    "score_category": "9.6",
    "hotel": "Pepe's House Cuenca Boutique Hotel l B&B",
    "score_hotel": "9.3",
        }
    )
  batch.put_item(
  Item={
    "id": 230,
    "province": "Cuenca",
    "category": "Comfort",
    "score_category": "9.4",
    "hotel": "Pepe's House Cuenca Boutique Hotel l B&B",
    "score_hotel": "9.3",
        }
    )
  batch.put_item(
  Item={
    "id": 231,
    "province": "Cuenca",
    "category": "Value for money",
    "score_category": "9.1",
    "hotel": "Pepe's House Cuenca Boutique Hotel l B&B",
    "score_hotel": "9.3",
        }
    )
  batch.put_item(
  Item={
    "id": 232,
    "province": "Cuenca",
    "category": "Location",
    "score_category": "9.7",
    "hotel": "Pepe's House Cuenca Boutique Hotel l B&B",
    "score_hotel": "9.3",
        }
    )
  batch.put_item(
  Item={
    "id": 233,
    "province": "Cuenca",
    "category": "Free WiFi",
    "score_category": "9.3",
    "hotel": "Pepe's House Cuenca Boutique Hotel l B&B",
    "score_hotel": "9.3",
        }
    )
  batch.put_item(
  Item={
    "id": 234,
    "province": "Cuenca",
    "category": "Staff",
    "score_category": "9.2",
    "hotel": "Hostal Mariscal Inn & Suite",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 235,
    "province": "Cuenca",
    "category": "Facilities",
    "score_category": "8.4",
    "hotel": "Hostal Mariscal Inn & Suite",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 236,
    "province": "Cuenca",
    "category": "Cleanliness",
    "score_category": "8.9",
    "hotel": "Hostal Mariscal Inn & Suite",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 237,
    "province": "Cuenca",
    "category": "Comfort",
    "score_category": "8.6",
    "hotel": "Hostal Mariscal Inn & Suite",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 238,
    "province": "Cuenca",
    "category": "Value for money",
    "score_category": "8.8",
    "hotel": "Hostal Mariscal Inn & Suite",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 239,
    "province": "Cuenca",
    "category": "Location",
    "score_category": "8.9",
    "hotel": "Hostal Mariscal Inn & Suite",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 240,
    "province": "Cuenca",
    "category": "Free WiFi",
    "score_category": "7.5",
    "hotel": "Hostal Mariscal Inn & Suite",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 241,
    "province": "Cuenca",
    "category": "Staff",
    "score_category": "9.3",
    "hotel": "Villa Emilia Hostal",
    "score_hotel": "9.4",
        }
    )
  batch.put_item(
  Item={
    "id": 242,
    "province": "Cuenca",
    "category": "Facilities",
    "score_category": "9.5",
    "hotel": "Villa Emilia Hostal",
    "score_hotel": "9.4",
        }
    )
  batch.put_item(
  Item={
    "id": 243,
    "province": "Cuenca",
    "category": "Cleanliness",
    "score_category": "9.6",
    "hotel": "Villa Emilia Hostal",
    "score_hotel": "9.4",
        }
    )
  batch.put_item(
  Item={
    "id": 244,
    "province": "Cuenca",
    "category": "Comfort",
    "score_category": "9.6",
    "hotel": "Villa Emilia Hostal",
    "score_hotel": "9.4",
        }
    )
  batch.put_item(
  Item={
    "id": 245,
    "province": "Cuenca",
    "category": "Value for money",
    "score_category": "9.5",
    "hotel": "Villa Emilia Hostal",
    "score_hotel": "9.4",
        }
    )
  batch.put_item(
  Item={
    "id": 246,
    "province": "Cuenca",
    "category": "Location",
    "score_category": "9.6",
    "hotel": "Villa Emilia Hostal",
    "score_hotel": "9.4",
        }
    )
  batch.put_item(
  Item={
    "id": 247,
    "province": "Cuenca",
    "category": "Free WiFi",
    "score_category": "8.9",
    "hotel": "Villa Emilia Hostal",
    "score_hotel": "9.4",
        }
    )
  batch.put_item(
  Item={
    "id": 248,
    "province": "Cuenca",
    "category": "Staff",
    "score_category": "8.9",
    "hotel": "Morenica del Rosario",
    "score_hotel": "8.5",
        }
    )
  batch.put_item(
  Item={
    "id": 249,
    "province": "Cuenca",
    "category": "Facilities",
    "score_category": "8.5",
    "hotel": "Morenica del Rosario",
    "score_hotel": "8.5",
        }
    )
  batch.put_item(
  Item={
    "id": 250,
    "province": "Cuenca",
    "category": "Cleanliness",
    "score_category": "9",
    "hotel": "Morenica del Rosario",
    "score_hotel": "8.5",
        }
    )
  batch.put_item(
  Item={
    "id": 251,
    "province": "Cuenca",
    "category": "Comfort",
    "score_category": "8.9",
    "hotel": "Morenica del Rosario",
    "score_hotel": "8.5",
        }
    )
  batch.put_item(
  Item={
    "id": 252,
    "province": "Cuenca",
    "category": "Value for money",
    "score_category": "8.7",
    "hotel": "Morenica del Rosario",
    "score_hotel": "8.5",
        }
    )
  batch.put_item(
  Item={
    "id": 253,
    "province": "Cuenca",
    "category": "Location",
    "score_category": "9.5",
    "hotel": "Morenica del Rosario",
    "score_hotel": "8.5",
        }
    )
  batch.put_item(
  Item={
    "id": 254,
    "province": "Cuenca",
    "category": "Free WiFi",
    "score_category": "5.8",
    "hotel": "Morenica del Rosario",
    "score_hotel": "8.5",
        }
    )
  batch.put_item(
  Item={
    "id": 255,
    "province": "Cuenca",
    "category": "Staff",
    "score_category": "9.3",
    "hotel": "Four Points by Sheraton Cuenca",
    "score_hotel": "9",
        }
    )
  batch.put_item(
  Item={
    "id": 256,
    "province": "Cuenca",
    "category": "Facilities",
    "score_category": "9.2",
    "hotel": "Four Points by Sheraton Cuenca",
    "score_hotel": "9",
        }
    )
  batch.put_item(
  Item={
    "id": 257,
    "province": "Cuenca",
    "category": "Cleanliness",
    "score_category": "9.3",
    "hotel": "Four Points by Sheraton Cuenca",
    "score_hotel": "9",
        }
    )
  batch.put_item(
  Item={
    "id": 258,
    "province": "Cuenca",
    "category": "Comfort",
    "score_category": "9.3",
    "hotel": "Four Points by Sheraton Cuenca",
    "score_hotel": "9",
        }
    )
  batch.put_item(
  Item={
    "id": 259,
    "province": "Cuenca",
    "category": "Value for money",
    "score_category": "8.8",
    "hotel": "Four Points by Sheraton Cuenca",
    "score_hotel": "9",
        }
    )
  batch.put_item(
  Item={
    "id": 260,
    "province": "Cuenca",
    "category": "Location",
    "score_category": "9",
    "hotel": "Four Points by Sheraton Cuenca",
    "score_hotel": "9",
        }
    )
  batch.put_item(
  Item={
    "id": 261,
    "province": "Cuenca",
    "category": "Free WiFi",
    "score_category": "8.4",
    "hotel": "Four Points by Sheraton Cuenca",
    "score_hotel": "9",
        }
    )
  batch.put_item(
  Item={
    "id": 262,
    "province": "Cuenca",
    "category": "Staff",
    "score_category": "8.5",
    "hotel": "Hotel Nass Pinar del Lago",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 263,
    "province": "Cuenca",
    "category": "Facilities",
    "score_category": "8.4",
    "hotel": "Hotel Nass Pinar del Lago",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 264,
    "province": "Cuenca",
    "category": "Cleanliness",
    "score_category": "8.8",
    "hotel": "Hotel Nass Pinar del Lago",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 265,
    "province": "Cuenca",
    "category": "Comfort",
    "score_category": "8.8",
    "hotel": "Hotel Nass Pinar del Lago",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 266,
    "province": "Cuenca",
    "category": "Value for money",
    "score_category": "8.8",
    "hotel": "Hotel Nass Pinar del Lago",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 267,
    "province": "Cuenca",
    "category": "Location",
    "score_category": "9",
    "hotel": "Hotel Nass Pinar del Lago",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 268,
    "province": "Cuenca",
    "category": "Free WiFi",
    "score_category": "7.9",
    "hotel": "Hotel Nass Pinar del Lago",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 269,
    "province": "Cuenca",
    "category": "Staff",
    "score_category": "8.9",
    "hotel": "Hosteria Dos Chorreras",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 270,
    "province": "Cuenca",
    "category": "Facilities",
    "score_category": "9.2",
    "hotel": "Hosteria Dos Chorreras",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 271,
    "province": "Cuenca",
    "category": "Cleanliness",
    "score_category": "9.3",
    "hotel": "Hosteria Dos Chorreras",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 272,
    "province": "Cuenca",
    "category": "Comfort",
    "score_category": "9.2",
    "hotel": "Hosteria Dos Chorreras",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 273,
    "province": "Cuenca",
    "category": "Value for money",
    "score_category": "8.5",
    "hotel": "Hosteria Dos Chorreras",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 274,
    "province": "Cuenca",
    "category": "Location",
    "score_category": "9.2",
    "hotel": "Hosteria Dos Chorreras",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 275,
    "province": "Cuenca",
    "category": "Free WiFi",
    "score_category": "7.4",
    "hotel": "Hosteria Dos Chorreras",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 276,
    "province": "Cuenca",
    "category": "Staff",
    "score_category": "9.3",
    "hotel": "Guesthouse Bella Vista",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 277,
    "province": "Cuenca",
    "category": "Facilities",
    "score_category": "9",
    "hotel": "Guesthouse Bella Vista",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 278,
    "province": "Cuenca",
    "category": "Cleanliness",
    "score_category": "9",
    "hotel": "Guesthouse Bella Vista",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 279,
    "province": "Cuenca",
    "category": "Comfort",
    "score_category": "9",
    "hotel": "Guesthouse Bella Vista",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 280,
    "province": "Cuenca",
    "category": "Value for money",
    "score_category": "9.3",
    "hotel": "Guesthouse Bella Vista",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 281,
    "province": "Cuenca",
    "category": "Location",
    "score_category": "8.5",
    "hotel": "Guesthouse Bella Vista",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 282,
    "province": "Cuenca",
    "category": "Free WiFi",
    "score_category": "9",
    "hotel": "Guesthouse Bella Vista",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 283,
    "province": "Cuenca",
    "category": "Staff",
    "score_category": "9.9",
    "hotel": "Itza Hotel Boutique Internacional",
    "score_hotel": "9.3",
        }
    )
  batch.put_item(
  Item={
    "id": 284,
    "province": "Cuenca",
    "category": "Facilities",
    "score_category": "9.5",
    "hotel": "Itza Hotel Boutique Internacional",
    "score_hotel": "9.3",
        }
    )
  batch.put_item(
  Item={
    "id": 285,
    "province": "Cuenca",
    "category": "Cleanliness",
    "score_category": "9.8",
    "hotel": "Itza Hotel Boutique Internacional",
    "score_hotel": "9.3",
        }
    )
  batch.put_item(
  Item={
    "id": 286,
    "province": "Cuenca",
    "category": "Comfort",
    "score_category": "9.6",
    "hotel": "Itza Hotel Boutique Internacional",
    "score_hotel": "9.3",
        }
    )
  batch.put_item(
  Item={
    "id": 287,
    "province": "Cuenca",
    "category": "Value for money",
    "score_category": "9",
    "hotel": "Itza Hotel Boutique Internacional",
    "score_hotel": "9.3",
        }
    )
  batch.put_item(
  Item={
    "id": 288,
    "province": "Cuenca",
    "category": "Location",
    "score_category": "9.7",
    "hotel": "Itza Hotel Boutique Internacional",
    "score_hotel": "9.3",
        }
    )
  batch.put_item(
  Item={
    "id": 289,
    "province": "Cuenca",
    "category": "Free WiFi",
    "score_category": "9.2",
    "hotel": "Itza Hotel Boutique Internacional",
    "score_hotel": "9.3",
        }
    )
  batch.put_item(
  Item={
    "id": 290,
    "province": "Cuenca",
    "category": "Staff",
    "score_category": "9.3",
    "hotel": "Hostal Casa de Lidice",
    "score_hotel": "9.1",
        }
    )
  batch.put_item(
  Item={
    "id": 291,
    "province": "Cuenca",
    "category": "Facilities",
    "score_category": "9.1",
    "hotel": "Hostal Casa de Lidice",
    "score_hotel": "9.1",
        }
    )
  batch.put_item(
  Item={
    "id": 292,
    "province": "Cuenca",
    "category": "Cleanliness",
    "score_category": "9.5",
    "hotel": "Hostal Casa de Lidice",
    "score_hotel": "9.1",
        }
    )
  batch.put_item(
  Item={
    "id": 293,
    "province": "Cuenca",
    "category": "Comfort",
    "score_category": "9.3",
    "hotel": "Hostal Casa de Lidice",
    "score_hotel": "9.1",
        }
    )
  batch.put_item(
  Item={
    "id": 294,
    "province": "Cuenca",
    "category": "Value for money",
    "score_category": "9.1",
    "hotel": "Hostal Casa de Lidice",
    "score_hotel": "9.1",
        }
    )
  batch.put_item(
  Item={
    "id": 295,
    "province": "Cuenca",
    "category": "Location",
    "score_category": "9.3",
    "hotel": "Hostal Casa de Lidice",
    "score_hotel": "9.1",
        }
    )
  batch.put_item(
  Item={
    "id": 296,
    "province": "Cuenca",
    "category": "Free WiFi",
    "score_category": "6.2",
    "hotel": "Hostal Casa de Lidice",
    "score_hotel": "9.1",
        }
    )
  batch.put_item(
  Item={
    "id": 297,
    "province": "Cuenca",
    "category": "Staff",
    "score_category": "9.5",
    "hotel": "Apartamentos Otorongo Cuenca Ecuador",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 298,
    "province": "Cuenca",
    "category": "Facilities",
    "score_category": "9",
    "hotel": "Apartamentos Otorongo Cuenca Ecuador",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 299,
    "province": "Cuenca",
    "category": "Cleanliness",
    "score_category": "9.1",
    "hotel": "Apartamentos Otorongo Cuenca Ecuador",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 300,
    "province": "Cuenca",
    "category": "Comfort",
    "score_category": "8.9",
    "hotel": "Apartamentos Otorongo Cuenca Ecuador",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 301,
    "province": "Cuenca",
    "category": "Value for money",
    "score_category": "8.9",
    "hotel": "Apartamentos Otorongo Cuenca Ecuador",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 302,
    "province": "Cuenca",
    "category": "Location",
    "score_category": "9.5",
    "hotel": "Apartamentos Otorongo Cuenca Ecuador",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 303,
    "province": "Cuenca",
    "category": "Free WiFi",
    "score_category": "9.4",
    "hotel": "Apartamentos Otorongo Cuenca Ecuador",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 304,
    "province": "Cuenca",
    "category": "Staff",
    "score_category": "9.2",
    "hotel": "El Dorado Hotel",
    "score_hotel": "9",
        }
    )
  batch.put_item(
  Item={
    "id": 305,
    "province": "Cuenca",
    "category": "Facilities",
    "score_category": "9",
    "hotel": "El Dorado Hotel",
    "score_hotel": "9",
        }
    )
  batch.put_item(
  Item={
    "id": 306,
    "province": "Cuenca",
    "category": "Cleanliness",
    "score_category": "9.3",
    "hotel": "El Dorado Hotel",
    "score_hotel": "9",
        }
    )
  batch.put_item(
  Item={
    "id": 307,
    "province": "Cuenca",
    "category": "Comfort",
    "score_category": "9.4",
    "hotel": "El Dorado Hotel",
    "score_hotel": "9",
        }
    )
  batch.put_item(
  Item={
    "id": 308,
    "province": "Cuenca",
    "category": "Value for money",
    "score_category": "8.8",
    "hotel": "El Dorado Hotel",
    "score_hotel": "9",
        }
    )
  batch.put_item(
  Item={
    "id": 309,
    "province": "Cuenca",
    "category": "Location",
    "score_category": "9.5",
    "hotel": "El Dorado Hotel",
    "score_hotel": "9",
        }
    )
  batch.put_item(
  Item={
    "id": 310,
    "province": "Cuenca",
    "category": "Free WiFi",
    "score_category": "8.9",
    "hotel": "El Dorado Hotel",
    "score_hotel": "9",
        }
    )
  batch.put_item(
  Item={
    "id": 311,
    "province": "Cuenca",
    "category": "Staff",
    "score_category": "8.4",
    "hotel": "Check Inn Bed and Breakfast",
    "score_hotel": "7.7",
        }
    )
  batch.put_item(
  Item={
    "id": 312,
    "province": "Cuenca",
    "category": "Facilities",
    "score_category": "7.4",
    "hotel": "Check Inn Bed and Breakfast",
    "score_hotel": "7.7",
        }
    )
  batch.put_item(
  Item={
    "id": 313,
    "province": "Cuenca",
    "category": "Cleanliness",
    "score_category": "8",
    "hotel": "Check Inn Bed and Breakfast",
    "score_hotel": "7.7",
        }
    )
  batch.put_item(
  Item={
    "id": 314,
    "province": "Cuenca",
    "category": "Comfort",
    "score_category": "7.7",
    "hotel": "Check Inn Bed and Breakfast",
    "score_hotel": "7.7",
        }
    )
  batch.put_item(
  Item={
    "id": 315,
    "province": "Cuenca",
    "category": "Value for money",
    "score_category": "8.4",
    "hotel": "Check Inn Bed and Breakfast",
    "score_hotel": "7.7",
        }
    )
  batch.put_item(
  Item={
    "id": 316,
    "province": "Cuenca",
    "category": "Location",
    "score_category": "9.5",
    "hotel": "Check Inn Bed and Breakfast",
    "score_hotel": "7.7",
        }
    )
  batch.put_item(
  Item={
    "id": 317,
    "province": "Cuenca",
    "category": "Free WiFi",
    "score_category": "7.3",
    "hotel": "Check Inn Bed and Breakfast",
    "score_hotel": "7.7",
        }
    )
  batch.put_item(
  Item={
    "id": 318,
    "province": "Cuenca",
    "category": "Staff",
    "score_category": "9",
    "hotel": "Hotel Valgus",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 319,
    "province": "Cuenca",
    "category": "Facilities",
    "score_category": "8.9",
    "hotel": "Hotel Valgus",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 320,
    "province": "Cuenca",
    "category": "Cleanliness",
    "score_category": "9.1",
    "hotel": "Hotel Valgus",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 321,
    "province": "Cuenca",
    "category": "Comfort",
    "score_category": "9.2",
    "hotel": "Hotel Valgus",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 322,
    "province": "Cuenca",
    "category": "Value for money",
    "score_category": "8.6",
    "hotel": "Hotel Valgus",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 323,
    "province": "Cuenca",
    "category": "Location",
    "score_category": "9.4",
    "hotel": "Hotel Valgus",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 324,
    "province": "Cuenca",
    "category": "Free WiFi",
    "score_category": "6.5",
    "hotel": "Hotel Valgus",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 325,
    "province": "Cuenca",
    "category": "Staff",
    "score_category": "8.3",
    "hotel": "Hotel Spa Santa Ana",
    "score_hotel": "7.5",
        }
    )
  batch.put_item(
  Item={
    "id": 326,
    "province": "Cuenca",
    "category": "Facilities",
    "score_category": "7.5",
    "hotel": "Hotel Spa Santa Ana",
    "score_hotel": "7.5",
        }
    )
  batch.put_item(
  Item={
    "id": 327,
    "province": "Cuenca",
    "category": "Cleanliness",
    "score_category": "8",
    "hotel": "Hotel Spa Santa Ana",
    "score_hotel": "7.5",
        }
    )
  batch.put_item(
  Item={
    "id": 328,
    "province": "Cuenca",
    "category": "Comfort",
    "score_category": "7.9",
    "hotel": "Hotel Spa Santa Ana",
    "score_hotel": "7.5",
        }
    )
  batch.put_item(
  Item={
    "id": 329,
    "province": "Cuenca",
    "category": "Value for money",
    "score_category": "7.6",
    "hotel": "Hotel Spa Santa Ana",
    "score_hotel": "7.5",
        }
    )
  batch.put_item(
  Item={
    "id": 330,
    "province": "Cuenca",
    "category": "Location",
    "score_category": "9",
    "hotel": "Hotel Spa Santa Ana",
    "score_hotel": "7.5",
        }
    )
  batch.put_item(
  Item={
    "id": 331,
    "province": "Cuenca",
    "category": "Free WiFi",
    "score_category": "7.5",
    "hotel": "Hotel Spa Santa Ana",
    "score_hotel": "7.5",
        }
    )
  batch.put_item(
  Item={
    "id": 332,
    "province": "Quito",
    "category": "Staff",
    "score_category": "9.3",
    "hotel": "Hotel David",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 333,
    "province": "Quito",
    "category": "Facilities",
    "score_category": "8.6",
    "hotel": "Hotel David",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 334,
    "province": "Quito",
    "category": "Cleanliness",
    "score_category": "8.9",
    "hotel": "Hotel David",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 335,
    "province": "Quito",
    "category": "Comfort",
    "score_category": "8.8",
    "hotel": "Hotel David",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 336,
    "province": "Quito",
    "category": "Value for money",
    "score_category": "9",
    "hotel": "Hotel David",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 337,
    "province": "Quito",
    "category": "Location",
    "score_category": "8.8",
    "hotel": "Hotel David",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 338,
    "province": "Quito",
    "category": "Free WiFi",
    "score_category": "8.6",
    "hotel": "Hotel David",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 339,
    "province": "Quito",
    "category": "Staff",
    "score_category": "9.3",
    "hotel": "Rincón Familiar Hostel Boutique",
    "score_hotel": "8.3",
        }
    )
  batch.put_item(
  Item={
    "id": 340,
    "province": "Quito",
    "category": "Facilities",
    "score_category": "8.1",
    "hotel": "Rincón Familiar Hostel Boutique",
    "score_hotel": "8.3",
        }
    )
  batch.put_item(
  Item={
    "id": 341,
    "province": "Quito",
    "category": "Cleanliness",
    "score_category": "8.6",
    "hotel": "Rincón Familiar Hostel Boutique",
    "score_hotel": "8.3",
        }
    )
  batch.put_item(
  Item={
    "id": 342,
    "province": "Quito",
    "category": "Comfort",
    "score_category": "8.5",
    "hotel": "Rincón Familiar Hostel Boutique",
    "score_hotel": "8.3",
        }
    )
  batch.put_item(
  Item={
    "id": 343,
    "province": "Quito",
    "category": "Value for money",
    "score_category": "8.6",
    "hotel": "Rincón Familiar Hostel Boutique",
    "score_hotel": "8.3",
        }
    )
  batch.put_item(
  Item={
    "id": 344,
    "province": "Quito",
    "category": "Location",
    "score_category": "9.1",
    "hotel": "Rincón Familiar Hostel Boutique",
    "score_hotel": "8.3",
        }
    )
  batch.put_item(
  Item={
    "id": 345,
    "province": "Quito",
    "category": "Free WiFi",
    "score_category": "8.6",
    "hotel": "Rincón Familiar Hostel Boutique",
    "score_hotel": "8.3",
        }
    )
  batch.put_item(
  Item={
    "id": 346,
    "province": "Quito",
    "category": "Staff",
    "score_category": "9.2",
    "hotel": "Boutique Hotel Antinea",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 347,
    "province": "Quito",
    "category": "Facilities",
    "score_category": "8.9",
    "hotel": "Boutique Hotel Antinea",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 348,
    "province": "Quito",
    "category": "Cleanliness",
    "score_category": "9.1",
    "hotel": "Boutique Hotel Antinea",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 349,
    "province": "Quito",
    "category": "Comfort",
    "score_category": "9",
    "hotel": "Boutique Hotel Antinea",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 350,
    "province": "Quito",
    "category": "Value for money",
    "score_category": "8.9",
    "hotel": "Boutique Hotel Antinea",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 351,
    "province": "Quito",
    "category": "Location",
    "score_category": "9.2",
    "hotel": "Boutique Hotel Antinea",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 352,
    "province": "Quito",
    "category": "Free WiFi",
    "score_category": "8.6",
    "hotel": "Boutique Hotel Antinea",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 353,
    "province": "Quito",
    "category": "Staff",
    "score_category": "9",
    "hotel": "Hotel Bellavista Quito",
    "score_hotel": "8.1",
        }
    )
  batch.put_item(
  Item={
    "id": 354,
    "province": "Quito",
    "category": "Facilities",
    "score_category": "8",
    "hotel": "Hotel Bellavista Quito",
    "score_hotel": "8.1",
        }
    )
  batch.put_item(
  Item={
    "id": 355,
    "province": "Quito",
    "category": "Cleanliness",
    "score_category": "8.5",
    "hotel": "Hotel Bellavista Quito",
    "score_hotel": "8.1",
        }
    )
  batch.put_item(
  Item={
    "id": 356,
    "province": "Quito",
    "category": "Comfort",
    "score_category": "8.4",
    "hotel": "Hotel Bellavista Quito",
    "score_hotel": "8.1",
        }
    )
  batch.put_item(
  Item={
    "id": 357,
    "province": "Quito",
    "category": "Value for money",
    "score_category": "8.2",
    "hotel": "Hotel Bellavista Quito",
    "score_hotel": "8.1",
        }
    )
  batch.put_item(
  Item={
    "id": 358,
    "province": "Quito",
    "category": "Location",
    "score_category": "8.6",
    "hotel": "Hotel Bellavista Quito",
    "score_hotel": "8.1",
        }
    )
  batch.put_item(
  Item={
    "id": 359,
    "province": "Quito",
    "category": "Free WiFi",
    "score_category": "8.7",
    "hotel": "Hotel Bellavista Quito",
    "score_hotel": "8.1",
        }
    )
  batch.put_item(
  Item={
    "id": 360,
    "province": "Quito",
    "category": "Staff",
    "score_category": "9.1",
    "hotel": "Hotel Bernys Estrellita",
    "score_hotel": "7.7",
        }
    )
  batch.put_item(
  Item={
    "id": 361,
    "province": "Quito",
    "category": "Facilities",
    "score_category": "7.8",
    "hotel": "Hotel Bernys Estrellita",
    "score_hotel": "7.7",
        }
    )
  batch.put_item(
  Item={
    "id": 362,
    "province": "Quito",
    "category": "Cleanliness",
    "score_category": "8.4",
    "hotel": "Hotel Bernys Estrellita",
    "score_hotel": "7.7",
        }
    )
  batch.put_item(
  Item={
    "id": 363,
    "province": "Quito",
    "category": "Comfort",
    "score_category": "8",
    "hotel": "Hotel Bernys Estrellita",
    "score_hotel": "7.7",
        }
    )
  batch.put_item(
  Item={
    "id": 364,
    "province": "Quito",
    "category": "Value for money",
    "score_category": "8.5",
    "hotel": "Hotel Bernys Estrellita",
    "score_hotel": "7.7",
        }
    )
  batch.put_item(
  Item={
    "id": 365,
    "province": "Quito",
    "category": "Location",
    "score_category": "8.2",
    "hotel": "Hotel Bernys Estrellita",
    "score_hotel": "7.7",
        }
    )
  batch.put_item(
  Item={
    "id": 366,
    "province": "Quito",
    "category": "Free WiFi",
    "score_category": "5.8",
    "hotel": "Hotel Bernys Estrellita",
    "score_hotel": "7.7",
        }
    )
  batch.put_item(
  Item={
    "id": 367,
    "province": "Quito",
    "category": "Staff",
    "score_category": "9.3",
    "hotel": "Wyndham Garden Quito",
    "score_hotel": "9",
        }
    )
  batch.put_item(
  Item={
    "id": 368,
    "province": "Quito",
    "category": "Facilities",
    "score_category": "8.9",
    "hotel": "Wyndham Garden Quito",
    "score_hotel": "9",
        }
    )
  batch.put_item(
  Item={
    "id": 369,
    "province": "Quito",
    "category": "Cleanliness",
    "score_category": "9.3",
    "hotel": "Wyndham Garden Quito",
    "score_hotel": "9",
        }
    )
  batch.put_item(
  Item={
    "id": 370,
    "province": "Quito",
    "category": "Comfort",
    "score_category": "9.3",
    "hotel": "Wyndham Garden Quito",
    "score_hotel": "9",
        }
    )
  batch.put_item(
  Item={
    "id": 371,
    "province": "Quito",
    "category": "Value for money",
    "score_category": "8.8",
    "hotel": "Wyndham Garden Quito",
    "score_hotel": "9",
        }
    )
  batch.put_item(
  Item={
    "id": 372,
    "province": "Quito",
    "category": "Location",
    "score_category": "9.4",
    "hotel": "Wyndham Garden Quito",
    "score_hotel": "9",
        }
    )
  batch.put_item(
  Item={
    "id": 373,
    "province": "Quito",
    "category": "Free WiFi",
    "score_category": "8.9",
    "hotel": "Wyndham Garden Quito",
    "score_hotel": "9",
        }
    )
  batch.put_item(
  Item={
    "id": 374,
    "province": "Quito",
    "category": "Staff",
    "score_category": "9.8",
    "hotel": "Posada Tambuca",
    "score_hotel": "9.4",
        }
    )
  batch.put_item(
  Item={
    "id": 375,
    "province": "Quito",
    "category": "Facilities",
    "score_category": "9.2",
    "hotel": "Posada Tambuca",
    "score_hotel": "9.4",
        }
    )
  batch.put_item(
  Item={
    "id": 376,
    "province": "Quito",
    "category": "Cleanliness",
    "score_category": "9.5",
    "hotel": "Posada Tambuca",
    "score_hotel": "9.4",
        }
    )
  batch.put_item(
  Item={
    "id": 377,
    "province": "Quito",
    "category": "Comfort",
    "score_category": "9.3",
    "hotel": "Posada Tambuca",
    "score_hotel": "9.4",
        }
    )
  batch.put_item(
  Item={
    "id": 378,
    "province": "Quito",
    "category": "Value for money",
    "score_category": "9.5",
    "hotel": "Posada Tambuca",
    "score_hotel": "9.4",
        }
    )
  batch.put_item(
  Item={
    "id": 379,
    "province": "Quito",
    "category": "Location",
    "score_category": "9.3",
    "hotel": "Posada Tambuca",
    "score_hotel": "9.4",
        }
    )
  batch.put_item(
  Item={
    "id": 380,
    "province": "Quito",
    "category": "Free WiFi",
    "score_category": "9.6",
    "hotel": "Posada Tambuca",
    "score_hotel": "9.4",
        }
    )
  batch.put_item(
  Item={
    "id": 381,
    "province": "Quito",
    "category": "Staff",
    "score_category": "9.4",
    "hotel": "Hostal Yumbo Imperial",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 382,
    "province": "Quito",
    "category": "Facilities",
    "score_category": "8",
    "hotel": "Hostal Yumbo Imperial",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 383,
    "province": "Quito",
    "category": "Cleanliness",
    "score_category": "8.3",
    "hotel": "Hostal Yumbo Imperial",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 384,
    "province": "Quito",
    "category": "Comfort",
    "score_category": "8.1",
    "hotel": "Hostal Yumbo Imperial",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 385,
    "province": "Quito",
    "category": "Value for money",
    "score_category": "9.1",
    "hotel": "Hostal Yumbo Imperial",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 386,
    "province": "Quito",
    "category": "Location",
    "score_category": "9.5",
    "hotel": "Hostal Yumbo Imperial",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 387,
    "province": "Quito",
    "category": "Free WiFi",
    "score_category": "8.1",
    "hotel": "Hostal Yumbo Imperial",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 388,
    "province": "Quito",
    "category": "Staff",
    "score_category": "9.2",
    "hotel": "Hotel Reina Isabel",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 389,
    "province": "Quito",
    "category": "Facilities",
    "score_category": "9",
    "hotel": "Hotel Reina Isabel",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 390,
    "province": "Quito",
    "category": "Cleanliness",
    "score_category": "9.3",
    "hotel": "Hotel Reina Isabel",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 391,
    "province": "Quito",
    "category": "Comfort",
    "score_category": "9.2",
    "hotel": "Hotel Reina Isabel",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 392,
    "province": "Quito",
    "category": "Value for money",
    "score_category": "8.9",
    "hotel": "Hotel Reina Isabel",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 393,
    "province": "Quito",
    "category": "Location",
    "score_category": "8.8",
    "hotel": "Hotel Reina Isabel",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 394,
    "province": "Quito",
    "category": "Free WiFi",
    "score_category": "8.4",
    "hotel": "Hotel Reina Isabel",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 395,
    "province": "Quito",
    "category": "Staff",
    "score_category": "9.9",
    "hotel": "Hotel Casona 1914",
    "score_hotel": "9.7",
        }
    )
  batch.put_item(
  Item={
    "id": 396,
    "province": "Quito",
    "category": "Facilities",
    "score_category": "9.7",
    "hotel": "Hotel Casona 1914",
    "score_hotel": "9.7",
        }
    )
  batch.put_item(
  Item={
    "id": 397,
    "province": "Quito",
    "category": "Cleanliness",
    "score_category": "9.8",
    "hotel": "Hotel Casona 1914",
    "score_hotel": "9.7",
        }
    )
  batch.put_item(
  Item={
    "id": 398,
    "province": "Quito",
    "category": "Comfort",
    "score_category": "9.8",
    "hotel": "Hotel Casona 1914",
    "score_hotel": "9.7",
        }
    )
  batch.put_item(
  Item={
    "id": 399,
    "province": "Quito",
    "category": "Value for money",
    "score_category": "9.7",
    "hotel": "Hotel Casona 1914",
    "score_hotel": "9.7",
        }
    )
  batch.put_item(
  Item={
    "id": 400,
    "province": "Quito",
    "category": "Location",
    "score_category": "9.1",
    "hotel": "Hotel Casona 1914",
    "score_hotel": "9.7",
        }
    )
  batch.put_item(
  Item={
    "id": 401,
    "province": "Quito",
    "category": "Free WiFi",
    "score_category": "9.3",
    "hotel": "Hotel Casona 1914",
    "score_hotel": "9.7",
        }
    )
  batch.put_item(
  Item={
    "id": 402,
    "province": "Quito",
    "category": "Staff",
    "score_category": "8.8",
    "hotel": "Hostal Juana de Arco",
    "score_hotel": "8.3",
        }
    )
  batch.put_item(
  Item={
    "id": 403,
    "province": "Quito",
    "category": "Facilities",
    "score_category": "8.1",
    "hotel": "Hostal Juana de Arco",
    "score_hotel": "8.3",
        }
    )
  batch.put_item(
  Item={
    "id": 404,
    "province": "Quito",
    "category": "Cleanliness",
    "score_category": "8.7",
    "hotel": "Hostal Juana de Arco",
    "score_hotel": "8.3",
        }
    )
  batch.put_item(
  Item={
    "id": 405,
    "province": "Quito",
    "category": "Comfort",
    "score_category": "8.3",
    "hotel": "Hostal Juana de Arco",
    "score_hotel": "8.3",
        }
    )
  batch.put_item(
  Item={
    "id": 406,
    "province": "Quito",
    "category": "Value for money",
    "score_category": "9.1",
    "hotel": "Hostal Juana de Arco",
    "score_hotel": "8.3",
        }
    )
  batch.put_item(
  Item={
    "id": 407,
    "province": "Quito",
    "category": "Location",
    "score_category": "9.2",
    "hotel": "Hostal Juana de Arco",
    "score_hotel": "8.3",
        }
    )
  batch.put_item(
  Item={
    "id": 408,
    "province": "Quito",
    "category": "Free WiFi",
    "score_category": "8.9",
    "hotel": "Hostal Juana de Arco",
    "score_hotel": "8.3",
        }
    )
  batch.put_item(
  Item={
    "id": 409,
    "province": "Quito",
    "category": "Staff",
    "score_category": "9",
    "hotel": "ibis Quito",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 410,
    "province": "Quito",
    "category": "Facilities",
    "score_category": "9",
    "hotel": "ibis Quito",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 411,
    "province": "Quito",
    "category": "Cleanliness",
    "score_category": "9.3",
    "hotel": "ibis Quito",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 412,
    "province": "Quito",
    "category": "Comfort",
    "score_category": "9.1",
    "hotel": "ibis Quito",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 413,
    "province": "Quito",
    "category": "Value for money",
    "score_category": "8.9",
    "hotel": "ibis Quito",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 414,
    "province": "Quito",
    "category": "Location",
    "score_category": "9.3",
    "hotel": "ibis Quito",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 415,
    "province": "Quito",
    "category": "Free WiFi",
    "score_category": "8.8",
    "hotel": "ibis Quito",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 416,
    "province": "Quito",
    "category": "Staff",
    "score_category": "9.5",
    "hotel": "ArtPlaza",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 417,
    "province": "Quito",
    "category": "Facilities",
    "score_category": "8.6",
    "hotel": "ArtPlaza",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 418,
    "province": "Quito",
    "category": "Cleanliness",
    "score_category": "9.1",
    "hotel": "ArtPlaza",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 419,
    "province": "Quito",
    "category": "Comfort",
    "score_category": "8.9",
    "hotel": "ArtPlaza",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 420,
    "province": "Quito",
    "category": "Value for money",
    "score_category": "8.8",
    "hotel": "ArtPlaza",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 421,
    "province": "Quito",
    "category": "Location",
    "score_category": "8.9",
    "hotel": "ArtPlaza",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 422,
    "province": "Quito",
    "category": "Free WiFi",
    "score_category": "9",
    "hotel": "ArtPlaza",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 423,
    "province": "Quito",
    "category": "Staff",
    "score_category": "8.9",
    "hotel": "ITSAHOME Apartments Torre Seis",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 424,
    "province": "Quito",
    "category": "Facilities",
    "score_category": "8.7",
    "hotel": "ITSAHOME Apartments Torre Seis",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 425,
    "province": "Quito",
    "category": "Cleanliness",
    "score_category": "9",
    "hotel": "ITSAHOME Apartments Torre Seis",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 426,
    "province": "Quito",
    "category": "Comfort",
    "score_category": "9",
    "hotel": "ITSAHOME Apartments Torre Seis",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 427,
    "province": "Quito",
    "category": "Value for money",
    "score_category": "8.9",
    "hotel": "ITSAHOME Apartments Torre Seis",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 428,
    "province": "Quito",
    "category": "Location",
    "score_category": "9.1",
    "hotel": "ITSAHOME Apartments Torre Seis",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 429,
    "province": "Quito",
    "category": "Free WiFi",
    "score_category": "8",
    "hotel": "ITSAHOME Apartments Torre Seis",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 430,
    "province": "Quito",
    "category": "Staff",
    "score_category": "9.7",
    "hotel": "Vista del Angel Hotel Boutique",
    "score_hotel": "9.3",
        }
    )
  batch.put_item(
  Item={
    "id": 431,
    "province": "Quito",
    "category": "Facilities",
    "score_category": "9.4",
    "hotel": "Vista del Angel Hotel Boutique",
    "score_hotel": "9.3",
        }
    )
  batch.put_item(
  Item={
    "id": 432,
    "province": "Quito",
    "category": "Cleanliness",
    "score_category": "9.6",
    "hotel": "Vista del Angel Hotel Boutique",
    "score_hotel": "9.3",
        }
    )
  batch.put_item(
  Item={
    "id": 433,
    "province": "Quito",
    "category": "Comfort",
    "score_category": "9.6",
    "hotel": "Vista del Angel Hotel Boutique",
    "score_hotel": "9.3",
        }
    )
  batch.put_item(
  Item={
    "id": 434,
    "province": "Quito",
    "category": "Value for money",
    "score_category": "9.2",
    "hotel": "Vista del Angel Hotel Boutique",
    "score_hotel": "9.3",
        }
    )
  batch.put_item(
  Item={
    "id": 435,
    "province": "Quito",
    "category": "Location",
    "score_category": "9",
    "hotel": "Vista del Angel Hotel Boutique",
    "score_hotel": "9.3",
        }
    )
  batch.put_item(
  Item={
    "id": 436,
    "province": "Quito",
    "category": "Free WiFi",
    "score_category": "9.5",
    "hotel": "Vista del Angel Hotel Boutique",
    "score_hotel": "9.3",
        }
    )
  batch.put_item(
  Item={
    "id": 437,
    "province": "Quito",
    "category": "Staff",
    "score_category": "9.2",
    "hotel": "Hotel Huasi Continental",
    "score_hotel": "8.2",
        }
    )
  batch.put_item(
  Item={
    "id": 438,
    "province": "Quito",
    "category": "Facilities",
    "score_category": "8",
    "hotel": "Hotel Huasi Continental",
    "score_hotel": "8.2",
        }
    )
  batch.put_item(
  Item={
    "id": 439,
    "province": "Quito",
    "category": "Cleanliness",
    "score_category": "8.5",
    "hotel": "Hotel Huasi Continental",
    "score_hotel": "8.2",
        }
    )
  batch.put_item(
  Item={
    "id": 440,
    "province": "Quito",
    "category": "Comfort",
    "score_category": "8.4",
    "hotel": "Hotel Huasi Continental",
    "score_hotel": "8.2",
        }
    )
  batch.put_item(
  Item={
    "id": 441,
    "province": "Quito",
    "category": "Value for money",
    "score_category": "8.5",
    "hotel": "Hotel Huasi Continental",
    "score_hotel": "8.2",
        }
    )
  batch.put_item(
  Item={
    "id": 442,
    "province": "Quito",
    "category": "Location",
    "score_category": "9",
    "hotel": "Hotel Huasi Continental",
    "score_hotel": "8.2",
        }
    )
  batch.put_item(
  Item={
    "id": 443,
    "province": "Quito",
    "category": "Free WiFi",
    "score_category": "10",
    "hotel": "Hotel Huasi Continental",
    "score_hotel": "8.2",
        }
    )
  batch.put_item(
  Item={
    "id": 444,
    "province": "Quito",
    "category": "Staff",
    "score_category": "8.8",
    "hotel": "Dann Carlton Quito",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 445,
    "province": "Quito",
    "category": "Facilities",
    "score_category": "8.8",
    "hotel": "Dann Carlton Quito",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 446,
    "province": "Quito",
    "category": "Cleanliness",
    "score_category": "9.1",
    "hotel": "Dann Carlton Quito",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 447,
    "province": "Quito",
    "category": "Comfort",
    "score_category": "9.2",
    "hotel": "Dann Carlton Quito",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 448,
    "province": "Quito",
    "category": "Value for money",
    "score_category": "8.4",
    "hotel": "Dann Carlton Quito",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 449,
    "province": "Quito",
    "category": "Location",
    "score_category": "9.5",
    "hotel": "Dann Carlton Quito",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 450,
    "province": "Quito",
    "category": "Free WiFi",
    "score_category": "8.4",
    "hotel": "Dann Carlton Quito",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 451,
    "province": "Guayaquil",
    "category": "Staff",
    "score_category": "8",
    "hotel": "Hotel Air Suites",
    "score_hotel": "7.5",
        }
    )
  batch.put_item(
  Item={
    "id": 452,
    "province": "Guayaquil",
    "category": "Facilities",
    "score_category": "7.3",
    "hotel": "Hotel Air Suites",
    "score_hotel": "7.5",
        }
    )
  batch.put_item(
  Item={
    "id": 453,
    "province": "Guayaquil",
    "category": "Cleanliness",
    "score_category": "7.9",
    "hotel": "Hotel Air Suites",
    "score_hotel": "7.5",
        }
    )
  batch.put_item(
  Item={
    "id": 454,
    "province": "Guayaquil",
    "category": "Comfort",
    "score_category": "7.7",
    "hotel": "Hotel Air Suites",
    "score_hotel": "7.5",
        }
    )
  batch.put_item(
  Item={
    "id": 455,
    "province": "Guayaquil",
    "category": "Value for money",
    "score_category": "7.4",
    "hotel": "Hotel Air Suites",
    "score_hotel": "7.5",
        }
    )
  batch.put_item(
  Item={
    "id": 456,
    "province": "Guayaquil",
    "category": "Location",
    "score_category": "8.5",
    "hotel": "Hotel Air Suites",
    "score_hotel": "7.5",
        }
    )
  batch.put_item(
  Item={
    "id": 457,
    "province": "Guayaquil",
    "category": "Free WiFi",
    "score_category": "7.1",
    "hotel": "Hotel Air Suites",
    "score_hotel": "7.5",
        }
    )
  batch.put_item(
  Item={
    "id": 458,
    "province": "Guayaquil",
    "category": "Staff",
    "score_category": "8.7",
    "hotel": "Hotel Perla Central",
    "score_hotel": "7.9",
        }
    )
  batch.put_item(
  Item={
    "id": 459,
    "province": "Guayaquil",
    "category": "Facilities",
    "score_category": "7.8",
    "hotel": "Hotel Perla Central",
    "score_hotel": "7.9",
        }
    )
  batch.put_item(
  Item={
    "id": 460,
    "province": "Guayaquil",
    "category": "Cleanliness",
    "score_category": "8.1",
    "hotel": "Hotel Perla Central",
    "score_hotel": "7.9",
        }
    )
  batch.put_item(
  Item={
    "id": 461,
    "province": "Guayaquil",
    "category": "Comfort",
    "score_category": "8.1",
    "hotel": "Hotel Perla Central",
    "score_hotel": "7.9",
        }
    )
  batch.put_item(
  Item={
    "id": 462,
    "province": "Guayaquil",
    "category": "Value for money",
    "score_category": "8.1",
    "hotel": "Hotel Perla Central",
    "score_hotel": "7.9",
        }
    )
  batch.put_item(
  Item={
    "id": 463,
    "province": "Guayaquil",
    "category": "Location",
    "score_category": "9.3",
    "hotel": "Hotel Perla Central",
    "score_hotel": "7.9",
        }
    )
  batch.put_item(
  Item={
    "id": 464,
    "province": "Guayaquil",
    "category": "Free WiFi",
    "score_category": "7.9",
    "hotel": "Hotel Perla Central",
    "score_hotel": "7.9",
        }
    )
  batch.put_item(
  Item={
    "id": 465,
    "province": "Guayaquil",
    "category": "Staff",
    "score_category": "9.3",
    "hotel": "Hotel Palace Guayaquil",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 466,
    "province": "Guayaquil",
    "category": "Facilities",
    "score_category": "8.9",
    "hotel": "Hotel Palace Guayaquil",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 467,
    "province": "Guayaquil",
    "category": "Cleanliness",
    "score_category": "9.3",
    "hotel": "Hotel Palace Guayaquil",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 468,
    "province": "Guayaquil",
    "category": "Comfort",
    "score_category": "9.1",
    "hotel": "Hotel Palace Guayaquil",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 469,
    "province": "Guayaquil",
    "category": "Value for money",
    "score_category": "8.8",
    "hotel": "Hotel Palace Guayaquil",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 470,
    "province": "Guayaquil",
    "category": "Location",
    "score_category": "8.9",
    "hotel": "Hotel Palace Guayaquil",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 471,
    "province": "Guayaquil",
    "category": "Free WiFi",
    "score_category": "8.8",
    "hotel": "Hotel Palace Guayaquil",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 472,
    "province": "Guayaquil",
    "category": "Staff",
    "score_category": "9.3",
    "hotel": "River Garden Hotel + Suites",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 473,
    "province": "Guayaquil",
    "category": "Facilities",
    "score_category": "9.1",
    "hotel": "River Garden Hotel + Suites",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 474,
    "province": "Guayaquil",
    "category": "Cleanliness",
    "score_category": "9.3",
    "hotel": "River Garden Hotel + Suites",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 475,
    "province": "Guayaquil",
    "category": "Comfort",
    "score_category": "9.3",
    "hotel": "River Garden Hotel + Suites",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 476,
    "province": "Guayaquil",
    "category": "Value for money",
    "score_category": "8.5",
    "hotel": "River Garden Hotel + Suites",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 477,
    "province": "Guayaquil",
    "category": "Location",
    "score_category": "9.4",
    "hotel": "River Garden Hotel + Suites",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 478,
    "province": "Guayaquil",
    "category": "Free WiFi",
    "score_category": "8.6",
    "hotel": "River Garden Hotel + Suites",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 479,
    "province": "Guayaquil",
    "category": "Staff",
    "score_category": "8.9",
    "hotel": "TRYP by Wyndham Guayaquil",
    "score_hotel": "8.5",
        }
    )
  batch.put_item(
  Item={
    "id": 480,
    "province": "Guayaquil",
    "category": "Facilities",
    "score_category": "8.5",
    "hotel": "TRYP by Wyndham Guayaquil",
    "score_hotel": "8.5",
        }
    )
  batch.put_item(
  Item={
    "id": 481,
    "province": "Guayaquil",
    "category": "Cleanliness",
    "score_category": "8.8",
    "hotel": "TRYP by Wyndham Guayaquil",
    "score_hotel": "8.5",
        }
    )
  batch.put_item(
  Item={
    "id": 482,
    "province": "Guayaquil",
    "category": "Comfort",
    "score_category": "8.8",
    "hotel": "TRYP by Wyndham Guayaquil",
    "score_hotel": "8.5",
        }
    )
  batch.put_item(
  Item={
    "id": 483,
    "province": "Guayaquil",
    "category": "Value for money",
    "score_category": "8.2",
    "hotel": "TRYP by Wyndham Guayaquil",
    "score_hotel": "8.5",
        }
    )
  batch.put_item(
  Item={
    "id": 484,
    "province": "Guayaquil",
    "category": "Location",
    "score_category": "9.4",
    "hotel": "TRYP by Wyndham Guayaquil",
    "score_hotel": "8.5",
        }
    )
  batch.put_item(
  Item={
    "id": 485,
    "province": "Guayaquil",
    "category": "Free WiFi",
    "score_category": "8.8",
    "hotel": "TRYP by Wyndham Guayaquil",
    "score_hotel": "8.5",
        }
    )
  batch.put_item(
  Item={
    "id": 486,
    "province": "Guayaquil",
    "category": "Staff",
    "score_category": "8.9",
    "hotel": "Wyndham Garden Guayaquil",
    "score_hotel": "8.5",
        }
    )
  batch.put_item(
  Item={
    "id": 487,
    "province": "Guayaquil",
    "category": "Facilities",
    "score_category": "8.6",
    "hotel": "Wyndham Garden Guayaquil",
    "score_hotel": "8.5",
        }
    )
  batch.put_item(
  Item={
    "id": 488,
    "province": "Guayaquil",
    "category": "Cleanliness",
    "score_category": "9",
    "hotel": "Wyndham Garden Guayaquil",
    "score_hotel": "8.5",
        }
    )
  batch.put_item(
  Item={
    "id": 489,
    "province": "Guayaquil",
    "category": "Comfort",
    "score_category": "9",
    "hotel": "Wyndham Garden Guayaquil",
    "score_hotel": "8.5",
        }
    )
  batch.put_item(
  Item={
    "id": 490,
    "province": "Guayaquil",
    "category": "Value for money",
    "score_category": "8.4",
    "hotel": "Wyndham Garden Guayaquil",
    "score_hotel": "8.5",
        }
    )
  batch.put_item(
  Item={
    "id": 491,
    "province": "Guayaquil",
    "category": "Location",
    "score_category": "9.2",
    "hotel": "Wyndham Garden Guayaquil",
    "score_hotel": "8.5",
        }
    )
  batch.put_item(
  Item={
    "id": 492,
    "province": "Guayaquil",
    "category": "Free WiFi",
    "score_category": "8.6",
    "hotel": "Wyndham Garden Guayaquil",
    "score_hotel": "8.5",
        }
    )
  batch.put_item(
  Item={
    "id": 493,
    "province": "Guayaquil",
    "category": "Staff",
    "score_category": "9.3",
    "hotel": "Unipark by Oro Verde Hotels",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 494,
    "province": "Guayaquil",
    "category": "Facilities",
    "score_category": "8.8",
    "hotel": "Unipark by Oro Verde Hotels",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 495,
    "province": "Guayaquil",
    "category": "Cleanliness",
    "score_category": "9.1",
    "hotel": "Unipark by Oro Verde Hotels",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 496,
    "province": "Guayaquil",
    "category": "Comfort",
    "score_category": "9.1",
    "hotel": "Unipark by Oro Verde Hotels",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 497,
    "province": "Guayaquil",
    "category": "Value for money",
    "score_category": "8.6",
    "hotel": "Unipark by Oro Verde Hotels",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 498,
    "province": "Guayaquil",
    "category": "Location",
    "score_category": "9.2",
    "hotel": "Unipark by Oro Verde Hotels",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 499,
    "province": "Guayaquil",
    "category": "Free WiFi",
    "score_category": "9.1",
    "hotel": "Unipark by Oro Verde Hotels",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 500,
    "province": "Guayaquil",
    "category": "Staff",
    "score_category": "9.2",
    "hotel": "Holiday Inn Guayaquil Airport; an IHG Hotel",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 501,
    "province": "Guayaquil",
    "category": "Facilities",
    "score_category": "9.1",
    "hotel": "Holiday Inn Guayaquil Airport; an IHG Hotel",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 502,
    "province": "Guayaquil",
    "category": "Cleanliness",
    "score_category": "9.3",
    "hotel": "Holiday Inn Guayaquil Airport; an IHG Hotel",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 503,
    "province": "Guayaquil",
    "category": "Comfort",
    "score_category": "9.3",
    "hotel": "Holiday Inn Guayaquil Airport; an IHG Hotel",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 504,
    "province": "Guayaquil",
    "category": "Value for money",
    "score_category": "8.4",
    "hotel": "Holiday Inn Guayaquil Airport; an IHG Hotel",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 505,
    "province": "Guayaquil",
    "category": "Location",
    "score_category": "9.4",
    "hotel": "Holiday Inn Guayaquil Airport; an IHG Hotel",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 506,
    "province": "Guayaquil",
    "category": "Free WiFi",
    "score_category": "8.8",
    "hotel": "Holiday Inn Guayaquil Airport; an IHG Hotel",
    "score_hotel": "8.8",
        }
    )
  batch.put_item(
  Item={
    "id": 507,
    "province": "Guayaquil",
    "category": "Staff",
    "score_category": "9",
    "hotel": "YU! Smarthotels",
    "score_hotel": "8.5",
        }
    )
  batch.put_item(
  Item={
    "id": 508,
    "province": "Guayaquil",
    "category": "Facilities",
    "score_category": "8.4",
    "hotel": "YU! Smarthotels",
    "score_hotel": "8.5",
        }
    )
  batch.put_item(
  Item={
    "id": 509,
    "province": "Guayaquil",
    "category": "Cleanliness",
    "score_category": "8.8",
    "hotel": "YU! Smarthotels",
    "score_hotel": "8.5",
        }
    )
  batch.put_item(
  Item={
    "id": 510,
    "province": "Guayaquil",
    "category": "Comfort",
    "score_category": "8.8",
    "hotel": "YU! Smarthotels",
    "score_hotel": "8.5",
        }
    )
  batch.put_item(
  Item={
    "id": 511,
    "province": "Guayaquil",
    "category": "Value for money",
    "score_category": "8.5",
    "hotel": "YU! Smarthotels",
    "score_hotel": "8.5",
        }
    )
  batch.put_item(
  Item={
    "id": 512,
    "province": "Guayaquil",
    "category": "Location",
    "score_category": "8.5",
    "hotel": "YU! Smarthotels",
    "score_hotel": "8.5",
        }
    )
  batch.put_item(
  Item={
    "id": 513,
    "province": "Guayaquil",
    "category": "Free WiFi",
    "score_category": "8.4",
    "hotel": "YU! Smarthotels",
    "score_hotel": "8.5",
        }
    )
  batch.put_item(
  Item={
    "id": 514,
    "province": "Guayaquil",
    "category": "Staff",
    "score_category": "9.3",
    "hotel": "Wyndham Guayaquil; Puerto Santa Ana",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 515,
    "province": "Guayaquil",
    "category": "Facilities",
    "score_category": "9.1",
    "hotel": "Wyndham Guayaquil; Puerto Santa Ana",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 516,
    "province": "Guayaquil",
    "category": "Cleanliness",
    "score_category": "9.3",
    "hotel": "Wyndham Guayaquil; Puerto Santa Ana",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 517,
    "province": "Guayaquil",
    "category": "Comfort",
    "score_category": "9.4",
    "hotel": "Wyndham Guayaquil; Puerto Santa Ana",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 518,
    "province": "Guayaquil",
    "category": "Value for money",
    "score_category": "8.5",
    "hotel": "Wyndham Guayaquil; Puerto Santa Ana",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 519,
    "province": "Guayaquil",
    "category": "Location",
    "score_category": "9.5",
    "hotel": "Wyndham Guayaquil; Puerto Santa Ana",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 520,
    "province": "Guayaquil",
    "category": "Free WiFi",
    "score_category": "8.9",
    "hotel": "Wyndham Guayaquil; Puerto Santa Ana",
    "score_hotel": "8.9",
        }
    )
  batch.put_item(
  Item={
    "id": 521,
    "province": "Guayaquil",
    "category": "Staff",
    "score_category": "8.9",
    "hotel": "Hotel de Alborada",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 522,
    "province": "Guayaquil",
    "category": "Facilities",
    "score_category": "8.4",
    "hotel": "Hotel de Alborada",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 523,
    "province": "Guayaquil",
    "category": "Cleanliness",
    "score_category": "8.8",
    "hotel": "Hotel de Alborada",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 524,
    "province": "Guayaquil",
    "category": "Comfort",
    "score_category": "8.5",
    "hotel": "Hotel de Alborada",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 525,
    "province": "Guayaquil",
    "category": "Value for money",
    "score_category": "8.4",
    "hotel": "Hotel de Alborada",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 526,
    "province": "Guayaquil",
    "category": "Location",
    "score_category": "8.4",
    "hotel": "Hotel de Alborada",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 527,
    "province": "Guayaquil",
    "category": "Free WiFi",
    "score_category": "8.8",
    "hotel": "Hotel de Alborada",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 528,
    "province": "Guayaquil",
    "category": "Staff",
    "score_category": "8.9",
    "hotel": "The Park Hotel",
    "score_hotel": "7.9",
        }
    )
  batch.put_item(
  Item={
    "id": 529,
    "province": "Guayaquil",
    "category": "Facilities",
    "score_category": "7.6",
    "hotel": "The Park Hotel",
    "score_hotel": "7.9",
        }
    )
  batch.put_item(
  Item={
    "id": 530,
    "province": "Guayaquil",
    "category": "Cleanliness",
    "score_category": "8.3",
    "hotel": "The Park Hotel",
    "score_hotel": "7.9",
        }
    )
  batch.put_item(
  Item={
    "id": 531,
    "province": "Guayaquil",
    "category": "Comfort",
    "score_category": "8",
    "hotel": "The Park Hotel",
    "score_hotel": "7.9",
        }
    )
  batch.put_item(
  Item={
    "id": 532,
    "province": "Guayaquil",
    "category": "Value for money",
    "score_category": "7.8",
    "hotel": "The Park Hotel",
    "score_hotel": "7.9",
        }
    )
  batch.put_item(
  Item={
    "id": 533,
    "province": "Guayaquil",
    "category": "Location",
    "score_category": "9.1",
    "hotel": "The Park Hotel",
    "score_hotel": "7.9",
        }
    )
  batch.put_item(
  Item={
    "id": 534,
    "province": "Guayaquil",
    "category": "Free WiFi",
    "score_category": "7.8",
    "hotel": "The Park Hotel",
    "score_hotel": "7.9",
        }
    )
  batch.put_item(
  Item={
    "id": 535,
    "province": "Guayaquil",
    "category": "Staff",
    "score_category": "9.1",
    "hotel": "Sheraton Guayaquil",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 536,
    "province": "Guayaquil",
    "category": "Facilities",
    "score_category": "8.7",
    "hotel": "Sheraton Guayaquil",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 537,
    "province": "Guayaquil",
    "category": "Cleanliness",
    "score_category": "9.1",
    "hotel": "Sheraton Guayaquil",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 538,
    "province": "Guayaquil",
    "category": "Comfort",
    "score_category": "9.1",
    "hotel": "Sheraton Guayaquil",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 539,
    "province": "Guayaquil",
    "category": "Value for money",
    "score_category": "8.3",
    "hotel": "Sheraton Guayaquil",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 540,
    "province": "Guayaquil",
    "category": "Location",
    "score_category": "9.4",
    "hotel": "Sheraton Guayaquil",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 541,
    "province": "Guayaquil",
    "category": "Free WiFi",
    "score_category": "8.8",
    "hotel": "Sheraton Guayaquil",
    "score_hotel": "8.7",
        }
    )
  batch.put_item(
  Item={
    "id": 542,
    "province": "Guayaquil",
    "category": "Staff",
    "score_category": "8.9",
    "hotel": "DC Suites Aeropuerto",
    "score_hotel": "8.1",
        }
    )
  batch.put_item(
  Item={
    "id": 543,
    "province": "Guayaquil",
    "category": "Facilities",
    "score_category": "8",
    "hotel": "DC Suites Aeropuerto",
    "score_hotel": "8.1",
        }
    )
  batch.put_item(
  Item={
    "id": 544,
    "province": "Guayaquil",
    "category": "Cleanliness",
    "score_category": "8.6",
    "hotel": "DC Suites Aeropuerto",
    "score_hotel": "8.1",
        }
    )
  batch.put_item(
  Item={
    "id": 545,
    "province": "Guayaquil",
    "category": "Comfort",
    "score_category": "8.4",
    "hotel": "DC Suites Aeropuerto",
    "score_hotel": "8.1",
        }
    )
  batch.put_item(
  Item={
    "id": 546,
    "province": "Guayaquil",
    "category": "Value for money",
    "score_category": "8.3",
    "hotel": "DC Suites Aeropuerto",
    "score_hotel": "8.1",
        }
    )
  batch.put_item(
  Item={
    "id": 547,
    "province": "Guayaquil",
    "category": "Location",
    "score_category": "8.6",
    "hotel": "DC Suites Aeropuerto",
    "score_hotel": "8.1",
        }
    )
  batch.put_item(
  Item={
    "id": 548,
    "province": "Guayaquil",
    "category": "Free WiFi",
    "score_category": "8.7",
    "hotel": "DC Suites Aeropuerto",
    "score_hotel": "8.1",
        }
    )
  batch.put_item(
  Item={
    "id": 549,
    "province": "Guayaquil",
    "category": "Staff",
    "score_category": "8.3",
    "hotel": "Airport Hotel",
    "score_hotel": "7.8",
        }
    )
  batch.put_item(
  Item={
    "id": 550,
    "province": "Guayaquil",
    "category": "Facilities",
    "score_category": "7.7",
    "hotel": "Airport Hotel",
    "score_hotel": "7.8",
        }
    )
  batch.put_item(
  Item={
    "id": 551,
    "province": "Guayaquil",
    "category": "Cleanliness",
    "score_category": "8.2",
    "hotel": "Airport Hotel",
    "score_hotel": "7.8",
        }
    )
  batch.put_item(
  Item={
    "id": 552,
    "province": "Guayaquil",
    "category": "Comfort",
    "score_category": "8",
    "hotel": "Airport Hotel",
    "score_hotel": "7.8",
        }
    )
  batch.put_item(
  Item={
    "id": 553,
    "province": "Guayaquil",
    "category": "Value for money",
    "score_category": "7.8",
    "hotel": "Airport Hotel",
    "score_hotel": "7.8",
        }
    )
  batch.put_item(
  Item={
    "id": 554,
    "province": "Guayaquil",
    "category": "Location",
    "score_category": "8.9",
    "hotel": "Airport Hotel",
    "score_hotel": "7.8",
        }
    )
  batch.put_item(
  Item={
    "id": 555,
    "province": "Guayaquil",
    "category": "Free WiFi",
    "score_category": "7.2",
    "hotel": "Airport Hotel",
    "score_hotel": "7.8",
        }
    )
  batch.put_item(
  Item={
    "id": 556,
    "province": "Guayaquil",
    "category": "Staff",
    "score_category": "8.9",
    "hotel": "Hotel Puerto Pacifico Guayaquil Airport",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 557,
    "province": "Guayaquil",
    "category": "Facilities",
    "score_category": "8.5",
    "hotel": "Hotel Puerto Pacifico Guayaquil Airport",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 558,
    "province": "Guayaquil",
    "category": "Cleanliness",
    "score_category": "8.9",
    "hotel": "Hotel Puerto Pacifico Guayaquil Airport",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 559,
    "province": "Guayaquil",
    "category": "Comfort",
    "score_category": "8.8",
    "hotel": "Hotel Puerto Pacifico Guayaquil Airport",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 560,
    "province": "Guayaquil",
    "category": "Value for money",
    "score_category": "8.2",
    "hotel": "Hotel Puerto Pacifico Guayaquil Airport",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 561,
    "province": "Guayaquil",
    "category": "Location",
    "score_category": "8.8",
    "hotel": "Hotel Puerto Pacifico Guayaquil Airport",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 562,
    "province": "Guayaquil",
    "category": "Free WiFi",
    "score_category": "7.9",
    "hotel": "Hotel Puerto Pacifico Guayaquil Airport",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 563,
    "province": "Guayaquil",
    "category": "Staff",
    "score_category": "8.7",
    "hotel": "Hilton Colon Guayaquil Hotel",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 564,
    "province": "Guayaquil",
    "category": "Facilities",
    "score_category": "8.8",
    "hotel": "Hilton Colon Guayaquil Hotel",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 565,
    "province": "Guayaquil",
    "category": "Cleanliness",
    "score_category": "9.1",
    "hotel": "Hilton Colon Guayaquil Hotel",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 566,
    "province": "Guayaquil",
    "category": "Comfort",
    "score_category": "9.2",
    "hotel": "Hilton Colon Guayaquil Hotel",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 567,
    "province": "Guayaquil",
    "category": "Value for money",
    "score_category": "8.3",
    "hotel": "Hilton Colon Guayaquil Hotel",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 568,
    "province": "Guayaquil",
    "category": "Location",
    "score_category": "9.1",
    "hotel": "Hilton Colon Guayaquil Hotel",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 569,
    "province": "Guayaquil",
    "category": "Free WiFi",
    "score_category": "8.4",
    "hotel": "Hilton Colon Guayaquil Hotel",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 570,
    "province": "Guayaquil",
    "category": "Staff",
    "score_category": "8.8",
    "hotel": "Pepe's House Guayaquil I Self Check-In MicroHotel",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 571,
    "province": "Guayaquil",
    "category": "Facilities",
    "score_category": "8.3",
    "hotel": "Pepe's House Guayaquil I Self Check-In MicroHotel",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 572,
    "province": "Guayaquil",
    "category": "Cleanliness",
    "score_category": "8.8",
    "hotel": "Pepe's House Guayaquil I Self Check-In MicroHotel",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 573,
    "province": "Guayaquil",
    "category": "Comfort",
    "score_category": "8.8",
    "hotel": "Pepe's House Guayaquil I Self Check-In MicroHotel",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 574,
    "province": "Guayaquil",
    "category": "Value for money",
    "score_category": "8.5",
    "hotel": "Pepe's House Guayaquil I Self Check-In MicroHotel",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 575,
    "province": "Guayaquil",
    "category": "Location",
    "score_category": "9",
    "hotel": "Pepe's House Guayaquil I Self Check-In MicroHotel",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 576,
    "province": "Guayaquil",
    "category": "Free WiFi",
    "score_category": "9.4",
    "hotel": "Pepe's House Guayaquil I Self Check-In MicroHotel",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 577,
    "province": "Guayaquil",
    "category": "Staff",
    "score_category": "8.6",
    "hotel": "Hotel Ramada",
    "score_hotel": "7.9",
        }
    )
  batch.put_item(
  Item={
    "id": 578,
    "province": "Guayaquil",
    "category": "Facilities",
    "score_category": "7.8",
    "hotel": "Hotel Ramada",
    "score_hotel": "7.9",
        }
    )
  batch.put_item(
  Item={
    "id": 579,
    "province": "Guayaquil",
    "category": "Cleanliness",
    "score_category": "8.3",
    "hotel": "Hotel Ramada",
    "score_hotel": "7.9",
        }
    )
  batch.put_item(
  Item={
    "id": 580,
    "province": "Guayaquil",
    "category": "Comfort",
    "score_category": "8.3",
    "hotel": "Hotel Ramada",
    "score_hotel": "7.9",
        }
    )
  batch.put_item(
  Item={
    "id": 581,
    "province": "Guayaquil",
    "category": "Value for money",
    "score_category": "7.8",
    "hotel": "Hotel Ramada",
    "score_hotel": "7.9",
        }
    )
  batch.put_item(
  Item={
    "id": 582,
    "province": "Guayaquil",
    "category": "Location",
    "score_category": "9.1",
    "hotel": "Hotel Ramada",
    "score_hotel": "7.9",
        }
    )
  batch.put_item(
  Item={
    "id": 583,
    "province": "Guayaquil",
    "category": "Free WiFi",
    "score_category": "8.2",
    "hotel": "Hotel Ramada",
    "score_hotel": "7.9",
        }
    )
  batch.put_item(
  Item={
    "id": 584,
    "province": "Guayaquil",
    "category": "Staff",
    "score_category": "8.4",
    "hotel": "Hotel Patrimonial by Greenfield",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 585,
    "province": "Guayaquil",
    "category": "Facilities",
    "score_category": "8.4",
    "hotel": "Hotel Patrimonial by Greenfield",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 586,
    "province": "Guayaquil",
    "category": "Cleanliness",
    "score_category": "8.7",
    "hotel": "Hotel Patrimonial by Greenfield",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 587,
    "province": "Guayaquil",
    "category": "Comfort",
    "score_category": "8.8",
    "hotel": "Hotel Patrimonial by Greenfield",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 588,
    "province": "Guayaquil",
    "category": "Value for money",
    "score_category": "8.6",
    "hotel": "Hotel Patrimonial by Greenfield",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 589,
    "province": "Guayaquil",
    "category": "Location",
    "score_category": "8.4",
    "hotel": "Hotel Patrimonial by Greenfield",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 590,
    "province": "Guayaquil",
    "category": "Free WiFi",
    "score_category": "8.7",
    "hotel": "Hotel Patrimonial by Greenfield",
    "score_hotel": "8.4",
        }
    )
  batch.put_item(
  Item={
    "id": 591,
    "province": "Guayaquil",
    "category": "Staff",
    "score_category": "8.7",
    "hotel": "Hotel Marcelius",
    "score_hotel": "8.3",
        }
    )
  batch.put_item(
  Item={
    "id": 592,
    "province": "Guayaquil",
    "category": "Facilities",
    "score_category": "8.3",
    "hotel": "Hotel Marcelius",
    "score_hotel": "8.3",
        }
    )
  batch.put_item(
  Item={
    "id": 593,
    "province": "Guayaquil",
    "category": "Cleanliness",
    "score_category": "8.7",
    "hotel": "Hotel Marcelius",
    "score_hotel": "8.3",
        }
    )
  batch.put_item(
  Item={
    "id": 594,
    "province": "Guayaquil",
    "category": "Comfort",
    "score_category": "8.6",
    "hotel": "Hotel Marcelius",
    "score_hotel": "8.3",
        }
    )
  batch.put_item(
  Item={
    "id": 595,
    "province": "Guayaquil",
    "category": "Value for money",
    "score_category": "8.2",
    "hotel": "Hotel Marcelius",
    "score_hotel": "8.3",
        }
    )
  batch.put_item(
  Item={
    "id": 596,
    "province": "Guayaquil",
    "category": "Location",
    "score_category": "8.7",
    "hotel": "Hotel Marcelius",
    "score_hotel": "8.3",
        }
    )
  batch.put_item(
  Item={
    "id": 597,
    "province": "Guayaquil",
    "category": "Free WiFi",
    "score_category": "7.9",
    "hotel": "Hotel Marcelius",
    "score_hotel": "8.3",
        }
    )
  batch.put_item(
  Item={
    "id": 598,
    "province": "Guayaquil",
    "category": "Staff",
    "score_category": "9.3",
    "hotel": "Hotel Boutique Mansion Del Rio",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 599,
    "province": "Guayaquil",
    "category": "Facilities",
    "score_category": "8.5",
    "hotel": "Hotel Boutique Mansion Del Rio",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 600,
    "province": "Guayaquil",
    "category": "Cleanliness",
    "score_category": "8.7",
    "hotel": "Hotel Boutique Mansion Del Rio",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 601,
    "province": "Guayaquil",
    "category": "Comfort",
    "score_category": "8.8",
    "hotel": "Hotel Boutique Mansion Del Rio",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 602,
    "province": "Guayaquil",
    "category": "Value for money",
    "score_category": "8.6",
    "hotel": "Hotel Boutique Mansion Del Rio",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 603,
    "province": "Guayaquil",
    "category": "Location",
    "score_category": "9.4",
    "hotel": "Hotel Boutique Mansion Del Rio",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 604,
    "province": "Guayaquil",
    "category": "Free WiFi",
    "score_category": "8.8",
    "hotel": "Hotel Boutique Mansion Del Rio",
    "score_hotel": "8.6",
        }
    )
  batch.put_item(
  Item={
    "id": 605,
    "province": "Guayaquil",
    "category": "Staff",
    "score_category": "8.9",
    "hotel": "Manso Boutique Guest House",
    "score_hotel": "8",
        }
    )
  batch.put_item(
  Item={
    "id": 606,
    "province": "Guayaquil",
    "category": "Facilities",
    "score_category": "7.9",
    "hotel": "Manso Boutique Guest House",
    "score_hotel": "8",
        }
    )
  batch.put_item(
  Item={
    "id": 607,
    "province": "Guayaquil",
    "category": "Cleanliness",
    "score_category": "8.1",
    "hotel": "Manso Boutique Guest House",
    "score_hotel": "8",
        }
    )
  batch.put_item(
  Item={
    "id": 608,
    "province": "Guayaquil",
    "category": "Comfort",
    "score_category": "8.1",
    "hotel": "Manso Boutique Guest House",
    "score_hotel": "8",
        }
    )
  batch.put_item(
  Item={
    "id": 609,
    "province": "Guayaquil",
    "category": "Value for money",
    "score_category": "8.2",
    "hotel": "Manso Boutique Guest House",
    "score_hotel": "8",
        }
    )
  batch.put_item(
  Item={
    "id": 610,
    "province": "Guayaquil",
    "category": "Location",
    "score_category": "9.4",
    "hotel": "Manso Boutique Guest House",
    "score_hotel": "8",
        }
    )
  batch.put_item(
  Item={
    "id": 611,
    "province": "Guayaquil",
    "category": "Free WiFi",
    "score_category": "8.5",
    "hotel": "Manso Boutique Guest House",
    "score_hotel": "8",
  })

print(categories.get_item(
    Key = {
        "id": 611,
        "category": "Free WiFi",
    }
)['Item'], flush = True)

"""
Inserting records in surroundings
"""

with surroundings.batch_writer() as batch:
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Parque Cojimíes",
    "distance": "16",
    "hotel": "La Facha Hostal Restaurant Surf",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "RestaurantSuly's Pasta Grill & Bar",
    "distance": "0.05",
    "hotel": "La Facha Hostal Restaurant Surf",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "RestaurantEl Económico",
    "distance": "0.15",
    "hotel": "La Facha Hostal Restaurant Surf",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "RestaurantAtardecer de Mompiche",
    "distance": "0.15",
    "hotel": "La Facha Hostal Restaurant Surf",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Mompiche Beach",
    "distance": "0.05",
    "hotel": "La Facha Hostal Restaurant Surf",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Playa de Portete",
    "distance": "3.5",
    "hotel": "La Facha Hostal Restaurant Surf",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Colonel Carlos Concha Torres Airport",
    "distance": "68",
    "hotel": "La Facha Hostal Restaurant Surf",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Parque Las Palmas",
    "distance": "0.25",
    "hotel": "Hotel Casa Arnaldo Esmeraldas",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Parque mina de piedra",
    "distance": "0.5",
    "hotel": "Hotel Casa Arnaldo Esmeraldas",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Refinerìa Petroecuador Esmeraldas",
    "distance": "2.9",
    "hotel": "Hotel Casa Arnaldo Esmeraldas",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Parque Infantil",
    "distance": "3",
    "hotel": "Hotel Casa Arnaldo Esmeraldas",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "cancha",
    "distance": "3.1",
    "hotel": "Hotel Casa Arnaldo Esmeraldas",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Estadio Folke Anderson",
    "distance": "3.2",
    "hotel": "Hotel Casa Arnaldo Esmeraldas",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Campo de Futbol",
    "distance": "3.4",
    "hotel": "Hotel Casa Arnaldo Esmeraldas",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cancha",
    "distance": "3.5",
    "hotel": "Hotel Casa Arnaldo Esmeraldas",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Parque San Jose Obrero",
    "distance": "3.6",
    "hotel": "Hotel Casa Arnaldo Esmeraldas",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "parque Iglesia San Jose de Obreo",
    "distance": "3.6",
    "hotel": "Hotel Casa Arnaldo Esmeraldas",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "RestaurantPizzería La Cascada de Tony",
    "distance": "0.04",
    "hotel": "Hotel Casa Arnaldo Esmeraldas",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cafe/barKaraoke Gio´s",
    "distance": "0.1",
    "hotel": "Hotel Casa Arnaldo Esmeraldas",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cafe/barLa canchita",
    "distance": "0.2",
    "hotel": "Hotel Casa Arnaldo Esmeraldas",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Playa Las Palmas",
    "distance": "0.15",
    "hotel": "Hotel Casa Arnaldo Esmeraldas",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Colonel Carlos Concha Torres Airport",
    "distance": "3.9",
    "hotel": "Hotel Casa Arnaldo Esmeraldas",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cancha de juego del Colegio Pierre",
    "distance": "0.7",
    "hotel": "Hotel la Barca",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "cleared area",
    "distance": "6",
    "hotel": "Hotel la Barca",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "RestaurantHot Dog Crocante",
    "distance": "0.01",
    "hotel": "Hotel la Barca",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "RestaurantSeaquarium",
    "distance": "0.04",
    "hotel": "Hotel la Barca",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "RestaurantKike's",
    "distance": "0.05",
    "hotel": "Hotel la Barca",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Atacames Beach",
    "distance": "0.01",
    "hotel": "Hotel la Barca",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Tonsupa Beach",
    "distance": "3.7",
    "hotel": "Hotel la Barca",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Same Beach",
    "distance": "8",
    "hotel": "Hotel la Barca",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Colonel Carlos Concha Torres Airport",
    "distance": "28",
    "hotel": "Hotel la Barca",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cancha de juego del Colegio Pierre",
    "distance": "7",
    "hotel": "Resort Playa Azul Departamentos frente al mar",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "cleared area",
    "distance": "13",
    "hotel": "Resort Playa Azul Departamentos frente al mar",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cancha de Futbol",
    "distance": "14",
    "hotel": "Resort Playa Azul Departamentos frente al mar",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Redondel de Codesa",
    "distance": "15",
    "hotel": "Resort Playa Azul Departamentos frente al mar",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Parque de Codesa",
    "distance": "15",
    "hotel": "Resort Playa Azul Departamentos frente al mar",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Campo de Futbol",
    "distance": "15",
    "hotel": "Resort Playa Azul Departamentos frente al mar",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Refinerìa Petroecuador Esmeraldas",
    "distance": "16",
    "hotel": "Resort Playa Azul Departamentos frente al mar",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cancha",
    "distance": "17",
    "hotel": "Resort Playa Azul Departamentos frente al mar",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Parque Roberto Luis Cervantes",
    "distance": "17",
    "hotel": "Resort Playa Azul Departamentos frente al mar",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Estadio Folke Anderson",
    "distance": "17",
    "hotel": "Resort Playa Azul Departamentos frente al mar",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "RestaurantCamarón Dorado",
    "distance": "0.35",
    "hotel": "Resort Playa Azul Departamentos frente al mar",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "RestaurantAiru",
    "distance": "1.2",
    "hotel": "Resort Playa Azul Departamentos frente al mar",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cafe/barCocktails Bar",
    "distance": "1.7",
    "hotel": "Resort Playa Azul Departamentos frente al mar",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Tonsupa Beach",
    "distance": "0.1",
    "hotel": "Resort Playa Azul Departamentos frente al mar",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Atacames Beach",
    "distance": "5",
    "hotel": "Resort Playa Azul Departamentos frente al mar",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Colonel Carlos Concha Torres Airport",
    "distance": "21",
    "hotel": "Resort Playa Azul Departamentos frente al mar",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cancha de juego del Colegio Pierre",
    "distance": "6",
    "hotel": "Escapaditas a la Playa",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "cleared area",
    "distance": "12",
    "hotel": "Escapaditas a la Playa",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cancha de Futbol",
    "distance": "15",
    "hotel": "Escapaditas a la Playa",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Parque de Codesa",
    "distance": "16",
    "hotel": "Escapaditas a la Playa",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Campo de Futbol",
    "distance": "16",
    "hotel": "Escapaditas a la Playa",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Refinerìa Petroecuador Esmeraldas",
    "distance": "17",
    "hotel": "Escapaditas a la Playa",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cancha",
    "distance": "18",
    "hotel": "Escapaditas a la Playa",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Parque Roberto Luis Cervantes",
    "distance": "18",
    "hotel": "Escapaditas a la Playa",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Estadio Folke Anderson",
    "distance": "18",
    "hotel": "Escapaditas a la Playa",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "RestaurantAiru",
    "distance": "0.4",
    "hotel": "Escapaditas a la Playa",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "RestaurantCamarón Dorado",
    "distance": "0.6",
    "hotel": "Escapaditas a la Playa",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cafe/barCocktails Bar",
    "distance": "0.85",
    "hotel": "Escapaditas a la Playa",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Tonsupa Beach",
    "distance": "0",
    "hotel": "Escapaditas a la Playa",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Atacames Beach",
    "distance": "4.5",
    "hotel": "Escapaditas a la Playa",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Colonel Carlos Concha Torres Airport",
    "distance": "22",
    "hotel": "Escapaditas a la Playa",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cancha de juego del Colegio Pierre",
    "distance": "5",
    "hotel": "Hotel Oceanic Lodge",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "RestaurantAiru",
    "distance": "0.5",
    "hotel": "Hotel Oceanic Lodge",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cafe/barCocktails Bar",
    "distance": "0.75",
    "hotel": "Hotel Oceanic Lodge",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cafe/barPicho's",
    "distance": "0.75",
    "hotel": "Hotel Oceanic Lodge",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Tonsupa Beach",
    "distance": "0.5",
    "hotel": "Hotel Oceanic Lodge",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Atacames Beach",
    "distance": "4.2",
    "hotel": "Hotel Oceanic Lodge",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Parque Cojimíes",
    "distance": "18",
    "hotel": "Seaside Garden Ecolodge Mompiche",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "RestaurantSuly's Pasta Grill & Bar",
    "distance": "2.5",
    "hotel": "Seaside Garden Ecolodge Mompiche",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "RestaurantEl Económico",
    "distance": "2.5",
    "hotel": "Seaside Garden Ecolodge Mompiche",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "RestaurantAtardecer de Mompiche",
    "distance": "2.6",
    "hotel": "Seaside Garden Ecolodge Mompiche",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Mompiche Beach",
    "distance": "0.04",
    "hotel": "Seaside Garden Ecolodge Mompiche",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Playa de Portete",
    "distance": "6",
    "hotel": "Seaside Garden Ecolodge Mompiche",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Colonel Carlos Concha Torres Airport",
    "distance": "66",
    "hotel": "Seaside Garden Ecolodge Mompiche",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cancha de juego del Colegio Pierre",
    "distance": "3.9",
    "hotel": "Hotel RC Tonsupa",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "cleared area",
    "distance": "11",
    "hotel": "Hotel RC Tonsupa",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cancha de Futbol",
    "distance": "17",
    "hotel": "Hotel RC Tonsupa",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Redondel de Codesa",
    "distance": "17",
    "hotel": "Hotel RC Tonsupa",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Parque de Codesa",
    "distance": "17",
    "hotel": "Hotel RC Tonsupa",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Campo de Futbol",
    "distance": "18",
    "hotel": "Hotel RC Tonsupa",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Refinerìa Petroecuador Esmeraldas",
    "distance": "18",
    "hotel": "Hotel RC Tonsupa",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cancha",
    "distance": "19",
    "hotel": "Hotel RC Tonsupa",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Parque Roberto Luis Cervantes",
    "distance": "20",
    "hotel": "Hotel RC Tonsupa",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Estadio Folke Anderson",
    "distance": "20",
    "hotel": "Hotel RC Tonsupa",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "RestaurantMuelle 3",
    "distance": "0.95",
    "hotel": "Hotel RC Tonsupa",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cafe/barMuelle 3",
    "distance": "0.95",
    "hotel": "Hotel RC Tonsupa",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cafe/barPicho's",
    "distance": "0.95",
    "hotel": "Hotel RC Tonsupa",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Tonsupa Beach",
    "distance": "0.15",
    "hotel": "Hotel RC Tonsupa",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Atacames Beach",
    "distance": "2.7",
    "hotel": "Hotel RC Tonsupa",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Colonel Carlos Concha Torres Airport",
    "distance": "24",
    "hotel": "Hotel RC Tonsupa",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Redondel de Codesa",
    "distance": "16",
    "hotel": "Departamento Frente al Mar Diamond Beach",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "RestaurantAiru",
    "distance": "0.2",
    "hotel": "Departamento Frente al Mar Diamond Beach",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cafe/barCocktails Bar",
    "distance": "0.65",
    "hotel": "Departamento Frente al Mar Diamond Beach",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cafe/barPicho's",
    "distance": "0.65",
    "hotel": "Departamento Frente al Mar Diamond Beach",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Atacames Beach",
    "distance": "4.3",
    "hotel": "Departamento Frente al Mar Diamond Beach",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cancha de Futbol",
    "distance": "16",
    "hotel": "Hotel Almond Beach",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Campo de Futbol",
    "distance": "17",
    "hotel": "Hotel Almond Beach",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Parque Roberto Luis Cervantes",
    "distance": "19",
    "hotel": "Hotel Almond Beach",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Estadio Folke Anderson",
    "distance": "19",
    "hotel": "Hotel Almond Beach",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cafe/barCocktails Bar",
    "distance": "0.4",
    "hotel": "Hotel Almond Beach",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "RestaurantMuelle 3",
    "distance": "0.4",
    "hotel": "Hotel Almond Beach",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cafe/barPicho's",
    "distance": "0.4",
    "hotel": "Hotel Almond Beach",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Tonsupa Beach",
    "distance": "0.3",
    "hotel": "Hotel Almond Beach",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Atacames Beach",
    "distance": "3.9",
    "hotel": "Hotel Almond Beach",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Colonel Carlos Concha Torres Airport",
    "distance": "23",
    "hotel": "Hotel Almond Beach",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "RestaurantHot Dog Crocante",
    "distance": "0.02",
    "hotel": "Cabañas Ecologicas Cayapas",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "RestaurantSeaquarium",
    "distance": "0.03",
    "hotel": "Cabañas Ecologicas Cayapas",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "RestaurantKike's",
    "distance": "0.04",
    "hotel": "Cabañas Ecologicas Cayapas",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Atacames Beach",
    "distance": "0.02",
    "hotel": "Cabañas Ecologicas Cayapas",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cancha de juego del Colegio Pierre",
    "distance": "4.9",
    "hotel": "Departamento 4 habitaciones 12 personas vista al mar 8vo piso Playa Almendro",
    "score": "7.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cafe/barCocktails Bar",
    "distance": "0.1",
    "hotel": "Departamento 4 habitaciones 12 personas vista al mar 8vo piso Playa Almendro",
    "score": "7.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cafe/barPicho's",
    "distance": "0.1",
    "hotel": "Departamento 4 habitaciones 12 personas vista al mar 8vo piso Playa Almendro",
    "score": "7.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cafe/barMuelle 3",
    "distance": "0.1",
    "hotel": "Departamento 4 habitaciones 12 personas vista al mar 8vo piso Playa Almendro",
    "score": "7.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Atacames Beach",
    "distance": "3.7",
    "hotel": "Departamento 4 habitaciones 12 personas vista al mar 8vo piso Playa Almendro",
    "score": "7.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Redondel de Codesa",
    "distance": "14",
    "hotel": "Resort Playa Azul Tonsupa Departamento de 2 Habitaciones",
    "score": "9.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "RestaurantCamarón Dorado",
    "distance": "0.5",
    "hotel": "Resort Playa Azul Tonsupa Departamento de 2 Habitaciones",
    "score": "9.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "RestaurantAiru",
    "distance": "1.4",
    "hotel": "Resort Playa Azul Tonsupa Departamento de 2 Habitaciones",
    "score": "9.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cafe/barCocktails Bar",
    "distance": "1.9",
    "hotel": "Resort Playa Azul Tonsupa Departamento de 2 Habitaciones",
    "score": "9.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Atacames Beach",
    "distance": "6",
    "hotel": "Resort Playa Azul Tonsupa Departamento de 2 Habitaciones",
    "score": "9.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cancha de juego del Colegio Pierre",
    "distance": "9",
    "hotel": "Tonsupa Diamond Beach Apart - Hotel",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cancha de Futbol",
    "distance": "12",
    "hotel": "Tonsupa Diamond Beach Apart - Hotel",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Redondel de Codesa",
    "distance": "13",
    "hotel": "Tonsupa Diamond Beach Apart - Hotel",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Parque de Codesa",
    "distance": "13",
    "hotel": "Tonsupa Diamond Beach Apart - Hotel",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Refinerìa Petroecuador Esmeraldas",
    "distance": "15",
    "hotel": "Tonsupa Diamond Beach Apart - Hotel",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "cleared area",
    "distance": "16",
    "hotel": "Tonsupa Diamond Beach Apart - Hotel",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cancha",
    "distance": "16",
    "hotel": "Tonsupa Diamond Beach Apart - Hotel",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Parque Roberto Luis Cervantes",
    "distance": "16",
    "hotel": "Tonsupa Diamond Beach Apart - Hotel",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Parque Eloy ALfaro",
    "distance": "16",
    "hotel": "Tonsupa Diamond Beach Apart - Hotel",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "RestaurantCamarón Dorado",
    "distance": "4.7",
    "hotel": "Tonsupa Diamond Beach Apart - Hotel",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "RestaurantAiru",
    "distance": "5",
    "hotel": "Tonsupa Diamond Beach Apart - Hotel",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cafe/barCocktails Bar",
    "distance": "5",
    "hotel": "Tonsupa Diamond Beach Apart - Hotel",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Tonsupa Beach",
    "distance": "5",
    "hotel": "Tonsupa Diamond Beach Apart - Hotel",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Atacames Beach",
    "distance": "8",
    "hotel": "Tonsupa Diamond Beach Apart - Hotel",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Colonel Carlos Concha Torres Airport",
    "distance": "20",
    "hotel": "Tonsupa Diamond Beach Apart - Hotel",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "RestaurantSuly's Pasta Grill & Bar",
    "distance": "0.3",
    "hotel": "Aparthotel Oleaje",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "RestaurantEl Económico",
    "distance": "0.4",
    "hotel": "Aparthotel Oleaje",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "RestaurantAtardecer de Mompiche",
    "distance": "0.4",
    "hotel": "Aparthotel Oleaje",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Mompiche Beach",
    "distance": "0.1",
    "hotel": "Aparthotel Oleaje",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Playa de Portete",
    "distance": "3.8",
    "hotel": "Aparthotel Oleaje",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cancha de juego del Colegio Pierre",
    "distance": "4.5",
    "hotel": "Hotel Makana Resort",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "RestaurantMuelle 3",
    "distance": "0.5",
    "hotel": "Hotel Makana Resort",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cafe/barMuelle 3",
    "distance": "0.5",
    "hotel": "Hotel Makana Resort",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cafe/barPicho's",
    "distance": "0.5",
    "hotel": "Hotel Makana Resort",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Atacames Beach",
    "distance": "3.4",
    "hotel": "Hotel Makana Resort",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cancha de juego del Colegio Pierre",
    "distance": "4.7",
    "hotel": "La Bocana",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "RestaurantMuelle 3",
    "distance": "0.15",
    "hotel": "La Bocana",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cafe/barMuelle 3",
    "distance": "0.2",
    "hotel": "La Bocana",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cafe/barPicho's",
    "distance": "0.2",
    "hotel": "La Bocana",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Atacames Beach",
    "distance": "3.5",
    "hotel": "La Bocana",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "RestaurantCamarón Dorado",
    "distance": "0.45",
    "hotel": "Departamentos frente al mar Resort Playa Azul",
    "score": "9.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "RestaurantAiru",
    "distance": "1.3",
    "hotel": "Departamentos frente al mar Resort Playa Azul",
    "score": "9.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cafe/barCocktails Bar",
    "distance": "1.8",
    "hotel": "Departamentos frente al mar Resort Playa Azul",
    "score": "9.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "RestaurantCamarón Dorado",
    "distance": "0.3",
    "hotel": "Suite Makana #403",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "RestaurantAiru",
    "distance": "0.001",
    "hotel": "Suite Makana #403",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cafe/barCocktails Bar",
    "distance": "1.5",
    "hotel": "Suite Makana #403",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Tonsupa Beach",
    "distance": "0.04",
    "hotel": "Suite Makana #403",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "RestaurantAiru",
    "distance": "0.3",
    "hotel": "Caramba Hospedaje",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "RestaurantCamarón Dorado",
    "distance": "0.65",
    "hotel": "Caramba Hospedaje",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Tonsupa Beach",
    "distance": "0.05",
    "hotel": "Caramba Hospedaje",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Atacames Beach",
    "distance": "4.4",
    "hotel": "Caramba Hospedaje",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cafe/barCocktails Bar",
    "distance": "0.35",
    "hotel": "Hotel Salduba",
    "score": "9.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "RestaurantMuelle 3",
    "distance": "0.35",
    "hotel": "Hotel Salduba",
    "score": "9.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cafe/barPicho's",
    "distance": "0.35",
    "hotel": "Hotel Salduba",
    "score": "9.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Tonsupa Beach",
    "distance": "0.25",
    "hotel": "Hotel Salduba",
    "score": "9.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "RestaurantMuelle 3",
    "distance": "0.45",
    "hotel": "Casa del mar",
    "score": "6.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cafe/barCocktails Bar",
    "distance": "0.45",
    "hotel": "Casa del mar",
    "score": "6.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cafe/barPicho's",
    "distance": "0.45",
    "hotel": "Casa del mar",
    "score": "6.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Tonsupa Beach",
    "distance": "0.4",
    "hotel": "Casa del mar",
    "score": "6.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "RestaurantAiru",
    "distance": "0.45",
    "hotel": "Tus Vacaciones en Tonsupa Ecuador.",
    "score": "9.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Cafe/barCocktails Bar",
    "distance": "0.9",
    "hotel": "Tus Vacaciones en Tonsupa Ecuador.",
    "score": "9.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "Tonsupa Beach",
    "distance": "0.35",
    "hotel": "Tus Vacaciones en Tonsupa Ecuador.",
    "score": "9.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Esmeraldas",
    "places": "RestaurantCamarón Dorado",
    "distance": "0.4",
    "hotel": "Departamentos frente al mar en Resort Playa Azul-Tonsupa",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque Del Molinero",
    "distance": "0.3",
    "hotel": "Hotel Santiago de Compostella Suites",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque Darwin",
    "distance": "0.6",
    "hotel": "Hotel Santiago de Compostella Suites",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque Puertas del Sol",
    "distance": "0.65",
    "hotel": "Hotel Santiago de Compostella Suites",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Redondel Feria Libre",
    "distance": "0.75",
    "hotel": "Hotel Santiago de Compostella Suites",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque La fogata",
    "distance": "0.8",
    "hotel": "Hotel Santiago de Compostella Suites",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque Angostura",
    "distance": "0.95",
    "hotel": "Hotel Santiago de Compostella Suites",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque El Ángel",
    "distance": "1.1",
    "hotel": "Hotel Santiago de Compostella Suites",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque San Pedro del Cebollar",
    "distance": "1.1",
    "hotel": "Hotel Santiago de Compostella Suites",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque Napo",
    "distance": "1.1",
    "hotel": "Hotel Santiago de Compostella Suites",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Plaza Del Arte",
    "distance": "1.2",
    "hotel": "Hotel Santiago de Compostella Suites",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantEl Lunch",
    "distance": "0.1",
    "hotel": "Hotel Santiago de Compostella Suites",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantGood Affinitty",
    "distance": "0.1",
    "hotel": "Hotel Santiago de Compostella Suites",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantPunto",
    "distance": "0.2",
    "hotel": "Hotel Santiago de Compostella Suites",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Modern Art Museum",
    "distance": "1.7",
    "hotel": "Hotel Santiago de Compostella Suites",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Straw hat Museum",
    "distance": "2.2",
    "hotel": "Hotel Santiago de Compostella Suites",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of skeletons Doctor Gabriel Moscoso",
    "distance": "2.5",
    "hotel": "Hotel Santiago de Compostella Suites",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Cañari Identity",
    "distance": "2.6",
    "hotel": "Hotel Santiago de Compostella Suites",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of Las Conceptas",
    "distance": "2.7",
    "hotel": "Hotel Santiago de Compostella Suites",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Popular Art Museum",
    "distance": "2.7",
    "hotel": "Hotel Santiago de Compostella Suites",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Aboriginal Cultures",
    "distance": "2.8",
    "hotel": "Hotel Santiago de Compostella Suites",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Metals",
    "distance": "3",
    "hotel": "Hotel Santiago de Compostella Suites",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Pumapungo Museum",
    "distance": "3.5",
    "hotel": "Hotel Santiago de Compostella Suites",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Chahuarchimbana House Museum",
    "distance": "4.1",
    "hotel": "Hotel Santiago de Compostella Suites",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RiverTomebamba River",
    "distance": "2.5",
    "hotel": "Hotel Santiago de Compostella Suites",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Mariscal Lamar International Airport",
    "distance": "4.3",
    "hotel": "Hotel Santiago de Compostella Suites",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Abdon Calderón Park",
    "distance": "0.15",
    "hotel": "Floré Hotel Boutique",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Plazoleta de Santo Domingo",
    "distance": "0.25",
    "hotel": "Floré Hotel Boutique",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Straw hat Museum",
    "distance": "0.35",
    "hotel": "Floré Hotel Boutique",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Plazoleta de la UNE",
    "distance": "0.35",
    "hotel": "Floré Hotel Boutique",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of skeletons Doctor Gabriel Moscoso",
    "distance": "0.4",
    "hotel": "Floré Hotel Boutique",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "El Barranco",
    "distance": "0.4",
    "hotel": "Floré Hotel Boutique",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Cañari Identity",
    "distance": "0.45",
    "hotel": "Floré Hotel Boutique",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Modern Art Museum",
    "distance": "0.45",
    "hotel": "Floré Hotel Boutique",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Plazoleta de la Merced",
    "distance": "0.5",
    "hotel": "Floré Hotel Boutique",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "María Auxiliadora",
    "distance": "0.55",
    "hotel": "Floré Hotel Boutique",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Cafe/barTRADITIONAL TAFFY “DAMADU” Las Herrerías.",
    "distance": "0.01",
    "hotel": "Floré Hotel Boutique",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Cafe/barWilly's cafe",
    "distance": "0.01",
    "hotel": "Floré Hotel Boutique",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Cafe/barCafetería y heladería",
    "distance": "0.02",
    "hotel": "Floré Hotel Boutique",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of Las Conceptas",
    "distance": "0.55",
    "hotel": "Floré Hotel Boutique",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Popular Art Museum",
    "distance": "0.7",
    "hotel": "Floré Hotel Boutique",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Aboriginal Cultures",
    "distance": "0.75",
    "hotel": "Floré Hotel Boutique",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "San Blas square",
    "distance": "0.8",
    "hotel": "Floré Hotel Boutique",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Pumapungo Museum",
    "distance": "1.4",
    "hotel": "Floré Hotel Boutique",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Metals",
    "distance": "1.8",
    "hotel": "Floré Hotel Boutique",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Chahuarchimbana House Museum",
    "distance": "2.2",
    "hotel": "Floré Hotel Boutique",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Cajas National Park",
    "distance": "19",
    "hotel": "Floré Hotel Boutique",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RiverTomebamba River",
    "distance": "0.5",
    "hotel": "Floré Hotel Boutique",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Mariscal Lamar International Airport",
    "distance": "2.5",
    "hotel": "Floré Hotel Boutique",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque Victor J. Cuesta",
    "distance": "0.1",
    "hotel": "Loft NASS Atahualpa",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "San Blas square",
    "distance": "0.1",
    "hotel": "Loft NASS Atahualpa",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Mary Corilé",
    "distance": "0.3",
    "hotel": "Loft NASS Atahualpa",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Cañari Identity",
    "distance": "0.3",
    "hotel": "Loft NASS Atahualpa",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque Carlos Cueva Tamariz",
    "distance": "0.35",
    "hotel": "Loft NASS Atahualpa",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of Las Conceptas",
    "distance": "0.35",
    "hotel": "Loft NASS Atahualpa",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of skeletons Doctor Gabriel Moscoso",
    "distance": "0.35",
    "hotel": "Loft NASS Atahualpa",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Plazoleta de la UNE",
    "distance": "0.4",
    "hotel": "Loft NASS Atahualpa",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Plazoleta Hermano Miguel",
    "distance": "0.4",
    "hotel": "Loft NASS Atahualpa",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Plaza Antiguo Iess",
    "distance": "0.45",
    "hotel": "Loft NASS Atahualpa",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantTortillas de choclo",
    "distance": "0.05",
    "hotel": "Loft NASS Atahualpa",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Cafe/barRoscas",
    "distance": "0.1",
    "hotel": "Loft NASS Atahualpa",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantChifa",
    "distance": "0.1",
    "hotel": "Loft NASS Atahualpa",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Aboriginal Cultures",
    "distance": "0.5",
    "hotel": "Loft NASS Atahualpa",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Popular Art Museum",
    "distance": "0.55",
    "hotel": "Loft NASS Atahualpa",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Abdon Calderón Park",
    "distance": "0.6",
    "hotel": "Loft NASS Atahualpa",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Straw hat Museum",
    "distance": "0.8",
    "hotel": "Loft NASS Atahualpa",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Pumapungo Museum",
    "distance": "0.8",
    "hotel": "Loft NASS Atahualpa",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Modern Art Museum",
    "distance": "1.2",
    "hotel": "Loft NASS Atahualpa",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Chahuarchimbana House Museum",
    "distance": "1.7",
    "hotel": "Loft NASS Atahualpa",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Metals",
    "distance": "2",
    "hotel": "Loft NASS Atahualpa",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Cajas National Park",
    "distance": "20",
    "hotel": "Loft NASS Atahualpa",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RiverTomebamba River",
    "distance": "0.7",
    "hotel": "Loft NASS Atahualpa",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Mariscal Lamar International Airport",
    "distance": "2",
    "hotel": "Loft NASS Atahualpa",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Modern Art Museum",
    "distance": "0.1",
    "hotel": "Hostal Posada del Angel",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque de San Sebastián",
    "distance": "0.2",
    "hotel": "Hostal Posada del Angel",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque de Los Arupos",
    "distance": "0.3",
    "hotel": "Hostal Posada del Angel",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Orilla corazones",
    "distance": "0.4",
    "hotel": "Hostal Posada del Angel",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Plazoleta de Santo Domingo",
    "distance": "0.4",
    "hotel": "Hostal Posada del Angel",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque de Los Corazones",
    "distance": "0.55",
    "hotel": "Hostal Posada del Angel",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "El Barranco",
    "distance": "0.6",
    "hotel": "Hostal Posada del Angel",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Straw hat Museum",
    "distance": "0.6",
    "hotel": "Hostal Posada del Angel",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Cafe/barCASAMIGOS CAFE",
    "distance": "0.01",
    "hotel": "Hostal Posada del Angel",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantRestaurant Thai Spicy",
    "distance": "0.03",
    "hotel": "Hostal Posada del Angel",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantMangiare Bene",
    "distance": "0.05",
    "hotel": "Hostal Posada del Angel",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of skeletons Doctor Gabriel Moscoso",
    "distance": "0.8",
    "hotel": "Hostal Posada del Angel",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Cañari Identity",
    "distance": "0.9",
    "hotel": "Hostal Posada del Angel",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of Las Conceptas",
    "distance": "0.95",
    "hotel": "Hostal Posada del Angel",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Popular Art Museum",
    "distance": "1.2",
    "hotel": "Hostal Posada del Angel",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Aboriginal Cultures",
    "distance": "1.2",
    "hotel": "Hostal Posada del Angel",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "San Blas square",
    "distance": "1.3",
    "hotel": "Hostal Posada del Angel",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Pumapungo Museum",
    "distance": "1.8",
    "hotel": "Hostal Posada del Angel",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Chahuarchimbana House Museum",
    "distance": "2.6",
    "hotel": "Hostal Posada del Angel",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RiverTomebamba River",
    "distance": "0.85",
    "hotel": "Hostal Posada del Angel",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Mariscal Lamar International Airport",
    "distance": "2.8",
    "hotel": "Hostal Posada del Angel",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of skeletons Doctor Gabriel Moscoso",
    "distance": "0.1",
    "hotel": "Hotel La Orquidea",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Abdon Calderón Park",
    "distance": "0.2",
    "hotel": "Hotel La Orquidea",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Plazoleta de la UNE",
    "distance": "0.25",
    "hotel": "Hotel La Orquidea",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Plazoleta Hermano Miguel",
    "distance": "0.25",
    "hotel": "Hotel La Orquidea",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Plazoleta de Santo Domingo",
    "distance": "0.35",
    "hotel": "Hotel La Orquidea",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of Las Conceptas",
    "distance": "0.4",
    "hotel": "Hotel La Orquidea",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque Victor J. Cuesta",
    "distance": "0.45",
    "hotel": "Hotel La Orquidea",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "San Blas square",
    "distance": "0.5",
    "hotel": "Hotel La Orquidea",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Cafe/barLa Baraca",
    "distance": "0.04",
    "hotel": "Hotel La Orquidea",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantRincón Mar y Tierra",
    "distance": "0.1",
    "hotel": "Hotel La Orquidea",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Cafe/barMoshi Moshi",
    "distance": "0.1",
    "hotel": "Hotel La Orquidea",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Straw hat Museum",
    "distance": "0.55",
    "hotel": "Hotel La Orquidea",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Popular Art Museum",
    "distance": "0.65",
    "hotel": "Hotel La Orquidea",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Aboriginal Cultures",
    "distance": "0.65",
    "hotel": "Hotel La Orquidea",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Modern Art Museum",
    "distance": "0.8",
    "hotel": "Hotel La Orquidea",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Pumapungo Museum",
    "distance": "1.2",
    "hotel": "Hotel La Orquidea",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Chahuarchimbana House Museum",
    "distance": "2",
    "hotel": "Hotel La Orquidea",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RiverTomebamba River",
    "distance": "0.6",
    "hotel": "Hotel La Orquidea",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Mariscal Lamar International Airport",
    "distance": "2.2",
    "hotel": "Hotel La Orquidea",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Plazoleta Hermano Miguel",
    "distance": "0.05",
    "hotel": "Hotel Boutique Castilla de Léon",
    "score": "8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of skeletons Doctor Gabriel Moscoso",
    "distance": "0.25",
    "hotel": "Hotel Boutique Castilla de Léon",
    "score": "8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Abdon Calderón Park",
    "distance": "0.45",
    "hotel": "Hotel Boutique Castilla de Léon",
    "score": "8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Plazoleta de la UNE",
    "distance": "0.45",
    "hotel": "Hotel Boutique Castilla de Léon",
    "score": "8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Plazoleta de Santo Domingo",
    "distance": "0.45",
    "hotel": "Hotel Boutique Castilla de Léon",
    "score": "8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque Victor J. Cuesta",
    "distance": "0.5",
    "hotel": "Hotel Boutique Castilla de Léon",
    "score": "8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantLas Colonias",
    "distance": "0.05",
    "hotel": "Hotel Boutique Castilla de Léon",
    "score": "8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantDöner Janos",
    "distance": "0.05",
    "hotel": "Hotel Boutique Castilla de Léon",
    "score": "8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Cafe/barel cafecito",
    "distance": "0.1",
    "hotel": "Hotel Boutique Castilla de Léon",
    "score": "8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Aboriginal Cultures",
    "distance": "0.8",
    "hotel": "Hotel Boutique Castilla de Léon",
    "score": "8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Popular Art Museum",
    "distance": "0.8",
    "hotel": "Hotel Boutique Castilla de Léon",
    "score": "8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Modern Art Museum",
    "distance": "0.95",
    "hotel": "Hotel Boutique Castilla de Léon",
    "score": "8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Pumapungo Museum",
    "distance": "1.3",
    "hotel": "Hotel Boutique Castilla de Léon",
    "score": "8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Chahuarchimbana House Museum",
    "distance": "2.1",
    "hotel": "Hotel Boutique Castilla de Léon",
    "score": "8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Metals",
    "distance": "2.2",
    "hotel": "Hotel Boutique Castilla de Léon",
    "score": "8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RiverTomebamba River",
    "distance": "0.8",
    "hotel": "Hotel Boutique Castilla de Léon",
    "score": "8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Aboriginal Cultures",
    "distance": "0.04",
    "hotel": "Selina Cuenca",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Popular Art Museum",
    "distance": "0.05",
    "hotel": "Selina Cuenca",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Plazoleta de la Merced",
    "distance": "0.2",
    "hotel": "Selina Cuenca",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of Las Conceptas",
    "distance": "0.25",
    "hotel": "Selina Cuenca",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque de La Madre",
    "distance": "0.25",
    "hotel": "Selina Cuenca",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Plaza de la Música",
    "distance": "0.25",
    "hotel": "Selina Cuenca",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Cañari Identity",
    "distance": "0.35",
    "hotel": "Selina Cuenca",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque Luis Cordero",
    "distance": "0.35",
    "hotel": "Selina Cuenca",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Cafe/barOrigami sushi bar",
    "distance": "0.01",
    "hotel": "Selina Cuenca",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantPuro Mote",
    "distance": "0.01",
    "hotel": "Selina Cuenca",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Cafe/barVieja diablos",
    "distance": "0.01",
    "hotel": "Selina Cuenca",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of skeletons Doctor Gabriel Moscoso",
    "distance": "0.55",
    "hotel": "Selina Cuenca",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "San Blas square",
    "distance": "0.6",
    "hotel": "Selina Cuenca",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Pumapungo Museum",
    "distance": "0.65",
    "hotel": "Selina Cuenca",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Metals",
    "distance": "1.5",
    "hotel": "Selina Cuenca",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Chahuarchimbana House Museum",
    "distance": "1.5",
    "hotel": "Selina Cuenca",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RiverTomebamba River",
    "distance": "0.3",
    "hotel": "Selina Cuenca",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Abdon Calderón Park",
    "distance": "0.1",
    "hotel": "Hotel Posada del Rey",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Plazoleta de la UNE",
    "distance": "0.2",
    "hotel": "Hotel Posada del Rey",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Straw hat Museum",
    "distance": "0.25",
    "hotel": "Hotel Posada del Rey",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of skeletons Doctor Gabriel Moscoso",
    "distance": "0.3",
    "hotel": "Hotel Posada del Rey",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Plazoleta de la Merced",
    "distance": "0.35",
    "hotel": "Hotel Posada del Rey",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "El Barranco",
    "distance": "0.35",
    "hotel": "Hotel Posada del Rey",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantHot dog",
    "distance": "0.01",
    "hotel": "Hotel Posada del Rey",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantHot coffee",
    "distance": "0.03",
    "hotel": "Hotel Posada del Rey",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Cafe/barVinilo",
    "distance": "0.03",
    "hotel": "Hotel Posada del Rey",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Aboriginal Cultures",
    "distance": "0.55",
    "hotel": "Hotel Posada del Rey",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Modern Art Museum",
    "distance": "0.6",
    "hotel": "Hotel Posada del Rey",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "San Blas square",
    "distance": "0.7",
    "hotel": "Hotel Posada del Rey",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Metals",
    "distance": "1.7",
    "hotel": "Hotel Posada del Rey",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RiverTomebamba River",
    "distance": "0.35",
    "hotel": "Hotel Posada del Rey",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Plazoleta de Santo Domingo",
    "distance": "0.15",
    "hotel": "Hotel Azul de la Plaza",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Abdon Calderón Park",
    "distance": "0.3",
    "hotel": "Hotel Azul de la Plaza",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Modern Art Museum",
    "distance": "0.4",
    "hotel": "Hotel Azul de la Plaza",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "María Auxiliadora",
    "distance": "0.45",
    "hotel": "Hotel Azul de la Plaza",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Straw hat Museum",
    "distance": "0.45",
    "hotel": "Hotel Azul de la Plaza",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "El Barranco",
    "distance": "0.5",
    "hotel": "Hotel Azul de la Plaza",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of skeletons Doctor Gabriel Moscoso",
    "distance": "0.5",
    "hotel": "Hotel Azul de la Plaza",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque de San Sebastián",
    "distance": "0.5",
    "hotel": "Hotel Azul de la Plaza",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Plazoleta de la UNE",
    "distance": "0.5",
    "hotel": "Hotel Azul de la Plaza",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Cañari Identity",
    "distance": "0.6",
    "hotel": "Hotel Azul de la Plaza",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantAkelarre",
    "distance": "0.05",
    "hotel": "Hotel Azul de la Plaza",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Cafe/barAkelarre Caffee y Restaurant",
    "distance": "0.05",
    "hotel": "Hotel Azul de la Plaza",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Cafe/barMocachino",
    "distance": "0.1",
    "hotel": "Hotel Azul de la Plaza",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of Las Conceptas",
    "distance": "0.7",
    "hotel": "Hotel Azul de la Plaza",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Popular Art Museum",
    "distance": "0.85",
    "hotel": "Hotel Azul de la Plaza",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Aboriginal Cultures",
    "distance": "0.9",
    "hotel": "Hotel Azul de la Plaza",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "San Blas square",
    "distance": "0.95",
    "hotel": "Hotel Azul de la Plaza",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Pumapungo Museum",
    "distance": "1.6",
    "hotel": "Hotel Azul de la Plaza",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Metals",
    "distance": "1.9",
    "hotel": "Hotel Azul de la Plaza",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Chahuarchimbana House Museum",
    "distance": "2.3",
    "hotel": "Hotel Azul de la Plaza",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RiverTomebamba River",
    "distance": "0.65",
    "hotel": "Hotel Azul de la Plaza",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Mariscal Lamar International Airport",
    "distance": "2.6",
    "hotel": "Hotel Azul de la Plaza",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Modern Art Museum",
    "distance": "0.25",
    "hotel": "Pepe's House Cuenca Boutique Hotel l B&B",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque de San Sebastián",
    "distance": "0.35",
    "hotel": "Pepe's House Cuenca Boutique Hotel l B&B",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Straw hat Museum",
    "distance": "0.4",
    "hotel": "Pepe's House Cuenca Boutique Hotel l B&B",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Abdon Calderón Park",
    "distance": "0.4",
    "hotel": "Pepe's House Cuenca Boutique Hotel l B&B",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque de Los Arupos",
    "distance": "0.45",
    "hotel": "Pepe's House Cuenca Boutique Hotel l B&B",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Orilla corazones",
    "distance": "0.55",
    "hotel": "Pepe's House Cuenca Boutique Hotel l B&B",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Plazoleta de la UNE",
    "distance": "0.6",
    "hotel": "Pepe's House Cuenca Boutique Hotel l B&B",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantJack",
    "distance": "0.1",
    "hotel": "Pepe's House Cuenca Boutique Hotel l B&B",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantOromar",
    "distance": "0.1",
    "hotel": "Pepe's House Cuenca Boutique Hotel l B&B",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Cafe/barMozart",
    "distance": "0.15",
    "hotel": "Pepe's House Cuenca Boutique Hotel l B&B",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of skeletons Doctor Gabriel Moscoso",
    "distance": "0.65",
    "hotel": "Pepe's House Cuenca Boutique Hotel l B&B",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Cañari Identity",
    "distance": "0.7",
    "hotel": "Pepe's House Cuenca Boutique Hotel l B&B",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of Las Conceptas",
    "distance": "0.75",
    "hotel": "Pepe's House Cuenca Boutique Hotel l B&B",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Popular Art Museum",
    "distance": "0.9",
    "hotel": "Pepe's House Cuenca Boutique Hotel l B&B",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Aboriginal Cultures",
    "distance": "0.95",
    "hotel": "Pepe's House Cuenca Boutique Hotel l B&B",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "San Blas square",
    "distance": "1.1",
    "hotel": "Pepe's House Cuenca Boutique Hotel l B&B",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Chahuarchimbana House Museum",
    "distance": "2.4",
    "hotel": "Pepe's House Cuenca Boutique Hotel l B&B",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Mariscal Lamar International Airport",
    "distance": "2.7",
    "hotel": "Pepe's House Cuenca Boutique Hotel l B&B",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Plazoleta Hermano Miguel",
    "distance": "0.1",
    "hotel": "Hostal Mariscal Inn & Suite",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "San Blas square",
    "distance": "0.35",
    "hotel": "Hostal Mariscal Inn & Suite",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Cañari Identity",
    "distance": "0.5",
    "hotel": "Hostal Mariscal Inn & Suite",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Abdon Calderón Park",
    "distance": "0.55",
    "hotel": "Hostal Mariscal Inn & Suite",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Mary Corilé",
    "distance": "0.6",
    "hotel": "Hostal Mariscal Inn & Suite",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Plaza Antiguo Iess",
    "distance": "0.6",
    "hotel": "Hostal Mariscal Inn & Suite",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantEl Gordito",
    "distance": "0.1",
    "hotel": "Hostal Mariscal Inn & Suite",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantParaíso",
    "distance": "0.1",
    "hotel": "Hostal Mariscal Inn & Suite",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Cafe/barel cafecito",
    "distance": "0.15",
    "hotel": "Hostal Mariscal Inn & Suite",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Straw hat Museum",
    "distance": "0.9",
    "hotel": "Hostal Mariscal Inn & Suite",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RiverTomebamba River",
    "distance": "0.9",
    "hotel": "Hostal Mariscal Inn & Suite",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Mariscal Lamar International Airport",
    "distance": "1.8",
    "hotel": "Hostal Mariscal Inn & Suite",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque Júpiter",
    "distance": "0.2",
    "hotel": "Villa Emilia Hostal",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Plaza de la Música",
    "distance": "0.35",
    "hotel": "Villa Emilia Hostal",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque de La Madre",
    "distance": "0.45",
    "hotel": "Villa Emilia Hostal",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque ECU 911",
    "distance": "0.45",
    "hotel": "Villa Emilia Hostal",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque Sagitario",
    "distance": "0.45",
    "hotel": "Villa Emilia Hostal",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque Santa Anita",
    "distance": "0.5",
    "hotel": "Villa Emilia Hostal",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Cancha Parque Santa Anita",
    "distance": "0.5",
    "hotel": "Villa Emilia Hostal",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Popular Art Museum",
    "distance": "0.6",
    "hotel": "Villa Emilia Hostal",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Aboriginal Cultures",
    "distance": "0.6",
    "hotel": "Villa Emilia Hostal",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Pumapungo Museum",
    "distance": "0.6",
    "hotel": "Villa Emilia Hostal",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantViandas Mami July",
    "distance": "0.05",
    "hotel": "Villa Emilia Hostal",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Cafe/barGarden Bar",
    "distance": "0.05",
    "hotel": "Villa Emilia Hostal",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantEl Manantial",
    "distance": "0.1",
    "hotel": "Villa Emilia Hostal",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of Las Conceptas",
    "distance": "0.85",
    "hotel": "Villa Emilia Hostal",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Cañari Identity",
    "distance": "0.95",
    "hotel": "Villa Emilia Hostal",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Metals",
    "distance": "0.001",
    "hotel": "Villa Emilia Hostal",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Chahuarchimbana House Museum",
    "distance": "0.001",
    "hotel": "Villa Emilia Hostal",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Straw hat Museum",
    "distance": "1.1",
    "hotel": "Villa Emilia Hostal",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of skeletons Doctor Gabriel Moscoso",
    "distance": "1.2",
    "hotel": "Villa Emilia Hostal",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Abdon Calderón Park",
    "distance": "1.2",
    "hotel": "Villa Emilia Hostal",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Modern Art Museum",
    "distance": "1.6",
    "hotel": "Villa Emilia Hostal",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RiverTomebamba River",
    "distance": "0.75",
    "hotel": "Villa Emilia Hostal",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Mariscal Lamar International Airport",
    "distance": "2.9",
    "hotel": "Villa Emilia Hostal",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Plazoleta de Santo Domingo",
    "distance": "0.04",
    "hotel": "Morenica del Rosario",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "María Auxiliadora",
    "distance": "0.3",
    "hotel": "Morenica del Rosario",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of skeletons Doctor Gabriel Moscoso",
    "distance": "0.45",
    "hotel": "Morenica del Rosario",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque de San Sebastián",
    "distance": "0.55",
    "hotel": "Morenica del Rosario",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Plazoleta Hermano Miguel",
    "distance": "0.55",
    "hotel": "Morenica del Rosario",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantChicago Pizza",
    "distance": "0.01",
    "hotel": "Morenica del Rosario",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantEl Pedregal Azteca",
    "distance": "0.01",
    "hotel": "Morenica del Rosario",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantQ' Buen Morocho con empanadas al horno",
    "distance": "0.03",
    "hotel": "Morenica del Rosario",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "San Blas square",
    "distance": "0.9",
    "hotel": "Morenica del Rosario",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Metals",
    "distance": "2.1",
    "hotel": "Morenica del Rosario",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque Lineal Río Tarqui",
    "distance": "0.3",
    "hotel": "Four Points by Sheraton Cuenca",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque Bilbao",
    "distance": "0.7",
    "hotel": "Four Points by Sheraton Cuenca",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque Iberia",
    "distance": "0.8",
    "hotel": "Four Points by Sheraton Cuenca",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Metals",
    "distance": "0.95",
    "hotel": "Four Points by Sheraton Cuenca",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque De La Compañia",
    "distance": "0.95",
    "hotel": "Four Points by Sheraton Cuenca",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Cancha de uso múltiple",
    "distance": "1.1",
    "hotel": "Four Points by Sheraton Cuenca",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "El Playón",
    "distance": "1.1",
    "hotel": "Four Points by Sheraton Cuenca",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Valladolid",
    "distance": "1.1",
    "hotel": "Four Points by Sheraton Cuenca",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Virgen de Bronce",
    "distance": "1.2",
    "hotel": "Four Points by Sheraton Cuenca",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque La Plateria",
    "distance": "1.3",
    "hotel": "Four Points by Sheraton Cuenca",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantPizzeria Pomodoro",
    "distance": "0.1",
    "hotel": "Four Points by Sheraton Cuenca",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantMcDonald's",
    "distance": "0.1",
    "hotel": "Four Points by Sheraton Cuenca",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantMayflower",
    "distance": "0.1",
    "hotel": "Four Points by Sheraton Cuenca",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Popular Art Museum",
    "distance": "2.3",
    "hotel": "Four Points by Sheraton Cuenca",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Straw hat Museum",
    "distance": "2.4",
    "hotel": "Four Points by Sheraton Cuenca",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Aboriginal Cultures",
    "distance": "2.4",
    "hotel": "Four Points by Sheraton Cuenca",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Pumapungo Museum",
    "distance": "2.5",
    "hotel": "Four Points by Sheraton Cuenca",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of Las Conceptas",
    "distance": "2.6",
    "hotel": "Four Points by Sheraton Cuenca",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Cañari Identity",
    "distance": "2.7",
    "hotel": "Four Points by Sheraton Cuenca",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Modern Art Museum",
    "distance": "2.7",
    "hotel": "Four Points by Sheraton Cuenca",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of skeletons Doctor Gabriel Moscoso",
    "distance": "2.9",
    "hotel": "Four Points by Sheraton Cuenca",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "San Blas square",
    "distance": "3",
    "hotel": "Four Points by Sheraton Cuenca",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RiverTomebamba River",
    "distance": "2.3",
    "hotel": "Four Points by Sheraton Cuenca",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Mariscal Lamar International Airport",
    "distance": "4.7",
    "hotel": "Four Points by Sheraton Cuenca",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque Puertas del Sol",
    "distance": "0.6",
    "hotel": "Hotel Nass Pinar del Lago",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Cancha Sintética",
    "distance": "1.2",
    "hotel": "Hotel Nass Pinar del Lago",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque San Pedro del Cebollar",
    "distance": "1.2",
    "hotel": "Hotel Nass Pinar del Lago",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Redondel Feria Libre",
    "distance": "1.3",
    "hotel": "Hotel Nass Pinar del Lago",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque Del Molinero",
    "distance": "1.4",
    "hotel": "Hotel Nass Pinar del Lago",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque Juan Stiehle",
    "distance": "1.5",
    "hotel": "Hotel Nass Pinar del Lago",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque Darwin",
    "distance": "1.6",
    "hotel": "Hotel Nass Pinar del Lago",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque del Dragón",
    "distance": "1.6",
    "hotel": "Hotel Nass Pinar del Lago",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Básquet y Fútbol",
    "distance": "1.7",
    "hotel": "Hotel Nass Pinar del Lago",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque El Ángel",
    "distance": "1.8",
    "hotel": "Hotel Nass Pinar del Lago",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantLa Pampa",
    "distance": "0.1",
    "hotel": "Hotel Nass Pinar del Lago",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantThe Vegetable Bar",
    "distance": "0.4",
    "hotel": "Hotel Nass Pinar del Lago",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantEl Faro",
    "distance": "0.5",
    "hotel": "Hotel Nass Pinar del Lago",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Modern Art Museum",
    "distance": "2.8",
    "hotel": "Hotel Nass Pinar del Lago",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Straw hat Museum",
    "distance": "3.3",
    "hotel": "Hotel Nass Pinar del Lago",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of skeletons Doctor Gabriel Moscoso",
    "distance": "3.6",
    "hotel": "Hotel Nass Pinar del Lago",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Cañari Identity",
    "distance": "3.7",
    "hotel": "Hotel Nass Pinar del Lago",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of Las Conceptas",
    "distance": "3.7",
    "hotel": "Hotel Nass Pinar del Lago",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Popular Art Museum",
    "distance": "3.8",
    "hotel": "Hotel Nass Pinar del Lago",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Metals",
    "distance": "3.8",
    "hotel": "Hotel Nass Pinar del Lago",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Aboriginal Cultures",
    "distance": "3.9",
    "hotel": "Hotel Nass Pinar del Lago",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Pumapungo Museum",
    "distance": "4.5",
    "hotel": "Hotel Nass Pinar del Lago",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Chahuarchimbana House Museum",
    "distance": "5",
    "hotel": "Hotel Nass Pinar del Lago",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RiverTomebamba River",
    "distance": "3.5",
    "hotel": "Hotel Nass Pinar del Lago",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Mariscal Lamar International Airport",
    "distance": "5",
    "hotel": "Hotel Nass Pinar del Lago",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "15 AREAS DEL INTERIOR DE LA CUENCA DEL RIO PAUTE",
    "distance": "1.5",
    "hotel": "Hosteria Dos Chorreras",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Cajas National Park",
    "distance": "6",
    "hotel": "Hosteria Dos Chorreras",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "15 AREAS DEL INTERIOR DE LA CUENCA DEL RIO PAUTE",
    "distance": "10",
    "hotel": "Hosteria Dos Chorreras",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Quinta Filita",
    "distance": "15",
    "hotel": "Hosteria Dos Chorreras",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "15 AREAS DEL INTERIOR DE LA CUENCA DEL RIO PAUTE",
    "distance": "15",
    "hotel": "Hosteria Dos Chorreras",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Cancha de juego",
    "distance": "19",
    "hotel": "Hosteria Dos Chorreras",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque Central",
    "distance": "19",
    "hotel": "Hosteria Dos Chorreras",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque San Pedro del Cebollar",
    "distance": "19",
    "hotel": "Hosteria Dos Chorreras",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Plaza de Baños",
    "distance": "19",
    "hotel": "Hosteria Dos Chorreras",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Plaza central de Checa",
    "distance": "20",
    "hotel": "Hosteria Dos Chorreras",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantLa Casa Vieja",
    "distance": "2.7",
    "hotel": "Hosteria Dos Chorreras",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantHermanos Prado",
    "distance": "10",
    "hotel": "Hosteria Dos Chorreras",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantCapilla Pamba",
    "distance": "14",
    "hotel": "Hosteria Dos Chorreras",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RiverTomebamba River",
    "distance": "22",
    "hotel": "Hosteria Dos Chorreras",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Mariscal Lamar International Airport",
    "distance": "24",
    "hotel": "Hosteria Dos Chorreras",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque de las Américas",
    "distance": "0.1",
    "hotel": "Guesthouse Bella Vista",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque La Libertad",
    "distance": "0.25",
    "hotel": "Guesthouse Bella Vista",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque Fray Jodoco Ricke",
    "distance": "0.55",
    "hotel": "Guesthouse Bella Vista",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Plaza Del Arte",
    "distance": "0.6",
    "hotel": "Guesthouse Bella Vista",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "María Auxiliadora",
    "distance": "0.6",
    "hotel": "Guesthouse Bella Vista",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Cristo Rey",
    "distance": "0.7",
    "hotel": "Guesthouse Bella Vista",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque de San Sebastián",
    "distance": "0.85",
    "hotel": "Guesthouse Bella Vista",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Plazoleta de Santo Domingo",
    "distance": "0.85",
    "hotel": "Guesthouse Bella Vista",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Modern Art Museum",
    "distance": "0.9",
    "hotel": "Guesthouse Bella Vista",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Canchas de la Floresta 2",
    "distance": "0.9",
    "hotel": "Guesthouse Bella Vista",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantBamboo Grill",
    "distance": "0.15",
    "hotel": "Guesthouse Bella Vista",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Cafe/barCafé cale",
    "distance": "0.2",
    "hotel": "Guesthouse Bella Vista",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantViko al carbón",
    "distance": "0.25",
    "hotel": "Guesthouse Bella Vista",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of skeletons Doctor Gabriel Moscoso",
    "distance": "1.3",
    "hotel": "Guesthouse Bella Vista",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Straw hat Museum",
    "distance": "1.4",
    "hotel": "Guesthouse Bella Vista",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Cañari Identity",
    "distance": "1.5",
    "hotel": "Guesthouse Bella Vista",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of Las Conceptas",
    "distance": "1.6",
    "hotel": "Guesthouse Bella Vista",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "San Blas square",
    "distance": "1.7",
    "hotel": "Guesthouse Bella Vista",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Popular Art Museum",
    "distance": "1.8",
    "hotel": "Guesthouse Bella Vista",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Aboriginal Cultures",
    "distance": "1.8",
    "hotel": "Guesthouse Bella Vista",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Pumapungo Museum",
    "distance": "2.4",
    "hotel": "Guesthouse Bella Vista",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Metals",
    "distance": "2.8",
    "hotel": "Guesthouse Bella Vista",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Chahuarchimbana House Museum",
    "distance": "3.2",
    "hotel": "Guesthouse Bella Vista",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RiverTomebamba River",
    "distance": "1.6",
    "hotel": "Guesthouse Bella Vista",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Plazoleta de Santo Domingo",
    "distance": "0.1",
    "hotel": "Itza Hotel Boutique Internacional",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Abdon Calderón Park",
    "distance": "0.25",
    "hotel": "Itza Hotel Boutique Internacional",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "María Auxiliadora",
    "distance": "0.35",
    "hotel": "Itza Hotel Boutique Internacional",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of Las Conceptas",
    "distance": "0.6",
    "hotel": "Itza Hotel Boutique Internacional",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantLa Fornace",
    "distance": "0.02",
    "hotel": "Itza Hotel Boutique Internacional",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantEucaliptos",
    "distance": "0.02",
    "hotel": "Itza Hotel Boutique Internacional",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Cafe/barLiron Liron Bar Restaurante",
    "distance": "0.03",
    "hotel": "Itza Hotel Boutique Internacional",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "San Blas square",
    "distance": "0.75",
    "hotel": "Itza Hotel Boutique Internacional",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Aboriginal Cultures",
    "distance": "0.85",
    "hotel": "Itza Hotel Boutique Internacional",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Pumapungo Museum",
    "distance": "1.5",
    "hotel": "Itza Hotel Boutique Internacional",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Mariscal Lamar International Airport",
    "distance": "2.3",
    "hotel": "Itza Hotel Boutique Internacional",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "María Auxiliadora",
    "distance": "0.15",
    "hotel": "Hostal Casa de Lidice",
    "score": "9.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Plazoleta de Santo Domingo",
    "distance": "0.2",
    "hotel": "Hostal Casa de Lidice",
    "score": "9.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Abdon Calderón Park",
    "distance": "0.5",
    "hotel": "Hostal Casa de Lidice",
    "score": "9.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Modern Art Museum",
    "distance": "0.5",
    "hotel": "Hostal Casa de Lidice",
    "score": "9.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque de San Sebastián",
    "distance": "0.6",
    "hotel": "Hostal Casa de Lidice",
    "score": "9.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of skeletons Doctor Gabriel Moscoso",
    "distance": "0.6",
    "hotel": "Hostal Casa de Lidice",
    "score": "9.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Plazoleta Hermano Miguel",
    "distance": "0.65",
    "hotel": "Hostal Casa de Lidice",
    "score": "9.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Plazoleta de la UNE",
    "distance": "0.7",
    "hotel": "Hostal Casa de Lidice",
    "score": "9.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Straw hat Museum",
    "distance": "0.7",
    "hotel": "Hostal Casa de Lidice",
    "score": "9.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque de Los Arupos",
    "distance": "0.75",
    "hotel": "Hostal Casa de Lidice",
    "score": "9.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantSabor Costeño",
    "distance": "0.05",
    "hotel": "Hostal Casa de Lidice",
    "score": "9.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantCarnivoros",
    "distance": "0.05",
    "hotel": "Hostal Casa de Lidice",
    "score": "9.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Restaurantchikiluki",
    "distance": "0.05",
    "hotel": "Hostal Casa de Lidice",
    "score": "9.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Cañari Identity",
    "distance": "0.8",
    "hotel": "Hostal Casa de Lidice",
    "score": "9.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Popular Art Museum",
    "distance": "1.1",
    "hotel": "Hostal Casa de Lidice",
    "score": "9.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Pumapungo Museum",
    "distance": "1.7",
    "hotel": "Hostal Casa de Lidice",
    "score": "9.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Chahuarchimbana House Museum",
    "distance": "2.5",
    "hotel": "Hostal Casa de Lidice",
    "score": "9.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RiverTomebamba River",
    "distance": "0.95",
    "hotel": "Hostal Casa de Lidice",
    "score": "9.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Mariscal Lamar International Airport",
    "distance": "2.4",
    "hotel": "Hostal Casa de Lidice",
    "score": "9.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Orilla corazones",
    "distance": "0.1",
    "hotel": "Apartamentos Otorongo Cuenca Ecuador",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque de Los Arupos",
    "distance": "0.2",
    "hotel": "Apartamentos Otorongo Cuenca Ecuador",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque de Los Corazones",
    "distance": "0.25",
    "hotel": "Apartamentos Otorongo Cuenca Ecuador",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque Napo",
    "distance": "0.55",
    "hotel": "Apartamentos Otorongo Cuenca Ecuador",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque La fogata",
    "distance": "0.55",
    "hotel": "Apartamentos Otorongo Cuenca Ecuador",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Plaza Del Arte",
    "distance": "0.7",
    "hotel": "Apartamentos Otorongo Cuenca Ecuador",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque Angostura",
    "distance": "0.75",
    "hotel": "Apartamentos Otorongo Cuenca Ecuador",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "La Gloria",
    "distance": "0.75",
    "hotel": "Apartamentos Otorongo Cuenca Ecuador",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantMolinos Del Batan",
    "distance": "0.1",
    "hotel": "Apartamentos Otorongo Cuenca Ecuador",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Cafe/barCafetería Imay",
    "distance": "0.2",
    "hotel": "Apartamentos Otorongo Cuenca Ecuador",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantOro mar marisquería",
    "distance": "0.2",
    "hotel": "Apartamentos Otorongo Cuenca Ecuador",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Straw hat Museum",
    "distance": "0.85",
    "hotel": "Apartamentos Otorongo Cuenca Ecuador",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Cañari Identity",
    "distance": "1.3",
    "hotel": "Apartamentos Otorongo Cuenca Ecuador",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of Las Conceptas",
    "distance": "1.4",
    "hotel": "Apartamentos Otorongo Cuenca Ecuador",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Popular Art Museum",
    "distance": "1.4",
    "hotel": "Apartamentos Otorongo Cuenca Ecuador",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Aboriginal Cultures",
    "distance": "1.5",
    "hotel": "Apartamentos Otorongo Cuenca Ecuador",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Pumapungo Museum",
    "distance": "2.1",
    "hotel": "Apartamentos Otorongo Cuenca Ecuador",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Chahuarchimbana House Museum",
    "distance": "2.8",
    "hotel": "Apartamentos Otorongo Cuenca Ecuador",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RiverTomebamba River",
    "distance": "1.2",
    "hotel": "Apartamentos Otorongo Cuenca Ecuador",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Mariscal Lamar International Airport",
    "distance": "3.4",
    "hotel": "Apartamentos Otorongo Cuenca Ecuador",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of skeletons Doctor Gabriel Moscoso",
    "distance": "0.2",
    "hotel": "El Dorado Hotel",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Plazoleta Hermano Miguel",
    "distance": "0.3",
    "hotel": "El Dorado Hotel",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Cañari Identity",
    "distance": "0.4",
    "hotel": "El Dorado Hotel",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of Las Conceptas",
    "distance": "0.5",
    "hotel": "El Dorado Hotel",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque Victor J. Cuesta",
    "distance": "0.55",
    "hotel": "El Dorado Hotel",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantGoda",
    "distance": "0.01",
    "hotel": "El Dorado Hotel",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantPicantes de Leo",
    "distance": "0.05",
    "hotel": "El Dorado Hotel",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantPavón Real",
    "distance": "0.05",
    "hotel": "El Dorado Hotel",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Modern Art Museum",
    "distance": "0.75",
    "hotel": "El Dorado Hotel",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Popular Art Museum",
    "distance": "0.75",
    "hotel": "El Dorado Hotel",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "El Barranco",
    "distance": "0.45",
    "hotel": "Check Inn Bed and Breakfast",
    "score": "7.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantAkelarre",
    "distance": "0.03",
    "hotel": "Check Inn Bed and Breakfast",
    "score": "7.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Cafe/barAkelarre Caffee y Restaurant",
    "distance": "0.04",
    "hotel": "Check Inn Bed and Breakfast",
    "score": "7.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantRestaurant El Asador N: 2",
    "distance": "0.1",
    "hotel": "Check Inn Bed and Breakfast",
    "score": "7.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of Las Conceptas",
    "distance": "0.65",
    "hotel": "Check Inn Bed and Breakfast",
    "score": "7.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque de La Madre",
    "distance": "0.35",
    "hotel": "Hotel Valgus",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque Sagitario",
    "distance": "0.4",
    "hotel": "Hotel Valgus",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque Las Candelas",
    "distance": "0.5",
    "hotel": "Hotel Valgus",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Popular Art Museum",
    "distance": "0.5",
    "hotel": "Hotel Valgus",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Plazoleta de la Merced",
    "distance": "0.55",
    "hotel": "Hotel Valgus",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "El Barranco",
    "distance": "0.55",
    "hotel": "Hotel Valgus",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Plaza de la Música",
    "distance": "0.55",
    "hotel": "Hotel Valgus",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque Júpiter",
    "distance": "0.6",
    "hotel": "Hotel Valgus",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantDomino's Pizza",
    "distance": "0.05",
    "hotel": "Hotel Valgus",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantRomolo e Remo",
    "distance": "0.15",
    "hotel": "Hotel Valgus",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantVrinda Vegetarian Restaurant",
    "distance": "0.2",
    "hotel": "Hotel Valgus",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Abdon Calderón Park",
    "distance": "0.85",
    "hotel": "Hotel Valgus",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of the Metals",
    "distance": "0.9",
    "hotel": "Hotel Valgus",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Museum of skeletons Doctor Gabriel Moscoso",
    "distance": "0.001",
    "hotel": "Hotel Valgus",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Pumapungo Museum",
    "distance": "1.1",
    "hotel": "Hotel Valgus",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "San Blas square",
    "distance": "1.2",
    "hotel": "Hotel Valgus",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Chahuarchimbana House Museum",
    "distance": "1.6",
    "hotel": "Hotel Valgus",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RiverTomebamba River",
    "distance": "0.4",
    "hotel": "Hotel Valgus",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Mariscal Lamar International Airport",
    "distance": "3",
    "hotel": "Hotel Valgus",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "El Barranco",
    "distance": "0.3",
    "hotel": "Hotel Spa Santa Ana",
    "score": "7.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Modern Art Museum",
    "distance": "0.3",
    "hotel": "Hotel Spa Santa Ana",
    "score": "7.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Abdon Calderón Park",
    "distance": "0.35",
    "hotel": "Hotel Spa Santa Ana",
    "score": "7.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque de San Sebastián",
    "distance": "0.45",
    "hotel": "Hotel Spa Santa Ana",
    "score": "7.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Parque de Los Arupos",
    "distance": "0.5",
    "hotel": "Hotel Spa Santa Ana",
    "score": "7.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Plazoleta de la UNE",
    "distance": "0.55",
    "hotel": "Hotel Spa Santa Ana",
    "score": "7.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Plazoleta de la Merced",
    "distance": "0.6",
    "hotel": "Hotel Spa Santa Ana",
    "score": "7.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "Cafe/barCafe Aurora Calle",
    "distance": "0.05",
    "hotel": "Hotel Spa Santa Ana",
    "score": "7.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantSegundo hogar",
    "distance": "0.1",
    "hotel": "Hotel Spa Santa Ana",
    "score": "7.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RestaurantRestaurant El Asador N: 2",
    "distance": "0.15",
    "hotel": "Hotel Spa Santa Ana",
    "score": "7.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "San Blas square",
    "distance": "0.001",
    "hotel": "Hotel Spa Santa Ana",
    "score": "7.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Cuenca",
    "places": "RiverTomebamba River",
    "distance": "0.55",
    "hotel": "Hotel Spa Santa Ana",
    "score": "7.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "La Alameda Park",
    "distance": "0.1",
    "hotel": "Hotel David",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Plaza de la Republica",
    "distance": "0.25",
    "hotel": "Hotel David",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "La Tolita",
    "distance": "0.35",
    "hotel": "Hotel David",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque García Moreno",
    "distance": "0.5",
    "hotel": "Hotel David",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque Julio Matovelle",
    "distance": "0.7",
    "hotel": "Hotel David",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Theatre Square",
    "distance": "0.8",
    "hotel": "Hotel David",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque El Ejido",
    "distance": "0.8",
    "hotel": "Hotel David",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Del Arbolito Park",
    "distance": "0.8",
    "hotel": "Hotel David",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Itchimbia Park",
    "distance": "0.9",
    "hotel": "Hotel David",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "San Agustin Square",
    "distance": "1.1",
    "hotel": "Hotel David",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantAsia.com",
    "distance": "0.04",
    "hotel": "Hotel David",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantUku Pacha",
    "distance": "0.05",
    "hotel": "Hotel David",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantChifa Xin Yuan",
    "distance": "0.1",
    "hotel": "Hotel David",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "El Ejido Park",
    "distance": "1.1",
    "hotel": "Hotel David",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Independence Square",
    "distance": "1.2",
    "hotel": "Hotel David",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Colonial Art Museum",
    "distance": "1.3",
    "hotel": "Hotel David",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Casa del Alabado Museum",
    "distance": "1.7",
    "hotel": "Hotel David",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Templo de la Patria Museum",
    "distance": "2.9",
    "hotel": "Hotel David",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Ecuador Natural Science Museum",
    "distance": "3.9",
    "hotel": "Hotel David",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Quito's Vivarium",
    "distance": "3.9",
    "hotel": "Hotel David",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Rumipamba Archaeological Park",
    "distance": "4.1",
    "hotel": "Hotel David",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Capilla del Hombre Museum",
    "distance": "4.6",
    "hotel": "Hotel David",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Guayasamin Museum",
    "distance": "4.7",
    "hotel": "Hotel David",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "TrainTerminal de Ferrocarriles",
    "distance": "2.9",
    "hotel": "Hotel David",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "TrainChimbacalle",
    "distance": "2.9",
    "hotel": "Hotel David",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Quito Mariscal Sucre International Airport",
    "distance": "19",
    "hotel": "Hotel David",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Santo Domingo Square",
    "distance": "0.2",
    "hotel": "Rincón Familiar Hostel Boutique",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "San Agustin Square",
    "distance": "0.25",
    "hotel": "Rincón Familiar Hostel Boutique",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Independence Square",
    "distance": "0.3",
    "hotel": "Rincón Familiar Hostel Boutique",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque Iglesia Inmaculada",
    "distance": "0.4",
    "hotel": "Rincón Familiar Hostel Boutique",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "San Francisco Square",
    "distance": "0.45",
    "hotel": "Rincón Familiar Hostel Boutique",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Theatre Square",
    "distance": "0.5",
    "hotel": "Rincón Familiar Hostel Boutique",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Casa del Alabado Museum",
    "distance": "0.55",
    "hotel": "Rincón Familiar Hostel Boutique",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Colonial Art Museum",
    "distance": "0.6",
    "hotel": "Rincón Familiar Hostel Boutique",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque Cumandá",
    "distance": "0.65",
    "hotel": "Rincón Familiar Hostel Boutique",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque",
    "distance": "0.8",
    "hotel": "Rincón Familiar Hostel Boutique",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Cafe/barCafe Dios No Muere",
    "distance": "0.05",
    "hotel": "Rincón Familiar Hostel Boutique",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantBellavista",
    "distance": "0.05",
    "hotel": "Rincón Familiar Hostel Boutique",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantNuevo Cordovéz",
    "distance": "0.1",
    "hotel": "Rincón Familiar Hostel Boutique",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "La Alameda Park",
    "distance": "1.3",
    "hotel": "Rincón Familiar Hostel Boutique",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Itchimbia Park",
    "distance": "1.4",
    "hotel": "Rincón Familiar Hostel Boutique",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Templo de la Patria Museum",
    "distance": "1.9",
    "hotel": "Rincón Familiar Hostel Boutique",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Foch Square",
    "distance": "3.2",
    "hotel": "Rincón Familiar Hostel Boutique",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Rumipamba Archaeological Park",
    "distance": "5",
    "hotel": "Rincón Familiar Hostel Boutique",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Ecuador Natural Science Museum",
    "distance": "5",
    "hotel": "Rincón Familiar Hostel Boutique",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Quito's Vivarium",
    "distance": "5",
    "hotel": "Rincón Familiar Hostel Boutique",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Capilla del Hombre Museum",
    "distance": "6",
    "hotel": "Rincón Familiar Hostel Boutique",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Guayasamin Museum",
    "distance": "6",
    "hotel": "Rincón Familiar Hostel Boutique",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "TrainTerminal de Ferrocarriles",
    "distance": "1.8",
    "hotel": "Rincón Familiar Hostel Boutique",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "TrainChimbacalle",
    "distance": "1.9",
    "hotel": "Rincón Familiar Hostel Boutique",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Quito Mariscal Sucre International Airport",
    "distance": "20",
    "hotel": "Rincón Familiar Hostel Boutique",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Colonial Art Museum",
    "distance": "0.15",
    "hotel": "Adamas House Hotel Boutique",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque Iglesia Inmaculada",
    "distance": "0.25",
    "hotel": "Adamas House Hotel Boutique",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Independence Square",
    "distance": "0.4",
    "hotel": "Adamas House Hotel Boutique",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Theatre Square",
    "distance": "0.45",
    "hotel": "Adamas House Hotel Boutique",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "San Agustin Square",
    "distance": "0.5",
    "hotel": "Adamas House Hotel Boutique",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "San Francisco Square",
    "distance": "0.55",
    "hotel": "Adamas House Hotel Boutique",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque Julio Matovelle",
    "distance": "0.6",
    "hotel": "Adamas House Hotel Boutique",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque García Moreno",
    "distance": "0.6",
    "hotel": "Adamas House Hotel Boutique",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Casa del Alabado Museum",
    "distance": "0.7",
    "hotel": "Adamas House Hotel Boutique",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "La Tolita",
    "distance": "0.75",
    "hotel": "Adamas House Hotel Boutique",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantMote Colonial",
    "distance": "0.04",
    "hotel": "Adamas House Hotel Boutique",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantSabor y Sazón",
    "distance": "0.1",
    "hotel": "Adamas House Hotel Boutique",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantCafetería Cachito II",
    "distance": "0.1",
    "hotel": "Adamas House Hotel Boutique",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Santo Domingo Square",
    "distance": "0.85",
    "hotel": "Adamas House Hotel Boutique",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "La Alameda Park",
    "distance": "1.1",
    "hotel": "Adamas House Hotel Boutique",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Templo de la Patria Museum",
    "distance": "1.8",
    "hotel": "Adamas House Hotel Boutique",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Foch Square",
    "distance": "2.8",
    "hotel": "Adamas House Hotel Boutique",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Rumipamba Archaeological Park",
    "distance": "4.4",
    "hotel": "Adamas House Hotel Boutique",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Ecuador Natural Science Museum",
    "distance": "4.6",
    "hotel": "Adamas House Hotel Boutique",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Quito's Vivarium",
    "distance": "4.6",
    "hotel": "Adamas House Hotel Boutique",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "TrainTerminal de Ferrocarriles",
    "distance": "2.5",
    "hotel": "Adamas House Hotel Boutique",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "TrainChimbacalle",
    "distance": "2.5",
    "hotel": "Adamas House Hotel Boutique",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque Gabriela Mistral",
    "distance": "0.05",
    "hotel": "Boutique Hotel Antinea",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Foch Square",
    "distance": "0.2",
    "hotel": "Boutique Hotel Antinea",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Santa Fe",
    "distance": "0.4",
    "hotel": "Boutique Hotel Antinea",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque Julio Andrade Marín",
    "distance": "0.8",
    "hotel": "Boutique Hotel Antinea",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Polipasto",
    "distance": "0.85",
    "hotel": "Boutique Hotel Antinea",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Polibosque",
    "distance": "0.85",
    "hotel": "Boutique Hotel Antinea",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque de Santa Clara de San Millán",
    "distance": "1.1",
    "hotel": "Boutique Hotel Antinea",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque Latinoamerica",
    "distance": "1.2",
    "hotel": "Boutique Hotel Antinea",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Redondel del Coliseo Rumiñahui",
    "distance": "1.2",
    "hotel": "Boutique Hotel Antinea",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantLa petite mariscal",
    "distance": "0.02",
    "hotel": "Boutique Hotel Antinea",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Cafe/barPandora lab",
    "distance": "0.03",
    "hotel": "Boutique Hotel Antinea",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantTrattoria Pizzeria Cosa Nostra",
    "distance": "0.04",
    "hotel": "Boutique Hotel Antinea",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Del Arbolito Park",
    "distance": "1.3",
    "hotel": "Boutique Hotel Antinea",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque El Ejido",
    "distance": "1.4",
    "hotel": "Boutique Hotel Antinea",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Ecuador Natural Science Museum",
    "distance": "2",
    "hotel": "Boutique Hotel Antinea",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Quito's Vivarium",
    "distance": "2.1",
    "hotel": "Boutique Hotel Antinea",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Capilla del Hombre Museum",
    "distance": "2.6",
    "hotel": "Boutique Hotel Antinea",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Guayasamin Museum",
    "distance": "2.6",
    "hotel": "Boutique Hotel Antinea",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Rumipamba Archaeological Park",
    "distance": "3",
    "hotel": "Boutique Hotel Antinea",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Colonial Art Museum",
    "distance": "3.2",
    "hotel": "Boutique Hotel Antinea",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Casa del Alabado Museum",
    "distance": "3.7",
    "hotel": "Boutique Hotel Antinea",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Templo de la Patria Museum",
    "distance": "4.7",
    "hotel": "Boutique Hotel Antinea",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "TrainTerminal de Ferrocarriles",
    "distance": "4.9",
    "hotel": "Boutique Hotel Antinea",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "TrainChimbacalle",
    "distance": "5",
    "hotel": "Boutique Hotel Antinea",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Quito Mariscal Sucre International Airport",
    "distance": "17",
    "hotel": "Boutique Hotel Antinea",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "PROINSA",
    "distance": "0.55",
    "hotel": "Hotel Bellavista Quito",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Guayasamin Museum",
    "distance": "0.65",
    "hotel": "Hotel Bellavista Quito",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Capilla del Hombre Museum",
    "distance": "0.65",
    "hotel": "Hotel Bellavista Quito",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Plaza Argentina",
    "distance": "0.7",
    "hotel": "Hotel Bellavista Quito",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque México",
    "distance": "0.85",
    "hotel": "Hotel Bellavista Quito",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Guapulo Park",
    "distance": "0.9",
    "hotel": "Hotel Bellavista Quito",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "República Dominicana",
    "distance": "1.1",
    "hotel": "Hotel Bellavista Quito",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Tribuna de los Shyris",
    "distance": "1.1",
    "hotel": "Hotel Bellavista Quito",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Jardín de los Niños",
    "distance": "1.1",
    "hotel": "Hotel Bellavista Quito",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Turquia",
    "distance": "1.2",
    "hotel": "Hotel Bellavista Quito",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantChivo Loco",
    "distance": "0.35",
    "hotel": "Hotel Bellavista Quito",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantAlma",
    "distance": "0.4",
    "hotel": "Hotel Bellavista Quito",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantNigiri",
    "distance": "0.45",
    "hotel": "Hotel Bellavista Quito",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "La Carolina Park",
    "distance": "1.2",
    "hotel": "Hotel Bellavista Quito",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Ecuador Natural Science Museum",
    "distance": "1.2",
    "hotel": "Hotel Bellavista Quito",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Quito's Vivarium",
    "distance": "1.4",
    "hotel": "Hotel Bellavista Quito",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Foch Square",
    "distance": "2.3",
    "hotel": "Hotel Bellavista Quito",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Rumipamba Archaeological Park",
    "distance": "3.1",
    "hotel": "Hotel Bellavista Quito",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Theatre Square",
    "distance": "5",
    "hotel": "Hotel Bellavista Quito",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "San Agustin Square",
    "distance": "5",
    "hotel": "Hotel Bellavista Quito",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Colonial Art Museum",
    "distance": "5",
    "hotel": "Hotel Bellavista Quito",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Casa del Alabado Museum",
    "distance": "6",
    "hotel": "Hotel Bellavista Quito",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Templo de la Patria Museum",
    "distance": "7",
    "hotel": "Hotel Bellavista Quito",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "TrainTerminal de Ferrocarriles",
    "distance": "7",
    "hotel": "Hotel Bellavista Quito",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "TrainChimbacalle",
    "distance": "7",
    "hotel": "Hotel Bellavista Quito",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Quito Mariscal Sucre International Airport",
    "distance": "15",
    "hotel": "Hotel Bellavista Quito",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "La Alameda Park",
    "distance": "0.2",
    "hotel": "Hotel Bernys Estrellita",
    "score": "7.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "La Tolita",
    "distance": "0.3",
    "hotel": "Hotel Bernys Estrellita",
    "score": "7.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Plaza de la Republica",
    "distance": "0.4",
    "hotel": "Hotel Bernys Estrellita",
    "score": "7.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque García Moreno",
    "distance": "0.45",
    "hotel": "Hotel Bernys Estrellita",
    "score": "7.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Theatre Square",
    "distance": "0.65",
    "hotel": "Hotel Bernys Estrellita",
    "score": "7.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque Julio Matovelle",
    "distance": "0.65",
    "hotel": "Hotel Bernys Estrellita",
    "score": "7.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Itchimbia Park",
    "distance": "0.8",
    "hotel": "Hotel Bernys Estrellita",
    "score": "7.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "San Agustin Square",
    "distance": "0.85",
    "hotel": "Hotel Bernys Estrellita",
    "score": "7.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque El Ejido",
    "distance": "0.95",
    "hotel": "Hotel Bernys Estrellita",
    "score": "7.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Del Arbolito Park",
    "distance": "0.95",
    "hotel": "Hotel Bernys Estrellita",
    "score": "7.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantCactus Food and Drink",
    "distance": "0",
    "hotel": "Hotel Bernys Estrellita",
    "score": "7.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantUku Pacha",
    "distance": "0.1",
    "hotel": "Hotel Bernys Estrellita",
    "score": "7.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantRestaurante El Mesón",
    "distance": "0.1",
    "hotel": "Hotel Bernys Estrellita",
    "score": "7.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Independence Square",
    "distance": "1.1",
    "hotel": "Hotel Bernys Estrellita",
    "score": "7.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Colonial Art Museum",
    "distance": "1.2",
    "hotel": "Hotel Bernys Estrellita",
    "score": "7.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Santo Domingo Square",
    "distance": "1.3",
    "hotel": "Hotel Bernys Estrellita",
    "score": "7.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Casa del Alabado Museum",
    "distance": "1.6",
    "hotel": "Hotel Bernys Estrellita",
    "score": "7.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Templo de la Patria Museum",
    "distance": "2.8",
    "hotel": "Hotel Bernys Estrellita",
    "score": "7.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Ecuador Natural Science Museum",
    "distance": "4",
    "hotel": "Hotel Bernys Estrellita",
    "score": "7.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Quito's Vivarium",
    "distance": "4.1",
    "hotel": "Hotel Bernys Estrellita",
    "score": "7.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Rumipamba Archaeological Park",
    "distance": "4.3",
    "hotel": "Hotel Bernys Estrellita",
    "score": "7.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Capilla del Hombre Museum",
    "distance": "4.8",
    "hotel": "Hotel Bernys Estrellita",
    "score": "7.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Guayasamin Museum",
    "distance": "4.8",
    "hotel": "Hotel Bernys Estrellita",
    "score": "7.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "TrainTerminal de Ferrocarriles",
    "distance": "2.8",
    "hotel": "Hotel Bernys Estrellita",
    "score": "7.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "TrainChimbacalle",
    "distance": "2.8",
    "hotel": "Hotel Bernys Estrellita",
    "score": "7.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Quito's Vivarium",
    "distance": "0.25",
    "hotel": "Wyndham Garden Quito",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Ecuador Natural Science Museum",
    "distance": "0.35",
    "hotel": "Wyndham Garden Quito",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Jardín de los Niños",
    "distance": "0.4",
    "hotel": "Wyndham Garden Quito",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Josemaría Escrivá de Balaguer",
    "distance": "0.4",
    "hotel": "Wyndham Garden Quito",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque EPMAPS",
    "distance": "0.4",
    "hotel": "Wyndham Garden Quito",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "La Carolina Park",
    "distance": "0.6",
    "hotel": "Wyndham Garden Quito",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Centro Deportivo - Ministerio del Deporte",
    "distance": "0.6",
    "hotel": "Wyndham Garden Quito",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Tribuna de los Shyris",
    "distance": "0.7",
    "hotel": "Wyndham Garden Quito",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "República Dominicana",
    "distance": "0.75",
    "hotel": "Wyndham Garden Quito",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Plaza Argentina",
    "distance": "0.9",
    "hotel": "Wyndham Garden Quito",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantALMUERZOS DE TOMY ROMAN",
    "distance": "0.03",
    "hotel": "Wyndham Garden Quito",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantTHE LOVERS REPUBLIC",
    "distance": "0.1",
    "hotel": "Wyndham Garden Quito",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantColumbus Parrilladas",
    "distance": "0.1",
    "hotel": "Wyndham Garden Quito",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Rumipamba Archaeological Park",
    "distance": "1.7",
    "hotel": "Wyndham Garden Quito",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Foch Square",
    "distance": "1.9",
    "hotel": "Wyndham Garden Quito",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Guayasamin Museum",
    "distance": "2.2",
    "hotel": "Wyndham Garden Quito",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Capilla del Hombre Museum",
    "distance": "2.2",
    "hotel": "Wyndham Garden Quito",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Theatre Square",
    "distance": "4.3",
    "hotel": "Wyndham Garden Quito",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Colonial Art Museum",
    "distance": "4.5",
    "hotel": "Wyndham Garden Quito",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "San Agustin Square",
    "distance": "4.5",
    "hotel": "Wyndham Garden Quito",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Independence Square",
    "distance": "4.6",
    "hotel": "Wyndham Garden Quito",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Casa del Alabado Museum",
    "distance": "5",
    "hotel": "Wyndham Garden Quito",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Templo de la Patria Museum",
    "distance": "6",
    "hotel": "Wyndham Garden Quito",
    "score": "9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque Julio Andrade Marín",
    "distance": "0.3",
    "hotel": "Posada Tambuca",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque de Santa Clara de San Millán",
    "distance": "0.35",
    "hotel": "Posada Tambuca",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Foch Square",
    "distance": "0.5",
    "hotel": "Posada Tambuca",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque Gabriela Mistral",
    "distance": "0.7",
    "hotel": "Posada Tambuca",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Santa Fe",
    "distance": "0.9",
    "hotel": "Posada Tambuca",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "El Ejido Park",
    "distance": "0.95",
    "hotel": "Posada Tambuca",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque El Ejido",
    "distance": "1.2",
    "hotel": "Posada Tambuca",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque EPMAPS",
    "distance": "1.3",
    "hotel": "Posada Tambuca",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Polipasto",
    "distance": "1.3",
    "hotel": "Posada Tambuca",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantQuinua",
    "distance": "0.02",
    "hotel": "Posada Tambuca",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Cafe/barMogens Cafe",
    "distance": "0.04",
    "hotel": "Posada Tambuca",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantLa Casa del Cangrejo y el Pargo",
    "distance": "0.04",
    "hotel": "Posada Tambuca",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Ecuador Natural Science Museum",
    "distance": "1.9",
    "hotel": "Posada Tambuca",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Quito's Vivarium",
    "distance": "1.9",
    "hotel": "Posada Tambuca",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Rumipamba Archaeological Park",
    "distance": "2.5",
    "hotel": "Posada Tambuca",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Theatre Square",
    "distance": "2.7",
    "hotel": "Posada Tambuca",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Colonial Art Museum",
    "distance": "2.9",
    "hotel": "Posada Tambuca",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "San Agustin Square",
    "distance": "2.9",
    "hotel": "Posada Tambuca",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Capilla del Hombre Museum",
    "distance": "3",
    "hotel": "Posada Tambuca",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Guayasamin Museum",
    "distance": "3",
    "hotel": "Posada Tambuca",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Casa del Alabado Museum",
    "distance": "3.4",
    "hotel": "Posada Tambuca",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Templo de la Patria Museum",
    "distance": "4.3",
    "hotel": "Posada Tambuca",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "TrainChimbacalle",
    "distance": "4.9",
    "hotel": "Posada Tambuca",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Quito Mariscal Sucre International Airport",
    "distance": "18",
    "hotel": "Posada Tambuca",
    "score": "9.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Santo Domingo Square",
    "distance": "0.15",
    "hotel": "Hostal Yumbo Imperial",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "San Francisco Square",
    "distance": "0.35",
    "hotel": "Hostal Yumbo Imperial",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "San Agustin Square",
    "distance": "0.4",
    "hotel": "Hostal Yumbo Imperial",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Casa del Alabado Museum",
    "distance": "0.45",
    "hotel": "Hostal Yumbo Imperial",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque Iglesia Inmaculada",
    "distance": "0.45",
    "hotel": "Hostal Yumbo Imperial",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque",
    "distance": "0.95",
    "hotel": "Hostal Yumbo Imperial",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantSheriff colonial",
    "distance": "0.05",
    "hotel": "Hostal Yumbo Imperial",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantCafé Quiteño Libre",
    "distance": "0.05",
    "hotel": "Hostal Yumbo Imperial",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Cafe/barCafe Niza",
    "distance": "0.1",
    "hotel": "Hostal Yumbo Imperial",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "La Alameda Park",
    "distance": "1.5",
    "hotel": "Hostal Yumbo Imperial",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Templo de la Patria Museum",
    "distance": "1.7",
    "hotel": "Hostal Yumbo Imperial",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Foch Square",
    "distance": "3.3",
    "hotel": "Hostal Yumbo Imperial",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "TrainChimbacalle",
    "distance": "1.8",
    "hotel": "Hostal Yumbo Imperial",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Quito Mariscal Sucre International Airport",
    "distance": "21",
    "hotel": "Hostal Yumbo Imperial",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Del Arbolito Park",
    "distance": "0.25",
    "hotel": "Hostal L'Auberge Inn",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque El Ejido",
    "distance": "0.45",
    "hotel": "Hostal L'Auberge Inn",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "El Ejido Park",
    "distance": "0.6",
    "hotel": "Hostal L'Auberge Inn",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "La Alameda Park",
    "distance": "0.65",
    "hotel": "Hostal L'Auberge Inn",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Plaza de la Republica",
    "distance": "0.7",
    "hotel": "Hostal L'Auberge Inn",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque Latinoamerica",
    "distance": "0.95",
    "hotel": "Hostal L'Auberge Inn",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Redondel del Coliseo Rumiñahui",
    "distance": "0.95",
    "hotel": "Hostal L'Auberge Inn",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "La Tolita",
    "distance": "0.95",
    "hotel": "Hostal L'Auberge Inn",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Polibosque",
    "distance": "1.1",
    "hotel": "Hostal L'Auberge Inn",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantRestaurante Nicolas",
    "distance": "0.03",
    "hotel": "Hostal L'Auberge Inn",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantRestaurante Ximenita",
    "distance": "0.04",
    "hotel": "Hostal L'Auberge Inn",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Cafe/barCentro Cafe",
    "distance": "0.1",
    "hotel": "Hostal L'Auberge Inn",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Itchimbia Park",
    "distance": "1.2",
    "hotel": "Hostal L'Auberge Inn",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Foch Square",
    "distance": "1.4",
    "hotel": "Hostal L'Auberge Inn",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Colonial Art Museum",
    "distance": "1.9",
    "hotel": "Hostal L'Auberge Inn",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Casa del Alabado Museum",
    "distance": "2.3",
    "hotel": "Hostal L'Auberge Inn",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Ecuador Natural Science Museum",
    "distance": "3.4",
    "hotel": "Hostal L'Auberge Inn",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Quito's Vivarium",
    "distance": "3.5",
    "hotel": "Hostal L'Auberge Inn",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Templo de la Patria Museum",
    "distance": "3.5",
    "hotel": "Hostal L'Auberge Inn",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Rumipamba Archaeological Park",
    "distance": "3.9",
    "hotel": "Hostal L'Auberge Inn",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Capilla del Hombre Museum",
    "distance": "4",
    "hotel": "Hostal L'Auberge Inn",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Guayasamin Museum",
    "distance": "4.1",
    "hotel": "Hostal L'Auberge Inn",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "TrainTerminal de Ferrocarriles",
    "distance": "3.4",
    "hotel": "Hostal L'Auberge Inn",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "TrainChimbacalle",
    "distance": "3.5",
    "hotel": "Hostal L'Auberge Inn",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Foch Square",
    "distance": "0.3",
    "hotel": "Hotel Reina Isabel",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque de Santa Clara de San Millán",
    "distance": "0.55",
    "hotel": "Hotel Reina Isabel",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Santa Fe",
    "distance": "0.6",
    "hotel": "Hotel Reina Isabel",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "El Ejido Park",
    "distance": "0.7",
    "hotel": "Hotel Reina Isabel",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Polipasto",
    "distance": "0.95",
    "hotel": "Hotel Reina Isabel",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Del Arbolito Park",
    "distance": "1.1",
    "hotel": "Hotel Reina Isabel",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Cafe/barPomaire",
    "distance": "0.04",
    "hotel": "Hotel Reina Isabel",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantRestaurante Comida China",
    "distance": "0.05",
    "hotel": "Hotel Reina Isabel",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantPato Horneado",
    "distance": "0.05",
    "hotel": "Hotel Reina Isabel",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Ecuador Natural Science Museum",
    "distance": "2.1",
    "hotel": "Hotel Reina Isabel",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Quito's Vivarium",
    "distance": "2.2",
    "hotel": "Hotel Reina Isabel",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Theatre Square",
    "distance": "2.5",
    "hotel": "Hotel Reina Isabel",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "San Agustin Square",
    "distance": "2.8",
    "hotel": "Hotel Reina Isabel",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Colonial Art Museum",
    "distance": "2.8",
    "hotel": "Hotel Reina Isabel",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Guayasamin Museum",
    "distance": "3.1",
    "hotel": "Hotel Reina Isabel",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Casa del Alabado Museum",
    "distance": "3.3",
    "hotel": "Hotel Reina Isabel",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Templo de la Patria Museum",
    "distance": "4.2",
    "hotel": "Hotel Reina Isabel",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "TrainTerminal de Ferrocarriles",
    "distance": "4.7",
    "hotel": "Hotel Reina Isabel",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "TrainChimbacalle",
    "distance": "4.7",
    "hotel": "Hotel Reina Isabel",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parterre Av. Naciones Unidas",
    "distance": "0.35",
    "hotel": "Hotel Finlandia",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Tribuna de los Shyris",
    "distance": "0.5",
    "hotel": "Hotel Finlandia",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Costa Rica",
    "distance": "0.75",
    "hotel": "Hotel Finlandia",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque México",
    "distance": "0.75",
    "hotel": "Hotel Finlandia",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque El Heraldo",
    "distance": "0.85",
    "hotel": "Hotel Finlandia",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Jardín de los Niños",
    "distance": "0.9",
    "hotel": "Hotel Finlandia",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Ecuador Natural Science Museum",
    "distance": "0.9",
    "hotel": "Hotel Finlandia",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Quito's Vivarium",
    "distance": "0.9",
    "hotel": "Hotel Finlandia",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantPassion #2",
    "distance": "0.02",
    "hotel": "Hotel Finlandia",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Cafe/barMonoBolón",
    "distance": "0.02",
    "hotel": "Hotel Finlandia",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantCinco Sentidos",
    "distance": "0.04",
    "hotel": "Hotel Finlandia",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Guayasamin Museum",
    "distance": "1.8",
    "hotel": "Hotel Finlandia",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Capilla del Hombre Museum",
    "distance": "1.8",
    "hotel": "Hotel Finlandia",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Rumipamba Archaeological Park",
    "distance": "2.4",
    "hotel": "Hotel Finlandia",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Foch Square",
    "distance": "2.9",
    "hotel": "Hotel Finlandia",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Colonial Art Museum",
    "distance": "6",
    "hotel": "Hotel Finlandia",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "San Agustin Square",
    "distance": "6",
    "hotel": "Hotel Finlandia",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Half of the World",
    "distance": "20",
    "hotel": "Hotel Finlandia",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "TrainTerminal de Ferrocarriles",
    "distance": "8",
    "hotel": "Hotel Finlandia",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "TrainChimbacalle",
    "distance": "8",
    "hotel": "Hotel Finlandia",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "La Tolita",
    "distance": "0.2",
    "hotel": "Hotel Casona 1914",
    "score": "9.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "La Alameda Park",
    "distance": "0.25",
    "hotel": "Hotel Casona 1914",
    "score": "9.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque García Moreno",
    "distance": "0.3",
    "hotel": "Hotel Casona 1914",
    "score": "9.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque Julio Matovelle",
    "distance": "0.55",
    "hotel": "Hotel Casona 1914",
    "score": "9.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Theatre Square",
    "distance": "0.55",
    "hotel": "Hotel Casona 1914",
    "score": "9.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "San Agustin Square",
    "distance": "0.75",
    "hotel": "Hotel Casona 1914",
    "score": "9.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque Iglesia Inmaculada",
    "distance": "0.85",
    "hotel": "Hotel Casona 1914",
    "score": "9.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Itchimbia Park",
    "distance": "0.95",
    "hotel": "Hotel Casona 1914",
    "score": "9.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Independence Square",
    "distance": "0.95",
    "hotel": "Hotel Casona 1914",
    "score": "9.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantRestaurant Gran Colombia",
    "distance": "0.05",
    "hotel": "Hotel Casona 1914",
    "score": "9.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantRestaurante Cuidad de China",
    "distance": "0.15",
    "hotel": "Hotel Casona 1914",
    "score": "9.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Colonial Art Museum",
    "distance": "0.95",
    "hotel": "Hotel Casona 1914",
    "score": "9.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque El Ejido",
    "distance": "1.1",
    "hotel": "Hotel Casona 1914",
    "score": "9.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Casa del Alabado Museum",
    "distance": "1.5",
    "hotel": "Hotel Casona 1914",
    "score": "9.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Templo de la Patria Museum",
    "distance": "2.6",
    "hotel": "Hotel Casona 1914",
    "score": "9.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Ecuador Natural Science Museum",
    "distance": "4.1",
    "hotel": "Hotel Casona 1914",
    "score": "9.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Capilla del Hombre Museum",
    "distance": "4.9",
    "hotel": "Hotel Casona 1914",
    "score": "9.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Guayasamin Museum",
    "distance": "4.9",
    "hotel": "Hotel Casona 1914",
    "score": "9.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "TrainTerminal de Ferrocarriles",
    "distance": "2.7",
    "hotel": "Hotel Casona 1914",
    "score": "9.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "TrainChimbacalle",
    "distance": "2.7",
    "hotel": "Hotel Casona 1914",
    "score": "9.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Santo Domingo Square",
    "distance": "0.1",
    "hotel": "Hostal Juana de Arco",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Independence Square",
    "distance": "0.5",
    "hotel": "Hostal Juana de Arco",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque Cumandá",
    "distance": "0.5",
    "hotel": "Hostal Juana de Arco",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Casa del Alabado Museum",
    "distance": "0.5",
    "hotel": "Hostal Juana de Arco",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "San Agustin Square",
    "distance": "0.55",
    "hotel": "Hostal Juana de Arco",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque Iglesia Inmaculada",
    "distance": "0.65",
    "hotel": "Hostal Juana de Arco",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Colonial Art Museum",
    "distance": "0.75",
    "hotel": "Hostal Juana de Arco",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque",
    "distance": "0.9",
    "hotel": "Hostal Juana de Arco",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Cafe/barCafeteria Virgen del Cisne",
    "distance": "0.01",
    "hotel": "Hostal Juana de Arco",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantRestaurante La Unión",
    "distance": "0.05",
    "hotel": "Hostal Juana de Arco",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Cafe/barLa Beata Café Taller",
    "distance": "0.1",
    "hotel": "Hostal Juana de Arco",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Itchimbia Park",
    "distance": "1.6",
    "hotel": "Hostal Juana de Arco",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Foch Square",
    "distance": "3.5",
    "hotel": "Hostal Juana de Arco",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "TrainTerminal de Ferrocarriles",
    "distance": "1.6",
    "hotel": "Hostal Juana de Arco",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "TrainChimbacalle",
    "distance": "1.6",
    "hotel": "Hostal Juana de Arco",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "República Dominicana",
    "distance": "0.5",
    "hotel": "ibis Quito",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Plaza Argentina",
    "distance": "0.75",
    "hotel": "ibis Quito",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque Gabriela Mistral",
    "distance": "0.75",
    "hotel": "ibis Quito",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Foch Square",
    "distance": "0.95",
    "hotel": "ibis Quito",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque EPMAPS",
    "distance": "0.001",
    "hotel": "ibis Quito",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "PROINSA",
    "distance": "1.1",
    "hotel": "ibis Quito",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Jardín de los Niños",
    "distance": "1.2",
    "hotel": "ibis Quito",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Santa Fe",
    "distance": "1.2",
    "hotel": "ibis Quito",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Cafe/barMal Santig",
    "distance": "0.04",
    "hotel": "ibis Quito",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantLa Ronda",
    "distance": "0.05",
    "hotel": "ibis Quito",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantPenny Royal",
    "distance": "0.1",
    "hotel": "ibis Quito",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Guapulo Park",
    "distance": "1.3",
    "hotel": "ibis Quito",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "La Carolina Park",
    "distance": "1.5",
    "hotel": "ibis Quito",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Capilla del Hombre Museum",
    "distance": "1.9",
    "hotel": "ibis Quito",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Guayasamin Museum",
    "distance": "1.9",
    "hotel": "ibis Quito",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Theatre Square",
    "distance": "3.7",
    "hotel": "ibis Quito",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Colonial Art Museum",
    "distance": "4",
    "hotel": "ibis Quito",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Casa del Alabado Museum",
    "distance": "4.5",
    "hotel": "ibis Quito",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque Julio Andrade Marín",
    "distance": "0.2",
    "hotel": "ArtPlaza",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque de Santa Clara de San Millán",
    "distance": "0.45",
    "hotel": "ArtPlaza",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "El Ejido Park",
    "distance": "0.55",
    "hotel": "ArtPlaza",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Foch Square",
    "distance": "0.55",
    "hotel": "ArtPlaza",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Santa Fe",
    "distance": "0.75",
    "hotel": "ArtPlaza",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque El Ejido",
    "distance": "0.75",
    "hotel": "ArtPlaza",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque Gabriela Mistral",
    "distance": "0.8",
    "hotel": "ArtPlaza",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Del Arbolito Park",
    "distance": "0.85",
    "hotel": "ArtPlaza",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Polipasto",
    "distance": "0.001",
    "hotel": "ArtPlaza",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Polibosque",
    "distance": "1.2",
    "hotel": "ArtPlaza",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantMi playita",
    "distance": "0.02",
    "hotel": "ArtPlaza",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Cafe/barTerraza Andina",
    "distance": "0.04",
    "hotel": "ArtPlaza",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantRestaurante Vegetariano",
    "distance": "0.05",
    "hotel": "ArtPlaza",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "La Alameda Park",
    "distance": "1.6",
    "hotel": "ArtPlaza",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Theatre Square",
    "distance": "2.3",
    "hotel": "ArtPlaza",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Ecuador Natural Science Museum",
    "distance": "2.3",
    "hotel": "ArtPlaza",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Quito's Vivarium",
    "distance": "2.4",
    "hotel": "ArtPlaza",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Colonial Art Museum",
    "distance": "2.5",
    "hotel": "ArtPlaza",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Casa del Alabado Museum",
    "distance": "3.1",
    "hotel": "ArtPlaza",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Capilla del Hombre Museum",
    "distance": "3.3",
    "hotel": "ArtPlaza",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Guayasamin Museum",
    "distance": "3.3",
    "hotel": "ArtPlaza",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Templo de la Patria Museum",
    "distance": "4",
    "hotel": "ArtPlaza",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "TrainTerminal de Ferrocarriles",
    "distance": "4.5",
    "hotel": "ArtPlaza",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Santa Fe",
    "distance": "0.3",
    "hotel": "ITSAHOME Apartments Torre Seis",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Foch Square",
    "distance": "0.4",
    "hotel": "ITSAHOME Apartments Torre Seis",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Polipasto",
    "distance": "0.5",
    "hotel": "ITSAHOME Apartments Torre Seis",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque Gabriela Mistral",
    "distance": "0.6",
    "hotel": "ITSAHOME Apartments Torre Seis",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Polibosque",
    "distance": "0.65",
    "hotel": "ITSAHOME Apartments Torre Seis",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque Julio Andrade Marín",
    "distance": "0.7",
    "hotel": "ITSAHOME Apartments Torre Seis",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Del Arbolito Park",
    "distance": "0.7",
    "hotel": "ITSAHOME Apartments Torre Seis",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque Latinoamerica",
    "distance": "0.85",
    "hotel": "ITSAHOME Apartments Torre Seis",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantAzuca",
    "distance": "0.04",
    "hotel": "ITSAHOME Apartments Torre Seis",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantLos Arrieros",
    "distance": "0.1",
    "hotel": "ITSAHOME Apartments Torre Seis",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantGuang Zhou",
    "distance": "0.1",
    "hotel": "ITSAHOME Apartments Torre Seis",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Ecuador Natural Science Museum",
    "distance": "2.4",
    "hotel": "ITSAHOME Apartments Torre Seis",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Quito's Vivarium",
    "distance": "2.5",
    "hotel": "ITSAHOME Apartments Torre Seis",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "San Agustin Square",
    "distance": "2.6",
    "hotel": "ITSAHOME Apartments Torre Seis",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Colonial Art Museum",
    "distance": "2.7",
    "hotel": "ITSAHOME Apartments Torre Seis",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Capilla del Hombre Museum",
    "distance": "3.1",
    "hotel": "ITSAHOME Apartments Torre Seis",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Guayasamin Museum",
    "distance": "3.2",
    "hotel": "ITSAHOME Apartments Torre Seis",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Casa del Alabado Museum",
    "distance": "3.2",
    "hotel": "ITSAHOME Apartments Torre Seis",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Rumipamba Archaeological Park",
    "distance": "3.2",
    "hotel": "ITSAHOME Apartments Torre Seis",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "TrainTerminal de Ferrocarriles",
    "distance": "4.4",
    "hotel": "ITSAHOME Apartments Torre Seis",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "TrainChimbacalle",
    "distance": "4.4",
    "hotel": "ITSAHOME Apartments Torre Seis",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Colonial Art Museum",
    "distance": "0.3",
    "hotel": "Vista del Angel Hotel Boutique",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque Julio Matovelle",
    "distance": "0.5",
    "hotel": "Vista del Angel Hotel Boutique",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Independence Square",
    "distance": "0.55",
    "hotel": "Vista del Angel Hotel Boutique",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parque García Moreno",
    "distance": "0.55",
    "hotel": "Vista del Angel Hotel Boutique",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "San Agustin Square",
    "distance": "0.6",
    "hotel": "Vista del Angel Hotel Boutique",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "San Francisco Square",
    "distance": "0.7",
    "hotel": "Vista del Angel Hotel Boutique",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Cancha",
    "distance": "0.8",
    "hotel": "Vista del Angel Hotel Boutique",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantMote Colonial",
    "distance": "0.15",
    "hotel": "Vista del Angel Hotel Boutique",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantSabor y Sazón",
    "distance": "0.2",
    "hotel": "Vista del Angel Hotel Boutique",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantCafetería Cachito II",
    "distance": "0.2",
    "hotel": "Vista del Angel Hotel Boutique",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Casa del Alabado Museum",
    "distance": "0.8",
    "hotel": "Vista del Angel Hotel Boutique",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Santo Domingo Square",
    "distance": "0.95",
    "hotel": "Vista del Angel Hotel Boutique",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Foch Square",
    "distance": "2.7",
    "hotel": "Vista del Angel Hotel Boutique",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Ecuador Natural Science Museum",
    "distance": "4.5",
    "hotel": "Vista del Angel Hotel Boutique",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Quito's Vivarium",
    "distance": "4.5",
    "hotel": "Vista del Angel Hotel Boutique",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "TrainTerminal de Ferrocarriles",
    "distance": "2.6",
    "hotel": "Vista del Angel Hotel Boutique",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "TrainChimbacalle",
    "distance": "2.6",
    "hotel": "Vista del Angel Hotel Boutique",
    "score": "9.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "San Agustin Square",
    "distance": "0.3",
    "hotel": "Hotel Huasi Continental",
    "score": "8.2"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Cafe/barCafe Dios No Muere",
    "distance": "0.1",
    "hotel": "Hotel Huasi Continental",
    "score": "8.2"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantLas Fritadas Restaurante & Café",
    "distance": "0.1",
    "hotel": "Hotel Huasi Continental",
    "score": "8.2"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "La Alameda Park",
    "distance": "1.4",
    "hotel": "Hotel Huasi Continental",
    "score": "8.2"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Tribuna de los Shyris",
    "distance": "0.2",
    "hotel": "Dann Carlton Quito",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "La Carolina Park",
    "distance": "0.35",
    "hotel": "Dann Carlton Quito",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Jardín de los Niños",
    "distance": "0.5",
    "hotel": "Dann Carlton Quito",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Ecuador Natural Science Museum",
    "distance": "0.55",
    "hotel": "Dann Carlton Quito",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "PROINSA",
    "distance": "0.6",
    "hotel": "Dann Carlton Quito",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Quito's Vivarium",
    "distance": "0.7",
    "hotel": "Dann Carlton Quito",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Parterre Av. Naciones Unidas",
    "distance": "0.8",
    "hotel": "Dann Carlton Quito",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Plaza Argentina",
    "distance": "0.8",
    "hotel": "Dann Carlton Quito",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantRomolo E Remo",
    "distance": "0.02",
    "hotel": "Dann Carlton Quito",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "RestaurantBela",
    "distance": "0.05",
    "hotel": "Dann Carlton Quito",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Cafe/barBoncaffe",
    "distance": "0.05",
    "hotel": "Dann Carlton Quito",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Guayasamin Museum",
    "distance": "1.5",
    "hotel": "Dann Carlton Quito",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Capilla del Hombre Museum",
    "distance": "1.5",
    "hotel": "Dann Carlton Quito",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Quito",
    "places": "Foch Square",
    "distance": "2.5",
    "hotel": "Dann Carlton Quito",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Plaza Jerusalén",
    "distance": "0.55",
    "hotel": "Hotel Air Suites",
    "score": "7.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Escuela de Futbol",
    "distance": "0.8",
    "hotel": "Hotel Air Suites",
    "score": "7.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Pista de Bicicross",
    "distance": "1.1",
    "hotel": "Hotel Air Suites",
    "score": "7.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque Alegria Guayaquil",
    "distance": "1.2",
    "hotel": "Hotel Air Suites",
    "score": "7.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Antonio Neumane Park",
    "distance": "1.2",
    "hotel": "Hotel Air Suites",
    "score": "7.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque de juegos",
    "distance": "1.4",
    "hotel": "Hotel Air Suites",
    "score": "7.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque De La 1ra",
    "distance": "1.5",
    "hotel": "Hotel Air Suites",
    "score": "7.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque Japones",
    "distance": "1.5",
    "hotel": "Hotel Air Suites",
    "score": "7.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque de juegos Sauces 2",
    "distance": "1.5",
    "hotel": "Hotel Air Suites",
    "score": "7.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque de la 4ta",
    "distance": "1.7",
    "hotel": "Hotel Air Suites",
    "score": "7.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantCharlot",
    "distance": "0.05",
    "hotel": "Hotel Air Suites",
    "score": "7.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantLa Isla Del Marisco",
    "distance": "0.05",
    "hotel": "Hotel Air Suites",
    "score": "7.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantComidas Típicas Colombianas",
    "distance": "0.1",
    "hotel": "Hotel Air Suites",
    "score": "7.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santa Ana Hill Lighthouse",
    "distance": "3.6",
    "hotel": "Hotel Air Suites",
    "score": "7.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santa Ana Hill",
    "distance": "3.8",
    "hotel": "Hotel Air Suites",
    "score": "7.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Seafront",
    "distance": "4.7",
    "hotel": "Hotel Air Suites",
    "score": "7.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Malecon 2000",
    "distance": "4.8",
    "hotel": "Hotel Air Suites",
    "score": "7.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Nahin Isaias Museum",
    "distance": "4.9",
    "hotel": "Hotel Air Suites",
    "score": "7.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Municipal Museum",
    "distance": "5",
    "hotel": "Hotel Air Suites",
    "score": "7.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Botanical Garden",
    "distance": "8",
    "hotel": "Hotel Air Suites",
    "score": "7.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "TrainDurán",
    "distance": "4.9",
    "hotel": "Hotel Air Suites",
    "score": "7.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "TrainEstación de Ferrocarriles Durán",
    "distance": "4.9",
    "hotel": "Hotel Air Suites",
    "score": "7.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "José Joaquín de Olmedo International Airport",
    "distance": "0.7",
    "hotel": "Hotel Air Suites",
    "score": "7.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Jardines del Malecon",
    "distance": "0.15",
    "hotel": "Hotel Perla Central",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Plaza de la Concepcion",
    "distance": "0.35",
    "hotel": "Hotel Perla Central",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Plaza Colón",
    "distance": "0.35",
    "hotel": "Hotel Perla Central",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santo Domingo",
    "distance": "0.4",
    "hotel": "Hotel Perla Central",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Cornelio Vernaza",
    "distance": "0.45",
    "hotel": "Hotel Perla Central",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santa Ana Hill",
    "distance": "0.45",
    "hotel": "Hotel Perla Central",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Areas verdes Malecon Simon Bolivar",
    "distance": "0.6",
    "hotel": "Hotel Perla Central",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santa Ana Hill Lighthouse",
    "distance": "0.6",
    "hotel": "Hotel Perla Central",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Plaza Pedro Carbo Noboa",
    "distance": "0.65",
    "hotel": "Hotel Perla Central",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Jacinto Moran de Buitron",
    "distance": "0.65",
    "hotel": "Hotel Perla Central",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantEl Poly",
    "distance": "0.04",
    "hotel": "Hotel Perla Central",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantKFC",
    "distance": "0.05",
    "hotel": "Hotel Perla Central",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Cafe/barAzúcar de Cuba",
    "distance": "0.05",
    "hotel": "Hotel Perla Central",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Seafront",
    "distance": "0.7",
    "hotel": "Hotel Perla Central",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santa Ana Park",
    "distance": "0.7",
    "hotel": "Hotel Perla Central",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Malecon 2000",
    "distance": "0.75",
    "hotel": "Hotel Perla Central",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Nahin Isaias Museum",
    "distance": "1.1",
    "hotel": "Hotel Perla Central",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Municipal Museum",
    "distance": "1.3",
    "hotel": "Hotel Perla Central",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Botanical Garden",
    "distance": "12",
    "hotel": "Hotel Perla Central",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "TrainDurán",
    "distance": "4.1",
    "hotel": "Hotel Perla Central",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "TrainEstación de Ferrocarriles Durán",
    "distance": "4.1",
    "hotel": "Hotel Perla Central",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "José Joaquín de Olmedo International Airport",
    "distance": "3.4",
    "hotel": "Hotel Perla Central",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque Jerusalén",
    "distance": "0.3",
    "hotel": "Luxva Hotel Boutique",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque Uruguay",
    "distance": "0.4",
    "hotel": "Luxva Hotel Boutique",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "cancha",
    "distance": "0.85",
    "hotel": "Luxva Hotel Boutique",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque Mirtos",
    "distance": "0.9",
    "hotel": "Luxva Hotel Boutique",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque Lineal Del Salado",
    "distance": "0.95",
    "hotel": "Luxva Hotel Boutique",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque Keneddy",
    "distance": "0.001",
    "hotel": "Luxva Hotel Boutique",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Recorrido del Periodista",
    "distance": "1.1",
    "hotel": "Luxva Hotel Boutique",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Las Lomas",
    "distance": "1.3",
    "hotel": "Luxva Hotel Boutique",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque Deportivo Ferroviaria",
    "distance": "1.3",
    "hotel": "Luxva Hotel Boutique",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque Infantil Ferroviaria",
    "distance": "1.5",
    "hotel": "Luxva Hotel Boutique",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantSyouki Sushi",
    "distance": "0.15",
    "hotel": "Luxva Hotel Boutique",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantRoling's Sport-Rock & Beer",
    "distance": "0.25",
    "hotel": "Luxva Hotel Boutique",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantLa Proli de ...",
    "distance": "0.25",
    "hotel": "Luxva Hotel Boutique",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Municipal Museum",
    "distance": "3.6",
    "hotel": "Luxva Hotel Boutique",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Nahin Isaias Museum",
    "distance": "3.6",
    "hotel": "Luxva Hotel Boutique",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Seafront",
    "distance": "3.6",
    "hotel": "Luxva Hotel Boutique",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Malecon 2000",
    "distance": "3.7",
    "hotel": "Luxva Hotel Boutique",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santa Ana Hill",
    "distance": "3.7",
    "hotel": "Luxva Hotel Boutique",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Botanical Garden",
    "distance": "11",
    "hotel": "Luxva Hotel Boutique",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "TrainDurán",
    "distance": "7",
    "hotel": "Luxva Hotel Boutique",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "TrainEstación de Ferrocarriles Durán",
    "distance": "7",
    "hotel": "Luxva Hotel Boutique",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Plaza Presidente Vicente Rocafuerte",
    "distance": "0.1",
    "hotel": "Hotel Palace Guayaquil",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Plaza Garibaldi",
    "distance": "0.25",
    "hotel": "Hotel Palace Guayaquil",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Nahin Isaias Museum",
    "distance": "0.25",
    "hotel": "Hotel Palace Guayaquil",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Las Iguanas Park",
    "distance": "0.25",
    "hotel": "Hotel Palace Guayaquil",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Plaza de la Administracion",
    "distance": "0.25",
    "hotel": "Hotel Palace Guayaquil",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Seminario Park",
    "distance": "0.25",
    "hotel": "Hotel Palace Guayaquil",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Plaza Pedro Carbo Noboa",
    "distance": "0.3",
    "hotel": "Hotel Palace Guayaquil",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Seafront",
    "distance": "0.35",
    "hotel": "Hotel Palace Guayaquil",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Malecon 2000",
    "distance": "0.35",
    "hotel": "Hotel Palace Guayaquil",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Municipal Museum",
    "distance": "0.35",
    "hotel": "Hotel Palace Guayaquil",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantPalace Restaurante",
    "distance": "0.01",
    "hotel": "Hotel Palace Guayaquil",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Cafe/barPasteles & Compañía",
    "distance": "0.02",
    "hotel": "Hotel Palace Guayaquil",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Cafe/barLa Pausa",
    "distance": "0.02",
    "hotel": "Hotel Palace Guayaquil",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santa Ana Hill",
    "distance": "1.4",
    "hotel": "Hotel Palace Guayaquil",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santa Ana Hill Lighthouse",
    "distance": "1.6",
    "hotel": "Hotel Palace Guayaquil",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Botanical Garden",
    "distance": "13",
    "hotel": "Hotel Palace Guayaquil",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "TrainDurán",
    "distance": "5",
    "hotel": "Hotel Palace Guayaquil",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "TrainEstación de Ferrocarriles Durán",
    "distance": "5",
    "hotel": "Hotel Palace Guayaquil",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "José Joaquín de Olmedo International Airport",
    "distance": "4.1",
    "hotel": "Hotel Palace Guayaquil",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Areas verdes Malecon Simon Bolivar",
    "distance": "0.35",
    "hotel": "River Garden Hotel + Suites",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Plaza Pedro Carbo Noboa",
    "distance": "0.4",
    "hotel": "River Garden Hotel + Suites",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Plaza Garibaldi",
    "distance": "0.45",
    "hotel": "River Garden Hotel + Suites",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Seafront",
    "distance": "0.45",
    "hotel": "River Garden Hotel + Suites",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Malecon 2000",
    "distance": "0.5",
    "hotel": "River Garden Hotel + Suites",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Plaza Presidente Vicente Rocafuerte",
    "distance": "0.55",
    "hotel": "River Garden Hotel + Suites",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Plaza de la Concepcion",
    "distance": "0.55",
    "hotel": "River Garden Hotel + Suites",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Plaza Colón",
    "distance": "0.6",
    "hotel": "River Garden Hotel + Suites",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santo Domingo",
    "distance": "0.65",
    "hotel": "River Garden Hotel + Suites",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantEl Malecon Restaurante",
    "distance": "0.05",
    "hotel": "River Garden Hotel + Suites",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Cafe/barEl Mono Golosso",
    "distance": "0.1",
    "hotel": "River Garden Hotel + Suites",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantChop Chop",
    "distance": "0.1",
    "hotel": "River Garden Hotel + Suites",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santa Ana Hill",
    "distance": "0.7",
    "hotel": "River Garden Hotel + Suites",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Nahin Isaias Museum",
    "distance": "0.75",
    "hotel": "River Garden Hotel + Suites",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santa Ana Hill Lighthouse",
    "distance": "0.85",
    "hotel": "River Garden Hotel + Suites",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Municipal Museum",
    "distance": "0.001",
    "hotel": "River Garden Hotel + Suites",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "TrainDurán",
    "distance": "4.3",
    "hotel": "River Garden Hotel + Suites",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "TrainEstación de Ferrocarriles Durán",
    "distance": "4.3",
    "hotel": "River Garden Hotel + Suites",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "José Joaquín de Olmedo International Airport",
    "distance": "3.6",
    "hotel": "River Garden Hotel + Suites",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Plaza Jerusalén",
    "distance": "0.3",
    "hotel": "TRYP by Wyndham Guayaquil",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Antonio Neumane Park",
    "distance": "0.55",
    "hotel": "TRYP by Wyndham Guayaquil",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Pista de Bicicross",
    "distance": "0.65",
    "hotel": "TRYP by Wyndham Guayaquil",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque Japones",
    "distance": "0.85",
    "hotel": "TRYP by Wyndham Guayaquil",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Escuela de Futbol",
    "distance": "1.4",
    "hotel": "TRYP by Wyndham Guayaquil",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque Alegria Guayaquil",
    "distance": "1.5",
    "hotel": "TRYP by Wyndham Guayaquil",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque Lineal",
    "distance": "1.5",
    "hotel": "TRYP by Wyndham Guayaquil",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque De La 1ra",
    "distance": "1.6",
    "hotel": "TRYP by Wyndham Guayaquil",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Roca Blanca",
    "distance": "1.7",
    "hotel": "TRYP by Wyndham Guayaquil",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque #5 Cdla FAE",
    "distance": "1.7",
    "hotel": "TRYP by Wyndham Guayaquil",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantWingers",
    "distance": "0.04",
    "hotel": "TRYP by Wyndham Guayaquil",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantLa Tablita del Tártaro",
    "distance": "0.04",
    "hotel": "TRYP by Wyndham Guayaquil",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantPuerto Moro",
    "distance": "0.04",
    "hotel": "TRYP by Wyndham Guayaquil",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santa Ana Hill Lighthouse",
    "distance": "3.3",
    "hotel": "TRYP by Wyndham Guayaquil",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santa Ana Hill",
    "distance": "3.5",
    "hotel": "TRYP by Wyndham Guayaquil",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Seafront",
    "distance": "4.3",
    "hotel": "TRYP by Wyndham Guayaquil",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Malecon 2000",
    "distance": "4.3",
    "hotel": "TRYP by Wyndham Guayaquil",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Nahin Isaias Museum",
    "distance": "4.5",
    "hotel": "TRYP by Wyndham Guayaquil",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Municipal Museum",
    "distance": "4.6",
    "hotel": "TRYP by Wyndham Guayaquil",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Botanical Garden",
    "distance": "9",
    "hotel": "TRYP by Wyndham Guayaquil",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "José Joaquín de Olmedo International Airport",
    "distance": "0.65",
    "hotel": "TRYP by Wyndham Guayaquil",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Antonio Neumane Park",
    "distance": "0.2",
    "hotel": "Wyndham Garden Guayaquil",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Plaza Jerusalén",
    "distance": "0.45",
    "hotel": "Wyndham Garden Guayaquil",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Pista de Bicicross",
    "distance": "0.45",
    "hotel": "Wyndham Garden Guayaquil",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque Japones",
    "distance": "0.55",
    "hotel": "Wyndham Garden Guayaquil",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque Lineal",
    "distance": "1.2",
    "hotel": "Wyndham Garden Guayaquil",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque Union y Progreso",
    "distance": "1.4",
    "hotel": "Wyndham Garden Guayaquil",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque Alegria Guayaquil",
    "distance": "1.6",
    "hotel": "Wyndham Garden Guayaquil",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Roca Blanca",
    "distance": "1.6",
    "hotel": "Wyndham Garden Guayaquil",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Cafe/barPiccadilly",
    "distance": "0.1",
    "hotel": "Wyndham Garden Guayaquil",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantCafetería Cedro del Líbano",
    "distance": "0.15",
    "hotel": "Wyndham Garden Guayaquil",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantLa Casa de Carlo",
    "distance": "0.2",
    "hotel": "Wyndham Garden Guayaquil",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Seafront",
    "distance": "4.2",
    "hotel": "Wyndham Garden Guayaquil",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Malecon 2000",
    "distance": "4.2",
    "hotel": "Wyndham Garden Guayaquil",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Nahin Isaias Museum",
    "distance": "4.3",
    "hotel": "Wyndham Garden Guayaquil",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Municipal Museum",
    "distance": "4.5",
    "hotel": "Wyndham Garden Guayaquil",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "José Joaquín de Olmedo International Airport",
    "distance": "0.9",
    "hotel": "Wyndham Garden Guayaquil",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Las Iguanas Park",
    "distance": "0.05",
    "hotel": "Unipark by Oro Verde Hotels",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Seminario Park",
    "distance": "0.1",
    "hotel": "Unipark by Oro Verde Hotels",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Municipal Museum",
    "distance": "0.2",
    "hotel": "Unipark by Oro Verde Hotels",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Plaza de la Administracion",
    "distance": "0.2",
    "hotel": "Unipark by Oro Verde Hotels",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Nahin Isaias Museum",
    "distance": "0.2",
    "hotel": "Unipark by Oro Verde Hotels",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Plaza Presidente Vicente Rocafuerte",
    "distance": "0.3",
    "hotel": "Unipark by Oro Verde Hotels",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque Juan Montalvo",
    "distance": "0.4",
    "hotel": "Unipark by Oro Verde Hotels",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Plaza Garibaldi",
    "distance": "0.4",
    "hotel": "Unipark by Oro Verde Hotels",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Malecon 2000",
    "distance": "0.45",
    "hotel": "Unipark by Oro Verde Hotels",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Cafe/barUnicafé",
    "distance": "0.03",
    "hotel": "Unipark by Oro Verde Hotels",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantUnDeli",
    "distance": "0.1",
    "hotel": "Unipark by Oro Verde Hotels",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantLa Canoa",
    "distance": "0.1",
    "hotel": "Unipark by Oro Verde Hotels",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santa Ana Hill",
    "distance": "1.6",
    "hotel": "Unipark by Oro Verde Hotels",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santa Ana Hill Lighthouse",
    "distance": "1.7",
    "hotel": "Unipark by Oro Verde Hotels",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "José Joaquín de Olmedo International Airport",
    "distance": "4.2",
    "hotel": "Unipark by Oro Verde Hotels",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Escuela de Futbol",
    "distance": "0.35",
    "hotel": "Holiday Inn Guayaquil Airport an IHG Hotel",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque de juegos",
    "distance": "0.75",
    "hotel": "Holiday Inn Guayaquil Airport an IHG Hotel",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque de juegos Sauces 2",
    "distance": "0.8",
    "hotel": "Holiday Inn Guayaquil Airport an IHG Hotel",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Brisas Del Rio",
    "distance": "1.2",
    "hotel": "Holiday Inn Guayaquil Airport an IHG Hotel",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque Alegria Guayaquil",
    "distance": "1.3",
    "hotel": "Holiday Inn Guayaquil Airport an IHG Hotel",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Plaza Jerusalén",
    "distance": "1.4",
    "hotel": "Holiday Inn Guayaquil Airport an IHG Hotel",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque de la 4ta",
    "distance": "1.5",
    "hotel": "Holiday Inn Guayaquil Airport an IHG Hotel",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Guayaquil Historic Park",
    "distance": "1.6",
    "hotel": "Holiday Inn Guayaquil Airport an IHG Hotel",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque De La 1ra",
    "distance": "1.7",
    "hotel": "Holiday Inn Guayaquil Airport an IHG Hotel",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Pista de Bicicross",
    "distance": "1.9",
    "hotel": "Holiday Inn Guayaquil Airport an IHG Hotel",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Cafe/barAntojitos cafe",
    "distance": "0.1",
    "hotel": "Holiday Inn Guayaquil Airport an IHG Hotel",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantBizcocho",
    "distance": "0.1",
    "hotel": "Holiday Inn Guayaquil Airport an IHG Hotel",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantTropiburger",
    "distance": "0.25",
    "hotel": "Holiday Inn Guayaquil Airport an IHG Hotel",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Antonio Neumane Park",
    "distance": "2",
    "hotel": "Holiday Inn Guayaquil Airport an IHG Hotel",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santa Ana Hill Lighthouse",
    "distance": "4.2",
    "hotel": "Holiday Inn Guayaquil Airport an IHG Hotel",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santa Ana Hill",
    "distance": "4.4",
    "hotel": "Holiday Inn Guayaquil Airport an IHG Hotel",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Seafront",
    "distance": "5",
    "hotel": "Holiday Inn Guayaquil Airport an IHG Hotel",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Malecon 2000",
    "distance": "5",
    "hotel": "Holiday Inn Guayaquil Airport an IHG Hotel",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Nahin Isaias Museum",
    "distance": "6",
    "hotel": "Holiday Inn Guayaquil Airport an IHG Hotel",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Municipal Museum",
    "distance": "6",
    "hotel": "Holiday Inn Guayaquil Airport an IHG Hotel",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "TrainDurán",
    "distance": "4.8",
    "hotel": "Holiday Inn Guayaquil Airport an IHG Hotel",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "TrainEstación de Ferrocarriles Durán",
    "distance": "4.8",
    "hotel": "Holiday Inn Guayaquil Airport an IHG Hotel",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "José Joaquín de Olmedo International Airport",
    "distance": "1.4",
    "hotel": "Holiday Inn Guayaquil Airport an IHG Hotel",
    "score": "8.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Plaza de la Concepcion",
    "distance": "0.2",
    "hotel": "YU! Smarthotels",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Plaza Colón",
    "distance": "0.25",
    "hotel": "YU! Smarthotels",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santo Domingo",
    "distance": "0.25",
    "hotel": "YU! Smarthotels",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Cornelio Vernaza",
    "distance": "0.3",
    "hotel": "YU! Smarthotels",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Jardines del Malecon",
    "distance": "0.4",
    "hotel": "YU! Smarthotels",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santa Ana Hill",
    "distance": "0.4",
    "hotel": "YU! Smarthotels",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Jacinto Moran de Buitron",
    "distance": "0.45",
    "hotel": "YU! Smarthotels",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santa Ana Hill Lighthouse",
    "distance": "0.5",
    "hotel": "YU! Smarthotels",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santa Ana Park",
    "distance": "0.55",
    "hotel": "YU! Smarthotels",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Plaza Pedro Carbo Noboa",
    "distance": "0.75",
    "hotel": "YU! Smarthotels",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantAna M",
    "distance": "0.1",
    "hotel": "YU! Smarthotels",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantAlbacora Dorada",
    "distance": "0.15",
    "hotel": "YU! Smarthotels",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantKFC",
    "distance": "0.2",
    "hotel": "YU! Smarthotels",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Seafront",
    "distance": "0.85",
    "hotel": "YU! Smarthotels",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Malecon 2000",
    "distance": "0.95",
    "hotel": "YU! Smarthotels",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Nahin Isaias Museum",
    "distance": "1.2",
    "hotel": "YU! Smarthotels",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Municipal Museum",
    "distance": "1.4",
    "hotel": "YU! Smarthotels",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "José Joaquín de Olmedo International Airport",
    "distance": "3.2",
    "hotel": "YU! Smarthotels",
    "score": "8.5"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santa Ana Park",
    "distance": "0.1",
    "hotel": "Wyndham Guayaquil Puerto Santa Ana",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santa Ana Hill Lighthouse",
    "distance": "0.2",
    "hotel": "Wyndham Guayaquil Puerto Santa Ana",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Jacinto Moran de Buitron",
    "distance": "0.25",
    "hotel": "Wyndham Guayaquil Puerto Santa Ana",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Cornelio Vernaza",
    "distance": "0.35",
    "hotel": "Wyndham Guayaquil Puerto Santa Ana",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Plaza Colón",
    "distance": "0.45",
    "hotel": "Wyndham Guayaquil Puerto Santa Ana",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Plaza de la Concepcion",
    "distance": "0.45",
    "hotel": "Wyndham Guayaquil Puerto Santa Ana",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Jardines del Malecon",
    "distance": "0.95",
    "hotel": "Wyndham Guayaquil Puerto Santa Ana",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Areas verdes Malecon Simon Bolivar",
    "distance": "1.4",
    "hotel": "Wyndham Guayaquil Puerto Santa Ana",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantMami-t",
    "distance": "0.05",
    "hotel": "Wyndham Guayaquil Puerto Santa Ana",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantLa Porteña",
    "distance": "0.1",
    "hotel": "Wyndham Guayaquil Puerto Santa Ana",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantGanchos Restobar",
    "distance": "0.1",
    "hotel": "Wyndham Guayaquil Puerto Santa Ana",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Seafront",
    "distance": "1.5",
    "hotel": "Wyndham Guayaquil Puerto Santa Ana",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Malecon 2000",
    "distance": "1.6",
    "hotel": "Wyndham Guayaquil Puerto Santa Ana",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Nahin Isaias Museum",
    "distance": "1.8",
    "hotel": "Wyndham Guayaquil Puerto Santa Ana",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Municipal Museum",
    "distance": "2.1",
    "hotel": "Wyndham Guayaquil Puerto Santa Ana",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "TrainDurán",
    "distance": "3.6",
    "hotel": "Wyndham Guayaquil Puerto Santa Ana",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "TrainEstación de Ferrocarriles Durán",
    "distance": "3.6",
    "hotel": "Wyndham Guayaquil Puerto Santa Ana",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "José Joaquín de Olmedo International Airport",
    "distance": "2.7",
    "hotel": "Wyndham Guayaquil Puerto Santa Ana",
    "score": "8.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque de la 4ta",
    "distance": "0.5",
    "hotel": "Hotel de Alborada",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Praque Sauces 9 R49",
    "distance": "0.55",
    "hotel": "Hotel de Alborada",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque mercado sauce s 9",
    "distance": "0.7",
    "hotel": "Hotel de Alborada",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque del niño",
    "distance": "0.85",
    "hotel": "Hotel de Alborada",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "El Parque del 8",
    "distance": "0.9",
    "hotel": "Hotel de Alborada",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque de juegos Sauces 6",
    "distance": "1.1",
    "hotel": "Hotel de Alborada",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque Alegria Guayaquil",
    "distance": "1.1",
    "hotel": "Hotel de Alborada",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque La Amistad",
    "distance": "1.1",
    "hotel": "Hotel de Alborada",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque De La 1ra",
    "distance": "1.1",
    "hotel": "Hotel de Alborada",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Canchas Sintéticas Zona FUTBOL 5",
    "distance": "1.2",
    "hotel": "Hotel de Alborada",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantMi Colombia",
    "distance": "0.2",
    "hotel": "Hotel de Alborada",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantD´Nikkoss",
    "distance": "0.2",
    "hotel": "Hotel de Alborada",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantD' Suly Restaurant",
    "distance": "0.25",
    "hotel": "Hotel de Alborada",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santa Ana Hill Lighthouse",
    "distance": "6",
    "hotel": "Hotel de Alborada",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santa Ana Hill",
    "distance": "6",
    "hotel": "Hotel de Alborada",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Botanical Garden",
    "distance": "6",
    "hotel": "Hotel de Alborada",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Seafront",
    "distance": "7",
    "hotel": "Hotel de Alborada",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Malecon 2000",
    "distance": "7",
    "hotel": "Hotel de Alborada",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Nahin Isaias Museum",
    "distance": "7",
    "hotel": "Hotel de Alborada",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Municipal Museum",
    "distance": "7",
    "hotel": "Hotel de Alborada",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "José Joaquín de Olmedo International Airport",
    "distance": "2.9",
    "hotel": "Hotel de Alborada",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Las Iguanas Park",
    "distance": "0.1",
    "hotel": "The Park Hotel",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Plaza Presidente Vicente Rocafuerte",
    "distance": "0.25",
    "hotel": "The Park Hotel",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantUnDeli",
    "distance": "0.05",
    "hotel": "The Park Hotel",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Plaza Jerusalén",
    "distance": "0.25",
    "hotel": "Sheraton Guayaquil",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Antonio Neumane Park",
    "distance": "0.4",
    "hotel": "Sheraton Guayaquil",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Pista de Bicicross",
    "distance": "0.5",
    "hotel": "Sheraton Guayaquil",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque Japones",
    "distance": "0.75",
    "hotel": "Sheraton Guayaquil",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque Lineal",
    "distance": "1.4",
    "hotel": "Sheraton Guayaquil",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Escuela de Futbol",
    "distance": "1.5",
    "hotel": "Sheraton Guayaquil",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque Union y Progreso",
    "distance": "1.6",
    "hotel": "Sheraton Guayaquil",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantTony Roma's",
    "distance": "0.05",
    "hotel": "Sheraton Guayaquil",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantMcDonald's",
    "distance": "0.05",
    "hotel": "Sheraton Guayaquil",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantPuerto Moro",
    "distance": "0.15",
    "hotel": "Sheraton Guayaquil",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "José Joaquín de Olmedo International Airport",
    "distance": "0.8",
    "hotel": "Sheraton Guayaquil",
    "score": "8.7"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Escuela de Futbol",
    "distance": "0.95",
    "hotel": "DC Suites Aeropuerto",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Antonio Neumane Park",
    "distance": "1.1",
    "hotel": "DC Suites Aeropuerto",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque Alegria Guayaquil",
    "distance": "1.4",
    "hotel": "DC Suites Aeropuerto",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque Japones",
    "distance": "1.4",
    "hotel": "DC Suites Aeropuerto",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque de juegos",
    "distance": "1.6",
    "hotel": "DC Suites Aeropuerto",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque de juegos Sauces 2",
    "distance": "1.7",
    "hotel": "DC Suites Aeropuerto",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Roca Blanca",
    "distance": "1.8",
    "hotel": "DC Suites Aeropuerto",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantComidas Típicas Colombianas",
    "distance": "0.15",
    "hotel": "DC Suites Aeropuerto",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantCharlot",
    "distance": "0.15",
    "hotel": "DC Suites Aeropuerto",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantGate Gourmet",
    "distance": "0.2",
    "hotel": "DC Suites Aeropuerto",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santa Ana Hill Lighthouse",
    "distance": "3.4",
    "hotel": "DC Suites Aeropuerto",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santa Ana Hill",
    "distance": "3.6",
    "hotel": "DC Suites Aeropuerto",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Seafront",
    "distance": "4.5",
    "hotel": "DC Suites Aeropuerto",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Malecon 2000",
    "distance": "4.6",
    "hotel": "DC Suites Aeropuerto",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Nahin Isaias Museum",
    "distance": "4.7",
    "hotel": "DC Suites Aeropuerto",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Municipal Museum",
    "distance": "4.9",
    "hotel": "DC Suites Aeropuerto",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "TrainDurán",
    "distance": "4.7",
    "hotel": "DC Suites Aeropuerto",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "TrainEstación de Ferrocarriles Durán",
    "distance": "4.7",
    "hotel": "DC Suites Aeropuerto",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "José Joaquín de Olmedo International Airport",
    "distance": "0.5",
    "hotel": "DC Suites Aeropuerto",
    "score": "8.1"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Plaza Jerusalén",
    "distance": "0.65",
    "hotel": "Airport Hotel",
    "score": "7.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Escuela de Futbol",
    "distance": "0.9",
    "hotel": "Airport Hotel",
    "score": "7.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Pista de Bicicross",
    "distance": "1.2",
    "hotel": "Airport Hotel",
    "score": "7.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque de juegos Sauces 2",
    "distance": "1.6",
    "hotel": "Airport Hotel",
    "score": "7.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantLa Isla Del Marisco",
    "distance": "0.25",
    "hotel": "Airport Hotel",
    "score": "7.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santa Ana Hill Lighthouse",
    "distance": "3.5",
    "hotel": "Airport Hotel",
    "score": "7.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Seafront",
    "distance": "4.6",
    "hotel": "Airport Hotel",
    "score": "7.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Nahin Isaias Museum",
    "distance": "4.8",
    "hotel": "Airport Hotel",
    "score": "7.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "José Joaquín de Olmedo International Airport",
    "distance": "0.55",
    "hotel": "Airport Hotel",
    "score": "7.8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Escuela de Futbol",
    "distance": "0.2",
    "hotel": "Hotel Puerto Pacifico Guayaquil Airport",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque Alegria Guayaquil",
    "distance": "0.75",
    "hotel": "Hotel Puerto Pacifico Guayaquil Airport",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque de juegos Sauces 2",
    "distance": "0.85",
    "hotel": "Hotel Puerto Pacifico Guayaquil Airport",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Plaza Jerusalén",
    "distance": "1.1",
    "hotel": "Hotel Puerto Pacifico Guayaquil Airport",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque de la 4ta",
    "distance": "1.1",
    "hotel": "Hotel Puerto Pacifico Guayaquil Airport",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque De La 1ra",
    "distance": "1.2",
    "hotel": "Hotel Puerto Pacifico Guayaquil Airport",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Brisas Del Rio",
    "distance": "1.3",
    "hotel": "Hotel Puerto Pacifico Guayaquil Airport",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "El Parque del 8",
    "distance": "1.5",
    "hotel": "Hotel Puerto Pacifico Guayaquil Airport",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Pista de Bicicross",
    "distance": "1.5",
    "hotel": "Hotel Puerto Pacifico Guayaquil Airport",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantRestaurant Bar Karbonero",
    "distance": "0.1",
    "hotel": "Hotel Puerto Pacifico Guayaquil Airport",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantEl sabroso de chocolatito 2",
    "distance": "0.4",
    "hotel": "Hotel Puerto Pacifico Guayaquil Airport",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Antonio Neumane Park",
    "distance": "1.7",
    "hotel": "Hotel Puerto Pacifico Guayaquil Airport",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santa Ana Hill Lighthouse",
    "distance": "4.3",
    "hotel": "Hotel Puerto Pacifico Guayaquil Airport",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santa Ana Hill",
    "distance": "4.5",
    "hotel": "Hotel Puerto Pacifico Guayaquil Airport",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Antonio Neumane Park",
    "distance": "0.45",
    "hotel": "Hilton Colon Guayaquil Hotel",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque Japones",
    "distance": "0.5",
    "hotel": "Hilton Colon Guayaquil Hotel",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque Lineal",
    "distance": "0.55",
    "hotel": "Hilton Colon Guayaquil Hotel",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Plaza Jerusalén",
    "distance": "0.9",
    "hotel": "Hilton Colon Guayaquil Hotel",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Bosque Palo Santo",
    "distance": "1.2",
    "hotel": "Hilton Colon Guayaquil Hotel",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Jardin",
    "distance": "1.2",
    "hotel": "Hilton Colon Guayaquil Hotel",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque Union y Progreso",
    "distance": "1.3",
    "hotel": "Hilton Colon Guayaquil Hotel",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Roca Blanca",
    "distance": "1.5",
    "hotel": "Hilton Colon Guayaquil Hotel",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Cafe/barCafé Colón",
    "distance": "0.03",
    "hotel": "Hilton Colon Guayaquil Hotel",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantLas Palmeras del Sabor",
    "distance": "0.15",
    "hotel": "Hilton Colon Guayaquil Hotel",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantCafetería Kennedy",
    "distance": "0.15",
    "hotel": "Hilton Colon Guayaquil Hotel",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Malecon 2000",
    "distance": "4.4",
    "hotel": "Hilton Colon Guayaquil Hotel",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Nahin Isaias Museum",
    "distance": "4.4",
    "hotel": "Hilton Colon Guayaquil Hotel",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "TrainDurán",
    "distance": "6",
    "hotel": "Hilton Colon Guayaquil Hotel",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "TrainEstación de Ferrocarriles Durán",
    "distance": "6",
    "hotel": "Hilton Colon Guayaquil Hotel",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "José Joaquín de Olmedo International Airport",
    "distance": "1.6",
    "hotel": "Hilton Colon Guayaquil Hotel",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Jardines del Malecon",
    "distance": "0.05",
    "hotel": "Pepe's House Guayaquil I Self Check-In MicroHotel",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Areas verdes Malecon Simon Bolivar",
    "distance": "0.45",
    "hotel": "Pepe's House Guayaquil I Self Check-In MicroHotel",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Plaza de la Concepcion",
    "distance": "0.5",
    "hotel": "Pepe's House Guayaquil I Self Check-In MicroHotel",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Plaza Pedro Carbo Noboa",
    "distance": "0.5",
    "hotel": "Pepe's House Guayaquil I Self Check-In MicroHotel",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Plaza Colón",
    "distance": "0.5",
    "hotel": "Pepe's House Guayaquil I Self Check-In MicroHotel",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Plaza Garibaldi",
    "distance": "0.55",
    "hotel": "Pepe's House Guayaquil I Self Check-In MicroHotel",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Seafront",
    "distance": "0.55",
    "hotel": "Pepe's House Guayaquil I Self Check-In MicroHotel",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santo Domingo",
    "distance": "0.55",
    "hotel": "Pepe's House Guayaquil I Self Check-In MicroHotel",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Cornelio Vernaza",
    "distance": "0.6",
    "hotel": "Pepe's House Guayaquil I Self Check-In MicroHotel",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Malecon 2000",
    "distance": "0.6",
    "hotel": "Pepe's House Guayaquil I Self Check-In MicroHotel",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Cafe/barAzúcar de Cuba",
    "distance": "0.15",
    "hotel": "Pepe's House Guayaquil I Self Check-In MicroHotel",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantEl Malecon Restaurante",
    "distance": "0.15",
    "hotel": "Pepe's House Guayaquil I Self Check-In MicroHotel",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Cafe/barEl Mono Golosso",
    "distance": "0.2",
    "hotel": "Pepe's House Guayaquil I Self Check-In MicroHotel",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santa Ana Hill",
    "distance": "0.6",
    "hotel": "Pepe's House Guayaquil I Self Check-In MicroHotel",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santa Ana Hill Lighthouse",
    "distance": "0.75",
    "hotel": "Pepe's House Guayaquil I Self Check-In MicroHotel",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Nahin Isaias Museum",
    "distance": "0.85",
    "hotel": "Pepe's House Guayaquil I Self Check-In MicroHotel",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Municipal Museum",
    "distance": "1.1",
    "hotel": "Pepe's House Guayaquil I Self Check-In MicroHotel",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "TrainDurán",
    "distance": "4.2",
    "hotel": "Pepe's House Guayaquil I Self Check-In MicroHotel",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "TrainEstación de Ferrocarriles Durán",
    "distance": "4.2",
    "hotel": "Pepe's House Guayaquil I Self Check-In MicroHotel",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "José Joaquín de Olmedo International Airport",
    "distance": "3.5",
    "hotel": "Pepe's House Guayaquil I Self Check-In MicroHotel",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Jardines del Malecon",
    "distance": "0.2",
    "hotel": "Hotel Ramada",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Areas verdes Malecon Simon Bolivar",
    "distance": "0.25",
    "hotel": "Hotel Ramada",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Plaza Garibaldi",
    "distance": "0.35",
    "hotel": "Hotel Ramada",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Malecon 2000",
    "distance": "0.4",
    "hotel": "Hotel Ramada",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Plaza Presidente Vicente Rocafuerte",
    "distance": "0.5",
    "hotel": "Hotel Ramada",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Nahin Isaias Museum",
    "distance": "0.65",
    "hotel": "Hotel Ramada",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Plaza de la Concepcion",
    "distance": "0.7",
    "hotel": "Hotel Ramada",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Plaza de la Administracion",
    "distance": "0.7",
    "hotel": "Hotel Ramada",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Cafe/barSweet & Coffee",
    "distance": "0.03",
    "hotel": "Hotel Ramada",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantChop Chop",
    "distance": "0.03",
    "hotel": "Hotel Ramada",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantEl Malecon Restaurante",
    "distance": "0.04",
    "hotel": "Hotel Ramada",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santa Ana Hill",
    "distance": "0.8",
    "hotel": "Hotel Ramada",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Municipal Museum",
    "distance": "0.9",
    "hotel": "Hotel Ramada",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santa Ana Hill Lighthouse",
    "distance": "0.95",
    "hotel": "Hotel Ramada",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "TrainDurán",
    "distance": "4.4",
    "hotel": "Hotel Ramada",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "TrainEstación de Ferrocarriles Durán",
    "distance": "4.4",
    "hotel": "Hotel Ramada",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "José Joaquín de Olmedo International Airport",
    "distance": "3.7",
    "hotel": "Hotel Ramada",
    "score": "7.9"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Plaza Pedro Carbo Noboa",
    "distance": "0.35",
    "hotel": "Hotel Patrimonial by Greenfield",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque de la Madre",
    "distance": "0.5",
    "hotel": "Hotel Patrimonial by Greenfield",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Areas verdes Malecon Simon Bolivar",
    "distance": "0.55",
    "hotel": "Hotel Patrimonial by Greenfield",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Jardines del Malecon",
    "distance": "0.55",
    "hotel": "Hotel Patrimonial by Greenfield",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque Medardo Angel Silva",
    "distance": "0.6",
    "hotel": "Hotel Patrimonial by Greenfield",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Seafront",
    "distance": "0.6",
    "hotel": "Hotel Patrimonial by Greenfield",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque Centenario",
    "distance": "0.65",
    "hotel": "Hotel Patrimonial by Greenfield",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Malecon 2000",
    "distance": "0.65",
    "hotel": "Hotel Patrimonial by Greenfield",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantComedor el Socio",
    "distance": "0.05",
    "hotel": "Hotel Patrimonial by Greenfield",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantRestaurant La Mordiita",
    "distance": "0.1",
    "hotel": "Hotel Patrimonial by Greenfield",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantAmbigú Coffee",
    "distance": "0.15",
    "hotel": "Hotel Patrimonial by Greenfield",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Municipal Museum",
    "distance": "0.95",
    "hotel": "Hotel Patrimonial by Greenfield",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santa Ana Hill",
    "distance": "0.001",
    "hotel": "Hotel Patrimonial by Greenfield",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santa Ana Hill Lighthouse",
    "distance": "1.1",
    "hotel": "Hotel Patrimonial by Greenfield",
    "score": "8.4"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque Union y Progreso",
    "distance": "0.25",
    "hotel": "Hotel Marcelius",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque Japones",
    "distance": "0.6",
    "hotel": "Hotel Marcelius",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque Infantil Atarazana",
    "distance": "0.8",
    "hotel": "Hotel Marcelius",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque Keneddy",
    "distance": "0.95",
    "hotel": "Hotel Marcelius",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Recorrido del Periodista",
    "distance": "0.95",
    "hotel": "Hotel Marcelius",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque Lineal",
    "distance": "0.001",
    "hotel": "Hotel Marcelius",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Antonio Neumane Park",
    "distance": "0.001",
    "hotel": "Hotel Marcelius",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque Franklin Veduga Loor",
    "distance": "1.2",
    "hotel": "Hotel Marcelius",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Parque #5 Cdla FAE",
    "distance": "1.3",
    "hotel": "Hotel Marcelius",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Las Lomas",
    "distance": "1.4",
    "hotel": "Hotel Marcelius",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantCuchara Rústica",
    "distance": "0.05",
    "hotel": "Hotel Marcelius",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Cafe/barLas Delicias",
    "distance": "0.05",
    "hotel": "Hotel Marcelius",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Cafe/barA Su Gusto",
    "distance": "0.1",
    "hotel": "Hotel Marcelius",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santa Ana Hill Lighthouse",
    "distance": "2.6",
    "hotel": "Hotel Marcelius",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santa Ana Hill",
    "distance": "2.8",
    "hotel": "Hotel Marcelius",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Seafront",
    "distance": "3.3",
    "hotel": "Hotel Marcelius",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Malecon 2000",
    "distance": "3.3",
    "hotel": "Hotel Marcelius",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Nahin Isaias Museum",
    "distance": "3.4",
    "hotel": "Hotel Marcelius",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Municipal Museum",
    "distance": "3.5",
    "hotel": "Hotel Marcelius",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Botanical Garden",
    "distance": "10",
    "hotel": "Hotel Marcelius",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "José Joaquín de Olmedo International Airport",
    "distance": "1.7",
    "hotel": "Hotel Marcelius",
    "score": "8.3"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santa Ana Hill",
    "distance": "0.05",
    "hotel": "Hotel Boutique Mansion Del Rio",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Plaza Colón",
    "distance": "0.15",
    "hotel": "Hotel Boutique Mansion Del Rio",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Plaza de la Concepcion",
    "distance": "0.15",
    "hotel": "Hotel Boutique Mansion Del Rio",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Cornelio Vernaza",
    "distance": "0.2",
    "hotel": "Hotel Boutique Mansion Del Rio",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santa Ana Hill Lighthouse",
    "distance": "0.25",
    "hotel": "Hotel Boutique Mansion Del Rio",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Santa Ana Park",
    "distance": "0.35",
    "hotel": "Hotel Boutique Mansion Del Rio",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Jacinto Moran de Buitron",
    "distance": "0.4",
    "hotel": "Hotel Boutique Mansion Del Rio",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Areas verdes Malecon Simon Bolivar",
    "distance": "0.95",
    "hotel": "Hotel Boutique Mansion Del Rio",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Cafe/barLa Galeta Tasca Bar",
    "distance": "0.02",
    "hotel": "Hotel Boutique Mansion Del Rio",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Cafe/barCasija De Barro",
    "distance": "0.05",
    "hotel": "Hotel Boutique Mansion Del Rio",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Cafe/barEscalon Bar & Lounge",
    "distance": "0.05",
    "hotel": "Hotel Boutique Mansion Del Rio",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Seafront",
    "distance": "1.1",
    "hotel": "Hotel Boutique Mansion Del Rio",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Malecon 2000",
    "distance": "1.2",
    "hotel": "Hotel Boutique Mansion Del Rio",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Nahin Isaias Museum",
    "distance": "1.5",
    "hotel": "Hotel Boutique Mansion Del Rio",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Municipal Museum",
    "distance": "1.7",
    "hotel": "Hotel Boutique Mansion Del Rio",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "TrainDurán",
    "distance": "3.7",
    "hotel": "Hotel Boutique Mansion Del Rio",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "TrainEstación de Ferrocarriles Durán",
    "distance": "3.7",
    "hotel": "Hotel Boutique Mansion Del Rio",
    "score": "8.6"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Nahin Isaias Museum",
    "distance": "0.1",
    "hotel": "Manso Boutique Guest House",
    "score": "8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Plaza de la Administracion",
    "distance": "0.15",
    "hotel": "Manso Boutique Guest House",
    "score": "8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Malecon 2000",
    "distance": "0.2",
    "hotel": "Manso Boutique Guest House",
    "score": "8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Seafront",
    "distance": "0.25",
    "hotel": "Manso Boutique Guest House",
    "score": "8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Seminario Park",
    "distance": "0.35",
    "hotel": "Manso Boutique Guest House",
    "score": "8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Las Iguanas Park",
    "distance": "0.35",
    "hotel": "Manso Boutique Guest House",
    "score": "8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Cafe/barEl Café de Tere",
    "distance": "0.15",
    "hotel": "Manso Boutique Guest House",
    "score": "8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "RestaurantLa Parrilla del Ñato",
    "distance": "0.15",
    "hotel": "Manso Boutique Guest House",
    "score": "8"
        }
    )
  batch.put_item(
  Item={
    "province": "Guayaquil",
    "places": "Cafe/barJuice and Coffee",
    "distance": "0.15",
    "hotel": "Manso Boutique Guest House",
    "score": "8"
  })

print(surroundings.get_item(
    Key = {
        "places": "Cafe/barJuice and Coffee",
        "distance": "0.15",
    }
)['Item'], flush = True )