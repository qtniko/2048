import tkinter as tk
import random
from typing import KeysView

root = tk.Tk()
root.title('2048')

board = tk.Frame(
    master=root,
    bg='#d4d5d6'
)
panel = tk.Frame(
    master=root,
    bg='#c2c2c2'
)

board.columnconfigure([1, 2, 3, 4], weight=1, minsize=50)
board.rowconfigure([1, 2, 3, 4], weight=1, minsize=50)

colors = [
    'snow',
    'papayawhip',
    '#fad275',
    'darkorange',
    'coral',
    'lightcoral',
    'lightpink',
    'hotpink',
    'orchid',
    'fuchsia',
    'mediumorchid',
    'blueviolet',
    'mediumslateblue',
    'slateblue',
    'cornflowerblue',
    'lightskyblue',
    'paleturquoise',
    'mediumturquoise'
]
tiles = []
unlocked_tiles = []
empty_tiles = []
genSwitch = []
weight = [4, 2, 2, 2, 2, 2, 2, 2, 2, 2]

class tile:
    def __init__(self, x, y):
        self.mergable=True
        self.x = x
        self.y = y
        self.value = 0
        self.frame = tk.Frame(master=board)
        self.frame.grid(row=y, column=x, padx=5, pady=5, sticky='nsew')
        self.label = tk.Label(
            master=self.frame,
            text='',
            width=11,
            height=5,
            bg=colors[0],
        )
        self.label.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
        tiles.append(self)

def end():
    for x in range(4):
        x+=1
        for y in range(4):
            y+=1
            for tile1 in tiles:
                if tile1.x == x and tile1.y == y:
                    if tile1.value == 0:
                        unlocked_tiles.append(tile1)
                        empty_tiles.append(tile1)
    for tile in tiles:
        tile.mergable = True
    generate()

def generate():
    if len(genSwitch)>0:
        available_tiles = [tile for tile in empty_tiles]
        loop=1
        while loop==1:
            loop=0
            gen = random.choice(available_tiles)
            if gen.value != 0:
                loop=1
        value = random.choice(weight)
        gen.value = value
        gen.label['text'] = str(value)
        gen.label['bg'] = colors[value//2]
    empty_tiles.clear()
    genSwitch.clear()

def merge(tile1, tile2):
    genSwitch.append('MeRg')
    tile1.value = 0
    tile1.label['text'] = ''
    tile1.label['bg'] = colors[0]
    tile2.value = (tile2.value)*2
    tile2.label['text'] = str(tile2.value)
    tile2.label['bg'] = colors[(colors.index(tile2.label['bg']))+1]
    score_display['text'] = str(int(score_display['text'])+tile2.value)

def move(tile1, tile2):
    genSwitch.append('MoOoOoOV')
    tile2.value = tile1.value
    tile2.label['text'] = tile1.label['text']
    tile2.label['bg'] = tile1.label['bg']
    tile1.value = 0
    tile1.label['text'] = ''
    tile1.label['bg'] = colors[0]

def down():
    for i in range(3):
        for y in range(3):
            y = 3 - y
            for x in range(4):
                x+=1
                for tile1 in tiles:
                    if tile1.x == x and tile1.y == y:
                        if tile1.value == 0: continue
                        for tile2 in tiles:
                            if tile2.x == x and tile2.y == y+1:
                                if tile1.value == tile2.value:
                                    if tile1.mergable == True and tile2.mergable == True:
                                        merge(tile1, tile2)
                                        tile1.mergable = False
                                        tile2.mergable = False
                                elif tile2.value == 0:
                                    move(tile1, tile2)
    end()
def up():
    for i in range(3):
        for y in range(3):
            y = 2 + y
            for x in range(4):
                x+=1
                for tile1 in tiles:
                    if tile1.x == x and tile1.y == y:
                        if tile1.value == 0: continue
                        for tile2 in tiles:
                            if tile2.x == x and tile2.y == y-1:
                                if tile1.value == tile2.value:
                                    if tile1.mergable == True and tile2.mergable == True:
                                        merge(tile1, tile2)
                                        tile1.mergable = False
                                        tile2.mergable = False
                                elif tile2.value == 0:
                                    move(tile1, tile2)
    end()
def right():
    for i in range(3):
        for y in range(4):
            y+=1
            for x in range(3):
                x = 3 - x
                for tile1 in tiles:
                    if tile1.x == x and tile1.y == y:
                        if tile1.value == 0:continue
                        for tile2 in tiles:
                            if tile2.x == x+1 and tile2.y == y:
                                if tile1.value == tile2.value:
                                    if tile1.mergable == True and tile2.mergable == True:
                                        merge(tile1, tile2)
                                        tile1.mergable = False
                                        tile2.mergable = False
                                elif tile2.value == 0:
                                    move(tile1, tile2)
    end()
def left():
    for i in range(3):
        for y in range(4):
            y+=1
            for x in range(3):
                x = 2 + x
                for tile1 in tiles:
                    if tile1.x == x and tile1.y == y:
                        if tile1.value == 0: continue
                        for tile2 in tiles:
                            if tile2.x == x-1 and tile2.y == y:
                                if tile1.value == tile2.value:
                                    if tile1.mergable == True and tile2.mergable == True:
                                        merge(tile1, tile2)
                                        tile1.mergable = False
                                        tile2.mergable = False
                                elif tile2.value == 0:
                                    move(tile1, tile2)
    end()

def keypress(key):
    if key.keysym == 'Down': down()
    if key.keysym == 'Up': up()
    if key.keysym == 'Right': right()
    if key.keysym == 'Left': left()

    if key.keysym == 's': down()
    if key.keysym == 'w': up()
    if key.keysym == 'd': right()
    if key.keysym == 'a': left()

tile_1 = tile(1, 1)
tile_2 = tile(1, 2)
tile_3 = tile(1, 3)
tile_4 = tile(1, 4)

tile_5 = tile(2, 1)
tile_6 = tile(2, 2)
tile_7 = tile(2, 3)
tile_8 = tile(2, 4)

tile_9 = tile(3, 1)
tile_10 = tile(3, 2)
tile_11 = tile(3, 3)
tile_12 = tile(3, 4)

tile_13 = tile(4, 1)
tile_14 = tile(4, 2)
tile_15 = tile(4, 3)
tile_16 = tile(4, 4)

score_tag = tk.Label(
    master=panel,
    text='Score:',
    width=20,
    height=1
)
score_tag.pack(fill=tk.BOTH, expand=True)
score_display = tk.Label(
    master=panel,
    text='0',
    width=20,
    height=1
)
score_display.pack(fill=tk.BOTH, expand=True)

for t in tiles:
     empty_tiles.append(t)
genSwitch.append('uwu')
generate()
for t in tiles:
    empty_tiles.append(t)
genSwitch.append('owo')
generate()

#c=0
#for i in tiles:
#    i.value=2**c
#    i.label['text']=str(2**c)
#    i.label['bg']=colors[c]
#    c+=1

board.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
panel.pack(padx=5, pady=5, fill=tk.BOTH)
root.bind("<Key>", keypress)
root.mainloop()
