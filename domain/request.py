import math


class Request:
    LAT_STEP = 0.007
    LON_STEP = 0.02

    def __init__(self):
        self.longitude = 37.530887
        self.latitude = 55.703118
        self.zoom = 15
        self.l = 'map'

    def get_longitude(self):
        return self.longitude

    def get_latitude(self):
        return self.latitude

    def get_zoom(self):
        return self.zoom

    def get_l(self):
        return self.l

    def up_zoom(self):
        self.zoom += 1
        if self.zoom > 15:
            self.zoom = 15

    def down_zoom(self):
        self.zoom -= 1
        if self.zoom < 0:
            self.zoom = 0

    def left(self):
        self.longitude -= self.LON_STEP * math.pow(2, 15 - self.zoom)

    def right(self):
        self.longitude += self.LON_STEP * math.pow(2, 15 - self.zoom)

    def up(self):
        self.latitude += self.LAT_STEP * math.pow(2, 15 - self.zoom)

    def down(self):
        self.latitude -= self.LAT_STEP * math.pow(2, 15 - self.zoom)