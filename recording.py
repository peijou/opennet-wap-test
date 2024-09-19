import pyautogui
import imageio
import numpy as np
import time

# Parameters for screen capture
duration = 100  # seconds to record
fps = 10  # frames per second
region = (0, 0, 1800, 1000)  # (left, top, width, height)

frames = []
start_time = time.time()

# Capture the screen and store frames
while time.time() - start_time < duration:
    screenshot = pyautogui.screenshot(region=region)
    frame = np.array(screenshot)  # Convert the screenshot to a NumPy array
    frames.append(frame)

    time.sleep(1 / fps)

# Save the frames as a GIF using imageio
imageio.mimsave('opennet-wap-testing.gif', frames, fps=fps)
