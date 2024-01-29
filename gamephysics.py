def is_collision(tile_map, x, y, width, height):
    """
    Vérifie s'il y a une collision à la nouvelle position du personnage. Le code est par contre à revoir, il y a de gros bug de colision 

    Parametres:
    - tile_map: instance de la classe TileMap
    - x, y: nouvelles coordonnées du coin supérieur gauche du personnage
    - width, height: largeur et hauteur du personnage

    Retourne:
    - True s'il y a collision, False sinon
    """
    # Convertis les coordonnées en indices de tuile
    tile_x = int(x / tile_map.tile_size)
    tile_y = int(y / tile_map.tile_size)

    # Vérifie les collisions avec les murs
    for row in range(tile_y, int((y + height) / tile_map.tile_size) + 1):
        for col in range(tile_x, int((x + width) / tile_map.tile_size) + 1):
            if tile_map.is_wall(col, row):
                print(f"Collision with wall at ({col}, {row})")  #Ligne pour le débogage, affiche les collisions dans le terminal
                return True  # Collision avec un mur

    return False  # Pas de collision


"""code qui fait traverser les murs mais gere un peut les colisions
    for row in range(tile_y, int((y + height) / tile_map.tile_size)):
            for col in range(tile_x, int((x + width) / tile_map.tile_size)):
                if tile_map.is_wall(col, row):
                    print(f"Collision with wall at ({col}, {row})")  #Ligne pour le débogage
                    return True  # Collision avec un mur

    return False  # Pas de collision
"""
