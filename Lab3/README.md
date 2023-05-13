# Сбор и аналитическая обработка информации о сетевом трафике
Kabanova Svetlana BISO-01-20

# Лабораторная работа №3

# Развертывание системы мониторинга ELK Stack

## Цель работы

1.  Освоить базовые подходы централизованного сбора и накопления
    информации
2.  Освоить современные инструменты развертывания контейнирозованных
    приложений
3.  Закрепить знания о современных сетевых протоколах прикладного уровня

## Задание

1.  Развернуть систему мониторинга на базе Elasticsearch
    -   Elasticsearch
    -   Beats (Filebeat, Packetbeat)
    -   Kibana
2.  Настроить сбор информации о сетевом трафике
3.  Настроить сбор информации из файлов журналов (лог-файлов)
4.  Оформить отчет в соответствии с шаблоном

## Ход работы:

##### 0. Important host settings

Before launching Elasticsearch you should review some important system
settings that can impact the performance of your services.

Disable memory paging and swapping performance on the host to improve
performance.

        sudo swapoff -a

Increase the number of memory maps available to Elasticsearch.

        sudo vi /etc/sysctl.conf

        vm.max_map_count=262144

        sudo sysctl -p

        cat /proc/sys/vm/max_map_count

##### 1. Run Elasticsearch in a Docker container

##### 2. Docker-compose

#### Beats (Filebeat, Packetbeat)

#### Kibana

### 2. Сбор информации о сетевом трафике

### 3. Сбор информации из файлов журналов (лог-файлов)

## Оценка результата

## Вывод
