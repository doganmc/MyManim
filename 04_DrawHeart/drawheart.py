from manimlib import *
import numpy as np
import math

class Heart(Scene):
    CONFIG = {
        "axes_kwargs": {
          
        "axis_config": {
            "stroke_color": GREY,
            "stroke_width": 2,
            "include_ticks": True,
            "include_tip": True,
            "line_to_number_buff": SMALL_BUFF,
            "label_direction": DR,
            "number_scale_val": 0.5,
        },
        "y_axis_config": {
            "label_direction": DR,
            "stroke_color":GREY,
        },
        "background_line_style": {
            "stroke_color": GREY,
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

        axes = Axes(**self.axes_kwargs)
        #self.add(axes)

        name1 = Text("Euler").set_color(YELLOW)
        name2 = Text("Newton").set_color(BLUE)
        name3 = Text ("Maxwell").set_color(PINK)
        name4 = Text("Lagrange").set_color(ORANGE)

        name1.move_to(axes.c2p(0, 0))
        self.play(Write(name1))
        self.play(name1.animate.move_to(axes.c2p(7, 3)))

        name2.move_to(axes.c2p(0, 0))
        self.play(Write(name2))
        self.play(name2.animate.move_to(axes.c2p(-7, 3)))

        name3.move_to(axes.c2p(0, 0))
        self.play(Write(name3))
        self.play(name3.animate.move_to(axes.c2p(7, -3)))

        name4.move_to(axes.c2p(0, 0))
        self.play(Write(name4))
        self.play(name4.animate.move_to(axes.c2p(-7, -3)))
        
        #func = lambda x : np.sin(x)
        #graph = axes.get_graph(func, color=RED, x_range = len(3))
        #graph = axes.get_parametric_curve(func)
        #self.play(Write(graph))

        self.wait(1)

        func = ParametricCurve(self.func, t_range = np.array([0, 2*PI]), fill_opacity=0.5).set_color(RED).move_to(axes.c2p(0,0))
        self.play(ShowCreation(func.scale(0.2), run_time=3))

        tugraz = Text("TUGraz").move_to(axes.c2p(0,0))
        self.play(Write(tugraz))

    def func(self, t):
        return np.array( (  16 * ( np.sin(t) ** 3 ), 13 * np.cos(t) - 5* np.cos(2*t) - 2 * np.cos(3*t) - np.cos(4*t), 0  ) )
