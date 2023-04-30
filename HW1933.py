import json

import requests

base_url = "https://petstore.swagger.io/v2"

status = "available"
headers = {"accept":"application/json",
           "Content-Type":"application/json",
           "api_key":"special-key"
           }
data = {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doge",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

data_new = {
  "id": 9223372036854250333,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "dogemoge",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

data=json.dumps(data)
data_new=json.dumps(data_new)

res_get = requests.get(f"{base_url}/pet/findByStatus?status={status}", headers=headers)
print(res_get.json())
print(res_get.status_code)

res_post = requests.post(f"{base_url}/pet", headers=headers, data=data)
print(res_post.json())
print(res_post.status_code)

res_put = requests.put(f"{base_url}/pet", headers=headers, data=data_new)
print(res_put.json())
print(res_put.status_code)

res_delete = requests.delete(f"{base_url}/pet/9223372036854250333", headers=headers, data=data_new)
print(res_delete.json())
print(res_delete.status_code)