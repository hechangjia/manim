from manim import *

class GradientBackgroundWithText(Scene):
    def construct(self):
        # 创建一个渐变背景矩形，覆盖整个屏幕
        background = Rectangle(
            width=config.frame_width,
            height=config.frame_height
        )
        background.set_fill(color=[BLUE, PINK], opacity=1)  # 设置渐变颜色和透明度

        # 添加背景到场景中
        self.add(background)

        # 创建动态文本
        text = Text("欢迎来到贺昌嘉的视频!非常感谢您的观看!", font_size=48, color=PURE_GREEN)

        # 初始位置在屏幕中心
        text.move_to(ORIGIN)

        # 动画 1：显示文字
        self.play(Write(text))
        self.wait(1)

        # 动画 2：放大文字并改变颜色
        self.play(text.animate.scale(1.5).set_color(PURE_RED))
        self.wait(1)

        # 动画 3：文字左右移动
        self.play(text.animate.shift(RIGHT * 4))
        self.wait(1)
        self.play(text.animate.shift(LEFT * 8))
        self.wait(1)

        # 动画 4：渐隐消失
        self.play(FadeOut(text))
