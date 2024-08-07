from PIL import Image
from random import randint


def base(img):
    '''Три базовые функции по изменению цвета всей картинки в канале RGB'''
    color = input('Какой цвет ты хочешь изменить? (R - Red, G - Green, B - Blue)\nВвод: ').upper()
    while color not in ('R', 'G', 'B'):
        print('Походу ты ввёл чё-то не то')
        color = input('Ввод: ').upper()
    ratio = int(input('На сколько процентов повысить цвет?\nВвод: ')) / 100 + 1
    for x in range(img.width):
        for y in range(img.height):
            r, g, b = img.getpixel((x, y))
            if color == 'R':
                pixel = (int(min(255, r * ratio)), g, b)
            elif color == 'G':
                pixel = (r, int(min(255, g * ratio)), b)
            else:
                pixel = (r, g, int(min(255, b * ratio)))
            img.putpixel((x, y), pixel)
    img.show()
    return 'Иииу кайфуем'


def white_change(img):
    '''Меняет белый цвет на заданный'''
    color_choice = input('Выберите заменяющий цвет ("синий", "красный" или "зелёный"):\nВвод: ')
    while color_choice not in ("синий", "красный", "зелёный"):
        color_choice = input('Выберите заменяющий цвет ("синий", "красный" или "зелёный"):\nВвод: ')
    for x in range(img.width):
        for y in range(img.height):
            r, g, b = img.getpixel((x, y))
            if r > 230 and g > 230 and b > 230:
                if color_choice == 'синий':
                    img.putpixel((x, y), (58, 100, 214))
                elif color_choice == 'красный':
                    img.putpixel((x, y), (176, 39, 62))
                else:
                    img.putpixel((x, y), (42, 212, 73))
    img.show()
    return 'Иииу откисаем'


# Не получилось сделать плавное затемнение
# def vignette(img):
#     w, h = img.size
#     for x in range(img.width):
#         for y in range(img.height):
#             r, g, b = img.getpixel((x, y))
#             if w - x < 100 or h - y < 100 or h - (h - y) < 100 or w - (w - x) < 100:
#                 coef = x + y / 200
#                 if int(coef) == 0:
#                     coef = 1
#                     color_near = False
#                     if
#                 img.putpixel((x, y), (int(r / coef), int(g / coef), int(b / coef)))
#     img.show()


def random_white(img):
    '''Заменяет белый цвет на радужный шум'''
    for x in range(img.width):
        for y in range(img.height):
            r, g, b = img.getpixel((x, y))
            if r > 220 and g > 220 and b > 220:
                r = randint(0, 255)
                g = randint(0, 255)
                b = randint(0, 255)
                img.putpixel((x, y), (r, g, b))
    img.show()
    return 'Иииу чилим'


#Да, я люблю библиотеку random))))
def Sepia(img):
    '''Высветляет или точечно затемняет рисунок'''
    q = int(input('1) Высветлить\n2) Затемнить\nВвод: '))
    while q not in (1, 2):
        q = int(input('Кажется ты не понял...\n1) Высветлить\n2) Затемнить\nВвод: '))
    for x in range(img.width):
        for y in range(img.height):
            r, g, b = img.getpixel((x, y))
            if q == 1:
                ratio = int(randint(0, 1000) / 100)
                img.putpixel((x, y), (r * ratio, g * ratio, b * ratio))
            else:
                ratio = int(randint(0, 120) / 100)
                img.putpixel((x, y), (r * ratio, g * ratio, b * ratio))
    img.show()
    return 'Иииу халявим'


def inverse(img):
    '''Переворачивает отенки всех 3х палитр'''
    for x in range(img.width):
        for y in range(img.height):
            r, g, b = img.getpixel((x, y))
            img.putpixel((x, y), (255 - r, 255 - g, 255 - b))
    img.show()
    return 'Иииу на веселе'


filters = {
    1: {
        'name': 'BASE FILTER',
        'description': 'Базовый фильтр изменяющий цвет картинки на заданный вами коэффициент',
        'start': base
    },

    2: {
        'name': 'WHITE CHANGE',
        'description': 'Меняет белый цвет на выбранный вами',
        'start': white_change
    },

     # 3: {
     #     'name': 'tcshhh',
     #     'description': 'Шёпотом',
     #     'start':vignette
     # }

    3: {
        'name': 'RANDOM WHITE',
        'description': 'Заменяет белый цвет на радужный шум',
        'start': random_white
    },

    4: {
        'name': 'SEPIA',
        'description': 'Попиксельно высветляет или затемняет изображение',
        'start': Sepia
    },

    5: {
        'name': 'INVERSE',
        'description': 'Накладывает эффект ренгтена на изображение',
        'start': inverse
    }}
