create a python3 virtual environment using command "virtualenv -p python3 <environment name>"(on linux)

activate the environment using command "source <environment name>/bin/activate"(on linux)

install requirements from requirements.txt using command "pip install -r requirements.txt".

go to the folder which has manage.py.

run command "python manage.py runserver"

http://localhost:8000/game_reset-  To reset all the parameters of the joined players and to get  the information if the game should be started or not.

http://localhost:8000/game/- Check all players' starting status

http://localhost:8000/game/<id>(get)- for getting details of a perticular player

Players having same defencive array  will play together.

http://localhost:8000/game/<id>(put)- Add defencive array for defencive role player.

PUT request for updating attacking number of offencive player.

The losing player gets removed from the game.

http://localhost:8000/refree/- to show the score of each game

http://localhost:8000/round_reset - to start the new round

Repeat the game for winners of previous round.

http://localhost:8000/refree/- to get the final winner.

Thanks
