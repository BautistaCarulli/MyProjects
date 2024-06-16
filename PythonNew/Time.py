import pytz
from datetime import datetime

country_timezones = {
    "Argentina": "America/Argentina/Buenos_Aires",
    "Brazil": "America/Sao_Paulo",
    "Chile": "America/Santiago",
    "Colombia": "America/Bogota",
    "Spain": "Europe/Madrid",
    "Mexico": "America/Mexico_City",
    "Perú": "America/Lima",
    "United States": "America/New_York",
    "Uruguay": "America/Montevideo",
    "Germany": "Europe/Berlin",
    "France": "Europe/Paris",
    "Italy": "Europe/Rome",
    "Greece": "Europe/Athens"
}

def get_current_time_in_country(country):
    timezone = country_timezones.get(country)
    if not timezone:
        return f"Sorry, I do not have information for {country}."
    
    country_tz = pytz.timezone(timezone)
    country_time = datetime.now(country_tz)
    return country_time.strftime('%Y-%m-%d %H:%M:%S')


user_input = input("Please add the country´s name: ")

current_time = get_current_time_in_country(user_input)
print(f"Current time in {user_input} is: {current_time}")
