import json

import requests
# resp1 = requests.get('https://www.google.com')
# print(resp1)
# resp2 = requests.get("https://eoswo8wq169wagi.m.pipedream.net")
# print(resp2)

# resp3 = requests.get("https://reqres.in/api/users?page=2")
# print("This is a string: \n"+resp3.text)
# jsonresp = resp3.json()
# print(jsonresp["data"][0]["first_name"])

# resp4 = requests.get("https://eoswo8wq169wagi.m.pipedream.net?key1=val1&key2=val2")

# queryparams = {"name":"Adit", "Surname": "Shah"}
# resp5 = requests.get("https://eo69sfrg1bn08uv.m.pipedream.net", params=queryparams)

# headers = {'my-token' : 'AditShah', 'Greet' : 'Hello'}
# resp6 = requests.get("https://eo69sfrg1bn08uv.m.pipedream.net", headers=headers)

# resp7 = requests.post('https://eo69sfrg1bn08uv.m.pipedream.net')
# resp8 = requests.delete("https://eo69sfrg1bn08uv.m.pipedream.net")
# resp9 = requests.put("https://eo69sfrg1bn08uv.m.pipedream.net")
# resp10 = requests.patch("https://eo69sfrg1bn08uv.m.pipedream.net")

# payload = {'name': 'Adit', 'surname': 'Shah'}
# resp11 = requests.post("https://eo69sfrg1bn08uv.m.pipedream.net", json=payload)
# resp12 = requests.post("https://httpbin.org/post", data=payload)
# print(resp12.text)


# files = {'file' : open('cat.png', 'rb')}
# r = requests.post(url='https://eo69sfrg1bn08uv.m.pipedream.net', files=files)

resp = requests.get("https://xkcd.com/354/")
print(resp.text)