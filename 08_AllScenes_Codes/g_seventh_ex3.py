from manimlib import *
import numpy as np

class Example3(Scene):
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


                self.wait(3)

                intro_words2 = Text("Beispiel 3: Nullzeile",font="Times New Roman").scale(2)
                intro_words2.set_color(YELLOW_C)

                underline2 = Underline(mobject=intro_words2)
                underline2.set_color(YELLOW_C)

                self.play(Write(intro_words2))

                self.play(ShowCreation(underline2),run_time=1)

                self.wait(3)

                self.play(ShrinkToCenter(intro_words2), ShrinkToCenter(underline2))

                self.wait(1)


                poly1 = Tex(   
                                r"{p(s) =",
                                r"{ ", r"1", r"s^{3}", r"+", r"2" ,r"s^2", r"+", r"5", r"s", r"+",r"10", r"}", r"}",
                                color=WHITE
                        ).shift(UP*2)

                self.play( Write(poly1[0]), Write(poly1[2:11]) )
                
                # for i in poly1:
                #     self.play(Write(i))

                self.wait(1)

                self.play(FadeIn(poly1[1]))
                self.play( FadeToColor( poly1[1],BLUE ),FadeToColor( poly1[4],BLUE ) , FadeToColor( poly1[7],YELLOW ), FadeToColor( poly1[10],YELLOW ) )

                self.wait(1)

                an = poly1[1].copy()
                nton1 = Arrow(UP,DOWN,buff=0)
                an1 = poly1[4].copy()
                n1ton2 = Arrow(DL,UR,buff=0)
                an2 = poly1[7].copy()
                n2ton3 = Arrow(UP,DOWN,buff=0)
                an3 = poly1[10].copy()
                n3ton4 = Arrow(DL,UR,buff=0)
                # an4 =  poly1[13].copy()
                # n4ton5 = Arrow(UP,DOWN,buff=0)
                # an5 = poly1[16].copy()
                # n5ton6 = Arrow(DL,UR,buff=0)
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
                # an4.next_to(n3ton4,UR)
                # n4ton5.next_to(an4,DOWN)
                # an5.next_to(n4ton5,DOWN)
                # n5ton6.next_to(an5,UR)     
                an6.next_to(n3ton4,UR)
                n6ton7.next_to(an6,DOWN)
                an7.next_to(n6ton7,DOWN)

                zzgroup=VGroup(an,nton1,an1,n1ton2,an2,n2ton3,an3,n3ton4,an6,n6ton7,an7).next_to(poly1,DOWN,buff=LARGE_BUFF)
                
                play_kw = {"run_time": 4}
                self.play(Write(zzgroup),**play_kw)

                self.wait(1)

                poly1.generate_target()
                poly1.target.to_corner(UR)
                self.play(MoveToTarget(poly1))

                zzgroup.generate_target()
                zzgroup.target.to_corner(UL)
                self.play(MoveToTarget(zzgroup))

                self.play(FadeToColor(poly1,WHITE))

                #self.play(ShrinkToCenter(zzgroup))




                row1 = Tex(r"a_3",r"\hspace{0.25cm}",r"a_1",r"\hspace{0.25cm}",r"0",r"\hspace{0.25cm}",r"a_1",r"\hspace{0.25cm}",r"\hdots").shift(UP*3 + LEFT*4.5)
                row2 = Tex(r"a_2",r"\hspace{0.25cm}",r"a_0",r"\hspace{0.25cm}",r"0",r"\hspace{0.25cm}",r"a_0",r"\hspace{0.25cm}",r"\hdots").next_to(row1,DOWN*1.5)
                row3 = Tex(r"b_1",r"\hspace{0.25cm}",r"b_2",r"\hspace{0.25cm}",r"b_3",r"\hspace{0.25cm}",r"b_4",r"\hspace{0.25cm}",r"\hdots").next_to(row2,DOWN*1.5)
                row4 = Tex(r"c_1",r"\hspace{0.25cm}",r"c_2",r"\hspace{0.25cm}",r"c_3",r"\hspace{0.25cm}",r"c_4",r"\hspace{0.25cm}",r"\hdots").next_to(row3,DOWN*1.5)
                row5 = Tex(r"d_1",r"\hspace{0.25cm}",r"d_2",r"\hspace{0.25cm}",r"d_3",r"\hspace{0.25cm}",r"d_4",r"\hspace{0.25cm}",r"\hdots").next_to(row4,DOWN*1.5)
                row6 = Tex(r"\vdots",r"\hspace{0.5cm}",r"\vdots").next_to(row5,DOWN*1.5).shift(LEFT*1.25)

                # SAME MATRIX FOR COLUMN TRACKERS:

                col1 = Tex(r"1",r"\\",r"2",r"\\",r"0",r"\\",r"c_1",r"\\",r"d_1",r"\\",r"e_1",r"\\",r"f_1",r"\\",r"g_1")#.shift(UP*1.55 + LEFT*6.15)
                col2 = Tex(r"5",r"\\",r"10",r"\\",r"0",r"\\",r"c_2",r"\\",r"d_2",r"\\",r"e_2",r"\\",r"0",r"\\",r"0")#.next_to(col1,RIGHT*1.5)
                col3 = Tex(r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0")#.next_to(col2,RIGHT*1.5)
                # col2 = Tex(r"a_1",r"\\",r"a_0",r"\\",r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0")#.next_to(col3,RIGHT*1.5)
                # col3 = Tex(r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0")

                colt1 = Tex(r"1",r"\\",r"2",r"\\",r"0")#.shift(UP*1.55 + LEFT*6.15)
                colt2 = Tex(r"5",r"\\",r"10",r"\\",r"0")#.next_to(col1,RIGHT*1.5)
                colt3 = Tex(r"0",r"\\",r"0",r"\\",r"0")#.next_to(col2,RIGHT*1.5)
                coltgr = VGroup(colt1,colt2,colt3).arrange(RIGHT,buff=LARGE_BUFF*2)

                coltr1 = Tex(r"1",r"\\",r"2",r"\\",r"4",r"\\",r"10")#.shift(UP*1.55 + LEFT*6.15)
                coltr2 = Tex(r"5",r"\\",r"10",r"\\",r"0",r"\\",r"0")#.next_to(col1,RIGHT*1.5)
                coltr3 = Tex(r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0")#.next_to(col2,RIGHT*1.5)
                coltrgr = VGroup(coltr1,coltr2,coltr3).arrange(RIGHT,buff=LARGE_BUFF*2)

                # colt1 = Tex(r"a_3",r"\\",r"\\",r"a_2",r"\\",r"\\",r"b_1",r"\\",r"\\",r"c_1",r"\\",r"\\",r"d_1")#.shift(UP*1.55 + LEFT*6.15)
                # colt2 = Tex(r"a_1",r"\\",r"\\",r"a_0",r"\\",r"\\",r"b_2",r"\\",r"\\",r"c_2",r"\\",r"\\",r"d_2")#.next_to(col1,RIGHT*1.5)
                # colt3 = Tex(r"0",r"\\",r"\\",r"0",r"\\",r"\\",r"b_3",r"\\",r"\\",r"c_3",r"\\",r"\\",r"d_3")#.next_to(col2,RIGHT*1.5)
                # colt4 = Tex(r"a_1",r"\\",r"\\",r"a_0",r"\\",r"\\",r"b_4",r"\\",r"\\",r"c_4",r"\\",r"\\",r"d_4")#.next_to(col3,RIGHT*1.5)
                # colt5 = Tex(r"0",r"\\",r"\\",r"0",r"\\",r"\\",r"0",r"\\",r"\\",r"0",r"\\",r"\\",r"0")
                # coltgr = VGroup(colt1,colt2,colt3,colt4,colt5).arrange(RIGHT,buff=LARGE_BUFF*2)

                # col1 = Tex(r"a_3",r"\\",r"\\",r"a_2",r"\\",r"\\",r"?",r"\\",r"\\",r"?",r"\\",r"\\",r"?")#.shift(UP*1.55 + LEFT*6.15)
                # col2 = Tex(r"a_1",r"\\",r"\\",r"a_0",r"\\",r"\\",r"?",r"\\",r"\\",r"?",r"\\",r"\\",r"?")#.next_to(col1,RIGHT*1.5)
                # col3 = Tex(r"0",r"\\",r"\\",r"0",r"\\",r"\\",r"?",r"\\",r"\\",r"?",r"\\",r"\\",r"?")#.next_to(col2,RIGHT*1.5)
                # col2 = Tex(r"a_1",r"\\",r"\\",r"a_0",r"\\",r"\\",r"?",r"\\",r"\\",r"?",r"\\",r"\\",r"?")#.next_to(col3,RIGHT*1.5)
                # col3 = Tex(r"0",r"\\",r"\\",r"0",r"\\",r"\\",r"0",r"\\",r"\\",r"0",r"\\",r"\\",r"0")

                colgr = VGroup(col1,col2,col3).arrange(RIGHT,buff=LARGE_BUFF*2) #.set_color(RED).set_opacity(0.5)
                rowgr = VGroup(row1,row2,row3,row4,row5,row6)

                colgr.to_corner(UL)
                coltgr.to_corner(UL)
                coltrgr.to_corner(UL)

                # col1[2:-1].set_color("#333333")
                # col2[2:-1].set_color("#333333")
                # col3[2:-1].set_color("#333333")
                # col2[2:-1].set_color("#333333")
                # col3[2:-1].set_color("#333333")

                colzz = VGroup(col1[0:2],col2[0:2],col3[0:2])

                self.play(TransformMatchingParts(zzgroup,colzz))

                #self.play(Write(colgr))
                #self.play( Write(col1[0:2]) ,Write(col2[0:2]), Write(col3[0:2]) )
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
                            r"2 \cdot 5}",
                            r"\over",
                            r"{(-2)} } }",
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
                            r"2 \cdot 0}",
                            r"\over",
                            r"{(-2)} } }",
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


                self.play(FadeOut(rectelem), FadeOut(crl1), FadeOut(crl2), FadeOut(rectver), FadeOut(recthor))



                frame = self.camera.frame
                self.camera.frame.save_state()
                frame2 = frame.copy()
                frame2.set_width(6)
                frame2.move_to(coltgr.get_center())
                frame2.shift(RIGHT/3)
                self.play(Transform(frame, frame2))


                #self.play(FocusOn(col1[2]))
                self.play(FadeToColor(col1[2],RED), FadeToColor(col2[2],RED), FadeToColor(col3[2],RED))
                self.wait(4)
                self.play(Restore(self.camera.frame))



                axes1 = Axes(**self.axes_kwargs)
                axes2 = Axes(**self.axes_kwargs)
                axes3 = Axes(**self.axes_kwargs)

                x_label_tex = r"Re{}"
                y_label_tex = r"Im{}"

                labels1 = self.axis_labels = VGroup(
                axes1.get_x_axis_label(x_label_tex).next_to(axes1.x_axis.tip),
                axes1.get_y_axis_label(y_label_tex).next_to(axes1.y_axis.tip),
                )

                labels2 = labels1.copy()
                labels3 = labels1.copy()

                ax1 = VGroup(axes1,labels1).scale(0.7).to_corner(LEFT).shift(DOWN)
                ax2 = VGroup(axes2,labels2).scale(0.7).next_to(axes1,RIGHT,buff=LARGE_BUFF)
                ax3 = VGroup(axes3,labels3).scale(0.7).next_to(axes2,RIGHT,buff=LARGE_BUFF)

                #self.add(ax1,ax2,ax3)

                self.play(ShowCreation(ax1),ShowCreation(ax2),ShowCreation(ax3))

                self.wait(15)


                dots11 = Dot(color=ORANGE)
                dots12 = Dot(color=ORANGE)
                dots11.move_to(axes1.c2p(-2, 0))
                dots12.move_to(axes1.c2p(2, 0))
                self.play(FadeIn(dots11, scale=0.5))
                self.play(FadeIn(dots12, scale=0.5))

                lines11 = Line(start=axes1.c2p(-2,0),end=axes1.c2p(0,0))
                braces11 = Brace(lines11,DOWN).scale(0.7).set_color(YELLOW)
                texts11 = Tex(r"\ell").next_to(braces11,DOWN).scale(0.7).set_color(YELLOW)

                #self.add(braces11,texts11)

                self.play(ShowCreation(braces11),ShowCreation(texts11))

                lines12 = Line(start=axes1.c2p(0,0),end=axes1.c2p(2,0))
                braces12 = Brace(lines12,DOWN).scale(0.7).set_color(YELLOW)
                texts12 = Tex(r"\ell").next_to(braces12,DOWN).scale(0.7).set_color(YELLOW)

                #self.add(braces12,texts12)
                self.play(ShowCreation(braces12),ShowCreation(texts12))

                self.wait(3)


                dots21 = Dot(color=ORANGE)
                dots22 = Dot(color=ORANGE)
                dots21.move_to(axes2.c2p(0, -2))
                dots22.move_to(axes2.c2p(0, 2))
                self.play(FadeIn(dots21, scale=0.5))
                self.play(FadeIn(dots22, scale=0.5))


                lines21 = Line(start=axes2.c2p(0,-2),end=axes2.c2p(0,0))
                braces21 = Brace(lines21,RIGHT).scale(0.7).set_color(YELLOW)
                texts21 = Tex(r"h").next_to(braces21,RIGHT).scale(0.7).set_color(YELLOW)

                #self.add(braces21,texts21)
                self.play(ShowCreation(braces21),ShowCreation(texts21))

                lines22 = Line(start=axes2.c2p(0,2),end=axes2.c2p(0,0))
                braces22 = Brace(lines22,RIGHT).scale(0.7).set_color(YELLOW)
                texts22 = Tex(r"h").next_to(braces22,RIGHT).scale(0.7).set_color(YELLOW)

                #self.add(braces22,texts22)
                self.play(ShowCreation(braces22),ShowCreation(texts22))

                self.wait(3)



                dots31 = Dot(color=ORANGE)
                dots32 = Dot(color=ORANGE)
                dots33 = Dot(color=ORANGE)
                dots34 = Dot(color=ORANGE)
                dots31.move_to(axes3.c2p(-2, -2))
                dots32.move_to(axes3.c2p(2, 2))
                dots33.move_to(axes3.c2p(-2, 2))
                dots34.move_to(axes3.c2p(2, -2))
                self.play(FadeIn(dots31, scale=0.5))
                self.play(FadeIn(dots32, scale=0.5))
                self.play(FadeIn(dots33, scale=0.5))
                self.play(FadeIn(dots34, scale=0.5))

                h_line = always_redraw(lambda: axes3.get_h_line(dots31.get_center()))
                v_line = always_redraw(lambda: axes3.get_v_line(dots31.get_center()))

                h_line2 = always_redraw(lambda: axes3.get_h_line(dots32.get_center()))
                v_line2 = always_redraw(lambda: axes3.get_v_line(dots32.get_center()))

                h_line3 = always_redraw(lambda: axes3.get_h_line(dots33.get_center()))
                v_line3 = always_redraw(lambda: axes3.get_v_line(dots33.get_center()))

                h_line4 = always_redraw(lambda: axes3.get_h_line(dots34.get_center()))
                v_line4 = always_redraw(lambda: axes3.get_v_line(dots34.get_center()))

                self.play(      ShowCreation(h_line),ShowCreation(v_line),
                                ShowCreation(h_line2),ShowCreation(v_line2),
                                ShowCreation(h_line3),ShowCreation(v_line3),
                                ShowCreation(h_line4),ShowCreation(v_line4)
                        )

        
                braceax1 = Brace(ax1,DOWN).set_color(RED)
                braceax2 = Brace(ax2,DOWN).set_color(GREEN)
                braceax3 = Brace(ax3,DOWN).set_color(RED)


                self.wait(25)


                ax1text = Tex(r"\text{instabil}").set_color(RED).next_to(braceax1,DOWN)
                ax2text = Tex(r"\text{stabil}").set_color(GREEN).next_to(braceax2,DOWN)
                ax3text = Tex(r"\text{instabil}").set_color(RED).next_to(braceax3,DOWN)

                
                #self.add(braceax1,braceax2,braceax3)
                #self.add(ax1text,ax2text,ax3text)
                self.play(ShowCreation(braceax1), ShowCreation(braceax3))
                self.play(ShowCreation(ax1text), ShowCreation(ax3text))

                self.wait(4)

                self.play(ShowCreation(braceax2))
                self.play(ShowCreation(ax2text))

                self.wait(10)

                #CameraFrame
                frame = self.camera.frame
                self.camera.frame.save_state()
                frame3 = frame.copy()
                frame3.set_width(6)
                frame3.move_to(coltgr.get_center())
                frame3.shift(RIGHT/3)
                self.play(Transform(frame, frame3))


                self.play(FadeToColor(col1[1],YELLOW), FadeToColor(col2[1],BLUE))

                a2 = Tex(r"a_2").move_to(col1[1].get_center()).set_color(YELLOW)
                a0 = Tex(r"a_0").move_to(col2[1].get_center()).set_color(BLUE)
                
                self.play( TransformMatchingParts(col1[1],a2), TransformMatchingParts(col2[1],a0) )

                self.wait(2)

                self.play( TransformMatchingParts(a2,col1[1]), TransformMatchingParts(a0,col2[1]) )

                self.wait(2)

                self.play(FadeOut(col1[2]), FadeOut(col2[2]), FadeOut(col3[2]) )

                col1[2].set_color(WHITE)
                col2[2].set_color(WHITE)
                col3[2].set_color(WHITE)


                self.remove(    ax1,ax2,ax3,braceax1,braceax2,braceax3,ax1text,ax2text,ax3text,
                                dots11,dots12,dots21,dots22,dots31,dots32,dots33,dots34,
                                lines11,lines12,lines21,lines22,
                                braces11,braces12,braces21,braces22,
                                texts11,texts12,texts21,texts22,
                                h_line,h_line2,h_line3,h_line4,
                                v_line,v_line2,v_line3,v_line4)

                

                self.play(Restore(self.camera.frame))
          

                # peq = Tex(      r"2", r"s^{2}", r"+", r"10", r"=", r"0", r"\\",
                #                 r"{\Longrightarrow}", r"s^{2}", r"=", r"5", r"\\",
                #                 r"{\Longrightarrow}", r"s_{1,2}", r"=", r"{\pm}", r"j", r"\sqrt{5}")

                peq1 = Tex(r"2", r"s^{2}", r"+", r"10", r"=", r"0")
                peq2 = Tex(r"{\Longrightarrow}", r"s^{2}", r"=", r"5")
                peq3 = Tex(r"{\Longrightarrow}", r"s_{1,2}", r"=", r"{\pm}", r"j", r"\sqrt{5}")

                peq = VGroup(peq1,peq2,peq3)
                peq.arrange(DOWN,buff=MED_LARGE_BUFF)
                

                for line in peq:
                        tm = -line.get_part_by_tex("=").get_center()
                        line.shift(tm[0] * RIGHT)

                peq1[0].set_color(YELLOW)
                peq1[3].set_color(BLUE)
                peq.next_to(poly1,DOWN,buff=MED_LARGE_BUFF*2)
                peq.to_corner(RIGHT)

                self.play(Write(peq1))
                self.play(Write(peq2))
                self.play(Write(peq3))

                self.play(FadeToColor(peq1[0],WHITE),FadeToColor(peq1[3],WHITE))
                self.wait(7)


                ax2gr = VGroup(ax2,braceax2,ax2text,lines21,lines22,dots21,dots22,braces21,braces22,texts21,texts22)
                
                ax2gr.scale(0.8)
                ax2gr.to_corner(LEFT)

                self.play(ShowCreation(ax2))

                self.play(ShowCreation(dots21), ShowCreation(dots22) )

                s1 = Tex(r"-",r"j",r"\sqrt{5}").scale(0.5).next_to(dots21,RIGHT).set_color(ORANGE)
                s2 = Tex(r"j",r"\sqrt{5}").scale(0.5).next_to(dots22,RIGHT).set_color(ORANGE)

                self.play(Write(s1),Write(s2))

                self.wait(4)

                self.play(ShowCreation(braceax2), ShowCreation(ax2text))

                self.wait(4)

                polyder = Tex(r"{ \frac{\partial}{\partial s} }",r"{ \Big(",r"2",r"s^{2}",r"+",r"10",r"\Big) }",r"=",r"4",r"s" ).next_to(peq,DOWN,buff=MED_LARGE_BUFF*2)
                polyder.to_corner(RIGHT)
                self.play(Write(polyder))

                self.play(FadeToColor(polyder[8],RED))


                coltr1[2].set_color(RED)
                self.play(Write(coltr1[2]), Write(col2[2]), Write(col3[2]) )

                self.wait(8)

                self.play(FadeToColor(polyder[8],WHITE))


                #self.play(*[FadeOut(mob)for mob in self.mobjects])




        #SHOW c1

                # crl1.generate_target()
                # crl2.generate_target()
                # crl1.target.become( Line(start=col1[1], end=col2[2],buff=0.1).set_color(YELLOW) )
                # crl2.target.become( Line(start=coltr1[2], end=col2[1],buff=0.1).set_color(BLUE) )

                # rectver.generate_target()
                # rectver.target.become( SurroundingRectangle( coltr1[1:3] ).set_color(ORANGE) )

                # recthor.generate_target()
                # recthor.target.become( SurroundingRectangle( col2[1:3] ).set_color(GREEN) )

                crl1 = Line(start=col1[1], end=col2[2],buff=0.1).set_color(YELLOW) 
                crl2 = Line(start=coltr1[2], end=col2[1],buff=0.1).set_color(BLUE)
                rectver = SurroundingRectangle( coltr1[1:3] ).set_color(ORANGE)
                recthor = SurroundingRectangle( col2[1:3] ).set_color(GREEN)

                self.play(ShowCreation(crl1), ShowCreation(crl2), ShowCreation(rectver), ShowCreation(recthor))

                # rectelem.generate_target()
                # rectelem.target.become( SurroundingRectangle( col1[3] ).set_color(RED) )

                # self.play(MoveToTarget(rectver),MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2))

                c1 = Tex(   r"{ {2 \cdot 0 ",
                            r"-",
                            r"4 \cdot 10}",
                            r"\over",
                            r"{(-4)} } }",
                            color=WHITE
                        ).scale(0.5)

                c1.next_to(col1[3],ORIGIN)
                c1.save_state()

                #self.play(ReplacementTransform(col1[3],c1))
                col1[3].replace(c1,stretch=True)

                # rectelem.generate_target()
                # rectelem.target.become( SurroundingRectangle( col1[3] ).set_color(RED) )                                
                # self.play(MoveToTarget(rectelem))

                rectelem = SurroundingRectangle( col1[3] ).set_color(RED)
                self.play(ShowCreation(rectelem))

                self.play(Write(c1))

                self.play(  col1[1].set_color, YELLOW,  col2[1].set_color, BLUE,
                            coltr1[2].set_color, BLUE,    col2[2].set_color, YELLOW,
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

                self.play(FadeToColor(coltr1[2],WHITE))
                
                self.play( ReplacementTransform(c1,coltr1[3]) )

                self.play( Write(coltr2[3]) )
                self.play( Write(col3[3]) )

                self.play(FadeOut(rectelem), FadeOut(crl1), FadeOut(crl2), FadeOut(rectver), FadeOut(recthor))


#####

                self.wait(2)


                col1box = SurroundingRectangle(coltr1)
                self.play(ShowCreation(col1box))

                # arc1 = CurvedArrow( col1[2].get_boundary_point(LEFT), col1[3].get_boundary_point(LEFT) ).scale(0.7).set_color(RED_E)
                # arc2 = CurvedArrow( col1[3].get_boundary_point(LEFT), col1[4].get_boundary_point(LEFT) ).scale(0.7).set_color(RED_A)
                # self.play(ShowCreation(arc1),ShowCreation(arc2))

                vza = Tex(r"\text{keine VZA}").to_corner(ORIGIN).shift(DOWN).set_color(YELLOW)
                khp = Tex(r"\text{Hurwitzpolynom}").next_to(vza,DOWN,buff=MED_SMALL_BUFF).set_color(GREEN)
                nbibo = Tex(r"\text{BIBO-Stabil}").next_to(khp,DOWN,buff=MED_SMALL_BUFF).set_color(GREEN)

                self.play(Write(vza))
                self.wait(1)
                self.play(Write(khp))
                self.wait(1)
                self.play(Write(nbibo))

                self.wait(2)

                self.play(*[FadeOut(mob)for mob in self.mobjects])

                self.wait(5)

#####

"""
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

                c2 = Tex(   r"{ {a_2 \cdot b_3 ",
                            r"-",
                            r"b_1 \cdot 0}",
                            r"\over",
                            r"{(-b_1)} } }",
                            color=WHITE
                        ).scale(0.5)

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

        #SHOW c2, c3
                self.play( Write(coltr2[3]) )
                self.play( Write(coltr3[3]) )


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

                self.play(FadeOut(rectelem), FadeOut(crl1), FadeOut(crl2), FadeOut(rectver), FadeOut(recthor))

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