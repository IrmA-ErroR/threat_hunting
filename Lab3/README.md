# Сбор и аналитическая обработка информации о сетевом трафике
Kabanova Svetlana BISO-01-20

# Лабораторная работа №3

# Развертывание системы мониторинга ELK Stack (Opensearch)

## Цель работы

1.  Освоить базовые подходы централизованного сбора и накопления
    информации
2.  Освоить современные инструменты развертывания контейнирозованных
    приложений
3.  Закрепить знания о современных сетевых протоколах прикладного уровня

## Задание

1.  Развернуть систему мониторинга на базе Opensearch
    -   Opensearch
    -   Beats (Filebeat, Packetbeat)
    -   OpenSearch Dashboards
2.  Настроить сбор информации о сетевом трафике
3.  Настроить сбор информации из файлов журналов (лог-файлов)
4.  Оформить отчет в соответствии с шаблоном

## Ход работы:

##### 0. Important host settings

Before launching OpenSearch you should review some important system
settings that can impact the performance of your services.

Disable memory paging and swapping performance on the host to improve
performance.

        sudo swapoff -a

Increase the number of memory maps available to OpenSearch.

        sudo vi /etc/sysctl.conf

        vm.max_map_count=262144

        sudo sysctl -p

        cat /proc/sys/vm/max_map_count

##### 1. Run OpenSearch in a Docker container

    docker pull opensearchproject/opensearch:latest
    docker pull opensearchproject/opensearch-dashboards:latest

##### 2. Docker-compose настраивался по [инструкции](https://opensearch.org/docs/latest/install-and-configure/install-opensearch/docker/)

#### Beats (Filebeat, Packetbeat)

#### OpenSearch Dashboards

### 2. Сбор информации о сетевом трафике

### 3. Сбор информации из файлов журналов (лог-файлов)