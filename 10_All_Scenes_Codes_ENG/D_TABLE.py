from manimlib import *
import numpy as np

class D_TABLE_ENG(Scene):

        def construct(self):
                
                play_kw_fast = {"run_time": 0.5}
                play_kw = {"run_time": 4}
                restore_time = 0.5

                
        #SHOW TEMPLATE POLYNOM AND ZIG ZAG PATTERN FIRST
                self.wait(1)
                poly1 = Tex(    r"{p(s) =",
                                r"{ ", r"a_7", r"s^7", r"+", r"a_6" ,r"s^6", r"+", r"a_5", r"s^5", r"+",r"a_4",r"s^4",r"+",r"a_3",r"s^3",r"+",r"a_2",r"s^2",r"+",r"a_1",r"s",r"+",r"a_0", r"}", r"}"
                            ).shift(UP*2)

                self.play( Write(poly1) )

                self.wait(3)

                self.play(  FadeToColor( poly1[1],BLUE ), FadeToColor( poly1[4],BLUE ),
                            FadeToColor( poly1[7],YELLOW ), FadeToColor( poly1[10],YELLOW ),
                            FadeToColor( poly1[13],PINK ), FadeToColor( poly1[16],PINK ),
                            FadeToColor( poly1[19],ORANGE ), FadeToColor( poly1[22],ORANGE ),
                        )
                
                deg_n = Tex(r"\text{deg}",r"\Big(p(s)\Big) :", r" n = 7" ).next_to(poly1.get_corner(LEFT),DOWN*3+RIGHT)
                deg_n[-1].set_color(RED)
            
                self.play(Write(deg_n))
                self.play(Indicate(poly1[2],color=RED))
                self.wait(0.5)
                self.play(FadeOut(deg_n))

                self.wait(0.5)
                
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
                an6 = poly1[19].copy()
                n6ton7 = Arrow(UP,DOWN,buff=0)
                an7 = poly1[22].copy()
                n7ton8 = Arrow(DL,UR,buff=0)
                an8 = Tex(r"0").set_color(RED)
                n8ton9 = Arrow(UP,DOWN,buff=0)
                an9 = Tex(r"0").set_color(RED)


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

                n7ton8.next_to(an7,UR)     
                an8.next_to(n7ton8,UR)
                n8ton9.next_to(an8,DOWN)
                an9.next_to(n8ton9,DOWN)

                zzgroup=VGroup(an,nton1,an1,n1ton2,an2,n2ton3,an3,n3ton4,an4,n4ton5,an5,n5ton6,an6,n6ton7,an7,n7ton8,an8,n8ton9,an9).next_to(poly1,DOWN,buff=LARGE_BUFF)                

                self.play(Write(zzgroup[0:15]),**play_kw)

                self.wait(4)

                self.play(Indicate(poly1[2],color=RED))
                self.play(Write(zzgroup[15:20]))

                self.wait(4)
                
                self.play(FadeOut(poly1),FadeOut(zzgroup))
                
                
        #START TO CREATE THE ROUTH ARRAY

                # COLUMN MATRIX:
                col1 = Tex(r"a_7",r"\\",r"a_6",r"\\",r"b_1",r"\\",r"c_1",r"\\",r"d_1",r"\\",r"e_1",r"\\",r"f_1",r"\\",r"g_1")
                col2 = Tex(r"a_5",r"\\",r"a_4",r"\\",r"b_2",r"\\",r"c_2",r"\\",r"d_2",r"\\",r"e_2",r"\\",r"0",r"\\",r"0")
                col3 = Tex(r"a_3",r"\\",r"a_2",r"\\",r"b_3",r"\\",r"c_3",r"\\",r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0")
                col4 = Tex(r"a_1",r"\\",r"a_0",r"\\",r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0")
                col5 = Tex(r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0")

                # SAME MATRIX FOR COLUMN TRACKERS:
                colt1 = Tex(r"a_7",r"\\",r"\\",r"a_6",r"\\",r"\\",r"b_1",r"\\",r"\\",r"c_1",r"\\",r"\\",r"d_1")
                colt2 = Tex(r"a_5",r"\\",r"\\",r"a_4",r"\\",r"\\",r"b_2",r"\\",r"\\",r"c_2",r"\\",r"\\",r"d_2")
                colt3 = Tex(r"a_3",r"\\",r"\\",r"a_2",r"\\",r"\\",r"b_3",r"\\",r"\\",r"c_3",r"\\",r"\\",r"d_3")
                colt4 = Tex(r"a_1",r"\\",r"\\",r"a_0",r"\\",r"\\",r"b_4",r"\\",r"\\",r"c_4",r"\\",r"\\",r"d_4")
                colt5 = Tex(r"0",r"\\",r"\\",r"0",r"\\",r"\\",r"0",r"\\",r"\\",r"0",r"\\",r"\\",r"0")
                coltgr = VGroup(colt1,colt2,colt3,colt4,colt5).arrange(RIGHT,buff=LARGE_BUFF*2).shift(UP/2)

                colgr = VGroup(col1,col2,col3,col4,col5).arrange(RIGHT,buff=LARGE_BUFF*2).shift(UP/2)             
                colzz = VGroup( col1[0:2], col2[0:2], col3[0:2], col4[0:2], col5[0:2] )
                self.play(Write(colzz))

                colgr.save_state()

                rectver = SurroundingRectangle( col1[0:2] ).set_color(ORANGE)
                recthor = SurroundingRectangle( col2[0:2] ).set_color(GREEN)

                crl1 = Line(start=col1[0], end=col2[1],buff=0.1).set_color(YELLOW)
                crl2 = Line(start=col1[1], end=col2[0],buff=0.1).set_color(BLUE)

                self.wait(10)

                self.play( ShowCreation(rectver), ShowCreation(recthor), ShowCreation(crl1), ShowCreation(crl2) ) 

    # CALCULATE THE REST OF THE TABLE

        # SHOW b1

                b1 = Tex(   r"{ {a_7 \cdot a_4 ",
                            r"-",
                            r"a_6 \cdot a_5}",
                            r"\over",
                            r"{(-a_6)} } }",
                            color=WHITE
                        ).scale(0.5)

                b1.next_to(col1[2],ORIGIN)
                b1.save_state()

                col1[2].replace(b1,stretch=True)

                rectelem = SurroundingRectangle( col1[2] ).set_color(RED)
                ## self.play(ShowCreation(rectelem)) #the legacy play for rectelem

                #CameraFrame
                frame = self.camera.frame
                self.camera.frame.save_state()
                frame2 = frame.copy()
                frame2.set_width(5)
                frame2.move_to(rectelem.get_center())
                frame2.shift(UR/2)
                frame2.shift(RIGHT/3)
                self.play(Transform(frame, frame2))

                # Show the determinant for the first and last time
                leftbracket = Line(DOWN*0.7,UP*0.7,stroke_width=1.5)
                rightbracket = Line(DOWN*0.7,UP*0.7,stroke_width=1.5).next_to(leftbracket,RIGHT*10)

                brackets = VGroup(leftbracket,rightbracket).next_to(col1[2],ORIGIN)

                a_7 = Tex(r"a_7").next_to(leftbracket.get_corner(UR),RIGHT).shift(DOWN/4)
                a_6 = Tex(r"a_6").next_to(leftbracket.get_corner(DR),RIGHT).shift(UP/4)

                a_5 = Tex(r"a_5").next_to(rightbracket.get_corner(UL),LEFT).shift(DOWN/4)
                a_4 = Tex(r"a_4").next_to(rightbracket.get_corner(DL),LEFT).shift(UP/4)

                divline = Line(start = leftbracket.get_corner(DOWN)+LEFT/2, end = rightbracket.get_corner(DOWN)+RIGHT/2, stroke_width=1 ).shift(DOWN/6)
                diva6 = Tex(r"-a_6").next_to(divline,DOWN,buff=SMALL_BUFF)

                detgroup = VGroup(brackets,a_7,a_6,a_5,a_4,divline,diva6).scale(0.4)
                rectdet = SurroundingRectangle( detgroup ).set_color(RED)

                self.play(ShowCreation(rectdet),Write(detgroup))

                rectdet.generate_target()
                rectdet.target.become(rectelem)

                self.wait(2)
                
                self.play(TransformMatchingShapes(detgroup,b1),ReplacementTransform(rectdet,rectelem))

                ##self.play(Write(b1),run_time = 4) #the legacy play for b1

                self.play(  FadeToColor(b1[0],YELLOW),
                            FadeToColor(b1[1],WHITE),
                            FadeToColor(b1[2],BLUE),
                            FadeToColor(b1[3],WHITE),
                            FadeToColor(b1[4],BLUE),

                            FadeToColor(col1[0],YELLOW),FadeToColor(col2[0],BLUE),
                            FadeToColor(col1[1],BLUE),  FadeToColor(col2[1],YELLOW),
                        )
                
                self.wait(10)
                

                """
                # Can be added to imply the determinant
                # hdet = Brace(b1, direction=DOWN, color=MAROON_B)
                # self.play(ShowCreation(hdet))
                # htext = Text("Hurwitz Determinant").next_to(hdet,DOWN).set_color(MAROON_B)
                # self.play(Write(htext))
                # self.play(FadeOut(hdet),FadeOut(htext))
                """

                self.wait(restore_time)

                colgr.restore()
                b1.restore()

                self.play(Restore(self.camera.frame))


        # SHOW b2

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[0], end=col3[1],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[1], end=col3[0],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col3[0:2] ).set_color(GREEN) )

                self.play(MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2))

                b2 = Tex(   r"{ {a_7 \cdot a_2 ",
                            r"-",
                            r"a_6 \cdot a_3}",
                            r"\over",
                            r"{(-a_6)} } }",
                            color=WHITE
                        ).scale(0.5)

                b2.next_to(col2[2],ORIGIN)
                b2.save_state()

                col2[2].replace(b2,stretch=True)

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col2[2] ).set_color(RED) )
                self.play(MoveToTarget(rectelem))

                self.play(Write(b2))

                self.play(  FadeToColor(b2[0],YELLOW),
                            FadeToColor(b2[1],WHITE),
                            FadeToColor(b2[2],BLUE),
                            FadeToColor(b2[3],WHITE),
                            FadeToColor(b2[4],BLUE),

                            FadeToColor(col1[0],YELLOW),FadeToColor(col3[0],BLUE),
                            FadeToColor(col1[1],BLUE),  FadeToColor(col3[1],YELLOW),
                        )

                self.wait(restore_time)

                colgr.restore()
                b2.restore()

        #SHOW b3

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[0], end=col4[1],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[1], end=col4[0],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col4[0:2] ).set_color(GREEN) )

                self.play(MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2))

                b3 = Tex(   r"{ {a_7 \cdot a_0 ",
                            r"-",
                            r"a_6 \cdot a_1}",
                            r"\over",
                            r"{(-a_6)} } }",
                            color=WHITE
                        ).scale(0.5)

                b3.next_to(col3[2],ORIGIN)
                b3.save_state()

                col3[2].replace(b3,stretch=True)

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col3[2] ).set_color(RED) )
                self.play(MoveToTarget(rectelem))

                self.play(Write(b3))

                self.play(  FadeToColor(b3[0],YELLOW),
                            FadeToColor(b3[1],WHITE),
                            FadeToColor(b3[2],BLUE),
                            FadeToColor(b3[3],WHITE),
                            FadeToColor(b3[4],BLUE),

                            FadeToColor(col1[0],YELLOW),FadeToColor(col4[0],BLUE),
                            FadeToColor(col1[1],BLUE),  FadeToColor(col4[1],YELLOW),
                        )

                self.wait(restore_time)
                
                colgr.restore()
                b3.restore()

        #SHOW b4

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[0], end=col5[1],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[1], end=col5[0],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col5[0:2] ).set_color(GREEN) )

                self.play(MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2))

                b4 = Tex(   r"{ {a_7 \cdot 0 ",
                            r"-",
                            r"a_6 \cdot 0}",
                            r"\over",
                            r"{(-a_6)} } }",
                            color=WHITE
                        ).scale(0.5)

                b4.next_to(col4[2],ORIGIN)
                b4.save_state()

                col4[2].replace(b4,stretch=True)

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col4[2] ).set_color(RED) )
                self.play(MoveToTarget(rectelem))

                self.play(Write(b4))

                self.play(  FadeToColor(b4[0],YELLOW),
                            FadeToColor(b4[1],WHITE),
                            FadeToColor(b4[2],BLUE),
                            FadeToColor(b4[3],WHITE),
                            FadeToColor(b4[4],BLUE),

                            FadeToColor(col1[0],YELLOW),FadeToColor(col5[0],BLUE),
                            FadeToColor(col1[1],BLUE),  FadeToColor(col5[1],YELLOW),
                        )

                self.play( Write(col5[2]) )

                self.wait(restore_time)
                
                colgr.restore()
                b4.restore()


                self.play( ReplacementTransform(b1,col1[2]) )
                self.play( ReplacementTransform(b2,col2[2]) )
                self.play( ReplacementTransform(b3,col3[2]) )
                self.play( ReplacementTransform(b4,col4[2]) )
                
        #SHOW c1

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[1], end=col2[2],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[2], end=col2[1],buff=0.1).set_color(BLUE) )

                rectver.generate_target()
                rectver.target.become( SurroundingRectangle( col1[1:3] ).set_color(ORANGE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col2[1:3] ).set_color(GREEN) )

                self.play(MoveToTarget(rectver),MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2))

                c1 = Tex(   r"{ {a_6 \cdot b_2 ",
                            r"-",
                            r"b_1 \cdot a_4}",
                            r"\over",
                            r"{(-b_1)} } }",
                            color=WHITE
                        ).scale(0.5)

                c1.next_to(col1[3],ORIGIN)
                c1.save_state()

                col1[3].replace(c1,stretch=True)

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col1[3] ).set_color(RED) )
                self.play(MoveToTarget(rectelem))

                self.play(Write(c1))

                self.play(  FadeToColor(c1[0],YELLOW),
                            FadeToColor(c1[1],WHITE),
                            FadeToColor(c1[2],BLUE),
                            FadeToColor(c1[3],WHITE),
                            FadeToColor(c1[4],BLUE),

                            FadeToColor(col1[1],YELLOW),FadeToColor(col2[1],BLUE),
                            FadeToColor(col1[2],BLUE),  FadeToColor(col2[2],YELLOW),
                        )

                self.wait(restore_time)
                
                colgr.restore()
                c1.restore()                

        #SHOW c2

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[1], end=col3[2],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[2], end=col3[1],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col3[1:3] ).set_color(GREEN) )

                self.play(MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2))

                c2 = Tex(   r"{ {a_6 \cdot b_3 ",
                            r"-",
                            r"b_1 \cdot a_2}",
                            r"\over",
                            r"{(-b_1)} } }",
                            color=WHITE
                        ).scale(0.5)

                c2.next_to(col2[3],ORIGIN)
                c2.save_state()

                col2[3].replace(c2,stretch=True)                

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col2[3] ).set_color(RED) )
                self.play(MoveToTarget(rectelem))

                self.play(Write(c2))

                self.play(  FadeToColor(c2[0],YELLOW),
                            FadeToColor(c2[1],WHITE),
                            FadeToColor(c2[2],BLUE),
                            FadeToColor(c2[3],WHITE),
                            FadeToColor(c2[4],BLUE),

                            FadeToColor(col1[1],YELLOW),FadeToColor(col3[1],BLUE),
                            FadeToColor(col1[2],BLUE),  FadeToColor(col3[2],YELLOW),
                        )

                self.wait(restore_time)
                
                colgr.restore()
                c2.restore()

        #SHOW c3

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[1], end=col4[2],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[2], end=col4[1],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col4[1:3] ).set_color(GREEN) )

                self.play(MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2))

                c3 = Tex(   r"{ {a_6 \cdot 0 ",
                            r"-",
                            r"b_1 \cdot a_0}",
                            r"\over",
                            r"{(-b_1)} } }",
                            color=WHITE
                        ).scale(0.5)

                c3.next_to(col3[3],ORIGIN)
                c3.save_state()

                col3[3].replace(c3,stretch=True)     

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col3[3] ).set_color(RED) )
                self.play(MoveToTarget(rectelem))

                self.play(Write(c3))

                self.play(  FadeToColor(c3[0],YELLOW),
                            FadeToColor(c3[1],WHITE),
                            FadeToColor(c3[2],BLUE),
                            FadeToColor(c3[3],WHITE),
                            FadeToColor(c3[4],BLUE),

                            FadeToColor(col1[1],YELLOW),FadeToColor(col4[1],BLUE),
                            FadeToColor(col1[2],BLUE),  FadeToColor(col4[2],YELLOW),
                )

                self.wait(restore_time)
                
                colgr.restore()
                c3.restore()


        #SHOW c4

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[1], end=col5[2],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[2], end=col5[1],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col5[1:3] ).set_color(GREEN) )

                self.play(MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2))

                c4 = Tex(   r"{ {a_6 \cdot 0 ",
                            r"-",
                            r"b_1 \cdot 0}",
                            r"\over",
                            r"{(-b_1)} } }",
                            color=WHITE
                        ).scale(0.5)

                c4.next_to(col4[3],ORIGIN)
                c4.save_state()

                col4[3].replace(c4,stretch=True) 

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col4[3] ).set_color(RED) )
                self.play(MoveToTarget(rectelem))

                self.play(Write(c4))

                self.play(  FadeToColor(c4[0],YELLOW),
                            FadeToColor(c4[1],WHITE),
                            FadeToColor(c4[2],BLUE),
                            FadeToColor(c4[3],WHITE),
                            FadeToColor(c4[4],BLUE),

                            FadeToColor(col1[1],YELLOW),FadeToColor(col5[1],BLUE),
                            FadeToColor(col1[2],BLUE),  FadeToColor(col5[2],YELLOW),
                        )

                self.play(Write(col5[3]))
                
                self.wait(restore_time)

                colgr.restore()
                c4.restore()

                saycalc = Tex(r"\text{The calculation continues until there are }", r"(n+1)", r"\text{ rows in the table.}").scale(0.8).to_corner(DOWN)
                saycalc[1].set_color(RED)

                self.play( ReplacementTransform(c1,col1[3]) )
                self.play( ReplacementTransform(c2,col2[3]) )
                self.play( ReplacementTransform(c3,col3[3]) )
                self.play( ReplacementTransform(c4,col4[3]), Write(saycalc) )
                
        #SHOW d1
                
                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[2], end=col2[3],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[3], end=col2[2],buff=0.1).set_color(BLUE) )

                rectver.generate_target()
                rectver.target.become( SurroundingRectangle( col1[2:4] ).set_color(ORANGE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col2[2:4] ).set_color(GREEN) )

                self.play(MoveToTarget(rectver),MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2),**play_kw_fast)

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

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col1[4] ).set_color(RED) )
                self.play(MoveToTarget(rectelem),**play_kw_fast)

                self.play(Write(d1),**play_kw_fast)

                self.play(  FadeToColor(d1[0],YELLOW),
                            FadeToColor(d1[1],WHITE),
                            FadeToColor(d1[2],BLUE),
                            FadeToColor(d1[3],WHITE),
                            FadeToColor(d1[4],BLUE),

                            FadeToColor(col1[2],YELLOW),FadeToColor(col2[2],BLUE),
                            FadeToColor(col1[3],BLUE),  FadeToColor(col2[3],YELLOW), **play_kw_fast
                        )

                self.wait(restore_time)
                
                colgr.restore()
                d1.restore()

        #SHOW d2

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[2], end=col3[3],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[3], end=col3[2],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col3[2:4] ).set_color(GREEN) )

                self.play(MoveToTarget(rectver),MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2),**play_kw_fast)

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

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col2[4] ).set_color(RED) )
                self.play(MoveToTarget(rectelem),**play_kw_fast)

                self.play(Write(d2),**play_kw_fast)

                self.play(  FadeToColor(d2[0],YELLOW),
                            FadeToColor(d2[1],WHITE),
                            FadeToColor(d2[2],BLUE),
                            FadeToColor(d2[3],WHITE),
                            FadeToColor(d2[4],BLUE),

                            FadeToColor(col1[2],YELLOW),FadeToColor(col3[2],BLUE),
                            FadeToColor(col1[3],BLUE),  FadeToColor(col3[3],YELLOW), **play_kw_fast
                        )

                self.wait(restore_time)
                
                colgr.restore()
                d2.restore()

        #SHOW d3

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[2], end=col4[3],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[3], end=col4[2],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col4[2:4] ).set_color(GREEN) )

                self.play(MoveToTarget(rectver),MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2),**play_kw_fast)

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

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col3[4] ).set_color(RED) )
                self.play(MoveToTarget(rectelem),**play_kw_fast)

                self.play(Write(d3),**play_kw_fast)

                self.play(  FadeToColor(d3[0],YELLOW),
                            FadeToColor(d3[1],WHITE),
                            FadeToColor(d3[2],BLUE),
                            FadeToColor(d3[3],WHITE),
                            FadeToColor(d3[4],BLUE),

                            FadeToColor(col1[2],YELLOW),FadeToColor(col4[2],BLUE),
                            FadeToColor(col1[3],BLUE),  FadeToColor(col4[3],YELLOW), **play_kw_fast
                        )

                self.wait(restore_time)
                
                colgr.restore()
                d3.restore()

        #SHOW d4

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[2], end=col5[3],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[3], end=col5[2],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col5[2:4] ).set_color(GREEN) )

                self.play(MoveToTarget(rectver),MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2),**play_kw_fast)

                d4 = Tex(   r"{ {b_1 \cdot 0 ",
                            r"-",
                            r"c_1 \cdot 0}",
                            r"\over",
                            r"{(-c_1)} } }",
                            color=WHITE
                        ).scale(0.5)

                d4.next_to(col4[4],ORIGIN)
                d4.save_state()

                col4[4].replace(d4,stretch=True) 

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col4[4] ).set_color(RED) )
                self.play(MoveToTarget(rectelem),**play_kw_fast)

                self.play(Write(d4),**play_kw_fast)

                self.play(  FadeToColor(d4[0],YELLOW),
                            FadeToColor(d4[1],WHITE),
                            FadeToColor(d4[2],BLUE),
                            FadeToColor(d4[3],WHITE),
                            FadeToColor(d4[4],BLUE),

                            FadeToColor(col1[2],YELLOW),FadeToColor(col5[2],BLUE),
                            FadeToColor(col1[3],BLUE),  FadeToColor(col5[3],YELLOW), **play_kw_fast
                        )

                self.play(Write(col5[4]),**play_kw_fast)

                self.wait(restore_time)
                
                colgr.restore()
                d4.restore()

                self.play( ReplacementTransform(d1,col1[4]),**play_kw_fast )
                self.play( ReplacementTransform(d2,col2[4]),**play_kw_fast )
                self.play( ReplacementTransform(d3,col3[4]),**play_kw_fast )
                self.play( ReplacementTransform(d4,col4[4]),**play_kw_fast )

        #SHOW e1

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[3], end=col2[4],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[4], end=col2[3],buff=0.1).set_color(BLUE) )

                rectver.generate_target()
                rectver.target.become( SurroundingRectangle( col1[3:5] ).set_color(ORANGE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col2[3:5] ).set_color(GREEN) )

                self.play(MoveToTarget(rectver),MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2),**play_kw_fast)

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

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col1[5] ).set_color(RED) )
                self.play(MoveToTarget(rectelem),**play_kw_fast)

                self.play(Write(e1),**play_kw_fast)

                self.play(  FadeToColor(e1[0],YELLOW),
                            FadeToColor(e1[1],WHITE),
                            FadeToColor(e1[2],BLUE),
                            FadeToColor(e1[3],WHITE),
                            FadeToColor(e1[4],BLUE),

                            FadeToColor(col1[3],YELLOW),FadeToColor(col2[3],BLUE),
                            FadeToColor(col1[4],BLUE),  FadeToColor(col2[4],YELLOW), **play_kw_fast
                        )

                self.wait(restore_time)
                
                colgr.restore()
                e1.restore()

        #SHOW e2

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[3], end=col3[4],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[4], end=col3[3],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col3[3:5] ).set_color(GREEN) )

                self.play(MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2),**play_kw_fast)

                e2 = Tex(   r"{ {c_1 \cdot 0 ",
                            r"-",
                            r"d_1 \cdot c_3}",
                            r"\over",
                            r"{(-d_1)} } }",
                            color=WHITE
                        ).scale(0.5)

                e2.next_to(col2[5],ORIGIN)
                e2.save_state()

                col2[5].replace(e2,stretch=True)

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col2[5] ).set_color(RED) )
                self.play(MoveToTarget(rectelem),**play_kw_fast)

                self.play(Write(e2),**play_kw_fast)

                self.play(  FadeToColor(e2[0],YELLOW),
                            FadeToColor(e2[1],WHITE),
                            FadeToColor(e2[2],BLUE),
                            FadeToColor(e2[3],WHITE),
                            FadeToColor(e2[4],BLUE),

                            FadeToColor(col1[3],YELLOW),FadeToColor(col3[3],BLUE),
                            FadeToColor(col1[4],BLUE),  FadeToColor(col3[4],YELLOW), **play_kw_fast
                        )

                self.wait(restore_time)
                
                colgr.restore()
                e2.restore()

        #SHOW e3

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[3], end=col4[4],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[4], end=col4[3],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col4[3:5] ).set_color(GREEN) )

                self.play(MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2),**play_kw_fast)

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col3[5] ).set_color(RED) )
                self.play(MoveToTarget(rectelem),**play_kw_fast)

                self.play(Write(col3[5]),**play_kw_fast)

        #SHOW e4

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[3], end=col5[4],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[4], end=col5[3],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col5[3:5] ).set_color(GREEN) )

                self.play(MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2),**play_kw_fast)

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col4[5] ).set_color(RED) )
                self.play(MoveToTarget(rectelem),**play_kw_fast)

                self.play(Write(col4[5]),**play_kw_fast)

        #SHOW e5 (0)                
                
                self.play(Write(col5[5]),**play_kw_fast)

                self.play( ReplacementTransform(e1,col1[5]),**play_kw_fast )
                self.play( ReplacementTransform(e2,col2[5]),**play_kw_fast )

        #SHOW f1

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[4], end=col2[5],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[5], end=col2[4],buff=0.1).set_color(BLUE) )

                rectver.generate_target()
                rectver.target.become( SurroundingRectangle( col1[4:6] ).set_color(ORANGE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col2[4:6] ).set_color(GREEN) )

                self.play(MoveToTarget(rectver),MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2),**play_kw_fast)

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

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col1[6] ).set_color(RED) )
                self.play(MoveToTarget(rectelem),**play_kw_fast)

                self.play(Write(f1),**play_kw_fast)

                self.play(  FadeToColor(f1[0],YELLOW),
                            FadeToColor(f1[1],WHITE),
                            FadeToColor(f1[2],BLUE),
                            FadeToColor(f1[3],WHITE),
                            FadeToColor(f1[4],BLUE),

                            FadeToColor(col1[4],YELLOW),FadeToColor(col2[4],BLUE),
                            FadeToColor(col1[5],BLUE),  FadeToColor(col2[5],YELLOW), **play_kw_fast
                        )

                self.wait(restore_time)
                
                colgr.restore()
                f1.restore()

        #SHOW f2

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[4], end=col3[5],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[5], end=col3[4],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col3[4:6] ).set_color(GREEN) )

                self.play(MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2),**play_kw_fast)

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col2[6] ).set_color(RED) )
                self.play(MoveToTarget(rectelem),**play_kw_fast)

                self.play(Write(col2[6]),**play_kw_fast)

        #SHOW f3

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[4], end=col4[5],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[5], end=col4[4],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col4[4:6] ).set_color(GREEN) )

                self.play(MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2),**play_kw_fast)

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col3[6] ).set_color(RED) )
                self.play(MoveToTarget(rectelem),**play_kw_fast)

                self.play(Write(col3[6]),**play_kw_fast)

        #SHOW f4

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[4], end=col5[5],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[5], end=col5[4],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col5[4:6] ).set_color(GREEN) )

                self.play(MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2),**play_kw_fast)

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col4[6] ).set_color(RED) )
                self.play(MoveToTarget(rectelem),**play_kw_fast)

                self.play(Write(col4[6]),**play_kw_fast)

        #SHOW f5 (0)

                self.play(Write(col5[6]),**play_kw_fast)

                self.play( ReplacementTransform(f1,col1[6]),**play_kw_fast )

        #SHOW g1

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[5], end=col2[6],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[6], end=col2[5],buff=0.1).set_color(BLUE) )

                rectver.generate_target()
                rectver.target.become( SurroundingRectangle( col1[5:7] ).set_color(ORANGE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col2[5:7] ).set_color(GREEN) )

                self.play(MoveToTarget(rectver),MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2),**play_kw_fast)

                g1 = Tex(   r"{ {e_1 \cdot 0 ",
                            r"-",
                            r"f_1 \cdot e_2}",
                            r"\over",
                            r"{(-f_1)} } }",
                            color=WHITE
                        ).scale(0.5)

                g1.next_to(col1[7],ORIGIN)
                g1.save_state()

                col1[7].replace(g1,stretch=True) 

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col1[7] ).set_color(RED) )
                self.play(MoveToTarget(rectelem),**play_kw_fast)

                self.play(Write(g1),**play_kw_fast)

                self.play(  FadeToColor(g1[0],YELLOW),
                            FadeToColor(g1[1],WHITE),
                            FadeToColor(g1[2],BLUE),
                            FadeToColor(g1[3],WHITE),
                            FadeToColor(g1[4],BLUE),

                            FadeToColor(col1[5],YELLOW),FadeToColor(col2[5],BLUE),
                            FadeToColor(col1[6],BLUE),  FadeToColor(col2[6],YELLOW), **play_kw_fast
                        )

                self.wait(restore_time)
                
                colgr.restore()
                g1.restore()

        #SHOW g2

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[5], end=col3[6],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[6], end=col3[5],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col3[5:7] ).set_color(GREEN) )

                self.play(MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2),**play_kw_fast)

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col2[7] ).set_color(RED) )
                self.play(MoveToTarget(rectelem),**play_kw_fast)

                self.play(Write(col2[7]),**play_kw_fast)

        #SHOW g3

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[5], end=col4[6],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[6], end=col4[5],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col4[5:7] ).set_color(GREEN) )

                self.play(MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2),**play_kw_fast)

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col3[7] ).set_color(RED) )
                self.play(MoveToTarget(rectelem),**play_kw_fast)

                self.play(Write(col3[7]),**play_kw_fast)

        #SHOW g4

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[5], end=col5[6],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[6], end=col5[5],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col5[5:7] ).set_color(GREEN) )

                self.play(MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2),**play_kw_fast)

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col4[7] ).set_color(RED) )
                self.play(MoveToTarget(rectelem),**play_kw_fast)

                self.play(Write(col4[7]),**play_kw_fast)

        #SHOW g5 (0)

                self.play(Write(col5[7]),**play_kw_fast)

                self.play( ReplacementTransform(g1,col1[7]),**play_kw_fast )

                self.wait(2)

                self.play(FadeOut(rectelem), FadeOut(crl1), FadeOut(crl2), FadeOut(rectver), FadeOut(recthor))

                self.wait(2)

        # ORIENTATE COLUMNS

                colgr.generate_target()
                colgr.target.arrange(buff=MED_LARGE_BUFF).to_corner(LEFT)
                self.play(MoveToTarget(colgr))

                self.play( FadeOut(colgr[1:6]) )


        #SHOW THE NUMBERLINE

                n_line = NumberLine(
                x_min=-5,  x_max=5,
                tick_frequency=1,
                unit_size=1,
                include_numbers=True,
                numbers_to_exclude=[-5,-4,-3,-2,-1,1,2,3,4,5] )

                # vertline = DashedLine(start=DOWN/3,end=UP/3).set_opacity(0.3).move_to(n_line.n2p(0)) #uncomment if needed
                # tdots1 = Tex(r"\dots").set_opacity(0.5).next_to(n_line,RIGHT) #uncomment if needed
                # tdots2 = Tex(r"\dots").set_opacity(0.5).next_to(n_line,LEFT) #uncomment if needed

                nlinegroup = VGroup(n_line)
                nlinegroup.scale(0.8)
                nlinegroup.next_to(col1,RIGHT,LARGE_BUFF).shift(RIGHT)


        #SHOW THE COEFFICIENTS

                col1box = SurroundingRectangle(col1)
                self.play(ShowCreation(col1box))

                col1brace = Brace(col1box,RIGHT)
                col1deg = Tex(r"{(n+1)}",r"=",r"8 \text{ rows}").scale(0.8).next_to(col1brace,RIGHT,SMALL_BUFF)
                col1deg[0].set_color(RED)

                self.play(ShowCreation(col1brace),Write(col1deg))
                
                self.wait(1)

                self.play(FadeOut(saycalc))

                
                self.play(  FadeToColor(col1[0],BLUE_E), FadeToColor(col1[1],TEAL_E), FadeToColor(col1[2],GREEN_E), FadeToColor(col1[3],YELLOW_E),  
                            FadeToColor(col1[4],RED_E), FadeToColor(col1[5],MAROON_E), FadeToColor(col1[6],PURPLE_E), FadeToColor(col1[7],GOLD_E), 
                        )

                samesign1 = Tex(r"\text{The polynomial is a Hurwitz polynomial if and only if all }",r"(n+1)")
                samesign2 = Tex(r"\text{elements of the first column are non-zero and have the same sign.}")
                samesign1[1].set_color(RED)
                samesign = VGroup(samesign1,samesign2).arrange(DOWN)
                samesign.scale(0.8).next_to(col1box,RIGHT,LARGE_BUFF).shift(DOWN*2)
                self.play(Write(samesign))

                self.play(FadeOut(col1brace),FadeOut(col1deg))

                self.play(ShowCreation(nlinegroup))

                self.wait(1)
                
                dota7 = Dot(color=BLUE_E)
                dota6 = Dot(color=TEAL_E)
                dotb1 = Dot(color=GREEN_E)
                dotc1 = Dot(color=YELLOW_E)
                dotd1 = Dot(color=RED_E)
                dote1 = Dot(color=MAROON_E)
                dotf1 = Dot(color=PURPLE_E)
                dotg1 = Dot(color=GOLD_E)

                dota7.move_to(n_line.n2p(0.5))
                dota6.move_to(n_line.n2p(1))
                dotb1.move_to(n_line.n2p(1.5))
                dotc1.move_to(n_line.n2p(2))
                dotd1.move_to(n_line.n2p(2.5))
                dote1.move_to(n_line.n2p(3))
                dotf1.move_to(n_line.n2p(3.5))
                dotg1.move_to(n_line.n2p(4))


                self.play(  FadeIn(dota7, scale=0.5), FadeIn(dota6, scale=0.5), FadeIn(dotb1, scale=0.5), FadeIn(dotc1, scale=0.5), 
                            FadeIn(dotd1, scale=0.5), FadeIn(dote1, scale=0.5), FadeIn(dotf1, scale=0.5), FadeIn(dotg1, scale=0.5) 
                        )

                a7x = Tex(r"a_7").next_to(dota7,DOWN,buff=0).scale(0.5).set_color(BLUE_E)
                a6x = Tex(r"a_6").next_to(dota6,DOWN,buff=0).scale(0.5).set_color(TEAL_E)
                b1x = Tex(r"b_1").next_to(dotb1,DOWN,buff=0).scale(0.5).set_color(GREEN_E)
                c1x = Tex(r"c_1").next_to(dotc1,DOWN,buff=0).scale(0.5).set_color(YELLOW_E)
                d1x = Tex(r"d_1").next_to(dotd1,DOWN,buff=0).scale(0.5).set_color(RED_E)
                e1x = Tex(r"e_1").next_to(dote1,DOWN,buff=0).scale(0.5).set_color(MAROON_E)
                f1x = Tex(r"f_1").next_to(dotf1,DOWN,buff=0).scale(0.5).set_color(PURPLE_E)
                g1x = Tex(r"g_1").next_to(dotg1,DOWN,buff=0).scale(0.5).set_color(GOLD_E)

                self.play(Write(a7x), Write(a6x), Write(b1x), Write(c1x), Write(d1x), Write(e1x), Write(f1x), Write(g1x))

                checkmark = Checkmark().next_to(n_line,UP)
                exmark = Exmark()
                checkmark.set_color(GREEN)
                exmark.set_color(RED_C).next_to(n_line,UP)
                hp = Text("HP").set_color(GREEN).next_to(checkmark,RIGHT)
                nohp = Text("not HP").set_color(RED_C).next_to(exmark,RIGHT)
                self.play(Write(checkmark), Write(hp))

                self.play( dota7.animate.move_to(n_line.n2p(4.5)), MaintainPositionRelativeTo(a7x,dota7) )

                self.wait(0.5)

                self.play( dotc1.animate.move_to(n_line.n2p(0)), MaintainPositionRelativeTo(c1x,dotc1), FadeTransform(checkmark,exmark), FadeTransform(hp,nohp) )

                self.wait(0.5)

                self.play( dota6.animate.move_to(n_line.n2p(-2)), MaintainPositionRelativeTo(a6x,dota6) )
                self.play( dotc1.animate.move_to(n_line.n2p(-1)), MaintainPositionRelativeTo(c1x,dotc1) )

                self.wait(0.5)
                
                self.play( dota7.animate.move_to(n_line.n2p(-3)), MaintainPositionRelativeTo(a7x,dota7), 
                           dotb1.animate.move_to(n_line.n2p(-0.5)), MaintainPositionRelativeTo(b1x,dotb1),
                           dotb1.animate.move_to(n_line.n2p(-0.5)), MaintainPositionRelativeTo(b1x,dotb1),
                           dotd1.animate.move_to(n_line.n2p(-1.5)), MaintainPositionRelativeTo(d1x,dotd1),
                           dote1.animate.move_to(n_line.n2p(-3.5)), MaintainPositionRelativeTo(e1x,dote1),
                           dotf1.animate.move_to(n_line.n2p(-4)), MaintainPositionRelativeTo(f1x,dotf1)
                        )

                self.wait(0.5)
                
                self.play( dotg1.animate.move_to(n_line.n2p(-4.5)), MaintainPositionRelativeTo(g1x,dotg1), FadeTransform(exmark,checkmark), FadeTransform(nohp,hp) )

                self.wait(5)

                self.play(*[FadeOut(mob)for mob in self.mobjects])

                self.wait(2)
                