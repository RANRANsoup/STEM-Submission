from dorothy import Dorothy
from cv2 import circle
import numpy as np

dot = Dorothy()

class MySketch:
    
    def __init__(self):
        # 初始化类并启动绘图循环
        # Initialize the class and start the drawing loop
        dot.start_loop(self.setup, self.draw)
        
    def setup(self):
        # 加载音频文件 / Load the audio file
        file_path = "week5/audio/drums.wav"
        dot.music.start_file_stream(file_path, fft_size=512, buffer_size=512)
        
        # 初始化节拍显示参数，用于背景闪烁
        # Initialize beat display parameter for background flashing
        self.show_beat = 0
        
        # 初始化球群参数
        # Initialize ball cluster parameters
        self.num_clusters = 80  # 球群数量 / Number of clusters
        self.num_balls_per_cluster = 50  # 每个球群的球数量 / Number of balls per cluster
        self.x = np.random.randint(0, dot.width, self.num_clusters)  # 随机初始化 x 坐标 / Randomly initialize x-coordinates
        self.y = np.random.randint(0, dot.height, self.num_clusters)  # 随机初始化 y 坐标 / Randomly initialize y-coordinates
        self.speed_y = np.random.uniform(0.5, 2, self.num_clusters)  # 垂直漂移速度 / Vertical drift speed
        self.speed_x = np.random.uniform(-1, 1, self.num_clusters)  # 水平漂移速度 / Horizontal drift speed

    def draw(self):
        # 设置背景颜色 / Set background color
        col = dot.black
        if dot.music.is_beat():  # 检测节拍 / Detect a beat
            self.show_beat = 10  # 持续闪烁时间 / Duration of flash
        
        if self.show_beat > 0:
            col = dot.white  # 节拍时切换背景为白色 / Change background to white on a beat
        
        dot.background(col)
        self.show_beat -= 1  # 减少节拍计数 / Decrease beat counter
        
        # 获取 FFT 数据 / Get FFT data
        fft_data = dot.music.fft()[:self.num_clusters]
        
        # 颜色渐变列表 / Grayscale gradient list
        color_palette = [
            (50, 50, 50),   # 深灰 / Dark gray
            (100, 100, 100),  # 中灰 / Medium gray
            (150, 150, 150),  # 浅灰 / Light gray
            (200, 200, 200),  # 更浅的灰 / Lighter gray
            (255, 255, 255),  # 纯白 / Pure white
        ]

        # 绘制球群 / Draw ball clusters
        for i in range(self.num_clusters):
            # 根据 FFT 数据调整扩散效果 / Adjust spread effect based on FFT data
            size_factor = int(fft_data[i])  # 调整球大小 / Adjust ball size
            expansion_factor = 1 + fft_data[i] * 8  # 控制扩散程度 / Control spread intensity

            # 球群中心坐标 / Ball cluster center coordinates
            center_x, center_y = self.x[i], self.y[i]
            
            # 绘制每个球 / Draw each ball
            for j in range(self.num_balls_per_cluster):
                # 计算球偏移 / Calculate ball offsets（难点）
                offset_x = np.cos(2 * np.pi * j / self.num_balls_per_cluster) * size_factor * expansion_factor
                offset_y = np.sin(2 * np.pi * j / self.num_balls_per_cluster) * size_factor * expansion_factor
                ball_x = center_x + offset_x
                ball_y = center_y + offset_y
                
                # 确定球的层级，用于选择颜色
                # Determine the layer of the ball to assign color
                layer_index = int(j / (self.num_balls_per_cluster / len(color_palette)))
                color = color_palette[layer_index]  # 根据层级选择颜色 / Choose color based on layer
                
                # 绘制球 / Draw the ball
                circle(dot.canvas, (int(ball_x), int(ball_y)), 1, color, -1)
            
            # 更新球群位置，缓慢漂移
            # Update ball cluster position with slow drifting
            self.x[i] = (self.x[i] + self.speed_x[i]) % dot.width
            self.y[i] = (self.y[i] + self.speed_y[i]) % dot.height


# 启动画面 / Launch the sketch
MySketch()

