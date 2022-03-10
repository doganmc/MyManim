from distutils.errors import LibError
from matplotlib import mathtext
from manimlib import *
import numpy as np
import math

class RouthOpening(Scene):
    CONFIG = {"title_kwargs": {
                "color" : YELLOW_C, 
                "opacity" : 0.7, 
                "font" : ""}
            }

    def construct(self):
        intro_words = Text("Das Routh Schema", **self.title_kwargs)
        intro_words.set_color(YELLOW_C).scale(2)

        underline = Underline(mobject=intro_words)
        underline.set_color(YELLOW_C)

        self.play(Write(intro_words))

        self.play(ShowCreation(underline),run_time=1)

        self.wait(1)

        self.play(ShrinkToCenter(intro_words), ShrinkToCenter(underline))

        self.wait(1)

class RouthDefinition(Scene):
    CONFIG = {
		"list_kwargs": {
			"math_mode": True,
		}
	}
    def construct(self):
        
        tf = Tex(   
                        r"{H(s) =",
                        r"{ {b_0 s^m + b_1 s^{m-1} + \hdots + b_{m-1} s + b_m}",
                        r"\over",
                        r"{a_0 s^n + a_1 s^{n-1} + \hdots + a_{n-1} s + a_n} }",
                        r" = ",
                        r"{ {B(s)}",
                        r"\over",
                        r"{A(s)} }",
                        color=WHITE
                    )

        poly = Tex(   
                        r"{p(s) =",
                        r"{ ", r"a_n", r"s^n", r"+", r"a_{n-1}", r"s^{n-1}", r"+", r"\hdots", r"+", r"a_1", r"s", r"+", r"a_0", r"}", r"}",
                        #r"{a_0 s^n + a_1 s^{n-1} + \hdots + a_{n-1} s + {a_n} } }",
                        color=GREEN
                    )

        for i in tf:
            self.play(Write(i))
        # self.play(  tf[0].set_color, WHITE,
        #             tf[1].set_color, WHITE,
        #             tf[2].set_color, WHITE,
        #             tf[3].set_color, WHITE,
        #             tf[4].set_color, WHITE,
        #             tf[5].set_color, WHITE,
        #             tf[6].set_color, WHITE,
        #             tf[7].set_color, WHITE,
        #         )

        # self.play(  poly[0].set_color, WHITE,
        #             poly[1].set_color, WHITE,
        #         )

        #self.wait(1)
        #ApplyMethod(FadeToColor,tf[3],GREEN)

        self.play( FadeToColor(tf[3],GREEN), FadeToColor(tf[7],GREEN) )

        tf.generate_target()
        tf.target.shift(UP*2)
        self.play(MoveToTarget(tf))
        
        self.wait(1)

        play_kw = {"run_time": 2}
        self.play( TransformMatchingTex(tf,poly), **play_kw )

        poly.generate_target()
        poly.target.shift(UP*3 + RIGHT*2)
        self.play(MoveToTarget(poly))

        self.wait(1)

        self.play( FadeToColor(poly,WHITE) )

        condtitle = Text("Die notwendige Bedingung:").set_color(ORANGE).to_corner(UL).shift(DOWN*2.5)
        self.play(Write(condtitle))

        condlist = BulletedList(r"\text{Kein Polynomkoeffizient verschwindet.}",
                                r"\text{Alle Polynomkoeffizienten besitzen das gleiche Vorzeichen.}",
                                r"\text{Grad p(s)} \leq 2 \Longrightarrow \text{notwendig und hinreichend.}",
                                **self.list_kwargs
                                ).to_corner(DL).shift(UP)

        #Group(condtitle,condlist).to_corner(LEFT).scale(1).shift(UP)

        for i in condlist:
            self.play(Write(i))

        condbox = SurroundingRectangle(condlist, buff = .1).set_color(ORANGE) #.stretch_to_fit_height(4)
        self.play(ShowCreation(condbox))

        self.wait(2)

        self.play(TransformMatchingTex(poly,poly.set_color_by_tex_to_color_map({
                "a_0": RED,
                "a_1": RED,
                "a_n": RED,
                "a_{n-1}": RED,
        }),transform_mismatches=True),
                FadeToColor(condlist[0],RED) 
        )
        
        self.wait(2)

        self.play(TransformMatchingTex(poly,poly.set_color_by_tex_to_color_map({
                "+": YELLOW,
        }),transform_mismatches=True),
                FadeToColor(condlist[1],YELLOW) 
        )

        self.wait(2)

        self.play(TransformMatchingTex(poly,poly.set_color_by_tex_to_color_map({
                "s^n": BLUE,
        }),transform_mismatches=True),
                FadeToColor(condlist[2],BLUE) 
        )

        self.play(FadeOut(condbox), FadeOut(condlist), FadeOut(condtitle), FadeToColor(poly,WHITE))

        poly.generate_target()
        poly.target.move_to(ORIGIN)
        self.play(MoveToTarget(poly))


class ZickZack(Scene):
    def construct(self):

        zikzak = Text("Zick-Zack-Muster").set_color(ORANGE)
        self.play(Write(zikzak))

        zikzak.generate_target()
        zikzak.target.to_corner(UP)
        self.play(MoveToTarget(zikzak))

        polyzz = Tex(   
                        r"{p(s) =",
                        r"{ ", r"a_n", r"s^n", r"+", r"a_{n-1}", r"s^{n-1}", r"+", r"a_{n-2}", r"s^{n-2}", r"+" , r"a_{n-3}", r"s^{n-3}", r"+", r"a_{n-4}", r"s^{n-4}", r"+", r"a_{n-5}", r"s^{n-5}", r"+" r"\hdots", r"+", r"a_1", r"s", r"+", r"a_0", r"}", r"}",
                        color=WHITE
                    ).scale(0.7)
        polyzz.to_corner(LEFT).shift(UP*2)

        polyzz.set_color_by_tex_to_color_map({
                "a_n": BLUE,
                "a_{n-1}": BLUE,
                "a_{n-2}": YELLOW,
                "a_{n-3}": YELLOW,
                "a_{n-4}": PINK,
                "a_{n-5}": PINK,
                })

        self.play(Write(polyzz))

        self.wait(2)

        an = Tex(r"a_n").set_color(BLUE)
        nton1 = Arrow(UP,DOWN,buff=0)
        an1 = Tex(r"a_{n-1}").set_color(BLUE)
        n1ton2 = Arrow(DL,UR,buff=0)
        an2 = Tex(r"a_{n-2}").set_color(YELLOW)
        n2ton3 = Arrow(UP,DOWN,buff=0)
        an3 = Tex(r"a_{n-3}").set_color(YELLOW)
        n3ton4 = Arrow(DL,UR,buff=0)
        an4 = Tex(r"a_{n-4}").set_color(PINK)
        n4ton5 = Arrow(UP,DOWN,buff=0)
        an5 = Tex(r"a_{n-5}").set_color(PINK)
        n5ton6 = Arrow(DL,UR,buff=0)
        an6 = Tex(r"\hdots")
        n6ton7 = Arrow(UP,DOWN,buff=0)
        an7 = Tex(r"\hdots")

        an.shift(LEFT*5)
        #self.add(an)

        nton1.next_to(an,DOWN)
        #self.add(nton1)

        an1.next_to(nton1,DOWN)
        #self.add(an1)

        n1ton2.next_to(an1,UR)
        #self.add(n1ton2)

        an2.next_to(n1ton2,UR)
        #self.add(an2)

        n2ton3.next_to(an2,DOWN)
        #self.add(n2ton3)

        an3.next_to(n2ton3,DOWN)
        #self.add(an3)

        n3ton4.next_to(an3,UR)
        #self.add(n3ton4)

        an4.next_to(n3ton4,UR)
        #self.add(an4)

        n4ton5.next_to(an4,DOWN)
        #self.add(n4ton5)

        an5.next_to(n4ton5,DOWN)
        #self.add(an5)

        n5ton6.next_to(an5,UR)
        #self.add(n5ton6)

        an6.next_to(n5ton6,UR)
        #self.add(an6)

        n6ton7.next_to(an6,DOWN)

        an7.next_to(n6ton7,DOWN)
        #self.add(an7)

        zzgroup=VGroup(an,nton1,an1,n1ton2,an2,n2ton3,an3,n3ton4,an4,n4ton5,an5,n5ton6,an6,an7)
        
        play_kw = {"run_time": 4}
        self.play(Write(zzgroup),**play_kw)

        self.wait(1)

class FullTable(Scene):
    def construct(self):

        row1 = Tex(r"a_0",r"\hspace{0.25cm}",r"a_2",r"\hspace{0.25cm}",r"a_4",r"\hspace{0.25cm}",r"a_6",r"\hspace{0.25cm}",r"\hdots").shift(UP*3 + LEFT*4.5)
        row2 = Tex(r"a_1",r"\hspace{0.25cm}",r"a_3",r"\hspace{0.25cm}",r"a_5",r"\hspace{0.25cm}",r"a_7",r"\hspace{0.25cm}",r"\hdots").next_to(row1,DOWN*2)
        row3 = Tex(r"b_1",r"\hspace{0.25cm}",r"b_2",r"\hspace{0.25cm}",r"b_3",r"\hspace{0.25cm}",r"b_4",r"\hspace{0.25cm}",r"\hdots").next_to(row2,DOWN*2)
        row4 = Tex(r"c_1",r"\hspace{0.25cm}",r"c_2",r"\hspace{0.25cm}",r"c_3",r"\hspace{0.25cm}",r"c_4",r"\hspace{0.25cm}",r"\hdots").next_to(row3,DOWN*2)
        row5 = Tex(r"d_1",r"\hspace{0.25cm}",r"d_2",r"\hspace{0.25cm}",r"d_3",r"\hspace{0.25cm}",r"d_4",r"\hspace{0.25cm}",r"\hdots").next_to(row4,DOWN*2)
        row6 = Tex(r"\vdots",r"\hspace{0.25cm}",r"\vdots").next_to(row5,DOWN*2).shift(LEFT*1.5)
        #row7 = Tex(r"e_1",r"\hspace{0.25cm}",r"e_2").next_to(row6,DOWN*2)
        #row8 = Tex(r"f_1").next_to(row7[0],DOWN*2)
        #row9 = Tex(r"g_0").next_to(row8[0],DOWN*2)

        rowgr = VGroup(row1,row2,row3,row4,row5,row6)
        self.play(Write(rowgr))

        lineab = Line().set_color(GREEN).set_width(5)
        lineab.next_to(row2,DOWN)

        self.play(Write(lineab))

        rowgr.save_state()

        self.wait(1)

# show b1
        b1 = Tex(   
                        r"{b_1",
                        r"=",
                        r"{ {a_1 a_2 ",
                        r"-",
                        r"a_0 a_3}",
                        r"\over",
                        r"{a_1} } }",
                        color=WHITE
                    )

        b1.shift(RIGHT*3 + UP*3)
        self.play(Write(b1))

        b1.save_state()

        self.play(  row2[0].set_color, YELLOW,
                    row1[1].set_color, YELLOW,
                    row1[0].set_color, BLUE,
                    row2[1].set_color, BLUE,
                    row3[0].set_color, RED,
                )

        self.play(  b1[0].set_color, RED,
                    b1[1].set_color, WHITE,
                    b1[2].set_color, YELLOW,
                    b1[4].set_color, BLUE,
                    b1[5].set_color, WHITE,
                    b1[6].set_color, YELLOW,
                )

        self.wait(1)

        rowgr.restore()
        b1.restore()

# show b2
        b2 = Tex(   
                        r"{b_2",
                        r"=",
                        r"{ {a_1 a_4 ",
                        r"-",
                        r"a_0 a_5}",
                        r"\over",
                        r"{a_1} } }",
                        color=WHITE
                    )

        b2.next_to(b1,DOWN).shift(DOWN)
        self.play(Write(b2))

        b2.save_state()

        self.play(  row2[0].set_color, YELLOW,
                    row1[2].set_color, YELLOW,
                    row1[0].set_color, BLUE,
                    row2[2].set_color, BLUE,
                    row3[1].set_color, RED,
                )

        self.play(  b2[0].set_color, RED,
                    b2[1].set_color, WHITE,
                    b2[2].set_color, YELLOW,
                    b2[4].set_color, BLUE,
                    b2[5].set_color, WHITE,
                    b2[6].set_color, YELLOW,
                )

        self.wait(1)

        rowgr.restore()
        b2.restore()

#show b3
        b3 = Tex(   
                        r"{b_3",
                        r"=",
                        r"{ {a_1 a_6 ",
                        r"-",
                        r"a_0 a_7}",
                        r"\over",
                        r"{a_1} } }",
                        color=WHITE
                    )

        b3.next_to(b2,DOWN).shift(DOWN)
        self.play(Write(b3))

        b3.save_state()

        self.play(  row2[0].set_color, YELLOW,
                    row1[3].set_color, YELLOW,
                    row1[0].set_color, BLUE,
                    row2[3].set_color, BLUE,
                    row3[2].set_color, RED,
                )

        self.play(  b3[0].set_color, RED,
                    b3[1].set_color, WHITE,
                    b3[2].set_color, YELLOW,
                    b3[4].set_color, BLUE,
                    b3[5].set_color, WHITE,
                    b3[6].set_color, YELLOW,
                )

        self.wait(1)
        
        rowgr.restore()
        b3.restore()

        self.play(FadeOut(b1),FadeOut(b2),FadeOut(b3),FadeOut(lineab))

#show c1
        linebc = Line().set_color(GREEN).set_width(5)
        linebc.next_to(row3,DOWN)

        self.play(Write(linebc))

        c1 = Tex(   
                        r"{c_1",
                        r"=",
                        r"{ {b_1 a_3 ",
                        r"-",
                        r"a_1 b_2}",
                        r"\over",
                        r"{b_1} } }",
                        color=WHITE
                    )

        c1.shift(RIGHT*3 + UP*3)
        self.play(Write(c1))

        c1.save_state()

        self.play(  row2[1].set_color, YELLOW,
                    row3[0].set_color, YELLOW,
                    row2[0].set_color, BLUE,
                    row3[1].set_color, BLUE,
                    row4[0].set_color, RED,
                )

        self.play(  c1[0].set_color, RED,
                    c1[1].set_color, WHITE,
                    c1[2].set_color, YELLOW,
                    c1[4].set_color, BLUE,
                    c1[5].set_color, WHITE,
                    c1[6].set_color, YELLOW,
                )

        self.wait(1)

        rowgr.restore()
        c1.restore()

#show c2
        c2 = Tex(   
                        r"{c_2",
                        r"=",
                        r"{ {b_1 a_5 ",
                        r"-",
                        r"a_1 b_3}",
                        r"\over",
                        r"{b_1} } }",
                        color=WHITE
                    )

        c2.next_to(c1,DOWN).shift(DOWN)
        self.play(Write(c2))

        c2.save_state()

        self.play(  row2[2].set_color, YELLOW,
                    row3[0].set_color, YELLOW,
                    row2[0].set_color, BLUE,
                    row3[2].set_color, BLUE,
                    row4[1].set_color, RED,
                )

        self.play(  c2[0].set_color, RED,
                    c2[1].set_color, WHITE,
                    c2[2].set_color, YELLOW,
                    c2[4].set_color, BLUE,
                    c2[5].set_color, WHITE,
                    c2[6].set_color, YELLOW,
                )

        self.wait(1)

        rowgr.restore()
        c2.restore()

#show c3
        c3 = Tex(   
                        r"{c_3",
                        r"=",
                        r"{ {b_1 a_7 ",
                        r"-",
                        r"a_1 b_4}",
                        r"\over",
                        r"{b_1} } }",
                        color=WHITE
                    )

        c3.next_to(c2,DOWN).shift(DOWN)
        self.play(Write(c3))

        c3.save_state()

        self.play(  row2[3].set_color, YELLOW,
                    row3[0].set_color, YELLOW,
                    row2[0].set_color, BLUE,
                    row3[3].set_color, BLUE,
                    row4[2].set_color, RED,
                )

        self.play(  c3[0].set_color, RED,
                    c3[1].set_color, WHITE,
                    c3[2].set_color, YELLOW,
                    c3[4].set_color, BLUE,
                    c3[5].set_color, WHITE,
                    c3[6].set_color, YELLOW,
                )

        self.wait(1)

        rowgr.restore()
        c3.restore()

        self.play(FadeOut(c1),FadeOut(c2),FadeOut(c3),FadeOut(linebc))

#show d1
        linecd = Line().set_color(GREEN).set_width(5)
        linecd.next_to(row4,DOWN)

        self.play(Write(linecd))

        d1 = Tex(   
                        r"{d_1",
                        r"=",
                        r"{ {c_1 b_2 ",
                        r"-",
                        r"b_1 c_2}",
                        r"\over",
                        r"{c_1} } }",
                        color=WHITE
                    )

        d1.shift(RIGHT*3 + UP*3)
        self.play(Write(d1))

        d1.save_state()

        self.play(  row3[1].set_color, YELLOW,
                    row4[0].set_color, YELLOW,
                    row3[0].set_color, BLUE,
                    row4[1].set_color, BLUE,
                    row5[0].set_color, RED,
                )

        self.play(  d1[0].set_color, RED,
                    d1[1].set_color, WHITE,
                    d1[2].set_color, YELLOW,
                    d1[4].set_color, BLUE,
                    d1[5].set_color, WHITE,
                    d1[6].set_color, YELLOW,
                )

        self.wait(1)

        rowgr.restore()
        d1.restore()

#show d2
        d2 = Tex(   
                        r"{d_2",
                        r"=",
                        r"{ {c_1 b_3 ",
                        r"-",
                        r"b_1 c_3}",
                        r"\over",
                        r"{c_1} } }",
                        color=WHITE
                    )

        d2.next_to(d1,DOWN).shift(DOWN)
        self.play(Write(d2))

        d2.save_state()

        self.play(  row3[2].set_color, YELLOW,
                    row4[0].set_color, YELLOW,
                    row3[0].set_color, BLUE,
                    row4[2].set_color, BLUE,
                    row5[1].set_color, RED,
                )

        self.play(  d2[0].set_color, RED,
                    d2[1].set_color, WHITE,
                    d2[2].set_color, YELLOW,
                    d2[4].set_color, BLUE,
                    d2[5].set_color, WHITE,
                    d2[6].set_color, YELLOW,
                )

        self.wait(1)

        rowgr.restore()
        d2.restore()

        self.play(FadeOut(d1),FadeOut(d2),FadeOut(linecd))
