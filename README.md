# randomJoke Descriptions
Replace "Chuck Norris" in a Chuck Norris joke with a random name

# Instructions
1. create a directory called JokeService
2. place Dockerfile, requirements.txt, and app.py in that directory
3. type "docker build -t python-jokeService ."
4. type "docker run -p 1234:5000 -d python-jokeService"
5. from the web browser, goto http://<docker-ip>:1234

#unit testing using pytest
1. in a processor with pytest (pip install pytest), create a JokeServicePytest directory and place the pytest-flask.py there.
2. run pytest -q pytest-flask.py
