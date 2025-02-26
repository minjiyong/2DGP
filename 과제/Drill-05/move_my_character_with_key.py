from tabnanny import check

from pico2d import *


open_canvas()
background = load_image('TUK_GROUND.png')
character = load_image('character_remove.png')


def handle_events():
    global running, dir_ud, dir_lr

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_lr += 1
            elif event.key == SDLK_LEFT:
                dir_lr -= 1
            elif event.key == SDLK_UP:
                dir_ud += 1
            elif event.key == SDLK_DOWN:
                dir_ud -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_lr -= 1
            elif event.key == SDLK_LEFT:
                dir_lr += 1
            elif event.key == SDLK_UP:
                dir_ud -= 1
            elif event.key == SDLK_DOWN:
                dir_ud += 1


def check_border():
    global x, y
    if x - 35 <= 0 or x + 35 >= 800:
        x -= dir_lr * 10
    if y - 35 <= 0 or y + 35 >= 600:
        y -= dir_ud * 10


running = True
x = 800 // 2
y = 600 // 2
frame = 0
frame_idle = 0
dir_ud = 0
dir_lr = 0

while running:
    clear_canvas()
    background.clip_draw(0, 0, 1280, 1024, 400, 300, 800, 600)

    if dir_lr == -1:
        character.clip_draw(43 + frame * 86, 180, 30, 40, x, y, 70, 70)
    elif dir_lr == 1:
        character.clip_draw(43 + frame * 86, 110, 30, 40, x, y, 70, 70)
    elif dir_ud == -1:
        character.clip_draw(43 + frame * 86, 250, 30, 40, x, y, 70, 70)
    elif dir_ud == 1:
        character.clip_draw(43 + frame * 86, 40, 30, 40, x, y, 70, 70)
    elif dir_lr == 0 and dir_ud == 0:
        character.clip_draw(41 + frame_idle * 48, 585, 33, 40, x, y, 70, 70)

    update_canvas()
    handle_events()
    frame = (frame + 1) % 6
    frame_idle = (frame_idle + 1) % 10
    x += dir_lr * 10
    y += dir_ud * 10
    check_border()
    delay(0.05)


close_canvas()

