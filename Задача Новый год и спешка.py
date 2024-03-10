tasks, minutes = map(int, input().split())

times_for_task = 0 #
total_time_task = 0 #
count_task = 0 #
time_left_for_tasks = 240 - minutes
time_on_next_task = 0

while time_left_for_tasks - total_time_task >= time_on_next_task and tasks > 0 and time_left_for_tasks != 0:  # Пока время выполнения задач + данное время меньше 240 выполняем цикл
    tasks -= 1
    count_task+=1                                                                # Выполняем первое задание
    times_for_task = count_task * 5                                              # Время на выполнения текущего задания
    total_time_task = times_for_task + total_time_task                           # Прибавляем к общему времени, время выполнения текущих заданий
    time_on_next_task = (count_task + 1) * 5                                     # Тут нужен счетчик который будет считать сколько времени понадобиться на выполнение следующей задачи

print(count_task)