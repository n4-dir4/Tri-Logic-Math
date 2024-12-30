import pygame, random
from menu import Menu

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Game(object):
    def __init__(self):
        # Create a new font obeject
        self.font = pygame.font.Font(None,65)
        # Create font for the score msg
        self.score_font = pygame.font.Font("kenvector_future.ttf",20)
        # Create a dictionary with keys: num1, num2, result
        # These variables will be used for creating the
        # arithmetic problem
        self.problem = {"num1":0,"num2":0,"result":0}
        # Create a variable that will hold the name of the operation
        self.operation = ""
        self.symbols = self.get_symbols()
        self.button_list = self.get_button_list()
        # Create boolean that will be true when clicked on the mouse button
        # This is because we have to wait some frames to be able to show
        # the rect green or red.
        self.reset_problem = False
        # Create menu
        items = ("Addition","Subtraction","Multiplication","Division")
        self.menu = Menu(items,ttf_font="XpressiveBlack Regular.ttf",font_size=50)
        # True: show menu
        self.show_menu = True
        # create the score counter
        self.score = 0
        # Count the number of problems
        self.count = 0
        # load background image
        self.background_image = pygame.image.load("background.jpg").convert()
        self.background_image = pygame.transform.scale(self.background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        # load sounds effects
        self.sound_1 = pygame.mixer.Sound("item1.ogg")
        self.sound_2 = pygame.mixer.Sound("item2.ogg")
        self.sound_3 = pygame.mixer.Sound("item3.ogg")
        # Play the start sound when the game begins
        self.sound_1.play()

        # Back button
        self.back_button = Button((SCREEN_WIDTH // 2) - 50, 10, 100, 40, "Back", font_size=30)

    def get_button_list(self):
        """ Return a list with four buttons """
        button_list = []
        # assign one of the buttons with the right answer
        choice = random.randint(1,4)
        # define the width and height
        width = 100
        height = 100
        # t_w: total width
        t_w = width * 2 + 50
        posX = (SCREEN_WIDTH / 2) - (t_w /2)
        posY = 400  # Adjusted to move buttons lower
        if choice == 1:
            btn = Button(posX,posY,width,height,self.problem["result"])
            button_list.append(btn)
        else:
            btn = Button(posX,posY,width,height,random.randint(0,100))
            button_list.append(btn)

        posX = (SCREEN_WIDTH / 2) - (t_w/2) + 150

        if choice == 2:
            btn = Button(posX,posY,width,height,self.problem["result"])
            button_list.append(btn)
        else:
            btn = Button(posX,posY,width,height,random.randint(0,100))
            button_list.append(btn)

        posX = (SCREEN_WIDTH / 2) - (t_w /2)
        posY = 550  # Adjusted to move buttons lower

        if choice == 3:
            btn = Button(posX,posY,width,height,self.problem["result"])
            button_list.append(btn)
        else:
            btn = Button(posX,posY,width,height,random.randint(0,100))
            button_list.append(btn)

        posX = (SCREEN_WIDTH / 2) - (t_w/2) + 150

        if choice == 4:
            btn = Button(posX,posY,width,height,self.problem["result"])
            button_list.append(btn)
        else:
            btn = Button(posX,posY,width,height,random.randint(0,100))
            button_list.append(btn)

        return button_list

    def get_symbols(self):
        """ Return a dictionary with all the operation symbols """
        symbols = {}
        sprite_sheet = pygame.image.load("symbols.png").convert()
        image = self.get_image(sprite_sheet, 0, 0, 64, 64)
        symbols["addition"] = image
        image = self.get_image(sprite_sheet, 64, 0, 64, 64)
        symbols["subtraction"] = image
        image = self.get_image(sprite_sheet, 128, 0, 64, 64)
        symbols["multiplication"] = image
        image = self.get_image(sprite_sheet, 192, 0, 64, 64)
        symbols["division"] = image

        # Tambahkan gambar buah
        apple_image = pygame.image.load("apple.png").convert_alpha()
        apple_image = pygame.transform.scale(apple_image, (40, 40))  # Made larger
        symbols["apple"] = apple_image

        strawberry_image = pygame.image.load("strawberry.png").convert_alpha()
        strawberry_image = pygame.transform.scale(strawberry_image, (40, 40))  # Made larger
        symbols["strawberry"] = strawberry_image

        cherry_image = pygame.image.load("cherry.png").convert_alpha()
        cherry_image = pygame.transform.scale(cherry_image, (40, 40))  # Made larger
        symbols["cherry"] = cherry_image

        return symbols

    def get_image(self,sprite_sheet,x,y,width,height):
        """ This method will cut an image and return it """
        # Create a new blank image
        image = pygame.Surface([width,height]).convert()
        # Copy the sprite from the large sheet onto the smaller
        image.blit(sprite_sheet,(0,0),(x,y,width,height))
        # Return the image
        return image

    def addition(self):
        """ These will set num1,num2,result for addition """
        a = random.randint(4,16)
        b = random.randint(4,16)
        self.problem["num1"] = a
        self.problem["num2"] = b
        self.problem["result"] = a + b
        self.operation = "addition"

    def subtraction(self):
        """ These will set num1,num2,result for subtraction """
        a = random.randint(4,16)
        b = random.randint(4,16)
        if a > b:
            self.problem["num1"] = a
            self.problem["num2"] = b
            self.problem["result"] = a - b
        else:
            self.problem["num1"] = b
            self.problem["num2"] = a
            self.problem["result"] = b - a
        self.operation = "subtraction"

    def multiplication(self):
        """ These will set num1,num2,result for multiplication """
        a = random.randint(2,16)
        b = random.randint(2,16)
        self.problem["num1"] = a
        self.problem["num2"] = b
        self.problem["result"] = a * b
        self.operation = "multiplication"

    def division(self):
        """ These will set num1, num2, result for division """
        divisor = random.randint(2, 16)
        quotient = random.randint(1, 16 // divisor)  # Pastikan hasil pembagian <= 6
        dividend = divisor * quotient  # Hitung dividend dari divisor dan quotient
        self.problem["num1"] = dividend
        self.problem["num2"] = divisor
        self.problem["result"] = quotient
        self.operation = "division"

    def check_result(self):
        """ Check the result """
        for button in self.button_list:
            if button.isPressed():
                # Check if the number on the button matches the correct answer
                if button.get_number() == self.problem["result"]:
                    # Set color to green for correct answer
                    button.set_color(GREEN)
                    # Increase score
                    self.score += 5
                    # Play sound effect for correct answer
                    self.sound_2.play()
                else:
                    # Set color to red for incorrect answer
                    button.set_color(RED)
                    # Play sound effect for incorrect answer
                    self.sound_3.play()

                # Set reset_problem True so it can go to the next problem
                self.reset_problem = True
                break  # Exit the loop after processing the clicked button


    def set_problem(self):
        """ Create a new problem """
        # Jalankan operasi sesuai jenis yang dipilih
        if self.operation == "addition":
            self.addition()
        elif self.operation == "subtraction":
            self.subtraction()
        elif self.operation == "multiplication":
            self.multiplication()
        elif self.operation == "division":
            self.division()

        # Pilih buah secara acak untuk num1 dan num2
        fruits = ["apple", "strawberry", "cherry"]
        self.problem["fruit1"] = random.choice(fruits)  # Buah untuk num1
        self.problem["fruit2"] = random.choice(fruits)  # Buah untuk num2

        # Perbarui daftar tombol jawaban
        self.button_list = self.get_button_list()

    def process_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                return True  # Berhenti loop utama

            if self.show_menu:
                # Teruskan event ke menu untuk diproses
                if self.menu.process_events(event):
                    return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.show_menu:
                    # Handle menu interaksi
                    if self.menu.state == 0:
                        self.operation = "addition"
                        self.set_problem()
                        self.show_menu = False
                    elif self.menu.state == 1:
                        self.operation = "subtraction"
                        self.set_problem()
                        self.show_menu = False
                    elif self.menu.state == 2:
                        self.operation = "multiplication"
                        self.set_problem()
                        self.show_menu = False
                    elif self.menu.state == 3:
                        self.operation = "division"
                        self.set_problem()
                        self.show_menu = False
                else:
                    # Check tombol "Back" atau jawaban
                    if self.back_button.isPressed():
                        self.show_menu = True
                        self.score = 0
                        self.count = 0
                    else:
                        self.check_result()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.show_menu = True
                    self.score = 0
                    self.count = 0
        return False  # Tidak ada permintaan keluar




    def run_logic(self):
        # Update menu
        self.menu.update()

    def display_message(self,screen,items):
        """ display every string that is inside of a tuple(args) """
        for index, message in enumerate(items):
            label = self.font.render(message,True,BLACK)
            # Get the width and height of the label
            width = label.get_width()
            height = label.get_height()

            posX = (SCREEN_WIDTH /2) - (width /2)
            # t_h: total height of text block
            t_h = len(items) * height
            posY = (SCREEN_HEIGHT /2) - (t_h /2) + (index * height)

            screen.blit(label,(posX,posY))

    def display_frame(self, screen):
        # Gambar latar belakang
        screen.blit(self.background_image, (0, 0))
        time_wait = False

        if self.show_menu:
            self.menu.display_frame(screen)
        elif self.count == 20:
            # Jika sudah 20 soal, tampilkan hasil akhir
            msg_1 = "You answered " + str(self.score // 5) + " correctly"
            msg_2 = "Your score was " + str(self.score)
            self.display_message(screen, (msg_1, msg_2))
            self.show_menu = True
            self.score = 0
            self.count = 0
            time_wait = True
        else:
            # Gambar tombol Back di bagian atas layar
            self.back_button.draw(screen)

            # Gambar buah untuk num1 (menggunakan self.problem["fruit1"])
            fruit1 = self.symbols[self.problem["fruit1"]]
            for i in range(self.problem["num1"]):
                x_offset = 275 + (i %4) * 50  # Maksimal 3 buah per baris, Made larger
                y_offset = 150 + (i // 4) * 50  # Posisi vertikal baris baru, Moved lower
                screen.blit(fruit1, (x_offset, y_offset))

            # Gambar buah untuk num2 (menggunakan self.problem["fruit2"])
            fruit2 = self.symbols[self.problem["fruit2"]]
            for i in range(self.problem["num2"]):
                x_offset = 575 + (i % 4) * 50  # Maksimal 3 buah per baris, Made larger
                y_offset = 150 + (i // 4) * 50  # Posisi vertikal baris baru, Moved lower
                screen.blit(fruit2, (x_offset, y_offset))

            # Gambar simbol operasi di tengah, lebih rendah agar dekat ke apel
            screen.blit(self.symbols[self.operation], (SCREEN_WIDTH // 2 - 32, 225))

            # Gambar tombol jawaban di bagian bawah
            for btn in self.button_list:
                btn.draw(screen)

            # Tampilkan skor di pojok kiri atas
            score_label = self.score_font.render("Score: " + str(self.score), True, BLACK)
            screen.blit(score_label, (10, 10))

        # Perbarui layar
        pygame.display.flip()

        if self.reset_problem:
            pygame.time.wait(1000)  # Tunggu 1 detik
            self.set_problem()
            self.count += 1
            self.reset_problem = False
        elif time_wait:
            pygame.time.wait(3000)  # Tunggu 3 detik di akhir

class Button(object):
    def __init__(self, x, y, width, height, text, font_size=40):
        self.rect = pygame.Rect(x, y, width, height)
        self.font = pygame.font.Font(None, font_size)
        self.text = self.font.render(str(text), True, BLACK)
        self.text_content = text  # Store the actual number or text
        self.background_color = WHITE

    def draw(self, screen, enable_hover=False):
        """ This method will draw the button to the screen """
        # Highlight hover only if enabled
        if enable_hover and self.isHovered():
            pygame.draw.rect(screen, RED, self.rect)
        else:
            pygame.draw.rect(screen, self.background_color, self.rect)

        # Draw the edges of the button
        pygame.draw.rect(screen, BLACK, self.rect, 3)
        # Get the width and height of the text surface
        width = self.text.get_width()
        height = self.text.get_height()
        # Calculate the posX and posY
        posX = self.rect.centerx - (width / 2)
        posY = self.rect.centery - (height / 2)
        # Draw the image into the screen
        screen.blit(self.text, (posX, posY))

    def isPressed(self):
        """ Return true if the mouse is on the button """
        pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0]

    def isHovered(self):
        """ Return true if the mouse is hovering over the button """
        pos = pygame.mouse.get_pos()
        return self.rect.collidepoint(pos)

    def set_color(self, color):
        """ Set the background color """
        self.background_color = color

    def get_number(self):
        """ Return the text content as a number if it is numeric """
        try:
            return int(self.text_content)
        except ValueError:
            return None  # Return None if conversion fails


