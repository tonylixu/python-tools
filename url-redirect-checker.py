'''
This python script checks whether a list of given URLs been redirected.
'''
import sys
import requests

def check_for_redirects(url):
    try:
        r = requests.get(url, allow_redirects=False, timeout=0.5)
        if 300 <= r.status_code < 400:
            return r.headers['location']
        else:
            return '[no redirect]'
    except requests.exceptions.Timeout:
        return '[timeout]'
    except requests.exceptions.ConnectionError:
        return '[connection error]'

def check_domains(urls):
    for url in urls:
        url_to_check = url if url.startswith('http') else "http://%s" % url
        redirect_url = check_for_redirects(url_to_check)
        print("%s => %s" % (url_to_check, redirect_url))