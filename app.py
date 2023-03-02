from flask import Flask, render_template
import json
import requests

app = Flask(__name__)


nytt_vaer = {
    "clearsky_day": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/01d.svg",
    "clearsky_night": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/01n.svg",
    "fair_day": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/02d.svg",
    "fair_night": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/02n.svg",
    "partlycloudy_day": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/03d.svg",
    "partlycloudy_night": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/03n.svg",
    "fog": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/15.svg",
    "cloudy": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/04.svg",
    "light_rain": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/46.svg",
    "rain": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/46.svg",
    "heavy_rain": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/10.svg",
    "light_sleet": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/47.svg",
    "sleet": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/12.svg",
    "heavy_sleet": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/48.svg",
    "light_snow": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/49.svg",
    "snow": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/13.svg",
    "heavy_snow": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/50.svg",
    "lightrainshowers_day": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/40d.svg",
    "lightrainshowers_night": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/40n.svg",
    "rainshowers_day": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/05d.svg",
    "rainshowers_night": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/05n.svg",
    "heavyrainshowers_day": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/41d.svg",
    "heavyrainshowers_night": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/41n.svg",
    "lightsleetshowers_day": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/42d.svg",
    "lightsleetshowers_night": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/42n.svg",
    "sleetshowers_day": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/07d.svg",
    "sleetshowers_night": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/07n.svg",
    "heavysleetshowers_day": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/43d.svg",
    "heavysleetshowers_night": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/43n.svg",
    "lightsnowshowers_day": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/44d.svg",
    "lightsnowshowers_night": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/44n.svg",
    "snowshowers_day": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/08d.svg",
    "snowshowers_night": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/08n.svg",
    "heavysnowshowers_day": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/45d.svg",
    "heavysnowshowers_night": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/45n.svg",
    "lightrainshowersandthunder_day": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/24d.svg",
    "lightrainshowersandthunder_night": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/24n.svg",
    "rainshowersandthunder_day": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/06d.svg",
    "rainshowersandthunder_night": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/06n.svg",
    "heavyrainshowersandthunder_day": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/25d.svg",
    "heavyrainshowersandthunder_night": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/25n.svg",
    "lightsleetshowersandthunder_day": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/26d.svg",
    "lightsleetshowersandthunder_night": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/26n.svg",
    "sleetshowersandthunder_day": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/20d.svg",
    "sleetshowersandthunder_night": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/20n.svg",
    "heavysleetshowersandthunder_day": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/27d.svg",
    "heavysleetshowersandthunder_night": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/27n.svg",
    "lightsnowshowersandthunder_day": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/28d.svg",
    "lightsnowshowersandthunder_night": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/28n.svg",
    "snowshowersandthunder_day": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/21d.svg",
    "snowshowersandthunder_night": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/21n.svg",
    "heavysnowshowersandthunder_day": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/29d.svg",
    "heavysnowshowersandthunder_night": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/29n.svg",
    "lightrainandthunder_day": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/30.svg",
    "rainandthunder_day": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/22.svg",
    "heavyrainandthunder_day": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/11.svg",
    "lightsleetandthunder_day": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/31.svg",
    "sleetandthunder_day": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/23.svg",
    "heavysleetandthunder_day": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/32.svg",
    "lightsnowandthunder_day": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/33.svg",
    "snowandthunder_day": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/14.svg",
    "heavysnowandthunder_day": "https://nrkno.github.io/yr-weather-symbols/symbols/light-mode/default/34.svg",

}




def hent_temperatur(lengdegrad, breddegrad): #temperatur
    url = f"https://api.met.no/weatherapi/locationforecast/2.0/complete?lat={lengdegrad}&lon={breddegrad}"
    res = requests.get(url, headers = { 'User-Agent': 'Elise' })
    data = res.json()
    
    return(data["properties"]["timeseries"][0]["data"]["instant"]["details"]["air_temperature"])


def hent_type_vaer(lengdegrad, breddegrad):
    url = f"https://api.met.no/weatherapi/locationforecast/2.0/complete?lat={lengdegrad}&lon={breddegrad}"
    res = requests.get(url, headers = { 'User-Agent': 'Elise' })
    data = res.json()
    type = data["properties"]["timeseries"][0]["data"]["next_1_hours"]["summary"]["symbol_code"]
    if type in nytt_vaer:
        return nytt_vaer[type]
    else:
        return type

    #return(data["properties"]["timeseries"][0]["data"]["next_1_hours"]["summary"]["symbol_code"])


#OM 3 TIMER
def hent_temperatur_om_3_timer(lengdegrad, breddegrad, timer):
    url = f"https://api.met.no/weatherapi/locationforecast/2.0/complete?lat={lengdegrad}&lon={breddegrad}"
    res = requests.get(url, headers = { 'User-Agent': 'Elise' })
    data = res.json()

    return(data["properties"]["timeseries"][timer]["data"]["instant"]["details"]["air_temperature"])

def hent_type_vaer_om_3_timer(lengdegrad, breddegrad, timer):
    url = f"https://api.met.no/weatherapi/locationforecast/2.0/complete?lat={lengdegrad}&lon={breddegrad}"
    res = requests.get(url, headers = { 'User-Agent': 'Elise' })
    data = res.json()
    type = data["properties"]["timeseries"][0]["data"]["next_1_hours"]["summary"]["symbol_code"]
    if type in nytt_vaer:
        return nytt_vaer[type]
    else:
        return type

    #return(data["properties"]["timeseries"][timer]["data"]["next_1_hours"]["summary"]["symbol_code"])


#OM 6 TIMER
def hent_temperatur_om_6_timer(lengdegrad, breddegrad, timer):
    url = f"https://api.met.no/weatherapi/locationforecast/2.0/complete?lat={lengdegrad}&lon={breddegrad}"
    res = requests.get(url, headers = { 'User-Agent': 'Elise' })
    data = res.json()

    return(data["properties"]["timeseries"][timer]["data"]["instant"]["details"]["air_temperature"])

def hent_type_vaer_om_6_timer(lengdegrad, breddegrad, timer):
    url = f"https://api.met.no/weatherapi/locationforecast/2.0/complete?lat={lengdegrad}&lon={breddegrad}"
    res = requests.get(url, headers = { 'User-Agent': 'Elise' })
    data = res.json()
    type = data["properties"]["timeseries"][0]["data"]["next_1_hours"]["summary"]["symbol_code"]
    if type in nytt_vaer:
        return nytt_vaer[type]
    else:
        return type

    #return(data["properties"]["timeseries"][timer]["data"]["next_1_hours"]["summary"]["symbol_code"])


#OM 9 TIMER
def hent_temperatur_om_9_timer(lengdegrad, breddegrad, timer):
    url = f"https://api.met.no/weatherapi/locationforecast/2.0/complete?lat={lengdegrad}&lon={breddegrad}"
    res = requests.get(url, headers = { 'User-Agent': 'Elise' })
    data = res.json()

    return(data["properties"]["timeseries"][timer]["data"]["instant"]["details"]["air_temperature"])

def hent_type_vaer_om_9_timer(lengdegrad, breddegrad, timer):
    url = f"https://api.met.no/weatherapi/locationforecast/2.0/complete?lat={lengdegrad}&lon={breddegrad}"
    res = requests.get(url, headers = { 'User-Agent': 'Elise' })
    data = res.json()
    type = data["properties"]["timeseries"][0]["data"]["next_1_hours"]["summary"]["symbol_code"]
    if type in nytt_vaer:
        return nytt_vaer[type]
    else:
        return type


#OM 12 TIMER
def hent_temperatur_om_12_timer(lengdegrad, breddegrad, timer):
    url = f"https://api.met.no/weatherapi/locationforecast/2.0/complete?lat={lengdegrad}&lon={breddegrad}"
    res = requests.get(url, headers = { 'User-Agent': 'Elise' })
    data = res.json()

    return(data["properties"]["timeseries"][timer]["data"]["instant"]["details"]["air_temperature"])

def hent_type_vaer_om_12_timer(lengdegrad, breddegrad, timer):
    url = f"https://api.met.no/weatherapi/locationforecast/2.0/complete?lat={lengdegrad}&lon={breddegrad}"
    res = requests.get(url, headers = { 'User-Agent': 'Elise' })
    data = res.json()
    type = data["properties"]["timeseries"][0]["data"]["next_1_hours"]["summary"]["symbol_code"]
    if type in nytt_vaer:
        return nytt_vaer[type]
    else:
        return type

    #return(data["properties"]["timeseries"][timer]["data"]["next_12_hours"]["summary"]["symbol_code"])

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/bergen")
def rute_bergen():
    temperatur = hent_temperatur(60.3881,5.33185)
    type_vaer = hent_type_vaer(60.3881,5.33185)
    temperatur_om_3_timer = hent_temperatur_om_3_timer(60.3881,5.33185, 3)
    type_vaer_om_3_timer = hent_type_vaer_om_3_timer(60.3881,5.33185, 3)
    temperatur_om_6_timer = hent_temperatur_om_6_timer(60.3881,5.33185, 6)
    type_vaer_om_6_timer = hent_type_vaer_om_6_timer(60.3881,5.33185, 6)
    temperatur_om_9_timer = hent_temperatur_om_9_timer(60.3881,5.33185, 9)
    type_vaer_om_9_timer = hent_type_vaer_om_9_timer(60.3881,5.33185, 9)
    temperatur_om_12_timer = hent_temperatur_om_12_timer(60.3881,5.33185, 12)
    type_vaer_om_12_timer = hent_type_vaer_om_12_timer(60.3881,5.33185, 12)
    return render_template("bergen.html", temperatur=temperatur, type_vaer=type_vaer, temperatur_om_3_timer=temperatur_om_3_timer, type_vaer_om_3_timer=type_vaer_om_3_timer, temperatur_om_6_timer=temperatur_om_6_timer, type_vaer_om_6_timer=type_vaer_om_6_timer, temperatur_om_9_timer=temperatur_om_9_timer, type_vaer_om_9_timer=type_vaer_om_9_timer, temperatur_om_12_timer=temperatur_om_12_timer, type_vaer_om_12_timer=type_vaer_om_12_timer)


@app.route("/kristiansand")
def rute_kristiansand():
    temperatur = hent_temperatur(58.1447, 7.99828)
    type_vaer = hent_type_vaer(58.1447, 7.99828)
    temperatur_om_3_timer = hent_temperatur_om_3_timer(58.1447, 7.99828, 3)
    type_vaer_om_3_timer = hent_type_vaer_om_3_timer(58.1447, 7.99828, 3)
    temperatur_om_6_timer = hent_temperatur_om_6_timer(58.1447, 7.99828, 6)
    type_vaer_om_6_timer = hent_type_vaer_om_6_timer(58.1447, 7.99828, 6)
    temperatur_om_9_timer = hent_temperatur_om_9_timer(58.1447, 7.99828, 9)
    type_vaer_om_9_timer = hent_type_vaer_om_9_timer(58.1447, 7.99828, 9)
    temperatur_om_12_timer = hent_temperatur_om_12_timer(58.1447, 7.99828, 12)
    type_vaer_om_12_timer = hent_type_vaer_om_12_timer(58.1447, 7.99828, 12)
    return render_template("kristiansand.html", temperatur=temperatur, type_vaer=type_vaer, temperatur_om_3_timer=temperatur_om_3_timer, type_vaer_om_3_timer=type_vaer_om_3_timer, temperatur_om_6_timer=temperatur_om_6_timer, type_vaer_om_6_timer=type_vaer_om_6_timer, temperatur_om_9_timer=temperatur_om_9_timer, type_vaer_om_9_timer=type_vaer_om_9_timer, temperatur_om_12_timer=temperatur_om_12_timer, type_vaer_om_12_timer=type_vaer_om_12_timer)


@app.route("/oslo")
def rute_oslo():
    temperatur = hent_temperatur(59.9138, 10.7387)
    type_vaer = hent_type_vaer(59.9138, 10.7387)
    temperatur_om_3_timer = hent_temperatur_om_3_timer(59.9138, 10.7387, 3)
    type_vaer_om_3_timer = hent_type_vaer_om_3_timer(59.9138, 10.7387, 3)
    temperatur_om_6_timer = hent_temperatur_om_6_timer(59.9138, 10.7387, 6)
    type_vaer_om_6_timer = hent_type_vaer_om_6_timer(59.9138, 10.7387, 6)
    temperatur_om_9_timer = hent_temperatur_om_9_timer(59.9138, 10.7387, 9)
    type_vaer_om_9_timer = hent_type_vaer_om_9_timer(59.9138, 10.7387, 9)
    temperatur_om_12_timer = hent_temperatur_om_12_timer(59.9138, 10.7387, 12)
    type_vaer_om_12_timer = hent_type_vaer_om_12_timer(59.9138, 10.7387, 12)
    return render_template("oslo.html", temperatur=temperatur, type_vaer=type_vaer, temperatur_om_3_timer=temperatur_om_3_timer, type_vaer_om_3_timer=type_vaer_om_3_timer, temperatur_om_6_timer=temperatur_om_6_timer, type_vaer_om_6_timer=type_vaer_om_6_timer, temperatur_om_9_timer=temperatur_om_9_timer, type_vaer_om_9_timer=type_vaer_om_9_timer, temperatur_om_12_timer=temperatur_om_12_timer, type_vaer_om_12_timer=type_vaer_om_12_timer)


@app.route("/sandvika")
def rute_sandvika():
    temperatur = hent_temperatur(59.89, 10.52)
    type_vaer = hent_type_vaer(59.89, 10.52)
    temperatur_om_3_timer = hent_temperatur_om_3_timer(59.89, 10.52, 3)
    type_vaer_om_3_timer = hent_type_vaer_om_3_timer(59.89, 10.52, 3)
    temperatur_om_6_timer = hent_temperatur_om_6_timer(59.89, 10.52, 6)
    type_vaer_om_6_timer = hent_type_vaer_om_6_timer(59.89, 10.52, 6)
    temperatur_om_9_timer = hent_temperatur_om_9_timer(59.89, 10.52, 9)
    type_vaer_om_9_timer = hent_type_vaer_om_9_timer(59.89, 10.52, 9)
    temperatur_om_12_timer = hent_temperatur_om_12_timer(59.89, 10.52, 12)
    type_vaer_om_12_timer = hent_type_vaer_om_12_timer(59.89, 10.52, 12)
    return render_template("sandvika.html", temperatur=temperatur, type_vaer=type_vaer, temperatur_om_3_timer=temperatur_om_3_timer, type_vaer_om_3_timer=type_vaer_om_3_timer, temperatur_om_6_timer=temperatur_om_6_timer, type_vaer_om_6_timer=type_vaer_om_6_timer, temperatur_om_9_timer=temperatur_om_9_timer, type_vaer_om_9_timer=type_vaer_om_9_timer, temperatur_om_12_timer=temperatur_om_12_timer, type_vaer_om_12_timer=type_vaer_om_12_timer)

@app.route("/tromsø")
def rute_tromsø():
    temperatur = hent_temperatur(69.6613, 18.9503)
    type_vaer = hent_type_vaer(69.6613, 18.9503)
    temperatur_om_3_timer = hent_temperatur_om_3_timer(69.6613, 18.9503, 3)
    type_vaer_om_3_timer = hent_type_vaer_om_3_timer(69.6613, 18.9503, 3)
    temperatur_om_6_timer = hent_temperatur_om_6_timer(69.6613, 18.9503, 6)
    type_vaer_om_6_timer = hent_type_vaer_om_6_timer(69.6613, 18.9503, 6)
    temperatur_om_9_timer = hent_temperatur_om_9_timer(69.6613, 18.9503, 9)
    type_vaer_om_9_timer = hent_type_vaer_om_9_timer(69.6613, 18.9503, 9)
    temperatur_om_12_timer = hent_temperatur_om_12_timer(69.6613, 18.9503, 12)
    type_vaer_om_12_timer = hent_type_vaer_om_12_timer(69.6613, 18.9503, 12)
    return render_template("tromsø.html", temperatur=temperatur, type_vaer=type_vaer, temperatur_om_3_timer=temperatur_om_3_timer, type_vaer_om_3_timer=type_vaer_om_3_timer, temperatur_om_6_timer=temperatur_om_6_timer, type_vaer_om_6_timer=type_vaer_om_6_timer, temperatur_om_9_timer=temperatur_om_9_timer, type_vaer_om_9_timer=type_vaer_om_9_timer, temperatur_om_12_timer=temperatur_om_12_timer, type_vaer_om_12_timer=type_vaer_om_12_timer)

