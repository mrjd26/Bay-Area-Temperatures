from django.shortcuts import render,render_to_response
from django.http import HttpResponse
import requests
import json

def index(request):

	Weather_Channel_API_Key = '0545ae02f230b8e0'

	# api format two words = capitalized & separated by underscore, e.g., San_Jose.

	Cities_list = ['San_Francisco','San_Jose',
			'Mountain_View','Sunnyvale','Los_Gatos',
			'Oakland','Napa','Sausalito','Santa_Cruz',
			'Redwood_City','Menlo_Park','San_Mateo',
			'Daly_City','Gilroy','Boulder_Creek']	

	#city,temperature list
	temperatures_list={}

	for city in Cities_list:

		r = requests.get("http://api.wunderground.com/api/"+Weather_Channel_API_Key+"/conditions/q/CA/"+city+".json")	

		data = r.json()

		temperatures_list[(data["current_observation"]["display_location"]["city"])]=round((data["current_observation"]["temp_f"]),1)

	if request.GET.get('update'):
		return HttpResponse(json.dumps(temperatures_list),content_type="application/json")

	else:
		return render_to_response('index.html',{'temperatures_list':temperatures_list})


