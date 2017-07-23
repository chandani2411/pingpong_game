create a python3 virtual environment using command "virtualenv -p python3 <environment name>"(on linux)

activate the environment using command "source <environment name>/bin/activate"(on linux)

install requirements from requirements.txt using command "pip install -r requirements.txt".

go to the folder which has manage.py.

run command "python manage.py runserver"

http://localhost:8000/game(get) - for list of all joined players

http://localhost:8000/game(post)- for adding a new player

http://localhost:8000/game/<id>(get)- for getting details of a perticular player

http://localhost:8000/game(put)- update player username, password or joined status

** http://localhost:8000/reset- to reset all the parameters of the joined players and to get  the information if the game should be started or not.

*please donot start the game without hitting http://localhost:8000/reset/ api.

once the api says its time to start the game, hit http://localhost:8000/game/play

It will take some time to announce the winner

to see the status of matches, see the terminal where server is running. I have written the print statements that reveal the current status of the game.

all the attacking numbers and defence array are random generated using static method in models.py

Thanks
