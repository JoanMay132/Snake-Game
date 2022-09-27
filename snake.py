from re import X


from turtle import Turtle, Screen
X=0
MOVE_DISTANCE=20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
 
class Snake:    

    def __init__(self):
        self.body_snakes=[]
        self.create_snake() #method
       
        self.head = self.body_snakes[0]
    def create_snake(self):
        
        for distance in range(1,4):
            self.add_segment(distance)
         

    def add_segment(self, distance):
            new_snake=Turtle(shape="square")
            new_snake.color("red")
            new_snake.penup()
            new_snake.setx(X)
            x=X+20
            self.body_snakes.append(new_snake) #refering to our atrribute body_snakes 
    def extend(self):
        # add a new segment to the snake   
        self.add_segment(self.body_snakes[-1].position())
    def move_snake(self):
        for seg_num in range(len(self.body_snakes)-1,0 , -1):
            new_x=self.body_snakes[seg_num-1].xcor()
            new_y=self.body_snakes[seg_num-1].ycor()
            self.body_snakes[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)
        #self.head.left(90)

    def up(self):
        if self.head.heading() !=DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() !=UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() !=RIGHT:
         self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
