from manimlib import *
import numpy as np

class Example3K(Scene):
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
                "include_ticks": True,
                "include_numbers": False,
			},
            "x_axis_config": {
                "include_tip": True,
            }
		}
	}

        def construct(self):


                self.wait(2)

                intro_words2 = Text("Beispiel 3 mit reellem Parameter K",font="Times New Roman").scale(2)
                intro_words2.set_color(YELLOW_C)

                underline2 = Underline(mobject=intro_words2)
                underline2.set_color(YELLOW_C)

                self.play(Write(intro_words2))

                self.play(ShowCreation(underline2),run_time=1)

                self.wait(2)

                self.play(ShrinkToCenter(intro_words2), ShrinkToCenter(underline2))

                self.wait(1)


                poly1 = Tex(   
                                r"{p(s) =",
                                r"{ ", r"1", r"s^{3}", r"+", r"K" ,r"s^2", r"+", r"5", r"s", r"+",r"10", r"}", r"}",
                                color=WHITE
                        ).to_corner(UP)

                self.play( Write(poly1) )

                
                self.play(FocusOn(poly1[4]))
                self.wait(1)
                self.play(Indicate(poly1[4],color=RED))
                
                # for i in poly1:
                #     self.play(Write(i))

                #self.play(FadeIn(poly1[1]))
                #self.play( FadeToColor( poly1[1],BLUE ),FadeToColor( poly1[4],BLUE ) , FadeToColor( poly1[7],YELLOW ), FadeToColor( poly1[10],YELLOW ) )



                row1 = Tex(r"a_3",r"\hspace{0.25cm}",r"a_1",r"\hspace{0.25cm}",r"0",r"\hspace{0.25cm}",r"a_1",r"\hspace{0.25cm}",r"\hdots").shift(UP*3 + LEFT*4.5)
                row2 = Tex(r"a_2",r"\hspace{0.25cm}",r"a_0",r"\hspace{0.25cm}",r"0",r"\hspace{0.25cm}",r"a_0",r"\hspace{0.25cm}",r"\hdots").next_to(row1,DOWN*1.5)
                row3 = Tex(r"b_1",r"\hspace{0.25cm}",r"b_2",r"\hspace{0.25cm}",r"b_3",r"\hspace{0.25cm}",r"b_4",r"\hspace{0.25cm}",r"\hdots").next_to(row2,DOWN*1.5)
                row4 = Tex(r"c_1",r"\hspace{0.25cm}",r"c_2",r"\hspace{0.25cm}",r"c_3",r"\hspace{0.25cm}",r"c_4",r"\hspace{0.25cm}",r"\hdots").next_to(row3,DOWN*1.5)
                row5 = Tex(r"d_1",r"\hspace{0.25cm}",r"d_2",r"\hspace{0.25cm}",r"d_3",r"\hspace{0.25cm}",r"d_4",r"\hspace{0.25cm}",r"\hdots").next_to(row4,DOWN*1.5)
                row6 = Tex(r"\vdots",r"\hspace{0.5cm}",r"\vdots").next_to(row5,DOWN*1.5).shift(LEFT*1.25)

                # SAME MATRIX FOR COLUMN TRACKERS:

                col1 = Tex(r"1",r"\\",r"K",r"\\",r"\hspace{0.5cm} 5-5K/2",r"\\",r"10")#.shift(UP*1.55 + LEFT*6.15)
                col2 = Tex(r"5",r"\\",r"10",r"\\",r"0",r"\\",r"0")#.next_to(col1,RIGHT*1.5)
                col3 = Tex(r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0")#.next_to(col2,RIGHT*1.5)
                # col2 = Tex(r"a_1",r"\\",r"a_0",r"\\",r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0")#.next_to(col3,RIGHT*1.5)
                # col3 = Tex(r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0")

                colt1 = Tex(r"a_3",r"\\",r"\\",r"a_2",r"\\",r"\\",r"b_1",r"\\",r"\\",r"c_1",r"\\",r"\\",r"d_1")#.shift(UP*1.55 + LEFT*6.15)
                colt2 = Tex(r"a_1",r"\\",r"\\",r"a_0",r"\\",r"\\",r"b_2",r"\\",r"\\",r"c_2",r"\\",r"\\",r"d_2")#.next_to(col1,RIGHT*1.5)
                colt3 = Tex(r"0",r"\\",r"\\",r"0",r"\\",r"\\",r"b_3",r"\\",r"\\",r"c_3",r"\\",r"\\",r"d_3")#.next_to(col2,RIGHT*1.5)
                colt4 = Tex(r"a_1",r"\\",r"\\",r"a_0",r"\\",r"\\",r"b_4",r"\\",r"\\",r"c_4",r"\\",r"\\",r"d_4")#.next_to(col3,RIGHT*1.5)
                colt5 = Tex(r"0",r"\\",r"\\",r"0",r"\\",r"\\",r"0",r"\\",r"\\",r"0",r"\\",r"\\",r"0")
                coltgr = VGroup(colt1,colt2,colt3,colt4,colt5).arrange(RIGHT,buff=LARGE_BUFF*2)

                # col1 = Tex(r"a_3",r"\\",r"\\",r"a_2",r"\\",r"\\",r"?",r"\\",r"\\",r"?",r"\\",r"\\",r"?")#.shift(UP*1.55 + LEFT*6.15)
                # col2 = Tex(r"a_1",r"\\",r"\\",r"a_0",r"\\",r"\\",r"?",r"\\",r"\\",r"?",r"\\",r"\\",r"?")#.next_to(col1,RIGHT*1.5)
                # col3 = Tex(r"0",r"\\",r"\\",r"0",r"\\",r"\\",r"?",r"\\",r"\\",r"?",r"\\",r"\\",r"?")#.next_to(col2,RIGHT*1.5)
                # col2 = Tex(r"a_1",r"\\",r"\\",r"a_0",r"\\",r"\\",r"?",r"\\",r"\\",r"?",r"\\",r"\\",r"?")#.next_to(col3,RIGHT*1.5)
                # col3 = Tex(r"0",r"\\",r"\\",r"0",r"\\",r"\\",r"0",r"\\",r"\\",r"0",r"\\",r"\\",r"0")
                
                #col1[1].scale(0.7)
                col1[2].scale(0.7)
                col1[2].shift(RIGHT)
                #col1[2] = "\frac{5\cdot(2-K)}{(-K)}"

                colgr = VGroup(col1,col2,col3).arrange(RIGHT,buff=LARGE_BUFF*2)  #.set_color(RED).set_opacity(0.5)
                rowgr = VGroup(row1,row2,row3,row4,row5,row6)

                colgr.next_to(poly1,DOWN,buff=LARGE_BUFF)

                # col1[2:-1].set_color("#333333")
                # col2[2:-1].set_color("#333333")
                # col3[2:-1].set_color("#333333")
                # col2[2:-1].set_color("#333333")
                # col3[2:-1].set_color("#333333")

                #self.play(Write(colgr))
                self.play( Write(col1[0:2]) ,Write(col2[0:2]), Write(col3[0:2]) )
                #self.add(colgr)
                
                #rowgr.save_state()
                colgr.save_state()

                #rectb = SurroundingRectangle(col1[0:2]).set_color(WHITE).set_stroke(opacity=0.5).stretch_to_fit_width(colgr.get_width())
                rectver = SurroundingRectangle( col1[0:2] ).set_color(ORANGE)
                recthor = SurroundingRectangle( col2[0:2] ).set_color(GREEN)
                #rectelem = SurroundingRectangle( col1[2] ).set_color(RED)


                crl1 = Line(start=col1[0], end=col2[1],buff=0.1).set_color(YELLOW)#.set_stroke(width=5).set_opacity(0.5)
                crl2 = Line(start=col1[1], end=col2[0],buff=0.1).set_color(BLUE)

                # self.add(rectb)
                # self.add(rectver)
                # self.add(recthor)
                # self.add(rectelem)
                
                #self.wait(2)

                self.play( ShowCreation(rectver), ShowCreation(recthor), ShowCreation(crl1), ShowCreation(crl2) ) 

                n_line = NumberLine(
                x_min=-5,  x_max=15,
                tick_frequency=1,
                unit_size=1,
                include_numbers=True,
                numbers_to_show=np.arange(-5,1,15),
                )

                n_line.scale(0.7).to_corner(DOWN)
                #self.play( ShowCreation(n_line) )

                inft = Tex(r"\infty").next_to(n_line,RIGHT).set_color(TEAL)

                vertline = DashedLine(start=DOWN,end=UP).scale(0.7).set_opacity(0.3).move_to(n_line.n2p(0))
                #self.play( ShowCreation(vertline) )

                nlinegroup = VGroup(n_line,inft,vertline)
                nlinegroup.scale(0.8)
                nlinegroup.to_corner(DOWN)

                self.play( ShowCreation(n_line) )
                self.play( ShowCreation(vertline) )

                # n_line = NumberLine(
                # x_min=-3,  x_max=3,
                # tick_frequency=1,
                # unit_size=1,
                # include_numbers=True,
                # numbers_to_show=np.arange(-3,1,3),
                # )

                # n_line.shift(LEFT*3 + DOWN*2.5)
                # self.play( ShowCreation(n_line) )

                # vertline = DashedLine(start=DOWN,end=UP).set_opacity(0.3).move_to(n_line.n2p(0))
                # self.play( ShowCreation(vertline) )

                # tdots1 = Tex(r"\hdots").set_opacity(0.5).next_to(n_line,RIGHT).shift(UP*0.1)
                # tdots2 = Tex(r"\hdots").set_opacity(0.5).next_to(n_line,LEFT).shift(UP*0.1)
 
                # self.play(ShowCreation(tdots1),ShowCreation(tdots2))

                # self.wait(2)


        # SHOW b1

                b1 = Tex(   r"{ {1 \cdot 10 ",
                            r"-",
                            r"K \cdot 5}",
                            r"\over",
                            r"{(-K)} } }",
                            color=WHITE
                        ).scale(0.5)

                b1.next_to(col1[2],ORIGIN)
                b1.save_state()

                col1[2].replace(b1,stretch=True)

                #self.play(ReplacementTransform(col1[2],b1))


                # rectelem.generate_target()
                # rectelem.target.become( SurroundingRectangle( col1[2] ).set_color(RED) )
                # self.play(MoveToTarget(rectelem))
                rectelem = SurroundingRectangle( col1[2] ).set_color(RED)
                self.play(ShowCreation(rectelem))

                self.play(Write(b1))

                self.play(  col1[0].set_color, YELLOW,  col2[0].set_color(BLUE),
                            col1[1].set_color, BLUE,    col2[1].set_color(YELLOW),
                        )

                self.play(  b1[0].set_color, YELLOW,
                            b1[1].set_color, WHITE,
                            b1[2].set_color, BLUE,
                            b1[3].set_color, WHITE,
                            b1[4].set_color, BLUE,
                        )


                #self.wait(1)

                # hdet = Brace(b1, direction=DOWN, color=MAROON_B)
                # self.play(ShowCreation(hdet))
                # htext = Text("Hurwitz-Determinante").next_to(hdet,DOWN).set_color(MAROON_B)
                # self.play(Write(htext))

                # self.wait(2)

                # self.play(FadeOut(hdet),FadeOut(htext))

                colgr.restore()
                b1.restore()
                #self.wait(1)


        # SHOW b2

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[0], end=col3[1],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[1], end=col3[0],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col3[0:2] ).set_color(GREEN) )

                # rectelem.generate_target()
                # rectelem.target.become( SurroundingRectangle( col2[2] ).set_color(RED) )

                self.play(MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2))

                b2 = Tex(   r"{ {1 \cdot 0 ",
                            r"-",
                            r"K \cdot 0}",
                            r"\over",
                            r"{(-K)} } }",
                            color=WHITE
                        ).scale(0.5)

                b2.next_to(col2[2],ORIGIN)
                b2.save_state()

                col2[2].replace(b2,stretch=True)

                #self.play(ReplacementTransform(col2[2],b2))


                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col2[2] ).set_color(RED) )
                self.play(MoveToTarget(rectelem))

                self.play(Write(b2))

                self.play(  col1[0].set_color, YELLOW,  col3[0].set_color(BLUE),
                            col1[1].set_color, BLUE,    col3[1].set_color(YELLOW),
                        )

                self.play(  b2[0].set_color, YELLOW,
                            b2[1].set_color, WHITE,
                            b2[2].set_color, BLUE,
                            b2[3].set_color, WHITE,
                            b2[4].set_color, BLUE,
                        )

                #self.wait(1)

                colgr.restore()
                b2.restore()
                #self.wait(1)

        #SHOW b3
                self.play( Write(col3[2]) )
                # crl1.generate_target()
                # crl2.generate_target()
                # crl1.target.become( Line(start=col1[0], end=col2[1],buff=0.1).set_color(YELLOW) )
                # crl2.target.become( Line(start=col1[1], end=col2[0],buff=0.1).set_color(BLUE) )

                # recthor.generate_target()
                # recthor.target.become( SurroundingRectangle( col2[0:2] ).set_color(GREEN) )

                # # rectelem.generate_target()
                # # rectelem.target.become( SurroundingRectangle( col3[2] ).set_color(RED) )

                # self.play(MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2))

                # b3 = Tex(   r"{ {a_3 \cdot a_0 ",
                #             r"-",
                #             r"a_2 \cdot a_1}",
                #             r"\over",
                #             r"{(-a_2)} } }",
                #             color=WHITE
                #         ).scale(0.5)

                # b3.next_to(col3[2],ORIGIN)
                # b3.save_state()

                # col3[2].replace(b3,stretch=True)

                # #self.play(ReplacementTransform(col3[2],b3))


                # rectelem.generate_target()
                # rectelem.target.become( SurroundingRectangle( col3[2] ).set_color(RED) )
                # self.play(MoveToTarget(rectelem))

                # self.play(Write(b3))

                # self.play(  col1[0].set_color, YELLOW,  col2[0].set_color(BLUE),
                #             col1[1].set_color, BLUE,    col2[1].set_color(YELLOW),
                #         )

                # self.play(  b3[0].set_color, YELLOW,
                #             b3[1].set_color, WHITE,
                #             b3[2].set_color, BLUE,
                #             b3[3].set_color, WHITE,
                #             b3[4].set_color, BLUE,
                #         )


                # #self.wait(1)
                
                colgr.restore()
                # b3.restore()

                # #self.play(FadeOut(b1),FadeOut(b2),FadeOut(b3))
                # #self.wait(1)



                self.play( ReplacementTransform(b1,col1[2]) )
                self.play( ReplacementTransform(b2,col2[2]) )
                #self.play( ReplacementTransform(b3,col3[2]) )


        

        #SHOW c1

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[1], end=col2[2],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[2], end=col2[1],buff=0.1).set_color(BLUE) )

                rectver.generate_target()
                rectver.target.become( SurroundingRectangle( col1[1:3] ).set_color(ORANGE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col2[1:3] ).set_color(GREEN) )

                # rectelem.generate_target()
                # rectelem.target.become( SurroundingRectangle( col1[3] ).set_color(RED) )



                self.play(MoveToTarget(rectver),MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2))

                c1 = Tex(   r"{ {K \cdot 0 ",
                            r"-",
                            r"\frac{5\cdot(2-K)}{(-K)} \cdot 10}",
                            r"\over",
                            r"{-(\frac{5\cdot(2-K)}{(-K)})} } }",
                            color=WHITE
                        ).scale(0.4)

                c1.next_to(col1[3],ORIGIN)
                c1.save_state()

                #self.play(ReplacementTransform(col1[3],c1))
                col1[3].replace(c1,stretch=True)


                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col1[3] ).set_color(RED) )
                self.play(MoveToTarget(rectelem))


                self.play(Write(c1))

                self.play(  col1[1].set_color, YELLOW,  col2[1].set_color, BLUE,
                            col1[2].set_color, BLUE,    col2[2].set_color, YELLOW,
                        )

                self.play(  c1[0].set_color, YELLOW,
                            c1[1].set_color, WHITE,
                            c1[2].set_color, BLUE,
                            c1[3].set_color, WHITE,
                            c1[4].set_color, BLUE,
                        )


                #self.wait(1)
                
                colgr.restore()
                c1.restore()
                

        #SHOW c2

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[1], end=col3[2],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[2], end=col3[1],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col3[1:3] ).set_color(GREEN) )

                # rectelem.generate_target()
                # rectelem.target.become( SurroundingRectangle( col2[3] ).set_color(RED) )

                self.play(MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2))

                c2 = Tex(   r"{ {K \cdot 0 ",
                            r"-",
                            r"\frac{5\cdot(2-K)}{(-K)} \cdot 0}",
                            r"\over",
                            r"{-(\frac{5\cdot(2-K)}{(-K)})} } }",
                            color=WHITE
                        ).scale(0.4)

                c2.next_to(col2[3],ORIGIN)
                c2.save_state()


                #self.play(ReplacementTransform(col2[3],c2))
                col2[3].replace(c2,stretch=True)                

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col2[3] ).set_color(RED) )
                self.play(MoveToTarget(rectelem))

                self.play(Write(c2))

                self.play(  col1[1].set_color, YELLOW,  col3[1].set_color, BLUE,
                            col1[2].set_color, BLUE,    col3[2].set_color, YELLOW,
                        )

                self.play(  c2[0].set_color, YELLOW,
                            c2[1].set_color, WHITE,
                            c2[2].set_color, BLUE,
                            c2[3].set_color, WHITE,
                            c2[4].set_color, BLUE,
                        )


                #self.wait(1)
                
                colgr.restore()
                c2.restore()

        #SHOW c3
                self.play( Write(col3[3]) )
                # crl1.generate_target()
                # crl2.generate_target()
                # crl1.target.become( Line(start=col1[1], end=col2[2],buff=0.1).set_color(YELLOW) )
                # crl2.target.become( Line(start=col1[2], end=col2[1],buff=0.1).set_color(BLUE) )

                # recthor.generate_target()
                # recthor.target.become( SurroundingRectangle( col2[1:3] ).set_color(GREEN) )

                # # rectelem.generate_target()
                # # rectelem.target.become( SurroundingRectangle( col3[3] ).set_color(RED) )

                # self.play(MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2))

                # c3 = Tex(   r"{ {a_2 \cdot 0 ",
                #             r"-",
                #             r"b_1 \cdot a_0}",
                #             r"\over",
                #             r"{(-b_1)} } }",
                #             color=WHITE
                #         ).scale(0.5)

                # c3.next_to(col3[3],ORIGIN)
                # c3.save_state()

                # #self.play(ReplacementTransform(col3[3],c3))
                # col3[3].replace(c3,stretch=True)     

                # rectelem.generate_target()
                # rectelem.target.become( SurroundingRectangle( col3[3] ).set_color(RED) )
                # self.play(MoveToTarget(rectelem))

                # self.play(Write(c3))

                # self.play(  col1[1].set_color, YELLOW,  col2[1].set_color, BLUE,
                #             col1[2].set_color, BLUE,    col2[2].set_color, YELLOW,
                #         )

                # self.play(  c3[0].set_color, YELLOW,
                #             c3[1].set_color, WHITE,
                #             c3[2].set_color, BLUE,
                #             c3[3].set_color, WHITE,
                #             c3[4].set_color, BLUE,
                #         )


                #self.wait(1)
                
                colgr.restore()
                # c3.restore()

                

                self.play( ReplacementTransform(c1,col1[3]) )
                self.play( ReplacementTransform(c2,col2[3]) )
                # self.play( ReplacementTransform(c3,col3[3]) )


                dotc1 = Dot(color=RED)
                dotc1.move_to(n_line.n2p(0))
                self.play(FadeIn(dotc1, scale=0.5))
                self.play( dotc1.animate.move_to(n_line.n2p(10)) )

                self.play(FadeOut(rectver),FadeOut(recthor),FadeOut(rectelem),FadeOut(crl1),FadeOut(crl2))

##############################################################################################################

                col1box = SurroundingRectangle(col1)
                self.play(ShowCreation(col1box))

                self.play(FadeOut(col2),FadeOut(col3))

                poly1.generate_target()
                poly1.target.to_corner(LEFT)
                #self.play(MoveToTarget(poly1))

                col1gr = VGroup(col1,col1box)
                col1gr.generate_target()
                col1gr.target.to_corner(LEFT)
                self.play(MoveToTarget(col1gr), MoveToTarget(poly1))

                self.play( FadeToColor(col1[1],BLUE), FadeToColor(col1[2],BLUE) )


                expl1 = Text("p(s) ist HP, wenn:",font="Times New Roman").next_to(col1gr,RIGHT,buff=LARGE_BUFF).shift(UP*1.8).set_color(TEAL)

                cond1 = Tex(r"K",r">",r"0").next_to(expl1,DOWN*1.5).set_color(BLUE)

                expl2 = Text("und",font="Times New Roman").next_to(cond1,DOWN*1.5).set_color(TEAL)
                
                cond2 = Tex(r"5",r"-",r"\frac{5K}{2}",r">",r"0").next_to(expl2,DOWN*1.5).set_color(BLUE)

                expl3 = Text("gelten.",font="Times New Roman").next_to(cond2,DOWN*1.5).set_color(TEAL)

                #self.play(Write(expl1), Write(cond1), Write(expl2), Write(cond2),Write(expl3))

                self.play(Write(expl1))
                self.wait(2)
                self.play(Write(cond1))
                self.wait(1)
                self.play(Write(expl2))
                self.wait(1)
                self.play(Write(cond2))
                #self.wait(1)
                self.play(Write(expl3))

                condfull = VGroup(expl1,cond1,expl2,cond2,expl3)
                #self.play(Write(condfull))

                condbrace = Brace(condfull,RIGHT).set_color(WHITE)

                self.play(ShowCreation(condbrace))

                self.wait(1)

                condres = Tex(r"K",r">",r"2",r"\Longrightarrow",r"\text{p(s) ist HP}").next_to(condfull,RIGHT,buff=LARGE_BUFF)#.shift(UP*2+RIGHT*3)
                condres[0:3].set_color(BLUE)
                condres[-1].set_color(TEAL)

                

                #self.play(FadeTransform(condfull,condres))
                self.play(Write(condres))
                

                #kline = DashedLine(get_center(dotk1),end=RIGHT).get_center()     #.set_color(GREEN).set_opacity(0.3).move_to(n_line.n2p(7))
                
                dotk1 = Dot(n_line.n2p(2)).scale(0.5)
                dotk2 = Dot(n_line.n2p(15)).scale(0.5)
                kline = DashedLine(start=dotk1, end=dotk2).set_color(TEAL).set_opacity(0.5)
                

                self.play( ShowCreation(kline) )
                self.play(Write(inft))

                kber = Brace(kline, direction=UP, color=TEAL)
                self.play(ShowCreation(kber))
                ktext = Text("Stabilitätsbereich für K",font="Times New Roman").next_to(kber,UP).set_color(WHITE)
                self.play(Write(ktext))

                self.wait(5)



                self.play(FadeOut(col1gr),FadeOut(condfull),FadeOut(condbrace),FadeOut(condres))



                frame = self.camera.frame
                self.camera.frame.save_state()
                frame2 = frame.copy()
                frame2.set_width(6)
                frame2.move_to(poly1.get_center())
                self.play(Transform(frame, frame2))

                self.play(FadeToColor(poly1[4],ORANGE))
                self.wait(1)

                newK = Tex(r"4").move_to(poly1[4].get_center())
                newK.set_color(ORANGE)

                self.play(ReplacementTransform(poly1[4],newK))

                self.remove(nlinegroup,kline,kber,ktext,dotc1)

                self.wait(5)

                self.play(Restore(self.camera.frame))

#####################


                poly2 = Tex(   
                                r"{p(s) =",
                                r"{ ", r"1", r"s^{3}", r"+", r"2" ,r"s^2", r"+", r"5", r"s", r"+",r"10", r"}", r"}",
                                color=WHITE
                        ).to_corner(UR)

                poly2[4].set_color(RED)

                self.play( Write(poly2) )

                centerline = DashedLine(start=UP*5,end=DOWN*5).set_color(PINK).set_opacity(0.5)

                self.play(ShowCreation(centerline))



                axes1 = Axes(**self.axes_kwargs)
                axes2 = Axes(**self.axes_kwargs)

                x_label_tex = r"Re{}"
                y_label_tex = r"Im{}"

                labels1 = self.axis_labels = VGroup(
                axes1.get_x_axis_label(x_label_tex).next_to(axes1.x_axis.tip),
                axes1.get_y_axis_label(y_label_tex).next_to(axes1.y_axis.tip),
                )

                labels2 = labels1.copy()

                ax1 = VGroup(axes1,labels1).scale(0.7).next_to(poly1,DOWN,buff=LARGE_BUFF)
                ax2 = VGroup(axes2,labels2).scale(0.7).next_to(poly2,DOWN,buff=LARGE_BUFF)

                self.play(ShowCreation(ax1),ShowCreation(ax2))

                dots11 = Dot(color=ORANGE)
                dots12 = Dot(color=ORANGE)
                dots1x = Dot(color=ORANGE)
                dots11.move_to(axes1.c2p(-1, 2))
                dots12.move_to(axes1.c2p(-1, -2))
                dots1x.move_to(axes1.c2p(-3, 0))
                self.play(FadeIn(dots11, scale=0.5))
                self.play(FadeIn(dots12, scale=0.5))
                self.play(FadeIn(dots1x, scale=0.5))


                dots21 = Dot(color=RED)
                dots22 = Dot(color=RED)
                dots2x = Dot(color=RED)
                dots21.move_to(axes2.c2p(0, -2))
                dots22.move_to(axes2.c2p(0, 2))
                dots2x.move_to(axes2.c2p(-2, 0))
                self.play(FadeIn(dots21, scale=0.5))
                self.play(FadeIn(dots22, scale=0.5))
                self.play(FadeIn(dots2x, scale=0.5))


                self.wait(6)


                braceax1 = Brace(ax1,DOWN).set_color(GREEN)
                braceax2 = Brace(ax2,DOWN).set_color(GREEN)

                ax1text = Tex(r"\text{stabil}").set_color(GREEN).next_to(braceax1,DOWN)
                ax2text = Tex(r"\text{stabil}").set_color(GREEN).next_to(braceax2,DOWN)

                self.play(ShowCreation(braceax1),ShowCreation(braceax2))
                self.play(ShowCreation(ax1text),ShowCreation(ax2text))


                self.wait(10)

                self.play(*[FadeOut(mob)for mob in self.mobjects])

                self.wait(2)

"""
        #SHOW d1

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[2], end=col2[3],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[3], end=col2[2],buff=0.1).set_color(BLUE) )

                rectver.generate_target()
                rectver.target.become( SurroundingRectangle( col1[2:4] ).set_color(ORANGE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col2[2:4] ).set_color(GREEN) )

                # rectelem.generate_target()
                # rectelem.target.become( SurroundingRectangle( col1[4] ) )

                self.play(MoveToTarget(rectver),MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2))

                d1 = Tex(   r"{ {b_1 \cdot c_2 ",
                            r"-",
                            r"c_1 \cdot b_2}",
                            r"\over",
                            r"{(-c_1)} } }",
                            color=WHITE
                        ).scale(0.5)

                d1.next_to(col1[4],ORIGIN)
                d1.save_state()

                col1[4].replace(d1,stretch=True) 
                #self.play(ReplacementTransform(col1[4],d1))

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col1[4] ).set_color(RED) )
                self.play(MoveToTarget(rectelem))

                self.play(Write(d1))

                self.play(  col1[2].set_color, YELLOW,  col2[2].set_color, BLUE,
                            col1[3].set_color, BLUE,    col2[3].set_color, YELLOW,
                        )

                self.play(  d1[0].set_color, YELLOW,
                            d1[1].set_color, WHITE,
                            d1[2].set_color, BLUE,
                            d1[3].set_color, WHITE,
                            d1[4].set_color, BLUE,
                        )


                #self.wait(1)
                
                colgr.restore()
                d1.restore()

        #SHOW d2

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[2], end=col3[3],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[3], end=col3[2],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col3[2:4] ).set_color(GREEN) )

                # rectelem.generate_target()
                # rectelem.target.become( SurroundingRectangle( col1[4] ) )

                self.play(MoveToTarget(rectver),MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2))

                d2 = Tex(   r"{ {b_1 \cdot c_3 ",
                            r"-",
                            r"c_1 \cdot b_3}",
                            r"\over",
                            r"{(-c_1)} } }",
                            color=WHITE
                        ).scale(0.5)

                d2.next_to(col2[4],ORIGIN)
                d2.save_state()

                col2[4].replace(d2,stretch=True) 
                #self.play(ReplacementTransform(col1[4],d1))

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col2[4] ).set_color(RED) )
                self.play(MoveToTarget(rectelem))

                self.play(Write(d2))

                self.play(  col1[2].set_color, YELLOW,  col3[2].set_color, BLUE,
                            col1[3].set_color, BLUE,    col3[3].set_color, YELLOW,
                        )

                self.play(  d2[0].set_color, YELLOW,
                            d2[1].set_color, WHITE,
                            d2[2].set_color, BLUE,
                            d2[3].set_color, WHITE,
                            d2[4].set_color, BLUE,
                        )


                #self.wait(1)
                
                colgr.restore()
                d2.restore()

        #SHOW d3

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[2], end=col2[3],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[3], end=col2[2],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col2[2:4] ).set_color(GREEN) )

                # rectelem.generate_target()
                # rectelem.target.become( SurroundingRectangle( col1[4] ) )

                self.play(MoveToTarget(rectver),MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2))

                d3 = Tex(   r"{ {b_1 \cdot 0 ",
                            r"-",
                            r"c_1 \cdot 0}",
                            r"\over",
                            r"{(-c_1)} } }",
                            color=WHITE
                        ).scale(0.5)

                d3.next_to(col3[4],ORIGIN)
                d3.save_state()

                col3[4].replace(d3,stretch=True) 
                #self.play(ReplacementTransform(col1[4],d1))

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col3[4] ).set_color(RED) )
                self.play(MoveToTarget(rectelem))

                self.play(Write(d3))

                self.play(  col1[2].set_color, YELLOW,  col2[2].set_color, BLUE,
                            col1[3].set_color, BLUE,    col2[3].set_color, YELLOW,
                        )

                self.play(  d3[0].set_color, YELLOW,
                            d3[1].set_color, WHITE,
                            d3[2].set_color, BLUE,
                            d3[3].set_color, WHITE,
                            d3[4].set_color, BLUE,
                        )


                #self.wait(1)
                
                colgr.restore()
                d3.restore()

                # # self.play(FadeOut(d1),FadeOut(d2),FadeOut(d3))

                # # self.play(FadeOut(rectb), FadeOut(rectver), FadeOut(recthor), FadeOut(rectelem) ) 

                # # self.wait(2)

        #SHOW d4

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[2], end=col3[3],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[3], end=col3[2],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col3[2:4] ).set_color(GREEN) )

                # rectelem.generate_target()
                # rectelem.target.become( SurroundingRectangle( col1[4] ) )

                self.play(MoveToTarget(rectver),MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2))

                d4 = Tex(   r"{ {b_1 \cdot 0 ",
                            r"-",
                            r"c_1 \cdot 0}",
                            r"\over",
                            r"{(-c_1)} } }",
                            color=WHITE
                        ).scale(0.5)

                d4.next_to(col2[4],ORIGIN)
                d4.save_state()

                col2[4].replace(d4,stretch=True) 
                #self.play(ReplacementTransform(col1[4],d1))

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col2[4] ).set_color(RED) )
                self.play(MoveToTarget(rectelem))

                self.play(Write(d4))

                self.play(  col1[2].set_color, YELLOW,  col3[2].set_color, BLUE,
                            col1[3].set_color, BLUE,    col3[3].set_color, YELLOW,
                        )

                self.play(  d4[0].set_color, YELLOW,
                            d4[1].set_color, WHITE,
                            d4[2].set_color, BLUE,
                            d4[3].set_color, WHITE,
                            d4[4].set_color, BLUE,
                        )


                #self.wait(1)

                self.play(Write(col3[4]))
                
                colgr.restore()
                d4.restore()

                self.play( ReplacementTransform(d1,col1[4]) )
                self.play( ReplacementTransform(d2,col2[4]) )
                self.play( ReplacementTransform(d3,col3[4]) )
                self.play( ReplacementTransform(d4,col2[4]) )


        #SHOW e1

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[3], end=col2[4],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[4], end=col2[3],buff=0.1).set_color(BLUE) )

                rectver.generate_target()
                rectver.target.become( SurroundingRectangle( col1[3:5] ).set_color(ORANGE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col2[3:5] ).set_color(GREEN) )

                # rectelem.generate_target()
                # rectelem.target.become( SurroundingRectangle( col1[4] ) )

                self.play(MoveToTarget(rectver),MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2))

                e1 = Tex(   r"{ {c_1 \cdot d_2 ",
                            r"-",
                            r"d_1 \cdot c_2}",
                            r"\over",
                            r"{(-d_1)} } }",
                            color=WHITE
                        ).scale(0.5)

                e1.next_to(col1[5],ORIGIN)
                e1.save_state()

                col1[5].replace(e1,stretch=True) 
                #self.play(ReplacementTransform(col1[4],d1))

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col1[5] ).set_color(RED) )
                self.play(MoveToTarget(rectelem))

                self.play(Write(e1))

                self.play(  col1[3].set_color, YELLOW,  col2[3].set_color, BLUE,
                            col1[4].set_color, BLUE,    col2[4].set_color, YELLOW,
                        )

                self.play(  e1[0].set_color, YELLOW,
                            e1[1].set_color, WHITE,
                            e1[2].set_color, BLUE,
                            e1[3].set_color, WHITE,
                            e1[4].set_color, BLUE,
                        )


                #self.wait(1)
                
                colgr.restore()
                e1.restore()

                #self.play(FadeOut(rectelem))

        #SHOW e2

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[3], end=col3[4],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[4], end=col3[3],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col3[3:5] ).set_color(GREEN) )

                # rectelem.generate_target()
                # rectelem.target.become( SurroundingRectangle( col1[4] ) )

                self.play(MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2))

                e2 = Tex(   r"{ {c_1 \cdot d_3 ",
                            r"-",
                            r"d_1 \cdot c_3}",
                            r"\over",
                            r"{(-d_1)} } }",
                            color=WHITE
                        ).scale(0.5)

                e2.next_to(col2[5],ORIGIN)
                e2.save_state()

                col2[5].replace(e2,stretch=True) 
                #self.play(ReplacementTransform(col1[4],d1))

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col2[5] ).set_color(RED) )
                self.play(MoveToTarget(rectelem))

                self.play(Write(e2))

                self.play(  col1[3].set_color, YELLOW,  col2[3].set_color, BLUE,
                            col1[4].set_color, BLUE,    col2[4].set_color, YELLOW,
                        )

                self.play(  e2[0].set_color, YELLOW,
                            e2[1].set_color, WHITE,
                            e2[2].set_color, BLUE,
                            e2[3].set_color, WHITE,
                            e2[4].set_color, BLUE,
                        )


                #self.wait(1)
                
                colgr.restore()
                e2.restore()




        #SHOW e3

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[3], end=col2[4],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[4], end=col2[3],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col2[3:5] ).set_color(GREEN) )

                # rectelem.generate_target()
                # rectelem.target.become( SurroundingRectangle( col1[4] ) )

                self.play(MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2))

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col3[5] ).set_color(RED) )
                self.play(MoveToTarget(rectelem))

                self.play(Write(col3[5]))


        #SHOW e4

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[3], end=col3[4],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[4], end=col3[3],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col3[3:5] ).set_color(GREEN) )

                # rectelem.generate_target()
                # rectelem.target.become( SurroundingRectangle( col1[4] ) )

                self.play(MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2))

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col2[5] ).set_color(RED) )
                self.play(MoveToTarget(rectelem))

                self.play(Write(col2[5]))



        #SHOW e5 (0)                
                
                self.play(Write(col3[5]))


                self.play( ReplacementTransform(e1,col1[5]) )
                self.play( ReplacementTransform(e2,col2[5]) )

        #SHOW f1

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[4], end=col2[5],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[5], end=col2[4],buff=0.1).set_color(BLUE) )

                rectver.generate_target()
                rectver.target.become( SurroundingRectangle( col1[4:6] ).set_color(ORANGE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col2[4:6] ).set_color(GREEN) )

                # rectelem.generate_target()
                # rectelem.target.become( SurroundingRectangle( col1[4] ) )

                self.play(MoveToTarget(rectver),MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2))

                f1 = Tex(   r"{ {d_1 \cdot e_2 ",
                            r"-",
                            r"e_1 \cdot d_2}",
                            r"\over",
                            r"{(-e_1)} } }",
                            color=WHITE
                        ).scale(0.5)

                f1.next_to(col1[6],ORIGIN)
                f1.save_state()

                col1[6].replace(f1,stretch=True) 
                #self.play(ReplacementTransform(col1[4],d1))

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col1[6] ).set_color(RED) )
                self.play(MoveToTarget(rectelem))

                self.play(Write(f1))

                self.play(  col1[4].set_color, YELLOW,  col2[4].set_color, BLUE,
                            col1[5].set_color, BLUE,    col2[5].set_color, YELLOW,
                        )

                self.play(  f1[0].set_color, YELLOW,
                            f1[1].set_color, WHITE,
                            f1[2].set_color, BLUE,
                            f1[3].set_color, WHITE,
                            f1[4].set_color, BLUE,
                        )


                #self.wait(1)
                
                colgr.restore()
                f1.restore()

                self.play(FadeOut(rectelem))


        #SHOW f2

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[4], end=col3[5],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[5], end=col3[4],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col3[4:6] ).set_color(GREEN) )

                self.play(MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2))

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col2[6] ).set_color(RED) )
                self.play(MoveToTarget(rectelem))

                self.play(Write(col2[6]))

        #SHOW f3

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[4], end=col2[5],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[5], end=col2[4],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col2[4:6] ).set_color(GREEN) )

                self.play(MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2))

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col3[6] ).set_color(RED) )
                self.play(MoveToTarget(rectelem))

                self.play(Write(col3[6]))

        #SHOW f4

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[4], end=col3[5],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[5], end=col3[4],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col3[4:6] ).set_color(GREEN) )

                self.play(MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2))

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col2[6] ).set_color(RED) )
                self.play(MoveToTarget(rectelem))

                self.play(Write(col2[6]))

        #SHOW f5 (0)

                self.play(Write(col3[6]))

                self.play( ReplacementTransform(f1,col1[6]) )

        #SHOW g1

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[5], end=col2[6],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[6], end=col2[5],buff=0.1).set_color(BLUE) )

                rectver.generate_target()
                rectver.target.become( SurroundingRectangle( col1[5:7] ).set_color(ORANGE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col2[5:7] ).set_color(GREEN) )

                # rectelem.generate_target()
                # rectelem.target.become( SurroundingRectangle( col1[4] ) )

                self.play(MoveToTarget(rectver),MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2))

                g1 = Tex(   r"{ {e_1 \cdot f_2 ",
                            r"-",
                            r"f_1 \cdot e_2}",
                            r"\over",
                            r"{(-f_1)} } }",
                            color=WHITE
                        ).scale(0.5)

                g1.next_to(col1[7],ORIGIN)
                g1.save_state()

                col1[7].replace(g1,stretch=True) 
                #self.play(ReplacementTransform(col1[4],d1))

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col1[7] ).set_color(RED) )
                self.play(MoveToTarget(rectelem))

                self.play(Write(g1))

                self.play(  col1[5].set_color, YELLOW,  col2[5].set_color, BLUE,
                            col1[6].set_color, BLUE,    col2[6].set_color, YELLOW,
                        )

                self.play(  g1[0].set_color, YELLOW,
                            g1[1].set_color, WHITE,
                            g1[2].set_color, BLUE,
                            g1[3].set_color, WHITE,
                            g1[4].set_color, BLUE,
                        )


                #self.wait(1)
                
                colgr.restore()
                g1.restore()

                #self.play( ReplacementTransform(g1,col1[7]) )

                #self.play(Write(col2[7]),Write(col3[7]),Write(col2[7]),Write(col3[7]))




        #SHOW g2

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[5], end=col3[6],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[6], end=col3[5],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col3[5:7] ).set_color(GREEN) )

                self.play(MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2))

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col2[7] ).set_color(RED) )
                self.play(MoveToTarget(rectelem))

                self.play(Write(col2[7]))

        #SHOW g3

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[5], end=col2[6],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[6], end=col2[5],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col2[5:7] ).set_color(GREEN) )

                self.play(MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2))

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col3[7] ).set_color(RED) )
                self.play(MoveToTarget(rectelem))

                self.play(Write(col3[7]))

        #SHOW g4

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[5], end=col3[6],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[6], end=col3[5],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col3[5:7] ).set_color(GREEN) )

                self.play(MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2))

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col2[7] ).set_color(RED) )
                self.play(MoveToTarget(rectelem))

                self.play(Write(col2[7]))

        #SHOW g5 (0)

                self.play(Write(col3[7]))

                self.play( ReplacementTransform(g1,col1[7]) )

                self.wait(2)

                self.play(FadeOut(rectelem), FadeOut(crl1), FadeOut(crl2), FadeOut(rectver), FadeOut(recthor))

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
                # recthor.target.become( SurroundingRectangle( col2[0:2] ).set_color(GREEN) )
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
"""