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

def view(game):
    vw = game.vw
    vh = game.vh
    font = game.font

    width = vw(100)
    height = vh(100)

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    COLORS = [(200, 200, 255), (100, 100, 255), (50, 50, 255)]

    instructions = font.lg.render("Up/Down: Rows, Left/Right: Modulo, Space: Toggle Numbers/Colors", True, BLACK)

    def pascal_triangle(rows, mod):
        triangle = [[1]]
        for i in range(1, rows):
            row = [1]
            for j in range(1, i):
                row.append((triangle[i-1][j-1] + triangle[i-1][j]) % mod)
            row.append(1)
            triangle.append(row)
        return triangle

    def draw_triangle(triangle, mod, display_numbers=True):
        num_rows = len(triangle)
        cell_width = width // (num_rows * 2)
        cell_height = 30

        for i, row in enumerate(triangle):
            x_offset = (width - len(row) * cell_width) // 2
            y = i * cell_height + 50

            for j, value in enumerate(row):
                color_index = value % mod
                color = COLORS[color_index % len(COLORS)]

                rect = pygame.Rect(x_offset + j * cell_width, y, cell_width, cell_height)
                pygame.draw.rect(game.gameDisplay, color, rect)

                if display_numbers:
                    text = font.lg.render(str(value), True, BLACK)
                    text_rect = text.get_rect(center=rect.center)
                    game.gameDisplay.blit(text, text_rect)

    rows = 14
    mod = 3
    display_numbers = True
    triangle = pascal_triangle(rows, mod)

    def update():
        nonlocal triangle, display_numbers, mod, rows

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
                    triangle = pascal_triangle(rows, mod)

                triangle = pascal_triangle(rows, mod)

        draw_triangle(triangle, mod, display_numbers)

        game.gameDisplay.blit(instructions, (10, 10))


    game.update_function = update
