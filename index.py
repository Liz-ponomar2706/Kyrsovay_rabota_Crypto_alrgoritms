from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import codecs
from functools import reduce
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
import binascii
import  time
import random
import string
from typing import Callable, Any


def text_info():
    with codecs.open("D:\практика\info.txt", "r", "utf_8_sig") as file:
        text = file.read()
    file.close()
    return text

def get_info():
    info = Tk()
    info.title("Информация")
    info.iconbitmap('D:\практика\eye.ico')
    info.configure(background='#B9BBDF')
    w = 700
    h = 560
    ws = info.winfo_screenwidth()
    hs = info.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    info.geometry('%dx%d+%d+%d' % (w, h, x, y))
    info.resizable(False, False)

    info_txt = text_info()
    text = ScrolledText(info, background='#B9BBDF', foreground="#253b6e", font=0.2, wrap=WORD)
    text.pack(fill=BOTH)
    text.insert("1.0", info_txt )

def selected_combobox(event):
    select = combobox.get()
    return select

window = Tk()
window.title("Криптография")
window.iconbitmap('D:\практика\eye.ico')
window.configure(background="#dde7f2")

#Размещения окна по центру
w = 1100
h = 750
ws = window.winfo_screenwidth()
hs = window.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
window.geometry('%dx%d+%d+%d' % (w, h, x, y))
window.resizable(False, False)

#Первый заголовок
label = Label(justify=CENTER, background="#dde7f2" ,foreground="#253b6e", width=800, font=24, text="Криптографическая зашифровка текста")
label.pack()

#Выбор зашифровки заголовок и меню 
label = ttk.Label(justify=LEFT, background="#dde7f2", foreground="#253b6e", font=16, text="Выберите тип криптографической зашифровки")
label.place(x=25, y=40)
kripts = ["Nush", "N-Hesh", "BaseKing", "MMB"]
kripts_var= StringVar(value=kripts[0])
combobox = ttk.Combobox(justify=CENTER, textvariable=kripts_var, values=kripts, background="#dde7f2", foreground="#253b6e", font=12, width=40, state="readonly")
combobox.place(x= 580, y=40)
combobox.bind("<<ComboboxSelected>>", selected_combobox)

#Заголовок и текст оригинала
label = ttk.Label(justify=LEFT, background="#dde7f2", foreground="#253b6e", font=14, text="Исходный текст")
label.place(x=200, y=95)
editor_text = ScrolledText(window, background="#B9BBDF", foreground="#253b6e", font=("Verdana", 14), width=35, wrap=None)
editor_text.place(x=60, y=130)

#Зашифровка или расшифровка
label_crypt = ttk.Label(justify=LEFT, background="#dde7f2", foreground="#253b6e", font=14, text="Зашифровка")
label_crypt.place(x=780, y=95)
#label_decrypt = ttk.Label(justify=LEFT, background="#dde7f2", foreground="#878ecd", font=14, text="Расшифровка")
#label.place(x=780, y=90)
editor_kript = ScrolledText(window, background="#B9BBDF", foreground="#253b6e", font=("Verdana", 14), width=35, wrap=None)
editor_kript.place(x=610, y=130)


# открываем файл в текстовое поле
def open_file():
    filepath = filedialog.askopenfilename()
    if filepath != "":
        with codecs.open(filepath, "r", "utf_8_sig") as file:
            text =file.read()
            editor_text.delete("1.0", END)
            editor_text.insert("1.0", text)
 
# сохраняем текст из текстового поля в файл
def save_file():
    filepath = filedialog.asksaveasfilename()
    if filepath != "":
        text = editor_kript.get("1.0", END)
        with codecs.open(filepath, "w", "utf_8_sig") as file:
            file.write(text)

def delete_text_editor():
    editor_text.delete("1.0", END)

def delete_text_kript():
    editor_kript.delete("1.0", END)

# Функция для копирования и выделения текста
def copy_editor_text():
    # Получаем текст из текстового поля
    text = editor_text.get("1.0", "end")
    # Копируем текст в буфер обмена операционной системы
    window.clipboard_clear()
    window.clipboard_append(text)
    window.update()
   

def copy_kript_text():
    # Получаем текст из текстового поля
    text = editor_kript.get("1.0", "end")
    # Копируем текст в буфер обмена операционной системы
    window.clipboard_clear()
    window.clipboard_append(text)
    window.update()

def selected_combobox():
    select = combobox.get()
    return select

class NushCipher:
    def __init__(self):
        self.mapping = {
            'a': 'x',
            'b': 'y',
            'c': 'z',
            'd': 'a',
            'e': 'b',
            'f': 'c',
            'g': 'd',
            'h': 'e',
            'i': 'f',
            'j': 'g',
            'k': 'h',
            'l': 'i',
            'm': 'j',
            'n': 'k',
            'o': 'l',
            'p': 'm',
            'q': 'n',
            'r': 'o',
            's': 'p',
            't': 'q',
            'u': 'r',
            'v': 's',
            'w': 't',
            'x': 'u',
            'y': 'v',
            'z': 'w',
            'а' : 'ь',
            'б' : 'ж',
            'в' : 'ц',
            'г' : 'д',
            'д' : 'н',
            'е' : 'ы',
            'ё' : 'ь',
            'ж' : 'в',
            'з' : 'л',
            'и' : 'у',
            'й' : 'ч',
            'к' : 'л',
            'л' : 'г',
            'м' : 'д',
            'н' : 'б',
            'о' : 'э',
            'п' : 'щ',
            'р' : 'к',
            'с' : 'ш',
            'т' : 'м',
            'у' : 'е',
            'ф' : 'а',
            'ц' : 'т',
            'ч' : 'с',
            'ш' : 'а',
            'щ' : 'п',
            'ъ' : 'и',
            'ы' : 'е',
            'ь' : 'о',
            'э' : 'я',
            'ю' : 'й',
            'я' : 'ю',
            '1' : '8',
            '2' : '9',
            '3' : '0',
            '4' : '5',
            '5' : '1',
            '6' : '7',
            '7' : '2',
            '8' : '3',
            '9' : '4',
            '0' : '6',
        }

    def encrypt(self, text):
        encrypted_text = ''
        for char in text:
            if char.lower() in self.mapping:
                encrypted_text += self.mapping[char.lower()]
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self, encrypted_text):
        decrypted_text = ''
        reverse_mapping = {v: k for k, v in self.mapping.items()}
        for char in encrypted_text:
            if char.lower() in reverse_mapping:
                decrypted_text += reverse_mapping[char.lower()]
            else:
                decrypted_text += char
        return decrypted_text
    
class NHash:
    def __init__(self, n):
        self.n = n
        self.alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

    def encrypt(self, text):
        encrypted_text = ''
        for char in text.lower():
            if char in self.alphabet:
                index = self.alphabet.index(char)
                encrypted_index = (index + self.n) % len(self.alphabet)
                encrypted_text += self.alphabet[encrypted_index]
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self, encrypted_text):
        decrypted_text = ''
        for char in encrypted_text.lower():
            if char in self.alphabet:
                index = self.alphabet.index(char)
                decrypted_index = (index - self.n) % len(self.alphabet)
                decrypted_text += self.alphabet[decrypted_index]
            else:
                decrypted_text += char
        return decrypted_text


class BaseKingCrypto:
    def __init__(self, key):
        self.key = key
        self.alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        self.alphabet_len = len(self.alphabet)

    def encrypt(self, plaintext):
        encrypted_text = ''
        for i, char in enumerate(plaintext.lower()):
            if char in self.alphabet:
                char_index = self.alphabet.index(char)
                key_index = ord(self.key[i % len(self.key)]) % self.alphabet_len
                encrypted_index = (char_index + key_index) % self.alphabet_len
                encrypted_text += self.alphabet[encrypted_index]
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self, encrypted_text):
        decrypted_text = ''
        for i, char in enumerate(encrypted_text.lower()):
            if char in self.alphabet:
                char_index = self.alphabet.index(char)
                key_index = ord(self.key[i % len(self.key)]) % self.alphabet_len
                decrypted_index = (char_index - key_index) % self.alphabet_len
                decrypted_text += self.alphabet[decrypted_index]
            else:
                decrypted_text += char
        return decrypted_text
    

class MMB:
    def __init__(self, key):
        self.key = key
        self.alphabet = string.ascii_uppercase + string.ascii_lowercase + string.digits + "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"

    def _shift_char(self, char, shift):
        if char in self.alphabet:
            return self.alphabet[(self.alphabet.index(char) + shift) % len(self.alphabet)]
        else:
            return char

    def encrypt(self, text):
        encrypted_text = ""
        for i, char in enumerate(text):
            shift = ord(self.key[i % len(self.key)]) % len(self.alphabet)
            encrypted_text += self._shift_char(char, shift)
        return encrypted_text

    def decrypt(self, encrypted_text):
        decrypted_text = ""
        for i, char in enumerate(encrypted_text):
            shift = ord(self.key[i % len(self.key)]) % len(self.alphabet)
            decrypted_text += self._shift_char(char, -shift)
        return decrypted_text

class AlgorithmTimerManager:
    def init(self, num_runs: int = 10):
        self.num_runs = num_runs
        self.timings = {}

    def time_algorithm(self, name: str, algorithm: Callable[..., Any], *args: Any, **kwargs: Any) -> float:
       
        total_time = 0.0
        for _ in range(self.num_runs):
            start_time = time.perf_counter()
            algorithm(*args, **kwargs)
            end_time = time.perf_counter()
            total_time += (end_time - start_time)
        
        avg_time = total_time / self.num_runs
        self.timings[name] = avg_time
        return avg_time

class AlgorithmSecurityManager:
    def init(self, num_runs: int = 10):
        self.num_runs = num_runs
        self.security_scores = {}

    def evaluate_algorithm(self, name: str, algorithm: Callable[..., Any], *args: Any, **kwargs: Any) -> float:
    
        time_score = self._evaluate_time(name, algorithm, *args, **kwargs)
        memory_score = self._evaluate_memory(name, algorithm, *args, **kwargs)
        randomness_score = self._evaluate_randomness(name, algorithm, *args, **kwargs)
        
        overall_score = (time_score + memory_score + randomness_score) / 3
        self.security_scores[name] = overall_score
        return overall_score

    def _evaluate_time(self, name: str, algorithm: Callable[..., Any], *args: Any, **kwargs: Any) -> float:
        total_time = 0.0
        for _ in range(self.num_runs):
            start_time = time.perf_counter()
            algorithm(*args, **kwargs)
            end_time = time.perf_counter()
            total_time += (end_time - start_time)
        
        avg_time = total_time / self.num_runs
        time_score = (1 - avg_time / 1.0) * 100  # Предположим, что 1 секунда - это максимально допустимое время
        return time_score

    def _evaluate_memory(self, name: str, algorithm: Callable[..., Any], *args: Any, **kwargs: Any) -> float:
        process = psutil.Process()
        initial_memory = process.memory_info().rss
        algorithm(*args, **kwargs)
        final_memory = process.memory_info().rss
        memory_delta = final_memory - initial_memory
        memory_score = (1 - memory_delta / 1024 ** 2) * 100  # Предположим, что 1 МБ - это максимально допустимый объем памяти
        return memory_score

    def _evaluate_randomness(self, name: str, algorithm: Callable[..., Any], *args: Any, **kwargs: Any) -> float:
        random_data = [algorithm(*args, **kwargs) for _ in range(1000)]
        min_value = min(random_data)
        max_value = max(random_data)
        value_range = max_value - min_value
        randomness_score = (1 - value_range / 100) * 100
        return randomness_score

def bk_cript():
    key = "mykey"
    crypto = BaseKingCrypto(key)
    kript_text = editor_text.get("1.0", END)
    ciphertext = crypto.encrypt(kript_text)
    return editor_kript.insert("1.0", ciphertext)



def bk_decrypt():
    key = "mykey"
    crypto = BaseKingCrypto(key)
    plaintext = editor_text.get("1.0", END)
    decrypted_text = crypto.decrypt(plaintext)
    return editor_kript.insert("1.0", decrypted_text)




def nush_cript():
    nush_cipher = NushCipher()
    kript_text = editor_text.get("1.0", END)
    ciphertext = nush_cipher.encrypt(kript_text)
    return editor_kript.insert("1.0", ciphertext)



def nush_decript():
    nush_cipher = NushCipher()
    kript_text = editor_text.get("1.0", END)
    decrypted_text = nush_cipher.decrypt(kript_text)
    return editor_kript.insert("1.0", decrypted_text)



def n_hesh():
    crypto = NHash(5)
    plaintext = editor_text.get("1.0", END)
    ciphertext = crypto.encrypt(plaintext)
    return editor_kript.insert("1.0", ciphertext)



def n_hesh_decrypt():
    crypto = NHash(5)
    plaintext = editor_text.get("1.0", END)
    decrypted_text = crypto.decrypt(plaintext)
    return editor_kript.insert("1.0", decrypted_text)



def mmb():
    key = "MYKEY123"
    mmb = MMB(key)
    plaintext = editor_text.get("1.0", END)
    encrypted_text = mmb.encrypt(plaintext)
    return editor_kript.insert("1.0", encrypted_text)




def mmb_decrypt():
    key = "MYKEY123"
    mmb = MMB(key)
    plaintext = editor_text.get("1.0", END)
    decrypted_text = mmb.decrypt(plaintext)
    return editor_kript.insert("1.0", decrypted_text)



    
def get_kript_text():
    label_crypt["text"]=f"Засшифровка"
    select=combobox.get()
    if (select == "Nush"):
        start_time = time.time()
        nush_cript()
        end_time = time.time()
        execution_time1 = end_time - start_time
    elif (select == "N-Hesh"):
        start_time = time.time()
        n_hesh()
        end_time = time.time()
        execution_time2 = end_time - start_time
    elif (select == "BaseKing"):
        start_time = time.time()
        bk_cript()
        end_time = time.time()
        execution_time3 = end_time - start_time
    elif (select == "MMB"):
        start_time = time.time()
        mmb()
        end_time = time.time()
        execution_time4 = end_time - start_time
    
    else: pass

      
        
def get_decrypt_text():
    label_crypt["text"]=f"Расшифровка"
    select=combobox.get()
    if (select == "Nush"):
        start_time = time.time()
        nush_decript()
        end_time = time.time()
        execution_time5 = end_time - start_time
    elif (select == "N-Hesh"):
        start_time = time.time()
        n_hesh_decrypt()
        end_time = time.time()
        execution_time6 = end_time - start_time
    elif (select == "BaseKing"):
        start_time = time.time()
        bk_decrypt()
        end_time = time.time()
        execution_time7 = end_time - start_time
    elif (select == "MMB"):
        start_time = time.time()
        mmb_decrypt()
        end_time = time.time()
        execution_time8 = end_time - start_time    
    else: pass
 

#Кнопки
btn_info = Button(window, text="?", background="#dde7f2", font=10, foreground="#253b6e", activebackground="#878ecd", activeforeground="#dde7f2", command=get_info )
btn_info.place(x=1070, y = 4)

btn_change_direction = Button(window, text="<--->", background="#dde7f2", font=20, foreground="#253b6e", activebackground="#878ecd", activeforeground="#dde7f2", command=get_decrypt_text)
btn_change_direction.place(x=525, y=330)

btn_output_text = Button(window, text="+", background="#878ECD", foreground="#dde7f2", font=20, activebackground="#dde7f2", activeforeground="#878ECD", command=open_file)
btn_output_text.place(x=500, y=645)

btn_copy_output = Button(window, text="[]", background="#878ECD", foreground="#dde7f2", font=20, activebackground="#dde7f2", activeforeground="#878ECD", command=copy_editor_text)
btn_copy_output.place(x=500, y=610)

btn_clear_output = Button(window, text="|", background="#878ECD", foreground="#dde7f2", font=20, activebackground="#dde7f2", activeforeground="#878ECD", command=delete_text_editor)
btn_clear_output.place(x=500, y=570)

btn_input_text = Button(window, text="+", background="#878ECD", foreground="#dde7f2", font=20, activebackground="#dde7f2", activeforeground="#878ECD", command=save_file)
btn_input_text.place(x=1050, y=645)

btn_copy_input = Button(window,text="[]", background="#878ECD", foreground="#dde7f2", font=20, activebackground="#dde7f2", activeforeground="#878ECD", command=copy_kript_text)
btn_copy_input.place(x=1050, y=610)

btn_clear_input = Button(window, text="|", background="#878ECD", foreground="#dde7f2", font=20, activebackground="#dde7f2", activeforeground="#878ECD", command=delete_text_kript)
btn_clear_input.place(x=1050, y=570)

btn_kript = Button(window, text="ШИФРОВКА", background="#dde7f2", font=20, foreground="#253b6e", activebackground="#878ecd", activeforeground="#dde7f2", command=get_kript_text)
btn_kript.place(x=480, y=700)

# Функции для отображения и скрытия всплывающей подсказки
def show_tooltip(event, text):
    x, y, _, _ = event.widget.bbox("insert")
    x += event.widget.winfo_rootx() + 25
    y += event.widget.winfo_rooty() + 25
    tooltip.geometry(f"+{x}+{y}")
    tooltip_label.configure(text=text)
    tooltip.deiconify()

def hide_tooltip(event):
    tooltip.withdraw()

# Создание всплывающей подсказки
tooltip = Toplevel(window)
tooltip.overrideredirect(True)
tooltip_label = Label(tooltip, justify='left', background="#878ECD", foreground="#dde7f2",
relief='solid', borderwidth=1, font=("tahoma", "11", "normal"))
tooltip_label.pack(ipadx=1)
tooltip.withdraw()

#Всплывающие подсказки для <->, ?, +, []
btn_change_direction.bind("<Enter>", lambda event: show_tooltip(event, "Переключение на расшифровку криптографии"))
btn_change_direction.bind("<Leave>", hide_tooltip)

btn_info.bind("<Enter>", lambda event: show_tooltip(event, "Инфо"))
btn_info.bind("<Leave>", hide_tooltip)

btn_output_text.bind("<Enter>", lambda event: show_tooltip(event, "Открыть файл"))
btn_output_text.bind("<Leave>", hide_tooltip)

btn_input_text.bind("<Enter>", lambda event: show_tooltip(event, "Сохранить в файл"))
btn_input_text.bind("<Leave>", hide_tooltip)

btn_copy_output.bind("<Enter>", lambda event: show_tooltip(event, "Скопировать"))
btn_copy_output.bind("<Leave>", hide_tooltip)

btn_copy_input.bind("<Enter>", lambda event: show_tooltip(event, "Скопировать"))
btn_copy_input.bind("<Leave>", hide_tooltip)

btn_clear_output.bind("<Enter>", lambda event: show_tooltip(event, "Очистить поле"))
btn_clear_output.bind("<Leave>", hide_tooltip)

btn_clear_input.bind("<Enter>", lambda event: show_tooltip(event, "Очистить поле"))
btn_clear_input.bind("<Leave>", hide_tooltip)


window.mainloop()