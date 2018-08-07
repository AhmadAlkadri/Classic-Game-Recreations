# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 23:59:59 2018

@author: Ahmad
"""
import pyglet
from pyglet.window import key
from pyglet.window import mouse

from random import randint

class button(object):
    def __init__(self,x,y,colour,text,size=24,width=0,height=0):
        self.x = x
        self.y = y
        self.text = text
        self.size = size
        self.width = width
        self.height = height
        
        # Create text label, and set box size based on the text
        if text:
            label = pyglet.text.Label(
                    text,
                    font_name = "Times New Roman",
                    font_size = self.size,
                    x=self.x, y=self.y,
                    anchor_x="left", anchor_y="bottom")
            self.width = label.content_width
            self.height = label.content_height
        
        # draw rectangle around text
        pyglet.graphics.draw(4,pyglet.gl.GL_QUADS,
                     ("v2i",self.create_quad_vertex_list(
                             self.x,self.y,self.width,self.height)),
                     ('c3B', tuple(list(colour)*4)))
        if text:
            label.draw()
        
    @staticmethod
    def create_quad_vertex_list(x, y, width, height):
        return x, y, x + width, y, x + width, y + height, x, y + height
    
    def clicked_on(self,mouse_x,mouse_y):
        if (self.x <= mouse_x <= (self.x + self.width)) and \
            (self.y <= mouse_y <= (self.y + self.height)):
                return True
        else:
            return False

class tile(button):
    def __init__(self,x,y,side,value,revealed=False):
        self.x = x
        self.y = y
        self.side = side
        self.value = value
        self.revealed = revealed
        self.color = (0,0,255)
        super(tile,self).__init__(self.x,self.y,self.color,"",width=self.side,height=self.side)

        self.draw_border()
        
    # Draws border around the tile
    def draw_border(self):
        x,y,s = self.x,self.y,self.side
        coords = (x,y,x+s,y,x+s,y+s,x,y+s)
        pyglet.graphics.draw(4, pyglet.gl.GL_LINE_LOOP,
                             ("v2f", coords),
                             ("c3f", (1.,1.,1.)*4))
    
    def redraw(self):
        super(tile,self).__init__(self.x,self.y,self.color,"",width=self.side,height=self.side)
        self.draw_border()
    
    def click(self):
        self.revealed = True
        self.color = (255,0,0)
        super(tile,self).__init__(self.x,self.y,self.color,"",width=self.side,height=self.side)

class intro(pyglet.window.Window):
    def __init__ (self):
        super(intro, self).__init__(800, 800, fullscreen = False, vsync = True)
    
    def on_draw(self):
        self.clear()
        
        # welcome message
        main_batch = pyglet.graphics.Batch()
        greeting = pyglet.text.Label("Welcome to Minesweeper!",
                  font_name = "Times New Roman",
                  font_size = 36,
                  x=self.width//2, y=self.height//2 + 200,
                  anchor_x="center", anchor_y="center",
                  batch=main_batch)
        
        # buttons
        self.new_game = button(self.width//2-100,self.height//2,(0,0,255),"New Game")
        
        # draw labels
        main_batch.draw()
    
    def on_mouse_press(self, x, y, button, modifiers):
        if self.new_game.clicked_on(x,y):
            main()
            self.close()

class main(pyglet.window.Window):
    def __init__ (self):
        # grid specifications
        self.sbox = 50 # side-length of one tile
        self.nbox = 10 # number of tiles in a side-length
        
        # initialize window
        super(main, self).__init__(self.sbox*self.nbox,self.sbox*self.nbox,fullscreen = False, vsync = True)
        self.grid = self.init_grid()
        
    def on_draw(self):
        self.clear()
        
        # draw grid
        for row in self.grid:
            for square in row:
                square.redraw()
        
        # welcome message
        main_batch = pyglet.graphics.Batch()        
        
        
                    
        # draw labels
        main_batch.draw()
    
    def init_grid(self):
        # get mine locations
        locs = [i for i in range(0,self.nbox**2)]
        num_mines = self.nbox**2//10
        mines = []
        for i in range(0,num_mines):
            ind = randint(0,len(locs)-1)
            mines.append(locs[ind])
            del locs[ind]
        
        # populate mine locations in grid
        grid_vals = [[0 for _ in range(0,self.nbox)] for _ in range(0,self.nbox)]
        for mine in mines:
            i = mine // self.nbox
            j = mine % self.nbox
            grid_vals[i][j] = -1
        print(grid_vals)
        
        # populate values depending on how many mines surround a tile
        for i in enumerate(grid_vals):
            for j in enumerate(grid_vals):
                pass
        
        # draw_grid
        grid = []
        for i in range(0,self.nbox):
            row = []
            for j in range(0,self.nbox):
                row.append(tile(i*self.sbox,j*self.sbox,self.sbox,0))
            grid.append(row)
        return grid
        
    def on_key_press(self, symbol, modifiers):
        self.clear()
        self.close()
        if symbol == key.A:
            print('The "A" key was pressed.')
        elif symbol == key.LEFT:
            print('The left arrow key was pressed.')
        elif symbol == key.ENTER:
            print('The enter key was pressed.')
    
    def on_mouse_press(self, x, y, button, modifiers):            
        if button == mouse.LEFT:
            print('The left mouse button was pressed.')
            print("Location: " + str(x) + "," + str(y))

# change resource path
pyglet.resource.path = [r"C:\Users\Ahmad\Documents\GitHub\Classic-Game-Recreations\minesweeper\resources"]
pyglet.resource.reindex()

# start game
intro()
pyglet.app.run()