import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	rname = requests.get('https://randomuser.me/api/')
	rjoke = requests.get('https://api.chucknorris.io/jokes/random')

	#print(rname.text)
	#print(rjoke.text)

	#get the random name
	rnameDict = ((eval(rname.text)["results"])[0])['name']
	rnameStr = rnameDict['first'] + " " + rnameDict['last']
	#get the random Chuck Norris joke
	rjokeDict = eval(rjoke.text)
	rjokeStr = rjokeDict["value"]

	#print(rnameDict)
	#print(rnameDict['first'])
	#print(rnameDict['last'])
	#print(rjokeDict["value"])
	#print(rnameStr)
	#print(rjokeStr)

	#replace Chuck Norris with name#
	#print(rjokeStr.replace("Chuck Norris", rnameStr))
	newjokeStr = rjokeStr.replace("Chuck Norris", rnameStr)

	return newjokeStr

if __name__ == '__main__':
	app.run(host="0.0.0.0", port=5000)

