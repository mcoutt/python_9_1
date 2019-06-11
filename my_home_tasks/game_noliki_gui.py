"""
Игра "Крестики-нолики".

Условия игры:
1. Пользователь должен выбрать игроков и нажать кнопку Start.
2. Пользователь кликает по любому свободному полю
3.1. Если игра с компьютером - он делает ход и показывается куда походил
3.2. Если игра с другим игроком - он должен сделать ход
Алгоритм повторяется пока
А. Или заканчиваются свободные поля
Б. Кто-то выигрывает - Вы или компьютер / второй игрок

Особенности реализации: компьютер играет по-умному.
1. Он первым своим ходом пытается занять центр поля.
2. Он старается предсказать ваше выигрышное поле и занять его.
3. Он ищет свои выигрышные поля и если такие есть - ходит туда.
"""
import tkinter as tk
from tkinter import messagebox as mb
import random


def about_game():
    """Показываем информацию об игре."""
    output = "\nChoose with whom you will play and press button 'Start game'.\n"
    output += "\nClick on the field if you want to put 'X' or 'O' there.\n"
    mb.showinfo(title="About", message=output)


def game_over(info):
    """Показываем информацию о завершении игры."""
    mb.showinfo(title="Result", message=info)


def close_win():
    """Корректное закрытие окна программы."""
    answer = mb.askyesno(title="Exit", message="Close the program?")
    if answer is True:
        root.destroy()


def config_win(width=500, height=500):
    """Конфигурируем окно программы."""
    # Название и фон
    root.title('Game "Tic-tac-toe"')
    root.configure(background='white')
    # Размеры экрана
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # Центрируем положение
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 1.4)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))
    # root.iconbitmap('icon.ico')
    root.resizable(False, False)

    # Меню
    top_menu = tk.Menu(root)
    # окно конфигурируется с указанием меню для него
    root.config(menu=top_menu)
    # формируется список команд пункта меню
    top_menu.add_command(label="About", command=about_game)
    top_menu.add_command(label="Exit", command=close_win)


def init_data():
    """Исходные данные."""
    global db_fields
    # global gamers_list
    global user_go
    global user_wait
    global xo
    global xo_go
    global xo_wait
    # Словарь с параметрами игрового поля: key: [(x, y), number_field]
    db_fields = {1: [(24, 24), 1], 2: [(136, 24), 2], 3: [(248, 24), 3],
                 4: [(24, 136), 4], 5: [(136, 136), 5], 6: [(248, 136), 6],
                 7: [(24, 248), 7], 8: [(136, 248), 8], 9: [(248, 248), 9]
                 }

    user_go = 'You'
    user_wait = ''
    xo = ['X', 'O']
    xo_go = xo[0]
    xo_wait = xo[1]


def change_move():
    """Меняем игроков."""
    global xo_go
    global xo_wait
    global user_go
    global user_wait
    xo_go, xo_wait = xo_wait, xo_go
    user_go, user_wait = user_wait, user_go


def start_game():
    """Запуск программы по кнопке Старт."""
    global users
    global user_wait
    if gamers.get() == 1:
        user_wait = 'Computer'
        users = 1
    else:
        user_wait = 'User 1'
        users = 2
    msg_rule.configure(text="Beginning of the game. You and {}.".format(user_wait))
    msg_info.configure(text="Click on the field if you want to put 'X' or 'O' there.")
    btn_start["state"] = "disabled"


def free_field():
    """Ищем свободные поля для записи."""
    return [x[1] for x in db_fields.values() if x[1] in range(1, 10)]


def random_field():
    """Случайный выбор поля компьютером."""
    return random.choice(free_field())


def predict_win(xo=None):
    """Предсказать выигрышное поле."""
    # Есть 8 выигрышных комбинаций - 3 по горизонтали, 3 по вертикали и крест
    xy = db_fields  # Для краткости записи
    win_list = [[xy[1][1], xy[2][1], xy[3][1]],
                [xy[4][1], xy[5][1], xy[6][1]],
                [xy[7][1], xy[8][1], xy[9][1]],
                [xy[1][1], xy[4][1], xy[7][1]],
                [xy[2][1], xy[5][1], xy[8][1]],
                [xy[3][1], xy[6][1], xy[9][1]],
                [xy[1][1], xy[5][1], xy[9][1]],
                [xy[3][1], xy[5][1], xy[7][1]]
                ]

    # Перебираем список выигрышных комбинаций
    for win in win_list:
        # Ищем комбинацию, где уже два поля заполнены, если такое есть
        if win.count(xo) == 2:
            for x in win:
                # Ищем цифру и выводим её
                if isinstance(x, int):
                    return x


def effective_step():
    """Стараемся делать эффективные ходы, хотя и рандомайзом."""
    free_fields = free_field()
    if len(free_fields) > 7:
        # Компьютеру нужно сделать свой первый ход, стараемся занять центр
        if 5 in free_fields:
            return 5
        else:
            return random_field()
    elif len(free_fields) > 5:
        # Компьютеру нужно сделать второй ход
        # 1. Пробуем мешать сопернику, предсказав его выигрышное поле
        # 2. Если такого нет - делаем случайный ход
        if predict_win(xo_wait):
            return predict_win(xo_wait)
        else:
            return random_field()
    else:
        # Компьютеру нужно сделать остальные ходы
        # 1. Ищем своё выигрышное поле
        # 2. Пробуем мешать сопернику, предсказав его выигрышное поле
        # 3. Если такого нет - делаем случайный ход
        if predict_win(xo_go):
            return predict_win(xo_go)
        elif predict_win(xo_wait):
            return predict_win(xo_wait)
        else:
            return random_field()


def rewrite_field(f_index=None, f_value=None):
    """Перезаписываем поле по индексу (номеру в таблице), нужным значением."""
    for key, value in db_fields.items():
        if value[1] == f_index:
            value[1] = f_value


def check_win():
    """Проверка выигрышных комбинаций или кол-ва свободных полей."""
    # Есть 8 выигрышных комбинаций - 3 по горизонтали, 3 по вертикали и крест
    xy = db_fields  # Для краткости записи
    win_list = [[xy[1][1], xy[2][1], xy[3][1]],
                [xy[4][1], xy[5][1], xy[6][1]],
                [xy[7][1], xy[8][1], xy[9][1]],
                [xy[1][1], xy[4][1], xy[7][1]],
                [xy[2][1], xy[5][1], xy[8][1]],
                [xy[3][1], xy[6][1], xy[9][1]],
                [xy[1][1], xy[5][1], xy[9][1]],
                [xy[3][1], xy[5][1], xy[7][1]]
                ]

    # Если есть хоть одна выигрышная комбинация, тогда...
    for win in win_list:
        if win.count(xo_go) == 3:
            for x in free_field():
                field_buttons[x].field_disabled()
            return ("Winner {}. Game over.".format(user_go))

    # Если выигрышных комбинаций нет и закончились свободные ячейки, тогда...
    if len(free_field()) == 0:
        return ("No winner. Game over.")


def comp_click():
    field_buttons[effective_step()].comp_step()
    if check_win():
        msg_result.configure(text=check_win())
        game_over(check_win())
    else:
        change_move()


class FieldButton:
    def __init__(self, f_x, f_y, f_num):
        self.f_num = f_num
        self.field = tk.Button(reg_field, text='', bd=0)
        self.field.bind('<Button-1>', self.field_change)
        self.field.place(x=f_x, y=f_y, width=110, height=110)

    def comp_step(self):
        self.field.config(state="disabled")
        rewrite_field(self.f_num, xo_go)
        self.field.config(text=xo_go)
        msg_info.configure(text="{0} makes move {1} -> {2}".format(user_go, xo_go, self.f_num))

    def field_change(self, event):
        if btn_start["state"] == "disabled":
            self.field.config(state="disabled")
            if self.field["text"] == '':
                rewrite_field(self.f_num, xo_go)
                msg_info.configure(text="{0} makes move {1} -> {2}".format(user_go, xo_go, self.f_num))
                self.field["text"] = xo_go
                if check_win():
                    msg_result.configure(text=check_win())
                    game_over(check_win())
                else:
                    change_move()
                    if users == 1:
                        comp_click()

    def field_disabled(self):
        self.field.config(text="*")
        self.field.config(state="disabled")


# Инициалищируем включение данных по игре
init_data()
# Начинаем рисовать окно программы
root = tk.Tk()
config_win(400, 550)

reg_start = tk.Frame(root, width=400, height=65, bg="white")
gamers = tk.IntVar()
gamers.set(1)
select_gm_1 = tk.Radiobutton(reg_start, text='You and Computer', variable=gamers, value=1)
select_gm_2 = tk.Radiobutton(reg_start, text='You an other gamer', variable=gamers, value=2)
select_gm_1.config(bg='white', highlightbackground='white', activebackground='white')
select_gm_2.config(bg='white', highlightbackground='white', activebackground='white')
btn_start = tk.Button(reg_start, text="Start game", command=start_game)
reg_start.pack()
btn_start.place(x=240, y=15)
select_gm_1.place(x=40, y=7)
select_gm_2.place(x=40, y=35)

reg_field = tk.Frame(root, width=400, height=400)
fields = tk.Canvas(reg_field, width=382, height=382, bg="gray70", bd=0, highlightthickness=0)
fields.create_line(135, 24, 135, 358)
fields.create_line(246, 24, 246, 358)
fields.create_line(24, 135, 358, 135)
fields.create_line(24, 247, 358, 247)
reg_field.pack()
fields.pack()
field_buttons = {}
for x in db_fields.values():
    field_buttons[x[1]] = FieldButton(x[0][0], x[0][1], x[1])

reg_messg = tk.Frame(root, width=400, bg="white")
msg_rule = tk.Label(reg_messg, bg="white", bd=10)
msg_info = tk.Label(reg_messg, bg="white", bd=0)
msg_result = tk.Label(reg_messg, bg="white", bd=10)
reg_messg.pack()
msg_rule.pack()
msg_rule.configure(text="Choose with whom you will play\nand press button 'Start game'.")
msg_info.pack()
msg_result.pack()

root.mainloop()

# The END / Конец.
