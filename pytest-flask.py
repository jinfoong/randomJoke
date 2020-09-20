import requests

def getJoke(x):
	response = requests.get(x)
	return response.status_code

def test_answer():
	assert getJoke("http://192.168.99.100:1234") == 200
	