import pygame
import sys
from Body import Snake
from Food import Food
from Menu import display_menu, display_difficulty_menu
from Items import *


def load_high_score():
    try:
        with open("highscore.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 0

def save_high_score(score):
    with open("highscore.txt", "w") as file:
        file.write(str(score))


def main():
    pygame.init()

    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
    surface = pygame.Surface(screen.get_size())
    surface = surface

    background_image = pygame.image.load("background.png")
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

    high_score = load_high_score()
    snake = Snake()
    food = Food()

    in_menu = True
    selected_item = 0
    in_difficulty_menu = False
    selected_difficulty_item = 0
    fps = 10

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if in_menu:
                    if event.key == pygame.K_RETURN:
                        if selected_item == 0:
                            in_menu = False
                            in_difficulty_menu = True
                        elif selected_item == 1:
                            pygame.quit()
                            sys.exit()
                    elif event.key in (pygame.K_UP, pygame.K_DOWN):
                        selected_item = (selected_item + 1) % len(MENU_ITEMS)
                elif in_difficulty_menu:
                    if event.key == pygame.K_RETURN:
                        if selected_difficulty_item == 0:
                            fps = 10
                        elif selected_difficulty_item == 1:
                            fps = 15
                        elif selected_difficulty_item == 2:
                            fps = 30
                        in_difficulty_menu = False
                        in_menu = False
                    elif event.key in (pygame.K_UP, pygame.K_DOWN):
                        selected_difficulty_item = (selected_difficulty_item + 1) % len(DIFFICULTY_ITEMS)
                elif not in_menu and not in_difficulty_menu:
                    if event.key == pygame.K_UP and snake.direction != DOWN:
                        snake.direction = UP
                    elif event.key == pygame.K_DOWN and snake.direction != UP:
                        snake.direction = DOWN
                    elif event.key == pygame.K_LEFT and snake.direction != RIGHT:
                        snake.direction = LEFT
                    elif event.key == pygame.K_RIGHT and snake.direction != LEFT:
                        snake.direction = RIGHT
                    elif event.key == pygame.K_SPACE:
                        snake.paused = not snake.paused
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()

        if in_menu:
            surface.blit(background_image, (1, 2))
            display_menu(surface, "Snake Game", MENU_ITEMS, selected_item)
        elif in_difficulty_menu:
            surface.blit(background_image, (1, 2))
            display_difficulty_menu(surface, DIFFICULTY_ITEMS, selected_difficulty_item)
        else:
            snake.update()

            if snake.get_head_position() == food.position:
                snake.length += 1
                if snake.length > high_score:
                    high_score = snake.length
                    save_high_score(high_score)
                food.randomize_position()

            if len(snake.positions) > 2 and snake.get_head_position() in snake.positions[2:]:
                snake.reset()

            surface.blit(background_image, (1, 2))
            snake.render(surface)
            food.render(surface)

            font = pygame.font.Font(None, 28)
            score_text = font.render(f"Score: {snake.length}", True, WHITE)
            high_score_text = font.render(f"High Score: {high_score}", True, WHITE)
            instructions_text = font.render("Pause: Spacebar" "/ " "Quit: ESC", True, WHITE)
            surface.blit(instructions_text, (5, 375))
            surface.blit(score_text, (10, 5))
            surface.blit(high_score_text, (105, 5))

            if snake.paused:
                pause_text = font.render("Paused", True, WHITE)
                surface.blit(pause_text,
                             ((WIDTH - pause_text.get_width()) // 2, (HEIGHT - pause_text.get_height()) // 2))

        screen.blit(surface, (0, 0))
        pygame.display.update()
        clock.tick(fps)


if __name__ == "__main__":
    main()
