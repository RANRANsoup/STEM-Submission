# Week 8 – 1 From Complexity to Simplicity

This week my research topic is exploring how interaction design can make visual elements change in interesting and dynamic ways as users interact with them through mathematical functions and animation effects.

I chose this topic for my research because I believe that dynamic feedback in design often enhances viewer immersion, and how to make this feedback more expressive through mathematical calculations is an area worth exploring. I hope to understand how to control the naturalness and precision of animation through mathematical formulas, and also explore how to balance richness and simplicity in design to avoid overly complex effects that can affect the audience's attention.

## Starting Point

At first, my goal was simple: try to use functions to make the size, shape and colour of the ball change with the distance of the mouse.

```python
radius = self.max_radius - (distance_from_mouse / 4)
radius = max(self.min_radius, radius)  

color_factor = 1 - (distance_from_mouse / dot.width)
color_factor = max(0, min(1, color_factor))  
color = (int(255 * color_factor), int(255 * (1 - color_factor)), int(255 * (color_factor ** 2)))
```



https://github.com/user-attachments/assets/15b12838-0e9d-49fe-937d-69d9f0678b64

This effect is very intuitive and can be perceived as a dynamic change in the sphere by mouse movement. When the mouse is close to the ball, the radius of the ball will increase, the shape will become more compressed, and the colour will gradually change from red to green, presenting a distance-aware effect.

## Confusing attempts

In order to enrich the visual effect, I designed the splitting and merging mechanism of the blobs. Tried to use some mathematical formulas to implement increasing the number of blobs and the offset to simulate the splitting effect.

1. I used the Euclidean distance formula to calculate the distance between the balls in each grid and the mouse.

```python
distance_from_mouse = np.sqrt((x - dot.mouse_x) ** 2 + (y - dot.mouse_y) ** 2)

```
2. A linear function based on distance is utilised, making smaller balls closer to the mouse larger.

```python
radius = self.max_radius - (distance_from_mouse / 4)
radius = max(self.min_radius, radius)


```
3. A linear scaling function is used, so that the number of blobs is higher when the mouse is close and lower when it is far away.

```python
num_balls = int(self.max_splitting * (1 - distance_from_mouse / dot.width))

```
4. The offset of each ball was calculated by means of the trigonometric functions cosine (cos) and sine (sin), so that the balls were distributed in a circle.

```python
offset_x = np.cos(angle) * radius * 0.6
offset_y = np.sin(angle) * radius * 0.6

```

https://github.com/user-attachments/assets/cac68496-0b0f-44bf-aa0f-9a5fdd97a3f8

REFLECTION: The accumulation of these practices leads to a dazzling effect on the image. I learnt an important principle here: design is not only about addition, but also about trade-offs.

## Back to simple

Based on my initial reflection, I realised that less is more and decided to go back to a simple design. The visual presentation is enhanced by ripples and compression effects. I used the sine function to add rhythm to the size of the balls, and limited the compression ratio to avoid visual clutter, thus enhancing the overall coherence and naturalness of the design. I made a few changes;

1. I simulated something like a simple linear incremental process, controlling the colour change over time by incrementing the self.color_shift variable so that the colour of the blob changes over time. The colour change is more pronounced when the ball is close to the mouse, but maintains the natural transition of colours.

```python
self.color_shift += 0.1
if self.color_shift > 255:
    self.color_shift = 0

```
2. I still calculated the distance between the ball and the mouse via the Euclidean distance formula, but this time I adjusted the radius of the ball and used a linear function to avoid too much variation.

```python
distance_from_mouse = np.sqrt((x - dot.mouse_x) ** 2 + (y - dot.mouse_y) ** 2)

radius = self.max_radius - (distance_from_mouse / 4)
radius = max(self.min_radius, radius)

```

3. I adjusted the ‘compression’ of the ball according to the mouse position by using scale_x and scale_y, and limited the maximum and minimum values of the scaling to avoid excessive distortion.

```python
scale_x = max(0.5, min(1.5, scale_x))
scale_y = max(0.5, min(1.5, scale_y))

```


https://github.com/user-attachments/assets/99c5cf9f-c021-4ce5-bb6a-df2b8ff95e64


## A beautiful mistake

During the experiment, I also realized that mistakes in design are not necessarily negative. Instead, they may become catalysts for innovation. For example, one of the previous mistakes was that unnecessary elements were not effectively removed in the design, resulting in repeated superimposition of the picture. Taking this opportunity, I tried to use the "eraser" effect to remove redundant visual elements through the superimposition of white lines and discovered different design possibilities. This process made me deeply realize that accidental mistakes can inspire new creativity.

Through this exploration, I have gained a new understanding of the value of mistakes in design. Accidental mistakes may actually contain potential creativity. At the same time, I am also more aware that "less is more" is not a limitation but emphasizes the core goal of design. Reasonable simplification can not only highlight the focus of design but also prevent users from losing focus in complex effects. Simplification does not necessarily mean deleting certain steps. Visual subtraction and focusing on the core goal of design are also effective approaches.

```python
ellipse_center = (x + int(np.sin(self.color_shift) * 20), y + int(np.cos(self.color_shift) * 20))
ellipse(layer, ellipse_center, (width + 10, height + 10), 0, 0, 360, (255, 255, 255), 1)

```


https://github.com/user-attachments/assets/3e0471f8-a5fe-4ac8-9807-29e74ffc44da

## Conclusion

Through this exploration, I have gained a new understanding of the value of mistakes in design. Accidental mistakes may actually contain potential creativity. At the same time, I am also more aware that "less is more" is not a limitation but emphasizes the core goal of design. Reasonable simplification can not only highlight the focus of design but also prevent users from losing focus in complex effects. Simplification does not necessarily mean deleting certain steps. Visual subtraction and focusing on the core goal of design are also effective approaches. In the future design process, I hope to explore more mathematical formulas, especially vector calculation, and think about how to influence the design effect over time. I have a hunch that this will bring more possibilities to my design.
