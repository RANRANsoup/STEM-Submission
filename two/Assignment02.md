# Week 5 Audio-Visual Balance

This week I explored how to create two different styles of visuals from audio input, I adapted the snow sketches provided in class by adding some audio responses and realising effects designed to work for soothing music and rhythmic music respectively.

My interest is in understanding the relationship between audio frequencies and visual mapping, and how parameter adjustments can create work that balances audio and visual effects.

## Reservations and changes

In the visualisation of the soothing music, I wanted to create a quiet starry night effect, in keeping with the soft, light tone.

The size of the stars changes gradually according to the frequency data.

```python
          fft_data = dot.music.fft()[:self.num_stars]
          for i in range(self.num_stars):
              size = int(fft_data[i])
              intensity = int(fft_data[i] * 10)
              self.colors[i] = (intensity, intensity, 255)
```

Creates a faint twinkling effect, like a star silently twinkling in the night sky.

```python
        self.speed_y = np.random.uniform(0.5, 2, self.num_stars)
        self.speed_x = np.random.uniform(-1, 1, self.num_stars)
```

I found that retaining the use of cooler tones better conveyed the emotion of the soothing music, while avoiding overly stimulating colour combinations and retaining a sense of harmony in the visuals.



https://github.com/user-attachments/assets/f97ed6ee-a48d-4605-b51f-86c5319e686b

[code here](https://github.com/RANRANsoup/STEM-Submission/blob/c2748d1aed6019f5486fc25c66eee9452c1aca17/two/week5-soothing%20music.py)


## Problems and challenges

The last effect was relatively simple to implement and initially worked well, but I ran into some challenges when trying to incorporate rhythmic music. Producing white flashing balls during strong tempo changes can sometimes be too jarring, especially if the tempo changes too quickly, and frequent flashing can lead to a sense of visual instability that doesn't fit with the overall visual atmosphere.


https://github.com/user-attachments/assets/4fcfc234-24a3-4708-8e86-80cdf9ca55aa


## Morphological changes

So I chose to make some changes and design an audio suitable for a strong rhythm. Firstly I achieved the diffusion effect of the blobs by calculating the offset of each blob.

```python
for j in range(self.num_balls_per_cluster):
    # Calculate ball offsets
    offset_x = np.cos(2 * np.pi * j / self.num_balls_per_cluster) * size_factor * expansion_factor
    offset_y = np.sin(2 * np.pi * j / self.num_balls_per_cluster) * size_factor * expansion_factor
    ball_x = center_x + offset_x
    ball_y = center_y + offset_y
```

When adjusting the size_factor and expansion_factor, I found that using FFT data directly may result in a range of values that are too large or too small, and it took a lot of time to adjust. Therefore, I searched and learnt online, and finally introduced expansion_factor to control the diffusion intensity, to make sure the visual effect doesn't look too cluttered and to maintain the balance of the image.

## Keep balance

To give the visuals a more layered, yet consistent feel, I used a gradient layer of black, white and grey to avoid overly abrupt colour switches. I also detected the beat via dot.music.is_beat(), where I switched background colours in short bursts to enhance the rhythmic echo.

```python
color_palette = [
    (50, 50, 50),   # Dark gray
    (100, 100, 100),  # Medium gray
    (150, 150, 150),  # Light gray
    (200, 200, 200),  # Lighter gray
    (255, 255, 255),  # Pure white
]
```

```python
layer_index = int(j / (self.num_balls_per_cluster / len(color_palette)))
color = color_palette[layer_index]
```


[code here](https://github.com/RANRANsoup/STEM-Submission/blob/e7aef9769e88444d5e675164fd6529ebac9b663e/two/week5-rhythmic.py)


https://github.com/user-attachments/assets/29485622-6285-4624-8950-be667b28c141

## Conclusion

I have significantly improved my understanding of the visualisation of different styles of music visualisation through audio input. The visual design needs to echo the qualities of the music, but it also needs to avoid a sense of instability caused by over-responsiveness. I used to think that most music visualisations looked monotonous, just long and short squares, but I now understand that it is their mission to be applicable to a wider range of scenarios.

As a next step, I plan to further explore the use of subtraction in design to enhance its coherence and aesthetics.
