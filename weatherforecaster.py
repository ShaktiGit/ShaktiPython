#http://www.pythonforbeginners.com/scraping/scraping-wunderground
#https://gist.github.com/jleclanche/2689784
#https://www.wunderground.com/weather/api/d/docs?d=resources/code-samples&MR=1
#key=3464c5f1e3322ac5
import urllib2
import json
f = urllib2.urlopen('http://api.wunderground.com/api/3464c5f1e3322ac5/geolookup/conditions/q/IA/Cedar_Rapids.json')
json_string = f.read()

parsed_json = json.loads(json_string)

location = parsed_json['location']['city']

temp_f = parsed_json['current_observation']['temp_f']

print("Location: ",location)
print("temp_f: ",temp_f)

f.close()
