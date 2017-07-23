from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
import requests
from .models import Player, Refree

@receiver(post_save, sender=Player)
def update_players(sender, **kwargs):
    current_player=kwargs.get('instance')
    # if current_player.active:
    len= current_player.defencive_array_length
    queryset=sender.objects.filter(defencive_array_length=len).exclude(id= kwargs.get('instance').id).exclude(joined=False)
    if queryset:
        opponent=queryset[0]


        if opponent.role=='defensive' and current_player.role=='offensive':
            if current_player.attacking_no and opponent.defencive_array:
                defence_list = opponent.defencive_array.split(',')
                if str(current_player.attacking_no) in defence_list:
                    defence_list.remove(str(current_player.attacking_no))
                    Player.objects.filter(id=opponent.id).update(
                        points=opponent.points + 1,
                        role='offensive',
                        defencive_array=','.join(defence_list)
                    )

                    Player.objects.filter(id=current_player.id).update(
                        role='defensive'
                    )
                    print(opponent.defencive_array)

                else:
                    Player.objects.filter(id=current_player.id).update(
                        points=current_player.points + 1
                    )
                    print(Player.objects.filter(id=current_player.id))

        elif opponent.role == 'offensive'and current_player.role=='defensive':
            if opponent.attacking_no and current_player.defencive_array:
                defence_list = opponent.defencive_array.split(',')
                if str(opponent.attacking_no) in defence_list:
                        defence_list.remove(str(opponent.attacking_no))
                        Player.objects.filter(id=current_player.id).update(
                            points=current_player.points + 1,
                            role='offensive',
                            defencive_array=','.join(defence_list)
                        )
                        Player.objects.filter(id=opponent.id).update(
                        role='defensive'
                        )
                        print(current_player.defencive_array)

                else:
                    Player.objects.filter(id=opponent.id).update(
                        points=opponent.points + 1
                    )
                    print(Player.objects.filter(id=current_player.id))
        # refree= Refree.objects.filter(id=1)
        if Player.objects.get(id=opponent.id).points == 5:

            Player.objects.filter(id=current_player.id).update(
                joined=False
            )
            Refree.objects.filter(id=1).update(
                scores=str(Refree.objects.get(id=1).scores) + '________________' + str(
                    opponent.username) + ':5 vs ' +
                    current_player.username + ':' + str(Player.objects.get(
                    id=current_player.id).points)
            )
            requests.get('http://localhost:8000/reset/')

        elif Player.objects.get(id=current_player.id).points == 5:
            Player.objects.filter(id=opponent.id).update(
                joined=False
        )
            Refree.objects.filter(id=1).update(
                scores=str(Refree.objects.get(id=1).scores) + '  |!|  ' + current_player.username + ':5 vs ' + opponent.username + ':' + str(Player.objects.get(
                    id=opponent.id).points)
            )
            requests.get('http://localhost:8000/reset/')

        if Player.objects.filter(joined=True).count()==1:
            Refree.objects.update(
                winner=Player.objects.get(joined=True).username
            )
