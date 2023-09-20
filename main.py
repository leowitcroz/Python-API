import requests

api_key ='cb1e687b41ba41ffa18efd211e7d2bdb'
url ='https://newsapi.org/v2/everything?q=tesla&from=2023-08-20&sortBy=publishedAt&apiKey=cb1e687b41ba41ffa18efd211e7d2bdb'

request = requests.get(url)
content = request.json()
for article in content['articles']:
    print(article['title'])