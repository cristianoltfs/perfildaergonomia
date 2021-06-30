import pygame 
from input_text import TextInputBox


pygame.init()
window = pygame.display.set_mode((500, 200))
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 100)

text_input_box = TextInputBox(50, 50, 400, font)
group = pygame.sprite.Group(text_input_box)

run = True
while run:
    clock.tick(10)
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False
            
    group.update(event_list)
    window.fill(0)
    group.draw(window)
    pygame.display.flip()

pygame.quit()
exit()