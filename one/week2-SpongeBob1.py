from dorothy import Dorothy 
from cv2 import circle
from cv2 import line

dot = Dorothy() 
class MySketch:
    def __init__(self):
        dot.start_loop(self.setup, self.draw)

    def setup(self):
        print("setup")
        dot.music.start_file_stream("/Users/wuxinran/Desktop/Git/STEM-4-Creatives-24-25/week2/audio/海绵宝宝.WAV")

    def draw(self):
        dot.background((182,182,182))
        print(dot.music.amplitude())
        x = dot.mouse_x
        y = dot.mouse_y

        # Stastic circles
        radius = dot.width//15
        n=(154,139,10)
        circle(dot.canvas, (0,radius), radius, n, -1)
        circle(dot.canvas, (0,radius*4), radius, n, -1)
        circle(dot.canvas, (0,radius*7), radius, n, -1)
        circle(dot.canvas, (0,radius*10), radius, n, -1)
        # column 2
        circle(dot.canvas, (radius*3,0), radius, n, -1)
        circle(dot.canvas, (radius*3,radius*3), radius, n, -1)
        circle(dot.canvas, (radius*3,radius*6), radius, n, -1)
        circle(dot.canvas, (radius*3,radius*9), radius, n, -1)
        circle(dot.canvas, (radius*3,radius*12), radius, n, -1)
        # column 3
        circle(dot.canvas, (radius*6,radius), radius, n, -1)
        circle(dot.canvas, (radius*6,radius*4), radius, n, -1)
        circle(dot.canvas, (radius*6,radius*7), radius, n, -1)
        circle(dot.canvas, (radius*6,radius*10), radius, n, -1)
        # column 4
        circle(dot.canvas, (radius*9,0), radius, n, -1)
        circle(dot.canvas, (radius*9,radius*3), radius, n, -1)
        circle(dot.canvas, (radius*9,radius*6), radius, n, -1)
        circle(dot.canvas, (radius*9,radius*9), radius, n, -1)
        circle(dot.canvas, (radius*9,radius*12), radius, n, -1)
        # column 5
        circle(dot.canvas, (radius*12,radius), radius, n, -1)
        circle(dot.canvas, (radius*12,radius*4), radius, n, -1)
        circle(dot.canvas, (radius*12,radius*7), radius, n, -1)
        circle(dot.canvas, (radius*12,radius*10), radius, n, -1)
        # column 6
        circle(dot.canvas, (radius*15,0), radius, n, -1)
        circle(dot.canvas, (radius*15,radius*3), radius, n, -1)
        circle(dot.canvas, (radius*15,radius*6), radius, n, -1)
        circle(dot.canvas, (radius*15,radius*9), radius, n, -1)
        circle(dot.canvas, (radius*15,radius*12), radius, n, -1)
        
        
        # Moving circles
        if dot.music.amplitude() > 0.01:
            radius = dot.width//15
            m = (251,243,95)
            circle(dot.canvas, (-20,radius-20), radius, m, -1)
            circle(dot.canvas, (0-20,radius*4-20), radius, m, -1)
            circle(dot.canvas, (0-20,radius*7-20), radius,m, -1)
            circle(dot.canvas, (0-20,radius*10-20), radius, m, -1)
            # column 2
            circle(dot.canvas, (radius*3-20,0-20), radius, m, -1)
            circle(dot.canvas, (radius*3-20,radius*3-20), radius, m, -1)
            circle(dot.canvas, (radius*3-20,radius*6-20), radius, m, -1)
            circle(dot.canvas, (radius*3-20,radius*9-20), radius, m, -1)
            circle(dot.canvas, (radius*3-20,radius*12-20), radius, m, -1)
            # column 3
            circle(dot.canvas, (radius*6-20,radius-20), radius, m, -1)
            circle(dot.canvas, (radius*6-20,radius*4-20), radius, m, -1)
            circle(dot.canvas, (radius*6-20,radius*7-20), radius, m, -1)
            circle(dot.canvas, (radius*6-20,radius*10-20), radius, m, -1)
            # column 4
            circle(dot.canvas, (radius*9-20,0-20), radius, (255,255,11), -1)
            circle(dot.canvas, (radius*9-20,radius*3-20), radius, (255,255,11), -1)
            circle(dot.canvas, (radius*9-20,radius*6-20), radius, (255,255,11), -1)
            circle(dot.canvas, (radius*9-20,radius*9-20), radius, (255,255,11), -1)
            circle(dot.canvas, (radius*9-20,radius*12-20), radius, (255,255,11), -1)
            # column 5
            circle(dot.canvas, (radius*12-20,radius-20), radius, (255,255,11), -1)
            circle(dot.canvas, (radius*12-20,radius*4-20), radius, (255,255,11), -1)
            circle(dot.canvas, (radius*12-20,radius*7-20), radius, (255,255,11), -1)
            circle(dot.canvas, (radius*12-20,radius*10-20), radius, (255,255,11), -1)
            # column 6
            circle(dot.canvas, (radius*15-20,0-20), radius, (255,255,11), -1)
            circle(dot.canvas, (radius*15-20,radius*3-20), radius, (255,255,11), -1)
            circle(dot.canvas, (radius*15-20,radius*6-20), radius, (255,255,11), -1)
            circle(dot.canvas, (radius*15-20,radius*9-20), radius, (255,255,11), -1)
            circle(dot.canvas, (radius*15-20,radius*12-20), radius, (255,255,11), -1)

        # Mouse_eyelash_left
        radius = 10
        line(dot.canvas,  (x-radius,y-radius),(x-radius,y-radius-radius*2*2*2-20), dot.black, 6)
        line(dot.canvas,  (x-radius,y-radius),(x-radius+30,y-radius-radius*2*2*2-20+3), dot.black, 6)
        line(dot.canvas,  (x-radius,y-radius),(x-radius-30,y-radius-radius*2*2*2-20+3), dot.black, 6)
        # Mouse_eyelash_right
        line(dot.canvas,  (x-radius+radius*2*2*2*2,y-radius),(x-radius+radius*2*2*2*2,y-radius-radius*2*2*2-20), dot.black, 6)
        line(dot.canvas,  (x-radius+radius*2*2*2*2,y-radius),(x-radius+30+radius*2*2*2*2,y-radius-radius*2*2*2-20+3), dot.black, 6)
        line(dot.canvas,  (x-radius+radius*2*2*2*2,y-radius),(x-radius-30+radius*2*2*2*2,y-radius-radius*2*2*2-20+3), dot.black, 6)
            
            
        # Mouse_eye_left
        circle(dot.canvas, (x-radius,y-radius), radius*2*2*2, dot.lavender, -1)
        circle(dot.canvas, (x,y), radius*2*2, dot.aqua, -1)
        circle(dot.canvas, (x,y), radius*2, dot.black, -1)
        # Mouse_eye_right
        circle(dot.canvas, (x+radius*15,y-radius), radius*2*2*2, dot.lavender, -1)
        circle(dot.canvas, (x+radius*14,y), radius*2*2, dot.aqua, -1)
        circle(dot.canvas, (x+radius*14,y), radius*2, dot.black, -1)



        
MySketch() 