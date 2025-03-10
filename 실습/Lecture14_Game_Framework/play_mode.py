from pico2d import *

import game_framework
import game_world
import item_mode
import title_mode
from grass import Grass
from boy import Boy


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(title_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            game_framework.push_mode(item_mode)
        else:
            boy.handle_event(event)


def init():
    global boy

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)


def update():
    game_world.update()


def draw():
    clear_canvas()
    game_world.render()
    update_canvas()


def finish():
    game_world.clear()

def pause():
    pass
def resume():
    pass