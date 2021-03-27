# import urllib
from urllib import request
import urllib.parse
# print(dir(urllib))
# print(dir(request))
# resp = request.urlopen("https://en.wikipedia.org/wiki/Wikipedia")
# print(resp.code)
# print(resp.length)
# print(resp.peek()) # prints part of the website output. b in the start indicates that the response is in bytes
# data = resp.read()
# print(type(data))
# output = data.decode("UTF-8")
# print(type(output))
# print(output)

##post
# url = 'https://pythonprogramming.net/'
# values = {'s': 'basic', 'submit': 'search'}
#
# data = urllib.parse.urlencode(values)
# print(data)
# data = data.encode('utf-8')
# req = urllib.request.Request(url, data)
# print(str(req.data))
# resp = urllib.request.urlopen(req)
# resp_data = resp.read()
# print(resp_data)


## error handling

try:
    x = urllib.request.urlopen('https://www.google.com/search?q=test')
    print(x.read())

except Exception as e:
    print(str(e))
