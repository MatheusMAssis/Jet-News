# initializing
#newsapi = NewsApiClient(api_key="653957fc61a94fb0b5525cdf0d0755a9")

#all_articles = newsapi.get_top_headlines(
#                                            q="tech",
#                                            category="technology",
#                                            language="en"
#                                        )

#print(all_articles["totalResults"])

from flask import Flask, render_template
from newsapi import NewsApiClient

app = Flask(__name__)
newsapi = NewsApiClient(api_key="653957fc61a94fb0b5525cdf0d0755a9")

def get_articles_on_startups():
    articles = newsapi.get_top_headlines(
                                            q="startup",
                                            category="technology",
                                            language="en",
                                        )
    list_of_articles = articles["articles"]

def get_articles_on_tech():
    articles = newsapi.get_top_headlines(
                                            q="tech",
                                            category="technology",
                                            language="en",
                                        )
    list_of_articles = articles["articles"]


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()