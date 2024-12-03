from dorothy import Dorothy 
from cv2 import circle, line

dot = Dorothy() 

class MySketch:
    def __init__(self):
        dot.start_loop(self.setup, self.draw)

    def setup(self):
        print("setup")
        dot.music.start_file_stream("week2/audio/海绵宝宝.WAV")

    def draw(self):
        dot.background((182,182,182))
        print(dot.music.amplitude())
        x = dot.mouse_x
        y = dot.mouse_y

        # Calculate the transition radius based on mouse_x for shape transformation
        max_radius = dot.width // 15
        transition_radius = int((x / dot.width) * max_radius)  # Transition from circle to square

        # Static circles (like your original circles)
        n = (154, 139, 10)
        for i in range(6):
            for j in range(5):
                cx = i * max_radius * 3
                cy = j * max_radius * 3
                if x > dot.width / 2:
                    # Draw square if mouse is in the right half of the canvas
                    self.draw_square(dot.canvas, (cx, cy), max_radius * 2, n)  # Larger square
                else:
                    # Draw circle if mouse is in the left half of the canvas
                    circle(dot.canvas, (cx, cy), max_radius, n, -1)
        
        # Dynamic circles (changing based on music amplitude)
        if dot.music.amplitude() > 0.01:
            m = (251,243,95)
            for i in range(6):
                for j in range(5):
                    cx = i * max_radius * 3
                    cy = j * max_radius * 3
                    if x > dot.width / 2:
                        # Draw square if mouse is in the right half of the canvas
                        self.draw_square(dot.canvas, (cx + 20, cy + 20), max_radius * 2, m)  # Larger square
                    else:
                        # Draw circle if mouse is in the left half of the canvas
                        circle(dot.canvas, (cx + 20, cy + 20), max_radius, m, -1)

        # Mouse eye drawing (left and right)
        radius = 10
        line(dot.canvas, (x - radius, y - radius), (x - radius, y - radius - radius * 2 * 2 * 2 - 20), dot.black, 6)
        line(dot.canvas, (x - radius, y - radius), (x - radius + 30, y - radius - radius * 2 * 2 * 2 - 20 + 3), dot.black, 6)
        line(dot.canvas, (x - radius, y - radius), (x - radius - 30, y - radius - radius * 2 * 2 * 2 - 20 + 3), dot.black, 6)

        line(dot.canvas, (x + radius * 2 * 2 * 2 * 2, y - radius), (x + radius * 2 * 2 * 2 * 2, y - radius - radius * 2 * 2 * 2 - 20), dot.black, 6)
        line(dot.canvas, (x + radius * 2 * 2 * 2 * 2, y - radius), (x + radius * 2 * 2 * 2 * 2 + 30, y - radius - radius * 2 * 2 * 2 - 20 + 3), dot.black, 6)
        line(dot.canvas, (x + radius * 2 * 2 * 2 * 2, y - radius), (x + radius * 2 * 2 * 2 * 2 - 30, y - radius - radius * 2 * 2 * 2 - 20 + 3), dot.black, 6)

        # Mouse eye (left and right)
        circle(dot.canvas, (x - radius, y - radius), radius * 2 * 2 * 2, dot.lavender, -1)
        circle(dot.canvas, (x, y), radius * 2 * 2, dot.aqua, -1)
        circle(dot.canvas, (x, y), radius * 2, dot.black, -1)

        circle(dot.canvas, (x + radius * 15, y - radius), radius * 2 * 2 * 2, dot.lavender, -1)
        circle(dot.canvas, (x + radius * 14, y), radius * 2 * 2, dot.aqua, -1)
        circle(dot.canvas, (x + radius * 14, y), radius * 2, dot.black, -1)

    def draw_square(self, canvas, center, size, color):
        """
        Draw a square with the given center, size, and color.
        :param canvas: Canvas to draw on
        :param center: Tuple of (x, y) coordinates for the square's center
        :param size: Size of the square
        :param color: RGB color to fill the square
        """
        x, y = center
        half_size = size // 2
        canvas[y - half_size:y + half_size, x - half_size:x + half_size] = color

MySketch()