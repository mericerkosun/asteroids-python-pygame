import pygame
from constants import *
from logger import log_state  # 1. Adım: log_state fonksiyonunu içe aktardık

def main():
    pygame.init() # 2. Adım: Pygame'i başlattık
    
    # 3. Adım: Ekran genişliği ve yüksekliğini ayarladık (pencere oluşturduk)
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    # 4. Adım: Sonsuz oyun döngüsü (Game Loop)
    while True:
        # 5. Adım: Otomatik kontrol için log alıyoruz
        log_state()
        
        for event in pygame.event.get():
    	    if event.type == pygame.QUIT:
                return
        # 6. Adım: Ekranı siyaha boyuyoruz
        screen.fill("black")
        
        # 7. Adım: Ekranı yeniliyoruz (Bunu her zaman en son yapın!)
        pygame.display.flip()

if __name__ == "__main__":
    main()
