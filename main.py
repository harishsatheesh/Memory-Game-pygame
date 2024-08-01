# import pygame, os, random

# pygame.init()

# # Variables for Game
# gameWidth = 840
# gameHeight = 640
# picSize = 128
# gameColumns = 5
# gameRows = 4
# padding = 10
# leftMargin = (gameWidth - ((picSize + padding) * gameColumns)) // 2
# rightMargin = leftMargin
# topMargin = (gameHeight - ((picSize + padding) * gameRows)) // 2
# bottomMargin = topMargin
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# BUTTON_COLOR = (200, 200, 200)
# BUTTON_HOVER_COLOR = (150, 150, 150)
# selection1 = None
# selection2 = None
# wrong_guesses = 0
# max_wrong_guesses = 5
# button_width = 100
# button_height = 40
# button_rect = pygame.Rect(10, 10, button_width, button_height)

# # Initialize font
# pygame.font.init()
# font = pygame.font.Font(None, 74)
# button_font = pygame.font.Font(None, 30)
# lose_text = font.render('You Lose!', True, BLACK)
# win_text = font.render('You Win!', True, BLACK)
# lose_text_rect = lose_text.get_rect(center=(gameWidth // 2, gameHeight // 2))
# win_text_rect = win_text.get_rect(center=(gameWidth // 2, gameHeight // 2))
# restart_text = button_font.render('Restart', True, BLACK)
# restart_text_rect = restart_text.get_rect(center=button_rect.center)

# def initialize_game():
#     global selection1, selection2, wrong_guesses, hiddenImages, memPicsRect, memoryPictures, memPics
#     global gameOver
#     selection1 = None
#     selection2 = None
#     wrong_guesses = 0
#     hiddenImages = []
#     memoryPictures = []
#     memPics = []
#     memPicsRect = []

#     # Load the BackGround image into Python
#     bgImage = pygame.image.load('Background.png')
#     bgImage = pygame.transform.scale(bgImage, (gameWidth, gameHeight))
#     bgImageRect = bgImage.get_rect()

#     # Create list of Memory Pictures
#     for item in os.listdir('images/'):
#         memoryPictures.append(item.split('.')[0])
#     memoryPicturesCopy = memoryPictures.copy()
#     memoryPictures.extend(memoryPicturesCopy)
#     memoryPicturesCopy.clear()
#     random.shuffle(memoryPictures)

#     # Load each of the images into the python memory
#     for item in memoryPictures:
#         picture = pygame.image.load(f'images/{item}.png')
#         picture = pygame.transform.scale(picture, (picSize, picSize))
#         memPics.append(picture)
#         pictureRect = picture.get_rect()
#         memPicsRect.append(pictureRect)

#     for i in range(len(memPicsRect)):
#         memPicsRect[i][0] = leftMargin + ((picSize + padding) * (i % gameColumns))
#         memPicsRect[i][1] = topMargin + ((picSize + padding) * (i % gameRows))
#         hiddenImages.append(False)

# initialize_game()

# # Loading the pygame screen.
# screen = pygame.display.set_mode((gameWidth, gameHeight))
# pygame.display.set_caption('Memory Game')
# gameIcon = pygame.image.load('images/Apple.png')
# pygame.display.set_icon(gameIcon)

# # Load the BackGround image into Python
# bgImage = pygame.image.load('Background.png')
# bgImage = pygame.transform.scale(bgImage, (gameWidth, gameHeight))
# bgImageRect = bgImage.get_rect()

# gameLoop = True
# gameOver = False
# while gameLoop:
#     # Load background image
#     screen.blit(bgImage, bgImageRect)
    
#     # Draw the restart button
#     pygame.draw.rect(screen, BUTTON_COLOR, button_rect)
#     screen.blit(restart_text, restart_text_rect)

#     # Display the wrong guesses count
#     wrong_guesses_text = button_font.render(f'Wrong Guesses: {wrong_guesses}', True, BLACK)
#     screen.blit(wrong_guesses_text, (button_rect.right + 10, button_rect.top))
    
#     # Input events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             gameLoop = False
#         if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#             if button_rect.collidepoint(event.pos):
#                 initialize_game()  # Restart the game
#                 gameOver = False
#             elif not gameOver:
#                 for item in memPicsRect:
#                     if item.collidepoint(event.pos):
#                         if hiddenImages[memPicsRect.index(item)] != True:
#                             if selection1 != None:
#                                 selection2 = memPicsRect.index(item)
#                                 hiddenImages[selection2] = True
#                             else:
#                                 selection1 = memPicsRect.index(item)
#                                 hiddenImages[selection1] = True

#     if not gameOver:
#         for i in range(len(memoryPictures)):
#             if hiddenImages[i] == True:
#                 screen.blit(memPics[i], memPicsRect[i])
#             else:
#                 pygame.draw.rect(screen, WHITE, (memPicsRect[i][0], memPicsRect[i][1], picSize, picSize))
#         pygame.display.update()

#         if selection1 != None and selection2 != None:
#             if memoryPictures[selection1] == memoryPictures[selection2]:
#                 selection1, selection2 = None, None
#             else:
#                 pygame.time.wait(1000)
#                 hiddenImages[selection1] = False
#                 hiddenImages[selection2] = False
#                 selection1, selection2 = None, None
#                 wrong_guesses += 1  # Increment wrong guesses

#         if wrong_guesses >= max_wrong_guesses:
#             gameOver = True

#         win = 1
#         for number in range(len(hiddenImages)):
#             win *= hiddenImages[number]

#         if win == 1:
#             gameOver = True

#     if gameOver:
#         if wrong_guesses >= max_wrong_guesses:
#             screen.blit(lose_text, lose_text_rect)
#         else:
#             screen.blit(win_text, win_text_rect)
#         pygame.display.update()

#         while gameOver:
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     gameLoop = False
#                     gameOver = False
#                 elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#                     if button_rect.collidepoint(event.pos):
#                         initialize_game()  # Restart the game
#                         gameOver = False

#     pygame.display.update()

# pygame.quit()

import pygame, os, random

pygame.init()

# Variables for Game
gameWidth = 840
gameHeight = 640
picSize = 128
gameColumns = 5
gameRows = 4
padding = 10
topMargin = (gameHeight - ((picSize + padding) * gameRows)) // 2 + 20  # Increase margin to shift tiles down
leftMargin = (gameWidth - ((picSize + padding) * gameColumns)) // 2
rightMargin = leftMargin
bottomMargin = topMargin
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (200, 200, 200)
BUTTON_HOVER_COLOR = (150, 150, 150)
selection1 = None
selection2 = None
wrong_guesses = 0
max_wrong_guesses = 5
button_width = 100
button_height = 40
button_rect = pygame.Rect(10, 10, button_width, button_height)

# Initialize font
pygame.font.init()
font = pygame.font.Font(None, 74)
button_font = pygame.font.Font(None, 30)
lose_text = font.render('You Lose!', True, BLACK)
win_text = font.render('You Win!', True, BLACK)
lose_text_rect = lose_text.get_rect(center=(gameWidth // 2, gameHeight // 2))
win_text_rect = win_text.get_rect(center=(gameWidth // 2, gameHeight // 2))
restart_text = button_font.render('Restart', True, BLACK)
restart_text_rect = restart_text.get_rect(center=button_rect.center)

def initialize_game():
    global selection1, selection2, wrong_guesses, hiddenImages, memPicsRect, memoryPictures, memPics
    global gameOver
    selection1 = None
    selection2 = None
    wrong_guesses = 0
    hiddenImages = []
    memoryPictures = []
    memPics = []
    memPicsRect = []

    # Load the BackGround image into Python
    bgImage = pygame.image.load('Background.png')
    bgImage = pygame.transform.scale(bgImage, (gameWidth, gameHeight))
    bgImageRect = bgImage.get_rect()

    # Create list of Memory Pictures
    for item in os.listdir('images/'):
        memoryPictures.append(item.split('.')[0])
    memoryPicturesCopy = memoryPictures.copy()
    memoryPictures.extend(memoryPicturesCopy)
    memoryPicturesCopy.clear()
    random.shuffle(memoryPictures)

    # Load each of the images into the python memory
    for item in memoryPictures:
        picture = pygame.image.load(f'images/{item}.png')
        picture = pygame.transform.scale(picture, (picSize, picSize))
        memPics.append(picture)
        pictureRect = picture.get_rect()
        memPicsRect.append(pictureRect)

    for i in range(len(memPicsRect)):
        memPicsRect[i][0] = leftMargin + ((picSize + padding) * (i % gameColumns))
        memPicsRect[i][1] = topMargin + ((picSize + padding) * (i // gameColumns))  # Changed to align correctly
        hiddenImages.append(False)

initialize_game()

# Loading the pygame screen.
screen = pygame.display.set_mode((gameWidth, gameHeight))
pygame.display.set_caption('Memory Game')
gameIcon = pygame.image.load('images/Apple.png')
pygame.display.set_icon(gameIcon)

# Load the BackGround image into Python
bgImage = pygame.image.load('Background.png')
bgImage = pygame.transform.scale(bgImage, (gameWidth, gameHeight))
bgImageRect = bgImage.get_rect()

gameLoop = True
gameOver = False
while gameLoop:
    # Load background image
    screen.blit(bgImage, bgImageRect)
    
    # Draw the restart button
    pygame.draw.rect(screen, BUTTON_COLOR, button_rect)
    screen.blit(restart_text, restart_text_rect)

    # Display the wrong guesses count aligned with the restart button
    wrong_guesses_text = button_font.render(f'Wrong Guesses: {wrong_guesses}', True, BLACK)
    wrong_guesses_text_rect = wrong_guesses_text.get_rect(midleft=(button_rect.right + 10, button_rect.centery))
    screen.blit(wrong_guesses_text, wrong_guesses_text_rect)
    
    # Input events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameLoop = False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                initialize_game()  # Restart the game
                gameOver = False
            elif not gameOver:
                for item in memPicsRect:
                    if item.collidepoint(event.pos):
                        if hiddenImages[memPicsRect.index(item)] != True:
                            if selection1 != None:
                                selection2 = memPicsRect.index(item)
                                hiddenImages[selection2] = True
                            else:
                                selection1 = memPicsRect.index(item)
                                hiddenImages[selection1] = True

    if not gameOver:
        for i in range(len(memoryPictures)):
            if hiddenImages[i] == True:
                screen.blit(memPics[i], memPicsRect[i])
            else:
                pygame.draw.rect(screen, WHITE, (memPicsRect[i][0], memPicsRect[i][1], picSize, picSize))
        pygame.display.update()

        if selection1 != None and selection2 != None:
            if memoryPictures[selection1] == memoryPictures[selection2]:
                selection1, selection2 = None, None
            else:
                pygame.time.wait(1000)
                hiddenImages[selection1] = False
                hiddenImages[selection2] = False
                selection1, selection2 = None, None
                wrong_guesses += 1  # Increment wrong guesses

        if wrong_guesses >= max_wrong_guesses:
            gameOver = True

        win = 1
        for number in range(len(hiddenImages)):
            win *= hiddenImages[number]

        if win == 1:
            gameOver = True

    if gameOver:
        if wrong_guesses >= max_wrong_guesses:
            screen.blit(lose_text, lose_text_rect)
        else:
            screen.blit(win_text, win_text_rect)
        pygame.display.update()

        while gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameLoop = False
                    gameOver = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if button_rect.collidepoint(event.pos):
                        initialize_game()  # Restart the game
                        gameOver = False

    pygame.display.update()

pygame.quit()