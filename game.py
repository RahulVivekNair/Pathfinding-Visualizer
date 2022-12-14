from tkinter import messagebox, Tk
import pygame
import sys

window_width = 600
window_height = 600
columns=30
rows=30

window = pygame.display.set_mode((window_width, window_height))

box_width= window_width // columns
box_height= window_height // rows

grid=[]
queue=[]
path=[]
class Box:
    def __init__(self,i,j):
        self.x=i
        self.y=j
        self.wall=False
        self.starting=False
        self.ending=False
        self.queued=False
        self.visited=False
        self.prior=None
        self.neighbours=[]

    def draw(self,win,color):
        pygame.draw.rect(win,color,(self.x*box_width,self.y*box_height,box_width,box_height))

    def set_neighbours(self):
        if self.x > 0:
            self.neighbours.append(grid[self.x - 1][self.y])
        if self.x < columns - 1:
            self.neighbours.append(grid[self.x + 1][self.y])
        if self.y > 0:
            self.neighbours.append(grid[self.x][self.y - 1])
        if self.y < rows - 1:
            self.neighbours.append(grid[self.x][self.y + 1])


for i in range(rows):
    arr = []
    for j in range(columns):
        arr.append(Box(i, j))
    grid.append(arr)

for i in range(rows):
    for j in range(columns):
        grid[i][j].set_neighbours()



def main():
    begin_search = False
    target_box_set = False
    start_box_set = False
    searching = True
    target_box = None
    start_box = None
    c=1
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
                    queue.append(start_box)
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
                
            #if event.type == pygame.KEYDOWN and target_box_set and start_box_set:
                #begin_search = True
            if event.type == pygame.KEYDOWN:
                # If the user presses the enter button the algorithm will start
                if event.key == pygame.K_SPACE and target_box_set and start_box_set:
                    begin_search = True

        if begin_search and c==1:
            if len(queue) > 0 and searching:
                current_box = queue.pop(0)
                current_box.visited = True
                if current_box == target_box:
                    searching = False
                    while current_box.prior != start_box:
                        path.append(current_box.prior)
                        current_box = current_box.prior
                else:
                    for neighbour in current_box.neighbours:
                        if not neighbour.queued and not neighbour.wall:
                            neighbour.queued = True
                            neighbour.prior = current_box
                            queue.append(neighbour)
            else:
                if searching:
                    Tk().wm_withdraw()
                    messagebox.showinfo("No Solution", "There is no solution!")
                    searching = False
        if begin_search and c==2:
             pass

        window.fill((0,0,0))
        for i in range(rows):
            for j in range(columns):
                box = grid[i][j]
                box.draw(window, (75, 75, 75))
                
                if box.queued:
                    box.draw(window, (200, 0, 0))
                if box.visited:
                    box.draw(window, (0, 200, 0))
                if box in path:
                    box.draw(window, (128, 0, 128))
                if box.starting:
                    box.draw(window, (0, 200, 200))
                if box.wall:
                    box.draw(window, (10, 10, 10))
                if box.ending:
                    box.draw(window, (200, 200, 0))
        gap = window_width // rows
    # Making the horizontal gridlines
        for row in range(1,rows):
            pygame.draw.line(window, (0,0,0), (0, row * gap), (window_width, row * gap))
        # Making the vertical gridlines
            for col in range(1,columns):
                pygame.draw.line(window, (0,0,0), (col * gap, 0), (col * gap, window_width))
        pygame.display.update()
    
main()