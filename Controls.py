import math
import pygame

from Constants import SPEED
from Physics.Bodies.Projectile import Projectile
from Physics.Vector import Vector


def controls(player, dt: float):
    keys = pygame.key.get_pressed()

    player.move(Vector(
        (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * dt * SPEED,
        (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * dt * SPEED
    ))


def shoot_positions(player, projectile_type):
    x, y = pygame.mouse.get_pos()
    angle = math.atan2(y - player.position.y, x - player.position.x)

    start_pos = Vector(player.position.x + math.cos(angle) * player.width,
                       player.position.y + math.sin(angle) * player.height)

    end_pos = Vector(math.cos(angle) * 500,
                     math.sin(angle) * 500)

    return start_pos, end_pos


def shoot_controls(player, event, world=None):
    if event.type == pygame.MOUSEBUTTONUP:
        pos, vel = shoot_positions(player, None)

        projectile = Projectile(pos, 16, 16, world=world)
        projectile.linear_velocity = vel

        player.has_shoot = True

        return projectile
