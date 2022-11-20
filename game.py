from tkinter import messagebox, Tk
import pygame
import sys

window_width = 600
window_height = 600
columns=25
rows=25

window = pygame.display.set_mode((window_width, window_height))

box_width= window_width // columns
box_height= window_height // rows

grid=[]

class Box:
    def __init__(self,i,j):
        self.x=i
        self.y=j
        self.wall=False
        self.starting=False
        self.ending=False
    def draw(self,win,color):
        pygame.draw.rect(win,color,(self.x*box_width,self.y*box_height,box_width-2,box_height-2))


for i in range(rows):
    arr = []
    for j in range(columns):
        arr.append(Box(i, j))
    grid.append(arr)




def main():
    begin_search = False
    target_box_set = False
    start_box_set = False
    #searching = True
    target_box = None
    start_box = None
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousearray=pygame.mouse.get_pressed()
                if mousearray[1] and not start_box_set:
                    i = x // box_width
                    j = y // box_height
                    start_box = grid[i][j]
                    start_box.starting = True
                    start_box_set = True
                    start_box.visited = True
                if mousearray[2] and not target_box_set:
                    i = x // box_width
                    j = y // box_height
                    target_box = grid[i][j]
                    target_box.ending = True
                    target_box_set = True
            elif event.type == pygame.MOUSEMOTION:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                
                if event.buttons[0]:
                    i = x // box_width
                    j = y // box_height
                    if i<rows and j<columns:
                        grid[i][j].wall = True
                
            if event.type == pygame.KEYDOWN and target_box_set and start_box_set:
                begin_search = True

        window.fill((0,0,0))
        for i in range(rows):
            for j in range(columns):
                box = grid[i][j]
                box.draw(window, (50, 50, 50))
                if box.starting:
                    box.draw(window, (0, 200, 200))
                if box.wall:
                    box.draw(window, (10, 10, 10))
                if box.ending:
                    box.draw(window, (200, 200, 0))
        pygame.display.update()
main()