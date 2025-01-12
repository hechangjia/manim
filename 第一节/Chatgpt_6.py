from manim import *

class DrawPolygon(Scene):
    def construct(self):
        # 创建一个多边形（三角形）
        triangle = Polygon(
            [-2, -1, 0],  # 第一个顶点坐标
            [2, -1, 0],   # 第二个顶点坐标
            [0, 2, 0],    # 第三个顶点坐标
            color=BLUE
        )
        triangle.set_fill(BLUE, opacity=0.5)  # 设置填充颜色和透明度

        # 显示多边形
        self.play(Create(triangle))
        self.wait(1)

        # 缩放动画
        self.play(triangle.animate.scale(0.5))
        self.wait(1)

        # 改变位置和颜色
        self.play(triangle.animate.shift(UP * 2).set_color(RED))
        self.wait(1)

        # 渐隐消失
        self.play(FadeOut(triangle))
