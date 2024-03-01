import requests
import json

def get_json_from_server(path):
    url = "http://127.0.0.1:8000/" + path
    response = requests.request("GET", url)

    if response.status_code == 200:
        json_data = response.json()
        return json_data
    else:
        print(f"Error: {response.status_code}")
        return None

def send_json_to_server(localpath, serverpath):
    with open(localpath, 'r') as json_file:
        json_data = json.load(json_file)

    # Specify the server URL where you want to send the data
    server_url = "http://127.0.0.1:8000/" + serverpath

    # Send the JSON data to the server
    response = requests.post(server_url, json=json_data)

    if response.status_code == 200:
        print("JSON data sent successfully!")
    else:
        print(f"Error sending data. Status code: {response.status_code}")

jsondirectory = "C:\Users\kavet\PycharmProjects\MagicGrow\jsonfiles"
jsonserverdirectory = "C:\Users\kavet\PycharmProjects\MagicGrow\jsonfileslocal"

send_json_to_server(jsondirectory + "\EC.json", jsonserverdirectory)
send_json_to_server(jsondirectory + "\ECChanges.json", jsonserverdirectory)
send_json_to_server(jsondirectory + "\LightChanges.json", jsonserverdirectory)
send_json_to_server(jsondirectory + "\pH.json", jsonserverdirectory)
send_json_to_server(jsondirectory + "\pHDownChanges.json", jsonserverdirectory)
send_json_to_server(jsondirectory + "\pHUpChanges.json", jsonserverdirectory)
send_json_to_server(jsondirectory + "\Temperature.json", jsonserverdirectory)
send_json_to_server(jsondirectory + "\WaterDownPumpChanges.json", jsonserverdirectory)
send_json_to_server(jsondirectory + "\WaterUpPumpChanges.json", jsonserverdirectory)