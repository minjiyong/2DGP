from pico2d import open_canvas, delay, close_canvas
import logo_mode as start_mode
import game_framework

# 게임 기본 구조
open_canvas()
game_framework.run(start_mode)
close_canvas()