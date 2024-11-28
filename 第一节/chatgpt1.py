from manim import *

# 定义场景类，继承自 Scene
class ComplexManimExample(Scene):
    def construct(self):
        # 创建一个正方形，并设置颜色为蓝色
        square = Square(side_length=2, color=BLUE)
        # 将正方形移到左侧
        square.shift(LEFT * 3)
        # 添加到场景中
        self.add(square)
        
        # 创建一个圆形，并设置颜色为绿色
        circle = Circle(radius=1, color=GREEN)
        # 将圆形移到右侧
        circle.shift(RIGHT * 3)
        # 添加到场景中
        self.add(circle)

        # 创建一个文字对象
        text = Text("Manim 动画示例", font_size=48, color=YELLOW)
        # 将文字放在屏幕顶部
        text.to_edge(UP)

        # 动画 1：让正方形旋转并移动到屏幕中心
        square_animation = AnimationGroup(
            square.animate.rotate(PI / 4).move_to(ORIGIN),
            run_time=3
        )

        # 动画 2：让圆形缩放并改变颜色
        circle_animation = AnimationGroup(
            circle.animate.scale(1.5).set_color(RED),
            run_time=3
        )

        # 动画 3：文字淡入，并伴随小幅度的缩放效果
        text_animation = AnimationGroup(
            FadeIn(text, scale=0.5),
            run_time=2
        )

        # 使用 Play 方法同时运行所有动画
        self.play(
            square_animation,
            circle_animation,
            text_animation
        )

        # 额外动画：在屏幕中央创建一条移动的直线
        line = Line(LEFT * 4, RIGHT * 4, color=PURPLE)
        line_animation = Create(line)
        self.play(line_animation)

        # 动画结束后，保持画面 2 秒
        self.wait(2)
