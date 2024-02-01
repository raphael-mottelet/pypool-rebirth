import sys
sys.path.append("..") #cette ligne nous permet de faire des imports en dehors du repertoire
from game_character.gamecharacter import Character

def initialize_player(animation_list, idle_animation_list):
    return Character(90, 190, animation_list, idle_animation_list)

#ce fichier avait pour but inital de set aléatoirement par la suite la position du joueur aléatoirement sur différents niveaux (tant que le joueur apparait sur un 0 (un passage))