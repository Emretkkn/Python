import json
# dictionary
person_str = '{"Name":"Emre", "Languages": ["Python","SQL","C#"]}'
person_dict = {"Name":"Emre", "Languages": ["Python","SQL","C#"]}
# JSON to Dict
# result = json.loads(person_str)
# print(result)
# print(type(result))

# with open("person.json") as file:
#     veri = json.load(file)
#     print(veri["Languages"][2])

rumeysa = {
    "name": "Rumeysa",
    "surname": "Koyun",
    "city": "Balikesir"
}

# Dict to JSON string   
# cevir = json.dumps(rumeysa)
# print(cevir)
# print(type(cevir))

with open("person.json","a") as file:
    json.dump(rumeysa, file)
    file.close()
# person_dict = json.loads(person_str)
# result = json.dumps(person_dict, indent=2, sort_keys=True)
# print(person_dict)
# print(result)
