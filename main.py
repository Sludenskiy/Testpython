#Library
import time

#Answers
p = 0
answer1 = 2
answer2 = 3
answer3 = 2
answer4 = 1
answer5 = 2
answer6 = 1
answer7 = 2
answer8 = 3
answer9 = 2
answer10 = 4
answer11 = 1
answer12 = 2
answer13 = 1
answer14 = 2
answer15 = 1

#Welcome to test
name = input("Введите ваше имя: ")
time.sleep(1)
print("Приветствую,", name)
time.sleep(1)
print("Давайте пройдем тест по ОФП!")
time.sleep(1)
print("Начинаем!")

#Test
time.sleep(0.5)
question1 = int(input("Физическая подготовка - это?\n 1) Простые упражнения, тренировки\n 2) Основная составляющая физического воспитания человека\n"))
if (question1==answer1):
    p=p+1
    print("Ответ правильный!")
else:
    print("Ошибка!")
time.sleep(0.5)
question2 = int(input("Какие наиболее важные виды движения человека являются?\n 1) Прыжки, лежать на кровати, делать пробежку\n 2) Метания, прыжки со скал, бег\n 3) Ходьба, бег, прыжки, метания, плавание, преодоление препятствий\n"))
if (question2==answer2):
    p=p+1
    print("Ответ правильный!")
else:
    print("Ошибка!")
time.sleep(0.5)
question3 = int(input("Что развивает физическая подготовка у людей?\n 1) Лень, гибкость\n 2) Сила, выносливость, быстрота, гибкость, ловкоcть\n 3) Только выносливость и силу\n 4) Ничего\n"))
if (question3==answer3):
    p=p+1
    print("Ответ правильный!")
else:
    print("Ошибка!")
time.sleep(0.5)
question4 = int(input("При физической подготовке можно-ли изменять функциональное состояние организма?\n 1) Да\n 2) Нет\n"))
if (question4==answer4):
    p=p+1
    print("Ответ правильный!")
else:
    print("Ошибка!")
time.sleep(0.5)
question5 = int(input("Физическое воспитание - это?\n 1) Простое формирование навыков\n 2) Педагогический процесс, направленный на формирование специальных знаний, умений и навыков\n 3) Прокачивание выносливости\n"))
if (question5==answer5):
    p=p+1
    print("Ответ правильный!")
else:
    print("Ошибка!")
time.sleep(0.5)
question6 = int(input("В физическом воспитании, какие различают две специфические стороны?\n 1) Обучение движениям и развитие физических качеств\n 2) Никаких\n 3) Трудовая и военная\n"))
if (question6==answer6):
    p=p+1
    print("Ответ правильный!")
else:
    print("Ошибка!")
time.sleep(0.5)
question7 = int(input("ОФП - это?\n 1) Умственное развитие человека\n 2) Процесс совершенствования двигательных качеств, направленных на всесторонее и гармоническое физическое развитие человека\n 3) Только физическое развитие\n"))
if (question7==answer7):
    p=p+1
    print("Ответ правильный!")
else:
    print("Ошибка!")
time.sleep(0.5)
question8 = int(input("Какие два вида физической подготовки есть?\n 1) Никаких\n 2) Общая подготовка\n 3) Общая и специальная физическая подготовка\n"))
if (question8==answer8):
    p=p+1
    print("Ответ правильный!")
else:
    print("Ошибка!")
time.sleep(0.5)
question9 = int(input("Какие виды секций по спорту есть в КиП ФИН?\n 1) Баскетбол, футбол\n 2) Баскетбол, футбол, волейбол, мини-футбол, настольный теннис и др.\n 3) Только волейбол\n"))
if (question9==answer9):
    p=p+1
    print("Ответ правильный!")
else:
    print("Ошибка!")
time.sleep(0.5)
question10 = int(input("Какие языки были использованы во верстке сайтов?\n 1)HTML & CSS\n 2) JavaScript & HTML\n 3) HTML\n 4) HTML, CSS, JavaScript\n"))
if (question10==answer10):
    p=p+1
    print("Ответ правильный!")
else:
    print("Ошибка!")
time.sleep(0.5)
question11 = int(input("Какие важные документы/файлы нужны для верстки и стилизации?\n 1) index.html & style.css\n 2) Только index.html\n"))
if (question11==answer11):
    p=p+1
    print("Ответ правильный!")
else:
    print("Ошибка!")
time.sleep(0.5)
question12 = int(input("Что содержит в себе тег <body>?\n 1) Картинку\n 2) Содержание сайта\n 3) Ничего\n"))
if (question12==answer12):
    p=p+1
    print("Ответ правильный!")
else:
    print("Ошибка!")
time.sleep(0.5)
question13 = int(input("Тег <nav> это?\n 1) Навигация по сайту\n 2) Текст\n 3) Видеофайл\n"))
if (question13==answer13):
    p=p+1
    print("Ответ правильный!")
else:
    print("Ошибка!")
time.sleep(0.5)
question14 = int(input("В каком языке лучше делать анимацию/переходы/видеоматериалы для сайта?\n 1) Никакой\n 2) JavaScript & HTML\n 3) JavaScript\n"))
if (question14==answer14):
    p=p+1
    print("Ответ правильный!")
else:
    print("Ошибка!")
time.sleep(0.5)
question15 = int(input("Какой редактор кода более адаптирован для верстки сайта?\n 1) VS code, sublime text 3, brackets\n 2) Конструктор сайтов\n 3) Site.google\n"))
if (question15==answer15):
    p=p+1
    print("Ответ правильный!")
else:
    print("Ошибка!")

#Points
if (p>=15):
    print("Вы прошли тест!", "Набрано очков: ", p)
else:
    print("Вы не прошли тест!","Набрано очков: ", p)
input()