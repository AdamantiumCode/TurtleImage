import os
import sys
import turtle as t

from PIL import Image


def get_pixels(image_path: str) -> list | None:
    if not os.path.isfile(image_path):
        print(
            f"No such file or directory: '{image_path}'"
            "\nPlease indicate the correct path"
        )
        return
    
    image = Image.open(image_path)
    image = image.convert('RGB')
    width, height = image.size
    
    pixels = list(image.getdata())
    
    return [
        pixels[i * width : (i + 1) * width]
        for i in range(height)
    ]


def draw_pixel(color: tuple, pixel_size: int) -> None:
    t.pencolor(*color)
    t.fillcolor(*color)
    t.begin_fill()
    for _ in range(4):
        t.left(90)
        t.forward(pixel_size)
    t.end_fill()
    
    t.up()
    t.forward(pixel_size)
    t.down()


if __name__ == "__main__":
    # Variables to change
    image_path = "./Code/image.png"
    pixel_size = 10
    drawing_speed = "fastest"
    
    # Get pixels
    pixels = get_pixels(image_path)
    if pixels is None:
        sys.exit()
    
    # Start drawing
    #t.hideturtle()
    t.title("Create by AdamantiumCode")
    t.colormode(255)
    t.speed(drawing_speed)
    
    start_cord = [-200, 300]
    
    for row in pixels:
        t.up()
        t.goto(start_cord)
        t.down()
        for pixel in row:
            draw_pixel(pixel, pixel_size)
            
        start_cord[1] -= pixel_size
    
    t.done()
