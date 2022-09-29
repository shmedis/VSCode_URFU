# Игра угадай число
# Компьютер сам загадывает и сам угадывает число

import numpy as np
import math

# Определяем функцию, которая угадывает случайное число
def random_predict(number: int = 1) -> int: #передаем на вход случайное натуральное число
    
    count = 0
    mini = 100
    lis = []
    
    # формируем список чисел убывающей геометрической прогрессии для работы алгоритма
    while mini != 1:
        lis.append(math.ceil(mini / 2))
        mini = math.ceil(mini / 2)
    
    # задаем первое предиктивное число из элементов прогрессии
    last = lis[0]

    # идем циклам по элементам прогрессии, начиная с первого
    for i in lis:
        count += 1
        predict_number = last
        
        # если предиктивное число меньше загаданного, увеличиваем следующее предиктивное число на следующий элемент прогрессии
        if number > predict_number:
            last += lis[count]
         # если предиктивное число больше загаданного, уменьшаем следующее предиктивное число на следующий элемент прогрессии
        elif number < predict_number:
            last -= lis[count]
        else:
            break  # выход из цикла если угадали
            
    return count


# Определяем функцию, которая определяет среднюю эффективность алгоритма
def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
