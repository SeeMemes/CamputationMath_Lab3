import matplotlib.pyplot as plt
import math
import numpy as np


def func1(x3, x2, x1, k, a, b, n):
    answer = 'По методу центральных прямоугольников ' + rect_mid(x3, x2, x1, k, a, b, eps, n)
    answer += 'По методу левых прямоугольников ' + rect_left(x3, x2, x1, k, a, b, eps, n)
    answer += 'По методу правых прямоугольников ' + rect_right(x3, x2, x1, k, a, b, eps, n)
    return answer


def rect_mid(x3, x2, x1, k, a, b, n):
    step = (b - a) / n
    summa = 0
    for i in range(0, n):
        summa += f(a + step / 2, x3, x2, x1, k)
        a += step
    summa *= step
    return 'ответ: ' + str(summa) + '. Решено за ' + str(n) + ' шага' + '\n'


def rect_left(x3, x2, x1, k, a, b, n):
    step = (b - a) / n
    summa = 0
    for i in range(0, n):
        summa += f(a, x3, x2, x1, k)
        a += step
    summa *= step
    return 'ответ: ' + str(summa) + '. Решено за ' + str(n) + ' шага' + '\n'


def rect_right(x3, x2, x1, k, a, b, n):
    step = (b - a) / n
    a += step
    summa = 0
    for i in range(0, n):
        summa += f(a, x3, x2, x1, k)
        a += step
    summa *= step
    return 'ответ: ' + str(summa) + '. Решено за ' + str(n) + ' шага' + '\n'


def func2(x3, x2, x1, k, a, b, n):
    step = (b - a) / n
    sum = 0
    for i in range(0, n):
        y0 = f(a, x3, x2, x1, k)
        a += step
        yn = f(a, x3, x2, x1, k)
        sum += step * (y0 + yn) / 2
    return 'По методу трапеций ответ: ' + str(sum) + '. Решено за ' + str(n) + ' шага.'


def func3(x3, x2, x1, k, a, b, n):
    step = (b - a) / n
    x0 = f(a, x3, x2, x1, k)
    a += step
    xn = f(b, x3, x2, x1, k)
    sum_1 = 0
    sum_2 = 0
    for i in range(1, n):
        if (i % 2 == 0):
            sum_2 += f(a, x3, x2, x1, k)
        else:
            sum_1 += f(a, x3, x2, x1, k)
        a += step
    answer = step * (x0 + xn + 2 * sum_2 + 4 * sum_1) / 3
    return 'Ответ: ' + str(answer) + '. Решено за ' + str(n) + ' шага.'


def f(x, x3, x2, x1, k):
    return x3 * pow(x, 3) + x2 * pow(x, 2) + x1 * x + k


def max_f2(x3, x2, a, b):
    return max((6 * x3 * a + 2 * x2), (6 * x3 * b + 2 * x2))


def printGraph(a, b):
    fig, ax = plt.subplots()
    x = np.linspace(a, b, 1000)
    y = f(x, x3, x2, x1, k)
    ax.plot(x, y)
    plt.show()


if __name__ == '__main__':

    n = 4

    answerGiven = True
    scannerline = True

    while scannerline:
        print('Ввод из файла/из строки (1/0): ')
        mes = input()
        if mes == '1':
            try:
                pathh = open('lol', 'r')
                x3, x2, x1, k = map(float, pathh.readline().split(' '))
                a, b = map(float, pathh.readline().split(' '))
                eps = float(pathh.readline())
                #n = int(pathh.readline())

                answerGiven = True
                scannerline = False
            finally:
                pathh.close()
        else:
            print('Коэффициент перед x^3: ')
            x3 = float(input())
            print('Коэффициент перед x^2: ')
            x2 = float(input())
            print('Коэффициент перед x^1: ')
            x1 = float(input())
            print('Свободный член: ')
            k = float(input())
            print('Левая граница приближения: ')
            a = float(input())
            print('Правая граница приближения: ')
            b = float(input())
            print('Погрешность: ')
            eps = float(input())
            #print('Начальное число разбиения')
            #n = int(input())
            answerGiven = True
            scannerline = False

    print('Выберите метод: \n' +
          '1. Метод прямоугольников \n' +
          '2. Метод трапеций \n' +
          '3. Метод Симпсона \n' +
          'Ваш ответ: ')
    answer = ''

    while answerGiven:
        give = input()
        if give == '1':
            printGraph(a, b)
            n = max(round(math.sqrt(max_f2(x3,x2,a,b)*(b-a)**3/(24*eps)))+1,n)
            answer = func1(x3, x2, x1, k, a, b, n)
            answerGiven = False
        elif give == '2':
            printGraph(a, b)
            n = max(round(math.sqrt(max_f2(x3,x2,a,b)*(b-a)**3/(12*eps)))+1,n)
            answer = func2(x3, x2, x1, k, a, b, n)
            answerGiven = False
        elif give == '3':
            printGraph(a, b)
            answer = func3(x3, x2, x1, k, a, b, n)
            answerGiven = False
        else:
            print('Ошибка: не тот номер \n' +
                  'попробуйте еще раз')
            continue

    print('Вывести в файл/консоль(1/0)')
    viv = input()
    if viv == '1':
        try:
            with open('l.txt', 'w') as file:
                file.writelines(answer)
        except:
            print("Ошибка: решений нет")
        finally:
            file.close()
    else:
        if (answer != 0):
            print(answer)
        else:
            print("Ошибка: решений нет")
