import requests

headers = {}
headers['Authorization']= 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg1NzYzOTU3LCJqdGkiOiJhNjU2NTI5ZGY0ZGQ0YTNiYjBiMjMxM2Q3OTRlZTY5MiIsInVzZXJfaWQiOjF9.uduHJqPO9DrG6OU9u13mwosTdAZuRt8anBqmtBiocQc'

r = requests.get('http://127.0.0.0.1:8000/paradigm/', headers=headers)

print(r.text)