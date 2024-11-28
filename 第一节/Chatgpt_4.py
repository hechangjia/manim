from manim import *

class DrawFunctionGraph(Scene):
    def construct(self):
        # 创建坐标系
        axes = Axes(
            x_range=[-3, 3, 1],  # x轴范围从-3到3，刻度间隔为1
            y_range=[-1, 1, 0.5],  # y轴范围从-1到1，刻度间隔为0.5
            axis_config={"color": BLUE},
        )
        self.play(Create(axes))  # 显示坐标系

        # 绘制正弦函数
        graph = axes.plot(lambda x: np.sin(x), color=YELLOW, x_range=[-3, 3])
        self.play(Create(graph), run_time=2)  # 绘制动画，持续2秒
        self.wait(1)

        # 添加标签
        label = axes.get_graph_label(graph, label="\\sin(x)", x_val=2, direction=UP)
        self.play(Write(label))
        self.wait(1)

        # 移除所有对象
        self.play(FadeOut(axes), FadeOut(graph), FadeOut(label))
