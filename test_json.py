import json
# x = '''{
#   "states": [
#     {
#       "name": "Alabama",
#       "abbreviation": "AL"
#     },
#     {
#       "name": "Alaska",
#       "abbreviation": "AK"
#     }
#   ]
# }'''
#
# ## loads
# y = json.loads(x)
# print(y)
# print(type(y))
# print(type(y["states"]))
#
# for state in y["states"]:
#     print(state["name"],state["abbreviation"])
#     del state["abbreviation"]
#
# newstring = json.dumps(y, indent=2, sort_keys=True)
# print(newstring)


with open('sample_json_file.json') as f:
    data = json.load(f)
for state in data['states']:
    # print(state)
    del state['abbreviation']
    print(state)

with open('new_states.json','w') as f:
    json.dump(data, f, indent=2)

