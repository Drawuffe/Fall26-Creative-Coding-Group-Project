from ColabTurtlePlus.Turtle import *
import numpy as np
  
from emily import draw_emily_tile
from cream import draw_cream_tile
from adamya import draw_adamya_tile
from dafu import draw_dafu_tile
from palette import palette_options, palette_names

def Create_Poster():
  

  tile_functions = [draw_adamya_tile, draw_dafu_tile, draw_cream_tile, draw_emily_tile]
  Title_text = input("Enter a title for your poster: ")

  nrows = int(input("Grid height: "))
  while nrows < 3 or nrows > 8:
    print("Should be between 3 and 8.")
    nrows = int(input("Grid height: "))

  ncols = int(input("Grid width: "))
  while ncols < 3 or ncols > 8:
    print("Should be between 3 and 8.")
    ncols = int(input("Grid width: "))

  p_name = input("Enter the name of the color palette you wish to use: ").lower()

  while p_name not in palette_names:
    print(f"Invalid palette name. The valid names are {palette_names}.")
    p_name = input("Enter the name of the color palette you wish to use: ").lower()

  print(f"You have selected the {p_name} palette.")

  print("Ready to create poster...")

  clearscreen()
  setup(550, 850)
  t = Turtle()
  t.speed(0)

  #draw boarder
  t.penup()
  t.jumpto(-250, 400)
  t.setheading(0)
  t.pencolor("black")
  t.pensize(1)
  t.pendown()

  for i in range(2):
    t.forward(500)
    t.right(90)
    t.forward(800)
    t.right(90)

  t.penup()


  size = 50
  y_offset = (nrows - 1) * size / 2
  x_offset = -(ncols - 1) * size / 2


  for row in range(nrows):
    y = y_offset - size * row

    for col in range(ncols):
      x = x_offset + size * col

      # Randomly choose which person's tile to draw
      F = tile_functions[np.random.randint(len(tile_functions))]

      # Corner tiles
      if row == 0 and col == 0:
        tile_type = 'corner'
        rotation = 0
      elif row == nrows-1 and col == 0:
        tile_type = 'corner'
        rotation = 90
      elif row == nrows-1 and col == ncols-1:
        tile_type = 'corner'
        rotation = 180
      elif row == 0 and col == ncols-1:
        tile_type = 'corner'
        rotation =270

      #Boder tiles
      elif row == 0 or row == nrows-1:
        tile_type = 'border'
        rotation = 0
      elif col == 0 or col == ncols-1:
        tile_type = 'border'
        rotation = 90

    #Center tiles
      else:
        tile_type = 'center'

      F(t, x, y, size, rotation, palette, tile_type)

  # Write the title and credits
  t.jumpto(0, 300)
  t.write(Title_text, align="center", font=(36, "Arial", "bold"))
  t.setheading(270)
  t.jumpto(0, -250)
  t.write("By Adamya, Dafu, Cream and Emily", align="center", font=(12, "Arial", "bold"))

  # Draw the color palette colors
  t.jumpto(-180, -350)
  for v in palette.values():
    t.color(v, v)
    t.setheading(90)
    t.pendown()

    # Draw square
    t.begin_fill()
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.end_fill()

    t.penup()
    t.right(180)
    t.forward(20)
    t.right(90)
    t.forward(20)

    # Write the RGB values
    t.write(v, align="center")
    t.setheading(0)
    t.forward(80)
    t.left(90)
    t.forward(20)

  t.hideturtle()
  t.done()
