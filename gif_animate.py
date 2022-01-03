import os

import pygame

DIRNAME = 'gifs'


class GIFAnimate:

    def __init__(self, x, y):
        # позиции картинки на экране
        self.x, self.y = x, y
        # список всех гифок в программе
        self.gifs_paths = self.get_gifs_paths()
        # список загруженых картинок
        self.gifs = []
        # текущий индекс гифки
        self.current_gif = 0
        # индекс картинки в текущей гифке
        self.current_index = 0
        # заргужаем все картинки сразу в мапять
        self.pre_load_images()

    def pre_load_images(self):
        # предзагрузка всех изображений
        for gif_paths in self.gifs_paths:
            loaded_images = []
            for path in gif_paths:
                loaded_images.append(pygame.image.load(path))
            self.gifs.append(loaded_images)

    def show_next_image(self, display, fps, current_step):
        # display - экран для отрисовки
        # fps - сколько кадров в секунду поддерживает приложение
        # current_step - какой кадр сейчас проигрывается
        # менять картинку необходимо
        # каждый fps//len(self.gifs[self.current_gif]) шаг
        gif_count = len(self.gifs[self.current_gif])
        step = fps // gif_count
        # проверяем, если сейчас кадр (fps+current_step)%step == 0,
        # то меняем картинку
        if (fps+current_step) % step == 0:
            self.current_index += 1
        # если индекс новой картинки выходит за количество картинок, то
        # новый индекс картинки равен 0
        if self.current_index >= gif_count:
            self.current_index = 0
        # отрисовываем на экране картинку
        display.blit(self.gifs[self.current_gif][self.current_index],
                     (self.x, self.y))

    def change_gif(self, index):
        # если крутим колесиком мыши, то надо делать сдвиг по картинке
        # назад или вперед, для этого просто сохраняем индекс текущей гифки
        self.current_gif += index
        if self.current_gif >= len(self.gifs):
            self.current_gif = 0
        elif self.current_gif < 0:
            self.current_gif = len(self.gifs) - 1

    def get_gifs_paths(self, dirname=DIRNAME):
        # Получаем список файлов в нужной директории, например, gifs
        dirfiles = os.listdir(dirname)
        # Прибавляем полный путь до них
        fullpaths = map(lambda name: os.path.join(dirname, name), dirfiles)
        # Получаем список вложенных папок
        dirs = []
        for file in fullpaths:
            if os.path.isdir(file):
                dirs.append(file)
        # Для каждой папки получаем список файлов и складываем в общий список
        files_list = []
        for dir in dirs:
            dirfiles = os.listdir(dir)
            files_list.append([os.path.join(dir, file) for file in dirfiles])
        return files_list
