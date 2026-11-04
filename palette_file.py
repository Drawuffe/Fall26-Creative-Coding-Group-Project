palette_options = {}
#color palette for random
import numpy as np
def random_rgb():
    return (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255))
random_palette = {
    "bg": random_rgb(),
    "primary": random_rgb(),
    "secondary": random_rgb(),
    "accent": random_rgb()
}

for role, color in random_palette.items():
    print(f"{role}: {color}")

palette_options["random"] = random_palette

# Color palette for person 1 here-Adamya
adamya_palette = {
        "bg": (15, 12, 28),
        "primary": (66, 135, 215),
        "secondary": (30, 250, 212),
        "accent": (154, 228, 164)
    }

# Add this line at the end
palette_options["redwine"] = adamya_palette

# Color palette for person 2 here-Dafu
dafu_palette = {
    "bg": (24, 28, 36),
    "primary": (96, 165, 250),
    "secondary": (45, 212, 191),
    "accent": (251, 146, 60)
}

# Add this line at the end
palette_options["dafun"] = dafu_palette

# Color palette for person 3 here-Cream
cream_palette = {
        "bg": (69, 40, 41),
        "primary": (116, 54, 45),
        "secondary": (164, 146, 80),
        "accent": (157, 188, 209)
    }
# Add this line at the end
palette_options["creamy"] = cream_palette

emily_palette = {
    "bg": (0, 38, 66),
    "primary": (132, 0, 50),
    "secondary": (229, 149, 0),
    "accent": (229, 218, 218)
}
palette_options["emily"] = emily_palette

palette_names = list(palette_options)
