def sauvegarde_argent(name, player_data):
    file_name = name + "_money.txt"
    with open(file_name, 'w') as current:
        current.write(player_data)


# def sauvegarde_monster(name, monster_data):
#     file_name = name + "_money.txt"
#     with open(file_name, 'w') as current:
#         current.write(monter_data)


# def sauvegarde_inv(name, inv_data):
#     file_name = name + "_money.txt"
#     with open(file_name, 'w') as current:
#         current.write(inv_data)