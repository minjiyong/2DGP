from pico2d import load_image, clear_canvas, get_events, update_canvas
from sdl2 import SDLK_ESCAPE, SDL_QUIT, SDL_KEYDOWN, SDLK_SPACE

import game_framework
import logo_mode
import play_mode


def init():
    global image
    image = load_image('title.png')

def finish():
    global image
    del image

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_mode(logo_mode)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.change_mode(play_mode)

def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def update():
    pass

def pause():
    pass
def resume():
    pass