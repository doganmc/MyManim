from manimlib import *
import numpy as np

class routhex1(Scene):
    def construct(self):

        title = Title("Aufgabe 1").set_color(YELLOW_C)

        poly1 = Tex(   
                        r"{p(s) =",
                        r"{ ", r"1" ,r"s^4", r"+", r"2", r"s^{3}", r"+",r"3", r"s^{2}", r"+", r"4", r"s", r"+", r"5", r"}", r"}",
                        color=WHITE
                    ).shift(UL*2)

        self.play(Write(title))

        self.play( Write(poly1[0]) )

        i=2
        while i < 14:
            self.play( Write(poly1[i]),run_time=0.25 )
            if i == 13:
                break
            i+=1

        self.wait(1.5)
        self.play( FadeIn( poly1[1].set_color(BLUE) ) )
        self.wait(1.5)

        self.play( FadeToColor( poly1[4],BLUE ), FadeToColor( poly1[7],YELLOW ), FadeToColor( poly1[10],YELLOW ), FadeToColor( poly1[13],PINK ) )

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
        an5 = Tex(r"?").set_color(PINK)
        # n5ton6 = Arrow(DL,UR,buff=0)
        # an6 = Tex(r"\hdots")
        # n6ton7 = Arrow(UP,DOWN,buff=0)
        # an7 = Tex(r"\hdots")

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

        # n5ton6.next_to(an5,UR)
        # #self.add(n5ton6)

        # an6.next_to(n5ton6,UR)
        # #self.add(an6)

        # n6ton7.next_to(an6,DOWN)

        # an7.next_to(n6ton7,DOWN)
        # #self.add(an7)

        zzgroup=VGroup(an,nton1,an1,n1ton2,an2,n2ton3,an3,n3ton4,an4,n4ton5,an5).shift(DOWN*2 + RIGHT*3) #,n5ton6,an6,an7)
        
        play_kw = {"run_time": 4}
        self.play(Write(zzgroup),**play_kw)

        self.wait(1)

        an5.generate_target()
        an5.target.become( Tex(r"0").set_color(PINK).next_to(n4ton5,DOWN) )
        self.play(MoveToTarget(an5))

        self.wait(1)

        self.play(ShrinkToCenter(title), ShrinkToCenter(zzgroup))

        poly1.generate_target()
        poly1.target.to_corner(UR)
        self.play(MoveToTarget(poly1))

        self.play(FadeToColor(poly1,WHITE))

        row1 = Tex(r"1",r"\hspace{1cm}",r"3",r"\hspace{1cm}",r"5",r"\hspace{1cm}",r"a_1",r"\hspace{1cm}",r"\hdots").shift(UP*3 + LEFT*2)
        row2 = Tex(r"2",r"\hspace{1cm}",r"4",r"\hspace{1cm}",r"0",r"\hspace{1cm}",r"a_0",r"\hspace{1cm}",r"\hdots").next_to(row1,DOWN*1.5)
        row3 = Tex(r"b_1",r"\hspace{1cm}",r"b_2",r"\hspace{1cm}",r"b_3",r"\hspace{1cm}",r"b_4",r"\hspace{1cm}",r"\hdots").next_to(row2,DOWN*1.5)
        row4 = Tex(r"c_1",r"\hspace{1cm}",r"c_2",r"\hspace{1cm}",r"c_3",r"\hspace{1cm}",r"c_4",r"\hspace{1cm}",r"\hdots").next_to(row3,DOWN*1.5)
        row5 = Tex(r"d_1",r"\hspace{1cm}",r"d_2",r"\hspace{1cm}",r"d_3",r"\hspace{1cm}",r"d_4",r"\hspace{1cm}",r"\hdots").next_to(row4,DOWN*1.5)
        row6 = Tex(r"\vdots",r"\hspace{1cm}",r"\vdots").next_to(row5,DOWN*1.5).shift(LEFT*1.25)

        # SAME MATRIX FOR COLUMN TRACKERS:

        col1 = Tex(r"a_7",r"\\",r"a_6",r"\\",r"b_1",r"\\",r"c_1",r"\\",r"d_1").shift(UP*1.55 + LEFT*5.5)
        col2 = Tex(r"a_5",r"\\",r"a_4",r"\\",r"b_2",r"\\",r"c_2",r"\\",r"d_2").next_to(col1,RIGHT*4.5)
        col3 = Tex(r"a_3",r"\\",r"a_2",r"\\",r"b_3",r"\\",r"c_3",r"\\",r"d_3").next_to(col2,RIGHT*4.5)
        col4 = Tex(r"a_1",r"\\",r"a_0",r"\\",r"b_4",r"\\",r"c_4",r"\\",r"d_4").next_to(col3,RIGHT*4.5)

        cols = Tex(r"s^4", r"\\", r"s^3", r"\\", r"s^2", r"\\", r"s^1", r"\\", r"s^0" ).next_to(col1,LEFT*1.5).set_color(TEAL_D)

        colgr = VGroup(col1,col2,col3,col4).set_color(RED).set_opacity(0.35)
        rowgr = VGroup(row1,row2,row3,row4,row5,row6)

        trrow = VGroup( row1[0:3],row2[0:3] )

        self.play(Write(trrow))
        self.wait(1)
        self.play(Write(cols))
        self.wait(2)

        #self.play(Write(rowgr))
        #self.add(colgr)

        rowgr.save_state()

        #rectb = SurroundingRectangle(rowgr[0:2]).set_color(WHITE).set_stroke(opacity=0.5).stretch_to_fit_height(1.5)
        rectver = SurroundingRectangle( col1[0:2] ).set_color(ORANGE)
        recthor = SurroundingRectangle( col2[0:2] ).set_color(GREEN)
        rectelem = SurroundingRectangle( col1[2] ).set_color(RED).stretch_to_fit_height(0.5)
        
        #self.play(Write(col1[4].set_color(RED)))
        self.play(ShowCreation(rectver), ShowCreation(recthor), ShowCreation(rectelem) ) 

        n_line = NumberLine(
        x_min=-6,  x_max=6,
        tick_frequency=1,
        unit_size=1,
        include_numbers=True,
        numbers_to_show=np.arange(-5,1,5),
        )

        n_line.shift(LEFT*2 + DOWN*2.5).scale(0.7)
        self.play( ShowCreation(n_line) )

        vertline = DashedLine(start=DOWN,end=UP).set_opacity(0.3).move_to(n_line.n2p(0))
        self.play( ShowCreation(vertline) )
        self.wait(1)

        # SHOW b1

        b1 = Tex(   
                        r"{b_1",
                        r"=",
                        r"{ {2 \cdot 3 ",
                        r"-",
                        r"4 \cdot 1}",
                        r"\over",
                        r"{2} } }",
                        r"=",
                        r"1",
                        color=WHITE
                )

        b1.shift(RIGHT*3.5 + UP*1.5)
        #b1.move_to(row3[0],ORIGIN)
        self.play(Write(b1))

        b1.save_state()

        self.play(  row2[0].set_color, YELLOW,
                row1[1].set_color, YELLOW,
                row1[0].set_color, BLUE,
                row2[1].set_color, BLUE,
                #row3[0].set_color, RED,
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
        self.play(TransformFromCopy(b1[8], b1m))

        dotb1 = Dot(color=RED)
        dotb1.move_to(n_line.n2p(0))
        self.play(FadeIn(dotb1, scale=0.5))
        self.play( dotb1.animate.move_to(n_line.n2p(1)) )
    

        rowgr.restore()
        b1.restore()
        self.play(FadeToColor(b1m,WHITE))

        checkmark = Checkmark().next_to(n_line,UP)
        exmark = Exmark()
        checkmark.set_color(GREEN)
        exmark.set_color(RED_C).next_to(n_line,UP)
        hp = Text("HP").set_color(GREEN).next_to(checkmark,RIGHT)
        nohp = Text("kein HP").set_color(RED_C).next_to(exmark,RIGHT)
        self.play(Write(checkmark), Write(hp))
        self.wait(1)

        # SHOW b2

        recthor.generate_target()
        recthor.target.become( SurroundingRectangle( col3[0:2] ).set_color(GREEN) )

        rectelem.generate_target()
        rectelem.target.become( SurroundingRectangle( col2[2] ).set_color(RED).stretch_to_fit_height(0.5) )

        self.play(MoveToTarget(recthor),MoveToTarget(rectelem))

        b2 = Tex(   
                        r"{b_2",
                        r"=",
                        r"{ {2 \cdot 5 ",
                        r"-",
                        r"1 \cdot 0}",
                        r"\over",
                        r"{2} } }",
                        r"=",
                        r"5",
                        color=WHITE
                )

        b2.next_to(b1,DOWN).shift(DOWN)
        self.play(Write(b2))

        b2.save_state()

        self.play(  row2[0].set_color, YELLOW,
                row1[2].set_color, YELLOW,
                row1[0].set_color, BLUE,
                row2[2].set_color, BLUE,
                #row3[1].set_color, RED,
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

        b2m = b2[8].copy().move_to(col2[2],ORIGIN)
        self.play(TransformFromCopy(b2[8], b2m))

        # dotb2 = Dot(color=RED)
        # dotb2.move_to(n_line.n2p(-5))
        # self.play(FadeIn(dotb2, scale=0.5))

        rowgr.restore()
        b2.restore()
        self.play(FadeToColor(b2m,WHITE))

        self.play(FadeOut(b1),FadeOut(b2))

        b3m = Tex(r"0").move_to(col3[2],ORIGIN)
        self.play(Write(b3m))
        self.wait(1)

        #SHOW c1

        # rectb.generate_target()
        # rectb.target.become( SurroundingRectangle(rowgr[1:3]).set_color(WHITE).set_stroke(opacity=0.5).stretch_to_fit_height(1.5) )

        rectver.generate_target()
        rectver.target.become( SurroundingRectangle( col1[1:3] ).set_color(ORANGE) )

        recthor.generate_target()
        recthor.target.become( SurroundingRectangle( col2[1:3] ).set_color(GREEN) )

        rectelem.generate_target()
        rectelem.target.become( SurroundingRectangle( col1[3] ).set_color(RED).stretch_to_fit_height(0.5) )

        self.play(MoveToTarget(rectver),MoveToTarget(recthor),MoveToTarget(rectelem))

        c1 = Tex(   
                        r"{c_1",
                        r"=",
                        r"{ {1 \cdot 4 ",
                        r"-",
                        r"2 \cdot 5}",
                        r"\over",
                        r"{1} } }",
                        r"=",
                        r"-6",
                        color=WHITE
                )

        c1.shift(RIGHT*3.5 + UP*1.5)
        self.play(Write(c1))

        c1.save_state()

        self.play(  row2[1].set_color, YELLOW,
                b1m.set_color, YELLOW,
                row2[0].set_color, BLUE,
                b2m.set_color, BLUE,
                #row4[0].set_color, RED,
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

        c1m = c1[8].copy().move_to(col1[3],ORIGIN)
        self.play(TransformFromCopy(c1[8], c1m))

        dotc1 = Dot(color=RED)
        dotc1.move_to(n_line.n2p(0))
        self.play(FadeIn(dotc1, scale=0.5))
        self.play( dotc1.animate.move_to(n_line.n2p(-6)), FadeTransform(checkmark,exmark), FadeTransform(hp,nohp) )
        

        rowgr.restore()
        c1.restore()
        self.play(FadeToColor(c1m,WHITE), FadeToColor(b1m,WHITE), FadeToColor(b2m,WHITE) )
        self.wait(1)

        #SHOW c2

        recthor.generate_target()
        recthor.target.become( SurroundingRectangle( col3[1:3] ).set_color(GREEN) )

        rectelem.generate_target()
        rectelem.target.become( SurroundingRectangle( col2[3] ).set_color(RED).stretch_to_fit_height(0.5) )

        self.play(MoveToTarget(recthor),MoveToTarget(rectelem))

        c2 = Tex(   
                        r"{c_2",
                        r"=",
                        r"{ {1 \cdot 0 ",
                        r"-",
                        r"2 \cdot 0}",
                        r"\over",
                        r"{1} } }",
                        r"=",
                        r"0",
                        color=WHITE
                )

        c2.next_to(c1,DOWN).shift(DOWN)
        self.play(Write(c2))

        c2.save_state()

        self.play(  row2[2].set_color, YELLOW,
                b1m.set_color, YELLOW,
                row2[0].set_color, BLUE,
                b2m.set_color, BLUE,
                #c1m.set_color, RED,
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

        rowgr.restore()
        c2.restore()
        self.play(FadeToColor(c1m,WHITE), FadeToColor(b1m,WHITE), FadeToColor(b2m,WHITE), FadeToColor(c1m,WHITE), FadeToColor(c2m,WHITE) )
        self.play(FadeOut(c1),FadeOut(c2))

        c3m = Tex(r"0").move_to(col3[3],ORIGIN)
        self.play(Write(c3m))
        self.wait(1)

        #SHOW d1

        # rectb.generate_target()
        # rectb.target.become( SurroundingRectangle(rowgr[2:4]).set_color(WHITE).set_stroke(opacity=0.5).stretch_to_fit_height(1.5) )

        rectver.generate_target()
        rectver.target.become( SurroundingRectangle( col1[2:4] ).set_color(ORANGE) )

        recthor.generate_target()
        recthor.target.become( SurroundingRectangle( col2[2:4] ).set_color(GREEN) )

        rectelem.generate_target()
        rectelem.target.become( SurroundingRectangle( col1[4] ).set_color(RED).stretch_to_fit_height(0.5) )

        self.play(MoveToTarget(rectver),MoveToTarget(recthor),MoveToTarget(rectelem))

        d1 = Tex(   
                        r"{d_1",
                        r"=",
                        r"{ {(-6) \cdot 5 ",
                        r"-",
                        r"1 \cdot 0}",
                        r"\over",
                        r"{(-6)} } }",
                        r"=",
                        r"5",
                        color=WHITE
                )

        d1.shift(RIGHT*3.5 + UP*1.5)
        self.play(Write(d1))

        d1.save_state()

        self.play(  b2m.set_color, YELLOW,
                c1m.set_color, YELLOW,
                b1m.set_color, BLUE,
                c1m.set_color, BLUE,
                #row5[0].set_color, RED,
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

        d1m = d1[8].copy().move_to(col1[4],ORIGIN)
        self.play(TransformFromCopy(d1[8], d1m))

        dotd1 = Dot(color=RED)
        dotd1.move_to(n_line.n2p(0))
        self.play(FadeIn(dotd1, scale=0.5))
        self.play( dotd1.animate.move_to(n_line.n2p(5)) )
        

        self.wait(1)

        rowgr.restore()
        d1.restore()
        self.play(FadeToColor(c1m,WHITE), FadeToColor(b1m,WHITE), FadeToColor(b2m,WHITE), FadeToColor(c1m,WHITE), FadeToColor(c2m,WHITE), FadeToColor(d1m,WHITE) )
        self.wait(1)

        #SHOW d2

        recthor.generate_target()
        recthor.target.become( SurroundingRectangle( col3[2:4] ).set_color(GREEN) )

        rectelem.generate_target()
        rectelem.target.become( SurroundingRectangle( col2[4] ).set_color(RED).stretch_to_fit_height(0.5) )

        self.play(MoveToTarget(recthor),MoveToTarget(rectelem))

        d2 = Tex(   
                        r"{d_2",
                        r"=",
                        r"{ {(-6) \cdot 0 ",
                        r"-",
                        r"1 \cdot 0}",
                        r"\over",
                        r"{(-6)} } }",
                        r"=",
                        r"0",
                        color=WHITE
                )

        d2.next_to(d1,DOWN).shift(DOWN)
        self.play(Write(d2))

        d2.save_state()

        self.play(  b2m.set_color, YELLOW,
                c1m.set_color, YELLOW,
                b1m.set_color, BLUE,
                c3m.set_color, BLUE,
                #row5[1].set_color, RED,
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

        rowgr.restore()
        d2.restore()
        self.play(FadeToColor(c1m,WHITE), FadeToColor(b1m,WHITE), FadeToColor(b2m,WHITE), FadeToColor(c1m,WHITE), FadeToColor(c2m,WHITE), FadeToColor(c3m,WHITE), FadeToColor(d1m,WHITE), FadeToColor(d2m,WHITE) )
        self.play(FadeOut(d1),FadeOut(d2))
        self.play(FadeOut(rectver), FadeOut(recthor), FadeOut(rectelem))

        self.wait(1)

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
