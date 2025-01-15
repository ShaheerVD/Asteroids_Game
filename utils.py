<<<<<<< HEAD
from pygame.image import load
from pathlib import Path

def load_sprite(name,with_alpha=True):
    filename = Path(__file__).parent / Path("assets/sprites/"+name+ ".png")
    sprite = load(filename.resolve())

    if with_alpha:
        return sprite.convert_alpha()
    
=======
from pygame.image import load
from pathlib import Path

def load_sprite(name,with_alpha=True):
    filename = Path(__file__).parent / Path("assets/sprites/"+name+ ".png")
    sprite = load(filename.resolve())

    if with_alpha:
        return sprite.convert_alpha()
    
>>>>>>> a54774c (add models and sprites)
    return sprite.convert()