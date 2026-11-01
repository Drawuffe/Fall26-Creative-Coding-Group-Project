# Function definition for person 2 here
def draw_dafu_tile(t, x, y, size, rotation, palette, tile_type="center"):
  """
  Draws a parameterized geometric tile centered at (x, y).

  Parameters:
  - t: Turtle object
  - x, y (float/int): Center coordinates of the tile
  - size (float/int): Width and height of the tile bounding box
  - rotation (int): Orientation angle (0, 90, 180, 270)
  - palette (dict): RGB tuples with keys 'bg', 'primary', 'secondary', 'accent'
  - tile_type (str): "center", "border", or "corner" (defaults to "center")
  """

  # ==========================================
  # TURTLE SETUP
  # ==========================================
  t.penup()
  t.jumpto(x, y)
  t.setheading(rotation)

  # Useful relative dimension constants (derived from size)
  half = size / 2
  quarter = size / 4

  # ==========================================
  # BASE BACKGROUND
  # All tile variations share a clean backdrop
  # ==========================================
  # Move to the bottom-left corner relative to orientation
  t.forward(-half)
  t.left(90)
  t.forward(-half)
  t.right(90)

  t.pencolor(palette["bg"])
  t.fillcolor(palette["bg"])
  t.pensize(2)
  t.pendown()
  t.begin_fill()
  for _ in range(4):
      t.forward(size)
      t.left(90)
  t.end_fill()
  t.penup()

  # Return turtle to the true center of the tile
  t.jumpto(x, y)
  t.setheading(rotation)

  ######################### YOUR CHANGES START HERE ###########################

  # ==========================================
  # CONDITIONAL GEOMETRY (Based on tile_type)
  # ==========================================

  # ------------------------------------------
  # OPTION 1: CORNER TILE
  # ------------------------------------------
  if tile_type == "corner":

    ############## This part is my own drawing #######################
    ################## Change it to your design ######################
      t.pencolor(palette["accent"])
      t.pensize(1)
      t.setheading(rotation)

      t.pendown()
      t.forward(half)
      t.right(90)
      t.forward(half)
      t.penup()

      t.goto(x, y)
      t.setheading(rotation)
      t.forward(10)
      t.right(45)

      t.pendown()
      t.forward(half)
      t.penup()
      t.goto(x, y)
      t.setheading(rotation)
      t.color(palette["primary"], palette["primary"])
      t.forward(quarter)
      t.left(90)
      t.pendown()
      t.begin_fill()
      t.circle(quarter, 90)
      t.goto(x, y)
      t.end_fill()
      t.penup()
      t.goto(x, y)
      t.color(palette["secondary"])
      t.dot(quarter/3)

  # ------------------------------------------
  # OPTION 2: BORDER TILE
  # ------------------------------------------
  elif tile_type == "border":
    ############## This part is my own drawing #######################
    ################## Change it to your design ######################

    t.color(palette["primary"], palette["primary"])
    t.forward(-half * 0.8)
    t.left(90)
    t.forward(quarter * 0.8)
    t.right(90)

    t.pendown()
    t.begin_fill()
    for _ in range(2):
        t.forward(size * 0.8)
        t.left(90)
        t.forward(quarter * 0.6)
        t.left(90)
    t.end_fill()
    t.penup()

    t.jumpto(x, y)
    t.setheading(rotation)
    t.pencolor(palette["accent"])
    t.pensize(2)
    t.forward(-half * 0.8)
    t.pendown()
    t.forward(size * 0.8)
    t.penup()

  # ------------------------------------------
  # OPTION 3: CENTER TILE
  # ------------------------------------------
  else:

    ############## This part is my own drawing #######################
    ################## Change it to your design ######################

      t.pencolor(palette["secondary"])
      t.jumpto(x, y)
      t.setheading(rotation + 30)
      t.forward(quarter * 0.5)
      t.left(60)
      t.forward(quarter * 0.5)
      t.pendown()
      for i in range(6):
          t.left(60)
          t.forward(half * 0.6)
      t.left(30)
      t.penup()

      t.forward(half * 0.3)

      t.color(palette["accent"])
      t.pendown()
      for i in range(6):
          t.left(60)
          t.forward(half * 0.15)
      t.penup()

      t.color(palette["primary"], palette["primary"])
      t.setheading(rotation + 30)
      for i in range(6):
          t.jumpto(x, y)
          t.pendown()
          t.begin_fill()
          for j in range(3):
              t.forward(quarter * 0.9)
              t.left(120)
          t.end_fill()
          t.penup()
          t.left(60)
      t.jumpto(x, y)
      t.setheading(rotation)
      t.pencolor(palette["accent"])
      t.pensize(2)

      for _ in range(12):
          t.pendown()
          t.forward(quarter * 0.5)
          t.penup()
          t.jumpto(x, y)
          t.right(30)



  # ==========================================
  # DRAW BORDER (OPTIONAL IF YOU WANT A BORDER)
  # ==========================================

  ############## This part is my own drawing #######################
  ################## Change it to your design ######################
  t.pencolor(palette["secondary"])
  t.pensize(2)

  # Go to the corner
  t.penup()
  t.jumpto(x, y)
  t.setheading(rotation)
  t.forward(-half)
  t.left(90)
  t.forward(-half)
  t.right(90)

  # Draw the border
  t.pendown()
  for _ in range(4):
      t.forward(size)
      t.left(90)
  t.penup()

  ######################### YOUR CHANGES END HERE #############################

  # ==========================================
  # TURTLE TEARDOWN
  # Reset pen, heading, and state for the next user
  # ==========================================
  t.penup()
  t.setheading(0)
  t.pencolor((0, 0, 0))