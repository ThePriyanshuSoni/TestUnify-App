import requests
import random
import string
# Assuming you've obtained the token from the API provider
token = "eyJhbGciOiJSUzI1NiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICJ6LWlEQVVidXlTSDYzRUFQVC1nUjRXR2lZNktsZEF2VGlhWU9SU242VkhFIn0.eyJleHAiOjE2OTI5OTM2MzIsImlhdCI6MTY5Mjk1NzYzMiwiYXV0aF90aW1lIjoxNjkyOTU3NjMyLCJqdGkiOiJmODRhM2QyNC1hYzM2LTQyM2UtYTcwZC1jMmQzMTU1OTNmMjAiLCJpc3MiOiJodHRwczovL2RldmlkcC5pbnZlbnR1bS5jby9hdXRoL3JlYWxtcy9wcml5YW5zaHUiLCJzdWIiOiI0ZGMzYzFiMy00ZWUxLTRlYjYtYWZiMC05YmU3YzE5YjYzOWYiLCJ0eXAiOiJCZWFyZXIiLCJhenAiOiJ1bmlmeW5nLWdhdGV3YXkiLCJub25jZSI6ImowRGtOdzJKMHpjZlFZLVNqYlA4RzJQSE9tejFiYW1abm5xODdoVVIzckUiLCJzZXNzaW9uX3N0YXRlIjoiN2UyOGI1NjktMzE5Yi00MGRhLTk0ODctOTA0OGRlNDNkMWI0IiwiYWNyIjoiMSIsInJlYWxtX2FjY2VzcyI6eyJyb2xlcyI6WyJvd25lciJdfSwic2NvcGUiOiJvcGVuaWQgcHJvZmlsZSBlbWFpbCIsInNpZCI6IjdlMjhiNTY5LTMxOWItNDBkYS05NDg3LTkwNDhkZTQzZDFiNCIsInRlbmFudF9pZCI6InByaXlhbnNodSIsInVzZXJfaWQiOiJwcml5YW5zaHUiLCJuYW1lIjoicHJpeWFuc2h1IHNvbmkiLCJwcmVmZXJyZWRfdXNlcm5hbWUiOiJwcml5YW5zaHUiLCJnaXZlbl9uYW1lIjoicHJpeWFuc2h1IiwiZmFtaWx5X25hbWUiOiJzb25pIiwiZW1haWwiOiJwcml5YW5zaHUuc29uaUBpbnZlbnR1bS5uZXQifQ.DQoGbTX1R24qQisL7naw27G-RVKOWgXqYVlt6YK4NU3hPPhZzwhPBYSfHhxCT2xBOdMbXKEplWvha2reT_mF3Is4eiB69cuepAxmBYpklHoAje4tuQI679GOQjKwtKF7o_E-SsdutA4rFrDGJWqO6n4Vfd1EgXdd4E42fMJ8vewdA1pkgrRcnt8A7V87uz2s9R4Bbl2haUCKcaKZCXuzV5ilm7gP68vYRivDbYk0Fw4UxDatq41ZjuoeGbuE1r04T-K2gOSw_6CZN0ZQeEiZDAqksSPq4rXId00MH7TeDb05AwG8DENZAcIuD6sEp3I7fZacBETg3jvWRJ_JJbeqgw"

headers = {"Authorization": f"Bearer {token}",}

# Make a request to the API endpoint
url = "http://unifyng.inventum.co/crm/personal_details/64d36cfafb40d7590f8cc342"
url1= "http://unifyng.inventum.co/settings/tags/save"

payload = {
              "tagName": (name),
              "description": "",
              "backgroundColor":
            {
              "r": 0,
              "g": 0,
              "b": 0,
              "a": 1
            }
          }

response = requests.post(url1, headers=headers, json=payload)

# Process the API response as needed
print(response.status_code)
print(response.json())







n = 7
m = 10
name = ''.join(random.choices(string.ascii_lowercase, k=n))
randomName = str(name)
randomMobile = ''.join(random.choices(string.octdigits, k=m))
randomStrUpper = ''.join(random.choices(string.ascii_uppercase + string.digits, k=n))