from pico2d import*

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

check = 0

x = 0;
y = 90;

while(True):
        if y == 90:
            while(x < 800):
                clear_canvas_now()
                grass.draw_now(400, 30)
                character.draw_now(x, 90)
                x= x + 5
                delay(0.01)
        if x == 800:
            while(y < 600):
                clear_canvas_now()
                grass.draw_now(400, 30)
                character.draw_now(800, y)
                y= y + 5
                delay(0.01)
        if y == 600:
            while(x > 0):
                clear_canvas_now()
                grass.draw_now(400, 30)
                character.draw_now(x, 600)
                x= x - 5
                delay(0.01)
        if x == 0:
            while(y > 0):
                clear_canvas_now()
                grass.draw_now(400, 30)
                character.draw_now(0, y)
                y= y - 5
                delay(0.01)


        x = 0;
        y = 90
        


close_canvas()
