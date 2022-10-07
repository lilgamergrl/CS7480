import pyxel
import random

"""
To run:
pyxel sketch_two
pyxel run sketch_two.py
pyxel play sketch_two.pyxapp --- when the app is playable as an exe
"""


class App:
    def __init__(self):
        self.top_of_screen = 160
        self.side_of_screen = 120
        self.player_y = 5
        self.player_x = 5
        self.block_count = 5
        self.isalive = False
        self.start = False

        self.blocks_x, self.blocks_y = self.get_blocks()
        pyxel.init(self.top_of_screen, self.side_of_screen, title="Otter Kick")
        img = pyxel.image(0).load(0, 0, "assets/otter_idle_1.png")
        pyxel.run(self.update, self.draw)

    def get_blocks(self):

        arr_y = []
        arr_x = []
        for i in range(self.block_count):
            x = random.randint(self.player_y + 50, self.top_of_screen)
            y = random.randint(self.player_x + 100, self.side_of_screen)
            if x not in arr_x:
                arr_x.append(x)
            else:
                while x in arr_x:
                    x = random.randint(self.player_y + 50, self.top_of_screen)
            arr_x.append(x)
            if y not in arr_y:
                arr_y.append(y)
            else:
                while y in arr_y:
                    y = random.randint(self.player_x + 100, self.side_of_screen)
            arr_y.append(y)
        if len(arr_x) == len(arr_y) == self.block_count:
            return arr_x, arr_y
        else:
            while len(arr_x) < self.block_count and len(arr_x) != len(arr_y) and \
                    self.block_count > len(arr_y) and len(arr_x) != len(arr_y):
                if len(arr_x) < len(arr_y):
                    arr_x.append(random.randint(self.player_y + 50, self.top_of_screen))
                elif len(arr_x) > len(arr_y):
                    arr_y.append(random.randint(self.player_x + 100, self.side_of_screen))
            return arr_x, arr_y

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()
        if pyxel.btnp(pyxel.KEY_DOWN):
            self.start = True
            self.isalive = True
            self.draw()

        if self.isalive and self.start:

            if pyxel.btnp(pyxel.KEY_UP):
                self.player_y += 3
            elif pyxel.btnp(pyxel.KEY_DOWN):
                self.player_y -= 3
            elif pyxel.btnp(pyxel.KEY_RIGHT):
                self.player_x += 3
            elif pyxel.btnp(pyxel.KEY_LEFT):
                self.player_x -= 3
        self.draw()

    def draw(self):
        print("Drawing")
        if not self.isalive and not self.start:
            pyxel.cls(0)
            pyxel.text(55, 41, "Hello, Pyxel!", pyxel.frame_count % 16)
            pyxel.image(0).load(self.player_x, self.player_y, "assets/otter_idle_1.png")
            pyxel.blt(61, 66, 0, 0, 0, 38, 16)
            print("Stage1")

        # Draw player
        if self.start:
            print("Stage2")
            for x, y in zip(self.blocks_x,self.blocks_y):
                img2 = pyxel.image(7).load(x,y)
                pyxel.blt(x , y, 0, 64, 32, 32, 8, 12)
                #pyxel.blt(self.blocks_x[i], self.blocks_y[i], 0, 0, 16, 40, 8, 12)


App()
