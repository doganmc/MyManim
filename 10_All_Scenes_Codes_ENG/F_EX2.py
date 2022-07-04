from manimlib import *
import numpy as np
import math

class F_EX2_ENG(Scene):
        def construct(self):
                                
                play_kw_fast = {"run_time": 0.25}
                restore_time = 0.5
                
        # EXAMPLE 2 OPENING SCENE

                self.wait(1)

                intro_words2 = Text("Example 2: A Polynomial With an Unknown Parameter")
                intro_words2.set_color(YELLOW_C).scale(1)

                underline2 = Underline(mobject=intro_words2)
                underline2.set_color(YELLOW_C)

                self.play(Write(intro_words2))

                self.play(ShowCreation(underline2),run_time=1)

                self.wait(3)

                self.play(ShrinkToCenter(intro_words2), ShrinkToCenter(underline2))

                self.wait(1)

                poly1 = Tex(   
                                r"{p(s) =",
                                r"{ ",r"2", r"s^{5}", r"+", r"4" ,r"s^{4}", r"+", r"10", r"s^{3}", r"+",r"12", r"s^{2}", r"+", r"K", r"s", r"+", r"2", r"}", r"}",
                                color=WHITE
                        ).shift(UP*2)
                
                poly1[13].set_color(RED)

                self.play( Write(poly1) )
                
                self.wait(4)

                self.play(FocusOn(poly1[13]))
                self.wait(1)
                self.play(Indicate(poly1[13],color=RED))
                self.wait(5) # it was 17.

                self.play( FadeToColor( poly1[1],BLUE ),FadeToColor( poly1[4],BLUE ) , FadeToColor( poly1[7],YELLOW ), FadeToColor( poly1[10],YELLOW ), FadeToColor( poly1[13],RED ), FadeToColor( poly1[16],PINK ) )

                deg_n = Tex(r"\text{deg}",r"\Big(p(s)\Big) :", r" n = 5" ).next_to(poly1.get_corner(LEFT),DOWN*3+RIGHT)
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

                zzgroup=VGroup(an,nton1,an1,n1ton2,an2,n2ton3,an3,n3ton4,an4,n4ton5,an5,n5ton6,an6,n6ton7,an7).next_to(poly1,DOWN,buff=LARGE_BUFF)
                
                play_kw = {"run_time": 4}
                self.play(Write(zzgroup,**play_kw))
                self.play(Indicate(poly1[2],color=RED))

                self.wait(1)

                poly1.generate_target()
                poly1.target.to_corner(UP)
                self.play(MoveToTarget(poly1))

                self.play(FadeToColor(poly1,WHITE), FadeToColor(poly1[13],RED))

            # CREATE THE ROUTH TABLE

                # COLUMN MATRIX:
                col1 = Tex(r"2",r"\\",r"4",r"\\",r"4",r"\\",r"13-K",r"\\",r"-\frac{K^2 - 14K + 21}{13-K}",r"\\",r"2")
                col2 = Tex(r"10",r"\\",r"12",r"\\",r"K-1",r"\\",r"2",r"\\",r"0",r"\\",r"0")
                col3 = Tex(r"K",r"\\",r"2",r"\\",r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0")
                col4 = Tex(r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0")

                col3[0].set_color(RED)
                col2[2].set_color(RED)

                # # col1[4] = -\frac{K^2 - 14K + 21}{13-K} ## TODO: write this with preventing the badness of column alignment (DONE)

                col1[4].scale(0.4)
                col1[4].shift(RIGHT*1.5)

                col1[3].scale(0.8)
                col1[3].shift(RIGHT/2)

                col2[2].scale(0.8)
                col2[2].shift(RIGHT/2)

                colgr = VGroup(col1,col2,col3,col4).arrange(RIGHT,buff=LARGE_BUFF*2)
                colgr.next_to(poly1,DOWN,buff=MED_LARGE_BUFF).shift(LEFT/1.5)


                # Just a bit more alignment to prevent badness
                col1[0].next_to(col2[0].get_corner(ORIGIN),ORIGIN,buff=0).shift(LEFT*2.9)
                col1[1].next_to(col2[1].get_corner(ORIGIN),ORIGIN,buff=0).shift(LEFT*2.9)
                col1[2].next_to(col2[2].get_corner(ORIGIN),ORIGIN,buff=0).shift(LEFT*3)
                col1[3].next_to(col2[3].get_corner(ORIGIN),ORIGIN,buff=0).shift(LEFT*3)
                col1[4].next_to(col2[4].get_corner(ORIGIN),ORIGIN,buff=0).shift(LEFT*3.1)
                col1[5].next_to(col2[5].get_corner(ORIGIN),ORIGIN,buff=0).shift(LEFT*2.9)

                col2[0].shift(RIGHT*0.1)
                col2[1].shift(RIGHT*0.1)
                
                col3[0].shift(RIGHT*0.1)

                colzz = VGroup(col1[0:2],col2[0:2],col3[0:2],col4[0:2])
                self.play(TransformMatchingParts(zzgroup,colzz))

                colgr.save_state()

                rectver = SurroundingRectangle( col1[0:2] ).set_color(ORANGE)
                recthor = SurroundingRectangle( col2[0:2] ).set_color(GREEN)

                crl1 = Line(start=col1[0], end=col2[1],buff=0.1).set_color(YELLOW)
                crl2 = Line(start=col1[1], end=col2[0],buff=0.1).set_color(BLUE)
                

                self.play( ShowCreation(rectver), ShowCreation(recthor), ShowCreation(crl1), ShowCreation(crl2) ) 

                n_line = NumberLine(
                x_min=-5,  x_max=14,
                tick_frequency=1,
                unit_size=1,
                include_numbers=True,
                numbers_to_exclude=[])

                n_line.scale(0.7).to_corner(DOWN)
                self.play( ShowCreation(n_line) )

                # vertline = DashedLine(start=DOWN,end=UP).scale(0.7).set_opacity(0.3).move_to(n_line.n2p(0))
                # self.play( ShowCreation(vertline) ) ## uncomment if needed

                dota5 = Dot(color=BLUE_E)
                dota5.move_to(n_line.n2p(0))
                self.play(FadeIn(dota5, scale=0.5),**play_kw_fast)
                self.play( dota5.animate.move_to(n_line.n2p(2)), FadeToColor(col1[0],BLUE_E), **play_kw_fast )

                self.wait(1)

                dota4 = Dot(color=YELLOW_E)
                dota4.move_to(n_line.n2p(0))
                self.play(FadeIn(dota4, scale=0.5),**play_kw_fast)
                self.play( dota4.animate.move_to(n_line.n2p(4)), FadeToColor(col1[1],YELLOW_E), **play_kw_fast )

                self.wait(1)

                self.play(FadeToColor(col1[0],WHITE), FadeToColor(col1[1],WHITE)) 


        # SHOW b1

                b1 = Tex(   r"{ {2 \cdot 12 ",
                            r"-",
                            r"4 \cdot 10}",
                            r"\over",
                            r"{(-4)} } }",
                            color=WHITE
                        ).scale(0.5)

                b1.next_to(col1[2],ORIGIN)
                b1.save_state()

                col1[2].replace(b1,stretch=True)

                rectelem = SurroundingRectangle( col1[2] ).set_color(RED)
                self.play(ShowCreation(rectelem),**play_kw_fast)

                self.play(Write(b1),**play_kw_fast)

                self.play(  FadeToColor(b1[0],YELLOW),
                            FadeToColor(b1[1],WHITE),
                            FadeToColor(b1[2],BLUE),
                            FadeToColor(b1[3],WHITE),
                            FadeToColor(b1[4],BLUE),

                            FadeToColor(col1[0],YELLOW),FadeToColor(col2[0],BLUE),
                            FadeToColor(col1[1],BLUE),  FadeToColor(col2[1],YELLOW),**play_kw_fast
                        )


                self.wait(restore_time)

                colgr.restore()
                b1.restore()

        # SHOW b2

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[0], end=col3[1],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[1], end=col3[0],buff=0.1).set_color(BLUE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col3[0:2] ).set_color(GREEN) )

                self.play(MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2),**play_kw_fast)

                b2 = Tex(   r"{ {2 \cdot 2 ",
                            r"-",
                            r"4 \cdot K}",
                            r"\over",
                            r"{(-4)} } }",
                            color=WHITE
                        ).scale(0.5)

                b2.next_to(col2[2],ORIGIN)
                b2.save_state()

                col2[2].replace(b2,stretch=True)

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col2[2] ).set_color(RED) )
                self.play(MoveToTarget(rectelem),**play_kw_fast)

                self.play(Write(b2),**play_kw_fast)

                self.play(  FadeToColor(b2[0],YELLOW),
                            FadeToColor(b2[1],WHITE),
                            FadeToColor(b2[2],BLUE),
                            FadeToColor(b2[3],WHITE),
                            FadeToColor(b2[4],BLUE),

                            FadeToColor(col1[0],YELLOW),FadeToColor(col3[0],BLUE),
                            FadeToColor(col1[1],BLUE),  FadeToColor(col3[1],YELLOW),**play_kw_fast
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

                self.play(MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2),**play_kw_fast)

                b3 = Tex(   r"{ {2 \cdot 0 ",
                            r"-",
                            r"4 \cdot 0}",
                            r"\over",
                            r"{(-4)} } }",
                            color=WHITE
                        ).scale(0.5)

                b3.next_to(col3[2],ORIGIN)
                b3.save_state()

                col3[2].replace(b3,stretch=True)

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col3[2] ).set_color(RED) )
                self.play(MoveToTarget(rectelem),**play_kw_fast)

                self.play(Write(b3),**play_kw_fast)

                self.play(  FadeToColor(b3[0],YELLOW),
                            FadeToColor(b3[1],WHITE),
                            FadeToColor(b3[2],BLUE),
                            FadeToColor(b3[3],WHITE),
                            FadeToColor(b3[4],BLUE),

                            FadeToColor(col1[0],YELLOW),FadeToColor(col4[0],BLUE),
                            FadeToColor(col1[1],BLUE),  FadeToColor(col4[1],YELLOW),**play_kw_fast
                        )


                self.wait(restore_time)
                
                colgr.restore()
                b3.restore()

        #SHOW b4

                self.play( Write(col4[2]),**play_kw_fast )
                
                colgr.restore()

                self.play( ReplacementTransform(b1,col1[2]),**play_kw_fast )

                dotb1 = Dot(color=GREEN,fill_opacity=0,stroke_width=5)
                dotb1.move_to(n_line.n2p(0))
                self.play(FadeIn(dotb1, scale=0.6),**play_kw_fast)
                self.play( dotb1.animate.move_to(n_line.n2p(4)), FadeToColor(col1[2],GREEN), **play_kw_fast )

                self.play( ReplacementTransform(b2,col2[2]),**play_kw_fast )
                self.play( ReplacementTransform(b3,col3[2]),**play_kw_fast )

                self.play(FadeToColor(col1[2],WHITE))
        

        #SHOW c1

                crl1.generate_target()
                crl2.generate_target()
                crl1.target.become( Line(start=col1[1], end=col2[2],buff=0.1).set_color(YELLOW) )
                crl2.target.become( Line(start=col1[2], end=col2[1],buff=0.1).set_color(BLUE) )

                rectver.generate_target()
                rectver.target.become( SurroundingRectangle( col1[1:3] ).set_color(ORANGE) )

                recthor.generate_target()
                recthor.target.become( SurroundingRectangle( col2[1:3] ).set_color(GREEN) )

                self.play(MoveToTarget(rectver),MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2),**play_kw_fast)

                c1 = Tex(   r"{ {4 \cdot (K-1) ",
                            r"-",
                            r"4 \cdot 12}",
                            r"\over",
                            r"{(-4)} } }",
                            color=WHITE
                        ).scale(0.5)

                c1.next_to(col1[3],ORIGIN)
                c1.save_state()

                col1[3].replace(c1,stretch=True)

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col1[3] ).set_color(RED) )
                self.play(MoveToTarget(rectelem),**play_kw_fast)

                self.play(Write(c1),**play_kw_fast)

                self.play(  FadeToColor(c1[0],YELLOW),
                            FadeToColor(c1[1],WHITE),
                            FadeToColor(c1[2],BLUE),
                            FadeToColor(c1[3],WHITE),
                            FadeToColor(c1[4],BLUE),

                            FadeToColor(col1[1],YELLOW),FadeToColor(col2[1],BLUE),
                            FadeToColor(col1[2],BLUE),  FadeToColor(col2[2],YELLOW),**play_kw_fast
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

                self.play(MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2),**play_kw_fast)

                c2 = Tex(   r"{ {4 \cdot 0",
                            r"-",
                            r"4 \cdot 2}",
                            r"\over",
                            r"{(-4)} } }",
                            color=WHITE
                        ).scale(0.5)

                c2.next_to(col2[3],ORIGIN)
                c2.save_state()

                col2[3].replace(c2,stretch=True)                

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col2[3] ).set_color(RED) )
                self.play(MoveToTarget(rectelem),**play_kw_fast)

                self.play(Write(c2),**play_kw_fast)

                self.play(  FadeToColor(c2[0],YELLOW),
                            FadeToColor(c2[1],WHITE),
                            FadeToColor(c2[2],BLUE),
                            FadeToColor(c2[3],WHITE),
                            FadeToColor(c2[4],BLUE),

                            FadeToColor(col1[1],YELLOW),FadeToColor(col3[1],BLUE),
                            FadeToColor(col1[2],BLUE),  FadeToColor(col3[2],YELLOW),**play_kw_fast
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

                self.play(MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2),**play_kw_fast)

                c3 = Tex(   r"{ {4 \cdot 0 ",
                            r"-",
                            r"4 \cdot 0}",
                            r"\over",
                            r"{(-4)} } }",
                            color=WHITE
                        ).scale(0.5)

                c3.next_to(col3[3],ORIGIN)
                c3.save_state()

                col3[3].replace(c3,stretch=True)     

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col3[3] ).set_color(RED) )
                self.play(MoveToTarget(rectelem),**play_kw_fast)

                self.play(Write(c3),**play_kw_fast)

                self.play(  FadeToColor(c3[0],YELLOW),
                            FadeToColor(c3[1],WHITE),
                            FadeToColor(c3[2],BLUE),
                            FadeToColor(c3[3],WHITE),
                            FadeToColor(c3[4],BLUE),

                            FadeToColor(col1[1],YELLOW),FadeToColor(col4[1],BLUE),
                            FadeToColor(col1[2],BLUE),  FadeToColor(col4[2],YELLOW),**play_kw_fast
                        )

                self.wait(restore_time)
                
                colgr.restore()
                c3.restore()


        #SHOW c4

                self.play(Write(col4[3]),**play_kw_fast)
                
                colgr.restore()               

                self.play( ReplacementTransform(c1,col1[3]),**play_kw_fast )

                dotc1 = Dot(color=ORANGE)
                dotc1.move_to(n_line.n2p(12)).shift(UP)
                c1q = Text("?").set_color(ORANGE).next_to(dotc1,UP)
                self.play(FadeIn(dotc1, scale=0.5), FadeToColor(col1[3],ORANGE), Write(c1q) ,**play_kw_fast)

                self.play( ReplacementTransform(c2,col2[3]),**play_kw_fast )
                self.play( ReplacementTransform(c3,col3[3]),**play_kw_fast )

                self.play(FadeToColor(col1[3],WHITE))

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

                d1 = Tex(   r"{ {4 \cdot 2 ",
                            r"-",
                            r"(13-K) \cdot (K-1)}",
                            r"\over",
                            r"{-(13-K)} } }",
                            color=WHITE
                        ).scale(0.3)

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
                            FadeToColor(col1[3],BLUE),  FadeToColor(col2[3],YELLOW),**play_kw_fast
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

                d2 = Tex(   r"{ {4 \cdot 0 ",
                            r"-",
                            r"(13-K) \cdot 0}",
                            r"\over",
                            r"{-(13-K)} } }",
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
                            FadeToColor(col1[3],BLUE),  FadeToColor(col3[3],YELLOW),**play_kw_fast
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

                d3 = Tex(   r"{ {4 \cdot 0 ",
                            r"-",
                            r"(13-K) \cdot 0}",
                            r"\over",
                            r"{-(13-K)} } }",
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
                            FadeToColor(col1[3],BLUE),  FadeToColor(col4[3],YELLOW),**play_kw_fast
                        )

                self.wait(restore_time)
                
                colgr.restore()
                d3.restore()

        #SHOW d4

                self.play(Write(col4[4]),**play_kw_fast)
                
                colgr.restore()

                self.play( ReplacementTransform(d1,col1[4]),**play_kw_fast )

                dotd1 = Dot(color=TEAL)
                dotd1.move_to(n_line.n2p(13)).shift(UP)
                d1q = Text("?").set_color(TEAL).next_to(dotd1,UP)
                self.play(FadeIn(dotd1, scale=0.5), FadeToColor(col1[4],TEAL), Write(d1q),**play_kw_fast)

                self.play( ReplacementTransform(d2,col2[4]),**play_kw_fast )
                self.play( ReplacementTransform(d3,col3[4]),**play_kw_fast )

                self.wait(1)
                self.play(FadeToColor(col1[4],WHITE))

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

                e1 = Tex(   r"{ {(13-K) \cdot 0 ",
                            r"-",
                            r"(-\frac{K^2 - 14K + 21}{13-K}) \cdot (2)}",
                            r"\over",
                            r"{-(-\frac{K^2 - 14K + 21}{13-K})} } }",
                            color=WHITE
                        ).scale(0.3)

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
                            FadeToColor(col1[4],BLUE),  FadeToColor(col2[4],YELLOW),**play_kw_fast
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

                e2 = Tex(   r"{ {(13-K) \cdot 0 ",
                            r"-",
                            r"(-\frac{K^2 - 14K + 21}{13-K}) \cdot 0}",
                            r"\over",
                            r"{-(-\frac{K^2 - 14K + 21}{13-K})} } }",
                            color=WHITE
                        ).scale(0.3)

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
                            FadeToColor(col1[4],BLUE),  FadeToColor(col3[4],YELLOW),**play_kw_fast
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

                e3 = Tex(   r"{ {(13-K) \cdot 0 ",
                            r"-",
                            r"(-\frac{K^2 - 14K + 21}{13-K}) \cdot 0}",
                            r"\over",
                            r"{-(-\frac{K^2 - 14K + 21}{13-K})} } }",
                            color=WHITE
                        ).scale(0.3)

                e3.next_to(col3[5],ORIGIN)
                e3.save_state()

                col3[5].replace(e3,stretch=True)

                rectelem.generate_target()
                rectelem.target.become( SurroundingRectangle( col3[5] ).set_color(RED) )
                self.play(MoveToTarget(rectelem),**play_kw_fast)

                self.play(Write(e3),**play_kw_fast)

                self.play(  FadeToColor(e3[0],YELLOW),
                            FadeToColor(e3[1],WHITE),
                            FadeToColor(e3[2],BLUE),
                            FadeToColor(e3[3],WHITE),
                            FadeToColor(e3[4],BLUE),

                            FadeToColor(col1[3],YELLOW),FadeToColor(col4[3],BLUE),
                            FadeToColor(col1[4],BLUE),  FadeToColor(col4[4],YELLOW),**play_kw_fast
                        )

                self.wait(restore_time)
                
                colgr.restore()
                e3.restore()


        #SHOW e4

                self.play(Write(col4[5]),**play_kw_fast)

                self.play( ReplacementTransform(e1,col1[5]),**play_kw_fast )


                dote1 = Dot(color=PURPLE,fill_opacity=0,stroke_width=5)
                dote1.move_to(n_line.n2p(0))
                self.play(FadeIn(dote1, scale=0.6),**play_kw_fast)
                self.play( dote1.animate.move_to(n_line.n2p(2)), FadeToColor(col1[5],PURPLE) ,**play_kw_fast )


                self.play( ReplacementTransform(e2,col2[5]),**play_kw_fast )
                self.play( ReplacementTransform(e3,col3[5]),**play_kw_fast )

                self.play(FadeOut(rectelem), FadeOut(crl1), FadeOut(crl2), FadeOut(rectver), FadeOut(recthor))
                
                self.wait(2)

                self.play(FadeToColor(col1[0],BLUE_E), FadeToColor(col1[1],YELLOW_E), FadeToColor(col1[2],GREEN), FadeToColor(col1[3],ORANGE), FadeToColor(col1[4],TEAL))
                
                self.wait(2)


                col1box = SurroundingRectangle(col1)
                self.play(ShowCreation(col1box))

                self.play(FadeOut(col2),FadeOut(col3),FadeOut(col4))
                
                poly1.generate_target()
                poly1.target.to_corner(LEFT)
                
                col1gr = VGroup(col1,col1box)
                col1gr.generate_target()
                col1gr.target.to_corner(LEFT)
                self.play(MoveToTarget(col1gr), MoveToTarget(poly1))

                
                col1brace = Brace(col1box,DOWN)
                col1deg = Tex(r"{(n+1)}",r"=",r"6 \text{ rows}").scale(0.8).next_to(col1brace,DOWN,SMALL_BUFF).shift(RIGHT*0.2)
                col1deg[0].set_color(RED)
                self.play(ShowCreation(col1brace),Write(col1deg))

                self.wait(5)
                
                expl1 = Tex(r"p(s)", r"\text{ is a Hurwitz polynomial if}")
                conds = Tex(r"13-K > 0", r"\ \land \ ", r"-\dfrac{K^2 - 14K + 21}{13-K} > 0", r"\ \land \ ", r"K>0")

                conds[0].set_color(ORANGE)
                conds[2].set_color(TEAL)
                conds[4].set_color(RED_D)

                condfull = VGroup(expl1,conds).arrange(DOWN,MED_SMALL_BUFF).next_to(col1box,RIGHT).to_corner(RIGHT).shift(LEFT)

                self.play(Write(expl1))
                self.play(Write(conds))


                self.wait(5)
                
                condres = Tex(r"1.71",r"<",r"K",r"<",r"12.29",r" \ \Longrightarrow \ ",r"p(s) \text{ is HP}").next_to(col1box,RIGHT).to_corner(ORIGIN).shift(RIGHT*2)
                condres[5].set_color(BLUE)
                condres[2].set_color(RED)

                self.play(TransformMatchingParts(condfull,condres), FadeOut(col1brace), FadeOut(col1deg))

                # Define the 4th and 5th row as functions
                def update_func(x):
                    return (13-x)

                def update_func2(x):
                    return ( -(x**2 - 14*x + 21)/(13-x) )

                
                val = 1.72
                vt = DecimalNumber(val,num_decimal_places=2)

                # # kval = Tex(r"K = ").next_to(condres[2],DOWN,LARGE_BUFF) ##uncomment if needed
                kbrace = Brace(condres[2],DOWN,buff=0.1)

                vt.next_to(kbrace,DOWN).set_color(RED)

                self.play(Write(kbrace),Write(vt))

                dotc1.generate_target()
                dotd1.generate_target()
                dotc1.target.move_to(n_line.n2p(11.29))
                dotd1.target.move_to(n_line.n2p(0))

                self.play(MoveToTarget(dotc1),MoveToTarget(dotd1),FadeOut(c1q),FadeOut(d1q))

                # WHILE LOOP TO MOVE DOTS depending on K values (TODO: Try to achieve this with updaters.)
                while val < 12.26:
                    self.remove(dotc1)
                    self.remove(dotd1)
                    self.remove(vt)
                    val+=0.02
                    dotc1 = Dot(color=ORANGE).move_to(n_line.n2p(update_func(val)))
                    dotd1 = Dot(color=TEAL).move_to(n_line.n2p(update_func2(val)))
                    vt = DecimalNumber(val,num_decimal_places=2).next_to(kbrace,DOWN).set_color(RED)
                    self.add(dotc1)
                    self.add(dotd1)
                    self.add(vt)
                    self.wait(0.001) # this should not be commented out.

                # # # ADD THIS PART IF NEEDED. THIS MAKES THE OPPOSITE OF THE LOOP ABOVE.
                # while val > 1.72:
                #     self.remove(dotc1)
                #     self.remove(dotd1)
                #     self.remove(vt)
                #     val-=0.02
                #     dotc1 = Dot(color=ORANGE).move_to(n_line.n2p(update_func(val)))
                #     dotd1 = Dot(color=TEAL).move_to(n_line.n2p(update_func2(val)))
                #     vt = DecimalNumber(val,num_decimal_places=2).next_to(kbrace,DOWN).set_color(RED)
                #     self.add(dotc1)
                #     self.add(dotd1)
                #     self.add(vt)
                #     self.wait(0.001)

                self.wait(2) #it was 8 seconds. changed to 2 because of the while loop
                self.play(*[FadeOut(mob)for mob in self.mobjects])
