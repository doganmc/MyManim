from __future__ import division
from time import strptime
from tkinter import font

from matplotlib import mathtext
from manimlib import *
#from manimlib.mobject.svg import brace
import numpy as np

class Opening(Scene):
    CONFIG = {"title_kwargs": {
                "color" : YELLOW_C, 
                "opacity" : 0.7, 
                "font" : ""}
            }

    def construct(self):
        #intro_words = Text("The Nyquist Criterion", font="Times New Roman", font_size=144)
        intro_words = Text("The Nyquist Criterion", **self.title_kwargs)
        intro_words.set_color(YELLOW_C).scale(2)

        underline = Underline(mobject=intro_words)
        underline.set_color(YELLOW_C)

        self.play(Write(intro_words))

        self.play(ShowCreation(underline),run_time=1)

        #self.play(self.camera.frame.animate.shift(OUT * 200)) #Makes the scene disappear without fading out.
        #self.play(self.camera.frame.animate.scale(100))    #NICE ALTERNATIVE
        #self.play(*[FadeOut(mob)for mob in self.mobjects]) #NICE ALTERNATIVE

        self.play(ShrinkToCenter(intro_words), ShrinkToCenter(underline))


class Plant(Scene):
    def construct(self):

        strp = ['Plant','P(s)']
        self.display_plantp(strp)

    def display_plantp(self, strp):
        plantp = VGroup()
        for s in strp:
            t = self.get_text(s)
            plantp.add(t)

        plantp.to_edge(UP, buff=0.3)
        plantp.arrange(DOWN, buff=0.3)

        rectplant = Rectangle()
        #plantp = Tex(r"\text{Plant}\\\text{P(s)}")
        linetoplant = Line([-4, 0, 0], [-2, 0, 0])
        linetoy = Line([2, 0, 0], [3, 0, 0])

        rectcont = Rectangle().shift(UP*2 + LEFT*4)
        #contc = Tex(r"\centering \text{Controller} \text{C(s)}").shift(UP*2 + LEFT*4).arrange(DOWN, center=False, aligned_edge=LEFT)
        contc = VGroup(Text("Controller"), Text("C(s)")).to_edge(UP, buff=0.3).arrange(DOWN, buff=0.3).shift(UP*2 + LEFT*4)
        linetocont = Line([-7, 2, 0], [-6, 2, 0])

        sumcirc = Circle(radius=0.2, color = WHITE).next_to(linetocont,LEFT,aligned_edge=LEFT) #not the best alignment
        sumsign = Tex("-").next_to(sumcirc,DR/3)

        linetoy2 = Line([5, 2, 0], [7, 2, 0])
        linetodown = Line([6, 2, 0], [6, -0.3, 0])
        linetoleft = Line([6, -0.3, 0], [-7.25, -0.3, 0])
        linetoup = Line(start=DOWN,end=UP).next_to(sumcirc,DOWN,aligned_edge=UP)
        linetocirc = Line(LEFT,RIGHT).next_to(sumcirc,LEFT,aligned_edge=RIGHT) #better alignment example

        refvalue = Tex("r").next_to(linetocirc,UP)
        outvalue = Tex("y").next_to(linetoy2,UR)

        frame = self.camera.frame
        self.camera.frame.save_state()
        frame2 = frame.copy()
        #frame2.set_width(rect.width)
        frame2.set_width(8)
        self.play(Transform(frame, frame2))

        self.play(ShowCreation(rectplant), ShowCreation(linetoplant), ShowCreation(linetoy))
        self.play(Write(plantp))
        #self.play(Restore(self.camera.frame))

        frame3 = frame.copy()
        frame3.set_width(20)
        self.play(Transform(frame, frame3))

        self.play(ApplyMethod(plantp.shift, UR*2), MaintainPositionRelativeTo(rectplant, plantp), 
                                                   MaintainPositionRelativeTo(linetoplant, plantp), 
                                                   MaintainPositionRelativeTo(linetoy, plantp) )

        self.wait(1)
        
        self.play(ShowCreation(rectcont), ShowCreation(linetocont))
        self.play(Write(contc))

        self.play(ShowCreation(linetoy2), ShowCreation(linetodown), ShowCreation(linetoleft), ShowCreation(linetoup), ShowCreation(linetocirc))

        self.play(ShowCreation(sumcirc), Write(sumsign))

        self.play(Write(refvalue),Write(outvalue))

        self.play(  FadeIn(linetoplant.add_tip()),
                    FadeIn(linetocont.add_tip()),
                    FadeIn(linetoy2.add_tip()),
                    FadeIn(linetoup.add_tip()),
                    FadeIn(linetocirc.add_tip())  )

        self.wait(1)

        numer = Tex(r'C(s)P(s)')
        divline = Line().next_to(numer,DOWN,buff=0.2).scale(1.5)
        denom = Tex(r'1+C(s)P(s)').next_to(divline,DOWN,buff=0.2)
        TS = Tex(r'T(s) = ').next_to(divline,LEFT)

        eqn = VGroup(TS,numer,divline,denom).shift(DOWN*2.5 + LEFT).scale(1.4)
        self.play(Write(eqn))
        
        self.wait(2)

        #self.play(Fade(numer.set_color_by_tex(r'C(s)P(s)',ORANGE)))
        self.play(FadeToColor(numer, ORANGE), FadeToColor(contc,ORANGE), FadeToColor(plantp,ORANGE))

        self.wait(2)

        #self.play(FadeIn(numer.set_color_by_tex(r'C(s)P(s)',WHITE)))
        self.play(FadeToColor(numer, WHITE), FadeToColor(contc,WHITE), FadeToColor(plantp,WHITE))

        self.wait(2)

        #self.play(FadeIn(numer.set_color_by_tex(r'C(s)P(s)',BLUE)))
        self.play(FadeToColor(denom, BLUE), FadeToColor(contc,BLUE), FadeToColor(plantp,BLUE), FadeToColor(sumsign,BLUE))

        self.wait(2)

        self.play(FadeToColor(denom, WHITE), FadeToColor(contc,WHITE), FadeToColor(plantp,WHITE), FadeToColor(sumsign,WHITE))

        framebox1 = SurroundingRectangle(rectcont, buff = .1).stretch_to_fit_width(11).shift(RIGHT*3)
        self.play(ShowCreation(framebox1))

        numer2 = Tex(r'L(s)').next_to(divline,UP,buff=0.2).scale(1.4)
        denom2 = Tex(r'1+L(s)').next_to(divline,DOWN,buff=0.2).scale(1.4)

        self.play(TransformMatchingTex(numer,numer2))
        self.play(TransformMatchingTex(denom,denom2))

        framebox2 = SurroundingRectangle(divline, buff = .1).stretch_to_fit_height(4)
        self.play(ShowCreation(framebox2))

        self.play(FadeOut(framebox1),FadeOut(framebox2))

        rightequal = Tex(r'=').next_to(divline,RIGHT,aligned_edge=RIGHT)
        rightline = Line().next_to(rightequal,RIGHT,aligned_edge=LEFT).scale(0.8)
        rightnumer = Tex(r'\mu_T(s)').next_to(rightline,UP,buff=0.2)
        rightdenom = Tex(r'v_T(s)').next_to(rightline,DOWN,buff=0.2)

        righteq = VGroup(rightequal,rightline,rightnumer,rightdenom).scale(1.4).next_to(eqn,RIGHT)
        self.play(Write(righteq))


    def get_text(self, strp):
        return Text(strp)
