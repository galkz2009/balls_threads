import random
import pygame
import threading
import time

num_of_balls = int(input("Enter the number of balls: "))


class ball(threading.Thread):
     
        def __init__(self, threadID, color, num_of_moves):
            """
            Initialize a ball thread.
            :param threadID: the ID of the thread
            :param color: the color of the ball
            :param num_of_moves: the number of moves the ball will make
            :return: None
            """
            threading.Thread.__init__(self) 
            self.radius = random.randint(10, 50)
            self.position = (random.randint(self.radius, 800-self.radius), random.randint(self.radius, 600-self.radius))
            self.color = color
            self.num_of_moves = num_of_moves
            self.current_move = 0
            self.next_move = 0
            self.threadID = threadID   

        def run(self):
              """
              Run the ball thread.
              :return: None
            """
              print (f"starting – {self.threadID}")
              while self.current_move < self.num_of_moves:
                    if self.current_move != self.next_move:   
                        self.change_position()
                        self.current_move = self.next_move
                    time.sleep(0.1)
              print (f"exiting – {self.threadID}")


        def increment_move(self):
            """
            Increment the next move counter.
            :return: None
            """
            self.next_move += 1

        def change_position(self):
            """
            Change the position of the ball to a new random location.
            :return: None
            """
            self.position = (random.randint(self.radius, 800-self.radius), random.randint(self.radius, 600-self.radius))


pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Bouncing Balls")   

list_of_balls = []
for i in range(num_of_balls):
    thread = ball(i+1, (random.randint(0,255), random.randint(0,255), random.randint(0,255)), random.randint(2, 10))
    list_of_balls.append(thread)
    thread.start()



running = True
        
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for thread in list_of_balls:
        # only erase the ball if it has moved at least once
        if thread.current_move > 0:
             pygame.draw.circle(screen, (0,0,0), thread.position, thread.radius)
             pygame.display.flip()
        # draw the ball at its new position
        thread.increment_move()
        time.sleep(0.3)
        pygame.draw.circle(screen, thread.color, thread.position, thread.radius)
        # erase the ball if the thread has finished running
        if not thread.is_alive():
             pygame.draw.circle(screen, (0,0,0), thread.position, thread.radius)
             pygame.display.flip()             
             list_of_balls.remove(thread)
        pygame.display.set_caption(f'Test caption - {len(list_of_balls)} balls remaining')
        if len(list_of_balls) == 0:
            running = False
        pygame.display.flip()



        






pygame.quit()


