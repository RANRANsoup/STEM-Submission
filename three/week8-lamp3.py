from cv2 import circle, ellipse
from dorothy import Dorothy
import numpy as np

# Initialize the Dorothy object to manage the graphical environment
dot = Dorothy()

class MySketch:
    def __init__(self):
        # Start the animation loop, passing setup and draw functions
        dot.start_loop(self.setup, self.draw)

    def setup(self):
        # Set initial values and configurations
        self.grid_size = 20  # Grid size (number of rows and columns)
        self.cell_size = dot.width // self.grid_size  # Calculate the size of each grid cell based on the canvas width
        self.max_radius = 40  # Maximum radius of the spheres
        self.min_radius = 10  # Minimum radius of the spheres
        self.color_shift = 0  # Initial color change value for dynamic color effect

    def draw(self):
        # Get the current layer of the canvas
        layer = dot.get_layer()

        # Update the color change value to achieve a dynamic color effect
        self.color_shift += 0.1
        if self.color_shift > 255:  # Reset the color change value if it exceeds 255
            self.color_shift = 0

        # Iterate over the grid, drawing a sphere at each grid position
        for row in range(self.grid_size):
            for col in range(self.grid_size):
                # Calculate the center of the sphere based on grid position
                x = col * self.cell_size + self.cell_size // 2
                y = row * self.cell_size + self.cell_size // 2

                # Calculate the distance between the sphere center and the mouse position
                distance_from_mouse = np.sqrt((x - dot.mouse_x) ** 2 + (y - dot.mouse_y) ** 2)

                # Calculate the radius of the sphere based on the mouse distance
                radius = self.max_radius - (distance_from_mouse / 4)
                radius = max(self.min_radius, radius)  # Limit the radius to avoid spheres disappearing

                # Calculate the color change factor based on the mouse distance
                color_factor = 1 - (distance_from_mouse / dot.width)
                color_factor = max(0, min(1, color_factor))  # Limit the color factor between 0 and 1
                color = (int(255 * color_factor), int(255 * (1 - color_factor)), int(255 * (color_factor * 255)))

                # Add dynamic color changes to the calculated color
                r = (int(color[0] + self.color_shift) % 250)
                g = (int(color[1] + self.color_shift) % 250)
                b = (int(color[2] + self.color_shift) % 250)
                dynamic_color = (r, g, b)

                # Calculate the "compression" level of the sphere based on horizontal and vertical distance from the mouse
                scale_x = 1 + 0.5 * (x - dot.mouse_x) / dot.width  # Scale based on horizontal distance
                scale_y = 1 + 0.5 * (y - dot.mouse_y) / dot.height  # Scale based on vertical distance

                # Limit the scaling ratio to avoid excessive stretching
                scale_x = max(0.5, min(1.5, scale_x))
                scale_y = max(0.5, min(1.5, scale_y))

                # Calculate the scaled width and height
                width = int(radius * scale_x)
                height = int(radius * scale_y)

                # Draw the "compressed" sphere (ellipse) using the calculated size and color
                center = (x, y)
                circle(layer, center, width, dynamic_color, -1)

                # Add a dynamic glowing effect to the sphere using an ellipse
                ellipse_center = (x + int(np.sin(self.color_shift) * 20), y + int(np.cos(self.color_shift) * 20))
                ellipse(layer, ellipse_center, (width + 10, height + 10), 0, 0, 360, (255, 255, 255), 1)

        dot.draw_layer(layer)

MySketch()


