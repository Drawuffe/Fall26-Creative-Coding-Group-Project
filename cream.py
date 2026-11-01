# Function definition for person 3 here
def draw_cream_tile(t, x, y, size, rotation, palette, tile_type="center"):
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
    t.pencolor(palette["secondary"])
    t.pensize(3)

    for i in range(3):
        t.penup()
        t.jumpto(x, y)
        t.setheading(rotation)
        t.forward(-half + i * 12)
        t.left(90)
        t.forward(-half + i * 12)

        t.pendown()
        t.forward(size - i * 24)
        t.backward(size - i * 24)
        t.right(90)
        t.forward(size - i * 24)

    t.penup()
  # ------------------------------------------
  # OPTION 2: BORDER TILE
  # ------------------------------------------
  elif tile_type == "border":

    ############## This part is my own drawing #######################
    ################## Change it to your design ######################
    t.pencolor(palette["primary"])
    t.pensize(3)

    t.penup()
    t.jumpto(x, y)
    t.setheading(rotation)
    t.forward(-half)
    t.left(90)
    t.forward(quarter / 3)
    t.right(90)

    t.pendown()
    t.forward(size)
    t.penup()

    t.pencolor(palette["accent"])
    t.pensize(2)

    t.jumpto(x, y)
    t.setheading(rotation)
    t.forward(-half)
    t.left(90)
    t.forward(-quarter / 8)
    t.right(90)

    t.pendown()
    t.forward(size)
    t.penup()

    t.fillcolor(palette["secondary"])
    t.pencolor(palette["secondary"])

    t.jumpto(x, y)
    t.setheading(rotation)
    t.forward(-half)
    t.left(90)
    t.forward(-half)
    t.right(90)

    t.pendown()
    t.begin_fill()
    for i in range(2):
        t.forward(size)
        t.left(90)
        t.forward(quarter * 1.3)
        t.left(90)
    t.end_fill()
    t.penup()

  # ------------------------------------------
  # OPTION 3: CENTER TILE
  # ------------------------------------------
  else:

    ############## This part is my own drawing #######################
    ################## Change it to your design ######################
    t.color(palette["primary"])
    t.penup()
    t.jumpto(x, y - quarter)
    t.setheading(45)

    t.pendown()
    t.begin_fill()
    for i in range(4):
        t.forward(quarter * 1.4)
        t.left(90)
    t.end_fill()
    t.penup()

    t.color(palette["accent"])

    for i in range(4):
        t.jumpto(x, y)
        t.setheading(i * 90)
        t.forward(quarter)

        t.pendown()
        t.begin_fill()
        t.forward(quarter)
        t.left(135)
        t.forward(quarter * 1.4)
        t.end_fill()
        t.penup()

    t.color(palette["secondary"])

    if rotation == 0:
          dot_x = x - quarter * 0.9
          dot_y = y - quarter * 0.2
    elif rotation == 90:
          dot_x = x
          dot_y = y - quarter * 0.9
    elif rotation == 180:
          dot_x = x + quarter * 0.9
          dot_y = y + quarter * 0.2
    else:
          dot_x = x
          dot_y = y + quarter * 0.9

    t.penup()
    t.jumpto(dot_x, dot_y)
    t.dot(quarter * 0.35)
  #=====================
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