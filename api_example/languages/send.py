import requests

headers = {}
headers['Authentication'] = 'sush'

r = requests.get('http://localhost:8000/paradigm', eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE0NTkyNTI2LCJqdGkiOiIzYzBkOTUyZmJlNjM0MWNlYTJkNzhjNjBkZjEwZGMzMCIsInVzZXJfaWQiOjJ9.yY_9-Fxw8mFLYZR68YKFfEl3tJwun5FRgiblGPvGRtI headers=headers)

print(r.text)