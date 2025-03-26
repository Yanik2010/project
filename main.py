import customtkinter as ctk

def handle_add_category():
    dialog_window = ctk.CTkToplevel()  # вспомогательное окно открывается в момент создания, цикл .mainloop() не нужен
    # оно закрывается либо при нажатии на крестик в углу этого окна, либо при вызове метода dialog_window.destroy()
    dialog_window.title("Добавить категорию")
    dialog_window.geometry("500x500")  # как правило, вспомогательные окна маленьких размеров

    def give_answer():
        categories.append(entry_answer.get())
        x.append(lambda c = categories[-1]: handle_open_category(c))
        y.append(ctk.CTkButton(master=scrollable_frame, text=categories[len(categories) - 1], font=my_font, width=200, height=50, command=x[-1]))
        y[-1].grid(row=len(y) - 1, column=0, padx=20, pady=20)
        tasks[categories[-1]] = []
        tasks_lable[categories[-1]] = []
        dialog_window.destroy()

    lbl_question = ctk.CTkLabel(master=dialog_window, text="Напишите название для новой категории", font=my_font)
    entry_answer = ctk.CTkEntry(master=dialog_window, font=my_font, width=200, placeholder_text="Введите ответ")
    btn_get_answer = ctk.CTkButton(master=dialog_window, font=my_font, text="Ответить", width=100, command=give_answer)
    rows, columns = 3, 1
    for i in range(rows):
        dialog_window.rowconfigure(index=i, weight=1)
    for i in range(columns):
        dialog_window.columnconfigure(index=i, weight=1)
    lbl_question.grid(row=0, column=0)
    entry_answer.grid(row=1, column=0)
    btn_get_answer.grid(row=2, column=0)

def handle_open_category(c):
    global flag
    if flag != None and len(tasks[flag]) > 0:
        for i in range(len(tasks_lable[flag])):
            tasks_lable[flag][i].grid_forget()
    flag = c
    widget_label.configure(text="Категория " + c, font=my_font)
    plus_left.configure(state="normal")
    for i in range(len(tasks[c])):
        tasks_lable[flag][i].grid()


def handle_add_task():
    dialog_window2 = ctk.CTkToplevel()  # вспомогательное окно открывается в момент создания, цикл .mainloop() не нужен
    # оно закрывается либо при нажатии на крестик в углу этого окна, либо при вызове метода dialog_window.destroy()
    dialog_window2.title("Добавить задачу")
    dialog_window2.geometry("500x500")  # как правило, вспомогательные окна маленьких размеров

    def give_answer2():
        global flag
        answer = entry_answer.get()
        tasks[flag].append(answer)
        if len(tasks[flag]) == 2:
            kkk=1
        tasks_lable[flag].append(ctk.CTkLabel(master=scrollable_frame2, text=answer, font=my_font, width=200, height=50))
        tasks_lable[flag][-1].grid(row=len(tasks[flag]), column=0, padx=20, pady=20)
        dialog_window2.destroy()
        print(tasks)

    lbl_question2 = ctk.CTkLabel(master=dialog_window2, text="Напишите название для новой задачи", font=my_font)
    entry_answer = ctk.CTkEntry(master=dialog_window2, font=my_font, width=200, placeholder_text="Введите ответ")
    btn_get_answer = ctk.CTkButton(master=dialog_window2, font=my_font, text="Ответить", width=100, command=give_answer2)
    rows, columns = 3, 1
    for i in range(rows):
        dialog_window2.rowconfigure(index=i, weight=1)
    for i in range(columns):
        dialog_window2.columnconfigure(index=i, weight=1)
    lbl_question2.grid(row=0, column=0)
    entry_answer.grid(row=1, column=0)
    btn_get_answer.grid(row=2, column=0)

# задаём цветовое оформление всего приложения
ctk.set_appearance_mode("dark")  # все возможные варианты: "dark", "light"
ctk.set_default_color_theme("green")  # также можно: "blue", "dark-blue", "green"

root = ctk.CTk()  # создаём окно и привязываем его переменной root
root.title("Название приложения")  # устанавливаем заголовок окна
root.title("Расположение виджетов в сетке - grid")
root.geometry("1250x800")  # устанавливаем размеры окна
my_font = ctk.CTkFont(family="Roboto", size=20)  # задаём шрифт, потом будем применять его к виджетам

scrollable_frame2 = ctk.CTkScrollableFrame(master=root)  # прокручиваемая рамка
scrollable_frame2.configure(height=500, width=700)

scrollable_frame = ctk.CTkScrollableFrame(master=root)  # прокручиваемая рамка
scrollable_frame.configure(height=500, width=300)



widget_label = ctk.CTkLabel(master=scrollable_frame2)  # создаём текстовый виджет label и привязываем его к окну root
widget_label.configure(text="Категория...", font=my_font)  # задание его конфигураций: text, font
widget_label.grid(row=0, column=0, padx=250)

categories = ["Работа", "Дом", "Покупки", "Места куда сходить"]
tasks = {"Работа": [], "Дом": [],"Покупки": [],"Места куда сходить": []}
tasks_lable = {"Работа": [], "Дом": [],"Покупки": [],"Места куда сходить": []}

x = [lambda : handle_open_category("Работа"), lambda : handle_open_category("Дом"), lambda : handle_open_category("Покупки"), lambda : handle_open_category("Места куда сходить")]

flag = None

y = [ctk.CTkButton(master=scrollable_frame, text=categories[0], font=my_font, width=200, height=50, command=x[0]),
ctk.CTkButton(master=scrollable_frame, text=categories[1], font=my_font, width=200, height=50, command=x[1]),
ctk.CTkButton(master=scrollable_frame, text=categories[2], font=my_font, width=200, height=50, command=x[2]),
ctk.CTkButton(master=scrollable_frame, text=categories[3], font=my_font, width=200, height=50, command=x[3])]

for i in range(len(y)):
    y[i].grid(row=i, column=0, padx=20, pady=20)

rows, columns = 3, 3
for i in range(rows):
    root.rowconfigure(index=i, weight=1)
for i in range(columns):
    root.columnconfigure(index=i, weight=1)
scrollable_frame.grid(row=0, column=2)
scrollable_frame2.grid(row=0, column=0)

plus_right = ctk.CTkButton(master=root, height=50, width=250)
plus_right.configure(text="+", font=my_font, command=handle_add_category)
plus_right.grid(row=1, column=2)

plus_left = ctk.CTkButton(master=root, height=50, width=250, command=handle_add_task)
plus_left.configure(text="+", font=my_font)
plus_left.grid(row=1, column=0)
plus_left.configure(state="disabled")

root.mainloop()
