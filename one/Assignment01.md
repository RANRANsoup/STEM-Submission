# Week 2 Exploring the Integration of Geometry and Audio Response

This week, I focused on exploring how simple geometric shapes can be combined with audio responses to create an interesting and rhythmic motion picture.

I was intrigued by the possibilities of visual and auditory interactions, especially how they could enhance the perception of audio. This experiment helped me consolidate the foundations of geometric drawing and also laid the groundwork for more complex dynamic visual design to follow.

## Static circles and dynamic circles

I started by implementing multiple fixed-position circles, a relatively simple part of the code that serves as a starting point for exploring the visual effects. SpongeBob ~

Next, I made the colour and size of the circles change according to the amplitude of the audio, trying to simulate the rhythmic feel of the audio. By comparing the static and dynamic effects, I was able to make the image more dynamic and interactive. Even though I only learnt to draw basic graphics, I tried to make the picture as interesting and rhythmic as possible, making the visuals closely match the audio, but overall, the result was better.

## Eyes 👀

I designed the mouse to look like SpongeBob SquarePants eyes.
```python
x = dot.mouse_x
y = dot.mouse_y
circle(dot.canvas, (x,y), radius, dot.aqua, -1)
```


https://github.com/user-attachments/assets/693f97c0-a4c4-4541-a849-7bc88e16f634




[see code](https://github.com/RANRANsoup/STEM-Submission/blob/a67e64ec3e19a819c7e2c473e6694a206ca8ba0e/one/week2-SpongeBob1.py)

## Square? Round!


I tried to explore how to cause shape changes in different ways:

1. Iterate over the pixel points and determine for each pixel point if it should be filled with a colour.

2. Calculate the distance from the pixel point to the centre using the Euclidean distance formula.
   
3. Determines whether the pixel needs to be filled with colour.
   
```python
    x, y = center
    if radius == 0:
        x1, y1 = x - size // 2, y - size // 2
        x2, y2 = x + size // 2, y + size // 2
        canvas[y1:y2, x1:x2] = color
    else:
        for i in range(-size // 2, size // 2):
            for j in range(-size // 2, size // 2):
                distance = np.sqrt(i**2 + j**2)
                if distance <= size // 2 - radius or (distance <= size // 2 and distance > size // 2 - radius):
                    canvas[y + j, x + i] = color
```
REFLECTION: Although this algorithm seems clean, this method may not be perfect when highly accurate graphics or dynamic shape changes are required.

Here's a demo of my attempt: [see code](https://github.com/RANRANsoup/STEM-Submission/blob/a67e64ec3e19a819c7e2c473e6694a206ca8ba0e/one/week2-SpongeBob2.py)




https://github.com/user-attachments/assets/f5a230ba-f9ff-497e-9283-36a894be2ed8





## Integration

I incorporated this attempt into my Week 2 assignment by combining mouse movements with shape changes to achieve a new background. [see code](https://github.com/RANRANsoup/STEM-Submission/blob/d17a15d25148d992fa48df4e0ca7a07b063093c8/one/week2-SpongeBob2.py)




https://github.com/user-attachments/assets/5496b005-fc7d-438f-8d3e-0b02128173f5



## Little progress 


During the second week, I drew circles like this:


<img width="953" alt="截屏2024-12-03 19 46 46" src="https://github.com/user-attachments/assets/5fa93dca-a01d-4133-b9a8-a0492a4244dd">


After a few weeks of study, here's how I drew the circle:


<img width="866" alt="截屏2024-12-03 19 50 32" src="https://github.com/user-attachments/assets/c1d18e7c-1d32-4ffa-8929-74a094155cd9">


The simplicity of expression does look pleasing to the eye, and I need more practice, but think I'm doing well so far ～

## Conclusions

The current work leaves much to be desired, such as the smoothness of the dynamic effects and the complexity of the algorithms.

As a next step, I would like to try more complex techniques, such as using Fourier Transform to process audio data, or designing more detailed dynamic visuals. At the same time, I plan to study more outstanding works to learn how to more effectively combine the interactive effects of visual and audio to make the design more innovative and expressive.
