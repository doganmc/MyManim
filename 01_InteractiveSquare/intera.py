from manimlib import *
import numpy as np

class Interactive(Scene):
    def construct(self):
        circ = Circle(radius=0.4)
        self.add(circ)
        
        #always(circ.move_to, self.mouse_drag_point) #move the object to the mouse drag point
        always(circ.move_to, self.mouse_point) #move the object with the mouse point

        rect = Rectangle().next_to(circ).shift(RIGHT).set_color(BLUE)
        self.play(ShowCreation(rect))

        #self.embed() # Activates "Interactive Shell"
        #ControlMobject()
        #EnableDisableButton()
        #Checkbox()

        checkmark = self.get_checkmark(rect)
        self.play(Write(checkmark))

### ### ### PLAY AND CLEAR BUTTON (Play creates the square and the checkmark, Clear removes them.)
    def init_play_button(self):
        play_rect = Text("Play").add_background_rectangle(color=BLACK, opacity=1, buff=0.25).to_corner(UR)

        def play_clicked(mobject):
                self.sqr = Square()
                self.play(ShowCreation(self.sqr))
                self.checksqr = Tex("\\checkmark")
                self.play(Write(self.checksqr))
                print("Created")

        self.play_btn = Button(play_rect, play_clicked)
        self.add(self.play_btn)

    def init_clear_button(self):
        clear_rect = Text("Clear") \
            .add_background_rectangle(color=BLACK, opacity=1, buff=0.25)
        clear_rect.set_width(self.play_btn.get_width()).next_to(self.play_btn, DOWN)

        def clear_clicked(mobject):
            if self.sqr != None and self.checksqr != None:
                self.play(FadeOut(self.sqr))
                self.play(FadeOut(self.checksqr))
                self.sqr = None
            print("Cleared")

        self.clear_btn = Button(clear_rect, clear_clicked)
        self.add(self.clear_btn)

    def setup(self):
        self.init_play_button()
        self.init_clear_button()
### ### ###

### CHECKMARK FUNCTION
    def get_checkmark(self, obj):
        checkmark = Tex("\\checkmark")
        checkmark.set_color(GREEN)
        checkmark.scale(1.25)
        checkmark.next_to(obj, ORIGIN, buff = 0)
        return checkmark
