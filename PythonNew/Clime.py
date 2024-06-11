import requests

def get_tempeture(City):
    url = "http://wttr.in/" + City + "?format=3"
    answer = requests.get(url)
    if answer.status_code ==200:
        print(answer.text)
    else:
        print("Verify your city")
        
city = input("City?: ")
get_tempeture(city)