# Sorting soda cans - for technical interview
# Sorting cans of Bubly seltzer water by color
import sensor, image, time

# Color Tracking Thresholds (L Min, L Max, A Min, A Max, B Min, B Max)
# The below thresholds track in general red/green things. You may wish to tune them...
thresholds = [(30, 100, 15, 127, 15, 127), # generic_red_thresholds -> index is 0 so code == (1 << 0)
              (30, 100, -64, -8, -32, 32), # generic_green_thresholds -> index is 1 so code == (1 << 1)
              (0, 15, 0, 40, -80, -20)] # generic_blue_thresholds -> index is 2 so code == (1 << 2)
# Codes are or'ed together when "merge=True" for "find_blobs".

sensor.reset()
sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.skip_frames(time = 2000)
sensor.set_auto_gain(False) # must be turned off for color tracking
sensor.set_auto_whitebal(False) # must be turned off for color tracking
clock = time.clock()

# Only blobs that with more pixels than "pixel_threshold" and more area than "area_threshold" are
# returned by "find_blobs" below. Change "pixels_threshold" and "area_threshold" if you change the
# camera resolution. "merge=True" must be set to merge overlapping color blobs for color codes.

while(True):
    clock.tick()
    img = sensor.snapshot()
    for blob in img.find_blobs(thresholds, pixels_threshold=200, area_threshold=200, merge=False):
        if blob.code() == 1: # red code
            img.draw_rectangle(blob.rect())
            img.draw_cross(blob.cx(), blob.cy())
            img.draw_string(blob.x() + 2, blob.y() + 2, "red")
        if blob.code() == 2: # green code
            img.draw_rectangle(blob.rect())
            img.draw_cross(blob.cx(), blob.cy())
            img.draw_string(blob.x() + 2, blob.y() + 2, "green")
    print(clock.fps())
