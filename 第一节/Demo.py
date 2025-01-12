from manim import *
class Tem(Scene):
	def construct(self):
		# 心形
		s = Square(color=BLUE,fill_opacity=0.613)
		c1 = Circle(color=GREEN,fill_opacity=0.613).move_to(s.get_top())
		c2 = c1.copy().move_to(s.get_right())
		group1 = VGroup(s,c1,c2).rotate(45*DEGREES)
		self.play(Create(c1),Create(c2),Create(s))
		self.wait()
		self.play(group1.animate.to_edge(LEFT,buff=1))
		self.wait()
		# ×
		r1 = Rectangle(color=RED,height=4,width=4/5,fill_opacity=0.5).rotate(45*DEGREES)
		r2 = r1.copy().rotate(90*DEGREES)
		group2 = VGroup(r1,r2)
		self.play(Create(r1),Create(r2))
		self.wait()

		# 机器人
		sbig = Square(color=RED,fill_opacity=0.5,side_length=(4+4/5)/(2**0.5))
		csmall1 = Circle(fill_color=BLACK,stroke_color=RED,fill_opacity=0.5,radius=0.5).move_to(LEFT*0.7+UP*0.5)
		csmall2 = csmall1.copy().move_to(RIGHT*0.7+UP*0.5)
		smile_arc = Arc(radius=1.5,start_angle=PI + PI / 3,angle=PI / 3,color=RED).next_to(sbig, DOWN, buff=-0.5)
		group3 = VGroup(sbig,csmall1,csmall2,smile_arc).to_edge(RIGHT,buff=1)
		self.play(Create(sbig),Create(csmall1),Create(csmall2),Create(smile_arc))
		self.wait()