from manim import *

class FormulaAnimation(Scene):
    def construct(self):
        # 定义公式的各部分
        formula_1 = MathTex("E", "=", "mc^2")
        formula_2 = MathTex("E", "=", "m", "\\cdot", "c", "\\cdot", "c")

        # 显示完整公式
        self.play(Write(formula_1))
        self.wait(1)

        # 将公式动态展开
        self.play(TransformMatchingTex(formula_1, formula_2))
        self.wait(1)

        # 高亮显示重点部分
        self.play(Indicate(formula_2[3:]))
        self.wait(1)

        # 渐隐消失
        self.play(FadeOut(formula_2))
