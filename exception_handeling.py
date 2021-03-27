try:
    with open('test_json.py') as a:
        print(a)
except FileNotFoundError:
    print("File not found")
else:
    print("All good!!!")
finally:
    print("Inside Finally!!!")
# with open('test_jso.py') as a:
#     print(a)