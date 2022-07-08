from manimlib import *
import numpy as np

class B_WHYROUTH_ENG(Scene):
    CONFIG = {
		"axes_kwargs": {
			"x_range": (-3, 3, 1),
			"y_range": (-3, 3, 1),
            "include_ticks": False,
			"height": 5,
			"width": 5,
			"axis_config": {
				"stroke_color": WHITE,
				"stroke_width": 4,
                "include_ticks": True,
			},
			"y_axis_config": {
				"include_tip": True,
                "include_ticks": False,
                "include_numbers": False,
			},
            "x_axis_config": {
                "include_tip": True,
            }
		}
	}
    def construct(self):
        
        tf = Tex(   
                        r"{G(s) =",
                        r"{ {b_m s^m + b_{m-1} s^{m-1} + \hdots + b_{1} s + b_0}",
                        r"\over",
                        r"{a_n s^n + a_{n-1} s^{n-1} + \hdots + a_1} s + a_0} }",
                        color=WHITE
                    )

        for i in tf:
            self.play(Write(i))

        tf.generate_target()
        tf.target.scale(0.7).to_corner(LEFT).shift(UP)
        self.play(MoveToTarget(tf))

        chareq = SurroundingRectangle(tf[3],buff=0.01).set_stroke(width=3).set_color(BLUE)
        chareqtxt = Tex(r"\text{characteristic}",r"\text{polynomial}").arrange(DOWN).next_to(chareq,DOWN).scale(0.7).set_color(BLUE)

        linetoeq = Arrow(start=chareq, end=chareqtxt, buff=0).set_color(BLUE)
        
        self.play(ShowCreation(chareq))
        self.play(ShowCreation(linetoeq))
        self.play(Write(chareqtxt))

        self.wait(2)

        axes = Axes(**self.axes_kwargs)

        x_label_tex = r"\Re"
        y_label_tex = r"\Im"

        xlabel = axes.get_x_axis_label(x_label_tex).next_to(axes.x_axis.tip)
        ylabel = axes.get_y_axis_label(y_label_tex).next_to(axes.y_axis.tip)
        labels = VGroup(xlabel,ylabel)

        axlabel = VGroup(axes,labels).scale(0.8).to_corner(RIGHT).shift(UP)

        self.play(FadeIn(axlabel))

        root1 = Arrow(start=axes.c2p(0, 0.5), end= axes.c2p(-1, 0.5), buff=0)
        root2 = Arrow(start=axes.c2p(0, 1), end= axes.c2p(-1, 1), buff=0)
        root3 = Arrow(start=axes.c2p(0, 1.5), end= axes.c2p(-1, 1.5), buff=0)
        root4 = Arrow(start=axes.c2p(0, 2), end= axes.c2p(-1, 2), buff=0)

        root5 = Arrow(start=axes.c2p(0, -0.5), end= axes.c2p(-1, -0.5), buff=0)
        root6 = Arrow(start=axes.c2p(0, -1), end= axes.c2p(-1, -1), buff=0)
        root7 = Arrow(start=axes.c2p(0, -1.5), end= axes.c2p(-1, -1.5), buff=0)
        root8 = Arrow(start=axes.c2p(0, -2), end= axes.c2p(-1, -2), buff=0)

        roots = VGroup(root1,root2,root3,root4,root5,root6,root7,root8).set_color(BLUE)

        self.play(ShowCreation(roots))

        rootline = Line(start=axes.c2p(0,-3), end=axes.c2p(-3,-3))

        rootbrace = Brace(rootline, direction=DOWN, color=BLUE)

        rootbracetxt = Tex(r"\text{Roots of the denominator}",r"\text{must lie on the}",r"\text{left half-plane}").set_color(BLUE).scale(0.5).arrange(DOWN,buff=SMALL_BUFF)
        rootbracetxt.next_to(rootbrace,DOWN)

        self.play(Write(rootbrace))
        self.play(Write(rootbracetxt)) 

        self.wait(2)


        #CameraFrame
        frame = self.camera.frame
        self.camera.frame.save_state()

        ps_h = Tex(r"p_0(s)","=",r"s^3",r"+",r"2",r"s^2",r"-",r"5",r"s",r"-",r"6")
        ps_1 = Tex(r"p_1(s)","=",r"2",r"s^4",r"+",r"2",r"s^2",r"+",r"s",r"+",r"1")
        ps_2 = Tex(r"p_2(s)","=",r"s^5",r"+",r"3",r"s^4",r"+",r"2",r"s^3",r"+",r"s^2",r"+",r"1")
        ps_3 = Tex(r"p_3(s)","=",r"5",r"s^6",r"+",r"3",r"s^5",r"+",r"2",r"s^4",r"+",r"7",r"s^3",r"+",r"s^2",r"+",r"9",r"s",r"+",r"1")
        ps_4 = Tex(r"p_4(s)","=",r"-",r"2",r"s^2",r"-",r"2",r"s",r"-",r"1")
        ps_5 = Tex(r"p_5(s)","=",r"s^2",r"+",r"4",r"s",r"-",r"3")
        ps_6 = Tex(r"p_6(s)","=",r"s^2",r"+",r"s",r"+",r"1")
        ps_7 = Tex(r"p_7(s)","=",r"s",r"+",r"8")

        polys = VGroup(ps_h,ps_1,ps_2,ps_3,ps_4,ps_5,ps_6,ps_7)
        polys.arrange(DOWN,buff=MED_LARGE_BUFF)


        for line in polys:
            tm = -line.get_part_by_tex("=").get_center()
            line.shift(tm[0] * RIGHT)


        # # # CAN BE USED IN FUTURE. 
        # for line in polys:
        #     tm = -line.get_part_by_tex("=").get_center()
        #     line.shift(tm[0] * RIGHT)
        # # #

        # # # SAME METHOD WITH while LOOP
        # y = 0
        # while y<7:
        #     tm = -polys[y].get_part_by_tex("=").get_center()
        #     polys[y].shift(tm[0] * RIGHT)
        #     y+=1
        # # #

        frame3 = frame.copy()
        frame4 = frame.copy()

        frame3.set_width(polys[0].get_width())
        frame3.move_to(polys[0])
        frame4.shift(RIGHT)

        self.play(  Transform(frame, frame3),
                    FadeOut(roots), FadeOut(rootbrace), FadeOut(rootbracetxt), FadeOut(chareq), FadeOut(chareqtxt), FadeOut(linetoeq), FadeOut(tf), FadeOut(axlabel))


        self.play(Write(ps_h))
        self.play(Transform(frame, frame4))


        x = 0
        while x<7:
            self.play(TransformMatchingTex(polys[x].copy(),polys[x+1],path_arc=90 * DEGREES))
            x+=1

        self.wait(5) #it was 10


        polys.generate_target()
        polys.target.to_corner(LEFT)
        self.play(MoveToTarget(polys),Restore(self.camera.frame))

        polysbrace = Brace(polys, direction=RIGHT, color=RED)

        polysbracetxt = Tex(r"\text{How to find the roots?}").arrange(DOWN).scale(0.8).next_to(polysbrace,RIGHT)
        polysbracetx2 = Tex(r"\text{How to check}",r"\text{the BIBO-stability?}").arrange(DOWN).scale(0.8).next_to(polysbrace,RIGHT)

        self.play(Write(polysbrace))
        self.play(Write(polysbracetxt))
        
        self.play(Transform(polysbracetxt,polysbracetx2))

        self.wait(5) #it was 10

        self.play(*[FadeOut(mob)for mob in self.mobjects])

        rhtext = Text("Answer: Routh-Hurwitz Stability Criterion",slant=ITALIC).shift(UP*3)

        scientist1 = ImageMobject("./Edward_J_Routh.jpg").shift(LEFT*2)
        scientist2 = ImageMobject("./Adolf_Hurwitz.jpg").shift(RIGHT*2)

        fs1box = SurroundingRectangle(scientist1,buff=0).set_color(GOLD_E)
        fs2box = SurroundingRectangle(scientist2,buff=0).set_color(GOLD_E)

        fs1_name = Text("Edward J. Routh").scale(0.9).next_to(fs1box,DOWN)
        fs2_name = Text("Adolf Hurwitz").scale(0.9).next_to(fs2box,DOWN)

        fs1_date = Text("1831 - 1907",slant=ITALIC).scale(0.9).next_to(fs1_name,DOWN)
        fs2_date = Text("1859 - 1919",slant=ITALIC).scale(0.9).next_to(fs2_name,DOWN)

        self.play(Write(rhtext))

        self.play(FadeIn(scientist1),FadeIn(scientist2))

        self.play(ShowCreation(fs1box),ShowCreation(fs2box))

        self.play(Write(fs1_name),Write(fs2_name))

        self.play(Write(fs1_date), Write(fs2_date))

        self.wait(3)

        self.play(*[FadeOut(mob)for mob in self.mobjects])

        self.wait(2)