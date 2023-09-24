from PyQt6.QtGui import QImage, QPixmap, QPainter, QPen, QBrush, QColor
from PyQt6.QtCore import Qt, QThread, pyqtSignal
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QLabel, QWidget, QPushButton, QComboBox, QTabWidget, QListWidget, QFormLayout, QLineEdit
import retro
import numpy as np
import sys
import random
import warnings
import datetime
import time
import os

DATA_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data')

env: retro.RetroEnv = None


class FrameTimer(QThread):
    end_frame_signal = pyqtSignal()
    update_frame_signal = pyqtSignal()

    def __init__(self, game_speed):
        super().__init__()
        self.game_speed = game_speed
        self.next_frame_ready = False
        self.is_game_running = True

    def end_frame_event(self):
        if self.game_speed == 2:
            self.next_frame_ready = True
            self.update_frame_signal.emit()

    def stop_game(self):
        self.is_game_running = False

    def run(self):
        if self.game_speed != 2:
            while self.is_game_running:
                if self.game_speed == 0:
                    self.msleep(1000 // 60)
                elif self.game_speed == 1:
                    self.msleep(1000 // 120)
                else:
                    self.msleep(1000 // 60)
                self.next_frame_ready = True
                self.update_frame_signal.emit()
        else:
            self.end_frame_event()


class Mario(QWidget):
    def __init__(self, main, game_level, game_speed):
        super().__init__()
        self.setWindowTitle('Mario')
        self.main = main
        self.game_speed = game_speed

        global env
        if env is not None:
            env.close()
        env = retro.make(game='SuperMarioBros-Nes', state=f'Level{game_level + 1}-1')
        self.env = env
        screen = self.env.reset()

        self.key_up = False
        self.key_down = False
        self.key_left = False
        self.key_right = False

        self.key_a = False
        self.key_b = False

        self.screen_width = screen.shape[0] * 2
        self.screen_height = screen.shape[1] * 2

        self.setFixedSize(self.screen_width, self.screen_height)
        self.move(100, 100)

        self.screen_label = QLabel(self)
        self.screen_label.setGeometry(0, 0, self.screen_width, self.screen_height)

        self.press_buttons = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0])

        self.frame_timer = FrameTimer(self.game_speed)
        self.frame_timer.end_frame_signal.connect(self.frame_timer.end_frame_event)
        self.frame_timer.update_frame_signal.connect(self.update_frame)
        self.frame_timer.start()

    def update_frame(self):
        screen = self.env.get_screen()
        qimage = QImage(screen, screen.shape[1], screen.shape[0], QImage.Format.Format_RGB888)
        pixmap = QPixmap(qimage)
        pixmap = pixmap.scaled(self.screen_width, self.screen_height, Qt.AspectRatioMode.IgnoreAspectRatio)
        self.screen_label.setPixmap(pixmap)

        self.update()

    def paintEvent(self, event):
        if not self.frame_timer.next_frame_ready:
            return
        self.frame_timer.next_frame_ready = False

        ram = self.env.get_ram()
        if ram[0x001D] == 3 or ram[0x0E] in (0x0B, 0x06) or ram[0xB5] == 2:
            if ram[0x001D] == 3:
                pass
            self.env.reset()
        else:
            press_buttons = np.array([self.key_b, 0, 0, 0, self.key_up, self.key_down, self.key_left, self.key_right, self.key_a])
            self.env.step(press_buttons)

        self.frame_timer.end_frame_signal.emit()

        try:
            self.main.mario_tile_map.update()
            self.main.mario_key_viewer.update()
        except:
            pass

    def keyPressEvent(self, event):
        if event.isAutoRepeat():
            return

        key = event.key()
        if key == Qt.Key.Key_Up:
            self.key_up = True
        if key == Qt.Key.Key_Down:
            self.key_down = True
        if key == Qt.Key.Key_Left:
            self.key_left = True
        if key == Qt.Key.Key_Right:
            self.key_right = True
        if key == Qt.Key.Key_A:
            self.key_a = True
        if key == Qt.Key.Key_B:
            self.key_b = True

        if key == Qt.Key.Key_Escape:
            self.main.close_mario()

    def keyReleaseEvent(self, event):
        if event.isAutoRepeat():
            return

        key = event.key()
        if key == Qt.Key.Key_Up:
            self.key_up = False
        if key == Qt.Key.Key_Down:
            self.key_down = False
        if key == Qt.Key.Key_Left:
            self.key_left = False
        if key == Qt.Key.Key_Right:
            self.key_right = False
        if key == Qt.Key.Key_A:
            self.key_a = False
        if key == Qt.Key.Key_B:
            self.key_b = False

    def closeEvent(self, event):
        self.main.close_mario()


class MarioTileMap(QWidget):
    def __init__(self, main):
        super().__init__()
        self.setWindowTitle('Tile Map')
        self.main = main

        self.setFixedSize(16 * 20, 13 * 20)
        self.move(560, 100)

        self.show()

    def paintEvent(self, e):
        painter = QPainter()
        painter.begin(self)

        try:
            ram = self.main.mario.env.get_ram()

            full_screen_tiles = ram[0x0500:0x069F + 1]
            full_screen_tile_count = full_screen_tiles.shape[0]

            full_screen_page1_tiles = full_screen_tiles[:full_screen_tile_count // 2].reshape((-1, 16))
            full_screen_page2_tiles = full_screen_tiles[full_screen_tile_count // 2:].reshape((-1, 16))

            full_screen_tiles = np.concatenate((full_screen_page1_tiles, full_screen_page2_tiles), axis=1).astype(np.int)

            enemy_drawn = ram[0x000F:0x0014]
            enemy_horizontal_position_in_level = ram[0x006E:0x0072 + 1]
            enemy_x_position_on_screen = ram[0x0087:0x008B + 1]
            enemy_y_position_on_screen = ram[0x00CF:0x00D3 + 1]

            for i in range(5):
                if enemy_drawn[i] == 1:
                    ex = (((enemy_horizontal_position_in_level[i] * 256) + enemy_x_position_on_screen[i]) % 512 + 8) // 16
                    ey = (enemy_y_position_on_screen[i] - 8) // 16 - 1
                    if 0 <= ex < full_screen_tiles.shape[1] and 0 <= ey < full_screen_tiles.shape[0]:
                        full_screen_tiles[ey][ex] = -1

            current_screen_in_level = ram[0x071A]
            screen_x_position_in_level = ram[0x071C]
            screen_x_position_offset = (256 * current_screen_in_level + screen_x_position_in_level) % 512
            sx = screen_x_position_offset // 16

            screen_tiles = np.concatenate((full_screen_tiles, full_screen_tiles), axis=1)[:, sx:sx + 16]

            painter.setPen(QPen(Qt.GlobalColor.black, 2, Qt.PenStyle.SolidLine))
            for i in range(screen_tiles.shape[0]):
                for j in range(screen_tiles.shape[1]):
                    if screen_tiles[i][j] > 0:
                        screen_tiles[i][j] = 1
                    if screen_tiles[i][j] == -1:
                        screen_tiles[i][j] = 2
                        painter.setBrush(QBrush(Qt.GlobalColor.red))
                    else:
                        painter.setBrush(QBrush(QColor.fromHslF(125 / 239, 0 if screen_tiles[i][j] == 0 else 1, 120 / 240)))
                    painter.drawRect(20 * j, 20 * i, 20, 20)

            player_x_position_current_screen_offset = ram[0x03AD]
            player_y_position_current_screen_offset = ram[0x03B8]
            px = (player_x_position_current_screen_offset + 8) // 16
            py = (player_y_position_current_screen_offset + 8) // 16 - 1
            painter.setBrush(QBrush(Qt.GlobalColor.blue))
            painter.drawRect(20 * px, 20 * py, 20, 20)
        except:
            pass

        painter.end()

    def closeEvent(self, event):
        self.main.close_mario()

    def keyPressEvent(self, event):
        if event.isAutoRepeat():
            return

        key = event.key()
        if key == Qt.Key.Key_Escape:
            self.main.close_mario()


class MarioKeyViewer(QWidget):
    def __init__(self, main):
        super().__init__()
        self.setWindowTitle('Key Viewer')
        self.main = main

        self.setFixedSize(320, 180)
        self.move(560, 400)

        self.show()

    def paintEvent(self, e):
        painter = QPainter()
        painter.begin(self)

        try:
            painter.setPen(QPen(Qt.GlobalColor.black, 2, Qt.PenStyle.SolidLine))
            painter.setBrush(QBrush(Qt.GlobalColor.red if self.main.mario.key_a else Qt.GlobalColor.white))
            painter.drawRect(30, 40, 40, 40)
            painter.setPen(QPen(Qt.GlobalColor.white if self.main.mario.key_a else Qt.GlobalColor.black, 2, Qt.PenStyle.SolidLine))
            painter.drawText(30 + 16, 40 + 24, 'A')

            painter.setPen(QPen(Qt.GlobalColor.black, 2, Qt.PenStyle.SolidLine))
            painter.setBrush(QBrush(Qt.GlobalColor.red if self.main.mario.key_b else Qt.GlobalColor.white))
            painter.drawRect(80, 90, 40, 40)
            painter.setPen(QPen(Qt.GlobalColor.white if self.main.mario.key_b else Qt.GlobalColor.black, 2, Qt.PenStyle.SolidLine))
            painter.drawText(80 + 16, 90 + 24, 'B')

            painter.setPen(QPen(Qt.GlobalColor.black, 2, Qt.PenStyle.SolidLine))
            painter.setBrush(QBrush(Qt.GlobalColor.red if self.main.mario.key_up else Qt.GlobalColor.white))
            painter.drawRect(200, 40, 40, 40)
            painter.setPen(QPen(Qt.GlobalColor.white if self.main.mario.key_up else Qt.GlobalColor.black, 2, Qt.PenStyle.SolidLine))
            painter.drawText(200 + 14, 40 + 24, '↑')

            painter.setPen(QPen(Qt.GlobalColor.black, 2, Qt.PenStyle.SolidLine))
            painter.setBrush(QBrush(Qt.GlobalColor.red if self.main.mario.key_down else Qt.GlobalColor.white))
            painter.drawRect(200, 90, 40, 40)
            painter.setPen(QPen(Qt.GlobalColor.white if self.main.mario.key_down else Qt.GlobalColor.black, 2, Qt.PenStyle.SolidLine))
            painter.drawText(200 + 14, 90 + 24, '↓')

            painter.setPen(QPen(Qt.GlobalColor.black, 2, Qt.PenStyle.SolidLine))
            painter.setBrush(QBrush(Qt.GlobalColor.red if self.main.mario.key_left else Qt.GlobalColor.white))
            painter.drawRect(150, 90, 40, 40)
            painter.setPen(QPen(Qt.GlobalColor.white if self.main.mario.key_left else Qt.GlobalColor.black, 2, Qt.PenStyle.SolidLine))
            painter.drawText(150 + 14, 90 + 24, '←')

            painter.setPen(QPen(Qt.GlobalColor.black, 2, Qt.PenStyle.SolidLine))
            painter.setBrush(QBrush(Qt.GlobalColor.red if self.main.mario.key_right else Qt.GlobalColor.white))
            painter.drawRect(250, 90, 40, 40)
            painter.setPen(QPen(Qt.GlobalColor.white if self.main.mario.key_right else Qt.GlobalColor.black, 2, Qt.PenStyle.SolidLine))
            painter.drawText(250 + 14, 90 + 24, '→')
        except:
            pass

        painter.end()

    def closeEvent(self, event):
        self.main.close_mario()

    def keyPressEvent(self, event):
        if event.isAutoRepeat():
            return

        key = event.key()
        if key == Qt.Key.Key_Escape:
            self.main.close_mario()


warnings.filterwarnings('error')


def relu(x):
    return np.maximum(0, x)


def sigmoid(x):
    return 1.0 / (1.0 + np.exp(-np.maximum(-700, x)))


class Chromosome:
    def __init__(self, layer, layer_size):
        self.w = []
        self.b = []

        self.layer = layer
        self.layer_size = [80] + layer_size + [6]

        for i in range(layer):
            self.w.append(np.random.uniform(low=-1, high=1, size=(self.layer_size[i], self.layer_size[i + 1])))
            self.b.append(np.random.uniform(low=-1, high=1, size=(self.layer_size[i + 1],)))

        self.l = [None for i in range(self.layer - 1)]

        self.distance = 0
        self.max_distance = 0
        self.frames = 0
        self.stop_frames = 0
        self.win = 0

    def predict(self, data):
        for i in range(self.layer - 1):
            if i == 0:
                self.l[i] = relu(np.matmul(data, self.w[i]) + self.b[i])
            else:
                self.l[i] = relu(np.matmul(self.l[i - 1], self.w[i]) + self.b[i])
        output = sigmoid(np.matmul(self.l[-1], self.w[-1]) + self.b[-1])
        result = (output > 0.5).astype(np.int)
        return result

    def fitness(self):
        return int(max(self.distance ** 1.8 - self.frames ** 1.5 + min(max(self.distance - 50, 0), 1) * 2500 + self.win * 1000000, 1))


class GeneticAlgorithm:
    def __init__(self, main, select_folder_name, replay_generation):
        self.main = main
        self.select_folder_name = select_folder_name

        folder = os.path.join(DATA_PATH, select_folder_name)

        self.network = [0, 0, 1, 0]
        network_file_path = os.path.join(folder, 'network.npy')
        if os.path.exists(network_file_path):
            self.network = np.load(network_file_path)

        self.layer = [2, 3, 4][self.network[0]]
        self.layer_size = []
        if self.layer == 2:
            self.layer_size = [11]
        elif self.layer == 3:
            self.layer_size = [16, 8]
        elif self.layer == 4:
            self.layer_size = [32, 16, 8]
        elif self.layer == 5:
            self.layer_size = [64, 32, 16, 8]
        else:
            self.layer_size = []
        self.generation_size = [10, 20, 30, 40, 50][self.network[1]]
        self.elitist_preserve_rate = [0, 0.1, 0.2, 0.3, 0.4][self.network[2]]
        self.static_mutation_rate = [0.05, 0.1, 0.15, 0.2, 0.25][self.network[3]]

        self.generation = 0
        if replay_generation == -1:
            generation_file_path = os.path.join(folder, 'generation.npy')
            if os.path.exists(generation_file_path):
                self.generation = np.load(generation_file_path)[0]
        else:
            self.generation = replay_generation

        self.fitness = []
        fitness_file_path = os.path.join(folder, 'fitness.npy')
        if os.path.exists(fitness_file_path):
            if replay_generation == -1:
                self.fitness = np.load(fitness_file_path)[:-1]
            else:
                self.fitness = np.load(fitness_file_path)

        self.chromosomes = []

        for i in range(self.generation_size):
            chromosome = Chromosome(self.layer, self.layer_size)
            if os.path.exists(os.path.join(folder, str(self.generation))):
                for j in range(self.layer):
                    chromosome.w[j] = np.load(os.path.join(DATA_PATH, select_folder_name, str(self.generation), str(i), f'w{j}.npy'))
                    chromosome.b[j] = np.load(os.path.join(DATA_PATH, select_folder_name, str(self.generation), str(i), f'b{j}.npy'))
            self.chromosomes.append(chromosome)

        self.current_chromosome_index = 0

    def elitist_preserve_selection(self):
        sort_chromosomes = sorted(self.chromosomes, key=lambda x: x.fitness(), reverse=True)
        self.fitness = np.append(self.fitness, sort_chromosomes[0].fitness())
        return sort_chromosomes[:int(self.generation_size * self.elitist_preserve_rate)]

    def roulette_wheel_selection(self):
        result = []
        fitness_sum = sum(c.fitness() for c in self.chromosomes)
        for _ in range(2):
            pick = random.uniform(0, fitness_sum)
            current = 0
            for chromosome in self.chromosomes:
                current += chromosome.fitness()
                if current > pick:
                    result.append(chromosome)
                    break
        return result

    def SBX(self, p1, p2):
        rand = np.random.random(p1.shape)
        gamma = np.empty(p1.shape)
        gamma[rand <= 0.5] = (2 * rand[rand <= 0.5]) ** (1.0 / (100 + 1))
        gamma[rand > 0.5] = (1.0 / (2.0 * (1.0 - rand[rand > 0.5]))) ** (1.0 / (100 + 1))
        c1 = 0.5 * ((1 + gamma) * p1 + (1 - gamma) * p2)
        c2 = 0.5 * ((1 - gamma) * p1 + (1 + gamma) * p2)
        return c1, c2

    def crossover(self, chromosome1, chromosome2):
        child1 = Chromosome(self.layer, self.layer_size)
        child2 = Chromosome(self.layer, self.layer_size)

        for i in range(self.layer):
            child1.w[i], child2.w[i] = self.SBX(chromosome1.w[i], chromosome2.w[i])
            child1.b[i], child2.b[i] = self.SBX(chromosome1.b[i], chromosome2.b[i])

        return child1, child2

    def static_mutation(self, data):
        mutation_array = np.random.random(data.shape) < self.static_mutation_rate
        gaussian_mutation = np.random.normal(size=data.shape)
        data[mutation_array] += gaussian_mutation[mutation_array]

    def mutation(self, chromosome):
        for i in range(self.layer):
            self.static_mutation(chromosome.w[i])
            self.static_mutation(chromosome.b[i])

    def next_generation(self):
        folder = os.path.join(DATA_PATH, self.select_folder_name)

        generation_data_path = os.path.join(folder, str(self.generation))
        if not os.path.exists(generation_data_path):
            os.mkdir(generation_data_path)

        for i in range(self.generation_size):
            chromosome_data_path = os.path.join(generation_data_path, str(i))
            if not os.path.exists(chromosome_data_path):
                os.mkdir(chromosome_data_path)
            for j in range(self.layer):
                np.save(os.path.join(chromosome_data_path, f'w{j}.npy'), self.chromosomes[i].w[j])
                np.save(os.path.join(chromosome_data_path, f'b{j}.npy'), self.chromosomes[i].b[j])
                np.save(os.path.join(chromosome_data_path, f'fitness.npy'), np.array([self.chromosomes[i].fitness()]))

        np.save(os.path.join(folder, 'generation.npy'), np.array([self.generation]))

        next_chromosomes = []
        next_chromosomes.extend(self.elitist_preserve_selection())

        np.save(os.path.join(folder, 'fitness.npy'), self.fitness)

        while len(next_chromosomes) < self.generation_size:
            selected_chromosome = self.roulette_wheel_selection()

            child_chromosome1, child_chromosome2 = self.crossover(selected_chromosome[0], selected_chromosome[1])
            self.mutation(child_chromosome1)
            self.mutation(child_chromosome2)

            next_chromosomes.append(child_chromosome1)
            if len(next_chromosomes) == self.generation_size:
                break
            next_chromosomes.append(child_chromosome2)

        self.chromosomes = next_chromosomes
        for c in self.chromosomes:
            c.distance = 0
            c.max_distance = 0
            c.frames = 0
            c.stop_frames = 0
            c.win = 0
        self.generation += 1
        self.current_chromosome_index = 0

    def replay_generation(self):
        for c in self.chromosomes:
            c.distance = 0
            c.max_distance = 0
            c.frames = 0
            c.stop_frames = 0
            c.win = 0
        self.current_chromosome_index = 0

    def replay_mario(self, index):
        for c in self.chromosomes:
            c.distance = 0
            c.max_distance = 0
            c.frames = 0
            c.stop_frames = 0
            c.win = 0
        self.current_chromosome_index = index


class MarioAI(QWidget):
    def __init__(self, main, game_level, game_speed, select_folder_name, replay_generation=-1):
        super().__init__()
        name = np.load(os.path.join(DATA_PATH, select_folder_name, 'name.npy'))[0]
        self.setWindowTitle(name)
        self.main = main
        self.game_speed = game_speed
        self.replay_generation = replay_generation

        self.ga = GeneticAlgorithm(main, select_folder_name, replay_generation)

        self.elite_fitness = 0
        if len(self.ga.fitness):
            self.elite_fitness = self.ga.fitness[-1]
        self.current_fitness = 0

        global env
        if env is not None:
            env.close()
        env = retro.make(game='SuperMarioBros-Nes', state=f'Level{game_level + 1}-1')
        self.env = env
        screen = self.env.reset()

        self.screen_width = screen.shape[0] * 2
        self.screen_height = screen.shape[1] * 2

        self.setFixedSize(self.screen_width, self.screen_height)
        self.move(400, 100)

        self.screen_label = QLabel(self)
        self.screen_label.setGeometry(0, 0, self.screen_width, self.screen_height)

        self.press_buttons = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0])
        self.predict = np.array([0, 0, 0, 0, 0, 0])

        self.frame_timer = FrameTimer(self.game_speed)
        self.frame_timer.end_frame_signal.connect(self.frame_timer.end_frame_event)
        self.frame_timer.update_frame_signal.connect(self.update_frame)
        self.frame_timer.start()

        screen = self.env.get_screen()
        qimage = QImage(screen, screen.shape[1], screen.shape[0], QImage.Format.Format_RGB888)
        pixmap = QPixmap(qimage)
        pixmap = pixmap.scaled(self.screen_width, self.screen_height, Qt.AspectRatioMode.IgnoreAspectRatio)
        self.screen_label.setPixmap(pixmap)

    def update_frame(self):
        screen = self.env.get_screen()
        qimage = QImage(screen, screen.shape[1], screen.shape[0], QImage.Format.Format_RGB888)
        pixmap = QPixmap(qimage)
        pixmap = pixmap.scaled(self.screen_width, self.screen_height, Qt.AspectRatioMode.IgnoreAspectRatio)
        self.screen_label.setPixmap(pixmap)

        self.update()

    def paintEvent(self, event):
        if not self.frame_timer.next_frame_ready:
            return
        self.frame_timer.next_frame_ready = False

        ram = self.env.get_ram()

        full_screen_tiles = ram[0x0500:0x069F + 1]
        full_screen_tile_count = full_screen_tiles.shape[0]

        full_screen_page1_tiles = full_screen_tiles[:full_screen_tile_count // 2].reshape((-1, 16))
        full_screen_page2_tiles = full_screen_tiles[full_screen_tile_count // 2:].reshape((-1, 16))

        full_screen_tiles = np.concatenate((full_screen_page1_tiles, full_screen_page2_tiles), axis=1).astype(np.int)

        enemy_drawn = ram[0x000F:0x0014]
        enemy_horizontal_position_in_level = ram[0x006E:0x0072 + 1]
        enemy_x_position_on_screen = ram[0x0087:0x008B + 1]
        enemy_y_position_on_screen = ram[0x00CF:0x00D3 + 1]

        for i in range(5):
            if enemy_drawn[i] == 1:
                ex = (((enemy_horizontal_position_in_level[i] * 256) + enemy_x_position_on_screen[i]) % 512 + 8) // 16
                ey = (enemy_y_position_on_screen[i] - 8) // 16 - 1
                if 0 <= ex < full_screen_tiles.shape[1] and 0 <= ey < full_screen_tiles.shape[0]:
                    full_screen_tiles[ey][ex] = -1

        current_screen_in_level = ram[0x071A]
        screen_x_position_in_level = ram[0x071C]
        screen_x_position_offset = (256 * current_screen_in_level + screen_x_position_in_level) % 512
        sx = screen_x_position_offset // 16

        screen_tiles = np.concatenate((full_screen_tiles, full_screen_tiles), axis=1)[:, sx:sx + 16]

        for i in range(screen_tiles.shape[0]):
            for j in range(screen_tiles.shape[1]):
                if screen_tiles[i][j] > 0:
                    screen_tiles[i][j] = 1
                if screen_tiles[i][j] == -1:
                    screen_tiles[i][j] = 2

        player_x_position_current_screen_offset = ram[0x03AD]
        player_y_position_current_screen_offset = ram[0x03B8]
        px = (player_x_position_current_screen_offset + 8) // 16
        py = (player_y_position_current_screen_offset + 8) // 16 - 1

        ix = px
        if ix + 8 > screen_tiles.shape[1]:
            ix = screen_tiles.shape[1] - 8
        iy = 2

        input_data = screen_tiles[iy:iy + 10, ix:ix + 8]

        if 2 <= py <= 11:
            input_data[py - 2][0] = 2

        input_data = input_data.flatten()

        current_chromosome = self.ga.chromosomes[self.ga.current_chromosome_index]
        current_chromosome.frames += 1
        current_chromosome.distance = ram[0x006D] * 256 + ram[0x0086]

        if current_chromosome.max_distance < current_chromosome.distance:
            current_chromosome.max_distance = current_chromosome.distance
            current_chromosome.stop_frame = 0
        else:
            current_chromosome.stop_frame += 1

        if ram[0x001D] == 3 or ram[0x0E] in (0x0B, 0x06) or ram[0xB5] == 2 or current_chromosome.stop_frame > 180:
            if ram[0x001D] == 3:
                current_chromosome.win = 1

            self.current_fitness = current_chromosome.fitness()

            if self.elite_fitness < self.current_fitness:
                self.elite_fitness = self.current_fitness

            try:
                if self.main.mario_ai_info.fitness_list_widget.count() <= self.ga.current_chromosome_index:
                    self.main.mario_ai_info.fitness_list_widget.addItem(f'{self.ga.current_chromosome_index + 1}번: {self.current_fitness}')
                    self.main.mario_ai_info.fitness_list_widget.scrollToBottom()
                    self.main.mario_ai_info.elite_fitness_label.setText(f'{self.elite_fitness}')
            except:
                pass

            self.ga.current_chromosome_index += 1

            if self.ga.current_chromosome_index == self.ga.generation_size:
                if self.replay_generation == -1:
                    try:
                        self.main.mario_ai_info.fitness_list_widget.clear()
                    except:
                        pass

                    self.ga.next_generation()

                    try:
                        self.main.mario_ai_graph.update()
                    except:
                        pass
                else:
                    self.ga.replay_generation()

            self.env.reset()
        else:
            self.predict = current_chromosome.predict(input_data)
            self.press_buttons = np.array([self.predict[5], 0, 0, 0, self.predict[0], self.predict[1], self.predict[2], self.predict[3], self.predict[4]])
            self.env.step(self.press_buttons)

        self.frame_timer.end_frame_signal.emit()

        try:
            self.main.mario_ai_tile_map.update()
            self.main.mario_ai_info.generation_label.setText(f'{self.ga.generation} 세대')
            self.main.mario_ai_info.current_chromosome_index_label.setText(f'{self.ga.current_chromosome_index + 1} / {self.ga.generation_size}')
            self.current_fitness = current_chromosome.fitness()
            self.main.mario_ai_info.elite_fitness_label.setText(f'{self.current_fitness if self.elite_fitness < self.current_fitness else self.elite_fitness}')
            self.main.mario_ai_info.fitness_label.setText(f'{self.current_fitness}')
            self.main.mario_ai_network.update()
        except:
            pass

    def keyPressEvent(self, event):
        if event.isAutoRepeat():
            return

        key = event.key()
        if key == Qt.Key.Key_Escape:
            self.main.close_mario_ai()

    def closeEvent(self, event):
        self.main.close_mario_ai()


class MarioAIListTool(QWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main

        self.current_ai = None

        self.ai_list = os.listdir(DATA_PATH)
        self.ai_list.reverse()
        self.ai_list_widget = QListWidget()
        for ai in self.ai_list:
            name = np.load(os.path.join(DATA_PATH, ai, 'name.npy'))[0]
            self.ai_list_widget.addItem(name)
        self.ai_list_widget.clicked.connect(self.change_current_ai)

        self.select_button = QPushButton('선택')
        self.select_button.clicked.connect(self.select_ai)

        self.form_layout = QFormLayout()

        self.generation_label = QLabel()
        self.elite_fitness_label = QLabel()

        self.layer_label = QLabel()
        self.generation_size_label = QLabel()
        self.elitist_preserve_rate_label = QLabel()
        self.static_mutation_rate_label = QLabel()

        self.form_layout.addRow("학습된 세대: ", self.generation_label)
        self.form_layout.addRow("엘리트 적합도: ", self.elite_fitness_label)
        self.form_layout.addRow("신경망 크기: ", self.layer_label)
        self.form_layout.addRow("세대 크기: ", self.generation_size_label)
        self.form_layout.addRow("엘리트 보존: ", self.elitist_preserve_rate_label)
        self.form_layout.addRow("변이: ", self.static_mutation_rate_label)

        ai_list_layout = QVBoxLayout()
        ai_list_layout.addWidget(self.ai_list_widget)
        ai_list_layout.addWidget(self.select_button)
        ai_list_layout.addLayout(self.form_layout)

        self.setLayout(ai_list_layout)

    def change_current_ai(self):
        self.current_ai = self.ai_list_widget.currentRow()

        network = np.load(os.path.join(DATA_PATH, self.ai_list[self.current_ai], 'network.npy'))

        if os.path.exists(os.path.join(DATA_PATH, self.ai_list[self.current_ai], 'generation.npy')):
            generation = np.load(os.path.join(DATA_PATH, self.ai_list[self.current_ai], 'generation.npy'))[0]
            self.generation_label.setText(f'{generation}세대')
        else:
            self.generation_label.setText('없음')

        if os.path.exists(os.path.join(DATA_PATH, self.ai_list[self.current_ai], 'fitness.npy')):
            elite_fitness = np.load(os.path.join(DATA_PATH, self.ai_list[self.current_ai], 'fitness.npy'))[-1]
            self.elite_fitness_label.setText(f'{elite_fitness}')
        else:
            self.elite_fitness_label.setText('없음')

        self.layer_label.setText(['2', '3', '4'][network[0]])
        self.generation_size_label.setText(['10', '20', '30', '40', '50'][network[1]])
        self.elitist_preserve_rate_label.setText(['0%', '10%', '20%', '30%', '40%'][network[2]])
        self.static_mutation_rate_label.setText(['5%', '10%', '15%', '20%', '25%'][network[3]])

    def select_ai(self):
        if self.current_ai is not None:
            self.main.close_mario_ai()
            self.main.run_mario_ai(self.ai_list[self.current_ai])


class MarioAICreateTool(QWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main

        form_layout = QFormLayout()

        self.ai_name_line_edit = QLineEdit()

        self.layer_combo_box = QComboBox()
        self.layer_combo_box.addItem('2')
        self.layer_combo_box.addItem('3')
        self.layer_combo_box.addItem('4')

        self.generation_size_combo_box = QComboBox()
        self.generation_size_combo_box.addItem('10')
        self.generation_size_combo_box.addItem('20')
        self.generation_size_combo_box.addItem('30')
        self.generation_size_combo_box.addItem('40')
        self.generation_size_combo_box.addItem('50')

        self.elitist_preserve_rate_combo_box = QComboBox()
        self.elitist_preserve_rate_combo_box.addItem('0%')
        self.elitist_preserve_rate_combo_box.addItem('10%')
        self.elitist_preserve_rate_combo_box.addItem('20%')
        self.elitist_preserve_rate_combo_box.addItem('30%')
        self.elitist_preserve_rate_combo_box.addItem('40%')
        self.elitist_preserve_rate_combo_box.setCurrentIndex(1)

        self.static_mutation_rate_combo_box = QComboBox()
        self.static_mutation_rate_combo_box.addItem('5%')
        self.static_mutation_rate_combo_box.addItem('10%')
        self.static_mutation_rate_combo_box.addItem('15%')
        self.static_mutation_rate_combo_box.addItem('20%')
        self.static_mutation_rate_combo_box.addItem('25%')

        create_ai_button = QPushButton("생성")
        create_ai_button.clicked.connect(self.create_ai)

        form_layout.addRow("이름: ", self.ai_name_line_edit)
        form_layout.addRow("신경망 크기: ", self.layer_combo_box)
        form_layout.addRow("세대 크기: ", self.generation_size_combo_box)
        form_layout.addRow("엘리트 보존: ", self.elitist_preserve_rate_combo_box)
        form_layout.addRow("변이: ", self.static_mutation_rate_combo_box)
        form_layout.addRow("", create_ai_button)

        self.setLayout(form_layout)

    def create_ai(self):
        folder_name = datetime.datetime.now().strftime("%Y-%m-%dT%H-%M-%S-%fZ")
        os.mkdir(os.path.join(DATA_PATH, folder_name))

        name = self.ai_name_line_edit.text()
        layer = self.layer_combo_box.currentIndex()
        generation_size = self.generation_size_combo_box.currentIndex()
        elitist_preserve_rate = self.elitist_preserve_rate_combo_box.currentIndex()
        static_mutation_rate = self.static_mutation_rate_combo_box.currentIndex()

        network = [layer, generation_size, elitist_preserve_rate, static_mutation_rate]

        if len(name) == 0:
            name = f'{[2, 3, 4][network[0]]}-{[10, 20, 30, 40, 50][network[1]]}-{[0, 10, 20, 30, 40][network[2]]}%-{[5, 10, 15, 20, 25][network[3]]}%'

        np.save(os.path.join(DATA_PATH, folder_name, 'network.npy'), np.array([layer, generation_size, elitist_preserve_rate, static_mutation_rate]))
        np.save(os.path.join(DATA_PATH, folder_name, 'name.npy'), np.array([name]))

        try:
            self.main.mario_ai_tool_box.mario_ai_list_tool.ai_list.insert(0, folder_name)
            self.main.mario_ai_tool_box.mario_ai_list_tool.ai_list_widget.insertItem(0, name)
            self.main.mario_ai_tool_box.tabs.setCurrentIndex(0)
        except:
            pass


class MarioAIToolBox(QWidget):
    def __init__(self, main):
        super().__init__()
        self.setWindowTitle('AI Tool Box')
        self.main = main

        self.setFixedSize(290, 480)
        self.move(100, 100)

        self.mario_ai_list_tool = MarioAIListTool(main)
        self.mario_ai_create_tool = MarioAICreateTool(main)

        self.tabs = QTabWidget()
        self.tabs.addTab(self.mario_ai_list_tool, 'AI 목록')
        self.tabs.addTab(self.mario_ai_create_tool, 'AI 생성')

        if len(self.mario_ai_list_tool.ai_list) == 0:
            self.tabs.setCurrentIndex(1)

        vbox = QVBoxLayout()
        vbox.addWidget(self.tabs)

        self.setLayout(vbox)

    def closeEvent(self, event):
        self.main.close_mario_ai_tool_box()

    def keyPressEvent(self, event):
        if event.isAutoRepeat():
            return

        key = event.key()
        if key == Qt.Key.Key_Escape:
            self.main.close_mario_ai_tool_box()


class MarioAITileMap(QWidget):
    def __init__(self, main):
        super().__init__()
        self.setWindowTitle('Tile Map')
        self.main = main

        self.setFixedSize(16 * 20, 13 * 20)
        self.move(860, 100)

        self.show()

    def paintEvent(self, e):
        painter = QPainter()
        painter.begin(self)

        try:
            ram = self.main.mario_ai.env.get_ram()

            full_screen_tiles = ram[0x0500:0x069F + 1]
            full_screen_tile_count = full_screen_tiles.shape[0]

            full_screen_page1_tiles = full_screen_tiles[:full_screen_tile_count // 2].reshape((-1, 16))
            full_screen_page2_tiles = full_screen_tiles[full_screen_tile_count // 2:].reshape((-1, 16))

            full_screen_tiles = np.concatenate((full_screen_page1_tiles, full_screen_page2_tiles), axis=1).astype(np.int)

            enemy_drawn = ram[0x000F:0x0014]
            enemy_horizontal_position_in_level = ram[0x006E:0x0072 + 1]
            enemy_x_position_on_screen = ram[0x0087:0x008B + 1]
            enemy_y_position_on_screen = ram[0x00CF:0x00D3 + 1]

            for i in range(5):
                if enemy_drawn[i] == 1:
                    ex = (((enemy_horizontal_position_in_level[i] * 256) + enemy_x_position_on_screen[i]) % 512 + 8) // 16
                    ey = (enemy_y_position_on_screen[i] - 8) // 16 - 1
                    if 0 <= ex < full_screen_tiles.shape[1] and 0 <= ey < full_screen_tiles.shape[0]:
                        full_screen_tiles[ey][ex] = -1

            current_screen_in_level = ram[0x071A]
            screen_x_position_in_level = ram[0x071C]
            screen_x_position_offset = (256 * current_screen_in_level + screen_x_position_in_level) % 512
            sx = screen_x_position_offset // 16

            screen_tiles = np.concatenate((full_screen_tiles, full_screen_tiles), axis=1)[:, sx:sx + 16]

            painter.setPen(QPen(Qt.GlobalColor.black, 2, Qt.PenStyle.SolidLine))
            for i in range(screen_tiles.shape[0]):
                for j in range(screen_tiles.shape[1]):
                    if screen_tiles[i][j] > 0:
                        screen_tiles[i][j] = 1
                    if screen_tiles[i][j] == -1:
                        screen_tiles[i][j] = 2
                        painter.setBrush(QBrush(Qt.GlobalColor.red))
                    else:
                        painter.setBrush(QBrush(QColor.fromHslF(125 / 239, 0 if screen_tiles[i][j] == 0 else 1, 120 / 240)))
                    painter.drawRect(20 * j, 20 * i, 20, 20)

            player_x_position_current_screen_offset = ram[0x03AD]
            player_y_position_current_screen_offset = ram[0x03B8]
            px = (player_x_position_current_screen_offset + 8) // 16
            py = (player_y_position_current_screen_offset + 8) // 16 - 1
            painter.setBrush(QBrush(Qt.GlobalColor.blue))
            painter.drawRect(20 * px, 20 * py, 20, 20)
        except:
            pass

        painter.end()

    def closeEvent(self, event):
        self.main.close_mario_ai()

    def keyPressEvent(self, event):
        if event.isAutoRepeat():
            return

        key = event.key()
        if key == Qt.Key.Key_Escape:
            self.main.close_mario_ai()


class MarioAIInfo(QWidget):
    def __init__(self, main):
        super().__init__()
        self.main = main
        self.setWindowTitle('Info')

        self.setFixedSize(320, 180)
        self.move(860, 400)

        self.fitness_list_widget = QListWidget()
        self.fitness_list_widget.setFixedWidth(140)
        self.fitness_list_widget.clicked.connect(self.change_current_mario)

        self.form_layout = QFormLayout()

        self.generation_label = QLabel()
        self.current_chromosome_index_label = QLabel()
        self.elite_fitness_label = QLabel()
        self.fitness_label = QLabel()

        self.form_layout.addRow("현재 세대: ", self.generation_label)
        self.form_layout.addRow("현재 마리오: ", self.current_chromosome_index_label)
        self.form_layout.addRow("엘리트 적합도: ", self.elite_fitness_label)
        self.form_layout.addRow("현재 적합도: ", self.fitness_label)

        ai_list_layout = QHBoxLayout()
        ai_list_layout.addWidget(self.fitness_list_widget)
        ai_list_layout.addLayout(self.form_layout)

        self.setLayout(ai_list_layout)

        self.show()

    def change_current_mario(self):
        current_mario = self.fitness_list_widget.currentRow()

        try:
            if self.main.mario_ai.replay_generation != -1:
                self.main.mario_ai.ga.replay_mario(current_mario)
                self.main.mario_ai.env.reset()
        except:
            pass

    def closeEvent(self, event):
        self.main.close_mario_ai()

    def keyPressEvent(self, event):
        if event.isAutoRepeat():
            return

        key = event.key()
        if key == Qt.Key.Key_Escape:
            self.main.close_mario_ai()


class MarioAINetwork(QWidget):
    def __init__(self, main):
        super().__init__()
        self.setWindowTitle('Neural Network')
        self.main = main

        self.setFixedSize(480, 480)
        self.move(1190, 100)

    def paintEvent(self, e):
        painter = QPainter()
        painter.begin(self)

        try:
            if self.main.mario_ai.ga.layer == 2:
                for i in range(5):
                    painter.setPen(QPen(Qt.GlobalColor.red if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].w[0][0][i] > 0 else Qt.GlobalColor.blue, 2, Qt.PenStyle.SolidLine))
                    painter.drawLine(240 - 40 * (5 - i), 0, 240 - 40 * (5 - i), 240 - 100)
                    painter.setPen(QPen(Qt.GlobalColor.red if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].w[0][0][6 + i] > 0 else Qt.GlobalColor.blue, 2, Qt.PenStyle.SolidLine))
                    painter.drawLine(240 + 40 * (5 - i), 0, 240 + 40 * (5 - i), 240 - 100)
                painter.setPen(QPen(Qt.GlobalColor.red if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].w[0][0][5] > 0 else Qt.GlobalColor.blue, 2, Qt.PenStyle.SolidLine))
                painter.drawLine(240, 0, 240, 240 - 100)

                for i in range(5):
                    for j in range(3):
                        painter.setPen(QPen(Qt.GlobalColor.red if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].w[1][i][j] > 0 else Qt.GlobalColor.blue, 2, Qt.PenStyle.SolidLine))
                        painter.drawLine(240 - 40 * (5 - i), 240 - 100, 240 - 30 - 60 * (2 - j), 240 + 100)
                        painter.setPen(QPen(Qt.GlobalColor.red if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].w[1][6 + i][j] > 0 else Qt.GlobalColor.blue, 2, Qt.PenStyle.SolidLine))
                        painter.drawLine(240 + 40 * (5 - i), 240 - 100, 240 - 30 - 60 * (2 - j), 240 + 100)
                        painter.setPen(QPen(Qt.GlobalColor.red if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].w[1][i][3 + j] > 0 else Qt.GlobalColor.blue, 2, Qt.PenStyle.SolidLine))
                        painter.drawLine(240 - 40 * (5 - i), 240 - 100, 240 - 30 + 60 * (2 - j), 240 + 100)
                        painter.setPen(QPen(Qt.GlobalColor.red if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].w[1][6 + i][3 + j] > 0 else Qt.GlobalColor.blue, 2, Qt.PenStyle.SolidLine))
                        painter.drawLine(240 + 40 * (5 - i), 240 - 100, 240 + 30 + 60 * (2 - j), 240 + 100)

                for j in range(3):
                    painter.setPen(QPen(Qt.GlobalColor.red if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].w[1][5][j] > 0 else Qt.GlobalColor.blue, 2, Qt.PenStyle.SolidLine))
                    painter.drawLine(240, 240 - 100, 240 - 30 - 60 * (2 - j), 240 + 100)
                    painter.setPen(QPen(Qt.GlobalColor.red if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].w[1][5][3 + j] > 0 else Qt.GlobalColor.blue, 2, Qt.PenStyle.SolidLine))
                    painter.drawLine(240, 240 - 100, 240 + 30 + 60 * (2 - j), 240 + 100)

                painter.setPen(QPen(Qt.GlobalColor.black, 2, Qt.PenStyle.SolidLine))

                for i in range(5):
                    painter.setBrush(QBrush(QColor.fromHslF(125 / 239, 0 if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].l[0][i] > 0 else 1, 120 / 240)))
                    painter.drawEllipse(240 - 16 - 40 * (5 - i), 240 - 16 - 100, 16 * 2, 16 * 2)
                    painter.setBrush(QBrush(QColor.fromHslF(125 / 239, 0 if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].l[0][6 + i] > 0 else 1, 120 / 240)))
                    painter.drawEllipse(240 - 16 + 40 * (5 - i), 240 - 16 - 100, 16 * 2, 16 * 2)
                painter.setBrush(QBrush(QColor.fromHslF(125 / 239, 0 if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].l[0][5] > 0 else 1, 120 / 240)))
                painter.drawEllipse(240 - 16, 240 - 16 - 100, 16 * 2, 16 * 2)

                for i in range(3):
                    painter.setPen(QPen(Qt.GlobalColor.black, 2, Qt.PenStyle.SolidLine))
                    painter.setBrush(QBrush(QColor.fromHslF(0.8, 0 if self.main.mario_ai.predict[i] == 0 else 1, 0.8)))
                    painter.drawEllipse(240 - 16 - 30 - 60 * (2 - i), 240 - 16 + 100, 16 * 2, 16 * 2)
                    painter.setBrush(QBrush(QColor.fromHslF(0.8, 0 if self.main.mario_ai.predict[6 - 1 - i] == 0 else 1, 0.8)))
                    painter.drawEllipse(240 - 16 + 30 + 60 * (2 - i), 240 - 16 + 100, 16 * 2, 16 * 2)

                    painter.drawText(240 - 16 - 30 - 60 * (2 - i) + 12, 240 - 16 + 100 + 19, ('U', 'D', 'L', 'R', 'A', 'B')[i])
                    painter.drawText(240 - 16 + 30 + 60 * (2 - i) + 12, 240 - 16 + 100 + 19, ('U', 'D', 'L', 'R', 'A', 'B')[6 - 1 - i])
            elif self.main.mario_ai.ga.layer == 3:
                for i in range(3):
                    painter.setPen(QPen(Qt.GlobalColor.red if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].w[0][0][i] > 0 else Qt.GlobalColor.blue, 2, Qt.PenStyle.SolidLine))
                    painter.drawLine(240 - 40 * (5 - i), 0, 240 - 40 * (5 - i), 240 - 140)
                    painter.setPen(QPen(Qt.GlobalColor.red if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].w[0][0][16 - 1 - i] > 0 else Qt.GlobalColor.blue, 2, Qt.PenStyle.SolidLine))
                    painter.drawLine(240 + 40 * (5 - i), 0, 240 + 40 * (5 - i), 240 - 140)

                for i in range(3):
                    for j in range(4):
                        painter.setPen(QPen(Qt.GlobalColor.red if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].w[1][i][j] > 0 else Qt.GlobalColor.blue, 2, Qt.PenStyle.SolidLine))
                        painter.drawLine(240 - 40 * (5 - i), 240 - 140, 240 - 22 - 44 * (3 - j), 240)
                        painter.setPen(QPen(Qt.GlobalColor.red if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].w[1][16 - 1 - i][j] > 0 else Qt.GlobalColor.blue, 2, Qt.PenStyle.SolidLine))
                        painter.drawLine(240 + 40 * (5 - i), 240 - 140, 240 - 22 - 44 * (3 - j), 240)
                        painter.setPen(QPen(Qt.GlobalColor.red if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].w[1][i][4 + j] > 0 else Qt.GlobalColor.blue, 2, Qt.PenStyle.SolidLine))
                        painter.drawLine(240 - 40 * (5 - i), 240 - 140, 240 + 22 + 44 * (3 - j), 240)
                        painter.setPen(QPen(Qt.GlobalColor.red if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].w[1][16 - 1 - i][4 + j] > 0 else Qt.GlobalColor.blue, 2, Qt.PenStyle.SolidLine))
                        painter.drawLine(240 + 40 * (5 - i), 240 - 140, 240 + 22 + 44 * (3 - j), 240)

                for i in range(4):
                    for j in range(3):
                        painter.setPen(QPen(Qt.GlobalColor.red if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].w[2][i][j] > 0 else Qt.GlobalColor.blue, 2, Qt.PenStyle.SolidLine))
                        painter.drawLine(240 - 22 - 44 * (3 - i), 240, 240 - 25 - 50 * (2 - j), 240 + 140)
                        painter.setPen(QPen(Qt.GlobalColor.red if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].w[2][4 + i][j] > 0 else Qt.GlobalColor.blue, 2, Qt.PenStyle.SolidLine))
                        painter.drawLine(240 + 22 + 44 * (3 - i), 240, 240 - 25 - 50 * (2 - j), 240 + 140)
                        painter.setPen(QPen(Qt.GlobalColor.red if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].w[2][i][3 + j] > 0 else Qt.GlobalColor.blue, 2, Qt.PenStyle.SolidLine))
                        painter.drawLine(240 - 22 - 44 * (3 - i), 240, 240 + 25 + 50 * (2 - j), 240 + 140)
                        painter.setPen(QPen(Qt.GlobalColor.red if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].w[2][4 + i][3 + j] > 0 else Qt.GlobalColor.blue, 2, Qt.PenStyle.SolidLine))
                        painter.drawLine(240 + 22 + 44 * (3 - i), 240, 240 + 25 + 50 * (2 - j), 240 + 140)

                painter.setPen(QPen(Qt.GlobalColor.black, 2, Qt.PenStyle.SolidLine))

                for i in range(3):
                    painter.setBrush(QBrush(QColor.fromHslF(125 / 239, 0 if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].l[0][i] > 0 else 1, 120 / 240)))
                    painter.drawEllipse(240 - 16 - 40 * (5 - i), 240 - 16 - 140, 16 * 2, 16 * 2)
                    painter.setBrush(QBrush(QColor.fromHslF(125 / 239, 0 if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].l[0][16 - 1 - i] > 0 else 1, 120 / 240)))
                    painter.drawEllipse(240 - 16 + 40 * (5 - i), 240 - 16 - 140, 16 * 2, 16 * 2)

                painter.setBrush(QBrush(Qt.GlobalColor.black))
                painter.drawEllipse(240 - 4, 240 - 4 - 140, 4 * 2, 4 * 2)
                painter.drawEllipse(240 - 4 - 20, 240 - 4 - 140, 4 * 2, 4 * 2)
                painter.drawEllipse(240 - 4 + 20, 240 - 4 - 140, 4 * 2, 4 * 2)

                for i in range(4):
                    painter.setBrush(QBrush(QColor.fromHslF(125 / 239, 0 if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].l[1][i] > 0 else 1, 120 / 240)))
                    painter.drawEllipse(240 - 16 - 22 - 44 * (3 - i), 240 - 16, 16 * 2, 16 * 2)
                    painter.setBrush(QBrush(QColor.fromHslF(125 / 239, 0 if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].l[1][4 + i] > 0 else 1, 120 / 240)))
                    painter.drawEllipse(240 - 16 + 22 + 44 * (3 - i), 240 - 16, 16 * 2, 16 * 2)

                for i in range(3):
                    painter.setPen(QPen(Qt.GlobalColor.black, 2, Qt.PenStyle.SolidLine))
                    painter.setBrush(QBrush(QColor.fromHslF(0.8, 0 if self.main.mario_ai.predict[i] == 0 else 1, 0.8)))
                    painter.drawEllipse(240 - 16 - 25 - 50 * (2 - i), 240 - 16 + 140, 16 * 2, 16 * 2)
                    painter.setBrush(QBrush(QColor.fromHslF(0.8, 0 if self.main.mario_ai.predict[6 - 1 - i] == 0 else 1, 0.8)))
                    painter.drawEllipse(240 - 16 + 25 + 50 * (2 - i), 240 - 16 + 140, 16 * 2, 16 * 2)

                    painter.drawText(240 - 16 - 25 - 50 * (2 - i) + 12, 240 - 16 + 140 + 19, ('U', 'D', 'L', 'R', 'A', 'B')[i])
                    painter.drawText(240 - 16 + 25 + 50 * (2 - i) + 12, 240 - 16 + 140 + 19, ('U', 'D', 'L', 'R', 'A', 'B')[6 - 1 - i])
            elif self.main.mario_ai.ga.layer == 4:
                for i in range(3):
                    painter.setPen(QPen(Qt.GlobalColor.red if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].w[0][0][i] > 0 else Qt.GlobalColor.blue, 2, Qt.PenStyle.SolidLine))
                    painter.drawLine(240 - 40 * (5 - i), 0, 240 - 40 * (5 - i), 240 - 180)
                    painter.setPen(QPen(Qt.GlobalColor.red if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].w[0][0][32 - 1 - i] > 0 else Qt.GlobalColor.blue, 2, Qt.PenStyle.SolidLine))
                    painter.drawLine(240 + 40 * (5 - i), 0, 240 + 40 * (5 - i), 240 - 180)

                for i in range(3):
                    for j in range(3):
                        painter.setPen(QPen(Qt.GlobalColor.red if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].w[1][i][j] > 0 else Qt.GlobalColor.blue, 2, Qt.PenStyle.SolidLine))
                        painter.drawLine(240 - 40 * (5 - i), 240 - 180, 240 - 44 * (4 - j), 240 - 60)
                        painter.setPen(QPen(Qt.GlobalColor.red if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].w[1][32 - 1 - i][j] > 0 else Qt.GlobalColor.blue, 2, Qt.PenStyle.SolidLine))
                        painter.drawLine(240 + 40 * (5 - i), 240 - 180, 240 - 44 * (4 - j), 240 - 60)
                        painter.setPen(QPen(Qt.GlobalColor.red if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].w[1][i][16 - 1 - j] > 0 else Qt.GlobalColor.blue, 2, Qt.PenStyle.SolidLine))
                        painter.drawLine(240 - 40 * (5 - i), 240 - 180, 240 + 44 * (4 - j), 240 - 60)
                        painter.setPen(QPen(Qt.GlobalColor.red if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].w[1][32 - 1 - i][16 - 1 - j] > 0 else Qt.GlobalColor.blue, 2, Qt.PenStyle.SolidLine))
                        painter.drawLine(240 + 40 * (5 - i), 240 - 180, 240 + 44 * (4 - j), 240 - 60)

                for i in range(3):
                    for j in range(4):
                        painter.setPen(QPen(Qt.GlobalColor.red if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].w[2][i][j] > 0 else Qt.GlobalColor.blue, 2, Qt.PenStyle.SolidLine))
                        painter.drawLine(240 - 44 * (4 - i), 240 - 60, 240 - 22 - 44 * (3 - j), 240 + 60)
                        painter.setPen(QPen(Qt.GlobalColor.red if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].w[2][16 - 1 - i][j] > 0 else Qt.GlobalColor.blue, 2, Qt.PenStyle.SolidLine))
                        painter.drawLine(240 + 44 * (4 - i), 240 - 60, 240 - 22 - 44 * (3 - j), 240 + 60)
                        painter.setPen(QPen(Qt.GlobalColor.red if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].w[2][i][4 + j] > 0 else Qt.GlobalColor.blue, 2, Qt.PenStyle.SolidLine))
                        painter.drawLine(240 - 44 * (4 - i), 240 - 60, 240 + 22 + 44 * (3 - j), 240 + 60)
                        painter.setPen(QPen(Qt.GlobalColor.red if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].w[2][16 - 1 - i][4 + j] > 0 else Qt.GlobalColor.blue, 2, Qt.PenStyle.SolidLine))
                        painter.drawLine(240 + 44 * (4 - i), 240 - 60, 240 + 22 + 44 * (3 - j), 240 + 60)

                for i in range(4):
                    for j in range(3):
                        painter.setPen(QPen(Qt.GlobalColor.red if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].w[3][i][j] > 0 else Qt.GlobalColor.blue, 2, Qt.PenStyle.SolidLine))
                        painter.drawLine(240 - 22 - 44 * (3 - i), 240 + 60, 240 - 25 - 50 * (2 - j), 240 + 180)
                        painter.setPen(QPen(Qt.GlobalColor.red if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].w[3][4 + i][j] > 0 else Qt.GlobalColor.blue, 2, Qt.PenStyle.SolidLine))
                        painter.drawLine(240 + 22 + 44 * (3 - i), 240 + 60, 240 - 25 - 50 * (2 - j), 240 + 180)
                        painter.setPen(QPen(Qt.GlobalColor.red if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].w[3][i][3 + j] > 0 else Qt.GlobalColor.blue, 2, Qt.PenStyle.SolidLine))
                        painter.drawLine(240 - 22 - 44 * (3 - i), 240 + 60, 240 + 25 + 50 * (2 - j), 240 + 180)
                        painter.setPen(QPen(Qt.GlobalColor.red if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].w[3][4 + i][3 + j] > 0 else Qt.GlobalColor.blue, 2, Qt.PenStyle.SolidLine))
                        painter.drawLine(240 + 22 + 44 * (3 - i), 240 + 60, 240 + 25 + 50 * (2 - j), 240 + 180)

                painter.setPen(QPen(Qt.GlobalColor.black, 2, Qt.PenStyle.SolidLine))

                for i in range(3):
                    painter.setBrush(QBrush(QColor.fromHslF(125 / 239, 0 if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].l[0][i] > 0 else 1, 120 / 240)))
                    painter.drawEllipse(240 - 16 - 40 * (5 - i), 240 - 16 - 180, 16 * 2, 16 * 2)
                    painter.setBrush(QBrush(QColor.fromHslF(125 / 239, 0 if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].l[0][32 - 1 - i] > 0 else 1, 120 / 240)))
                    painter.drawEllipse(240 - 16 + 40 * (5 - i), 240 - 16 - 180, 16 * 2, 16 * 2)

                painter.setBrush(QBrush(Qt.GlobalColor.black))
                painter.drawEllipse(240 - 4, 240 - 4 - 180, 4 * 2, 4 * 2)
                painter.drawEllipse(240 - 4 - 30, 240 - 4 - 180, 4 * 2, 4 * 2)
                painter.drawEllipse(240 - 4 + 30, 240 - 4 - 180, 4 * 2, 4 * 2)

                for i in range(3):
                    painter.setBrush(QBrush(QColor.fromHslF(125 / 239, 0 if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].l[1][i] > 0 else 1, 120 / 240)))
                    painter.drawEllipse(240 - 16 - 44 * (4 - i), 240 - 16 - 60, 16 * 2, 16 * 2)
                    painter.setBrush(QBrush(QColor.fromHslF(125 / 239, 0 if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].l[1][16 - 1 - i] > 0 else 1, 120 / 240)))
                    painter.drawEllipse(240 - 16 + 44 * (4 - i), 240 - 16 - 60, 16 * 2, 16 * 2)

                painter.setBrush(QBrush(Qt.GlobalColor.black))
                painter.drawEllipse(240 - 4, 240 - 4 - 60, 4 * 2, 4 * 2)
                painter.drawEllipse(240 - 4 - 20, 240 - 4 - 60, 4 * 2, 4 * 2)
                painter.drawEllipse(240 - 4 + 20, 240 - 4 - 60, 4 * 2, 4 * 2)

                for i in range(4):
                    painter.setBrush(QBrush(QColor.fromHslF(125 / 239, 0 if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].l[2][i] > 0 else 1, 120 / 240)))
                    painter.drawEllipse(240 - 16 - 22 - 44 * (3 - i), 240 - 16 + 60, 16 * 2, 16 * 2)
                    painter.setBrush(QBrush(QColor.fromHslF(125 / 239, 0 if self.main.mario_ai.ga.chromosomes[self.main.mario_ai.ga.current_chromosome_index].l[2][4 + i] > 0 else 1, 120 / 240)))
                    painter.drawEllipse(240 - 16 + 22 + 44 * (3 - i), 240 - 16 + 60, 16 * 2, 16 * 2)

                for i in range(3):
                    painter.setPen(QPen(Qt.GlobalColor.black, 2, Qt.PenStyle.SolidLine))
                    painter.setBrush(QBrush(QColor.fromHslF(0.8, 0 if self.main.mario_ai.predict[i] == 0 else 1, 0.8)))
                    painter.drawEllipse(240 - 16 - 25 - 50 * (2 - i), 240 - 16 + 180, 16 * 2, 16 * 2)
                    painter.setBrush(QBrush(QColor.fromHslF(0.8, 0 if self.main.mario_ai.predict[6 - 1 - i] == 0 else 1, 0.8)))
                    painter.drawEllipse(240 - 16 + 25 + 50 * (2 - i), 240 - 16 + 180, 16 * 2, 16 * 2)

                    painter.drawText(240 - 16 - 25 - 50 * (2 - i) + 12, 240 - 16 + 180 + 19, ('U', 'D', 'L', 'R', 'A', 'B')[i])
                    painter.drawText(240 - 16 + 25 + 50 * (2 - i) + 12, 240 - 16 + 180 + 19, ('U', 'D', 'L', 'R', 'A', 'B')[6 - 1 - i])
        except:
            pass

        painter.end()

    def closeEvent(self, event):
        self.main.close_mario_ai()

    def keyPressEvent(self, event):
        if event.isAutoRepeat():
            return

        key = event.key()
        if key == Qt.Key.Key_Escape:
            self.main.close_mario_ai()


class MarioAIGraph(QWidget):
    def __init__(self, main):
        super().__init__()
        self.setWindowTitle('Graph')
        self.main = main

        self.setFixedSize(1570, 300)
        self.move(100, 620)

    def paintEvent(self, e):
        painter = QPainter()
        painter.begin(self)

        try:
            x_len = len(self.main.mario_ai.ga.fitness)
            y_max = 0

            if x_len >= 1:
                y_max = np.max(self.main.mario_ai.ga.fitness)

            px = -1
            py = -1

            painter.setPen(QPen(Qt.GlobalColor.blue, 2, Qt.PenStyle.SolidLine))
            for i in range(0, x_len):
                x = int(1560 * (i + 1) / x_len)
                y = int(280 * self.main.mario_ai.ga.fitness[i] / y_max)

                if px != -1:
                    painter.drawLine(px, 290 - py, x, 290 - y)

                px = x
                py = y

            painter.setPen(QPen(Qt.GlobalColor.red, 2, Qt.PenStyle.SolidLine))
            painter.setBrush(QBrush(Qt.GlobalColor.red))

            for i in range(0, x_len):
                x = int(1560 * (i + 1) / x_len)
                y = int(280 * self.main.mario_ai.ga.fitness[i] / y_max)

                if self.main.mario_ai.replay_generation == i:
                    painter.setPen(QPen(Qt.GlobalColor.green, 1, Qt.PenStyle.SolidLine))
                    painter.drawLine(0, 290 - y, 1570, 290 - y)
                    painter.drawLine(x, 0, x, 300)
                    painter.setPen(QPen(Qt.GlobalColor.red, 2, Qt.PenStyle.SolidLine))

                painter.drawEllipse(x - 2, 290 - y - 2, 2 * 2, 2 * 2)
        except:
            pass

        painter.end()

    def closeEvent(self, event):
        self.main.close_mario_ai()

    def keyPressEvent(self, event):
        if event.isAutoRepeat():
            return

        key = event.key()
        if key == Qt.Key.Key_Escape:
            self.main.close_mario_ai()


class MarioReplayToolBox(QWidget):
    def __init__(self, main):
        super().__init__()
        self.setWindowTitle('Replay Tool Box')
        self.main = main

        self.setFixedSize(290, 480)
        self.move(100, 100)

        self.current_ai = None

        self.ai_list = os.listdir(DATA_PATH)
        self.ai_list.reverse()
        self.ai_list_widget = QListWidget()
        for ai in self.ai_list:
            name = np.load(os.path.join(DATA_PATH, ai, 'name.npy'))[0]
            self.ai_list_widget.addItem(name)
        self.ai_list_widget.clicked.connect(self.change_current_ai)

        self.select_button = QPushButton('선택')
        self.select_button.clicked.connect(self.select_ai)

        self.replay_generation_line_edit = QLineEdit()
        self.replay_generation_line_edit.setPlaceholderText("세대 입력")

        self.form_layout = QFormLayout()

        self.generation_label = QLabel()
        self.elite_fitness_label = QLabel()

        self.layer_label = QLabel()
        self.generation_size_label = QLabel()
        self.elitist_preserve_rate_label = QLabel()
        self.static_mutation_rate_label = QLabel()

        self.form_layout.addRow("학습된 세대: ", self.generation_label)
        self.form_layout.addRow("엘리트 적합도: ", self.elite_fitness_label)
        self.form_layout.addRow("신경망 크기: ", self.layer_label)
        self.form_layout.addRow("세대 크기: ", self.generation_size_label)
        self.form_layout.addRow("엘리트 보존: ", self.elitist_preserve_rate_label)
        self.form_layout.addRow("변이: ", self.static_mutation_rate_label)

        ai_list_layout = QVBoxLayout()
        ai_list_layout.addWidget(self.ai_list_widget)
        ai_list_layout.addWidget(self.replay_generation_line_edit)
        ai_list_layout.addWidget(self.select_button)
        ai_list_layout.addLayout(self.form_layout)

        self.setLayout(ai_list_layout)

    def change_current_ai(self):
        self.current_ai = self.ai_list_widget.currentRow()

        network = np.load(os.path.join(DATA_PATH, self.ai_list[self.current_ai], 'network.npy'))

        if os.path.exists(os.path.join(DATA_PATH, self.ai_list[self.current_ai], 'generation.npy')):
            generation = np.load(os.path.join(DATA_PATH, self.ai_list[self.current_ai], 'generation.npy'))[0]
            self.generation_label.setText(f'{generation}세대')
        else:
            self.generation_label.setText('없음')

        if os.path.exists(os.path.join(DATA_PATH, self.ai_list[self.current_ai], 'fitness.npy')):
            elite_fitness = np.load(os.path.join(DATA_PATH, self.ai_list[self.current_ai], 'fitness.npy'))[-1]
            self.elite_fitness_label.setText(f'{elite_fitness}')
        else:
            self.elite_fitness_label.setText('없음')

        self.layer_label.setText(['2', '3', '4'][network[0]])
        self.generation_size_label.setText(['10', '20', '30', '40', '50'][network[1]])
        self.elitist_preserve_rate_label.setText(['0%', '10%', '20%', '30%', '40%'][network[2]])
        self.static_mutation_rate_label.setText(['5%', '10%', '15%', '20%', '25%'][network[3]])

    def select_ai(self):
        if self.current_ai is not None:
            try:
                replay_generation = int(self.replay_generation_line_edit.text())
                generation = -1
                if os.path.exists(os.path.join(DATA_PATH, self.ai_list[self.current_ai], 'generation.npy')):
                    generation = np.load(os.path.join(DATA_PATH, self.ai_list[self.current_ai], 'generation.npy'))[0]

                if 0 <= replay_generation <= generation:
                    self.main.close_mario_ai()
                    self.main.run_mario_replay(self.ai_list[self.current_ai], replay_generation)
                else:
                    self.replay_generation_line_edit.clear()
            except:
                self.replay_generation_line_edit.clear()

    def closeEvent(self, event):
        self.main.close_mario_replay_tool_box()

    def keyPressEvent(self, event):
        if event.isAutoRepeat():
            return

        key = event.key()
        if key == Qt.Key.Key_Escape:
            self.main.close_mario_replay_tool_box()


class MarioGYM(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Mario GYM')

        self.mario = None
        self.mario_tile_map = None
        self.mario_key_viewer = None

        self.mario_ai_tool_box = None

        self.mario_ai = None
        self.mario_ai_tile_map = None
        self.mario_ai_info = None
        self.mario_ai_network = None
        self.mario_ai_graph = None

        self.mario_replay_tool_box = None

        self.setFixedSize(360, 240)

        mario_button = QPushButton('Super Mario Bros.')
        mario_button.clicked.connect(self.run_mario)
        mario_ai_button = QPushButton('Mario GYM')
        mario_ai_button.clicked.connect(self.run_mario_ai_tool_box)
        mario_replay_button = QPushButton('Replay')
        mario_replay_button.clicked.connect(self.run_mario_replay_tool_box)

        self.game_level_combo_box = QComboBox()
        self.game_level_combo_box.addItem('Level 1')
        self.game_level_combo_box.addItem('Level 2')
        self.game_level_combo_box.addItem('Level 3')
        self.game_level_combo_box.addItem('Level 4')
        self.game_level_combo_box.addItem('Level 5')
        self.game_level_combo_box.addItem('Level 6')
        self.game_level_combo_box.addItem('Level 7')
        self.game_level_combo_box.addItem('Level 8')

        self.game_speed_combo_box = QComboBox()
        self.game_speed_combo_box.addItem('보통 속도')
        self.game_speed_combo_box.addItem('빠른 속도')
        self.game_speed_combo_box.addItem('최고 속도')

        open_ai_folder_button = QPushButton('AI 폴더 열기')
        open_ai_folder_button.clicked.connect(self.open_ai_folder)

        vbox_layout = QVBoxLayout()
        vbox_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        vbox_layout.addWidget(mario_button)
        vbox_layout.addWidget(mario_ai_button)
        vbox_layout.addWidget(mario_replay_button)
        vbox_layout.addWidget(open_ai_folder_button)
        vbox_layout.addWidget(self.game_level_combo_box)
        vbox_layout.addWidget(self.game_speed_combo_box)

        self.setLayout(vbox_layout)

    def run_mario(self):
        self.mario_tile_map = MarioTileMap(self)
        self.mario_tile_map.show()

        self.mario_key_viewer = MarioKeyViewer(self)
        self.mario_key_viewer.show()

        self.mario = Mario(self, self.game_level_combo_box.currentIndex(), self.game_speed_combo_box.currentIndex())
        self.mario.show()

        self.hide()

    def close_mario(self):
        self.mario.frame_timer.stop_game()
        self.mario.close()
        self.mario_tile_map.close()
        self.mario_key_viewer.close()
        self.show()

    def run_mario_ai_tool_box(self):
        self.mario_ai_tool_box = MarioAIToolBox(self)
        self.mario_ai_tool_box.show()

        self.hide()

    def close_mario_ai_tool_box(self):
        self.close_mario_ai()
        self.mario_ai_tool_box.close()
        self.show()

    def run_mario_ai(self, select_folder_name):
        self.mario_ai_tile_map = MarioAITileMap(self)
        self.mario_ai_tile_map.show()
        self.mario_ai_info = MarioAIInfo(self)
        self.mario_ai_info.show()
        self.mario_ai_network = MarioAINetwork(self)
        self.mario_ai_network.show()
        self.mario_ai_graph = MarioAIGraph(self)
        self.mario_ai_graph.show()
        self.mario_ai = MarioAI(self, self.game_level_combo_box.currentIndex(), self.game_speed_combo_box.currentIndex(), select_folder_name)
        self.mario_ai.show()

    def close_mario_ai(self):
        if self.mario_ai is not None:
            self.mario_ai.frame_timer.stop_game()
            self.mario_ai.close()
            self.mario_ai_tile_map.close()
            self.mario_ai_info.close()
            self.mario_ai_network.close()
            self.mario_ai_graph.close()
            self.mario_ai = None

    def run_mario_replay_tool_box(self):
        self.mario_replay_tool_box = MarioReplayToolBox(self)
        self.mario_replay_tool_box.show()

        self.hide()

    def close_mario_replay_tool_box(self):
        self.close_mario_replay()
        self.mario_replay_tool_box.close()
        self.show()

    def run_mario_replay(self, select_folder_name, replay_generation):
        self.mario_ai_tile_map = MarioAITileMap(self)
        self.mario_ai_tile_map.show()
        self.mario_ai_info = MarioAIInfo(self)
        self.mario_ai_info.show()
        self.mario_ai_network = MarioAINetwork(self)
        self.mario_ai_network.show()
        self.mario_ai_graph = MarioAIGraph(self)
        self.mario_ai_graph.show()
        self.mario_ai = MarioAI(self, self.game_level_combo_box.currentIndex(), self.game_speed_combo_box.currentIndex(), select_folder_name, replay_generation)
        self.mario_ai.show()

    def close_mario_replay(self):
        if self.mario_ai is not None:
            self.mario_ai.frame_timer.stop_game()
            self.mario_ai.close()
            self.mario_ai_tile_map.close()
            self.mario_ai_info.close()
            self.mario_ai_network.close()
            self.mario_ai_graph.close()
            self.mario_ai = None

    def open_ai_folder(self):
        if os.name == 'nt':
            os.startfile(DATA_PATH)
        elif sys.platform.startswith("darwin"):
            os.system(f'open {DATA_PATH}')

    def keyPressEvent(self, event):
        if event.isAutoRepeat():
            return

        key = event.key()
        if key == Qt.Key.Key_Escape:
            self.close()


# def exception_hook(except_type, value, traceback):
#     print(except_type, value, traceback)
#     print(traceback.format_exc())
#     exit(1)


def run():
    # sys.excepthook = exception_hook
    app = QApplication(sys.argv)
    w = MarioGYM()
    w.show()
    app.exec()


try:
    if not os.path.exists(DATA_PATH):
        os.mkdir(DATA_PATH)
    if not os.path.exists(os.path.join(retro.data.path(), 'stable', 'SuperMarioBros-Nes', 'rom.nes')):
        rom_file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Super Mario Bros. (World).nes')
        rom_file = open(rom_file_path, "rb")
        data, hash = retro.data.groom_rom(rom_file_path, rom_file)

        known_hashes = retro.data.get_known_hashes()

        if hash in known_hashes:
            game, ext, curpath = known_hashes[hash]
            with open(os.path.join(curpath, game, 'rom%s' % ext), 'wb') as f:
                f.write(data)
except:
    print('failed to import ROM file', file=sys.stderr)


if __name__ == '__main__':
    run()
