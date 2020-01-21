from newsapi import NewsApiClient

# initializing
newsapi = NewsApiClient(api_key="653957fc61a94fb0b5525cdf0d0755a9")

all_articles = newsapi.get_top_headlines(
                                            q="startup",
                                            category="technology",
                                        )

print(all_articles)