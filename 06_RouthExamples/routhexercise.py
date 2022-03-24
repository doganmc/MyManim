from manimlib import *
import numpy as np

class shiftin(Scene):
        def construct(self):
                
                row1 = Tex(r"a_7",r"\hspace{0.25cm}",r"a_5",r"\hspace{0.25cm}",r"a_3",r"\hspace{0.25cm}",r"a_1",r"\hspace{0.25cm}",r"\hdots").shift(UP*3 + LEFT*4.5)
                row2 = Tex(r"a_6",r"\hspace{0.25cm}",r"a_4",r"\hspace{0.25cm}",r"a_2",r"\hspace{0.25cm}",r"a_0",r"\hspace{0.25cm}",r"\hdots").next_to(row1,DOWN*1.5)
                row3 = Tex(r"b_1",r"\hspace{0.25cm}",r"b_2",r"\hspace{0.25cm}",r"b_3",r"\hspace{0.25cm}",r"b_4",r"\hspace{0.25cm}",r"\hdots").next_to(row2,DOWN*1.5)
                row4 = Tex(r"c_1",r"\hspace{0.25cm}",r"c_2",r"\hspace{0.25cm}",r"c_3",r"\hspace{0.25cm}",r"c_4",r"\hspace{0.25cm}",r"\hdots").next_to(row3,DOWN*1.5)
                row5 = Tex(r"d_1",r"\hspace{0.25cm}",r"d_2",r"\hspace{0.25cm}",r"d_3",r"\hspace{0.25cm}",r"d_4",r"\hspace{0.25cm}",r"\hdots").next_to(row4,DOWN*1.5)
                row6 = Tex(r"\vdots",r"\hspace{0.5cm}",r"\vdots").next_to(row5,DOWN*1.5).shift(LEFT*1.25)

                # SAME MATRIX FOR COLUMN TRACKERS:

                col1 = Tex(r"a_7",r"\\",r"a_6",r"\\",r"b_1",r"\\",r"c_1",r"\\",r"d_1").shift(UP*1.55 + LEFT*6.15)
                col2 = Tex(r"a_5",r"\\",r"a_4",r"\\",r"b_2",r"\\",r"c_2",r"\\",r"d_2").next_to(col1,RIGHT*1.5)
                col3 = Tex(r"a_3",r"\\",r"a_2",r"\\",r"b_3",r"\\",r"c_3",r"\\",r"d_3").next_to(col2,RIGHT*1.5)
                col4 = Tex(r"a_1",r"\\",r"a_0",r"\\",r"b_4",r"\\",r"c_4",r"\\",r"d_4").next_to(col3,RIGHT*1.5)

                colgr = VGroup(col1,col2,col3,col4).set_color(RED).set_opacity(0.5)
                rowgr = VGroup(row1,row2,row3,row4,row5,row6)

                self.play(Write(rowgr))
                #self.add(colgr)
                
                rowgr.save_state()

                rectb = SurroundingRectangle(rowgr[0:2]).set_color(WHITE).set_stroke(opacity=0.5).stretch_to_fit_height(1.5)
                rectver = SurroundingRectangle( col1[0:2] ).set_color(ORANGE)
                recthor = SurroundingRectangle( col2[0:2] ).set_color(GREEN)
                rectelem = SurroundingRectangle( row3[0] ).set_color(RED).stretch_to_fit_height(0.5)

                # self.add(rectb)
                # self.add(rectver)
                # self.add(recthor)
                # self.add(rectelem)
                
                self.wait(2)

                self.play(ShowCreation(rectb), ShowCreation(rectver), ShowCreation(recthor), ShowCreation(rectelem) ) 


                n_line = NumberLine(
                x_min=-3,  x_max=3,
                tick_frequency=1,
                unit_size=1,
                include_numbers=True,
                numbers_to_show=np.arange(-3,1,3),
                )

                n_line.shift(LEFT*3 + DOWN*2.5)
                self.play( ShowCreation(n_line) )

                vertline = DashedLine(start=DOWN,end=UP).set_opacity(0.3).move_to(n_line.n2p(0))
                self.play( ShowCreation(vertline) )

                tdots1 = Tex(r"\hdots").set_opacity(0.5).next_to(n_line,RIGHT).shift(UP*0.1)
                tdots2 = Tex(r"\hdots").set_opacity(0.5).next_to(n_line,LEFT).shift(UP*0.1)
 
                self.play(ShowCreation(tdots1),ShowCreation(tdots2))

                self.wait(2)
        # SHOW b1

                b1 = Tex(   
                                r"{b_1",
                                r"=",
                                r"{ {a_6 a_5 ",
                                r"-",
                                r"a_7 a_4}",
                                r"\over",
                                r"{a_6} } }",
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

                hdet = Brace(b1, direction=DOWN, color=MAROON_B)
                self.play(ShowCreation(hdet))
                htext = Text("Hurwitz-Determinante").next_to(hdet,DOWN).set_color(MAROON_B)
                self.play(Write(htext))

                self.wait(2)

                self.play(FadeOut(hdet),FadeOut(htext))

                rowgr.restore()
                b1.restore()
                self.wait(1)


        # SHOW b2

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col3[0:2] ).set_color(GREEN) )

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( row3[1] ).set_color(RED).stretch_to_fit_height(0.5) )

                self.play(MoveToTarget(recthor),MoveToTarget(rectelem))

                b2 = Tex(   
                                r"{b_2",
                                r"=",
                                r"{ {a_6 a_3 ",
                                r"-",
                                r"a_7 a_2}",
                                r"\over",
                                r"{a_6} } }",
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
                self.wait(1)

        #SHOW b3

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col4[0:2] ).set_color(GREEN) )

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( row3[2] ).set_color(RED).stretch_to_fit_height(0.5) )

                self.play(MoveToTarget(recthor),MoveToTarget(rectelem))

                b3 = Tex(   
                                r"{b_3",
                                r"=",
                                r"{ {a_6 a_1 ",
                                r"-",
                                r"a_7 a_0}",
                                r"\over",
                                r"{a_6} } }",
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

                self.play(FadeOut(b1),FadeOut(b2),FadeOut(b3))
                self.wait(1)

        #SHOW c1

                rectb.generate_target()
                rectb.target.become( SurroundingRectangle(rowgr[1:3]).set_color(WHITE).set_stroke(opacity=0.5).stretch_to_fit_height(1.5) )

                rectver.generate_target()
                rectver.target.become( SurroundingRectangle( col1[1:3] ).set_color(ORANGE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col2[1:3] ).set_color(GREEN) )

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( row4[0] ).set_color(RED).stretch_to_fit_height(0.5) )

                self.play(MoveToTarget(rectb),MoveToTarget(rectver),MoveToTarget(recthor),MoveToTarget(rectelem))

                c1 = Tex(   
                                r"{c_1",
                                r"=",
                                r"{ {b_1 a_4 ",
                                r"-",
                                r"a_6 b_2}",
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
                self.wait(1)

        #SHOW c2

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col3[1:3] ).set_color(GREEN) )

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( row4[1] ).set_color(RED).stretch_to_fit_height(0.5) )

                self.play(MoveToTarget(recthor),MoveToTarget(rectelem))

                c2 = Tex(   
                                r"{c_2",
                                r"=",
                                r"{ {b_1 a_2 ",
                                r"-",
                                r"a_6 b_3}",
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
                self.wait(1)

        #SHOW c3

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col4[1:3] ).set_color(GREEN) )

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( row4[2] ).set_color(RED).stretch_to_fit_height(0.5) )

                self.play(MoveToTarget(recthor),MoveToTarget(rectelem))

                c3 = Tex(   
                                r"{c_3",
                                r"=",
                                r"{ {b_1 a_0 ",
                                r"-",
                                r"a_6 b_4}",
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

                self.play(FadeOut(c1),FadeOut(c2),FadeOut(c3))
                self.wait(1)

        #SHOW d1

                rectb.generate_target()
                rectb.target.become( SurroundingRectangle(rowgr[2:4]).set_color(WHITE).set_stroke(opacity=0.5).stretch_to_fit_height(1.5) )

                rectver.generate_target()
                rectver.target.become( SurroundingRectangle( col1[2:4] ).set_color(ORANGE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col2[2:4] ).set_color(GREEN) )

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( row5[0] ).set_color(RED).stretch_to_fit_height(0.5) )

                self.play(MoveToTarget(rectb),MoveToTarget(rectver),MoveToTarget(recthor),MoveToTarget(rectelem))

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
                self.wait(1)

        #SHOW d2

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col3[2:4] ).set_color(GREEN) )

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( row5[1] ).set_color(RED).stretch_to_fit_height(0.5) )

                self.play(MoveToTarget(recthor),MoveToTarget(rectelem))

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
                self.wait(1)

        #SHOW d3

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col4[2:4] ).set_color(GREEN) )

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( row5[2] ).set_color(RED).stretch_to_fit_height(0.5) )

                self.play(MoveToTarget(recthor),MoveToTarget(rectelem))

                d3 = Tex(   
                                r"{d_3",
                                r"=",
                                r"{ {c_1 b_4 ",
                                r"-",
                                r"b_1 c_4}",
                                r"\over",
                                r"{c_1} } }",
                                color=WHITE
                        )

                d3.next_to(d2,DOWN).shift(DOWN)
                self.play(Write(d3))

                d3.save_state()

                self.play(  row3[3].set_color, YELLOW,
                        row4[0].set_color, YELLOW,
                        row3[0].set_color, BLUE,
                        row4[3].set_color, BLUE,
                        row5[2].set_color, RED,
                        )

                self.play(  d3[0].set_color, RED,
                        d3[1].set_color, WHITE,
                        d3[2].set_color, YELLOW,
                        d3[4].set_color, BLUE,
                        d3[5].set_color, WHITE,
                        d3[6].set_color, YELLOW,
                        )

                self.wait(1)

                rowgr.restore()
                d3.restore()

                self.play(FadeOut(d1),FadeOut(d2),FadeOut(d3))

                self.play(FadeOut(rectb), FadeOut(rectver), FadeOut(recthor), FadeOut(rectelem) ) 

                self.wait(2)

        #SHOW THE COEFFICIENTS

                firstcol1 = Tex(r"a_{7}",r">",r"0")
                firstcol2 = Tex(r"a_{6}",r">",r"0").next_to(firstcol1,DOWN*2)
                firstcol3 = Tex(r"b_1",r">",r"0").next_to(firstcol2,DOWN*2).set_color(RED)
                firstcol4 = Tex(r"c_1",r">",r"0").next_to(firstcol3,DOWN*2).set_color(RED)
                firstcol5 = Tex(r"d_1",r">",r"0").next_to(firstcol4,DOWN*2).set_color(RED)
                firstcol6 = Tex(r"\vdots").next_to(firstcol5,DOWN*2)

                firstcols = VGroup(firstcol1,firstcol2,firstcol3,firstcol4,firstcol5,firstcol6).shift(UP*3 + RIGHT*3)

                ruf1 = Tex(r"!").next_to(firstcol1[1],UP,buff=0)
                ruf2 = Tex(r"!").next_to(firstcol2[1],UP,buff=0)
                ruf3 = Tex(r"!").next_to(firstcol3[1],UP,buff=0).set_color(RED)
                ruf4 = Tex(r"!").next_to(firstcol4[1],UP,buff=0).set_color(RED)
                ruf5 = Tex(r"!").next_to(firstcol5[1],UP,buff=0).set_color(RED)

                rufs = VGroup(ruf1,ruf2,ruf3,ruf4,ruf5)

                self.play(Write(firstcols),Write(rufs))
                self.wait(1)

                dotb1 = Dot(color=RED)
                dotc1 = Dot(color=RED)
                dotd1 = Dot(color=RED)

                dotb1.move_to(n_line.n2p(0.5))
                dotc1.move_to(n_line.n2p(2.5))
                dotd1.move_to(n_line.n2p(1.5))


                self.play(FadeIn(dotb1, scale=0.5), FadeIn(dotc1, scale=0.5), FadeIn(dotd1, scale=0.5) )

                b1x = firstcol3[0].copy().next_to(dotb1,DOWN,buff=0).scale(0.5).set_color(RED)
                c1x = firstcol4[0].copy().next_to(dotc1,DOWN,buff=0).scale(0.5).set_color(RED)
                d1x = firstcol5[0].copy().next_to(dotd1,DOWN,buff=0).scale(0.5).set_color(RED)

                self.play(Write(b1x), Write(c1x), Write(d1x))

                checkmark = Checkmark().next_to(n_line,UP)
                exmark = Exmark()
                checkmark.set_color(GREEN)
                exmark.set_color(RED_C).next_to(n_line,UP)
                hp = Text("HP").set_color(GREEN).next_to(checkmark,RIGHT)
                nohp = Text("kein HP").set_color(RED_C).next_to(exmark,RIGHT)
                #exmark.next_to(checkmark, ORIGIN)
                self.play(Write(checkmark), Write(hp))

                self.play( dotb1.animate.move_to(n_line.n2p(2))   , MaintainPositionRelativeTo(b1x,dotb1) )
                self.play( dotc1.animate.move_to(n_line.n2p(0.7)) , MaintainPositionRelativeTo(c1x,dotc1) ) 
                self.play( dotd1.animate.move_to(n_line.n2p(1))   , MaintainPositionRelativeTo(d1x,dotd1) )

                self.play( dotb1.animate.move_to(n_line.n2p(0.3))   , MaintainPositionRelativeTo(b1x,dotb1) )
                self.play( dotc1.animate.move_to(n_line.n2p(1.3)) , MaintainPositionRelativeTo(c1x,dotc1) ) 
                self.play( dotd1.animate.move_to(n_line.n2p(3))   , MaintainPositionRelativeTo(d1x,dotd1) )

                self.play( dotb1.animate.move_to(n_line.n2p(1.4))   , MaintainPositionRelativeTo(b1x,dotb1) )
                self.play( dotc1.animate.move_to(n_line.n2p(-0.4)) , MaintainPositionRelativeTo(c1x,dotc1), FadeTransform(checkmark,exmark), FadeTransform(hp,nohp) ) 
                self.play( dotd1.animate.move_to(n_line.n2p(2.5))   , MaintainPositionRelativeTo(d1x,dotd1) )
                self.play( dotc1.animate.move_to(n_line.n2p(0.4)) , MaintainPositionRelativeTo(c1x,dotc1), FadeTransform(exmark,checkmark), FadeTransform(nohp,hp) ) 

                self.wait(5)

                self.play(*[FadeOut(mob)for mob in self.mobjects])

                self.wait(2)
###########################
                # recthor.generate_target()
                # recthor.target.become( SurroundingRectangle( col3[0:2] ).set_color(GREEN) )
                # #self.play(MoveToTarget(recthor))

                # rectelem.generate_target()
                # rectelem.target.become( SurroundingRectangle( row3[1] ).set_color(RED).stretch_to_fit_height(0.5) )
                # self.play(MoveToTarget(recthor),MoveToTarget(rectelem))

                # recthor.generate_target()
                # recthor.target.become( SurroundingRectangle( col4[0:2] ).set_color(GREEN) )
                # #self.play(MoveToTarget(recthor))

                # rectelem.generate_target()
                # rectelem.target.become( SurroundingRectangle( row3[2] ).set_color(RED).stretch_to_fit_height(0.5) )
                # self.play(MoveToTarget(recthor),MoveToTarget(rectelem))




###################
class deneme(Scene):
        def construct(self):

                n_line = NumberLine(
                x_min=-3,  x_max=3,
                tick_frequency=1,
                unit_size=1,
                include_numbers=True,
                numbers_to_show=np.arange(-3,1,3),
                )

                #n_line.shift(LEFT*3 + DOWN*2.5)
                self.play( ShowCreation(n_line) )

                firstcol1 = Tex(r"a_{7}",r">",r"0")
                firstcol2 = Tex(r"a_{6}",r">",r"0").next_to(firstcol1,DOWN*2)
                firstcol3 = Tex(r"b_1",r">",r"0").next_to(firstcol2,DOWN*2).set_color(RED)
                firstcol4 = Tex(r"c_1",r">",r"0").next_to(firstcol3,DOWN*2).set_color(RED)
                firstcol5 = Tex(r"d_1",r">",r"0").next_to(firstcol4,DOWN*2).set_color(RED)
                firstcol6 = Tex(r"\vdots").next_to(firstcol5,DOWN*2)

                dotb1 = Dot(color=RED)
                dotc1 = Dot(color=RED)
                dotd1 = Dot(color=RED)

                dotb1.move_to(n_line.n2p(0.5))
                dotc1.move_to(n_line.n2p(2.5))
                dotd1.move_to(n_line.n2p(1.5))

                self.play(FadeIn(dotb1, scale=0.5), FadeIn(dotc1, scale=0.5), FadeIn(dotd1, scale=0.5) )


                b1x = firstcol3[0].copy().next_to(dotb1,DOWN,buff=0).scale(0.5).set_color(RED)
                c1x = firstcol4[0].copy().next_to(dotc1,DOWN,buff=0).scale(0.5).set_color(RED)
                d1x = firstcol5[0].copy().next_to(dotd1,DOWN,buff=0).scale(0.5).set_color(RED)


                self.play(Write(b1x), Write(c1x), Write(d1x))

##############
                checkmark = Checkmark().next_to(n_line,UP)
                exmark = Exmark()
                checkmark.set_color(GREEN)
                exmark.set_color(RED_C).next_to(n_line,UP)
                hp = Text("HP").set_color(GREEN).next_to(checkmark,RIGHT)
                nohp = Text("kein HP").set_color(RED_C).next_to(exmark,RIGHT)
                #exmark.next_to(checkmark, ORIGIN)
                self.play(Write(checkmark), Write(hp))

                self.play( dotb1.animate.move_to(n_line.n2p(2))   , MaintainPositionRelativeTo(b1x,dotb1) )
                self.play( dotc1.animate.move_to(n_line.n2p(0.7)) , MaintainPositionRelativeTo(c1x,dotc1) ) 
                self.play( dotd1.animate.move_to(n_line.n2p(1))   , MaintainPositionRelativeTo(d1x,dotd1) )

                self.play( dotb1.animate.move_to(n_line.n2p(0.3))   , MaintainPositionRelativeTo(b1x,dotb1) )
                self.play( dotc1.animate.move_to(n_line.n2p(1.3)) , MaintainPositionRelativeTo(c1x,dotc1) ) 
                self.play( dotd1.animate.move_to(n_line.n2p(3))   , MaintainPositionRelativeTo(d1x,dotd1) )

                self.play( dotb1.animate.move_to(n_line.n2p(1.4))   , MaintainPositionRelativeTo(b1x,dotb1) )
                self.play( dotc1.animate.move_to(n_line.n2p(-0.4)) , MaintainPositionRelativeTo(c1x,dotc1), FadeTransform(checkmark,exmark), FadeTransform(hp,nohp) ) 
                self.play( dotd1.animate.move_to(n_line.n2p(2.5))   , MaintainPositionRelativeTo(d1x,dotd1) )
                self.play( dotc1.animate.move_to(n_line.n2p(0.4)) , MaintainPositionRelativeTo(c1x,dotc1), FadeTransform(exmark,checkmark), FadeTransform(nohp,hp) ) 
################
