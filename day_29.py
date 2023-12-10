def print_in_color(word, color):
    color_codes = {
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "reset": "\033[0m"
    }

    if color in color_codes:
        print(color_codes[color], word, sep="", end="")
    else:
        print(word, end="")

    # Resetting the color to default after printing
    print(color_codes["reset"], end="")

# Example usage
print("Super Subroutine ", end="")
print_in_color("with ", "red")
print_in_color("my", "green")
