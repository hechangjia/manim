from manim import *

class DynamicText(Scene):
    def construct(self):
        # 创建一个文本对象
        text = Text("欢迎来到贺昌嘉的视频!非常感谢您的支持! ",font_size=32)

        # 初始位置在屏幕中心
        text.move_to(ORIGIN)

        # 显示文字
        self.play(Write(text))
        self.wait(1)

        # 放大文字并改变颜色
        self.play(text.animate.scale(1.5).set_color(PURE_BLUE))
        self.wait(1)

        # 文字左右移动
        self.play(text.animate.shift(RIGHT * 4))
        self.wait(1)
        self.play(text.animate.shift(LEFT * 8))
        self.wait(1)

        # 渐隐消失
        self.play(FadeOut(text))
