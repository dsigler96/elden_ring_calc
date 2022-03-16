from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

hero_dict = {
    "level" : 7,
    "vig" : 14,
    "mind" : 9,
    "end" : 12,
    "str" : 16,
    "dex" : 9,
    "int" : 7,
    "faith" : 8,
    "arc" : 11
}

bandit_dict = {
    "level" : 5,
    "vig" : 10,
    "mind" : 11,
    "end" : 10,
    "str" : 9,
    "dex" : 13,
    "int" : 9,
    "faith" : 8,
    "arc" : 14
}

astrologer_dict = {
    "level" : 6,
    "vig" : 9,
    "mind" : 15,
    "end" : 9,
    "str" : 8,
    "dex" : 12,
    "int" : 16,
    "faith" : 7,
    "arc" : 9
}

warrior_dict = {
    "level" : 8,
    "vig" : 11,
    "mind" : 12,
    "end" : 11,
    "str" : 10,
    "dex" : 16,
    "int" : 10,
    "faith" : 8,
    "arc" : 9
}

prisoner_dict = {
    "level" : 9,
    "vig" : 11,
    "mind" : 12,
    "end" : 11,
    "str" : 11,
    "dex" : 14,
    "int" : 14,
    "faith" : 6,
    "arc" : 9
}

confessor_dict = {
    "level" : 10,
    "vig" : 10,
    "mind" : 13,
    "end" : 10,
    "str" : 12,
    "dex" : 12,
    "int" : 9,
    "faith" : 14,
    "arc" : 9
}

wretch_dict = {
    "level" : 1,
    "vig" : 10,
    "mind" : 10,
    "end" : 10,
    "str" : 10,
    "dex" : 10,
    "int" : 10,
    "faith" : 10,
    "arc" : 10
}

vagabond_dict = {
    "level" : 9,
    "vig" : 15,
    "mind" : 10,
    "end" : 11,
    "str" : 14,
    "dex" : 13,
    "int" : 9,
    "faith" : 9,
    "arc" : 7
}

prophet_dict = {
    "level" : 7,
    "vig" : 10,
    "mind" : 14,
    "end" : 8,
    "str" : 11,
    "dex" : 10,
    "int" : 7,
    "faith" : 16,
    "arc" : 10
}

samurai_dict = {
    "level" : 9,
    "vig" : 12,
    "mind" : 11,
    "end" : 13,
    "str" : 12,
    "dex" : 15,
    "int" : 9,
    "faith" : 8,
    "arc" : 8
}

player_dict = {
    "level" : 0,
    "vig" : 0,
    "mind" : 0,
    "end" : 0,
    "str" : 0,
    "dex" : 0,
    "int" : 0,
    "faith" : 0,
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

def levels_calc(dict, player):
    refresh_player = player.copy()

    for key in player:
        if player[key] <= hero_dict[key]:
            player[key] = hero_dict[key]
    dict["Hero"] = sum(player.values()) - sum(hero_dict.values()) + hero_dict["level"]
    for key in player:
        player[key] = refresh_player[key]

    for key in player:
        if player[key] <= bandit_dict[key]:
            player[key] = bandit_dict[key]
    dict["Bandit"] = sum(player.values()) - sum(bandit_dict.values()) + bandit_dict["level"]
    for key in player:
        player[key] = refresh_player[key]

    for key in player:
        if player[key] <= astrologer_dict[key]:
            player[key] = astrologer_dict[key]
    dict["Astrologer"] = sum(player.values()) - sum(astrologer_dict.values()) + astrologer_dict["level"]
    for key in player:
        player[key] = refresh_player[key]

    for key in player:
        if player[key] <= warrior_dict[key]:
            player[key] = warrior_dict[key]
    dict["Warrior"] = sum(player.values()) - sum(warrior_dict.values()) + warrior_dict["level"]
    for key in player:
        player[key] = refresh_player[key]

    for key in player:
        if player[key] <= prisoner_dict[key]:
            player[key] = prisoner_dict[key]
    dict["Prisoner"] = sum(player.values()) - sum(prisoner_dict.values()) + prisoner_dict["level"]
    for key in player:
        player[key] = refresh_player[key]

    for key in player:
        if player[key] <= confessor_dict[key]:
            player[key] = confessor_dict[key]
    dict["Confessor"] = sum(player.values()) - sum(confessor_dict.values()) + confessor_dict["level"]
    for key in player:
        player[key] = refresh_player[key]

    for key in player:
        if player[key] <= wretch_dict[key]:
            player[key] = wretch_dict[key]
    dict["Wretch"] = sum(player.values()) - sum(wretch_dict.values()) + wretch_dict["level"]
    for key in player:
        player[key] = refresh_player[key]

    for key in player:
        if player[key] <= vagabond_dict[key]:
            player[key] = vagabond_dict[key]
    dict["Vagabond"] = sum(player.values()) - sum(vagabond_dict.values()) + vagabond_dict["level"]
    for key in player:
        player[key] = refresh_player[key]

    for key in player:
        if player[key] <= prophet_dict[key]:
            player[key] = prophet_dict[key]
    dict["Prophet"] = sum(player.values()) - sum(prophet_dict.values()) + prophet_dict["level"]
    for key in player:
        player[key] = refresh_player[key]

    for key in player:
        if player[key] <= samurai_dict[key]:
            player[key] = samurai_dict[key]
    dict["Samurai"] = sum(player.values()) - sum(samurai_dict.values()) + samurai_dict["level"]
    return dict

def clicked():
    print("You clicked it!")

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(475, 250, 960, 540)
    win.setWindowTitle("Elden Ring PvP Optimizer")

    label = QtWidgets.QLabel(win)
    label.setText("Stats")
    label.move(20, 20)

    b1 = QtWidgets.QPushButton(win)
    b1.setText("Don't click me")
    b1.clicked.connect(clicked)

    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    #player_dict = get_stats(player_dict)
    #levels_dict = levels_calc(levels_dict, player_dict)
    #for key, value in sorted(levels_dict.items(), key=lambda x: x[1]):
        #print(value, ": ", key)
    window()
    window.title("Elden Ring PvP Optimizer")
