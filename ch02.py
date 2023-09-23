import requests
from urllib.parse import quote, quote_plus, unquote

url = "http://webscrapingfordatascience.com/"
url = "http://webscrapingfordatascience.com/basichttp/"
url = "http://webscrapingfordatascience.com/paramhttp/"
url = "http://webscrapingfordatascience.com/paramhttp/?query=test"
url = "http://webscrapingfordatascience.com/paramhttp/?query=anothertest"
url = "http://webscrapingfordatascience.com/paramhttp/?query=another%20test%3F%26"
url = "http://webscrapingfordatascience.com/paramhttp/?query=test&other=ignored"
url = "http://webscrapingfordatascience.com/paramhttp/?query=a query with spaces"
url = "http://webscrapingfordatascience.com/paramhttp/?query=complex?&"

r = requests.get(url)

# Response content
print(r.text)
# HTTP Status code
print(r.status_code)
# Textual Status code
print(r.reason)
# HTTP Response Hearders
print(r.headers)
# Request info saved as Python object
print(r.request)
# HTTP Request headers
print(r.request.headers)
#  Encoded Parameters
print(r.request.url)

raw_string = "a query with /, spaces and?&"
url = "http://webscrapingfordatascience.com/paramhttp/?query="
print("\n\nUsing quote:")
# nothing is safe, even '/', encode everything
r = requests.get(url + quote(raw_string, safe=""))
print(r.url)
print(r.text)
print("\nUsing  quote_plus:")
r = requests.get(url + quote_plus(raw_string))
print(r.url)
print(r.text)

# Rewriting the code
url = "http://webscrapingfordatascience.com/paramhttp/"
parameters = {
    "query": "a query with /, spaces and ?&"
}
r = requests.get(url, params=parameters)
print(r.url)
print(r.text)

# # Silencing requests completely
# class NonEncodedSession(requests.Session):
#     # Override the default send method
#     def send(self, *a, **kw):
#         # Revert the encoding whiich was applied
#         a[0].url = unquote(a[0].url)
#         return requests.Session.send(self, *a, **kw)
    
# my_requests = NonEncodedSession()
# url = "http://example.com/?spaces |pipe"
# r = my_requests.get(ur)
# print(r.url)
# # Will show: http://example.com/?spaces |pipe

def calc(a, b, op):
    url = "http://webscrapingfordatascience.com/calchttp/"
    params = {'a': a, 'b': b, 'op': op}
    r = requests.get(url, params=params)
    return r.text

print(calc(4, 6, '*'))
print(calc(4, 6, '/'))
print(calc("4", 6, '*'))

url = "https://en.wikipedia.org/w/index.php" + "?title=List_of_Game_of_Thrones_episodes&oldid=802553687"
r = requests.get(url)
print(r.text)
print(r.url)