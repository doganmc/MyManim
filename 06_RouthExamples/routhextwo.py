from tkinter import N
from manimlib import *
import numpy as np

class routhext(Scene):
    def construct(self):

        title = Title("Aufgabe 2").set_color(YELLOW_C)

        poly1 = Tex(   
                        r"{p(s) =",
                        r"{ ",r"2", r"s^{5}", r"+", r"4" ,r"s^4", r"+", r"10", r"s^{3}", r"+",r"12", r"s^{2}", r"+", r"K", r"s", r"+", r"2", r"}", r"}",
                        color=WHITE
                    ).shift(UL*2)

        self.play( Write(title) )
        self.play( Write(poly1) )
        
        # for i in poly1:
        #     self.play(Write(i))

        self.wait(1)

        self.play( FadeToColor( poly1[1],BLUE ),FadeToColor( poly1[4],BLUE ) , FadeToColor( poly1[7],YELLOW ), FadeToColor( poly1[10],YELLOW ), FadeToColor( poly1[13],PINK ), FadeToColor( poly1[16],PINK ) )

        self.wait(1)

        an = poly1[1].copy()
        nton1 = Arrow(UP,DOWN,buff=0)
        an1 = poly1[4].copy()
        n1ton2 = Arrow(DL,UR,buff=0)
        an2 = poly1[7].copy()
        n2ton3 = Arrow(UP,DOWN,buff=0)
        an3 = poly1[10].copy()
        n3ton4 = Arrow(DL,UR,buff=0)
        an4 =  poly1[13].copy()
        n4ton5 = Arrow(UP,DOWN,buff=0)
        an5 = poly1[16].copy()
        n5ton6 = Arrow(DL,UR,buff=0)
        an6 = Tex(r"0")
        n6ton7 = Arrow(UP,DOWN,buff=0)
        an7 = Tex(r"0")

        an.shift(LEFT*5)
        nton1.next_to(an,DOWN)
        an1.next_to(nton1,DOWN)
        n1ton2.next_to(an1,UR)
        an2.next_to(n1ton2,UR)
        n2ton3.next_to(an2,DOWN)
        an3.next_to(n2ton3,DOWN)
        n3ton4.next_to(an3,UR)
        an4.next_to(n3ton4,UR)
        n4ton5.next_to(an4,DOWN)
        an5.next_to(n4ton5,DOWN)
        n5ton6.next_to(an5,UR)     
        an6.next_to(n5ton6,UR)
        n6ton7.next_to(an6,DOWN)
        an7.next_to(n6ton7,DOWN)

        zzgroup=VGroup(an,nton1,an1,n1ton2,an2,n2ton3,an3,n3ton4,an4,n4ton5,an5,n5ton6,an6,n6ton7,an7).shift(DOWN*2 + RIGHT*3)
        
        play_kw = {"run_time": 4}
        self.play(Write(zzgroup),**play_kw)

        self.wait(1)

        self.play(ShrinkToCenter(title), ShrinkToCenter(zzgroup))

        poly1.generate_target()
        poly1.target.scale(0.75).to_corner(UR)
        self.play(MoveToTarget(poly1))

        self.play(FadeToColor(poly1,WHITE))

        # row1 = Tex(r"1",r"\hspace{1cm}",r"3",r"\hspace{1cm}",r"5",r"\hspace{1cm}",r"a_1",r"\hspace{1cm}",r"\hdots").shift(UP*3 + LEFT*2)
        # row2 = Tex(r"2",r"\hspace{1cm}",r"4",r"\hspace{1cm}",r"0",r"\hspace{1cm}",r"a_0",r"\hspace{1cm}",r"\hdots").next_to(row1,DOWN*1.5)
        # row3 = Tex(r"b_1",r"\hspace{1cm}",r"b_2",r"\hspace{1cm}",r"b_3",r"\hspace{1cm}",r"b_4",r"\hspace{1cm}",r"\hdots").next_to(row2,DOWN*1.5)
        # row4 = Tex(r"c_1",r"\hspace{1cm}",r"c_2",r"\hspace{1cm}",r"c_3",r"\hspace{1cm}",r"c_4",r"\hspace{1cm}",r"\hdots").next_to(row3,DOWN*1.5)
        # row5 = Tex(r"d_1",r"\hspace{1cm}",r"d_2",r"\hspace{1cm}",r"d_3",r"\hspace{1cm}",r"d_4",r"\hspace{1cm}",r"\hdots").next_to(row4,DOWN*1.5)
        # row6 = Tex(r"\vdots",r"\hspace{1cm}",r"\vdots").next_to(row5,DOWN*1.5).shift(LEFT*1.25)        

        # col1 = Tex(r"a_7",r"\\",r"a_6",r"\\",r"b_1",r"\\",r"c_1",r"\\",r"d_1").shift(UP*1.55 + LEFT*5.5)
        # col2 = Tex(r"a_5",r"\\",r"a_4",r"\\",r"b_2",r"\\",r"c_2",r"\\",r"d_2").next_to(col1,RIGHT*4.5)
        # col3 = Tex(r"a_3",r"\\",r"a_2",r"\\",r"b_3",r"\\",r"c_3",r"\\",r"d_3").next_to(col2,RIGHT*4.5)
        # col4 = Tex(r"a_1",r"\\",r"a_0",r"\\",r"b_4",r"\\",r"c_4",r"\\",r"d_4").next_to(col3,RIGHT*4.5)

        # colt1 = Tex(r"a_7",r"\\",r"a_6",r"\\",r"b_1",r"\\",r"c_1",r"\\",r"d_1").shift(UP*1.55 + LEFT*5.5)
        # colt2 = Tex(r"a_5",r"\\",r"a_4",r"\\",r"b_2",r"\\",r"c_2",r"\\",r"d_2").next_to(col1,RIGHT*4.5)
        # colt3 = Tex(r"a_3",r"\\",r"a_2",r"\\",r"b_3",r"\\",r"c_3",r"\\",r"d_3").next_to(col2,RIGHT*4.5)
        # colt4 = Tex(r"a_1",r"\\",r"a_0",r"\\",r"b_4",r"\\",r"c_4",r"\\",r"d_4").next_to(col3,RIGHT*4.5)

        col1 = Tex(r"2",r"\\",r"4",r"\\",r"b_1",r"\\",r"c_1",r"\\",r"d_1",r"\\",r"e_1").shift(UP*1.55 + LEFT*5.5)
        col2 = Tex(r"10",r"\\",r"12",r"\\",r"b_2",r"\\",r"c_2",r"\\",r"d_2",r"\\",r"e_2").next_to(col1,RIGHT*4.5)
        col3 = Tex(r"K",r"\\",r"2",r"\\",r"b_3",r"\\",r"c_3",r"\\",r"d_3",r"\\",r"e_3").next_to(col2,RIGHT*4.5)
        col4 = Tex(r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0").next_to(col3,RIGHT*4.5)

        # SAME MATRIX FOR COLUMN TRACKERS:

        colt1 = Tex(r"a_5",r"\\",r"a_4",r"\\",r"b_1",r"\\",r"c_1",r"\\",r"d_1",r"\\",r"e_1").shift(UP*1.55 + LEFT*5.5)
        colt2 = Tex(r"a_3",r"\\",r"a_2",r"\\",r"b_2",r"\\",r"c_2",r"\\",r"d_2",r"\\",r"e_2").next_to(col1,RIGHT*4.5)
        colt3 = Tex(r"a_1",r"\\",r"a_0",r"\\",r"b_3",r"\\",r"c_3",r"\\",r"d_3",r"\\",r"e_3").next_to(col2,RIGHT*4.5)
        colt4 = Tex(r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0").next_to(col3,RIGHT*4.5)

        colgr = VGroup(col1,col2,col3,col4)
        coltgr = VGroup(colt1,colt2,colt3,colt4).set_color(RED_C)

        cols = Tex(r"s^5", r"\\", r"s^4", r"\\", r"s^3", r"\\", r"s^2", r"\\", r"s^1", r"\\", r"s^0" ).scale(0.9).next_to(col1,LEFT*1.5).set_color(TEAL_D)
        
        self.play(Write(coltgr))
        self.wait(2)
        self.play(FadeOut(coltgr))

        self.play(Write(col1[0:2]), Write(col2[0:2]), Write(col3[0:2]), Write(col4[0:6]))

        #colpoly = VGroup(col1[0:2], col2[0:2], col3[0:2], col4[0:6])
        #self.play(Transform(coltgr,colpoly))
        
        #self.add(coltgr)
        #self.add(colgr)

        # self.add(col1[0:2], col2[0:2], col3[0:2], col4[0:6])
        # self.add(cols)

        colgr.save_state()

        self.wait(1)
        self.play(Write(cols))
        self.wait(2)

        #rectb = SurroundingRectangle(rowgr[0:2]).set_color(WHITE).set_stroke(opacity=0.5).stretch_to_fit_height(1.5)
        rectver = SurroundingRectangle( col1[0:2] ).set_color(ORANGE)
        recthor = SurroundingRectangle( col2[0:2] ).set_color(GREEN)
        rectelem = SurroundingRectangle( col1[2] ).set_color(RED)
        
        self.play( ShowCreation(rectver), ShowCreation(recthor), ShowCreation(rectelem) ) 

        n_line = NumberLine(
        x_min=-5,  x_max=14,
        tick_frequency=1,
        unit_size=1,
        include_numbers=True,
        numbers_to_show=np.arange(-5,1,5),
        )

        n_line.shift( DOWN*2.5).scale(0.7)
        self.play( ShowCreation(n_line) )

        vertline = DashedLine(start=DOWN,end=UP).set_opacity(0.3).move_to(n_line.n2p(0))
        self.play( ShowCreation(vertline) )

        self.wait(1)

######## SHOW b1

        b1 = Tex(   
                        r"{b_1",
                        r"=",
                        r"{ {4 \cdot 10 ",
                        r"-",
                        r"2 \cdot 12}",
                        r"\over",
                        r"{4} } }",
                        r"=",
                        r"4",
                        color=WHITE
                )

        b1.shift(RIGHT*3.5 + UP*1.5)
        self.play(Write(b1))
        b1.save_state()

        self.play(  col1[1].set_color, YELLOW,
                    col2[0].set_color, YELLOW,
                    col1[0].set_color, BLUE,
                    col2[1].set_color, BLUE,
                )

        self.play(  b1[0].set_color, RED,
                b1[1].set_color, WHITE,
                b1[2].set_color, YELLOW,
                b1[4].set_color, BLUE,
                b1[5].set_color, WHITE,
                b1[6].set_color, YELLOW,
                b1[7].set_color, WHITE,
                b1[8].set_color, RED,
                )

        self.wait(1)

        b1m = b1[8].copy().move_to(col1[2],ORIGIN)
        b1p = (4*10 - 2*12)/4
        self.play(TransformFromCopy(b1[8], b1m))

        dotb1 = Dot(color=RED)
        dotb1.move_to(n_line.n2p(0))
        self.play(FadeIn(dotb1, scale=0.5))
        self.play( dotb1.animate.move_to(n_line.n2p(b1p)) )
    

        colgr.restore()
        b1.restore()
        self.play(FadeToColor(b1m,WHITE))

        # checkmark = Checkmark().next_to(n_line,UP)
        # exmark = Exmark()
        # checkmark.set_color(GREEN)
        # exmark.set_color(RED_C).next_to(n_line,UP)
        # hp = Text("HP").set_color(GREEN).next_to(checkmark,RIGHT)
        # nohp = Text("kein HP").set_color(RED_C).next_to(exmark,RIGHT)
        # self.play(Write(checkmark), Write(hp))
        self.wait(1)

######## SHOW b2 and b3

        recthor.generate_target()
        recthor.target.become( SurroundingRectangle( col3[0:2] ).set_color(GREEN) )

        rectelem.generate_target()
        rectelem.target.become( SurroundingRectangle( col2[2] ).set_color(RED) )

        self.play(MoveToTarget(recthor),MoveToTarget(rectelem))

        b2 = Tex(   
                        r"{b_2",
                        r"=",
                        r"{ {4 \cdot K ",
                        r"-",
                        r"2 \cdot 2}",
                        r"\over",
                        r"{4} } }",
                        r"=",
                        r"K-1",
                        color=WHITE
                )

        b2.next_to(b1,DOWN).shift(DOWN+RIGHT*0.25)
        self.play(Write(b2))
        b2.save_state()

        self.play(  col1[0].set_color, YELLOW,
                    col3[1].set_color, YELLOW,
                    col1[1].set_color, BLUE,
                    col3[0].set_color, BLUE,
                )

        self.play(  b2[0].set_color, RED,
                b2[1].set_color, WHITE,
                b2[2].set_color, YELLOW,
                b2[4].set_color, BLUE,
                b2[5].set_color, WHITE,
                b2[6].set_color, YELLOW,
                b2[7].set_color, WHITE,
                b2[8].set_color, RED,
                )

        self.wait(1)

        b2m = b2[8].copy().scale(0.5).move_to(col2[2],ORIGIN)
        self.play(TransformFromCopy(b2[8], b2m))


        colgr.restore()
        b2.restore()
        self.play(FadeToColor(b2m,WHITE))

        self.play(FadeOut(b1),FadeOut(b2))


        recthor.generate_target()
        recthor.target.become( SurroundingRectangle( col4[0:2] ).set_color(GREEN) )

        rectelem.generate_target()
        rectelem.target.become( SurroundingRectangle( col3[2] ).set_color(RED) )

        self.play(MoveToTarget(recthor),MoveToTarget(rectelem))

        b3m = Tex(r"0").move_to(col3[2],ORIGIN)
        self.play(Write(b3m))
        self.wait(1)

######## SHOW c1

        rectver.generate_target()
        rectver.target.become( SurroundingRectangle( col1[1:3] ).set_color(ORANGE) )

        recthor.generate_target()
        recthor.target.become( SurroundingRectangle( col2[1:3] ).set_color(GREEN) )

        rectelem.generate_target()
        rectelem.target.become( SurroundingRectangle( col1[3] ).set_color(RED) )

        self.play(MoveToTarget(rectver),MoveToTarget(recthor),MoveToTarget(rectelem))

        c1 = Tex(   
                        r"{c_1",
                        r"=",
                        r"{ {4 \cdot 12 ",
                        r"-",
                        r"4 \cdot (K-1)}",
                        r"\over",
                        r"{4} } }",
                        r"=",
                        r"13-K",
                        color=WHITE
                )

        c1.shift(RIGHT*3.5 + UP*1.5)
        self.play(Write(c1))

        c1.save_state()

        self.play(  b1m.set_color, YELLOW,
                    col2[1].set_color, YELLOW,
                    col1[1].set_color, BLUE,
                    b2m.set_color, BLUE,
                )

        self.play(  c1[0].set_color, RED,
                c1[1].set_color, WHITE,
                c1[2].set_color, YELLOW,
                c1[4].set_color, BLUE,
                c1[5].set_color, WHITE,
                c1[6].set_color, YELLOW,
                c1[7].set_color, WHITE,
                c1[8].set_color, RED,
                )

        self.wait(1)

        c1m = c1[8].copy().scale(0.5).move_to(col1[3],ORIGIN)
        self.play(TransformFromCopy(c1[8], c1m))
        
        colgr.restore()
        c1.restore()
        self.play(FadeToColor(c1m,WHITE), FadeToColor(b1m,WHITE), FadeToColor(b2m,WHITE) )
        self.wait(1)

######## SHOW c2 and c3

        recthor.generate_target()
        recthor.target.become( SurroundingRectangle( col3[1:3] ).set_color(GREEN) )

        rectelem.generate_target()
        rectelem.target.become( SurroundingRectangle( col2[3] ).set_color(RED) )

        self.play(MoveToTarget(recthor),MoveToTarget(rectelem))

        c2 = Tex(   
                        r"{c_2",
                        r"=",
                        r"{ {4 \cdot 2",
                        r"-",
                        r"4 \cdot 0}",
                        r"\over",
                        r"{4} } }",
                        r"=",
                        r"2",
                        color=WHITE
                )

        c2.next_to(c1,DOWN).shift(DOWN + LEFT*0.5)
        self.play(Write(c2))
        c2.save_state()

        self.play(  b1m.set_color, YELLOW,
                    col3[1].set_color, YELLOW,
                    col1[1].set_color, BLUE,
                    b3m.set_color, BLUE,
                )

        self.play(  c2[0].set_color, RED,
                c2[1].set_color, WHITE,
                c2[2].set_color, YELLOW,
                c2[4].set_color, BLUE,
                c2[5].set_color, WHITE,
                c2[6].set_color, YELLOW,
                c2[7].set_color, WHITE,
                c2[8].set_color, RED,
                )

        c2m = c2[8].copy().move_to(col2[3],ORIGIN)
        self.play(TransformFromCopy(c2[8], c2m))

        self.wait(1)

        colgr.restore()
        c2.restore()
        self.play(FadeToColor(c1m,WHITE), FadeToColor(b1m,WHITE), FadeToColor(b2m,WHITE), FadeToColor(b3m,WHITE), FadeToColor(c1m,WHITE), FadeToColor(c2m,WHITE) )
        self.play(FadeOut(c1),FadeOut(c2))


        recthor.generate_target()
        recthor.target.become( SurroundingRectangle( col4[1:3] ).set_color(GREEN) )

        rectelem.generate_target()
        rectelem.target.become( SurroundingRectangle( col3[3] ).set_color(RED) )

        self.play(MoveToTarget(recthor),MoveToTarget(rectelem))

        c3m = Tex(r"0").move_to(col3[3],ORIGIN)
        self.play(Write(c3m))
        self.wait(1)

####### SHOW d1

        # rectb.generate_target()
        # rectb.target.become( SurroundingRectangle(rowgr[2:4]).set_color(WHITE).set_stroke(opacity=0.5).stretch_to_fit_height(1.5) )

        rectver.generate_target()
        rectver.target.become( SurroundingRectangle( col1[2:4] ).set_color(ORANGE) )

        recthor.generate_target()
        recthor.target.become( SurroundingRectangle( col2[2:4] ).set_color(GREEN) )

        rectelem.generate_target()
        rectelem.target.become( SurroundingRectangle( col1[4] ).set_color(RED) )

        self.play(MoveToTarget(rectver),MoveToTarget(recthor),MoveToTarget(rectelem))

        d1 = Tex(   
                        r"{d_1",
                        r"=",
                        r"{ {(13-K) \cdot (K-1) ",
                        r"-",
                        r"4 \cdot 2}",
                        r"\over",
                        r"{(13-K)} } }",
                        r"=",
                        r"-\frac{K^2 - 14K + 21}{13-K}",
                        color=WHITE
                ).scale(0.5)

        d1.shift(RIGHT*3.5 + UP*1.5)
        self.play(Write(d1))
        d1.save_state()

        self.play(  c1m.set_color, YELLOW,
                    b2m.set_color, YELLOW,
                    b1m.set_color, BLUE,
                    c2m.set_color, BLUE,
                )

        self.play(  d1[0].set_color, RED,
                d1[1].set_color, WHITE,
                d1[2].set_color, YELLOW,
                d1[4].set_color, BLUE,
                d1[5].set_color, WHITE,
                d1[6].set_color, YELLOW,
                d1[7].set_color, WHITE,
                d1[8].set_color, RED,
                )

        d1m = d1[8].copy().scale(0.5).move_to(col1[4],ORIGIN)
        self.play(TransformFromCopy(d1[8], d1m))

        self.wait(1)

        colgr.restore()
        d1.restore()
        self.play(FadeToColor(c1m,WHITE), FadeToColor(c2m,WHITE), FadeToColor(b1m,WHITE), FadeToColor(b2m,WHITE),FadeToColor(b3m,WHITE), FadeToColor(c1m,WHITE), FadeToColor(d1m,WHITE) )
        self.wait(1)

####### SHOW d2 and d3

        recthor.generate_target()
        recthor.target.become( SurroundingRectangle( col3[2:4] ).set_color(GREEN) )

        rectelem.generate_target()
        rectelem.target.become( SurroundingRectangle( col2[4] ).set_color(RED) )

        self.play(MoveToTarget(recthor),MoveToTarget(rectelem))

        d2 = Tex(   
                        r"{d_2",
                        r"=",
                        r"{ {(13-K) \cdot 0 ",
                        r"-",
                        r"4 \cdot 0}",
                        r"\over",
                        r"{(13-K)} } }",
                        r"=",
                        r"0",
                        color=WHITE
                )

        d2.next_to(d1,DOWN).shift(DOWN)
        self.play(Write(d2))
        d2.save_state()

        self.play(  c1m.set_color, YELLOW,
                    b3m.set_color, YELLOW,
                    b1m.set_color, BLUE,
                    c3m.set_color, BLUE,
                )

        self.play(  d2[0].set_color, RED,
                d2[1].set_color, WHITE,
                d2[2].set_color, YELLOW,
                d2[4].set_color, BLUE,
                d2[5].set_color, WHITE,
                d2[6].set_color, YELLOW,
                d2[7].set_color, WHITE,
                d2[8].set_color, RED,
                )

        d2m = d2[8].copy().move_to(col2[4],ORIGIN)
        self.play(TransformFromCopy(d2[8], d2m))

        self.wait(1)

        colgr.restore()
        d2.restore()
        self.play(FadeToColor(c1m,WHITE), FadeToColor(b1m,WHITE), FadeToColor(b2m,WHITE), FadeToColor(b3m,WHITE), FadeToColor(c1m,WHITE), FadeToColor(c2m,WHITE), FadeToColor(c3m,WHITE), FadeToColor(d1m,WHITE), FadeToColor(d2m,WHITE) )
        self.play(FadeOut(d1),FadeOut(d2))


        recthor.generate_target()
        recthor.target.become( SurroundingRectangle( col4[2:4] ).set_color(GREEN) )

        rectelem.generate_target()
        rectelem.target.become( SurroundingRectangle( col3[4] ).set_color(RED) )

        self.play(MoveToTarget(recthor),MoveToTarget(rectelem))

        d3m = Tex(r"0").move_to(col3[4],ORIGIN)
        self.play(Write(d3m))        
        
####### SHOW e1

        rectver.generate_target()
        rectver.target.become( SurroundingRectangle( col1[3:5] ).set_color(ORANGE) )

        recthor.generate_target()
        recthor.target.become( SurroundingRectangle( col2[3:5] ).set_color(GREEN) )

        rectelem.generate_target()
        rectelem.target.become( SurroundingRectangle( col1[5] ).set_color(RED) )

        self.play(MoveToTarget(rectver),MoveToTarget(recthor),MoveToTarget(rectelem))

        e1 = Tex(   
                        r"{e_1",
                        r"=",
                        r"{ {(-\frac{K^2 - 14K + 21}{13-K}) \cdot (2) ",
                        r"-",
                        r"(13-K) \cdot 0}",
                        r"\over",
                        r"{-\frac{K^2 - 14K + 21}{13-K}} } }",
                        r"=",
                        r"2",
                        color=WHITE
                ).scale(0.5)

        e1.shift(RIGHT*3.5 + UP*1.5)
        self.play(Write(e1))
        e1.save_state()

        self.play(  d1m.set_color, YELLOW,
                    c2m.set_color, YELLOW,
                    c1m.set_color, BLUE,
                    d2m.set_color, BLUE,
                )

        self.play(  e1[0].set_color, RED,
                e1[1].set_color, WHITE,
                e1[2].set_color, YELLOW,
                e1[4].set_color, BLUE,
                e1[5].set_color, WHITE,
                e1[6].set_color, YELLOW,
                e1[7].set_color, WHITE,
                e1[8].set_color, RED,
                )

        e1m = e1[8].copy().scale(2).move_to(col1[5],ORIGIN)
        self.play(TransformFromCopy(e1[8], e1m))

        e1.restore()
        self.play(FadeOut(e1))
        self.play(FadeToColor(d1m,WHITE), FadeToColor(d2m,WHITE), FadeToColor(c1m,WHITE), FadeToColor(c2m,WHITE), FadeToColor(e1m,WHITE) )

        self.wait(1)   
     
####### SHOW e2 and e3

        recthor.generate_target()
        recthor.target.become( SurroundingRectangle( col3[3:5] ).set_color(GREEN) )

        rectelem.generate_target()
        rectelem.target.become( SurroundingRectangle( col2[5] ).set_color(RED) )

        self.play(MoveToTarget(recthor),MoveToTarget(rectelem))

        e2m = Tex(r"0").move_to(col2[5],ORIGIN)
        self.play(Write(e2m))

        recthor.generate_target()
        recthor.target.become( SurroundingRectangle( col4[3:5] ).set_color(GREEN) )

        rectelem.generate_target()
        rectelem.target.become( SurroundingRectangle( col3[5] ).set_color(RED) )      
 
        self.play(MoveToTarget(recthor),MoveToTarget(rectelem))

        e3m = Tex(r"0").move_to(col3[5],ORIGIN)
        self.play(Write(e3m))

        self.wait(2)

        self.play(FadeOut(rectver), FadeOut(recthor), FadeOut(rectelem))

        rootrect = SurroundingRectangle(col1).stretch_to_fit_width(1)

        self.play(ShowCreation(rootrect))

        expl1 = Text("p(s) ist HP, wenn:").shift(UP*2+RIGHT*3).set_color(YELLOW)

        cond1 = Tex(r"-\frac{-K^2 - 14K + 21}{13-K}",r">",r"0").next_to(expl1,DOWN*1.5)

        expl2 = Text("und").next_to(cond1,DOWN*1.5).set_color(YELLOW)
        
        cond2 = Tex(r"13-K",r">",r"0").next_to(expl2,DOWN*1.5)

        expl3 = Text("gelten.").next_to(cond2,DOWN*1.5)

        self.play(Write(expl1), Write(cond1), Write(expl2), Write(cond2),Write(expl3))

        condfull = VGroup(expl1,cond1,expl2,cond2,expl3)
        #self.play(Write(condfull))

        condres = Tex(r"1.71",r"<",r"K",r"<",r"12.29",r"\\",r"\Longrightarrow",r"\text{p(s) ist HP}").shift(UP*2+RIGHT*3)
        condres[0].set_color(YELLOW)
        condres[4].set_color(BLUE)
        condres[6].set_color(GREEN)

        self.wait(3)

        self.play(FadeTransform(condfull,condres))

        dotk1 = Dot(color=YELLOW)
        dotk1.move_to(n_line.n2p(0))
        self.play(FadeIn(dotk1, scale=0.5))
        self.play( dotk1.animate.move_to(n_line.n2p(1.71)) )

        dotk2 = Dot(color=BLUE)
        dotk2.move_to(n_line.n2p(0))
        self.play(FadeIn(dotk2, scale=0.5))
        self.play( dotk2.animate.move_to(n_line.n2p(12.29)) )

        #kline = DashedLine(get_center(dotk1),end=RIGHT).get_center()     #.set_color(GREEN).set_opacity(0.3).move_to(n_line.n2p(7))
        
        kline = Line(start=dotk1, end=dotk2).set_color(GREEN).set_opacity(0.5)

        self.play( ShowCreation(kline) )

        kber = Brace(kline, direction=UP, color=GREEN)
        self.play(ShowCreation(kber))
        ktext = Text("Stabilitätsbereich für K").next_to(kber,UP).set_color(GREEN)
        self.play(Write(ktext))


        self.wait(3)
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        self.wait(3)

        # #self.wait(1)
"""
        col1rect = SurroundingRectangle(col1).set_color(ORANGE)
        self.play(ShowCreation(col1rect))

        self.wait(1)

        rootrect = SurroundingRectangle(c1m).set_opacity(0.25).set_color(RED)
        self.play(ShowCreation(rootrect))

                
        textexp = Tex(r"\text{Ein Polynomkoeffizient des p(s) liegen}", r"\\", r"\text{in der linken Halbebene,}", r"\\", r"\text{ $\Longrightarrow$ p(s) ist kein Hurwitzpolynom.}").shift(RIGHT*3.5 + UP*1.5).scale(0.7)
        self.play(Write(textexp))

        self.wait(3)
        self.play(*[FadeOut(mob)for mob in self.mobjects])
        self.wait(3)

        # textexp2 = Tex(r"\text{Hurwitzdeterminante ergibt sich ", r"\\", r"\text{die Nullstellen des p(s)}" ).shift(RIGHT*3.5 + UP*1.5).scale(0.7)
        # self.play(Write(textexp2))
"""
