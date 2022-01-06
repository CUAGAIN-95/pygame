class Player:
    def __init__(self, screen):
        self.color = (111, 111, 111)
        self.width = 45
        self.height = 60
        self.x_pos = (screen.width / 2) - (self.width / 2)
        self.y_pos = (screen.height / 2) - (self.height / 2)
        self.to_x = 0
        self.to_y = 0
        self.speed = 0.5

    def __del__(self):
        pass

    def move(self, screen, dt):
        self.x_pos += self.to_x * dt
        self.y_pos += self.to_y * dt

        if self.x_pos < 0:
            self.x_pos = 0
        elif self.x_pos > screen.width - self.width:
            self.x_pos = screen.width - self.width
        if self.y_pos < 0:
            self.y_pos = 0
        elif self.y_pos > screen.height - self.height:
            self.y_pos = screen.height - self.height


