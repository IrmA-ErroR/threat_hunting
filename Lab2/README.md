# Сбор и аналитическая обработка информации о сетевом трафике
Kabanova Svetlana BISO-01-20

# Лабораторная работа №2

# Сбор и аналитическая обработка информации о сетевом трафике

### Цель работы

1.  Развить практические навыки использования современного стека
    инструментов сбора и аналитической обработки информации о сетвом
    трафике
2.  Освоить базовые подходы блокировки нежелательного сетевого трафика
3.  Закрепить знания о современных сетевых протоколах прикладного уровня

## Задание

1.  Собрать сетевой трафик (объемом не менее 100 Мб)
2.  Выделить метаинформацию сетевого трафика с помощью утилиты Zeek
3.  Собрать данные об источниках нежелательного трафика, например –
    https://github.com/StevenBlack
4.  Написать программу на любом удобном языке (python, bash, R …),
    котрая подсчитывает процент нежелательного трафика в собранном на
    этапе 1.

## Ход работы:

### 1 - Сбор сетевого трафика в файл my_trash.pcapng

1.  Использовался сетевой анализатор – Wireshark
2.  Для формирования необходимого объема Интернет был изучен на предмет
    различных “вредных” сайтов.

``` bash
ls -lah /home/irina/threat_hunting/Lab2/data/my_trash.pcapng
```

    -rw------- 1 root root 118M мая  2 23:19 /home/irina/threat_hunting/Lab2/data/my_trash.pcapng

### 2 - Выделение метаинформации сетевого трафика с помощью утилиты Zeek

Zeek сортирует метаинформацию о трафике в соответствующие папки по
протоколам. Нас будет интересовать прежде всего папка DNS запросов.

##### 1. Install zeek (Docker)

    docker pull zeek/zeek:lts

Метаинформация – результат работы Zeek – была перенаправлена в отдельную
папку в подпапке практической работы, /data

##### 2. Run && Analise

``` bash
docker run -w /data -v /home/irina/threat_hunting/Lab2/data:/data zeek/zeek:lts zeek -C -r my_trash.pcapng
```

Запуск докер-контейнера -\> (-v - смонтировать папку с хоста в
контейнер; -w - установить рабочую директорию data)

-\> Запуск zeek в рабочей директории (поскольку, папка смонтирована,
результаты работы zeek копируются из контейнера на хост)

### 3 - Сбор данных об источниках нежелательного трафика из репозитория https://github.com/StevenBlack

``` bash
curl https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts -o hosts
```

      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed

      0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
      1 5624k    1 98286    0     0   415k      0  0:00:13 --:--:--  0:00:13  413k
    100 5624k  100 5624k    0     0  5062k      0  0:00:01  0:00:01 --:--:-- 5066k

### 4 - Подсчет трафика на языке Python

``` python
bad_hosts = [] # нежелательные хосты
with open('hosts') as file:
    for line in file.readlines()[40:]:
        if line[0] == '#':
            continue
        try:
            bad_hosts.append(line.split()[1])
        except IndexError:
            continue
        
hosts = [] # все хосты
with open('data/dns.log') as file:
    for line in file.readlines():
        if line[0] == '#':
            continue
        try:
            hosts.append(line.split()[9])
        except IndexError:
            continue
```

##### Процент нежелательного трафика:

``` python
bad_count = len([host for host in hosts if host in bad_hosts])
percentile = round(bad_count/len(hosts),3)*100
print("Количество нежелательных хостов: {}.".format(str(bad_count)),
"Процент нежелательного трафика: {}%.".format(str(percentile)),sep='\n')
```

    Количество нежелательных хостов: 42.
    Процент нежелательного трафика: 10.5%.
