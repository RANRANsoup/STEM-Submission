from dorothy import Dorothy
from cv2 import circle
import numpy as np

dot = Dorothy()

class MySketch:
    
    def __init__(self):
        # Initialize the class and start the drawing loop
        dot.start_loop(self.setup, self.draw)
        
    def setup(self):
        # Load the audio file
        file_path = "week5/audio/drums.wav"
        dot.music.start_file_stream(file_path, fft_size=512, buffer_size=512)
        
        # Initialize beat display parameter for background flashing
        self.show_beat = 0
        
        # Initialize ball cluster parameters
        self.num_clusters = 80  # Number of clusters
        self.num_balls_per_cluster = 50  # Number of balls per cluster
        self.x = np.random.randint(0, dot.width, self.num_clusters)  # Randomly initialize x-coordinates
        self.y = np.random.randint(0, dot.height, self.num_clusters)  # Randomly initialize y-coordinates
        self.speed_y = np.random.uniform(0.5, 2, self.num_clusters)  # Vertical drift speed
        self.speed_x = np.random.uniform(-1, 1, self.num_clusters)  # Horizontal drift speed

    def draw(self):
        # Set background color
        col = dot.black
        if dot.music.is_beat():  # Detect a beat
            self.show_beat = 10  # Duration of flash
        
        if self.show_beat > 0:
            col = dot.white  # Change background to white on a beat
        
        dot.background(col)
        self.show_beat -= 1  # Decrease beat counter
        
        # Get FFT data
        fft_data = dot.music.fft()[:self.num_clusters]
        
        # Grayscale gradient list
        color_palette = [
            (50, 50, 50),   # Dark gray
            (100, 100, 100),  # Medium gray
            (150, 150, 150),  # Light gray
            (200, 200, 200),  # Lighter gray
            (255, 255, 255),  # Pure white
        ]

        # Draw ball clusters
        for i in range(self.num_clusters):
            # Adjust spread effect based on FFT data
            size_factor = int(fft_data[i])  # Adjust ball size
            expansion_factor = 1 + fft_data[i] * 8  # Control spread intensity

            # Ball cluster center coordinates
            center_x, center_y = self.x[i], self.y[i]
            
            # Draw each ball
            for j in range(self.num_balls_per_cluster):
                # Calculate ball offsets
                offset_x = np.cos(2 * np.pi * j / self.num_balls_per_cluster) * size_factor * expansion_factor
                offset_y = np.sin(2 * np.pi * j / self.num_balls_per_cluster) * size_factor * expansion_factor
                ball_x = center_x + offset_x
                ball_y = center_y + offset_y
                
                # Determine the layer of the ball to assign color
                layer_index = int(j / (self.num_balls_per_cluster / len(color_palette)))
                color = color_palette[layer_index]  # Choose color based on layer
                
                # Draw the ball
                circle(dot.canvas, (int(ball_x), int(ball_y)), 1, color, -1)
            
            # Update ball cluster position with slow drifting
            self.x[i] = (self.x[i] + self.speed_x[i]) % dot.width
            self.y[i] = (self.y[i] + self.speed_y[i]) % dot.height


MySketch()

