from manimlib import *
import numpy as np

class RouthDefinition(Scene):
    # CONFIG = {"title_kwargs": {
    #             "color" : YELLOW_C, 
    #             "opacity" : 0.7, 
    #             "font" : ""}
    #         }
    CONFIG = {
		"list_kwargs": {
			"math_mode": True,
		}
	}

# OPENING SCENE

    def construct(self):
        intro_words = Text("Das Routh Schema")#, **self.title_kwargs)
        intro_words.set_color(YELLOW_C).scale(2)

        underline = Underline(mobject=intro_words)
        underline.set_color(YELLOW_C)

        self.play(Write(intro_words))

        self.play(ShowCreation(underline),run_time=1)

        self.wait(1)

        self.play(ShrinkToCenter(intro_words), ShrinkToCenter(underline))

        self.wait(1)
        

# CRITERIA SCENE
        
        tf = Tex(   
                        r"{H(s) =",
                        r"{ {b_0 s^m + b_1 s^{m-1} + \hdots + b_{m-1} s + b_m}",
                        r"\over",
                        r"{a_n s^n + a_{n-1} s^{n-1} + \hdots + a_1} s + a_0} }",
                        r" = ",
                        r"{ {B(s)}",
                        r"\over",
                        r"{A(s)} }",
                        color=WHITE
                    )

        poly = Tex(   
                        r"{p(s) =",
                        r"{ ", r"a_n", r"s^n", r"+", r"a_{n-1}", r"s^{n-1}", r"+", r"\hdots", r"+", r"a_1", r"s", r"+", r"a_0", r"}", r"}",
                        color=GREEN_D
                    )

        for i in tf:
            self.play(Write(i))

        self.play( FadeToColor(tf[3],GREEN_D), FadeToColor(tf[7],GREEN_D) )

        tf.generate_target()
        tf.target.shift(UP*2)
        self.play(MoveToTarget(tf))
        
        self.wait(2)

        play_kw = {"run_time": 1.5}
        self.play( TransformMatchingTex(tf,poly), **play_kw )

        poly.generate_target()
        poly.target.shift(UP*2.5 + RIGHT*3).scale(0.8)
        self.play(MoveToTarget(poly))

        self.wait(2)

        self.play( FadeToColor(poly,WHITE) )

        condtitle = Title("Routh-Hurwitz Stabilitätskriterien").set_color(YELLOW_C)
        self.play(Write(condtitle))

        condlist = BulletedList(r"\text{p(s) muss ein Hurwitzpolynom sein}",
                                r"\text{Alle Nullstellen des p(s) müssen einen echt negativen Realteil haben.}",
                                r"\text{Kein Polynomkoeffizient verschwindet.}",
                                r"\text{Alle Polynomkoeffizienten besitzen das gleiche Vorzeichen.}",
                                r"\text{Die angegebene Bedingungen sind für Polynome Grad p(s) $\leq$ 2 notwendig und hinreichend.}",
                                **self.list_kwargs
                                ).scale(0.7).to_corner(LEFT)

        play_kwlist = {"run_time": 7.5}
        self.play(Write(condlist), **play_kwlist)

        self.wait(2)

        self.play(TransformMatchingTex(poly,poly.set_color_by_tex_to_color_map({
                "a_0": RED,
                "a_1": RED,
                "a_n": RED,
                "a_{n-1}": RED,
        }),transform_mismatches=True),
                FadeToColor(condlist[2],RED) 
        )
        
        self.wait(2)

        self.play(TransformMatchingTex(poly,poly.set_color_by_tex_to_color_map({
                "+": YELLOW,
        }),transform_mismatches=True),
                FadeToColor(condlist[3],YELLOW) 
        )

        self.wait(2)

        self.play(TransformMatchingTex(poly,poly.set_color_by_tex_to_color_map({
                "s^n": BLUE,
        }),transform_mismatches=True),
                FadeToColor(condlist[4],BLUE) 
        )

        #self.play(FadeOut(condlist), FadeOut(condtitle), FadeToColor(poly,WHITE), FadeOut(poly))
        # poly.generate_target()
        # poly.target.move_to(ORIGIN)
        # self.play(MoveToTarget(poly))

        self.play(*[FadeOut(mob)for mob in self.mobjects])

# ZICK ZACK SCENE

        zikzak = Title("Das Routh Schema").set_color(YELLOW_C)
        self.play(Write(zikzak))

        zikzak.generate_target()
        zikzak.target.to_corner(UP)
        self.play(MoveToTarget(zikzak))

        polyzz = Tex(   
                        r"{p(s) =",
                        r"{ ", r"a_n", r"s^n", r"+", r"a_{n-1}", r"s^{n-1}", r"+", r"a_{n-2}", r"s^{n-2}", r"+" , r"a_{n-3}", r"s^{n-3}", r"+", r"a_{n-4}", r"s^{n-4}", r"+", r"a_{n-5}", r"s^{n-5}", r"+" r"\hdots", r"+", r"a_1", r"s", r"+", r"a_0", r"}", r"}",
                        color=WHITE
                    ).scale(0.7)
        polyzz.to_corner(LEFT).shift(UP*2)

        polyzz.set_color_by_tex_to_color_map({
                "a_n": BLUE,
                "a_{n-1}": BLUE,
                "a_{n-2}": YELLOW,
                "a_{n-3}": YELLOW,
                "a_{n-4}": PINK,
                "a_{n-5}": PINK,
                })

        self.play(Write(polyzz))

        self.wait(2)

        an = Tex(r"a_n").set_color(BLUE)
        nton1 = Arrow(UP,DOWN,buff=0)
        an1 = Tex(r"a_{n-1}").set_color(BLUE)
        n1ton2 = Arrow(DL,UR,buff=0)
        an2 = Tex(r"a_{n-2}").set_color(YELLOW)
        n2ton3 = Arrow(UP,DOWN,buff=0)
        an3 = Tex(r"a_{n-3}").set_color(YELLOW)
        n3ton4 = Arrow(DL,UR,buff=0)
        an4 = Tex(r"a_{n-4}").set_color(PINK)
        n4ton5 = Arrow(UP,DOWN,buff=0)
        an5 = Tex(r"a_{n-5}").set_color(PINK)
        n5ton6 = Arrow(DL,UR,buff=0)
        an6 = Tex(r"\hdots")
        n6ton7 = Arrow(UP,DOWN,buff=0)
        an7 = Tex(r"\hdots")

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

        zzgroup=VGroup(an,nton1,an1,n1ton2,an2,n2ton3,an3,n3ton4,an4,n4ton5,an5,n5ton6,an6,an7).scale(0.8)
        
        play_kw = {"run_time": 4}
        self.play(Write(zzgroup),**play_kw)

        zikzak.generate_target()
        zikzak.target.shift(UP*4)
        #self.play(MoveToTarget(zikzak))

        polyzz.generate_target()
        polyzz.target.to_corner(UP)
        #self.play(MoveToTarget(zikzak))

        zzgroup.generate_target()
        zzgroup.target.shift(UP*2.5)
        self.play( MoveToTarget(zikzak), MoveToTarget(polyzz), MoveToTarget(zzgroup) )

        zzbox = SurroundingRectangle(zzgroup).set_color(BLACK)
        self.play(ShowCreation(zzbox))

        zztext = BulletedList("Die Anordnung wird als Zick-Zack Muster genannt.",
                              "Bei geradem Polynomgrad n die letzte Spalte mit einem Nullelement ausgefüllt wird.",
                              ).scale(0.8).to_corner(LEFT).shift(DOWN*2)

        self.play(Write(zztext))

        zztext3 = BulletedList("Das Polynom ist genau dann Hurwitzpolynom, wenn alle Elemente der ersten Spalte sich von Null unterscheiden und das gleiche Vorzeichen besitzen."
                            ).scale(0.8).to_corner(LEFT).next_to(zztext,DOWN)
        
        self.play(Write(zztext3))

        self.wait(5)

        self.play(*[FadeOut(mob)for mob in self.mobjects])
