# Function definition for person 1 here
def draw_adamya_tile(t, x, y, size, rotation, palette, tile_type="center"):
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
  # ==========================================
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

  # ==========================================
  # CONDITIONAL GEOMETRY
  # ==========================================

  # ------------------------------------------
  # CORNER TILE: nested diamonds
  # ------------------------------------------
  if tile_type == "corner":
      radius = quarter * 0.9

      # Large primary diamond
      t.jumpto(x, y)
      t.setheading(rotation)
      t.forward(radius)
      t.left(90)
      t.pencolor(palette["primary"])
      t.fillcolor(palette["primary"])
      t.pendown()
      t.begin_fill()
      for _ in range(4):
          t.forward(radius)
          t.left(90)
      t.end_fill()
      t.penup()

      # Smaller secondary diamond
      radius = quarter * 0.45
      t.jumpto(x, y)
      t.setheading(rotation)
      t.forward(radius)
      t.left(90)
      t.pencolor(palette["secondary"])
      t.fillcolor(palette["secondary"])
      t.pendown()
      t.begin_fill()
      for _ in range(4):
          t.forward(radius)
          t.left(90)
      t.end_fill()
      t.penup()

      # Accent center
      t.jumpto(x, y)
      t.dot(quarter * 0.28, palette["accent"])

  # ------------------------------------------
  # BORDER TILE: row of three diamonds
  # ------------------------------------------
  elif tile_type == "border":
      radius = quarter * 0.38

      for offset in (-quarter, 0, quarter):
          t.jumpto(x, y)
          t.setheading(rotation)
          t.forward(offset)
          t.setheading(rotation)

          # Draw a primary diamond
          t.forward(radius)
          t.left(90)
          t.pencolor(palette["primary"])
          t.fillcolor(palette["primary"])
          t.pendown()
          t.begin_fill()
          for _ in range(4):
              t.forward(radius)
              t.left(90)
          t.end_fill()
          t.penup()

          # Add an accent dot to each diamond
          t.jumpto(x, y)
          t.setheading(rotation)
          t.forward(offset)
          t.dot(quarter * 0.2, palette["accent"])

  # ------------------------------------------
  # CENTER TILE: hexagon with nested dots
  # ------------------------------------------
  else:
      radius = quarter * 0.8

      # Filled primary hexagon
      t.jumpto(x, y)
      t.setheading(rotation)
      t.forward(radius)
      t.setheading(rotation + 120)
      t.pencolor(palette["primary"])
      t.fillcolor(palette["primary"])
      t.pendown()
      t.begin_fill()
      for _ in range(6):
          t.forward(radius)
          t.left(60)
      t.end_fill()
      t.penup()

      # Secondary and accent center dots
      t.jumpto(x, y)
      t.dot(quarter * 0.62, palette["secondary"])
      t.dot(quarter * 0.24, palette["accent"])

  # ==========================================
  # TILE BORDER
  # ==========================================
  t.pencolor(palette["secondary"])
  t.pensize(2)

  t.penup()
  t.jumpto(x, y)
  t.setheading(rotation)
  t.forward(-half)
  t.left(90)
  t.forward(-half)
  t.right(90)

  t.pendown()
  for _ in range(4):
      t.forward(size)
      t.left(90)
  t.penup()

  # ==========================================
  # TURTLE TEARDOWN
  # ==========================================
  t.penup()
  t.setheading(0)
  t.pencolor((0, 0, 0))