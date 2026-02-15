import requests

url = "https://api.bing.microsoft.com/api/v7/entities/ad599477-9e6d-4a0e-bab5-0edf9db7115a"
headers = {
    "Ocp-Apim-Subscription-Key": "e039e1836b0c4cd6a4808dd37db4a5a3"
}

response = requests.get(url, headers=headers)
data = response.json()

print(data)
