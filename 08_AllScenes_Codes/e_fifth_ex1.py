from manimlib import *
import numpy as np

class Example1(Scene):
    def construct(self):

                self.wait(1)
                # INTRO FOR EXAMPLE 1
                intro_words = Text("Beispiel 1",font="Times New Roman")
                intro_words.set_color(YELLOW_C).scale(2)

                underline = Underline(mobject=intro_words)
                underline.set_color(YELLOW_C)

                self.play(Write(intro_words))

                self.play(ShowCreation(underline),run_time=1)

                self.wait(1)

                self.play(ShrinkToCenter(intro_words), ShrinkToCenter(underline))

                self.wait(1)



                poly1 = Tex(   
                                r"{p(s) =",
                                r"{ ", r"1" ,r"s^4", r"+", r"2", r"s^{3}", r"+",r"3", r"s^{2}", r"+", r"4", r"s", r"+", r"5", r"}", r"}",
                                color=WHITE
                        ).shift(UP*2)

                self.play( Write(poly1[0]), Write(poly1[2:-1]), Write(poly1[-1]) )

                self.wait(1)

                poly1[1].set_color(BLUE)
                self.play(Write(poly1[1]))
                
                ################## ##################
                # NICE ALTERNATIVE
                # self.play( Write(poly1[0]) )

                # i=2
                # while i < 14:
                #         self.play( Write(poly1[i]),run_time=0.25 )
                #         if i == 13:
                #                 break
                #         i+=1

                # self.wait(1.5)
                # self.play( FadeIn( poly1[1].set_color(BLUE) ) )
                # self.wait(1.5)
                ################## ##################

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

                zzgroup=VGroup(an,nton1,an1,n1ton2,an2,n2ton3,an3,n3ton4,an4,n4ton5,an5).next_to(poly1,DOWN,buff=LARGE_BUFF) #,n5ton6,an6,an7)
                
                play_kw = {"run_time": 4}
                self.play(Write(zzgroup),**play_kw)

                self.wait(5)

                an5.generate_target()
                an5.target.become( Tex(r"0").set_color(PINK).next_to(n4ton5,DOWN) )
                self.play(MoveToTarget(an5))

                self.wait(1)

                poly1.generate_target()
                poly1.target.to_corner(UR)
                self.play(MoveToTarget(poly1))

                zzgroup.generate_target()
                zzgroup.target.to_corner(UL)
                self.play(MoveToTarget(zzgroup))

                #self.play(ShrinkToCenter(zzgroup))


                self.play(FadeToColor(poly1,WHITE))


################################################                


                row1 = Tex(r"a_7",r"\hspace{0.25cm}",r"a_5",r"\hspace{0.25cm}",r"a_3",r"\hspace{0.25cm}",r"a_1",r"\hspace{0.25cm}",r"\hdots").shift(UP*3 + LEFT*4.5)
                row2 = Tex(r"a_6",r"\hspace{0.25cm}",r"a_4",r"\hspace{0.25cm}",r"a_2",r"\hspace{0.25cm}",r"a_0",r"\hspace{0.25cm}",r"\hdots").next_to(row1,DOWN*1.5)
                row3 = Tex(r"b_1",r"\hspace{0.25cm}",r"b_2",r"\hspace{0.25cm}",r"b_3",r"\hspace{0.25cm}",r"b_4",r"\hspace{0.25cm}",r"\hdots").next_to(row2,DOWN*1.5)
                row4 = Tex(r"c_1",r"\hspace{0.25cm}",r"c_2",r"\hspace{0.25cm}",r"c_3",r"\hspace{0.25cm}",r"c_4",r"\hspace{0.25cm}",r"\hdots").next_to(row3,DOWN*1.5)
                row5 = Tex(r"d_1",r"\hspace{0.25cm}",r"d_2",r"\hspace{0.25cm}",r"d_3",r"\hspace{0.25cm}",r"d_4",r"\hspace{0.25cm}",r"\hdots").next_to(row4,DOWN*1.5)

                # SAME MATRIX FOR COLUMN TRACKERS:

                col1 = Tex(r"1",r"\\",r"2",r"\\",r"1",r"\\",r"-6",r"\\",r"5")#.shift(UP*1.55 + LEFT*6.15)
                col2 = Tex(r"3",r"\\",r"4",r"\\",r"5",r"\\",r"0",r"\\",r"0")#.next_to(col1,RIGHT*1.5)
                col3 = Tex(r"5",r"\\",r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0")#.next_to(col2,RIGHT*1.5)

                # col1 = Tex(r"a_4",r"\\",r"a_3",r"\\",r"1",r"\\",r"-6",r"\\",r"5")#.shift(UP*1.55 + LEFT*6.15)
                # col2 = Tex(r"a_2",r"\\",r"a_1",r"\\",r"5",r"\\",r"0",r"\\",r"0")#.next_to(col1,RIGHT*1.5)
                # col3 = Tex(r"a_0",r"\\",r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0")#.next_to(col2,RIGHT*1.5)

                colt1 = Tex(r"a_7",r"\\",r"\\",r"a_6",r"\\",r"\\",r"b_1",r"\\",r"\\",r"c_1",r"\\",r"\\",r"d_1")#.shift(UP*1.55 + LEFT*6.15)
                colt2 = Tex(r"a_5",r"\\",r"\\",r"a_4",r"\\",r"\\",r"b_2",r"\\",r"\\",r"c_2",r"\\",r"\\",r"d_2")#.next_to(col1,RIGHT*1.5)
                colt3 = Tex(r"a_3",r"\\",r"\\",r"a_2",r"\\",r"\\",r"b_3",r"\\",r"\\",r"c_3",r"\\",r"\\",r"d_3")#.next_to(col2,RIGHT*1.5)
                coltgr = VGroup(colt1,colt2,colt3).arrange(RIGHT,buff=LARGE_BUFF*2)

                # col1 = Tex(r"a_7",r"\\",r"\\",r"a_6",r"\\",r"\\",r"?",r"\\",r"\\",r"?",r"\\",r"\\",r"?")#.shift(UP*1.55 + LEFT*6.15)
                # col2 = Tex(r"a_5",r"\\",r"\\",r"a_4",r"\\",r"\\",r"?",r"\\",r"\\",r"?",r"\\",r"\\",r"?")#.next_to(col1,RIGHT*1.5)
                # col3 = Tex(r"a_3",r"\\",r"\\",r"a_2",r"\\",r"\\",r"?",r"\\",r"\\",r"?",r"\\",r"\\",r"?")#.next_to(col2,RIGHT*1.5)
                # col2 = Tex(r"a_1",r"\\",r"\\",r"a_0",r"\\",r"\\",r"?",r"\\",r"\\",r"?",r"\\",r"\\",r"?")#.next_to(col3,RIGHT*1.5)
                # col3 = Tex(r"0",r"\\",r"\\",r"0",r"\\",r"\\",r"0",r"\\",r"\\",r"0",r"\\",r"\\",r"0")

                colgr = VGroup(col1,col2,col3).arrange(RIGHT,buff=LARGE_BUFF*2)  #.set_color(RED).set_opacity(0.5)
                rowgr = VGroup(row1,row2,row3,row4,row5)

                colgr.to_corner(UL)

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


                n_line = NumberLine(
                x_min=-6,  x_max=6,
                tick_frequency=1,
                unit_size=1,
                include_numbers=True,
                numbers_to_show=np.arange(-5,1,5),
                )

                n_line.scale(0.6).next_to(poly1,DOWN,buff=LARGE_BUFF)#.to_corner(RIGHT)
                self.play( ShowCreation(n_line) )

                vertline = DashedLine(start=DOWN,end=UP).scale(0.6).set_opacity(0.3).move_to(n_line.n2p(0))
                self.play( ShowCreation(vertline) )

                # self.wait(2)


        # SHOW b1

                b1 = Tex(   r"{ {1 \cdot 4 ",
                            r"-",
                            r"2 \cdot 3}",
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
                            r"2 \cdot 5}",
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

                self.play(Write(col3[2]))
                #self.wait(1)
                
                colgr.restore()
                #self.wait(1)

                self.play( ReplacementTransform(b1,col1[2]) )
                self.play( ReplacementTransform(b2,col2[2]) )

                dotb1 = Dot(color=GREEN)
                dotb1.move_to(n_line.n2p(0))
                self.play(FadeIn(dotb1, scale=0.5))
                self.play( dotb1.animate.move_to(n_line.n2p(1)) )        

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

                c1 = Tex(   r"{ {2 \cdot 5 ",
                            r"-",
                            r"1 \cdot 4}",
                            r"\over",
                            r"{(-1)} } }",
                            color=WHITE
                        ).scale(0.5)

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

                c2 = Tex(   r"{ {2 \cdot 0 ",
                            r"-",
                            r"1 \cdot 0}",
                            r"\over",
                            r"{(-1)} } }",
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

        #SHOW c3

                self.play(Write(col3[3]) )
                #self.wait(1)
                
                colgr.restore()

                self.play( ReplacementTransform(c1,col1[3]) )
                self.play( ReplacementTransform(c2,col2[3]) )

                dotc1 = Dot(color=RED)
                dotc1.move_to(n_line.n2p(0))
                self.play(FadeIn(dotc1, scale=0.5))
                self.play( dotc1.animate.move_to(n_line.n2p(-6)) )

                self.play(FocusOn(col1[3]))
                self.play(Indicate(col1[3],color=RED))
                self.wait(10)

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

                d1 = Tex(   r"{ {1 \cdot 0 ",
                            r"-",
                            r"(-6) \cdot 5}",
                            r"\over",
                            r"{-(-6)} } }",
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

                d2 = Tex(   r"{ {1 \cdot 0 ",
                            r"-",
                            r"(-6) \cdot 0}",
                            r"\over",
                            r"{-(-6)} } }",
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

                self.play(Write(col3[4]))
                #self.wait(1)
                
                colgr.restore()
                #self.wait(2)

                self.play( ReplacementTransform(d1,col1[4]) )
                self.play( ReplacementTransform(d2,col2[4]) )

                dotd1 = Dot(color=GREEN)
                dotd1.move_to(n_line.n2p(0))
                self.play(FadeIn(dotd1, scale=0.5))
                self.play( dotd1.animate.move_to(n_line.n2p(5)) )

                self.wait(2)

                self.play(FadeOut(rectelem), FadeOut(crl1), FadeOut(crl2), FadeOut(rectver), FadeOut(recthor))

                self.wait(2)


                col1box = SurroundingRectangle(col1)
                self.play(ShowCreation(col1box))

                arc1 = CurvedArrow( col1[2].get_boundary_point(LEFT), col1[3].get_boundary_point(LEFT) ).scale(0.7).set_color(RED_E)
                arc2 = CurvedArrow( col1[3].get_boundary_point(LEFT), col1[4].get_boundary_point(LEFT) ).scale(0.7).set_color(RED_A)
                self.play(ShowCreation(arc1),ShowCreation(arc2))

                vza = Tex(r"\text{zwei VZA}",r"\Longrightarrow",r"\text{zwei Nullstellen in rechten Halbebene}").to_corner(ORIGIN).shift(DOWN)
                khp = Tex(r"\text{Kein Hurwitzpolynom}").next_to(vza,DOWN,buff=MED_SMALL_BUFF)
                nbibo = Tex(r"\text{Nicht BIBO-Stabil}").next_to(khp,DOWN,buff=MED_SMALL_BUFF)

                self.play(Write(vza))
                self.wait(1)
                self.play(Write(khp))
                self.wait(1)
                self.play(Write(nbibo))

                self.wait(2)
                self.play(*[FadeOut(mob)for mob in self.mobjects])
                self.wait(2)

"""
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