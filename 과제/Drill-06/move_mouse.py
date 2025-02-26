from pico2d import *
import random
import time

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)

TUK_ground = load_image('TUK_GROUND_FULL.png')
character = load_image('animation_sheet.png')
hand = load_image('hand_arrow.png')


def lerp(start, end, t):
    return start + t * (end - start)


def handle_events():
    global running
    global x, y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
    pass



running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
t = 0.005
frame = 0
mouse_x = random.randint(0, TUK_WIDTH)
mouse_y = random.randint(0, TUK_HEIGHT)
hide_cursor()

while running:
    clear_canvas()
    TUK_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    hand.draw(mouse_x, mouse_y)
    if mouse_x > x:
        character.clip_draw(frame * 100, 100, 100, 100, x, y)
    elif mouse_x < x:
        character.clip_composite_draw(frame * 100, 100, 100, 100, 0, 'h', x, y, 100, 100)
    update_canvas()

    frame = (frame + 1) % 8
    x = lerp(x, mouse_x, t)
    y = lerp(y, mouse_y, t)

    if abs(x - mouse_x) < 2 and abs(y - mouse_y) < 2:
        mouse_x = random.randint(0, TUK_WIDTH)
        mouse_y = random.randint(0, TUK_HEIGHT)

    handle_events()

close_canvas()




