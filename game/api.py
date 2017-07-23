from rest_framework import viewsets
from rest_framework.response import Response
from .models import Player, Refree, Game
from rest_framework.decorators import detail_route, list_route
from .serializers import PlayerSerializer, AddPlayerSerializer, RefreeSerializer
from .utils import round


class StartViewset(viewsets.ViewSet):
    queryset = Player.objects.all()

    def list(self, request):
        all_players = self.queryset
        # if players_joined ==8:
        for i, obj in enumerate(all_players):
            obj.player_id = i
            obj.defencive_array_length = 8 - int(i / 2)
            obj.attacking_no = None
            obj.defencive_array = None
            obj.points = 0
            obj.joined=True
            obj.refree = Refree.objects.get(id=1)
            if obj.player_id % 2 == 0:
                obj.role = 'offensive'
            else:
                obj.role = 'defensive'
            obj.save()
            Refree.objects.update(
                scores= '',
                winner=''
            )
        return Response({'status': 'ready to start game'})

class ResetViewSet(viewsets.ViewSet):
    queryset = Player.objects.filter(joined=True)
    def list(self,request):

        for i,obj in enumerate(Player.objects.filter(joined=True)):
            obj.player_id= i
            obj.defencive_array_length= 8-int(i/2)
            obj.attacking_no=0
            obj.defencive_array=None
            obj.points=0
            obj.refree= Refree.objects.get(id=1)
            if obj.player_id % 2 == 0:
                obj.role = 'offensive'
            else:
                obj.role = 'defensive'
            obj.save()
        return Response({'status':'ready to next round ofgame'})

class GameViewset(viewsets.ModelViewSet):
    queryset = Player.objects.filter(joined=True)

    def get_serializer_class(self):
        if self.action in ["update", "create"]:
            return self.add_serializer_class
        else:
            return self.serializer_class

    serializer_class = PlayerSerializer
    add_serializer_class = AddPlayerSerializer

class RefreeViewset(viewsets.ModelViewSet):
    queryset = Refree.objects.all()
    serializer_class = RefreeSerializer



    # @list_route()
    # def play(self, request, *args, **kwargs):
    #     queryset= Player.objects.filter(joined=True)
    #
    #     active_players=Player.objects.filter(joined=True).count()
    #     second_round=[]
    #     final_round=[]
    #
    #     for i in range(0,active_players,2):
    #         obj1=queryset[i]
    #         obj2=queryset[i+1]
    #         winner=round(obj1, obj2)
    #         second_round.append(winner)
    #
    #     for i, obj in enumerate(second_round):
    #         obj.game_id = i
    #         obj.defencive_array_length = 8 - int(i / 2)
    #         obj.points = 0
    #
    #         if obj.game_id % 2 == 0:
    #             obj.role = 'offensive'
    #         else:
    #             obj.role = 'defensive'
    #
    #         obj.save()
    #     print('round 1 winners:'+str(second_round))
    #     for i in range(0,len(second_round),2):
    #         # print(second_round[i])
    #         obj1=second_round[i]
    #         obj2=second_round[i+1]
    #         winner=round(obj1, obj2)
    #         final_round.append(winner)
    #
    #     for i, obj in enumerate(final_round):
    #         obj.game_id = i
    #         obj.defencive_array_length = 8 - int(i / 2)
    #         obj.points = 0
    #
    #         if obj.game_id % 2 == 0:
    #             obj.role = 'offensive'
    #         else:
    #             obj.role = 'defensive'
    #         obj.save()
    #     print('round 2 winners:' + str(final_round))
    #     for i in range(0, len(final_round), 2):
    #         obj1 = final_round[i]
    #         obj2 = final_round[i + 1]
    #         winner = round(obj1, obj2)
    #         print('winner:'+winner.username)
    #         return Response({'winner':str(winner)})