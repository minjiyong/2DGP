from pico2d import*
import math

open_canvas()

grass = load_image('grass.png')
boy = load_image('character.png')

def draw_boy(x, y):
        clear_canvas_now()
        boy.draw_now(x, y)
        delay(0.05)

def run_circle():
        print('CIRCLE')

        r, cx, cy = 300, 800 // 2, 600 // 2
        
        for degree in range(0, 360, 3):
                theta = math.radians(degree)
                x = r * math.cos(theta) + cx
                y = r * math.sin(theta) + cy

                draw_boy(x, y)

def run_top():
        print('TOP')
        for x in range(0, 750, 10):
                draw_boy(x, 550)
        pass

def run_right():
        print('RIGHT')
        for y in range(550, 0, -10):
                draw_boy(750, y)
        pass

def run_down():
        print('DOWN')
        for x in range(750, 0, -10):
                draw_boy(x, 0)
        pass

def run_left():
        print('LEFT')
        for y in range(0, 550, 10):
                draw_boy(0, y)
        pass
        

def run_rectangle():
        print('RECTANGLE')
        run_top()
        run_right()
        run_down()
        run_left()

def run_left_to_top():
        print('LEFT TO TOP')
        for i in range(0, 400, 10):
                draw_boy(i, i)

def run_top_to_right():
        print('TOP TO RIGHT')
        j = 400
        for i in range(400, 800, 10):
                j = j - 10
                draw_boy(i, j)
        pass

def run_right_to_left():
        print('RIGHT TO LEFT')
        for i in range(800, 0, -10):
                draw_boy(i, 0)
        pass

def run_triangle():
        print('TRIANGLE')
        run_left_to_top()
        run_top_to_right()
        run_right_to_left()
        pass


while(True):
        run_circle()
        run_rectangle()
        run_triangle()


close_canvas()
