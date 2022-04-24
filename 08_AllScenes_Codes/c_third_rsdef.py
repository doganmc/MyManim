from manimlib import *
import numpy as np

class RouthHurwitzDefinition(Scene):
    CONFIG = {
		"list_kwargs": {
			"math_mode": True,
		}
	}

# OPENING SCENE

    def construct(self):
        # # # intro_words = Text("Routh-Hurwitz Stabilitätskriterium",font="Times New Roman").scale(0.7)#, **self.title_kwargs)
        # # # intro_words.set_color(YELLOW_C).scale(2)

        # # # underline = Underline(mobject=intro_words)
        # # # underline.set_color(YELLOW_C)

        # # # self.play(Write(intro_words))

        # # # self.play(ShowCreation(underline),run_time=1)

        # # # self.wait(1)

        # # # self.play(ShrinkToCenter(intro_words), ShrinkToCenter(underline))

        # # # self.wait(1)
        

# CRITERIA SCENE
        
        # # tf = Tex(   
        # #                 r"{G(s) =",
        # #                 r"{ {b_0 s^m + b_1 s^{m-1} + \hdots + b_{m-1} s + b_m}",
        # #                 r"\over",
        # #                 r"{a_n s^n + a_{n-1} s^{n-1} + \hdots + a_1} s + a_0} }",
        # #                 # r" = ",
        # #                 # r"{ {B(s)}",
        # #                 # r"\over",
        # #                 # r"{A(s)} }",
        # #                 color=WHITE
        # #             )

        poly = Tex(   
                        r"{p(s) =",
                        r"{ ", r"a_n", r"s^n", r"+", r"a_{n-1}", r"s^{n-1}", r"+", r"\hdots", r"+", r"a_1", r"s", r"+", r"a_0", r"}", r"}",
                        color=WHITE
                    )

        # # for i in tf:
        # #     self.play(Write(i))

        # # self.play( FadeToColor(tf[3],GREEN_D) )

        # # tf.generate_target()
        # # tf.target.shift(UP*2)
        # # self.play(MoveToTarget(tf))
        
        # # self.wait(1)

        # # play_kw = {"run_time": 1.5}
        # # self.play( TransformMatchingTex(tf,poly), **play_kw )
        
        self.play(Write(poly))

        self.wait(1)

        poly.generate_target()
        poly.target.shift(UP*2.5 + RIGHT*3).scale(0.8)
        self.play(MoveToTarget(poly))

        self.wait(2)

        self.play( FadeToColor(poly,WHITE) )

        condtitle = Title("Routh-Hurwitz Stabilitätskriterien").set_color(YELLOW_C)
        self.play(Write(condtitle))

        self.wait(4)

        condhurwitz = Text("p(s) ist genau dann ein Hurwitzpolynom, wenn:",font="Times New Roman",run_time=4).scale(0.9).set_color(WHITE).next_to(condtitle,DOWN*5).to_corner(LEFT)
        self.play(Write(condhurwitz))

        condlist = BulletedList(r"\text{Alle Nullstellen des p(s) einen negativen Realteil haben.}",
                                r"\text{Kein Polynomkoeffizient verschwindet.}",
                                r"\text{Alle Polynomkoeffizienten das gleiche Vorzeichen besitzen.}",
                                **self.list_kwargs,buff=1
                                ).scale(0.7).next_to(condhurwitz,DOWN*2).to_corner(LEFT)

        lastcond = Tex(r"\text{Die angegebene Bedingungen sind für Polynome Grad p(s) $\leq$ 2 notwendig und hinreichend.}").scale(0.7).next_to(condlist,DOWN*2).to_corner(LEFT)

        condbox = SurroundingRectangle(condlist).set_color(GREEN)
        polybox = SurroundingRectangle(poly).set_color(GREEN)

        self.play(ShowCreation(condbox),ShowCreation(polybox))

        # play_kwlist = {"run_time": 7.5}
        # self.play(Write(condlist), **play_kwlist)

        self.wait(1)

        self.play(Write(condlist[0],run_time=4))

        self.wait(1)

        condlist[1].set_color(RED_B)
        self.play(Write(condlist[1],run_time=4), FadeToColor(poly[1],RED_B), FadeToColor(poly[4],RED_B), FadeToColor(poly[9],RED_B), FadeToColor(poly[12],RED_B))

        self.wait(1)

        condlist[2].set_color(ORANGE)
        self.play(Write(condlist[2],run_time=4), FadeToColor(poly[3],ORANGE), FadeToColor(poly[6],ORANGE), FadeToColor(poly[8],ORANGE), FadeToColor(poly[11],ORANGE))

        self.wait(1)

        lastcond.set_color(BLUE)
        self.play(Write(lastcond,run_time=4), FadeToColor(poly[2],BLUE))

        self.wait(10)

        self.play(*[FadeOut(mob)for mob in self.mobjects])


# HURWITZ MATRIX AND DETERMINANT SCENE

        htitle = Title("Hurwitzmatrix").set_color(YELLOW)
        self.play(Write(htitle))

        poly.set_color(WHITE)
        self.play(Write(poly))

        self.wait(4)

        hmat = [ ["a_{n-1}","a_{n}","0","0","\\dots","\\dots"],
                 ["a_{n-3}","a_{n-2}","a_{n-1}","a_{n}","\\dots","\\dots"],
                 ["a_{n-5}","a_{n-4}","a_{n-3}","a_{n-2}","\\dots","\\dots"],
                 ["a_{n-7}","a_{n-6}","a_{n-5}","a_{n-4}","\\dots","\\dots"],
                 ["\\dots","\\dots","\\dots","\\dots","\\dots","a_2"],
                 ["0","0","\\dots","\\dots","0","a_0"]
                ]

        m = Matrix(hmat)
        m.scale(0.7).next_to(htitle,DOWN).to_corner(LEFT)
        self.play(Write(m))

        mcount = 0
        while mcount<6:
            self.play(FadeToColor(m[0][mcount*7],RED),run_time=0.5)
            mcount+=1

        h_nnmat = Tex(r"\rightarrow", r"\text{n x n Matrix}").next_to(m,RIGHT).scale(0.8)
        self.play(Write(h_nnmat))

        self.wait(5)

        hlist = BulletedList(   "Nicht vorhandene Koeffizienten werden also durch eine Null ersetzt.",
                                "Die Matrix ist dann positiv definit, wenn alle Hauptminoren (nordwestlichen Unterdeterminanten) positiv sind.",
                                math_mode=False).scale(0.8).next_to(m,DOWN*2).to_corner(LEFT)

        self.play(Write(hlist[0]),run_time=4)

        self.wait(5)

        self.play(Write(hlist[1]),run_time=5)

        self.wait(5)

        self.play(FadeOut(poly),FadeOut(m),FadeOut(h_nnmat),FadeOut(hlist))

        hexp = Tex(r"\text{Beispiel für} \hspace*{0.25cm} n=3 :").scale(0.8).set_color(GREEN).next_to(htitle,DOWN*2).to_corner(LEFT).shift(RIGHT)
        self.play(Write(hexp))

        poly_hexp = Tex(r"p(s)",r"=",r"a_3",r"s^3",r"+",r"a_2",r"s^2",r"+",r"a_1",r"s",r"+",r"a_0").scale(0.8).next_to(hexp,RIGHT*1.5)
        self.play(Write(poly_hexp))

        Hdet = Tex(r"H = ").scale(0.8).next_to(hexp,DOWN*5).to_corner(LEFT).shift(RIGHT)
        self.play(Write(Hdet))

        mat_hexp = [    ["a_2","a_3","0"],
                        ["a_0","a_1","a_2"],
                        ["0","0","a_0"],
                   ]
        
        mhexp = Matrix(mat_hexp)
        mhexp.scale(0.8).next_to(Hdet,RIGHT)
        self.play(Write(mhexp))

        self.wait(2)

        H1 = Tex(r"H_1",r"=",r"a_2",r">",r"0").set_color(TEAL_E)
        H2 = Tex(r"H_2",r"=",r"a_2 a_1",r"-",r"a_0 a_3",r">",r"0").set_color(ORANGE)
        H3 = Tex(r"H_3",r"=",r"a_0 H_2",r">",r"0").set_color(PINK)

        H123 = VGroup(H1,H2,H3).scale(0.8).arrange(DOWN)
        

        for line in H123:
            tm = -line.get_part_by_tex("=").get_center()
            line.shift(tm[0] * RIGHT)

        H123.next_to(mhexp,RIGHT*3)


        H1box = SurroundingRectangle(mhexp[0][-1]).set_color(TEAL_E)
        self.play(ShowCreation(H1box),Write(H1))

        self.wait(1)

        H2box = SurroundingRectangle(mhexp[0][0:2]).set_color(ORANGE).stretch_to_fit_height(1).shift(DOWN*0.3)
        self.play(ShowCreation(H2box),Write(H2))

        self.wait(1)

        H3box = SurroundingRectangle(mhexp[0][0:-1]).set_color(PINK)
        self.play(ShowCreation(H3box),Write(H3))

        self.wait(3)

        n3cond = BulletedList(r"\text{Für n $\geq$ 3 wird die Hurwitzdeterminante als eine neue hinreichende und}",math_mode=True).scale(0.8).next_to(Hdet,DOWN*5).to_corner(LEFT)
        n3cond1 = Tex(r"\text{notwendige Bedingung benutzt.").scale(0.8).next_to(n3cond,DOWN).to_corner(LEFT)
        self.play(Write(n3cond),run_time=4)
        self.play(Write(n3cond1),run_time=2)

        self.wait(15)

        self.play(*[FadeOut(mob)for mob in self.mobjects])


# SHOW p_0, ... , p_7 FROM [FirstWhyRouth] AND CROSS OUT THE NON-STABLE ONES.

        ps_h = Tex(r"p_0(s)","=",r"s^3",r"+",r"2",r"s^2",r"-",r"5",r"s",r"-",r"6")
        ps_1 = Tex(r"p_1(s)","=",r"2",r"s^4",r"+",r"2",r"s^2",r"+",r"s",r"+",r"1")
        ps_2 = Tex(r"p_2(s)","=",r"s^5",r"+",r"3",r"s^4",r"+",r"2",r"s^3",r"+",r"s^2",r"+",r"1")
        ps_3 = Tex(r"p_3(s)","=",r"5",r"s^6",r"+",r"3",r"s^5",r"+",r"2",r"s^4",r"+",r"7",r"s^3",r"+",r"s^2",r"+",r"9",r"s",r"+",r"1")
        ps_4 = Tex(r"p_4(s)","=",r"-",r"2",r"s^2",r"-",r"2",r"s",r"-",r"1")
        ps_5 = Tex(r"p_5(s)","=",r"s^2",r"+",r"4",r"s",r"-",r"3")
        ps_6 = Tex(r"p_6(s)","=",r"s^2",r"+",r"s",r"+",r"1")
        ps_7 = Tex(r"p_7(s)","=",r"s",r"+",r"8")

        polys = VGroup(ps_h,ps_1,ps_2,ps_3,ps_4,ps_5,ps_6,ps_7)
        polys.arrange(DOWN,buff=MED_LARGE_BUFF)


        for line in polys:
            tm = -line.get_part_by_tex("=").get_center()
            line.shift(tm[0] * RIGHT)

        polys.to_corner(LEFT)

        self.play(Write(polys))

        self.wait(3)

        polycond = BulletedList("Kein Polynomkoeffizient verschwindet.",
                                "Alle Polynomkoeffizienten besitzen das gleiche Vorzeichen.",
                                ).scale(0.5).to_corner(UR)

        polycondbox = SurroundingRectangle(polycond).set_color(BLACK)

        self.play(ShowCreation(polycond), ShowCreation(polycondbox))

        self.wait(1)

        cross1 = Cross(ps_1).set_color(BLUE)
        cross2 = Cross(ps_2).set_color(YELLOW)
        cross5 = Cross(ps_5).set_color(YELLOW)
        crossh = Cross(ps_h).set_color(YELLOW)

        self.play( FadeToColor(polycond[0],BLUE) )
        self.play( ShowCreation(cross1), FadeToColor(ps_1,RED) )

        self.wait(8)
        
        self.play( FadeToColor(polycond[1],YELLOW) )
        self.play( ShowCreation(cross2), FadeToColor(ps_2,RED) )
        self.play( ShowCreation(cross5), FadeToColor(ps_5,RED) )
        self.play( ShowCreation(crossh), FadeToColor(ps_h,RED) )

        self.wait(11)
        
        self.play( FadeToColor(ps_4,GREEN), FadeToColor(ps_6,GREEN), FadeToColor(ps_7,GREEN) )

        self.wait(10)

        self.play(      FadeOut(ps_1), FadeOut(cross1),
                        FadeOut(ps_2), FadeOut(cross2),
                        FadeOut(ps_5), FadeOut(cross5),
                        FadeOut(ps_h), FadeOut(crossh),
                        FadeOut(ps_4), FadeOut(ps_6), FadeOut(ps_7),
                        FadeOut(polycond), FadeOut(polycondbox) 
                )


        ps_3.generate_target()
        ps_3.target.move_to(ORIGIN)
        self.play(MoveToTarget(ps_3))

        self.wait(1)

        ps3q = Tex(r"?").set_color(ORANGE).next_to(ps_3,ORIGIN,buff=0).scale(2)
        self.play(Transform(ps_3,ps3q))

        self.wait(7)

        self.play(*[FadeOut(mob)for mob in self.mobjects])


# SECOND OPENING SCENE

        intro_words2 = Text("Das Routh-Schema",font="Times New Roman")
        intro_words2.set_color(YELLOW_C).scale(2)

        underline2 = Underline(mobject=intro_words2)
        underline2.set_color(YELLOW_C)

        self.play(Write(intro_words2))

        self.play(ShowCreation(underline2),run_time=1)

        self.wait(2)

        self.play(ShrinkToCenter(intro_words2), ShrinkToCenter(underline2))

        self.wait(1)


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

        polyzz.generate_target()
        polyzz.target.to_corner(UP)

        zzgroup.generate_target()
        zzgroup.target.shift(UP*2.5)
        self.play( MoveToTarget(zikzak), MoveToTarget(polyzz), MoveToTarget(zzgroup) )

        zzbox = SurroundingRectangle(zzgroup).set_color(BLACK)
        self.play(ShowCreation(zzbox))

        zztext = BulletedList("Die Anordnung wird als Zick-Zack Muster genannt.",
                              "Bei geradem Polynomgrad n, wird die letzte Spalte mit einem Nullelement ausgefuellt.",
                              "Bei ungeradem Polynomgrad n, wird eine Nullspalte als letzte Spalte gestaltet.",
                              "Das Polynom ist genau dann Hurwitzpolynom, wenn alle Elemente der ersten Spalte sich von Null unterscheiden und das gleiche Vorzeichen besitzen."
                              ).scale(0.7).to_corner(LEFT).shift(DOWN*2)

        # for i in zztext:
        #         self.play(Write(i),run_time=4)
        self.play(Write(zztext[0]), run_time=4)
        self.wait(2)
        self.play(Write(zztext[1]), run_time=4)
        self.wait(2)
        self.play(Write(zztext[2]), run_time=4)
        self.wait(2)
        self.play(Write(zztext[3]), run_time=6)

        self.wait(10)

        self.play(*[FadeOut(mob)for mob in self.mobjects])