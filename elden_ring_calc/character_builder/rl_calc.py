from models import ClassStartingStats


player_dict = {
    "lv" : 0,
    "vig" : 0,
    "mnd" : 0,
    "end" : 0,
    "str" : 0,
    "dex" : 0,
    "int" : 0,
    "fai" : 0,
    "arc" : 0
}

levels_dict = {
    "Hero" : 0,
    "Bandit" : 0,
    "Astrologer": 0,
    "Warrior" : 0,
    "Prisoner" : 0,
    "Confessor" : 0,
    "Wretch" : 0,
    "Vagabond" : 0,
    "Prophet" : 0,
    "Samurai" : 0
}

def get_stats(dict):
    int_dict = dict.copy()
    for key in dict:
        if key == "level":
            dict[key] = 0
        else:
            dict[key] = input("%s: " % key)
    for key, value in dict.items():
        if value == "":
            int_dict[key] = 0
        else:
            int_dict[key] = int(dict[key])
    return int_dict

# def levels_calc(dict, player):
#     refresh_player = player.copy()

#     for key in player:
#         if player[key] <= hero_dict[key]:
#             player[key] = hero_dict[key]
#     dict["Hero"] = sum(player.values()) - sum(hero_dict.values()) + hero_dict["level"]
#     for key in player:
#         player[key] = refresh_player[key]

#     for key in player:
#         if player[key] <= bandit_dict[key]:
#             player[key] = bandit_dict[key]
#     dict["Bandit"] = sum(player.values()) - sum(bandit_dict.values()) + bandit_dict["level"]
#     for key in player:
#         player[key] = refresh_player[key]

#     for key in player:
#         if player[key] <= astrologer_dict[key]:
#             player[key] = astrologer_dict[key]
#     dict["Astrologer"] = sum(player.values()) - sum(astrologer_dict.values()) + astrologer_dict["level"]
#     for key in player:
#         player[key] = refresh_player[key]

#     for key in player:
#         if player[key] <= warrior_dict[key]:
#             player[key] = warrior_dict[key]
#     dict["Warrior"] = sum(player.values()) - sum(warrior_dict.values()) + warrior_dict["level"]
#     for key in player:
#         player[key] = refresh_player[key]

#     for key in player:
#         if player[key] <= prisoner_dict[key]:
#             player[key] = prisoner_dict[key]
#     dict["Prisoner"] = sum(player.values()) - sum(prisoner_dict.values()) + prisoner_dict["level"]
#     for key in player:
#         player[key] = refresh_player[key]

#     for key in player:
#         if player[key] <= confessor_dict[key]:
#             player[key] = confessor_dict[key]
#     dict["Confessor"] = sum(player.values()) - sum(confessor_dict.values()) + confessor_dict["level"]
#     for key in player:
#         player[key] = refresh_player[key]

#     for key in player:
#         if player[key] <= wretch_dict[key]:
#             player[key] = wretch_dict[key]
#     dict["Wretch"] = sum(player.values()) - sum(wretch_dict.values()) + wretch_dict["level"]
#     for key in player:
#         player[key] = refresh_player[key]

#     for key in player:
#         if player[key] <= vagabond_dict[key]:
#             player[key] = vagabond_dict[key]
#     dict["Vagabond"] = sum(player.values()) - sum(vagabond_dict.values()) + vagabond_dict["level"]
#     for key in player:
#         player[key] = refresh_player[key]

#     for key in player:
#         if player[key] <= prophet_dict[key]:
#             player[key] = prophet_dict[key]
#     dict["Prophet"] = sum(player.values()) - sum(prophet_dict.values()) + prophet_dict["level"]
#     for key in player:
#         player[key] = refresh_player[key]

#     for key in player:
#         if player[key] <= samurai_dict[key]:
#             player[key] = samurai_dict[key]
#     dict["Samurai"] = sum(player.values()) - sum(samurai_dict.values()) + samurai_dict["level"]
#     return dict


# if __name__ == '__main__':
    #player_dict = get_stats(player_dict)
    #levels_dict = levels_calc(levels_dict, player_dict)
    #for key, value in sorted(levels_dict.items(), key=lambda x: x[1]):
        #print(value, ": ", key)
    
