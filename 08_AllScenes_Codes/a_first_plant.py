from manimlib import *
import numpy as np

class Plant(Scene):
    CONFIG = {
		"axes_kwargs": {
			"x_range": (-3, 3, 1),
			"y_range": (-3, 3, 1),
			"height": 5,
			"width": 5,
			"axis_config": {
				"stroke_color": WHITE,
				"stroke_width": 4,
			},
			"y_axis_config": {
				"include_tip": True,
			},
            "x_axis_config": {
                "include_tip": True,
            }
		}
	}

    def construct(self):

        self.wait(3.5)

        intro_words = Text("Routh-Hurwitz-Kriterium",font="Times New Roman").scale(0.7)#, **self.title_kwargs)
        intro_words.set_color(YELLOW_C).scale(2)

        underline = Underline(mobject=intro_words)
        underline.set_color(YELLOW_C)

        self.play(Write(intro_words))

        self.play(ShowCreation(underline))

        self.wait(3)

        self.play(ShrinkToCenter(intro_words), ShrinkToCenter(underline))

        self.wait(3)



        strp = ['Strecke','P(s)']
        self.display_plantp(strp)
    ############################### PLANT FUNCTION
    def display_plantp(self, strp):
        plantp = VGroup()
        for s in strp:
            t = self.get_text(s)
            plantp.add(t)
    ###############################


        plantp.to_edge(UP, buff=0.3)
        plantp.arrange(DOWN, buff=0.3)

        rectplant = Rectangle()
        #plantp = Tex(r"\text{Plant}\\\text{P(s)}")
        linetoplant = Line([-4, 0, 0], [-2, 0, 0])
        linetoy = Line([2, 0, 0], [3, 0, 0])

        rectcont = Rectangle().shift(UP*2 + LEFT*4)
        #contc = Tex(r"\centering \text{Controller} \text{C(s)}").shift(UP*2 + LEFT*4).arrange(DOWN, center=False, aligned_edge=LEFT)
        contc = VGroup(Text("Regler",font="Times New Roman"), Text("R(s)",font="Times New Roman")).to_edge(UP, buff=0.3).arrange(DOWN, buff=0.3).shift(UP*2 + LEFT*4)
        linetocont = Line([-7, 2, 0], [-6, 2, 0])

        sumcirc = Circle(radius=0.2, color = WHITE).next_to(linetocont,LEFT,aligned_edge=LEFT) #not the best alignment
        sumsign = Tex(r"-").next_to(sumcirc,DR/3)

        linetoy2 = Line([5, 2, 0], [7, 2, 0])
        linetodown = Line([6, 2, 0], [6, -0.3, 0])
        #linetoleft = Line([6, -0.3, 0], [-7.25, -0.3, 0])
        linetoup = Line(start=DOWN,end=UP).next_to(sumcirc,DOWN,aligned_edge=UP)
        linetoleft = Line(linetodown.get_corner(DOWN),linetoup.get_corner(DOWN))

        linetocirc = Line(LEFT,RIGHT).next_to(sumcirc,LEFT,aligned_edge=RIGHT) #better alignment example

        refvalue = Tex(r"r").next_to(linetocirc,UP)
        outvalue = Tex(r"y").next_to(linetoy2,UR)

        frame = self.camera.frame
        self.camera.frame.save_state()
        frame2 = frame.copy()
        #frame2.set_width(rect.width)
        frame2.set_width(8)
        self.play(Transform(frame, frame2))

        self.play(ShowCreation(rectplant), ShowCreation(linetoplant), ShowCreation(linetoy))
        self.play(Write(plantp))
        #self.play(Restore(self.camera.frame))

        frame3 = frame.copy()
        frame3.set_width(20)
        self.play(Transform(frame, frame3))

        self.play(ApplyMethod(plantp.shift, UR*2), MaintainPositionRelativeTo(rectplant, plantp), 
                                                   MaintainPositionRelativeTo(linetoplant, plantp), 
                                                   MaintainPositionRelativeTo(linetoy, plantp) )

        self.wait(1)
        
        self.play(ShowCreation(rectcont), ShowCreation(linetocont))
        self.play(Write(contc))

        self.wait(1)

        self.play(ShowCreation(linetoy2), ShowCreation(linetodown), ShowCreation(linetoleft), ShowCreation(linetoup), ShowCreation(linetocirc))

        self.play(ShowCreation(sumcirc), Write(sumsign))

        self.play(Write(refvalue),Write(outvalue))

        ar_linetoplant = linetoplant.copy()
        ar_linetoplant.add_tip()

        ar_linetocont = linetocont.copy()
        ar_linetocont.add_tip()

        ar_linetoy2 = linetoy2.copy()
        ar_linetoy2.add_tip()

        ar_linetoup = linetoup.copy()
        ar_linetoup.add_tip()

        ar_linetocirc = linetocirc.copy()
        ar_linetocirc.add_tip()

        self.play(  TransformMatchingShapes( linetoplant,ar_linetoplant ),
                    TransformMatchingShapes( linetocont,ar_linetocont ),
                    TransformMatchingShapes( linetoy2,ar_linetoy2 ),
                    TransformMatchingShapes( linetoup,ar_linetoup ),
                    TransformMatchingShapes( linetocirc, ar_linetocirc ),
        )

        # self.play(  Transform( linetoplant,linetoplant.add_tip() ),
        #             Transform( linetocont,linetocont.add_tip() ),
        #             Transform( linetoy2,linetoy2.add_tip() ),
        #             Transform( linetoup,linetoup.add_tip() ),
        #             Transform( linetocirc,linetocirc.add_tip() ),
        #             run_time=3
        # )

        # self.play(  FadeIn(linetoplant.add_tip()),
        #             FadeIn(linetocont.add_tip()),
        #             FadeIn(linetoy2.add_tip()),
        #             FadeIn(linetoup.add_tip()),
        #             FadeIn(linetocirc.add_tip())  )

        self.wait(1)

        numer = Tex(r'R(s)P(s)')
        divline = Line().next_to(numer,DOWN,buff=0.2).scale(1.5)
        denom = Tex(r'1+R(s)P(s)').next_to(divline,DOWN,buff=0.2)
        TS = Tex(r'G(s) = ').next_to(divline,LEFT)

        eqn = VGroup(TS,numer,divline,denom).shift(DOWN*2.5 + LEFT).scale(1.4)
        self.play(Write(eqn))
        
        self.wait(10)

        #self.play(Fade(numer.set_color_by_tex(r'C(s)P(s)',ORANGE)))
        self.play(FadeToColor(numer, ORANGE), FadeToColor(contc,ORANGE), FadeToColor(plantp,ORANGE))

        self.wait(2)

        #self.play(FadeIn(numer.set_color_by_tex(r'C(s)P(s)',WHITE)))
        self.play(FadeToColor(numer, WHITE), FadeToColor(contc,WHITE), FadeToColor(plantp,WHITE))

        self.wait(2)

        #self.play(FadeIn(numer.set_color_by_tex(r'C(s)P(s)',BLUE)))
        self.play(FadeToColor(denom, BLUE), FadeToColor(contc,BLUE), FadeToColor(plantp,BLUE), FadeToColor(sumsign,BLUE))

        self.wait(2)

        self.play(FadeToColor(denom, WHITE), FadeToColor(contc,WHITE), FadeToColor(plantp,WHITE), FadeToColor(sumsign,WHITE))

        framebox1 = SurroundingRectangle(rectcont, buff = .1).stretch_to_fit_width(11).shift(RIGHT*3)
        self.play(ShowCreation(framebox1))

        numer2 = Tex(r'L(s)').next_to(divline,UP,buff=0.2).scale(1.4)
        denom2 = Tex(r'1+L(s)').next_to(divline,DOWN,buff=0.2).scale(1.4)

        self.play(TransformMatchingTex(numer,numer2))
        self.play(TransformMatchingTex(denom,denom2))

        framebox2 = SurroundingRectangle(divline, buff = .1).stretch_to_fit_height(4)
        self.play(ShowCreation(framebox2))

        self.play(FadeOut(framebox1),FadeOut(framebox2))

        rightequal = Tex(r'=').next_to(divline,RIGHT,aligned_edge=RIGHT)
        rightline = Line().next_to(rightequal,RIGHT,aligned_edge=LEFT).scale(0.8)
        rightnumer = Tex(r'\mu(s)').next_to(rightline,UP,buff=0.2)
        rightdenom = Tex(r'\nu(s)').next_to(rightline,DOWN,buff=0.2)

        righteq = VGroup(rightequal,rightline,rightnumer,rightdenom).scale(1.4).next_to(eqn,RIGHT)
        self.play(Write(righteq))

        
        self.wait(2)
        self.play(*[FadeOut(mob)for mob in self.mobjects])



        self.play(Restore(self.camera.frame))

        self.wait(1)

# ZERO PLACEMENT SCENE

        titlegraph = Title("Nullstellen-Verteilung").set_color(YELLOW_C)
        self.play(Write(titlegraph))
        
        textTs = Tex(   
                        "G(s) =",
                        "{\mu(s)",
                        "\\over",
                        "\\nu(s)}",
                        color=WHITE
                    )

        #textTs.shift(DOWN*2 + RIGHT*4)
        

        # self.play(  textTs[0].set_color, WHITE,
        #             textTs[1].set_color, WHITE,
        #             textTs[2].set_color, WHITE,
        #             textTs[3].set_color, ORANGE,
        #         )
		
        
        axes = Axes(**self.axes_kwargs).shift(DOWN*0.5).to_corner(LEFT)
        axes.add_coordinate_labels(font_size=20, num_decimal_places=0)

        x_label_tex = r"Re{ \{ s_{\nu} \} }"
        y_label_tex = r"Im{ \{ s_{\nu} \} }"

        labels = self.axis_labels = VGroup(
            axes.get_x_axis_label(x_label_tex).next_to(axes.x_axis.tip),
            axes.get_y_axis_label(y_label_tex).next_to(axes.y_axis.tip),
        )

        self.play(FadeIn(axes), FadeIn(labels))


        textTs.next_to(axes,RIGHT,buff=LARGE_BUFF*4)
        self.play(Write(textTs))
        self.play(FadeToColor(textTs[3],ORANGE))

        check = Checkmark().set_color(GREEN).next_to(textTs,LEFT,buff=LARGE_BUFF)
        ex = Exmark().set_color(RED).next_to(textTs,LEFT,buff=LARGE_BUFF)

        dot = Dot(color=ORANGE)
        dot2 = Dot(color=ORANGE)
        dot.move_to(axes.c2p(1, 0))
        dot2.move_to(axes.c2p(1, 0))
        self.play(FadeIn(dot, scale=0.5),Write(ex))
        self.play(FadeIn(dot2, scale=0.5))
        self.play(dot.animate.move_to(axes.c2p(2, 0)), dot2.animate.move_to(axes.c2p(2, 0)))
        self.wait()
        self.play(dot.animate.move_to(axes.c2p(-2, 0)), dot2.animate.move_to(axes.c2p(-2, 0)),Transform(ex,check))
        self.wait()
        self.play(dot.animate.move_to(axes.c2p(-1, 1)), dot2.animate.move_to(axes.c2p(-1, -1)))


        self.wait(3)
        self.play(*[FadeOut(mob)for mob in self.mobjects])


# STABILITY METHODS SCENE

        self.wait(1)

        methodtitle = Title("Stabilitätskriterien").set_color(YELLOW_C)
        self.play(Write(methodtitle))

        self.wait(1)

        methodlist = BulletedList(  r"\text{Routh-Hurwitz-Kriterium}",
                                    r"\text{Nyquist-Kriterium}",
                                    r"\dots",
                                    buff=1,math_mode=True).next_to(methodtitle,DOWN*3).to_corner(LEFT).shift(RIGHT)

        # self.play(Write(methodlist),run_time=8)
        for i in methodlist:
            self.play(Write(i),run_time=3)
        
        self.wait(3)

        self.play(FadeToColor(methodlist[0], GREEN))

        self.wait(5)
        self.play(*[FadeOut(mob)for mob in self.mobjects])

# FUNCTION FOR PLANT SCENE

    def get_text(self, strp):
        return Text(strp,font="Times New Roman")


"""
# HURWITZ MATRIX SCENE ( IS USED IN THIRD SCENE )

class Hurwitz(Scene):
    def construct(self):
                
        hmat = [ ["a_{n-1}","a_{n}","0","0","\\dots","\\dots"],
                 ["a_{n-3}","a_{n-2}","a_{n-1}","a_{n}","\\dots","\\dots"],
                 ["a_{n-5}","a_{n-4}","a_{n-3}","a_{n-2}","\\dots","\\dots"],
                 ["a_{n-7}","a_{n-6}","a_{n-5}","a_{n-4}","\\dots","\\dots"],
                 ["\\dots","\\dots","\\dots","\\dots","\\dots","a_2"],
                 ["0","0","\\dots","\\dots","0","a_0"]
                ]

        m = Matrix(hmat)
        self.add(m)

        mcount = 0
        while mcount<6:
            self.play(FadeToColor(m[0][mcount*7],RED))
            mcount+=1
"""