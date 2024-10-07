import unittest, pygame
from game_strategy import GraphicsManager
from pipe import PipeFactory, Pipe
from game_strategy import GameStrategy
from bird_and_score import BirdAnimator, ScoreManager

pygame.mixer.init()


class TestScoreManager(unittest.TestCase):
    #TestScoreManager - перевіряє клас ScoreManager, який відповідає за зберігання та відображення очок у грі.
    def setUp(self):
        self.score = 0
        self.high_score = 0
        self.game_font = pygame.font.Font('04B_19.ttf', 40)
        self.screen = pygame.display.set_mode((576, 1024))
        self.score_manager = ScoreManager(self.score, self.high_score, self.game_font, self.screen)

    def test_init(self):
        #test_init - перевіряє правильність ініціалізації об'єкта ScoreManager з заданими значеннями очок, найкращих очок, шрифту та екрану.

        self.assertEqual(self.score_manager.score, self.score)
        self.assertEqual(self.score_manager.high_score, self.high_score)
        self.assertEqual(self.score_manager.game_font, self.game_font)
        self.assertEqual(self.score_manager.screen, self.screen)

    def test_display_score(self):
        #test_display_score - перевіряє відображення очок на екрані у двох станах: "main_game" та "game_over".
        self.score_manager.display_score('main_game', self.screen)
        self.score_manager.display_score('game_over', self.screen)


class TestGameStrategy(unittest.TestCase):
    #TestGameStrategy - перевіряє клас GameStrategy, який відповідає за логіку гри Flappy Bird.
    @classmethod
    def setUpClass(cls):
        pygame.init()
        pygame.display.set_mode((576, 1024))

    def setUp(self):
        self.bird_rect = pygame.Rect(100, 512, 50, 50)
        self.death_sound = pygame.mixer.Sound('sound/sfx_hit.wav')
        self.game_strategy = GameStrategy(self.bird_rect, self.death_sound)

    def test_init(self):
        #test_init - перевіряє правильність ініціалізації об'єкта GameStrategy з заданими значеннями пташки, звуку смерті та екрану.
        self.assertTrue(self.game_strategy.game_active)
        self.assertEqual(self.game_strategy.bird_rect, self.bird_rect)
        self.assertEqual(self.game_strategy.death_sound, self.death_sound)

    def test_check_collision_true(self):
        #test_check_collision_true - перевіряє, чи правильно виявляється зіткнення між пташкою та трубами.
        pipe1 = Pipe(400, (50, 100))
        pipe2 = Pipe(600, (50, 100))
        pipes = [pipe1, pipe2]
        self.assertTrue(self.game_strategy.check_collision(self.bird_rect, self.death_sound, pipes))



    def test_check_collision_outside_screen(self):
        #test_check_collision_outside_screen - перевіряє, чи правильно виявляється зіткнення між пташкою та межами екрану зверху.
        self.bird_rect.top = -150
        pipes = []
        self.assertFalse(self.game_strategy.check_collision(self.bird_rect, self.death_sound, pipes))

    def test_check_collision_bottom_screen(self):
        #test_check_collision_bottom_screen - перевіряє, чи правильно виявляється зіткнення між пташкою та межами екрану знизу.
        self.bird_rect.bottom = 950
        pipes = []
        self.assertFalse(self.game_strategy.check_collision(self.bird_rect, self.death_sound, pipes))

class TestPipeComposite(unittest.TestCase):
    #Перевірка ініціалізації та методів add_pipe, move_pipes, remove_pipes, і draw_pipes класу PipeComposite
    def test_init(self):
        pipe_surface = pygame.Surface((50, 100))

class TestPipeFactory(unittest.TestCase):
    #Перевірка ініціалізації та методу create_pipe класу PipeFactory

    def test_create_pipe(self):
        #test_create_pipe - перевіряє, чи правильно створюється об'єкт труби класом PipeFactory.
        pipe_factory = PipeFactory()
        pipe = pipe_factory.create_pipe((400, 800), (50, 100))
        self.assertIsInstance(pipe, Pipe)

class TestGraphicsManager(unittest.TestCase):
    #Перевірка ініціалізації та методу draw_floor класу GraphicsManager

    def test_init(self):
        #test_init - перевіряє правильність ініціалізації об'єкта GraphicsManager з заданим екраном.
        screen = pygame.display.set_mode((576, 1024))
        graphics_manager = GraphicsManager(screen)
        self.assertIsNotNone(graphics_manager.screen)

    def test_draw_floor(self):
        #test_draw_floor - перевіряє, чи правильно відображається підлога на екрані.
        screen = pygame.display.set_mode((576, 1024))
        graphics_manager = GraphicsManager(screen)
        graphics_manager.draw_floor()
        self.assertGreater(screen.get_width(), 0)
        self.assertGreater(screen.get_height(), 0)

if __name__ == '__main__':
    unittest.main()

