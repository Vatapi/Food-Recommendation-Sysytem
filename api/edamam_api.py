import requests
import json

payload = {'q':"potato and paneer" , 'app_id':'6cbe9008' , 'app_key':'c300031de9d768b3b7ca4fa828c95e0e' , 'from':0 , 'to':50}
r = requests.get(url="https://api.edamam.com/search" , params=payload)

print(r.status_code);
response = json.loads(r.content)
# print(response)
i=0
for y in response['hits']:
    print(y['recipe']['label']);
    ingr = y['recipe']['ingredients']
    for x in ingr:
        print(x['text'] + " and the right amount is " + str(x['weight']))
    print()
    i = i+1

print("hello")
