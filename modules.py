import time
def abc(name):
    print("Hello", name)


abc("Jijo")
a = time.time()
print(a)
# time.sleep(5)
b = time.ctime(a)
print(b)
c = time.localtime()
print(c)
d = time.gmtime()
print(d)
e = time.mktime(c)
print(e)
f = time.asctime(c)
print(f)
g = time.strftime("%m-%y-%d")
print(g)
h = time.strptime("Sat Feb 13 11:19:09 2021")
print(h)
