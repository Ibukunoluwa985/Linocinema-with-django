from requests.exceptions import ConnectionError
import requests

def get_linocinemablog_random_post():
    try:
        url = "https://www.linocinemablog.com/blog/api/random_blog_list/"
        r = requests.get(url)
        if r.status_code == 200:
            posts = r.json()
            return posts
        return None
    except ConnectionError as e:
        return None