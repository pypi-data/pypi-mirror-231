import unittest
from unittest.mock import MagicMock

from pygame.math import Vector2
from pygame.sprite import Sprite
from pygame.surface import Surface

from pygutils.camera import TopDownCamera


class DummySprite(Sprite):
    def __init__(self, x: int, y: int, *groups) -> None:
        super().__init__(*groups)

        self.image = Surface((5, 5))
        self.rect = self.image.get_rect(center=(x, y))


class TopDownCameraTest(unittest.TestCase):
    def test_retrieve_sprites_ordered_by_y_coordinate(self):
        sprite1 = DummySprite(3, 3)
        sprite2 = DummySprite(2, 2)
        sprite3 = DummySprite(1, 1)

        camera = TopDownCamera(None, [sprite1, sprite2, sprite3])

        self.assertListEqual([sprite3, sprite2, sprite1], camera.sprites())

    def test_retrieve_only_visible_sprites_on_surface(self):
        sprite1 = DummySprite(20, 20)
        sprite2 = DummySprite(2, 2)
        sprite3 = DummySprite(2, 8)

        camera = TopDownCamera(None, [sprite1, sprite2, sprite3])
        camera.offset = Vector2(0, 0)

        visible_sprites = camera.get_visible_sprites(Surface((10, 10)))
        expected_sprites = [
            (sprite.image, sprite.rect.topleft) for sprite in [sprite2, sprite3]
        ]

        self.assertListEqual(expected_sprites, visible_sprites)

    def test_dont_draw_background_if_not_exists(self):
        screen = MagicMock(spec=Surface)

        camera = TopDownCamera(None)
        camera.draw(screen, DummySprite(5, 5))

        screen.blit.assert_not_called()

    def test_draw_background_if_it_exists(self):
        screen = MagicMock(spec=Surface)
        screen.get_width.return_value = 10
        screen.get_height.return_value = 10

        bg = Surface((10, 10))

        camera = TopDownCamera(bg)
        camera.draw(screen, DummySprite(5, 5))

        screen.blit.assert_called_once_with(bg, Vector2(0, 0))

    def test_draw_all_visible_sprites(self):
        visible_sprites = [(Surface((5, 5)), (0, 0)), (Surface((10, 10)), (0, 1))]

        screen = MagicMock(spec=Surface)

        camera = TopDownCamera(None)
        camera.get_visible_sprites = MagicMock(return_value=visible_sprites)
        camera.draw(screen, DummySprite(5, 5))

        screen.blits.assert_called_once_with(visible_sprites, True)
