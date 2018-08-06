# -*- coding: utf-8 -*-
"""
Created on Sun Aug  5 23:59:59 2018

@author: Ahmad
"""
import pyglet
from pyglet.window import key
from pyglet.window import mouse

from time import time # Used for FPS calc

class button(object):
    def __init__(self,x,y,colour,text,size=24):
        self.x = x
        self.y = y
        self.text = text
        self.size = size
        
        # Create text label, and set box size based on the text
        label = pyglet.text.Label(
                text,
                font_name = "Times New Roman",
                font_size = self.size,
                x=self.x, y=self.y,
                anchor_x="left", anchor_y="bottom"
                )
        self.width = label.content_width+10
        self.height = label.content_height+10
        
        # draw rectangle around text
        pyglet.graphics.draw(4,pyglet.gl.GL_QUADS,
                     ("v2i",self.create_quad_vertex_list(
                             self.x-5,self.y-5,self.width,self.height)),
                     ('c3B', tuple(list(colour)*4)))

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

class main(pyglet.window.Window):
    def __init__ (self):
        super(main, self).__init__(800, 800, fullscreen = False, vsync = True)
    
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
        
        
        new_game = button(self.width//2-100,self.height//2,(0,0,255),"New Game")
        
        # buttons
        self.buttons = [new_game]
        
        # draw labels
        
        main_batch.draw()
        
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
        for button in self.buttons:
            if button.clicked_on(x,y):
                print("Button " + button.text + " clicked!")

# change resource path
pyglet.resource.path = [r"C:\Users\Ahmad\Documents\GitHub\Classic-Game-Recreations\minesweeper\resources"]
pyglet.resource.reindex()

# Create window
greet_window = main()




        

















        

pyglet.app.run()