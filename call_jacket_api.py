import requests
import http.client, urllib.request, urllib.parse, urllib.error, base64, requests, json 
 
#Subscribtion to Cognitive Services
#Simply replace subscription key with your Cognitive API Subscription Key the key below is for Demo purpose only
subscription_key = '032a5d50c0a14e3a8a0b831e9ccbab61'
uri_base = 'https://southcentralus.api.cognitive.microsoft.com/customvision/v1.1/Prediction/c68956a1-8ac5-4d1e-ba8b-311978e4a93d/url?iterationId=da0a8dcb-41be-4387-8850-4ec6262ca48d'  
 
headers = {
 
    'Content-Type': 'application/json',
 
    'Ocp-Apim-Subscription-Key': subscription_key,
    
    'Prediction-Key' : subscription_key
 
}

body = {'url': 'http://road.cc/sites/default/files/styles/main_width/public/images/Rapha%20Hardshell%20Jacket/Rapha%20Hardshell%20Jacket.JPG?itok=52GEJo5i'}
  
try:
 
     # Execute the REST API call and get the response.
 
    response = requests.request('POST', uri_base, json=body,data=None, headers=headers)
    
 
 
    print ('Response:')
 
    parsed = json.loads(response.text)
 
    print (json.dumps(parsed, sort_keys=True, indent=2))
 
 
 
except Exception as e:
 
    print('Error:')
 
    print(e)