# Turtle Image
 Image processing and reproduction using the turtle module in Python

# Python version
 I used python version 3.11.5 

 But you can use any version of Python 3

# How to use?
 1. Install the necessary dependencies using this command - "pip install -r requirements.txt" or its equivalent

 2. Run program

# Your program settings
 In the file "main.py " you can:

 1. Select an image and specify the full or short path to it in "IMAGE_PATH" variable

 2. You can change drawing mode in "DRAWING MODE" variable. A list of all modes and their description can be found below

 3. You can also change pixel size in "PIXEL_SIZE" variable

 4. Variable "DRAWING_SPEED" is responsible for the drawing speed. It can be any natural integer or the string "fastest" for the maximum possible speed

 5. To hide the turtle cursor, specify the appropriate value in the "HIDE_TURTLE" variable

 6. You can also change the "start_position" to shift the point from which the image is drawn

 All variables are located immediately after the line - if \_\_name__ == "\_\_main__"

# Drawing Modes
 1. linear - basic drawing mode. The turtle just moves across the screen leaving lines behind it

 2. pixel - individual pixels immediately appear on the screen

 3. row - as soon as the turtle draws a row of pixels, it immediately appears on the screen

 4. instant - as soon as the turtle finishes drawing the image it will appear on the screen
