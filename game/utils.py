from .models import Game, Player
def round(obj1,obj2):
    while obj1.points < 5 and obj2.points < 5:
        if obj1.role == 'offensive' and obj2.role == 'defensive':
            attacking_no = obj1.attacking_no
            defensive_array = obj2.defencive_array
            if attacking_no in defensive_array:
                obj2.points = obj2.points + 1
                obj2.role = 'offensive'
                obj2.save()
                obj1.role = 'defensive'
                obj1.save()

                print(obj1.points, obj2.points)
                if obj2.points == 5:
                    break
            else:
                obj1.points = obj1.points + 1
                obj1.save()
                print(obj1.points, obj2.points)
                if obj1.points==5:
                    break

        elif obj1.role == 'defensive' and obj2.role == 'offensive':
            attacking_no = obj2.attacking_no
            defensive_array = obj1.defencive_array
            if attacking_no in defensive_array:
                obj1.points = obj1.points + 1
                obj1.role = 'offensive'
                obj1.save()
                obj2.role = 'defensive'
                obj2.save()
                print(obj1.points, obj2.points)

                if obj1.points == 5:
                    break
            else:
                obj2.points = obj2.points + 1
                obj2.save()
                print(obj1.points, obj2.points)

                if obj2.points == 5:
                    break
    print('-------------------------------------')
    if obj1.points == 5:
        return obj1
    elif obj2.points == 5:
        return obj2
    else:
        return None

# def game(game_id):
#     queryset = Player.objects.filter(joined=True)
#
#     active_players = Player.objects.filter(joined=True).count()
#     # second_round = []
#     # final_round = []
#
#     for i in range(0, active_players, 2):
#         obj1 = queryset[i]
#         obj2 = queryset[i + 1]
#         winner = round(obj1, obj2)
#         Game.objects.update(
#             gid=game_id,
#             round_winners=round_winners.append(winner)
#         )



