# 이것은 각 상태들을 객체로 구현한 것임.

from pico2d import get_time, load_image, SDL_KEYDOWN, SDL_KEYUP, SDLK_SPACE, SDLK_LEFT, SDLK_RIGHT, load_font
from state_machine import *
from ball import Ball
import game_world
import game_framework


PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 60.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.1
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5


class AutoRun:
    @staticmethod
    def enter(boy, e):
        if boy.face_dir == 1:
            boy.action = 1
            boy.dir = 1
        elif boy.face_dir == -1:
            boy.action = 0
            boy.dir = -1
        boy.frame = 0
        boy.start_time = get_time()
        pass
    @staticmethod
    def exit(boy, e):
        pass
    @staticmethod
    def do(boy):
        boy.frame = (boy.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5
        boy.x += boy.dir * RUN_SPEED_PPS * game_framework.frame_time
        if boy.x < 0:
            boy.face_dir = 1
            boy.action = 1
            boy.dir = 1
        elif boy.x > 9999:
            boy.face_dir = -1
            boy.action = 0
            boy.dir = -1

        if get_time() - boy.start_time > 5:
            boy.state_machine.add_event(('TIME_OUT', 0))
        pass
    @staticmethod
    def draw(boy):
        if boy.face_dir == 1:
            boy.image.clip_draw(int(boy.frame) * 182, 334, 182, 170, boy.x, boy.y)
        elif boy.face_dir == -1:
            boy.image.clip_composite_draw(int(boy.frame) * 182, 334, 182, 170, 0, 'h', boy.x, boy.y, 182, 170)


class Bird:

    def __init__(self):
        self.x, self.y = 400, 400
        self.face_dir = 1
        self.image = load_image('bird_animation.png')
        self.state_machine = StateMachine(self)
        self.state_machine.start(AutoRun)
        self.state_machine.set_transitions(
            {
                #Idle: {right_down: Run, left_down: Run, left_up: Run, right_up: Run, space_down: Idle},
                #Run: {right_down: Idle, left_down: Idle, right_up: Idle, left_up: Idle, space_down: Run},
            }
        )
        self.font = load_font('ENCR10B.TTF', 16)

    def update(self):
        self.state_machine.update()

    def handle_event(self, event):
        # 여기서 받을 수 있는 것만 걸러야 함. right left  등등..
        self.state_machine.add_event(('INPUT', event))
        pass

    def draw(self):
        self.state_machine.draw()
        self.font.draw(self.x - 60, self.y + 50, f'(Time: {get_time():.2f})', (255, 255, 0))

    def fire_ball(self):
        ball = Ball(self.x, self.y, self.face_dir * 10)
        game_world.add_object(ball)