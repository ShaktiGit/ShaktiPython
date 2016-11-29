# https://straymarcs.net/2014/12/how-to-create-your-own-weather-forecast-program-using-python/
# http://stackoverflow.com/questions/24069197/httpresponse-object-json-object-must-be-str-not-bytes
#import urllib2

#UserID: Shakti006
#pwd: weatherunderground@2016
#key ID: 9eaeebc1ed4d615c
#Project Name: WeatherForcaster
#Company website: WeatherForcaster.com
#mail: shaktijena2012@gmail.com
import urllib
import json
key = "9eaeebc1ed4d615c"
while 1:
    zip = input('For which ZIP code would you like to see the weather? ')
    url = 'http://api.wunderground.com/api/' + key + '/geolookup/conditions/q/PA/' + zip + '.json'
    f = urllib.request.urlopen(url).read()
    parsed_json =json.loads(f.decode('utf-8'))
    city = parsed_json['location']['city']
    state = parsed_json['location']['state']
    weather = parsed_json['current_observation']['weather']
    temperature_string = parsed_json['current_observation']['temperature_string']
    feelslike_string = parsed_json['current_observation']['feelslike_string']
    print ('Weather in ' + city + ', ' + state + ': ' + weather.lower() + '. The temperature is ' + temperature_string + ' but it feels like ' + feelslike_string + '.')
f.close()
