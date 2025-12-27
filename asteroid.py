from constants import *
import random
import pygame
from circleshape import CircleShape
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        # Talimata göre: surface, color, center, radius, width
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        # Hız vektörü ile zamanı çarpıp pozisyona ekliyoruz
        self.position += self.velocity * dt
    def split(self):
        self.kill() # Bu asteroid her halükarda yok olur

        # Eğer zaten en küçük boyuttaysa, bölünmez (direkt yok olur)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # Orta veya büyük boyuttaysa:
        log_event("asteroid_split")
        
        # 20 ile 50 derece arasında rastgele bir açı seç
        random_angle = random.uniform(20, 50)

        # Mevcut hız vektörünü bu açılarla döndürerek yeni yönler belirle
        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        # Yeni yarıçapı hesapla (Eskisinden bir boy küçük)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Yeni asteroidleri yarat (Tam olarak eski asteroidin olduğu yerde)
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = a * 1.2  # Biraz daha hızlandır
        
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = b * 1.2  # Biraz daha hızlandır
