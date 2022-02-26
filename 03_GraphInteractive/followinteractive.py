from manimlib import *
import numpy as np
import math

class GraphInteractive(Scene):
    CONFIG = {
        "axes_kwargs": {
            "x_range": (-4, 4, 1),
            "y_range": (-4, 4, 1),
            #"height": 7,
            #"width": 7,
        "axis_config": {
            "stroke_color": WHITE,
            "stroke_width": 2,
            "include_ticks": True,
            "include_tip": True,
            "line_to_number_buff": SMALL_BUFF,
            "label_direction": DR,
            "number_scale_val": 0.5,
        },
        "y_axis_config": {
            "label_direction": DR,
            "stroke_color":WHITE,
        },
        "background_line_style": {
            "stroke_color": BLACK,
            "stroke_width": 0,
            "stroke_opacity": 0,
        },
        # Defaults to a faded version of line_config
        "faded_line_style": None,
        "x_line_frequency": 1,
        "y_line_frequency": 1,
        "faded_line_ratio": 1,
        "make_smooth_after_applying_functions": True,
        }
    }
    def construct(self):
        caxes = ComplexPlane(**self.axes_kwargs)
        caxes.add_coordinate_labels()

        frame = self.camera.frame
        self.camera.frame.save_state()
        frame2 = frame.copy()
        frame2.set_width(15)
        self.play(Transform(frame, frame2))        

        x_label_tex = r"Re{ \{ s_{\upsilon_T} \} }"
        y_label_tex = r"Im{ \{ s_{\upsilon_T} \} }"

        labels = self.axis_labels = VGroup(
            caxes.get_x_axis_label(x_label_tex).next_to(caxes.x_axis.tip),
            caxes.get_y_axis_label(y_label_tex).next_to(caxes.y_axis.tip),
        )

        self.play(FadeIn(caxes),FadeIn(labels))

        unitcircle = Circle(color = GREEN, radius=1).set_fill(GREEN, opacity=0.5)
        self.play(ShowCreation(unitcircle))

        dotx = Dot( (0, 0, 0)  ).set_color(YELLOW).scale(0.8).set_opacity(0.5)

        unitarrow = VMobject()
        unitarrow.add_updater(lambda x: x.become(Line(unitcircle.get_center(), dotx.get_center()).set_color(PINK))) #UPDATER
        self.add(unitarrow)
        self.play(MoveAlongPath(dotx, unitcircle), rate_func=linear, run_time=2)

    def init_play_button(self):
        play_rect = Text("Bigger Circle").add_background_rectangle(color=BLACK, opacity=1, buff=0.25).to_corner(UR)

        def play_clicked(mobject):
            self.biggercircle = Circle(color = RED, radius=2)
            self.play(ShowCreation(self.biggercircle))
            self.dotbig = Dot( (0, 0, 0)  ).set_color(YELLOW).scale(0.8).set_opacity(0.5)
            self.unitarrow2 = VMobject()
            self.unitarrow2.add_updater(lambda x: x.become(Line(self.biggercircle.get_center(), self.dotbig.get_center()).set_color(BLUE))) #UPDATER
            self.add(self.unitarrow2)    
            self.play(MoveAlongPath(self.dotbig, self.biggercircle), rate_func=linear, run_time=5)
            print("Big Circle Has Been Created")

        self.play_btn = Button(play_rect, play_clicked)
        self.add(self.play_btn)

    def init_play_button2(self):
        play_rect2 = Text("Smaller Circle").add_background_rectangle(color=BLACK, opacity=1, buff=0.25).next_to(self.play_btn, DOWN)
    
        def play_clicked2(mobject):
            self.smallcircle = Circle(color = ORANGE, radius=0.5)
            self.play(ShowCreation(self.smallcircle))
            self.dotsmall = Dot( (0, 0, 0)  ).set_color(YELLOW).scale(0.8).set_opacity(0.5)
            self.unitarrow3 = VMobject()
            self.unitarrow3.add_updater(lambda x: x.become(Line(self.smallcircle.get_center(), self.dotsmall.get_center()).set_color(RED))) #UPDATER
            self.add(self.unitarrow3)
            self.play(MoveAlongPath(self.dotsmall, self.smallcircle), rate_func=linear, run_time=2)
            print("Small Circle Has Been Created")

        self.play_btn2 = Button(play_rect2, play_clicked2)
        self.add(self.play_btn2)

    def init_clear_button(self):
        clear_rect = Text("Clear") \
            .add_background_rectangle(color=BLACK, opacity=1, buff=0.25)
        clear_rect.set_width(self.play_btn.get_width()).to_corner(DR).scale(0.5)

        def clear_clicked(mobject):
            if  self.smallcircle != None and self.dotsmall != None and self.unitarrow3 != None:
                self.play(FadeOut(self.smallcircle), FadeOut(self.dotsmall), FadeOut(self.unitarrow3))
                self.smallcircle = None
                self.dotsmall = None
                self.unitarrow3 = None
            #print("Cleared")

            if  self.biggercircle != None and self.dotbig != None and self.unitarrow2 != None:
                self.play(FadeOut(self.smallcircle), FadeOut(self.dotsmall), FadeOut(self.unitarrow3))
                self.biggercircle = None
                self.dotbig = None
                self.unitarrow2 = None
            print("Cleared")            

        self.clear_btn = Button(clear_rect, clear_clicked)
        self.add(self.clear_btn)

    def setup(self):
        self.init_play_button()
        self.init_play_button2()
        self.init_clear_button()
