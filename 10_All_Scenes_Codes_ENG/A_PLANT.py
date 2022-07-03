from manimlib import *
import numpy as np

class A_PLANT_ENG(Scene):
    CONFIG = {
		"axes_kwargs": {
			"x_range": (-3, 3, 1),
			"y_range": (-3, 3, 1),
			"height": 5,
			"width": 5,
			"axis_config": {
				"stroke_color": WHITE,
				"stroke_width": 3,
			},
			"y_axis_config": {
				"include_tip": True,
                "line_to_number_direction":LEFT,
			},
            "x_axis_config": {
                "include_tip": True,
                "line_to_number_direction":DOWN*0.5+RIGHT*0.25,
                "numbers_to_exclude":None,
            }
		}
	}
    def construct(self):

        self.wait(3) # it was 3.5

        intro_words = Text("Routh-Hurwitz Criterion").scale(1)
        intro_words.set_color(YELLOW_C).scale(2)

        underline = Underline(mobject=intro_words)
        underline.set_color(YELLOW_C)

        self.play(Write(intro_words))

        self.play(ShowCreation(underline))

        self.wait(3)

        self.play(ShrinkToCenter(intro_words), ShrinkToCenter(underline))

        self.wait(3)


        plant_text = Text("Plant")
        ps_text = Tex(r"P(s)")
        plgr = VGroup(plant_text,ps_text).arrange(DOWN)

        contr_text = Text("Controller")
        cr_text = Tex(r"C(s)")
        clgr = VGroup(contr_text, cr_text).arrange(DOWN)


        rectplant = Rectangle().shift(UP*2+RIGHT*2.5)
        rectcont = Rectangle().next_to(rectplant,LEFT*4)

        plgr.move_to(rectplant,ORIGIN)
        clgr.move_to(rectcont,ORIGIN)

        plant = VGroup(plgr,rectplant)
        controller = VGroup(clgr, rectcont)


        linetoplant = Line( start = rectcont.get_corner(RIGHT) , end = rectplant.get_corner(LEFT), buff=0)
        ltp_tip = ArrowTip(tip_style=1).next_to(linetoplant.get_corner(RIGHT),LEFT,buff=0)
        linetoy = Line( start = rectplant.get_corner(RIGHT), end = rectplant.get_bounding_box_point(RIGHT)+RIGHT, buff=0 )


        sumcirc = Circle(radius=0.2, color = WHITE).next_to(rectcont,LEFT*4)
        sumsign = Tex(r"-").next_to(sumcirc,DR/3)


        linetocont = Line( start = sumcirc.get_corner(RIGHT), end = rectcont.get_corner(LEFT) )
        ltct_tip = ArrowTip(tip_style=1).next_to(linetocont.get_corner(RIGHT),LEFT,buff=0)
        linetoy2 = Line( start = linetoy.get_corner(RIGHT), end = linetoy.get_bounding_box_point(RIGHT)+RIGHT)
        lty2_tip = ArrowTip(tip_style=1).next_to(linetoy2.get_corner(RIGHT),LEFT,buff=0).shift(RIGHT*0.1)
        linetodown = Line( start = linetoy2.get_corner(LEFT), end =  linetoy2.get_bounding_box_point(LEFT)+DOWN*2 )


        linetoleft = Line( start = linetodown.get_corner(DOWN), end = sumcirc.get_corner(ORIGIN)+DOWN*2 )
        linetoup = Line( start = linetoleft.get_corner(LEFT) , end = sumcirc.get_corner(DOWN) )
        ltu_tip = ArrowTip(tip_style=1,angle=PI/2).next_to(linetoup.get_corner(UP),DOWN,buff=0)
        
        
        linetocirc = Line( start = sumcirc.get_bounding_box_point(LEFT)+LEFT, end = sumcirc.get_corner(LEFT) )
        ltc_tip = ArrowTip(tip_style=1).next_to(linetocirc.get_corner(RIGHT),LEFT,buff=0)


        refvalue = Tex(r"r").next_to(linetocirc,UP)
        outvalue = Tex(r"y").next_to(linetoy,UR)


        frame = self.camera.frame
        self.camera.frame.save_state()
        frame2 = frame.copy()
        frame2.move_to(plant)
        frame2.set_width(plant.get_width() + 1)
        self.play(Transform(frame, frame2))

        self.play(ShowCreation(rectplant), ShowCreation(linetoplant), ShowCreation(linetoy))
        self.play(Write(plgr))

        # frame3 = frame.copy() # Camera could be moved if necessary like this.
        # frame3.set_width(20)
        # self.play(Transform(frame, frame3))
        self.play(Restore(self.camera.frame))

        self.wait(2)
        
        self.play(ShowCreation(rectcont), ShowCreation(linetocont))
        self.play(Write(clgr))

        self.wait(1)

        self.play(ShowCreation(linetoy2), ShowCreation(linetodown), ShowCreation(linetoleft), ShowCreation(linetoup), ShowCreation(linetocirc))

        self.play(ShowCreation(sumcirc), Write(sumsign))

        self.play(Write(refvalue),Write(outvalue))

        lines = VGroup(linetocirc,linetocont,linetodown,linetoleft,linetoplant,linetoup,linetoy,linetoy2)
        arrows = VGroup(ltc_tip, ltct_tip, ltp_tip, lty2_tip, ltu_tip)
        
        for i in arrows:
            self.play(Write(i))

        self.wait(1)

        G_s = Tex(  r"G(s)",
                    r"=",
                    r"{\bar{y}(s)",
                    r"\over",
                    r"\bar{r}(s)}",
                    r"=",
                    r"{C(s)P(s)",
                    r"\over",
                    r"1+C(s)P(s)}",
                ).scale(1.5)

        new_Gs = Tex(   r"G(s)",
                        r"=",
                        r"{\mu(s)",
                        r"\over",
                        r"\nu(s)}",
                ).scale(1.5)

        G_s.next_to(linetoleft,DOWN*3).to_corner(ORIGIN)
        new_Gs.next_to(linetoleft,DOWN*3).to_corner(ORIGIN)

        self.play(Write(G_s))
        
        self.wait(10)

        self.play(  FadeToColor(G_s[6], ORANGE), FadeToColor(controller,ORANGE), FadeToColor(plant,ORANGE),
                    FadeToColor(linetocirc, ORANGE), FadeToColor(linetocont, ORANGE), FadeToColor(linetoplant, ORANGE),  FadeToColor(linetoy, ORANGE), FadeToColor(linetoy2, ORANGE),
                    FadeToColor(ltc_tip, ORANGE), FadeToColor(ltct_tip, ORANGE) , FadeToColor(ltp_tip, ORANGE), FadeToColor(lty2_tip, ORANGE) )

        self.wait(2)

        self.play(  FadeToColor(G_s[6], WHITE), FadeToColor(controller,WHITE), FadeToColor(plant,WHITE),
                    FadeToColor(linetocirc, WHITE), FadeToColor(linetocont, WHITE), FadeToColor(linetoplant, WHITE), FadeToColor(linetoy, WHITE), FadeToColor(linetoy2, WHITE),
                    FadeToColor(ltc_tip, WHITE), FadeToColor(ltct_tip, WHITE) , FadeToColor(ltp_tip, WHITE), FadeToColor(lty2_tip, WHITE) )

        self.wait(2)

        self.play(  FadeToColor(G_s[8], BLUE), FadeToColor(controller,BLUE), FadeToColor(plant,BLUE), FadeToColor(sumsign,BLUE),
                    FadeToColor(linetocont, BLUE), FadeToColor(linetoplant, BLUE),  FadeToColor(linetoy, BLUE), 
                    FadeToColor(linetodown, BLUE), FadeToColor(linetoleft, BLUE), FadeToColor(linetoup, BLUE),
                    FadeToColor(ltct_tip, BLUE) , FadeToColor(ltp_tip, BLUE), FadeToColor(ltu_tip, BLUE) )

        self.wait(2)

        self.play(  FadeToColor(G_s[8], WHITE), FadeToColor(controller,WHITE), FadeToColor(plant,WHITE), FadeToColor(sumsign,WHITE),
                    FadeToColor(linetocont, WHITE), FadeToColor(linetoplant, WHITE),  FadeToColor(linetoy, WHITE), 
                    FadeToColor(linetodown, WHITE), FadeToColor(linetoleft, WHITE), FadeToColor(linetoup, WHITE),
                    FadeToColor(ltct_tip, WHITE) , FadeToColor(ltp_tip, WHITE), FadeToColor(ltu_tip, WHITE) )


        Gs_box = SurroundingRectangle(G_s)
        self.play(ShowCreation(Gs_box))

        Gs_box.generate_target()
        Gs_box.target.become( SurroundingRectangle(new_Gs) )

        self.play( TransformMatchingParts(G_s,new_Gs), MoveToTarget(Gs_box) )
        self.play(FadeOut(Gs_box))

        self.wait(2)
       
        tofade = VGroup (plant,controller,arrows,lines,sumcirc,sumsign,refvalue,outvalue)
        self.play( FadeOut(tofade) )
        #self.play(*[FadeOut(mob)for mob in self.mobjects]) # To fade out all objects

        self.wait(0.5) # it was 1

# POLE PLACEMENT SCENE

        titlegraph = Title("Pole-Distribution").set_color(YELLOW_C)
        	
        axes = Axes(**self.axes_kwargs).shift(DOWN*0.5).to_corner(LEFT)
        axes.add_coordinate_labels(font_size=20, num_decimal_places=0, x_values=[0], y_values=[0])

        x_label_tex = r"\Re{  s_{\nu}  }"
        y_label_tex = r"\Im{  s_{\nu}  }"
        
        xlabel = axes.get_x_axis_label(x_label_tex).next_to(axes.x_axis.tip)
        ylabel = axes.get_y_axis_label(y_label_tex).next_to(axes.y_axis.tip)
        labels = VGroup(xlabel,ylabel)

        new_Gs.generate_target()
        new_Gs.target.scale(0.8).next_to(axes,RIGHT,buff=LARGE_BUFF*3)
        self.play(Write(titlegraph),MoveToTarget(new_Gs))

        self.play(FadeIn(axes), FadeIn(labels))

        bibodef = Tex(r"G(s)", r"\text{ is BIBO-stable, when }", r"\nu(s)", r"\text{ is a Hurwitz polynomial}" ).scale(0.8)
        bibodef[2].set_color(ORANGE)
        bibodef.to_corner(DR).shift(UP/1.8)

        defbox = SurroundingRectangle(bibodef)
        self.play(Write(bibodef,run_time=4),ShowCreation(defbox))

        self.wait(0.5)

        check = Checkmark().set_color(GREEN).next_to(new_Gs,LEFT,buff=MED_LARGE_BUFF)
        ex = Exmark().set_color(RED).next_to(new_Gs,LEFT,buff=MED_LARGE_BUFF)

        dot1 = Dot(color=ORANGE,fill_opacity=0,stroke_width=5)
        dot2 = dot1.copy()
        dot3 = dot1.copy()

        dot1.move_to(axes.c2p(1, 1))
        dot2.move_to(axes.c2p(1, -1))
        dot3.move_to(axes.c2p(-1,0))

        self.play(FadeIn(dot1, scale=0.5), FadeIn(dot2, scale=0.5), FadeIn(dot3, scale=0.5), Write(ex), FadeToColor(new_Gs[4],ORANGE) )

        self.wait(1)

        self.play( dot1.animate.move_to(axes.c2p(0, 1)), dot2.animate.move_to(axes.c2p(0, -1)), dot3.animate.move_to(axes.c2p(-2, 0)) )

        self.wait(1)

        self.play( dot1.animate.move_to(axes.c2p(-1, 1)), dot2.animate.move_to(axes.c2p(-1, -1)), FadeTransform(ex,check) )

        self.wait(1)

        self.play( dot3.animate.move_to(axes.c2p(0, 0)), FadeTransform(check,ex) )


        self.wait(3)
        self.play(*[FadeOut(mob)for mob in self.mobjects])


# STABILITY METHODS SCENE

        self.wait(1)

        methodtitle = Title("Stability Methods").set_color(YELLOW_C)
        self.play(Write(methodtitle))

        self.wait(1)

        methodlist = BulletedList(  "Routh-Hurwitz Criterion",
                                    "Nyquist Criterion",
                                    "Circle Criterion",
                                    "...",buff=1).next_to(methodtitle,DOWN*3).to_corner(LEFT).shift(RIGHT)

        for i in methodlist:
            self.play(Write(i),run_time=2.5)
        
        self.wait(3)

        otherlist = methodlist[1:4]
        otherlist.generate_target()
        otherlist.target.set_opacity(0.25)

        self.play( FadeToColor(methodlist[0], TEAL_D), MoveToTarget(otherlist) )

        self.wait(5)

        self.play(*[FadeOut(mob)for mob in self.mobjects])
