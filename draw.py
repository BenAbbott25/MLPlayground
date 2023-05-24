import cv2
import numpy as np
import csv


def drawNumber():
    # Set the dimensions of the canvas
    canvas_size = 560
    pixel_size = 20

    # Create a black canvas
    canvas = np.zeros((canvas_size, canvas_size), dtype=np.uint8)

    # Create a window to display the canvas
    cv2.namedWindow("Drawing Canvas")

    # Create a flag to track mouse button state
    drawing = False

    # Mouse callback function
    def draw_pixel(event, x, y, flags, param):
        global drawing

        if event == cv2.EVENT_LBUTTONDOWN:
            drawing = True
        elif event == cv2.EVENT_LBUTTONUP:
            drawing = False
        elif event == cv2.EVENT_MOUSEMOVE:
            if drawing:
                # Calculate the pixel coordinates
                pixel_x = x // pixel_size
                pixel_y = y // pixel_size

                # Draw a white pixel on the canvas
                cv2.rectangle(canvas, (pixel_x * pixel_size, pixel_y * pixel_size),
                            ((pixel_x + 1) * pixel_size, (pixel_y + 1) * pixel_size),
                            (255), -1)

    # Set the callback function for mouse events
    cv2.setMouseCallback("Drawing Canvas", draw_pixel)

    while True:
        # Display the canvas
        cv2.imshow("Drawing Canvas", canvas)

        # Wait for a key press
        key = cv2.waitKey(1) & 0xFF

        # Quit if 'q' is pressed
        if key == ord("q"):
            break
        # Clear the canvas if 'c' is pressed
        elif key == ord("c"):
            canvas.fill(0)

    # Resize the canvas to 28x28
    resized_canvas = cv2.resize(canvas, (28, 28), interpolation=cv2.INTER_AREA)

    # Convert the canvas to a flattened array
    draw_array = resized_canvas.flatten()

    # Print the resulting data array
    print(draw_array)

    # Close the window
    cv2.destroyAllWindows()

    return draw_array
