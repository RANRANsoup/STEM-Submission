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
        self.max_splitting = 10  # Maximum number of small spheres for splitting effect
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

                # Calculate the number of small spheres for the splitting effect
                # The closer the sphere is to the mouse, the more small spheres there are
                num_balls = int(self.max_splitting * (1 - distance_from_mouse / dot.width))
                num_balls = max(1, num_balls)  # Ensure there is at least one small sphere

                # Calculate the offset for the small spheres
                angle_step = 2 * np.pi / num_balls
                for i in range(num_balls):
                    # Calculate the offset position for each small sphere
                    angle = i * angle_step
                    offset_x = np.cos(angle) * radius * 0.6  # Offset based on angle
                    offset_y = np.sin(angle) * radius * 0.6
                    new_x = x + int(offset_x)
                    new_y = y + int(offset_y)

                    # Calculate the radius of the small spheres
                    ball_radius = int(radius / num_balls)  # Radius for each small sphere

                    # Draw the small sphere
                    circle(layer, (new_x, new_y), ball_radius, color, -1)

        dot.draw_layer(layer)

MySketch()
