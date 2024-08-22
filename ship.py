import pygame

class Ship:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.image = pygame.image.load('game/spaceship.png')
        self.image = pygame.transform.scale(self.image, (60, 48))  # Resize ship image
        self.rect = self.image.get_rect()
        self.screen_rect = ai_game.screen.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

        self.moving_right = False
        self.moving_left = False
        self.speed = ai_game.ship_speed

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.speed

        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)
