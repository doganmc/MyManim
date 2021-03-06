from manimlib import *
import numpy as np

class GraphFollow(Scene):
    CONFIG = {
		"axes_kwargs": {
			"x_range": (-3, 3, 1),
			"y_range": (-3, 3, 1),
			"height": 5,
			"width": 5,
			"axis_config": {
				"stroke_color": WHITE,
				"stroke_width": 4,
			},
			"y_axis_config": {
				"include_tip": True,
			},
            "x_axis_config": {
                "include_tip": True,
            }
		}
	}
    def construct(self):
        textTs = Tex(   
                        "T(s) =",
                        "{\mu_T(s)",
                        "\\over",
                        "\\upsilon_T(s)}",
                        color=WHITE
                    )

        textTs.shift(DOWN*2 + RIGHT*4)

        self.play(  textTs[0].set_color, WHITE,
                    textTs[1].set_color, WHITE,
                    textTs[2].set_color, WHITE,
                    textTs[3].set_color, ORANGE,
                )
		
        
        axes = Axes(**self.axes_kwargs).shift(LEFT*2)
        axes.add_coordinate_labels(font_size=20, num_decimal_places=0)

        x_label_tex = r"Re{ \{ s_{\upsilon_T} \} }"
        y_label_tex = r"Im{ \{ s_{\upsilon_T} \} }"

        labels = self.axis_labels = VGroup(
            axes.get_x_axis_label(x_label_tex).next_to(axes.x_axis.tip),
            axes.get_y_axis_label(y_label_tex).next_to(axes.y_axis.tip),
        )

        self.play(FadeIn(axes), FadeIn(labels))

        dot = Dot(color=ORANGE)
        dot2 = Dot(color=ORANGE)
        dot.move_to(axes.c2p(1, 0))
        dot2.move_to(axes.c2p(1, 0))
        self.play(FadeIn(dot, scale=0.5))
        self.play(FadeIn(dot2, scale=0.5))
        self.play(dot.animate.move_to(axes.c2p(2, 0)), dot2.animate.move_to(axes.c2p(2, 0)))
        self.wait()
        self.play(dot.animate.move_to(axes.c2p(-2, 0)), dot2.animate.move_to(axes.c2p(-2, 0)))
        self.wait()
        self.play(dot.animate.move_to(axes.c2p(-1, 1)), dot2.animate.move_to(axes.c2p(-1, -1)))

        leftline = DashedLine(start=DOWN, end=UP).set_color(BLUE)
        rightline = DashedLine(start=DOWN, end=UP).set_color(BLUE)

        leftline.move_to(axes.c2p(-1,0)).set_opacity(0.2)
        rightline.move_to(axes.c2p(1,0)).set_opacity(0.2)

        self.play(FadeIn(leftline), FadeIn(rightline))

        unitcircle = Circle(color = GREEN, radius=0.8).move_to(axes.c2p(0,0)).set_fill(GREEN, opacity=0.5)

        self.play(FadeIn(unitcircle))

        dotx = Dot( (0, 0, 0)  ).set_color(YELLOW).move_to(axes.c2p(1,0)).scale(0.8).set_opacity(0.5)

        unitarrow = VMobject().move_to(axes.c2p(0,0))
        unitarrow.add_updater(lambda x: x.become(Line(unitcircle.get_center(), dotx.get_center()).set_color(PINK))) #UPDATER
        self.add(unitarrow)

        self.play(MoveAlongPath(dotx, unitcircle), rate_func=linear, run_time=5)
