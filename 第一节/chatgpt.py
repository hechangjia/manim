from manim import *

class HelloWorld(Scene):
    def construct(self):
        text = Text("你好,贺昌嘉")
        self.play(Write(text))
        self.wait()

# 保存为文件并运行：
if __name__ == "__main__":
    import os
    os.system("manim -pql script_name.py HelloWorld")
