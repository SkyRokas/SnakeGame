import pygame
from Items import *


def display_menu(screen, title, items, selected_item):
    screen.fill(BLACK)

    font = pygame.font.Font(None, MENU_FONT_SIZE)
    title_text = font.render(title, True, WHITE)
    screen.blit(title_text, ((WIDTH - title_text.get_width()) // 2, 100))

    button_font = pygame.font.Font(None, BUTTON_FONT_SIZE)
    for i, item in enumerate(items):
        text = button_font.render(item, True, WHITE)
        rect = pygame.Rect(
            (WIDTH - text.get_width()) // 2,
            200 + i * MENU_ITEM_HEIGHT,
            text.get_width(),
            text.get_height()
        )
        pygame.draw.rect(screen, RED if i == selected_item else WHITE, rect, 2)
        screen.blit(text, rect.topleft)

    pygame.display.flip()


def display_difficulty_menu(screen, items, selected_item):
    screen.fill(BLACK)

    font = pygame.font.Font(None, MENU_FONT_SIZE)
    title_text = font.render("Difficulty", True, WHITE)
    screen.blit(title_text, ((WIDTH - title_text.get_width()) // 2, 100))

    button_font = pygame.font.Font(None, BUTTON_FONT_SIZE)
    for i, item in enumerate(items):
        text = button_font.render(item, True, WHITE)
        rect = pygame.Rect(
            (WIDTH - text.get_width()) // 2,
            200 + i * MENU_ITEM_HEIGHT,
            text.get_width(),
            text.get_height()
        )
        pygame.draw.rect(screen, RED if i == selected_item else WHITE, rect, 2)
        screen.blit(text, rect.topleft)

    pygame.display.flip()
