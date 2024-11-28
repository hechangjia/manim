from manim import *

class RotateSquare(Scene):
    def construct(self):
        # 创建一个正方形
        square = Square(side_length=2, color=GREEN)  # 边长为2，颜色为绿色

        # 设置初始位置在屏幕中心
        square.move_to(ORIGIN)

        # 绘制正方形动画
        self.play(Create(square))
        self.wait(1)

        # 旋转正方形90度并改变颜色
        self.play(Rotate(square, angle=PI / 2), square.animate.set_color(RED))
        self.wait(1)

        # 渐隐消失
        self.play(FadeOut(square))
        self.wait(1)
