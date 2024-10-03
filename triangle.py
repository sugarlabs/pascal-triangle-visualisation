# Copyright (C) 2024 Spandan Barve
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import pygame
from utils import pascal_triangle
import random


def view(game):
    vw = game.vw
    vh = game.vh
    font = game.font

    width = vw(100)
    # height variable is assigned but never used
    _ = vh(100)

    BLACK = (0, 0, 0)
    COLORS = [
        (80, 80, 255),    # Blue
        (255, 80, 80),    # Red
        (80, 255, 80),    # Green
        (255, 255, 80),   # Yellow
        (255, 80, 255),   # Pink
        (80, 255, 255),   # Cyan
        (255, 150, 80),   # Orange
        (150, 80, 255),   # Purple
        (80, 150, 255),   # Sky Blue
        (255, 80, 150),   # Magenta
        (255, 200, 80),   # Gold
        (80, 255, 150),   # Mint
        (150, 255, 80),   # Lime
        (80, 80, 150),    # Navy Blue
        (150, 255, 255),  # Light Cyan
        (255, 150, 150),  # Light Red
        (80, 200, 255),   # Light Sky Blue
        (255, 80, 200),   # Hot Pink
        (255, 230, 80),   # Soft Yellow
        (80, 255, 200),   # Aqua Green
        (150, 80, 150),   # Lavender
        (200, 80, 255),   # Bright Purple
        (255, 120, 80),   # Coral
        (80, 255, 120),   # Pastel Green
        (255, 180, 80),   # Peach
        (80, 120, 255),   # Bright Blue
        (200, 255, 80),   # Light Lime
        (80, 255, 255),   # Neon Cyan
        (80, 40, 40),     # Slate
        (255, 80, 120)    # Rose
    ]

    BUTTON_COLOR = (200, 200, 200)

    color_index = 0

    def draw_triangle(triangle, mod, display_numbers=True):
        num_rows = len(triangle)
        cell_width = width // (num_rows * 1.5)
        cell_height = vh(80) // num_rows

        for i, row in enumerate(triangle):
            x_offset = (width - len(row) * cell_width) // 2
            y = i * cell_height + 50

            for j, value in enumerate(row):
                color_mod = value % mod
                color = (COLORS[color_index][0],
                         COLORS[color_index][1],
                         COLORS[color_index][2],
                         int(20 + (color_mod / mod) * 200))
                temp_surface = pygame.Surface((cell_width,
                                               cell_height),
                                              pygame.SRCALPHA)
                temp_surface.fill(color)
                rect = pygame.Rect(x_offset + j * cell_width - vw(15), y,
                                   cell_width, cell_height)

                game.gameDisplay.blit(temp_surface, rect)

                if display_numbers and num_rows <= 50:
                    if num_rows > 32:
                        text = font.sm.render(str(value), True, BLACK)
                    elif num_rows > 25:
                        text = font.md.render(str(value), True, BLACK)
                    elif num_rows > 8:
                        text = font.lg.render(str(value), True, BLACK)
                    elif num_rows > 5:
                        text = font.xl.render(str(value), True, BLACK)
                    else:
                        text = font.xxl.render(str(value), True, BLACK)
                    text_rect = text.get_rect(center=rect.center)
                    game.gameDisplay.blit(text, text_rect)

    rows = 14
    mod = 3
    display_numbers = True
    triangle = pascal_triangle(rows, mod)

    instructions = font.lg.render(
        "Use < Arrow Keys > + < Space Bar > to control parameters",
        True,
        BLACK
    )

    # Controls
    row_decrement_rect = pygame.Rect((width - 140, vh(15)), (40, 40))
    row_increment_rect = pygame.Rect((width - 80, vh(15)), (40, 40))

    modulo_decrement_rect = pygame.Rect((width - 140, vh(30)), (40, 40))
    modulo_increment_rect = pygame.Rect((width - 80, vh(30)), (40, 40))

    color_change_rect = pygame.Rect((width - 140, vh(42)), (100, 40))

    minus_sign = font.xl.render("-", True, BLACK)
    plus_sign = font.xl.render("+", True, BLACK)

    def draw_controls():
        # Rows
        text = font.lg.render(f"Rows: {rows}", True, BLACK)
        game.gameDisplay.blit(text,
                              (row_decrement_rect.x,
                               row_decrement_rect.y - 40))

        pygame.draw.rect(game.gameDisplay, BUTTON_COLOR, row_decrement_rect)
        game.blit_centered(minus_sign, row_decrement_rect.center)
        pygame.draw.rect(game.gameDisplay, BUTTON_COLOR, row_increment_rect)
        game.blit_centered(plus_sign, row_increment_rect.center)

        # Modulo
        text = font.lg.render(f"Modulo: {mod}", True, BLACK)
        game.gameDisplay.blit(text,
                              (modulo_decrement_rect.x,
                               modulo_decrement_rect.y - 40))

        pygame.draw.rect(game.gameDisplay, BUTTON_COLOR, modulo_decrement_rect)
        game.blit_centered(minus_sign, modulo_decrement_rect.center)
        pygame.draw.rect(game.gameDisplay, BUTTON_COLOR, modulo_increment_rect)
        game.blit_centered(plus_sign, modulo_increment_rect.center)

        # Color
        pygame.draw.rect(game.gameDisplay,
                         COLORS[color_index],
                         color_change_rect)

    def update():
        nonlocal triangle, display_numbers, mod, rows, color_index

        for event in game.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    rows += 1
                    triangle = pascal_triangle(rows, mod)
                elif event.key == pygame.K_DOWN:
                    rows = max(1, rows - 1)
                    triangle = pascal_triangle(rows, mod)
                elif event.key == pygame.K_RIGHT:
                    mod += 1
                    triangle = pascal_triangle(rows, mod)
                elif event.key == pygame.K_LEFT:
                    mod = max(1, mod - 1)
                    triangle = pascal_triangle(rows, mod)
                elif event.key == pygame.K_SPACE:
                    display_numbers = not display_numbers

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_pos = pygame.mouse.get_pos()
                if row_decrement_rect.collidepoint(mouse_pos):
                    rows = max(1, rows - 1)
                    triangle = pascal_triangle(rows, mod)
                if row_increment_rect.collidepoint(mouse_pos):
                    rows += 1
                    triangle = pascal_triangle(rows, mod)
                if modulo_decrement_rect.collidepoint(mouse_pos):
                    mod = max(1, mod - 1)
                    triangle = pascal_triangle(rows, mod)
                if modulo_increment_rect.collidepoint(mouse_pos):
                    mod += 1
                    triangle = pascal_triangle(rows, mod)
                if color_change_rect.collidepoint(mouse_pos):
                    color_index = random.choice(list(range(len(COLORS))))

        draw_triangle(triangle, mod, display_numbers)
        draw_controls()
        game.blit_centered(instructions, (width // 2, vh(96)))

    game.update_function = update
