import requests
# r = requests.get('https://search.datacite.org/works/10.7910/dvn/mjfkdn')
# print(r)
# print(dir(r))
# print(help(r))
# print(r.text)
# r = requests.get('https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#/media/File:HTTP_logo.svg')
# print(r.content)
# print(r)
# print(r.ok) # check if the response is less than 400

## You can write this to a file using open function and copy it to the directory specified
# print(r.headers)

# payload = {'count': 2, 'page': 25}
# r = requests.get("https://httpbin.org/get", params=payload) #parameters
# print(r.text)
# print(r.url)
#

## post

# payload = {'username': 'admin', 'password': 'testing'}
# r = requests.post("https://httpbin.org/post", data=payload)
# # print(r.text)
# r_dict = r.json()
# print(r_dict['form'])

##Auth

# r = requests.get('https://httpbin.org/basic-auth/abcd/testing', auth=('abcd','testing'))
#try wrong username/ password and check print(r)
# print(r.text)
# print(r)
##delay

# r = requests.get('https://httpbin.org/delay/10', timeout=3)
# print(r)

##cookies
# cookies = dict(username = 'abcd')
# r = requests.get('https://httpbin.org/cookies', cookies=cookies)
# print(r.text)


# session
# s =requests.session()
# s.get('https://httpbin.org/cookies/set/sessioncookie/1234567')
# r = s.get('https://httpbin.org/cookies')
# print(r.text)