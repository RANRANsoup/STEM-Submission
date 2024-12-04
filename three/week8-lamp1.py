from cv2 import circle
from dorothy import Dorothy
import numpy as np

dot = Dorothy()

class MySketch:
    def __init__(self):
        dot.start_loop(self.setup, self.draw)

    def setup(self):
        self.grid_size = 8  # Grid size
        self.cell_size = dot.width // self.grid_size  # Size of each grid cell
        self.max_radius = 80  # Maximum radius of the sphere
        self.min_radius = 20  # Minimum radius of the sphere
        print("setup")

    def draw(self):
        # Get the current canvas
        layer = dot.get_layer()

        # Iterate through each cell in the grid
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                # Calculate the initial center position of the sphere
                x = col * self.cell_size + self.cell_size // 2
                y = row * self.cell_size + self.cell_size // 2

                # Calculate the distance between the sphere and the mouse
                distance_from_mouse = np.sqrt((x - dot.mouse_x) ** 2 + (y - dot.mouse_y) ** 2)

                # Calculate the radius of the sphere based on the mouse position
                radius = self.max_radius - (distance_from_mouse / 4)
                radius = max(self.min_radius, radius)  # Limit the minimum radius

                # Calculate the color of the sphere based on the distance between the mouse and the sphere
                color_factor = 1 - (distance_from_mouse / dot.width)
                color_factor = max(0, min(1, color_factor))  # Keep it between 0 and 1
                color = (int(255 * color_factor), int(255 * (1 - color_factor)), int(255 * (color_factor ** 2)))

                # Calculate the compression level of the sphere
                scale_x = 1 + 0.5 * (x - dot.mouse_x) / dot.width  # Horizontal scaling
                scale_y = 1 + 0.5 * (y - dot.mouse_y) / dot.height  # Vertical scaling

                # Limit the scaling ratio to prevent excessive stretching
                scale_x = max(0.5, min(1.5, scale_x))
                scale_y = max(0.5, min(1.5, scale_y))

                # Calculate the width and height after deformation
                width = int(radius * scale_x)
                height = int(radius * scale_y)

                # Draw the "compressed" sphere
                center = (x, y)
                circle(layer, center, max(width, height), color, -1)

        dot.draw_layer(layer)

MySketch()
