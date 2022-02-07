class Request:
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
        if self.zoom > 17:
            self.zoom = 17

    def down_zoom(self):
        self.zoom -= 1
        if self.zoom < 0:
            self.zoom = 0