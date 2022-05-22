from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

punch_sound = Audio('assets/nach', loop=False, autoplay=False)


for z in range(10):
    for x in range(10):
        Entity(
            model="cube", color=color.dark_gray, texture="white_cube", collider="box", ignore=True,
            position=(x, 0, z),
            parent=scene,
            origin_y=0.5,
        )


class TextureBox(Button):
    def __init__(self, position=(5, 2, 5)):
        super().__init__(
            parent=scene,
            position=position,
            model="cube",
            origin_y=0.5,
            texture="a.jpg",
            color=color.color(0, 0, 1)
        )

        self.texture_choice = 0
        self.textures = ["a.jpg", 'b.jpg', 'c.jpg', '1.png', '2.jpg', '3.jpg', '4.jpg',
                         '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg', '11.jpg', '12.jpg', '13.jpg']

    def input(self, key):
        if self.hovered:
            if key == 'left mouse down':
                punch_sound.play()
                self.texture_choice += 1
                self.texture_choice %= len(self.textures)
                self.texture = self.textures[self.texture_choice]


input_handler.bind('right arrow', 'd')
input_handler.bind('left arrow', 'a')
input_handler.bind('up arrow', 'w')
input_handler.bind('down arrow', 's')

TextureBox()

player = FirstPersonController()
app.run()
