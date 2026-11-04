# [Generative Poster Group project]

![Example final poster](example_poster.svg)

**Created by:** Adamya, Dafu, Cream, and Emily  
**Course:** Creative Coding, Pratt Institute  
**Semester:** Fall 2026

## About the Project

[Write a short description of your project. What was the idea behind your poster generator? What visual qualities or design ideas inspired it? How does the program combine everyone's individual tile designs into a unified composition?]

## The Interface

The user can input their title for the poster, the scale of the poster through tiles, and the color palette they want for their poster.

## Meet the Designers

- **Cream:** [Brief description of their tile designs or contribution.]
- **Emily:** [Brief description of their tile designs or contribution.]
- **Adamya:** [Brief description of their tile designs or contribution.]
- **Dafu:** [Brief description of their tile designs or contribution.]

## Try it yourself

Copy this code into a Colab Notebook.

```python
!git clone https://github.com/Drawuffe/Fall26-Creative-Coding-Group-Project.git
%cd Fall26-Creative-Coding-Group-Project
!pip install -r requirments.txt
from project import Create_Poster
Create_Poster()
```

Or click below to open an example notebook in Google Colab and generate your own poster!

[![Open In Colab]([https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1zNzpmjo-DxmOubNH1tTY58AlxK4rNTaZ?usp=sharing)

### How to Use

1. Open the notebook in Google Colab.
2. Run the setup cells to download the project code and install the required libraries.
3. Run the cell that calls the function and prompts the user to choose a title, grid dimensions, and color palette.
4. Your own poster will be saved as poster.svg!

## Files

- `project.py` – Main poster-generation program.
- `emily.py` – Collection of Emily's custom tile-drawing functions.
- `cream.py` – Collection of Cream's custom tile-drawing functions.
- `adamya.py` – Collection of Adamya's custom tile-drawing functions.
- `dafu.py` – Collection of Dafu's custom tile-drawing functions.
- `palette.py` – Available color palettes.
- `requirements.txt` – Required Python libraries.
- `example_poster.svg` – Scalable vector version of an example final poster image.
