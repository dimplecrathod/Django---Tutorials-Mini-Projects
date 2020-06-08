import requests

headers = {}
headers['Authorization']= 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg1NzY4NDcwLCJqdGkiOiJjM2UyM2FlZTU5MmI0ZmM4YjAzMzJmNTA2M2MxODQ5ZSIsInVzZXJfaWQiOjF9.C5f4iD8zzgbmILQ2sVyF-vaZKr7N2e-k-q-uLVJCxt0'

r = requests.get('http://127.0.0.0.1:8000/languages/', headers=headers)

print(r.text)