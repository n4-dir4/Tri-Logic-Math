import pygame
import sys

# Dimensi layar
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768


class Menu:
    def __init__(self, items, font_color=(0, 0, 0), select_color=(255, 0, 0), ttf_font=None, font_size=40):
        # Warna teks
        self.font_color = font_color
        self.select_color = select_color
        self.items = items

        # Font untuk teks menu
        self.font = pygame.font.Font(ttf_font, font_size)

        # Gambar background
        self.background_image = pygame.image.load("background.jpg").convert()
        self.background_image = pygame.transform.scale(self.background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # Daftar rect untuk elemen menu
        self.rect_list = self.get_rect_list(items)

        # Tombol "Exit" di bawah layar
        self.close_button_rect = pygame.Rect(
            (SCREEN_WIDTH // 2) - 50,  # Di tengah layar secara horizontal
            SCREEN_HEIGHT - 60,       # Margin 60px dari bawah
            100,                      # Lebar tombol
            40                        # Tinggi tombol
        )

        self.state = -1  # Status hover (-1 artinya tidak ada elemen yang dihover)

    def get_rect_list(self, items):
        """Hitung posisi setiap elemen menu dan buat rect"""
        rect_list = []
        logo_offset = 80  # Tambahkan ruang untuk logo di atas
        padding = 60      # Jarak antar elemen menu

        for index, item in enumerate(items):
            size = self.font.size(item)
            width, height = size[0], size[1]

            # Hitung posisi X dan Y
            posX = (SCREEN_WIDTH // 2) - (width // 2)
            t_h = len(items) * (height + padding)
            posY = (SCREEN_HEIGHT // 2) - (t_h // 2) + logo_offset + (index * (height + padding))

            # Buat rect berdasarkan posisi
            rect = pygame.Rect(posX, posY, width, height)
            rect_list.append(rect)

        return rect_list

    def collide_points(self):
        """Deteksi mouse pada elemen menu"""
        index = -1
        mouse_pos = pygame.mouse.get_pos()
        for i, rect in enumerate(self.rect_list):
            if rect.collidepoint(mouse_pos):
                index = i
        return index

    def update(self):
        """Perbarui state hover berdasarkan posisi mouse"""
        self.state = self.collide_points()

    def process_events(self, event):
        """Proses event yang diteruskan dari game.py"""

        if event.type == pygame.QUIT:
            print("QUIT event detected in menu.py")  # Debugging
            return True  # Sinyal untuk keluar

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.close_button_rect.collidepoint(mouse_pos):
                return True  # Sinyal untuk keluar

        return False  # Tidak ada permintaan keluar



    def display_frame(self, screen):
        """Gambar elemen menu di layar"""
        # Gambar background
        screen.blit(self.background_image, (0, 0))

        # Gambar logo
        logo_label = self.font.render("TriLogicMath", True, self.font_color)
        logo_width = logo_label.get_width()
        screen.blit(logo_label, ((SCREEN_WIDTH // 2) - (logo_width // 2), 20))  # Logo di atas

        # Gambar elemen menu
        logo_offset = 80
        for index, item in enumerate(self.items):
            if self.state == index:
                label = self.font.render(item, True, self.select_color)
            else:
                label = self.font.render(item, True, self.font_color)

            # Ukuran teks
            width = label.get_width()
            height = label.get_height()

            # Posisi di tengah layar dengan offset logo
            posX = (SCREEN_WIDTH // 2) - (width // 2)
            t_h = len(self.items) * (height + 60)  # Padding antar elemen
            posY = (SCREEN_HEIGHT // 2) - (t_h // 2) + logo_offset + (index * (height + 60))

            screen.blit(label, (posX, posY))

        # Gambar tombol Exit di bawah layar
        if self.close_button_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (255, 0, 0), self.close_button_rect)  # Warna merah saat hover
        else:
            pygame.draw.rect(screen, (255, 255, 255), self.close_button_rect)  # Warna putih biasa
        pygame.draw.rect(screen, (0, 0, 0), self.close_button_rect, 2)  # Garis tepi hitam

        close_label = self.font.render("Exit", True, (0, 0, 0))
        screen.blit(
            close_label,
            (self.close_button_rect.x + (self.close_button_rect.width - close_label.get_width()) // 2,
             self.close_button_rect.y + (self.close_button_rect.height - close_label.get_height()) // 2)
        )
