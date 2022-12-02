import arcade

BREDDE = 350
HOEJDE = 700
MOVE = 5

class Våben:
    def __init__(self, fast_punkt, retningsvektor_x, retningsvektor_y, farve, retningsændring):
        self.fast_punkt = fast_punkt
        self.retningsvektor_x = retningsvektor_x
        self.retningsvektor_y = retningsvektor_y
        self.punkt = self.fast_punkt
        self.farve = farve
        self.retningsændring = retningsændring

    def opdater(self, delta_tid):
        x, y = self.punkt
        vx = self.retningsvektor_x
        vy = self.retningsvektor_y
        x += vx * delta_tid
        y += vy * delta_tid
        self.punkt = (x, y)
        self.retningsvektor_x += self.retningsændring

    def tegn(self):
        x, y = self.punkt
        arcade.draw_circle_filled(x, y, 5, self.farve)



class Vindue(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.csscolor.LIGHT_SKY_BLUE)

    def setup(self):
        self.våben = Våben((175, 50), 0, 20, arcade.csscolor.RED, 0)

    def update(self, delta_tid):
        self.våben.opdater(delta_tid)

    def on_draw(self):
        self.clear()
        self.våben.tegn()

    def key_press(self, key, modifiers):
        if key == arcade.key.D:
            self.våben.retningsændring = MOVE


def main():
    vindue = Vindue(BREDDE, HOEJDE, "Ret linje som klasse")
    vindue.setup()

    arcade.run()


main()