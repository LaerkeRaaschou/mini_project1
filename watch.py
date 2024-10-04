import pygame
import math
from datetime import datetime

# Setting up the screen
pygame.init()
screen_size = (640,640)
screen = pygame.display.set_mode(screen_size)
screen.fill((250,220,248))

# Global varibles
radius = 250
ANGLE = - 90
screen_center = (screen_size[0] // 2 , screen_size[1] // 2)
font = pygame.font.SysFont(None, 40)

# Make sure the window stays open until the user closes it
# Drawing the watch over and over again
run_flag = True
while run_flag is True:

    # Drawing the clock face
    screen.fill((250,220,248))
    pygame.draw.circle(screen,(252, 198, 3),screen_center,5)
    pygame.draw.circle(screen,(50,50,255),screen_center,radius,10)

    # Drawing minut marks and numbers
    for angle in range(0, 360, 6):
        # Calculating the start and end of the minut marks
        radian_angle = math.radians(angle - 60)
        start_offset = [(radius - 35) * math.cos(radian_angle), (radius - 35) * math.sin(radian_angle)]
        start_position = (screen_center[0] + start_offset[0], screen_center[1] + start_offset[1])

        end_offset = [(radius - 15) * math.cos(radian_angle), (radius - 15) * math.sin(radian_angle)]
        end_position = (screen_center[0] + end_offset[0], screen_center[1] + end_offset[1])

        if angle%30:
            # Minut marks
            pygame.draw.line(screen, (250,117,248), start_position, end_position, 3)

        else:
            # Thicker hour marks and text
            pygame.draw.line(screen, (250,117,248), start_position, end_position, 6)

            text = font.render(f'{angle // 30 + 1}', True, (250,117,248))
            text_width = text.get_width()
            text_height = text.get_height()

            text_x = screen_center[0] - text_width//2 + (radius - 55) * math.cos(radian_angle)
            text_y = screen_center[1] - text_height//2 + (radius - 55) * math.sin(radian_angle)
            screen.blit(text, (text_x, text_y))
            
    # Getting the time
    s = datetime.now().second
    m = datetime.now().minute
    h = datetime.now().hour

    # print(s,m,h)
    
    # Sekond hand
    s_end_x = screen_center[0] + (radius - 75) * math.cos(math.radians(ANGLE + 6 * s))
    s_end_y = screen_center[1] + (radius - 75) * math.sin(math.radians(ANGLE + 6 * s))
    s_end_position = (s_end_x, s_end_y)
    pygame.draw.aaline(screen, (252, 198, 3), screen_center,s_end_position,3)

    # Minut hand
    m_end_x = screen_center[0] + (radius - 50) * math.cos(math.radians(ANGLE + 6 * m + 0.1 * s))
    m_end_y = screen_center[1] + (radius - 50) * math.sin(math.radians(ANGLE + 6 * m + 0.1 * s))
    m_end_position = (m_end_x, m_end_y)
    pygame.draw.line(screen, (252, 198, 3), screen_center, m_end_position, 6)

    # Hour hand
    h_end_x = screen_center[0] + (radius - 110) * math.cos(math.radians(ANGLE + 30 * h + 0.5 * m))
    h_end_y = screen_center[1] + (radius - 110) * math.sin(math.radians(ANGLE + 30 * h + 0.5 * m))
    h_end_position = (h_end_x, h_end_y)
    pygame.draw.line(screen, (252, 198, 3), screen_center, h_end_position, 10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_flag = False
    pygame.display.flip() # Refresh the screen so drawing appears