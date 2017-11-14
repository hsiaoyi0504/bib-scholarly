import scholarly
import requests

with open('example.txt') as f:
    for line in f:
        title = line.rstrip('\n')
        pub = next(scholarly.search_pubs_query(title))
        r = requests.get(pub.url_scholarbib)
        print(r.text)