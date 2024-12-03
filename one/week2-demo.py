from dorothy import Dorothy
import numpy as np

dot = Dorothy()

class MySketch:

    def __init__(self):
        dot.start_loop(self.setup, self.draw)

    def setup(self):
        print("setup")

    def draw(self):
        # Set the background color
        dot.background((30, 30, 30))  # Dark gray background
        size = 60  # Side length of the square
        border = 20  # Grid spacing
        grid = 6  # Number of rows and columns in the grid

        # Create the canvas
        canvas = dot.get_layer()

        # Calculate the transition for corner radius
        max_radius = size // 2  # Maximum corner radius (fully rounded into a circle)
        radius = int((dot.mouse_x / dot.width) * max_radius)

        for i in range(grid):
            for j in range(grid):
                # Calculate the center point of each square
                x = i * (size + border) + size // 2
                y = j * (size + border) + size // 2

                # Color variation: transition to brighter colors
                brightness = int((dot.mouse_y / dot.height) * 255)
                color = (brightness, 120, 200)  # RGB color format

                # Draw the shape
                self.draw_shape(canvas, (x, y), size, radius, color)

        # Render the canvas content to the window
        dot.draw_layer(canvas)

    def draw_shape(self, canvas, center, size, radius, color):
        x, y = center
        if radius == 0:
            # Draw a square
            x1, y1 = x - size // 2, y - size // 2
            x2, y2 = x + size // 2, y + size // 2
            canvas[y1:y2, x1:x2] = color
        else:
            # Draw a rounded rectangle approximating a circle
            for i in range(-size // 2, size // 2):
                for j in range(-size // 2, size // 2):
                    distance = np.sqrt(i**2 + j**2)
                    if distance <= size // 2 - radius or (distance <= size // 2 and distance > size // 2 - radius):
                        canvas[y + j, x + i] = color

MySketch()
