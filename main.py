from http.server import HTTPServer, BaseHTTPRequestHandler
from fastapi import FastAPI

from bs4 import BeautifulSoup
import requests
import json
from pydantic import BaseModel


# class Item(BaseModel):
#

class Dish:
    def __init__(self, categoryName, id, name, description, price):
        self.categoryName = categoryName
        self.id = id
        self.name = name
        self.description = description
        self.price = price

    def __print__(self):
        print("")


source = requests.get('https://www.10bis.co.il/NextApi/GetRestaurantMenu?culture=en&uiCulture=en&restaurantId=19156&deliveryMethod=pickup').text
soup = BeautifulSoup(source, 'lxml')
data = soup.body.p.text

err = json.loads(data)
dishList = err['Data']['categoriesList']

dishes = {}
for category in dishList:
    curr_category = category['categoryName']
    dish_by_category = {}
    print(curr_category)
    for dish in category['dishList']:
        curr_dish = Dish(curr_category, dish['dishId'], dish['dishName'], dish['dishDescription'],
                         dish['dishPrice'])
        dish_by_category[dish['dishId']] = curr_dish
        print(curr_dish.id)
    dishes[curr_category] = dish_by_category



app = FastAPI()

@app.get("/drinks")
def drinks():
    return dishes["Drinks"]

@app.get("/drink/{drink_id}")
def drink(drink_id: int):
    return dishes["Drinks"][drink_id]

@app.get("/pizzas")
def drinks():
    return dishes["Pizzas"]

@app.get("/pizza/{pizza_id}")
def drink(pizza_id: int):
    return dishes["Pizzas"][pizza_id]

@app.get("/desserts")
def drinks():
    return dishes["Desserts"]

@app.get("/dessert/{dessert_id}")
def drink(dessert_id: int):
    return dishes["Desserts"][dessert_id]

# @app.post("/order")
# def order():


