from turtle import Turtle

MOVE_DISTANCE = 20
NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180


class Snake:
    def __init__(self):
        self.starting_position = [(0, 0), (-20, 0), (-40, 0)]
        self.segment = []
        self.new_x = 0
        self.new_y = 0
        self.snake()  # call this method only once in during initialization inside the class and create the class object
        self.head = self.segment[0]

    def snake(self):
        for position in self.starting_position:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segment.append(new_segment)

    def extend_segment(self):
        self.add_segment(self.segment[-1].position())  # return the current location at the end of current segment

    def move(self):
        for num in range(len(self.segment) - 1, 0, -1):
            self.new_x = self.segment[num - 1].xcor()  # get the coordinate for the second last section
            self.new_y = self.segment[num - 1].ycor()
            self.segment[num].goto(self.new_x, self.new_y)  # move the last section to that coordinate
        self.head.fd(MOVE_DISTANCE)  # now move the overlapped single section

    def up(self):
        if self.head.heading() != SOUTH:
            self.head.setheading(NORTH)

    def down(self):
        if self.head.heading() != NORTH:
            self.head.setheading(SOUTH)

    def right(self):
        if self.head.heading() != WEST:
            self.head.setheading(EAST)

    def left(self):
        if self.head.heading() != EAST:
            self.head.setheading(WEST)
