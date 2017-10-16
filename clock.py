import turtle
import datetime
import time

def draw_hour(t, hour):
  t.color("blue")
  t.width(3)
  t.right((360/12) * hour)
  t.forward(150)
  t.forward(-150)
  t.setheading(90)

def draw_min(t, min):
  t.color("lightblue")
  t.width(3)
  t.right((360/60) * min)
  t.forward(150)
  t.forward(-150)
  t.setheading(90)

def draw_sec(t, sec):
  t.color("black")
  t.width(1)
  t.right((360/60) * sec)
  t.forward(150)
  t.forward(-150)
  t.setheading(90)

def up_time():
  for i in range(1000):
    global t
    t.reset()
    t.speed(0)
    now = datetime.datetime.time(datetime.datetime.now())
    h = now.hour
    m = now.minute
    s = now.second
    draw_hour(t,h)
    draw_min(t,m)
    draw_sec(t,s)
    time.sleep(1)

def main():
  win = turtle.Screen()
  win.listen()
  win.onkey(up_time, "a")
  win.mainloop()

t = turtle.Turtle()

main()