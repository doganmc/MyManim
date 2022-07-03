from manimlib import *
import numpy as np

class E_EX1_ENG(Scene):
    def construct(self):

                play_kw_fast = {"run_time": 0.5}
                restore_time = 0.5
                self.wait(1)

                # INTRO FOR EXAMPLE 1
                intro_words = Text("Example 1: A Quartic Polynomial")
                intro_words.set_color(YELLOW_C).scale(1.5)

                underline = Underline(mobject=intro_words)
                underline.set_color(YELLOW_C)

                self.play(Write(intro_words))

                self.play(ShowCreation(underline),run_time=1)

                self.wait(1)

                self.play(ShrinkToCenter(intro_words), ShrinkToCenter(underline))

                self.wait(1)

                poly1 = Tex(    r"{p(s) =",
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

                deg_n = Tex(r"\text{deg}",r"\Big(p(s)\Big) :", r" n = 4" ).next_to(poly1.get_corner(LEFT),DOWN*3+RIGHT)
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
                an5 = Tex(r"?").set_color(PINK)

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

                zzgroup=VGroup(an,nton1,an1,n1ton2,an2,n2ton3,an3,n3ton4,an4,n4ton5,an5).next_to(poly1,DOWN,buff=LARGE_BUFF) #,n5ton6,an6,an7)
                
                play_kw = {"run_time": 4}
                self.play(Write(zzgroup),**play_kw)

                self.wait(5)

                an5.generate_target()
                an5.target.become( Tex(r"0").set_color(PINK).next_to(n4ton5,DOWN) )
                self.play(Indicate(poly1[2],color=RED))
                self.play(MoveToTarget(an5))

                self.wait(1)

                poly1.generate_target()
                poly1.target.to_corner(UR)
                self.play(MoveToTarget(poly1))

                zzgroup.generate_target()
                zzgroup.target.to_corner(UL)
                self.play(MoveToTarget(zzgroup))

                self.play(FadeToColor(poly1,WHITE))           


        # CREATE THE ROUTH TABLE

                # COLUMN MATRIX:
                col1 = Tex(r"1",r"\\",r"2",r"\\",r"1",r"\\",r"-6",r"\\",r"5")
                col2 = Tex(r"3",r"\\",r"4",r"\\",r"5",r"\\",r"0",r"\\",r"0")
                col3 = Tex(r"5",r"\\",r"0",r"\\",r"0",r"\\",r"0",r"\\",r"0")

                # SAME MATRIX FOR COLUMN TRACKERS:
                colt1 = Tex(r"a_7",r"\\",r"\\",r"a_6",r"\\",r"\\",r"b_1",r"\\",r"\\",r"c_1",r"\\",r"\\",r"d_1")
                colt2 = Tex(r"a_5",r"\\",r"\\",r"a_4",r"\\",r"\\",r"b_2",r"\\",r"\\",r"c_2",r"\\",r"\\",r"d_2")
                colt3 = Tex(r"a_3",r"\\",r"\\",r"a_2",r"\\",r"\\",r"b_3",r"\\",r"\\",r"c_3",r"\\",r"\\",r"d_3")
                
                coltgr = VGroup(colt1,colt2,colt3).arrange(RIGHT,buff=LARGE_BUFF*2)
                colgr = VGroup(col1,col2,col3).arrange(RIGHT,buff=LARGE_BUFF*2)

                colgr.to_corner(UL)

                colzz = VGroup(col1[0:2],col2[0:2],col3[0:2])
                self.play(TransformMatchingParts(zzgroup,colzz))
                
                colgr.save_state()

                rectver = SurroundingRectangle( col1[0:2] ).set_color(ORANGE)
                recthor = SurroundingRectangle( col2[0:2] ).set_color(GREEN)

                crl1 = Line(start=col1[0], end=col2[1],buff=0.1).set_color(YELLOW)
                crl2 = Line(start=col1[1], end=col2[0],buff=0.1).set_color(BLUE)
                
                self.wait(2)

                self.play( ShowCreation(rectver), ShowCreation(recthor), ShowCreation(crl1), ShowCreation(crl2) ) 

                n_line = NumberLine(
                x_min=-6,  x_max=6,
                tick_frequency=1,
                unit_size=1,
                include_numbers=True,
                numbers_to_exclude=[] )

                n_line.scale(0.6).next_to(poly1,DOWN,buff=LARGE_BUFF)
                self.play( ShowCreation(n_line) )

                # vertline = DashedLine(start=DOWN,end=UP).scale(0.6).set_opacity(0.3).move_to(n_line.n2p(0)) ## uncomment this if needed
                # self.play( ShowCreation(vertline) ) ## uncomment this if needed
        
                dota4 = Dot(color=BLUE_E)
                dota4.move_to(n_line.n2p(0))
                self.play(FadeIn(dota4, scale=0.5),**play_kw_fast)
                self.play( dota4.animate.move_to(n_line.n2p(1)), FadeToColor(col1[0],BLUE_E), **play_kw_fast )

                self.wait(1)

                dota3 = Dot(color=YELLOW_E)
                dota3.move_to(n_line.n2p(0))
                self.play(FadeIn(dota3, scale=0.5),**play_kw_fast)
                self.play( dota3.animate.move_to(n_line.n2p(2)), FadeToColor(col1[1],YELLOW_E), **play_kw_fast )

                self.wait(1)

                self.play(FadeToColor(col1[0],WHITE), FadeToColor(col1[1],WHITE)) 

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

                self.play(Write(col3[2]),**play_kw_fast)
                self.wait(1)
                
                colgr.restore()
                self.wait(1)

                self.play( ReplacementTransform(b1,col1[2]),**play_kw_fast )

                dotb1 = Dot(color=GREEN,fill_opacity=0,stroke_width=5)
                dotb1.move_to(n_line.n2p(0))
                self.play(FadeIn(dotb1, scale=0.6),**play_kw_fast)
                self.play( dotb1.animate.move_to(n_line.n2p(1)), FadeToColor(col1[2],GREEN), **play_kw_fast )

                self.play( ReplacementTransform(b2,col2[2]),**play_kw_fast )
                
                self.wait(1)
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

                c1 = Tex(   r"{ {2 \cdot 5 ",
                            r"-",
                            r"1 \cdot 4}",
                            r"\over",
                            r"{(-1)} } }",
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

                c2 = Tex(   r"{ {2 \cdot 0 ",
                            r"-",
                            r"1 \cdot 0}",
                            r"\over",
                            r"{(-1)} } }",
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

                self.play(Write(col3[3]),**play_kw_fast )
                
                self.wait(restore_time)
                
                colgr.restore()

                self.play( ReplacementTransform(c1,col1[3]),**play_kw_fast )

                dotc1 = Dot(color=ORANGE)
                dotc1.move_to(n_line.n2p(0))
                self.play(FadeIn(dotc1, scale=0.5),**play_kw_fast)
                self.play( dotc1.animate.move_to(n_line.n2p(-6)),**play_kw_fast )

                self.play(FlashAround(col1[3],color=ORANGE))
                self.play(Indicate(col1[3],color=ORANGE))

                self.play( ReplacementTransform(c2,col2[3]),**play_kw_fast )

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

                self.play(MoveToTarget(rectver),MoveToTarget(recthor),MoveToTarget(crl1),MoveToTarget(crl2),**play_kw_fast)

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

                self.play(Write(col3[4]),**play_kw_fast)
                
                self.wait(restore_time)
                
                colgr.restore()
                self.wait(2)

                self.play( ReplacementTransform(d1,col1[4]),**play_kw_fast )
                
                dotd1 = Dot(color=TEAL_C)
                dotd1.move_to(n_line.n2p(0))
                self.play(FadeIn(dotd1, scale=0.5),**play_kw_fast)
                self.play( dotd1.animate.move_to(n_line.n2p(5)), FadeToColor(col1[4],TEAL_C),**play_kw_fast )

                self.play( ReplacementTransform(d2,col2[4]),**play_kw_fast )

                self.play(FadeToColor(col1[0],BLUE_E), FadeToColor(col1[1],YELLOW_E), FadeToColor(col1[2],GREEN), FadeToColor(col1[3],ORANGE))

                self.wait(2)

                self.play(FadeOut(rectelem), FadeOut(crl1), FadeOut(crl2), FadeOut(rectver), FadeOut(recthor))

                self.wait(4)

                col1box = SurroundingRectangle(col1)
                self.play(ShowCreation(col1box))

                col1brace = Brace(col1box,DOWN)
                col1deg = Tex(r"{(n+1)}",r"=",r"5 \text{ rows}").scale(0.8).next_to(col1brace,DOWN,SMALL_BUFF).shift(RIGHT/1.25)
                col1deg[0].set_color(RED)

                self.play(ShowCreation(col1brace),Write(col1deg))
                
                self.wait(1)

                arc1 = CurvedArrow( col1[2].get_boundary_point(LEFT), col1[3].get_boundary_point(LEFT) ).scale(0.7).set_color(RED_E)
                arc2 = CurvedArrow( col1[3].get_boundary_point(LEFT), col1[4].get_boundary_point(LEFT) ).scale(0.7).set_color(RED_A)

                col1box.generate_target()
                col1box.target.stretch_to_fit_width(col1.get_width()+0.5)

                col1brace.generate_target()
                col1brace.target.stretch_to_fit_width(col1.get_width()+0.5)

                self.play(ShowCreation(arc1),ShowCreation(arc2),MoveToTarget(col1box),MoveToTarget(col1brace))

                self.wait(4)

                khp = Tex(r"p(s)",r"\text{ is not a Hurwitz polynomial.}").to_corner(ORIGIN).shift(DOWN*1.5)
                vza = Tex(r"\text{two}",r"\text{ sign changes}",r"\Longrightarrow",r"\text{two}",r"\text{ roots in the right half-plane}").next_to(khp,DOWN,buff=LARGE_BUFF)

                vza[0].set_color(PINK)
                vza[3].set_color(PINK)
                
                self.play(Write(khp))
                self.wait(3)
                self.play(Write(vza))

                self.wait(3)
                self.play(*[FadeOut(mob)for mob in self.mobjects])
                self.wait(2)
