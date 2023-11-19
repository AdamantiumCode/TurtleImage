import os
import sys
import turtle as t

from PIL import Image


def get_pixel_grid(image_path: str) -> list | None:
    if not os.path.isfile(image_path):
        print(
            f"No such file: '{image_path}'"
            "\nPlease indicate the correct path"
        )
        return
    
    image = Image.open(image_path)
    
    if image.format not in ('PNG', 'JPG', 'JPEG'):
        print(
            f"File {image_path} is not image"
            "\nPlease select a file of the appropriate format: "
            ".png, .jpg, .jpeg"
        )
        return
    
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


def linear_drawing(pixel_grid, start_position: list, pixel_size: int) -> None:
    for pixel_row in pixel_grid:
        t.up()
        t.goto(start_position)
        t.down()
        
        for pixel in pixel_row:
            draw_pixel(pixel, pixel_size)
        
        start_position[1] -= pixel_size


def pixel_drawing(pixel_grid, start_position: list, pixel_size: int) -> None:
    t.tracer(0, 0)
    
    for pixel_row in pixel_grid:
        t.up()
        t.goto(start_position)
        t.down()
        
        for pixel in pixel_row:
            draw_pixel(pixel, pixel_size)
            t.update()
        
        start_position[1] -= pixel_size


def row_drawing(pixel_grid, start_position: list, pixel_size: int) -> None:
    t.tracer(0, 0)
    
    for pixel_row in pixel_grid:
        t.up()
        t.goto(start_position)
        t.down()
        
        for pixel in pixel_row:
            draw_pixel(pixel, pixel_size)
        
        t.update()
        start_position[1] -= pixel_size
        

def instant_drawing(pixel_grid, start_position: list, pixel_size: int) -> None:
    t.tracer(0, 0)
    
    for pixel_row in pixel_grid:
        t.up()
        t.goto(start_position)
        t.down()
        
        for pixel in pixel_row:
            draw_pixel(pixel, pixel_size)

        start_position[1] -= pixel_size
    
    t.update()


if __name__ == "__main__":
    # Settings to change
    IMAGE_PATH = "./Code/image.png"
    DRAWING_MODE = "pixel"
    PIXEL_SIZE = 15
    DRAWING_SPEED = "fastest"
    HIDE_TURTLE = False
    start_position = [-360, 300]
    
    # Get pixels
    pixel_grid = get_pixel_grid(IMAGE_PATH)
    if pixel_grid is None:
        sys.exit()
    
    # Start drawing
    t.title("Create by AdamantiumCode")
    t.colormode(255)
    t.speed(DRAWING_SPEED)
    
    if HIDE_TURTLE:
        t.hideturtle()
    
    if DRAWING_MODE == "linear":
        linear_drawing(pixel_grid, start_position, PIXEL_SIZE)
    elif DRAWING_MODE == "pixel":
        pixel_drawing(pixel_grid, start_position, PIXEL_SIZE)
    elif DRAWING_MODE == "row":
        row_drawing(pixel_grid, start_position, PIXEL_SIZE)
    elif DRAWING_MODE == "instant":
        instant_drawing(pixel_grid, start_position, PIXEL_SIZE)
    else:
        print(
            "Incorrect drawing mode!\nThis program has only these drawing modes: "
            "linear, pixel, row, instant"
        )
        sys.exit()
    
    t.done()
