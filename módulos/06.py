import requests
import pandas as pd

url = "http://www.omdbapi.com/"
params = {"t": "Titanic", "apikey": "YOUR_KEY"} 
resp = requests.get(url, params=params)
print("Status code:", resp.status_code)

if resp.status_code == 200:
    data = resp.json()
    df = pd.DataFrame([{
        "title": data.get("Title"),
        "year": data.get("Year"),
        "rated": data.get("Rated"),
        "released": data.get("Released"),
        "runtime": data.get("Runtime"),
        "director": data.get("Director")
    }])
    print(df)
else:
    print("Erro ao acessar OMDB")