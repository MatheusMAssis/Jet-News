<p align="center">
  <img width="300" height="300" src="/static/jet_news_logo.png">
</p>
<h3 align="center">
  Jet_News is a website that uses Flask to host and Google News API to get all recent tech news and display all of them separated by two categories: tech and startups, and Bootstrap to create a responsive layout. It uses Docker to create a properly deployment folder and uses Heroku to host the website on the cloud.
  </br></br>Also, it has been deployed and you can have a look clicking <a href="http://jet-news.herokuapp.com">here</a>.
</h3>
<hr>

## About
  To understand more about creating a responsive template, a deployment system and a functional website, I developed Jet_News. A simple website that gets news from an API and display them through Flask to a Responsive template made with Bootstrap. To deploy it, I used Docker and Heroku.

#### > Getting News from Google API
  I found a simple API called [News API](https://newsapi.org/) and used it to get the most recent news about Tech and Startups that were written in English. To do this, all I needed was this piece of code, that is inside *main.py*
```python
from newsapi import NewsApiClient
newsapi = NewsApiClient(api_key="myKey")

def get_articles_keyWord():
    articles = newsapi.get_everything(
                                       q="keyWord",
                                       language="en",
                                     )
    list_of_articles = articles["articles"]
    return list_of_articles
```

#### > Website display
  In order to have a good template, I was inspired by famous news websites. I also used Bootstrap to keep everything responsive, making it possible to use my website on the cellphone or on the computer.

#### Built With
* [Python](https://www.python.org/)
* [Flask](https://palletsprojects.com/p/flask/)
* [News API](https://newsapi.org/)
* [Bootstrap](https://getbootstrap.com/)
* [Docker](https://www.docker.com/)
* [Heroku](https://www.heroku.com/)

## Authors

* **Matheus Assis** - [GitHub](https://github.com/MatheusMAssis)

## Credits

Powered by [NewsAPI](https://newsapi.org/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Thanks

![Alt Text](https://media.giphy.com/media/vFKqnCdLPNOKc/giphy.gif)

Thanks for visiting my GitHub! <3
