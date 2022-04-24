from manimlib import *
import numpy as np
import math

class WhyRouth(Scene):
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
                        # r" = ",
                        # r"{ {B(s)}",
                        # r"\over",
                        # r"{A(s)} }",
                        color=WHITE
                    )

        # poly = Tex(   
        #                 r"{p(s) =",
        #                 r"{ ", r"a_n", r"s^n", r"+", r"a_{n-1}", r"s^{n-1}", r"+", r"\hdots", r"+", r"a_1", r"s", r"+", r"a_0", r"}", r"}",
        #                 color=GREEN_D
        #             )

        for i in tf:
            self.play(Write(i))

        tf.generate_target()
        tf.target.scale(0.7).to_corner(UL)
        self.play(MoveToTarget(tf))

        chareq = SurroundingRectangle(tf[3],buff=0.01).set_stroke(width=3).set_color(BLUE)
        chareqtxt = Text("charakteristisches \n     Polynom", font="Times New Roman").next_to(chareq,DOWN).scale(0.7).set_color(BLUE)

        linetoeq = Arrow(start=chareq, end=chareqtxt, buff=0).set_color(BLUE)
        
        self.play(ShowCreation(chareq))
        self.play(ShowCreation(linetoeq))
        self.play(Write(chareqtxt))

        self.wait(2)

        axes = Axes(**self.axes_kwargs)

        x_label_tex = r"Re{}"
        y_label_tex = r"Im{}"

        labels = self.axis_labels = VGroup(
            axes.get_x_axis_label(x_label_tex).next_to(axes.x_axis.tip),
            axes.get_y_axis_label(y_label_tex).next_to(axes.y_axis.tip),
        )

        axlabel = VGroup(axes,labels).scale(0.8).to_corner(UR)

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

        rootbracetxt = Text("Nullstellen vom Nennerpolynom\nmüssen in der linken\nHalbebene liegen ", font="Times New Roman").scale(0.5).next_to(rootbrace,DOWN)

        # self.add(rootbrace)
        # self.add(rootbracetxt)
        self.play(Write(rootbrace))
        self.play(Write(rootbracetxt))


        #self.remove(roots,rootline,rootbrace,rootbracetxt,chareq,chareqtxt,linetoeq)
        self.play(FadeOut(roots), FadeOut(rootbrace), FadeOut(rootbracetxt), FadeOut(chareq), FadeOut(chareqtxt), FadeOut(linetoeq))


        self.wait(3)

        tf2 = Tex(   
                        r"{G(s) =",
                        r"{ {1}",
                        r"\over",
                        r"{s+a} }",
                        color=WHITE
                    ).scale(0.7).next_to(tf,DOWN*4).to_corner(LEFT)
        
        #self.add(tf2)
        self.play(Write(tf2))

        self.wait(8)

        tf2conds = Tex(r"a > 0 \hspace{0.5cm},\hspace{0.5cm} s < 0",r"\\",r"a < 0 \hspace{0.5cm},\hspace{0.5cm} s > 0").scale(0.7).next_to(tf2,RIGHT*3)
        
        #self.add(tf2conds)
        self.play(Write(tf2conds))


        self.wait(2)


        condbox1 = SurroundingRectangle(tf2conds[0],buff=0.05).set_color(GREEN_C)
        condbox2 = SurroundingRectangle(tf2conds[1],buff=0.05).set_color(RED_C)

        #self.add(condbox1,condbox2)
        #self.play(ShowCreation(condbox1), ShowCreation(condbox2))

        dots1 = Dot(color=GREEN_C)
        dots2 = Dot(color=RED_C)
        dots1.move_to(axes.c2p(0, 0))
        dots2.move_to(axes.c2p(0, 0))


        self.play(FadeIn(dots1, scale=0.5))
        self.play(ShowCreation(condbox1), dots1.animate.move_to(axes.c2p(-2, 0)))

        self.wait(1)

        self.play(FadeIn(dots2, scale=0.5))
        self.play(ShowCreation(condbox2), dots2.animate.move_to(axes.c2p(2, 0)))

        self.wait(10)

        ltr = Tex(r"\mathcal{L}^{-1}\{G(s)\}", r"=", r"e^{", r"-at}" , r"=", r"e^{", r"st}").scale(0.8).next_to(tf2,DOWN*4).to_corner(LEFT)
        ltr[3].set_color(YELLOW_C)
        ltr[-1].set_color(YELLOW_C)

        #self.add(ltr)
        self.play(Write(ltr))

        rootsltr = Text("Nullstellen", font="Times New Roman").scale(0.8).set_color(YELLOW_C).next_to(ltr[4],DOWN*2)

        arrowltr1 = Arrow(start=ltr[3],end=rootsltr,buff=0.1).set_color(YELLOW_C).set_opacity(0.5)
        arrowltr2 = Arrow(start=ltr[-1],end=rootsltr,buff=0.1).set_color(YELLOW_C).set_opacity(0.5)

        # self.add(arrowltr1,arrowltr2)
        # self.add(rootsltr)


        self.play(ShowCreation(arrowltr1), ShowCreation(arrowltr2))
        self.play(Write(rootsltr))

        self.wait(11)


        axes2 = Axes(
            x_range=(0, 2, 0.5),
            y_range=(0, 2, 0.5),
            height=3,
            width=5,
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
            },
            x_axis_config={
                "include_tip": True,
            },
            y_axis_config={
                "include_tip": False,
            }
        )
        # axes2.add_coordinate_labels(
        #     font_size=20,
        #     num_decimal_places=1,
        # )

        labels2 = self.axis_labels = VGroup(
            axes2.get_x_axis_label("t").next_to(axes2.x_axis.tip),
            #axes2.get_y_axis_label("").next_to(axes2.y_axis.tip),
        )

        ax2 = VGroup(axes2,labels2)        

        ax2.scale(0.8).to_corner(DR)
        # self.add(ax2)
        self.play(ShowCreation(ax2))

        stable = Text("Stabil", font="Times New Roman").scale(0.8).next_to(ltr,DOWN*6).to_corner(LEFT).set_color(GREEN_C)
        notstable = Text("Nicht Stabil", font="Times New Roman").scale(0.8).next_to(stable,DOWN*2).to_corner(LEFT).set_color(RED_C)

        self.wait(7)

        func1 = lambda q: np.exp(-2*q) #Not a VMobject
        graph1 = axes2.get_graph(func1, color=GREEN_C, x_range=(0,2)) #VMobject
        self.play(ShowCreation(graph1))

        self.wait(8)

        self.play(Write(stable))

        self.wait(13)

        func2 = lambda q: np.exp(0.4*q) #Not a VMobject
        graph2 = axes2.get_graph(func2, color=RED_C, x_range=(0,2)) #VMobject
        self.play(ShowCreation(graph2))

        self.wait(3)

        self.play(Write(notstable))

        self.wait(13)

        exmp1 = Text("Beispiel", font="Times New Roman").scale(0.8).to_corner(UL).set_color(YELLOW_C)
        underline = Underline(mobject=exmp1).set_color(YELLOW_C)

        #CameraFrame
        frame = self.camera.frame
        self.camera.frame.save_state()
        frame2 = frame.copy()
        frame2.set_width(5)
        frame2.move_to(exmp1)
        self.play(Transform(frame, frame2), TransformMatchingParts(tf,exmp1))

        #self.play( TransformMatchingParts(tf,exmp1) )
        self.play(Write(underline))
        self.remove(graph1,graph2,dots1,dots2,ltr,arrowltr1,arrowltr2,rootsltr,stable,notstable,tf2,tf2conds,condbox1,condbox2,ax2)

        axes3 = Axes(
            x_range=(0, 2, 0.5),
            y_range=(-1, 2, 0.5),
            height=3,
            width=5,
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 2,
            },
            x_axis_config={
                "include_tip": True,
            },
            y_axis_config={
                "include_tip": False,
            }
        )

        labels3 = self.axis_labels = VGroup(
            axes2.get_x_axis_label("t").next_to(axes3.x_axis.tip),
            #axes2.get_y_axis_label("").next_to(axes2.y_axis.tip),
        )
        ax3 = VGroup(axes3,labels3)

        ax3.scale(0.8).to_corner(DR)
        #self.add(ax3)
        self.play(ShowCreation(ax3))

        axes.generate_target()
        #axes.target.become( axes.add_coordinate_labels( font_size=15, num_decimal_places=1,) )
        axes.target.become( axes.add_coordinate_labels( x_values=(-3, -2, -1, 1, 2), y_values={0} ) )


        self.play(Restore(self.camera.frame))
        #CameraFrame



        tf3 = Tex(r"G(s) =",r"\frac{1}{s+1}",r"\cdot",r"\frac{1}{s+3}",r"\cdot",r"\frac{1}{s-2}",r"=",r"\frac{A}{s+1}",r"+",r"\frac{B}{s+3}",r"+",r"\frac{C}{s-2}").scale(0.8).next_to(exmp1,DOWN*2).to_corner(LEFT)
        ltr_tf3 = Tex(r"\mathcal{L}^{-1}\{G(s)\}", r"=", r"A \cdot e^{-t}" , r"+", r"B \cdot e^{-3t}", r"+", r"C \cdot e^{2t}").scale(0.8).next_to(tf3,DOWN*4).to_corner(LEFT)

        tf3[1].set_color(GOLD_B)
        tf3[3].set_color(TEAL_C)
        tf3[5].set_color(MAROON_C)

        tf3[7].set_color(GOLD_B)
        tf3[9].set_color(TEAL_C)
        tf3[11].set_color(MAROON_C)

        ltr_tf3[2].set_color(GOLD_B)
        ltr_tf3[4].set_color(TEAL_C)
        ltr_tf3[6].set_color(MAROON_C)

        # self.add(tf3)
        # self.add(ltr_tf3)
        self.play(Write(tf3[0:6]))

        self.wait(7)

        self.play(Write(tf3[6:12]))

        self.wait(7)

        self.play(Write(ltr_tf3))

        self.wait(6)

        dots1_tf3 = Dot(color=GOLD_B)
        dots2_tf3 = Dot(color=TEAL_C)
        dots3_tf3 = Dot(color=MAROON_C)

        dots1_tf3.move_to(axes.c2p(0, 0))
        dots2_tf3.move_to(axes.c2p(0, 0))
        dots3_tf3.move_to(axes.c2p(0, 0))

        stable_tf3 = Text("G(s) ist stabil", font="Times New Roman").scale(0.8).to_corner(LEFT).set_color(GREEN_C).next_to(ltr_tf3,DOWN*8)
        notstable_tf3 = Text("G(s) ist nicht stabil", font="Times New Roman").scale(0.8).to_corner(LEFT).set_color(RED_C).next_to(ltr_tf3,DOWN*8)

        checkmark = Checkmark().next_to(stable_tf3,RIGHT).set_color(GREEN_C)
        exmark = Exmark().next_to(notstable_tf3,RIGHT).set_color(RED_C)

        consts = Tex(r"A",r"B",r"C").scale(0.5)
        consts[0].set_color(GOLD_B)
        consts[1].set_color(TEAL_C)
        consts[2].set_color(MAROON_C)

        consts[0].next_to(axes3.c2p(0,-0.5),LEFT)
        consts[1].next_to(axes3.c2p(0,2),LEFT)
        consts[2].next_to(axes3.c2p(0,1),LEFT)

        #self.add(consts)
        self.play(Write(consts))

        self.play(FadeIn(dots1_tf3, scale=0.5))
        self.play( dots1_tf3.animate.move_to(axes.c2p(-1, 0)) )
        func1_tf3 = lambda q: (-0.5)*np.exp(-1*q) #Not a VMobject
        graph1_tf3 = axes3.get_graph(func1_tf3, color=GOLD_B, x_range=(0,2)) #VMobject
        self.play(ShowCreation(graph1_tf3),Write(stable_tf3),Write(checkmark))


        self.play(FadeIn(dots2_tf3, scale=0.5))
        self.play( dots2_tf3.animate.move_to(axes.c2p(-3, 0)) )
        func2_tf3 = lambda q: (2)*np.exp(-3*q) #Not a VMobject
        graph2_tf3 = axes3.get_graph(func2_tf3, color=TEAL_C, x_range=(0,2)) #VMobject
        self.play(ShowCreation(graph2_tf3))

        self.wait(1)

        self.play(FadeIn(dots3_tf3, scale=0.5))   
        self.play( dots3_tf3.animate.move_to(axes.c2p(2, 0)) )
        func3_tf3 = lambda q: (1)*np.exp(0.5*q) #Not a VMobject
        graph3_tf3 = axes3.get_graph(func3_tf3, color=MAROON_C, x_range=(0,2)) #VMobject
        self.play(ShowCreation(graph3_tf3),FadeTransform(stable_tf3,notstable_tf3),FadeTransform(checkmark,exmark))

        self.wait(7)

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

        frame3 = frame.copy()
        frame4 = frame.copy()

        frame3.set_width(polys[0].get_width())
        frame3.move_to(polys[0])

        frame4.shift(RIGHT)

        self.play(Transform(frame, frame3), TransformMatchingTex(tf3,polys[0]))

        self.play( ShrinkToCenter(exmp1),ShrinkToCenter(axlabel),ShrinkToCenter(ax3),ShrinkToCenter(ltr_tf3),ShrinkToCenter(notstable_tf3),ShrinkToCenter(exmark),
                    ShrinkToCenter(consts),ShrinkToCenter(graph1_tf3),ShrinkToCenter(graph2_tf3),ShrinkToCenter(graph3_tf3),ShrinkToCenter(underline),
                    ShrinkToCenter(dots1_tf3),ShrinkToCenter(dots2_tf3),ShrinkToCenter(dots3_tf3) )

        self.play(Transform(frame, frame4))


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


        x = 0
        while x<7:
            self.play(TransformMatchingTex(polys[x].copy(),polys[x+1],path_arc=90 * DEGREES))
            x+=1

        self.wait(10)

        polys.generate_target()
        polys.target.to_corner(LEFT)
        self.play(MoveToTarget(polys),Restore(self.camera.frame))

        polysbrace = Brace(polys, direction=RIGHT, color=RED)

        polysbracetxt = Text("Wie bestimmt man\ndie Nullstellen?", font="Times New Roman").scale(0.8).next_to(polysbrace,RIGHT)
        polysbracetx2 = Text("Wie bestimmt man\ndie Stabilität?", font="Times New Roman").scale(0.8).next_to(polysbrace,RIGHT)


        # self.add(polysbrace)
        # self.add(polysbracetxt)
        self.play(Write(polysbrace))
        self.play(Write(polysbracetxt))
        
        self.play(Transform(polysbracetxt,polysbracetx2))

        self.wait(10)

        self.play(*[FadeOut(mob)for mob in self.mobjects])

        func = ParametricCurve(self.func, t_range = np.array([0, 2*PI]), fill_opacity=0.5).set_color(RED).move_to(ORIGIN)
        self.play(ShowCreation(func.scale(0.2), run_time=3))

        tugraz = Text(" Routh\nHurwitz").move_to(ORIGIN)
        self.play(Write(tugraz))

        self.wait(4)

        self.play(*[FadeOut(mob)for mob in self.mobjects])

        self.wait(2)

    # HEART FUNCTION
    def func(self, t):
        return np.array( (  16 * ( np.sin(t) ** 3 ), 13 * np.cos(t) - 5* np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t), 0  ) )
