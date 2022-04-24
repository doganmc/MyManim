from manimlib import *
import numpy as np

class FullTable(Scene):
        def construct(self):

        #SHOW TEMPLATE POLYNOM AND ZICK-ZACK
                self.wait(1)
                poly1 = Tex(   
                                r"{p(s) =",
                                r"{ ", r"a_7", r"s^6", r"+", r"a_6" ,r"s^6", r"+", r"a_5", r"s^5", r"+",r"a_4",r"s^4",r"+",r"a_3",r"s^3",r"+",r"a_2",r"s^2",r"+",r"a_1",r"s",r"+",r"a_0", r"}", r"}",
                                color=WHITE
                        ).shift(UP*2)

                self.play( Write(poly1) )
                
                # for i in poly1:
                #     self.play(Write(i))

                self.wait(3)

                self.play(      FadeToColor( poly1[1],BLUE ), FadeToColor( poly1[4],BLUE ),
                                FadeToColor( poly1[7],YELLOW ), FadeToColor( poly1[10],YELLOW ),
                                FadeToColor( poly1[13],PINK ), FadeToColor( poly1[16],PINK ),
                                FadeToColor( poly1[19],ORANGE ), FadeToColor( poly1[22],ORANGE ), )

                self.wait(2)

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
                an6.next_to(n3ton4,UR)
                n6ton7.next_to(an6,DOWN)
                an7.next_to(n6ton7,DOWN)

                n7ton8.next_to(an7,UR)     
                an8.next_to(n7ton8,UR)
                n8ton9.next_to(an8,DOWN)
                an9.next_to(n8ton9,DOWN)

                zzgroup=VGroup(an,nton1,an1,n1ton2,an2,n2ton3,an3,n3ton4,an6,n6ton7,an7,n7ton8,an8,n8ton9,an9).next_to(poly1,DOWN,buff=LARGE_BUFF)
                
                play_kw = {"run_time": 4}
                self.play(Write(zzgroup[0:11]),**play_kw)

                self.wait(4)

                self.play(Write(zzgroup[11:16]))

                self.wait(4)

                # poly1.generate_target()
                # poly1.target.to_corner(UR)
                # self.play(MoveToTarget(poly1))

                # zzgroup.generate_target()
                # zzgroup.target.to_corner(UL)
                # self.play(MoveToTarget(zzgroup))

                #self.play(FadeToColor(poly1,WHITE))
                self.play(FadeOut(poly1))













 ###################################################################################################################################################################               
                row1 = Tex(r"a_7",r"\hspace{0.25cm}",r"a_5",r"\hspace{0.25cm}",r"a_3",r"\hspace{0.25cm}",r"a_1",r"\hspace{0.25cm}",r"\hdots").shift(UP*3 + LEFT*4.5)
                row2 = Tex(r"a_6",r"\hspace{0.25cm}",r"a_4",r"\hspace{0.25cm}",r"a_2",r"\hspace{0.25cm}",r"a_0",r"\hspace{0.25cm}",r"\hdots").next_to(row1,DOWN*1.5)
                row3 = Tex(r"b_1",r"\hspace{0.25cm}",r"b_2",r"\hspace{0.25cm}",r"b_3",r"\hspace{0.25cm}",r"b_4",r"\hspace{0.25cm}",r"\hdots").next_to(row2,DOWN*1.5)
                row4 = Tex(r"c_1",r"\hspace{0.25cm}",r"c_2",r"\hspace{0.25cm}",r"c_3",r"\hspace{0.25cm}",r"c_4",r"\hspace{0.25cm}",r"\hdots").next_to(row3,DOWN*1.5)
                row5 = Tex(r"d_1",r"\hspace{0.25cm}",r"d_2",r"\hspace{0.25cm}",r"d_3",r"\hspace{0.25cm}",r"d_4",r"\hspace{0.25cm}",r"\hdots").next_to(row4,DOWN*1.5)
                row6 = Tex(r"\vdots",r"\hspace{0.5cm}",r"\vdots").next_to(row5,DOWN*1.5).shift(LEFT*1.25)
                rowgr = VGroup(row1,row2,row3,row4,row5,row6)

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
                coltgr = VGroup(colt1,colt2,colt3,colt4,colt5).arrange(RIGHT,buff=LARGE_BUFF*2)

                colgr = VGroup(col1,col2,col3,col4,col5).arrange(RIGHT,buff=LARGE_BUFF*2)



                
                colzz = VGroup( col1[0:2], col2[0:2], col3[0:2], col4[0:2], col5[0:2] )
                self.play(TransformMatchingParts(zzgroup,colzz))

                self.wait(15)
                #self.play( Write(col1[0:2]) ,Write(col2[0:2]), Write(col3[0:2]), Write(col4[0:2]), Write(col5[0:2]) )
                
                #rowgr.save_state()
                colgr.save_state()

                rectver = SurroundingRectangle( col1[0:2] ).set_color(ORANGE)
                recthor = SurroundingRectangle( col2[0:2] ).set_color(GREEN)

                crl1 = Line(start=col1[0], end=col2[1],buff=0.1).set_color(YELLOW)
                crl2 = Line(start=col1[1], end=col2[0],buff=0.1).set_color(BLUE)

                self.play( ShowCreation(rectver), ShowCreation(recthor), ShowCreation(crl1), ShowCreation(crl2) ) 





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

                #self.play(ReplacementTransform(col1[2],b1))


                # rectelem.generate_target()
                # rectelem.target.become( SurroundingRectangle( col1[2] ).set_color(RED) )
                # self.play(MoveToTarget(rectelem))
                rectelem = SurroundingRectangle( col1[2] ).set_color(RED)
                self.play(ShowCreation(rectelem))

                #CameraFrame
                frame = self.camera.frame
                self.camera.frame.save_state()
                frame2 = frame.copy()
                frame2.set_width(5)
                frame2.move_to(rectelem.get_center())
                frame2.shift(UR/2)
                frame2.shift(RIGHT/3)
                self.play(Transform(frame, frame2))

                self.play(Write(b1),run_time = 4)

                self.play(  col1[0].set_color, YELLOW,  col2[0].set_color(BLUE),
                            col1[1].set_color, BLUE,    col2[1].set_color(YELLOW),
                        )

                self.play(  b1[0].set_color, YELLOW,
                            b1[1].set_color, WHITE,
                            b1[2].set_color, BLUE,
                            b1[3].set_color, WHITE,
                            b1[4].set_color, BLUE,
                        )


                self.wait(15)


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

                self.play(Restore(self.camera.frame))


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

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[0], end=col4[1],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[1], end=col4[0],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col4[0:2] ).set_color(GREEN) )

                # rectelem.generate_target()
                # rectelem.target.become( SurroundingRectangle( col3[2] ).set_color(RED) )

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

                #self.play(ReplacementTransform(col3[2],b3))


                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col3[2] ).set_color(RED) )
                self.play(MoveToTarget(rectelem))

                self.play(Write(b3))

                self.play(  col1[0].set_color, YELLOW,  col4[0].set_color(BLUE),
                            col1[1].set_color, BLUE,    col4[1].set_color(YELLOW),
                        )

                self.play(  b3[0].set_color, YELLOW,
                            b3[1].set_color, WHITE,
                            b3[2].set_color, BLUE,
                            b3[3].set_color, WHITE,
                            b3[4].set_color, BLUE,
                        )


                #self.wait(1)
                
                colgr.restore()
                b3.restore()

                #self.play(FadeOut(b1),FadeOut(b2),FadeOut(b3))
                #self.wait(1)

        #SHOW b4

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[0], end=col5[1],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[1], end=col5[0],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col5[0:2] ).set_color(GREEN) )

                # rectelem.generate_target()
                # rectelem.target.become( SurroundingRectangle( col4[2] ).set_color(RED) )

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
                #self.play(ReplacementTransform(col4[2],b4))

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col4[2] ).set_color(RED) )
                self.play(MoveToTarget(rectelem))

                self.play(Write(b4))

                self.play(  col1[0].set_color, YELLOW,  col5[0].set_color(BLUE),
                            col1[1].set_color, BLUE,    col5[1].set_color(YELLOW),
                        )

                self.play(  b4[0].set_color, YELLOW,
                            b4[1].set_color, WHITE,
                            b4[2].set_color, BLUE,
                            b4[3].set_color, WHITE,
                            b4[4].set_color, BLUE,
                        )


                #self.wait(1)

                self.play( Write(col5[2]) )
                
                colgr.restore()
                b4.restore()

                #self.play(FadeOut(rectelem))

                self.play( ReplacementTransform(b1,col1[2]) )
                self.play( ReplacementTransform(b2,col2[2]) )
                self.play( ReplacementTransform(b3,col3[2]) )
                self.play( ReplacementTransform(b4,col4[2]) )

                # k1 = Tex(r"b_1").next_to(col1[2],ORIGIN)
                # k2 = Tex(r"b_2").next_to(col2[2],ORIGIN)
                # k3 = Tex(r"b_3").next_to(col3[2],ORIGIN)
                # k4 = Tex(r"0").next_to(col4[2],ORIGIN)

                # self.play(ReplacementTransform(b1,k1), ReplacementTransform(b2,k2), ReplacementTransform(b3,k3), ReplacementTransform(b4,k4) )

                # col1[2].generate_target()
                # col1[2].target.replace( Tex(r"b_1").next_to(col1[2],ORIGIN) )

                # col2[2].generate_target()
                # col2[2].target.replace( Tex(r"b_2").next_to(col2[2],ORIGIN) )

                # col3[2].generate_target()
                # col3[2].target.replace( Tex(r"b_3").next_to(col3[2],ORIGIN) )

                # col4[2].generate_target()
                # col4[2].target.replace( Tex(r"0").next_to(col4[2],ORIGIN) )

                # col1[2] = Tex(r"b_1").next_to(col1[2],ORIGIN)
                # col2[2] = Tex(r"b_2").next_to(col2[2],ORIGIN)
                # col3[2] = Tex(r"b_3").next_to(col1[2],ORIGIN)
                # col4[2] = Tex(r"0").next_to(col2[2],ORIGIN)

                #self.play( Transform(b1,col1[2]), Transform(b2,col2[2]), Transform(b3,col3[2]), Transform(b4,col4[2]) )

        

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

                c1 = Tex(   r"{ {a_6 \cdot b_2 ",
                            r"-",
                            r"b_1 \cdot a_4}",
                            r"\over",
                            r"{(-b_1)} } }",
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

                c2 = Tex(   r"{ {a_6 \cdot b_3 ",
                            r"-",
                            r"b_1 \cdot a_2}",
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

        #SHOW c3

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[1], end=col4[2],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[2], end=col4[1],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col4[1:3] ).set_color(GREEN) )

                # rectelem.generate_target()
                # rectelem.target.become( SurroundingRectangle( col3[3] ).set_color(RED) )

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

                #self.play(ReplacementTransform(col3[3],c3))
                col3[3].replace(c3,stretch=True)     

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col3[3] ).set_color(RED) )
                self.play(MoveToTarget(rectelem))

                self.play(Write(c3))

                self.play(  col1[1].set_color, YELLOW,  col4[1].set_color, BLUE,
                            col1[2].set_color, BLUE,    col4[2].set_color, YELLOW,
                        )

                self.play(  c3[0].set_color, YELLOW,
                            c3[1].set_color, WHITE,
                            c3[2].set_color, BLUE,
                            c3[3].set_color, WHITE,
                            c3[4].set_color, BLUE,
                        )


                #self.wait(1)
                
                colgr.restore()
                c3.restore()


        #SHOW c4

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[1], end=col5[2],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[2], end=col5[1],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col5[1:3] ).set_color(GREEN) )

                # rectelem.generate_target()
                # rectelem.target.become( SurroundingRectangle( col4[3] ).set_color(RED) )

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
                #self.play(ReplacementTransform(col4[3],c4))

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col4[3] ).set_color(RED) )
                self.play(MoveToTarget(rectelem))

                self.play(Write(c4))

                self.play(  col1[1].set_color, YELLOW,  col5[1].set_color, BLUE,
                            col1[2].set_color, BLUE,    col5[2].set_color, YELLOW,
                        )

                self.play(  c4[0].set_color, YELLOW,
                            c4[1].set_color, WHITE,
                            c4[2].set_color, BLUE,
                            c4[3].set_color, WHITE,
                            c4[4].set_color, BLUE,
                        )


                #self.wait(1)

                #self.add(col5[3])
                self.play(Write(col5[3]))
                
                colgr.restore()
                c4.restore()

                #self.play(FadeOut(rectelem))

                # l1 = Tex(r"c_1").next_to(col1[3],ORIGIN)
                # l2 = Tex(r"c_2").next_to(col2[3],ORIGIN)
                # l3 = Tex(r"c_3").next_to(col3[3],ORIGIN)
                # l4 = Tex(r"0").next_to(col4[3],ORIGIN)

                # self.play(ReplacementTransform(c1,l1), ReplacementTransform(c2,l2), ReplacementTransform(c3,l3), ReplacementTransform(c4,l4) )

                # col1[3].generate_target()
                # col1[3].target.become( Tex(r"c_1").next_to(col1[2],ORIGIN) )

                # col2[3].generate_target()
                # col2[3].target.become( Tex(r"c_2").next_to(col2[2],ORIGIN) )

                # col3[3].generate_target()
                # col3[3].target.become( Tex(r"c_3").next_to(col3[2],ORIGIN) )

                # col4[3].generate_target()
                # col4[3].target.become( Tex(r"0").next_to(col4[2],ORIGIN) )
                

                self.play( ReplacementTransform(c1,col1[3]) )
                self.play( ReplacementTransform(c2,col2[3]) )
                self.play( ReplacementTransform(c3,col3[3]) )
                self.play( ReplacementTransform(c4,col4[3]) )

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

                self.play(MoveToTarget(rectver),MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2),run_time=0.1)

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
                self.play(MoveToTarget(rectelem),run_time=0.1)

                self.play(Write(d1),run_time=0.1)

                self.play(  col1[2].set_color, YELLOW,  col2[2].set_color, BLUE,
                            col1[3].set_color, BLUE,    col2[3].set_color, YELLOW,
                        run_time=0.1)

                self.play(  d1[0].set_color, YELLOW,
                            d1[1].set_color, WHITE,
                            d1[2].set_color, BLUE,
                            d1[3].set_color, WHITE,
                            d1[4].set_color, BLUE,
                        run_time=0.1)


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

                self.play(MoveToTarget(rectver),MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2),run_time=0.1)

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
                self.play(MoveToTarget(rectelem),run_time=0.1)

                self.play(Write(d2),run_time=0.1)

                self.play(  col1[2].set_color, YELLOW,  col3[2].set_color, BLUE,
                            col1[3].set_color, BLUE,    col3[3].set_color, YELLOW,
                        run_time=0.1)

                self.play(  d2[0].set_color, YELLOW,
                            d2[1].set_color, WHITE,
                            d2[2].set_color, BLUE,
                            d2[3].set_color, WHITE,
                            d2[4].set_color, BLUE,
                        run_time=0.1)


                #self.wait(1)
                
                colgr.restore()
                d2.restore()

        #SHOW d3

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[2], end=col4[3],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[3], end=col4[2],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col4[2:4] ).set_color(GREEN) )

                # rectelem.generate_target()
                # rectelem.target.become( SurroundingRectangle( col1[4] ) )

                self.play(MoveToTarget(rectver),MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2),run_time=0.1)

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
                self.play(MoveToTarget(rectelem),run_time=0.1)

                self.play(Write(d3),run_time=0.1)

                self.play(  col1[2].set_color, YELLOW,  col4[2].set_color, BLUE,
                            col1[3].set_color, BLUE,    col4[3].set_color, YELLOW,
                        run_time=0.1)

                self.play(  d3[0].set_color, YELLOW,
                            d3[1].set_color, WHITE,
                            d3[2].set_color, BLUE,
                            d3[3].set_color, WHITE,
                            d3[4].set_color, BLUE,
                        run_time=0.1)


                #self.wait(1)
                
                colgr.restore()
                d3.restore()

                # # self.play(FadeOut(d1),FadeOut(d2),FadeOut(d3))

                # # self.play(FadeOut(rectb), FadeOut(rectver), FadeOut(recthor), FadeOut(rectelem) ) 

                # # self.wait(2)

        #SHOW d4

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[2], end=col5[3],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[3], end=col5[2],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col5[2:4] ).set_color(GREEN) )

                # rectelem.generate_target()
                # rectelem.target.become( SurroundingRectangle( col1[4] ) )

                self.play(MoveToTarget(rectver),MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2),run_time=0.1)

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
                #self.play(ReplacementTransform(col1[4],d1))

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col4[4] ).set_color(RED) )
                self.play(MoveToTarget(rectelem),run_time=0.1)

                self.play(Write(d4),run_time=0.1)

                self.play(  col1[2].set_color, YELLOW,  col5[2].set_color, BLUE,
                            col1[3].set_color, BLUE,    col5[3].set_color, YELLOW,
                        run_time=0.1)

                self.play(  d4[0].set_color, YELLOW,
                            d4[1].set_color, WHITE,
                            d4[2].set_color, BLUE,
                            d4[3].set_color, WHITE,
                            d4[4].set_color, BLUE,
                        run_time=0.1)


                #self.wait(1)

                self.play(Write(col5[4]),run_time=0.1)
                
                colgr.restore()
                d4.restore()

                self.play( ReplacementTransform(d1,col1[4]),run_time=0.1 )
                self.play( ReplacementTransform(d2,col2[4]),run_time=0.1 )
                self.play( ReplacementTransform(d3,col3[4]),run_time=0.1 )
                self.play( ReplacementTransform(d4,col4[4]),run_time=0.1 )


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

                self.play(MoveToTarget(rectver),MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2),run_time=0.1)

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
                self.play(MoveToTarget(rectelem),run_time=0.1)

                self.play(Write(e1),run_time=0.1)

                self.play(  col1[3].set_color, YELLOW,  col2[3].set_color, BLUE,
                            col1[4].set_color, BLUE,    col2[4].set_color, YELLOW,
                        run_time=0.1)

                self.play(  e1[0].set_color, YELLOW,
                            e1[1].set_color, WHITE,
                            e1[2].set_color, BLUE,
                            e1[3].set_color, WHITE,
                            e1[4].set_color, BLUE,
                        run_time=0.1)


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

                self.play(MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2),run_time=0.1)

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
                self.play(MoveToTarget(rectelem),run_time=0.1)

                self.play(Write(e2),run_time=0.1)

                self.play(  col1[3].set_color, YELLOW,  col2[3].set_color, BLUE,
                            col1[4].set_color, BLUE,    col2[4].set_color, YELLOW,
                        run_time=0.1)

                self.play(  e2[0].set_color, YELLOW,
                            e2[1].set_color, WHITE,
                            e2[2].set_color, BLUE,
                            e2[3].set_color, WHITE,
                            e2[4].set_color, BLUE,
                        run_time=0.1)


                #self.wait(1)
                
                colgr.restore()
                e2.restore()




        #SHOW e3

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[3], end=col4[4],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[4], end=col4[3],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col4[3:5] ).set_color(GREEN) )

                # rectelem.generate_target()
                # rectelem.target.become( SurroundingRectangle( col1[4] ) )

                self.play(MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2),run_time=0.1)

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col3[5] ).set_color(RED) )
                self.play(MoveToTarget(rectelem),run_time=0.1)

                self.play(Write(col3[5]),run_time=0.1)


        #SHOW e4

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[3], end=col5[4],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[4], end=col5[3],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col5[3:5] ).set_color(GREEN) )

                # rectelem.generate_target()
                # rectelem.target.become( SurroundingRectangle( col1[4] ) )

                self.play(MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2),run_time=0.1)

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col4[5] ).set_color(RED) )
                self.play(MoveToTarget(rectelem),run_time=0.1)

                self.play(Write(col4[5]),run_time=0.1)



        #SHOW e5 (0)                
                
                self.play(Write(col5[5]),run_time=0.1)


                self.play( ReplacementTransform(e1,col1[5]),run_time=0.1 )
                self.play( ReplacementTransform(e2,col2[5]),run_time=0.1 )

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

                self.play(MoveToTarget(rectver),MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2),run_time=0.1)

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
                self.play(MoveToTarget(rectelem),run_time=0.1)

                self.play(Write(f1),run_time=0.1)

                self.play(  col1[4].set_color, YELLOW,  col2[4].set_color, BLUE,
                            col1[5].set_color, BLUE,    col2[5].set_color, YELLOW,
                        run_time=0.1)

                self.play(  f1[0].set_color, YELLOW,
                            f1[1].set_color, WHITE,
                            f1[2].set_color, BLUE,
                            f1[3].set_color, WHITE,
                            f1[4].set_color, BLUE,
                        run_time=0.1)


                #self.wait(1)
                
                colgr.restore()
                f1.restore()

                self.play(FadeOut(rectelem),run_time=0.1)


        #SHOW f2

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[4], end=col3[5],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[5], end=col3[4],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col3[4:6] ).set_color(GREEN) )

                self.play(MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2),run_time=0.1)

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col2[6] ).set_color(RED) )
                self.play(MoveToTarget(rectelem),run_time=0.1)

                self.play(Write(col2[6]),run_time=0.1)

        #SHOW f3

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[4], end=col4[5],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[5], end=col4[4],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col4[4:6] ).set_color(GREEN) )

                self.play(MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2),run_time=0.1)

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col3[6] ).set_color(RED) )
                self.play(MoveToTarget(rectelem),run_time=0.1)

                self.play(Write(col3[6]),run_time=0.1)

        #SHOW f4

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[4], end=col5[5],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[5], end=col5[4],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col5[4:6] ).set_color(GREEN) )

                self.play(MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2),run_time=0.1)

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col4[6] ).set_color(RED) )
                self.play(MoveToTarget(rectelem),run_time=0.1)

                self.play(Write(col4[6]),run_time=0.1)

        #SHOW f5 (0)

                self.play(Write(col5[6]),run_time=0.1)

                self.play( ReplacementTransform(f1,col1[6]),run_time=0.1 )

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

                self.play(MoveToTarget(rectver),MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2),run_time=0.1)

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
                self.play(MoveToTarget(rectelem),run_time=0.1)

                self.play(Write(g1),run_time=0.1)

                self.play(  col1[5].set_color, YELLOW,  col2[5].set_color, BLUE,
                            col1[6].set_color, BLUE,    col2[6].set_color, YELLOW,
                        run_time=0.1)

                self.play(  g1[0].set_color, YELLOW,
                            g1[1].set_color, WHITE,
                            g1[2].set_color, BLUE,
                            g1[3].set_color, WHITE,
                            g1[4].set_color, BLUE,
                        run_time=0.1)


                #self.wait(1)
                
                colgr.restore()
                g1.restore()

                #self.play( ReplacementTransform(g1,col1[7]) )

                #self.play(Write(col2[7]),Write(col3[7]),Write(col4[7]),Write(col5[7]))




        #SHOW g2

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[5], end=col3[6],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[6], end=col3[5],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col3[5:7] ).set_color(GREEN) )

                self.play(MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2),run_time=0.1)

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col2[7] ).set_color(RED) )
                self.play(MoveToTarget(rectelem),run_time=0.1)

                self.play(Write(col2[7]),run_time=0.1)

        #SHOW g3

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[5], end=col4[6],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[6], end=col4[5],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col4[5:7] ).set_color(GREEN) )

                self.play(MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2),run_time=0.1)

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col3[7] ).set_color(RED) )
                self.play(MoveToTarget(rectelem),run_time=0.1)

                self.play(Write(col3[7]),run_time=0.1)

        #SHOW g4

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[5], end=col5[6],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[6], end=col5[5],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col5[5:7] ).set_color(GREEN) )

                self.play(MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2),run_time=0.1)

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col4[7] ).set_color(RED) )
                self.play(MoveToTarget(rectelem),run_time=0.1)

                self.play(Write(col4[7]),run_time=0.1)

        #SHOW g5 (0)

                self.play(Write(col5[7]),run_time=0.1)

                self.play( ReplacementTransform(g1,col1[7]),run_time=0.1 )

                self.wait(2)

                self.play(FadeOut(rectelem), FadeOut(crl1), FadeOut(crl2), FadeOut(rectver), FadeOut(recthor),)

                self.wait(2)


        # ORIENTATE COLUMNS

                colgr.generate_target()
                colgr.target.arrange(buff=MED_LARGE_BUFF).to_corner(LEFT)
                self.play(MoveToTarget(colgr))


        #SHOW THE NUMBERLINE

                n_line = NumberLine(
                x_min=-3,  x_max=3,
                tick_frequency=1,
                unit_size=1,
                include_numbers=False,
                numbers_to_show=np.arange(-3,1,3),
                )

                #n_line.shift(LEFT*3 + DOWN*2.5)
                #n_line.to_corner(RIGHT)
                #self.play( ShowCreation(n_line) )

                vertline = DashedLine(start=DOWN/2,end=UP/2).set_opacity(0.3).move_to(n_line.n2p(0))
                #self.play( ShowCreation(vertline) )

                tdots1 = Tex(r"\hdots").set_opacity(0.5).next_to(n_line,RIGHT)
                tdots2 = Tex(r"\hdots").set_opacity(0.5).next_to(n_line,LEFT)

                nlinegroup = VGroup(n_line,vertline,tdots1,tdots2)
                nlinegroup.scale(0.8)
                nlinegroup.to_corner(RIGHT)
 
                #self.play(ShowCreation(tdots1),ShowCreation(tdots2))

                self.play(ShowCreation(nlinegroup))


        #SHOW THE COEFFICIENTS

                col1box = SurroundingRectangle(col1)
                self.play(ShowCreation(col1box))

                firstcol1 = Tex(r"a_{7}",r">",r"0")
                firstcol2 = Tex(r"a_{6}",r">",r"0")
                firstcol3 = Tex(r"b_1",r">",r"0").set_color(TEAL)
                firstcol4 = Tex(r"c_1",r">",r"0").set_color(ORANGE)
                firstcol5 = Tex(r"d_1",r">",r"0").set_color(BLUE)
                firstcol6 = Tex(r"\vdots")

                firstcols = VGroup(firstcol1,firstcol2,firstcol3,firstcol4,firstcol5,firstcol6)
                firstcols.arrange(DOWN)
                firstcols.next_to(colgr,RIGHT,buff=LARGE_BUFF)

                firstcolbox = SurroundingRectangle(firstcols)

                self.play(Write(firstcols))
                self.play(ShowCreation(firstcolbox))

                self.wait(1)

                dotb1 = Dot(color=TEAL)
                dotc1 = Dot(color=ORANGE)
                dotd1 = Dot(color=BLUE)

                dotb1.move_to(n_line.n2p(0.5))
                dotc1.move_to(n_line.n2p(2.5))
                dotd1.move_to(n_line.n2p(1.5))


                self.play(FadeIn(dotb1, scale=0.5), FadeIn(dotc1, scale=0.5), FadeIn(dotd1, scale=0.5) )

                b1x = firstcol3[0].copy().next_to(dotb1,DOWN,buff=0).scale(0.5).set_color(TEAL)
                c1x = firstcol4[0].copy().next_to(dotc1,DOWN,buff=0).scale(0.5).set_color(ORANGE)
                d1x = firstcol5[0].copy().next_to(dotd1,DOWN,buff=0).scale(0.5).set_color(BLUE)

                self.play(Write(b1x), Write(c1x), Write(d1x))

                checkmark = Checkmark().next_to(vertline,UP)
                exmark = Exmark()
                checkmark.set_color(GREEN)
                exmark.set_color(RED_C).next_to(vertline,UP)
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


"""
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
"""