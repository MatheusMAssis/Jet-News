#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, make_response, request,render_template
from flask_cors import CORS
from newsapi import NewsApiClient

app = Flask(__name__)
origins = ["*", "/*","http://127.0.0.1:4200"]

CORS(app, resources={ r'/*': {'origins': origins}}, supports_credentials=True)
app.config['CORS_HEADERS'] = 'Content-Type'


app = Flask(__name__)
newsapi = NewsApiClient(api_key="653957fc61a94fb0b5525cdf0d0755a9")

def get_articles_on_startups():
    articles = newsapi.get_everything(
                                         q="startup",
                                         language="en",
                                     )
    list_of_articles = articles["articles"]
    print(len(list_of_articles))
    return list_of_articles[0], list_of_articles[1], list_of_articles[2]

def get_articles_on_tech():
    articles = newsapi.get_everything(
                                         q="tech",
                                         language="en",
                                     )
    list_of_articles = articles["articles"]
    print(len(list_of_articles))
    return list_of_articles[0], list_of_articles[1], list_of_articles[2]


@app.route("/", methods=["GET"])
def home():
    first_technews, second_technews, third_technews = get_articles_on_tech()
    first_stupnews, second_stupnews, third_stupnews = get_articles_on_startups()

    return render_template("index.html",
                            first_technews_image=first_technews["urlToImage"],
                            first_technews_title=first_technews["title"],
                            first_technews_text=first_technews["description"],
                            first_technews_hyperlink=first_technews["url"],
                            
                            second_technews_image=second_technews["urlToImage"],
                            second_technews_title=second_technews["title"],
                            second_technews_text=second_technews["description"],
                            second_technews_hyperlink=second_technews["url"],

                            third_technews_image=third_technews["urlToImage"],
                            third_technews_title=third_technews["title"],
                            third_technews_text=third_technews["description"],
                            third_technews_hyperlink=third_technews["url"],

                            first_stupnews_image=first_stupnews["urlToImage"],
                            first_stupnews_title=first_stupnews["title"],
                            first_stupnews_hyperlink=first_stupnews["url"],

                            second_stupnews_image=second_stupnews["urlToImage"],
                            second_stupnews_title=second_stupnews["title"],
                            second_stupnews_hyperlink=second_stupnews["url"], 

                            third_stupnews_image=third_stupnews["urlToImage"],
                            third_stupnews_title=third_stupnews["title"],
                            third_stupnews_hyperlink=third_stupnews["url"], 
                          )

if __name__ == "__main__":
    # app.run()
    
    # dev
    #app.run(use_reloader=False, port=5000)
    # prod
    app.run(host='0.0.0.0')
