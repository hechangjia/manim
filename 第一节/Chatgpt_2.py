from manim import *

class GradientBackground(Scene):
    def construct(self):
        # 创建一个渐变背景
        background = Rectangle(
            width=500, height=500, fill_color=PURE_GREEN , fill_opacity=1
        )
        background.set_fill(color=[BLUE, PURPLE], opacity=1)

        # 显示背景
        self.add(background)

        # 添加文本
        text = Text("Gradient Background", font_size=48, color=WHITE)
        self.play(Write(text))
        self.wait(2)

        # 渐隐文字
        self.play(FadeOut(text))
