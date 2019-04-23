# -*- coding: utf-8 -*-

import scrapy

import json
import re






class BbcbotSpider(scrapy.Spider):
    name = 'bbcbot'
    #allowed_domains = ['hhttps://www.finecooking.com/recipe/herbed-dutch-baby-creamy-mushrooms-leeks']
    start_urls = ['https://www.bbc.com/food/recipes/easy_chocolate_cake_31070']

    def parse(self, response):
        parsed= json.loads(response.xpath('//script[@type="application/ld+json"]/text()').get())
        heading=parsed['name']
        image=parsed['image']
        if type(image)==list:
            image=image[0]
        elif type(image)==dict:
            image=image['url']
        elif type(image)==str:
            image=image
        ing=parsed['recipeIngredient']
        cooking_method=parsed['recipeInstructions']
        if type(cooking_method)==str:
            cooking_method=re.split(r'\s{2,}', cooking_method)
        else:
            cooking_method=cooking_method

        scraped_info = {
            'heading':heading,
            'image': image,
            'ingredients':ing,
            'cooking_method':cooking_method
        }

        yield scraped_info





