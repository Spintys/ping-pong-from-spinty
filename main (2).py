class gamesprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.y = player_y 
        self.rect.x = player_x 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(gamesprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5: 
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < min_width - 80:
            self.rect.x += self.speed
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 1, 20, -10)
        bullets.add(bullet)