from dorothy import Dorothy
from cv2 import circle, rectangle
import numpy as np


dot = Dorothy()
class MySketch:
    
    def __init__(self):
        dot.start_loop(self.setup, self.draw)
        
    def setup(self):
        # Load the audio file
        file_path = "/Users/wuxinran/Desktop/Git/STEM-4-Creatives-24-25/week5/Lorraine.WAV"
        dot.music.start_file_stream(file_path, fft_size=512, buffer_size=512)
        
        # Initialize stars
        self.num_stars = 100  # Number of stars
        self.x = np.random.randint(0, dot.width, self.num_stars)
        self.y = np.random.randint(0, dot.height, self.num_stars)
        self.speed_y = np.random.uniform(0.5, 2, self.num_stars)  # Slow falling speed
        self.speed_x = np.random.uniform(-1, 1, self.num_stars)  # Slow drifting speed
        self.colors = [255 for _ in range(self.num_stars)]  # Initial color set to white

    def draw(self):
        # Set the background color
        dot.background(dot.black)
        
        # Get FFT data
        fft_data = dot.music.fft()[:self.num_stars]
        
        # Draw and update stars
        for i in range(self.num_stars):
            # Adjust star size and color based on FFT data
            size = int(fft_data[i])  # Star size amplitude
            intensity = int(fft_data[i] * 10)  # Soft color change
            self.colors[i] = (intensity, intensity, 255)  # Cool tone color change
            
            # Draw the star
            circle(dot.canvas, (self.x[i], self.y[i]), size, self.colors[i], -1)
            
            # Update star position, slow drift
            self.x[i] = (self.x[i] + self.speed_x[i]) % dot.width
            self.y[i] = (self.y[i] + self.speed_y[i]) % dot.height
        
        # Add a transparent layer for trailing effect
        cover = dot.get_layer()
        rectangle(cover, (0, 0), (dot.width, dot.height), dot.darkblue, -1)
        dot.draw_layer(cover, 0.2)  # Adjust opacity to make the effect softer

MySketch()


