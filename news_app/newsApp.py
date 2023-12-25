from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='56a727f8eac24f589754c70c13bdd0e3')


top_headlines = newsapi.get_top_headlines(q='nature',
                                          sources='bbc-news,the-verge',
                                          category='business',
                                          language='en')
dt=top_headlines['articles']
for x,y in enumerate(dt):
    print(f'{x} {y["description"]}')
