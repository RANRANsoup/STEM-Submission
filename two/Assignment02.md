# Week 5

这一周，我探索了如何通过音频输入创建两种不同风格的视觉效果，我通过添加一些音频反应和实现效果，改编了课堂上提供的雪景素描，分别设计了适用于舒缓的音乐和有节奏感的音乐。我的兴趣是理解音频频率与视觉映射之间的关系，以及如何通过参数调整创造出能够平衡音频和视觉效果的作品。

## 保留和改变

在舒缓的音乐的可视化中，我想营造一种静谧的星空效果，符合柔和、轻盈的音律。

圆的大小根据频率数据逐渐变化。

```python
          fft_data = dot.music.fft()[:self.num_stars]
          for i in range(self.num_stars):
              size = int(fft_data[i])
              intensity = int(fft_data[i] * 10)
              self.colors[i] = (intensity, intensity, 255)
```
形成微弱的闪烁效果，像夜空中的星星在静静地闪烁。

```python
        self.speed_y = np.random.uniform(0.5, 2, self.num_stars)
        self.speed_x = np.random.uniform(-1, 1, self.num_stars)
```

我发现保留使用冷色调（如蓝白色）能更好地传递舒缓音乐的情感，同时避免了过于刺激的色彩组合，保留了视觉效果的和谐感。



https://github.com/user-attachments/assets/f97ed6ee-a48d-4605-b51f-86c5319e686b

[code here](https://github.com/RANRANsoup/STEM-Submission/blob/c2748d1aed6019f5486fc25c66eee9452c1aca17/two/week5-soothing%20music.py)


## 问题与挑战

上一个效果的实现相对简单，初步效果还不错，但在尝试加入节奏感强的音乐时，我遇到了一些挑战。在强烈的节奏变化时产生白色闪烁的球有时会显得过于突兀，尤其是当节奏变化过快时，频繁的闪烁会导致视觉上的不稳定感，和整体的视觉氛围也不搭。


https://github.com/user-attachments/assets/4fcfc234-24a3-4708-8e86-80cdf9ca55aa


## 形态变化

于是我选择做些改变，设计一个适合强节奏感的音频。首先我通过计算每个小球的偏移实现球团的扩散效果。

```python
for j in range(self.num_balls_per_cluster):
    # Calculate ball offsets
    offset_x = np.cos(2 * np.pi * j / self.num_balls_per_cluster) * size_factor * expansion_factor
    offset_y = np.sin(2 * np.pi * j / self.num_balls_per_cluster) * size_factor * expansion_factor
    ball_x = center_x + offset_x
    ball_y = center_y + offset_y
```

在调整 size_factor 和 expansion_factor 时，我发现直接使用 FFT 数据可能会导致数值范围过大或过小，调整时花了很多时间。因此，我上网搜索学习，最后引入了expansion_factor以控制扩散强度，确保视觉效果不会显得过于杂乱，且能保持画面的平衡。

## 保持平衡

为了让视觉效果更具层次感，但又不失稳定感，我使用了黑白灰色系的渐变层级，避免了过于突兀的颜色切换。我还通过 dot.music.is_beat() 检测节拍，我在短时间内切换背景颜色，从而增强节奏呼应。

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

这种方式使得小球在激烈的变化中仍能保持平衡。



https://github.com/user-attachments/assets/29485622-6285-4624-8950-be667b28c141

## 结论

我通过音频输入，显著提高了对不同风格的音乐可视化视觉效果的理解。视觉设计需要与音乐特质相呼应，但也需避免过度响应导致的不稳定感。我曾经觉得大部分音乐可视化看起来很单调，只是长长短短的方块，但是我现在理解了能适用到更多的场景里才是他们的使命。
下一步，我计划进一步探索如何增在设计上用减法，体现设计整体的流畅度和节奏感，提升视觉表现的连贯性与美感。
