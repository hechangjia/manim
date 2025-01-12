from manim import *

# 场景类继承自 Scene
class CircleWithText(Scene):
    def construct(self):
        # 创建一个圆形对象
        circle = Circle(radius=1, color=BLUE)  # 半径为1，颜色为蓝色
        circle.set_fill(BLUE, opacity=0.5)    # 设置填充颜色和透明度

        # 创建一个文本对象
        text = Text("Hello, Manim!", font_size=36, color=YELLOW)  # 字体大小为36，颜色为黄色

        # 让文本放置在圆的下面
        text.next_to(circle, DOWN)  # DOWN 表示下方，也可以用 UP, LEFT, RIGHT 等方向

        # 将初始状态的圆和文本添加到场景中
        self.play(Create(circle), Write(text))  # Create 为圆的绘制动画，Write 为文本显示动画
        self.wait(1)  # 等待1秒

        # 让圆形扩大
        self.play(circle.animate.scale(2))  # 将圆放大2倍
        self.wait(1)  # 等待1秒

        # 让文本淡出，圆形消失
        self.play(FadeOut(text), Uncreate(circle))  # FadeOut 为渐隐动画，Uncreate 为渐消失动画
        self.wait(1)  # 等待1秒
