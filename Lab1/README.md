Kabanova Svetlana BISO-01-20

# Системы аутентификации и защиты от несанкционированного доступа

Лабораторная работа №1

## Цель

Вывести информацию о системе

## Исходные данные

1.  Ноутбук Acer Aspire
2.  ОС Linux Kali
3.  VS Code
4.  Командная оболочка Zsh
5.  Интерпретатор языка R 4.2.2

## Задача

Собрать информацию о системе при помощи встроенных утилит.

## План

1.  Выведем информацию о системе
2.  Выведем информацию о процессоре, оперативной памяти, дисках
3.  Выведем информацио о последних 30-ти логах системы

## Шаги

1\. Выполним команду `uname -a` для получения сведений об используемом
дистрибутиве:

``` zsh
lsb_release -a
```

    Distributor ID: Kali
    Description:    Kali GNU/Linux Rolling
    Release:    2023.1
    Codename:   kali-rolling

Получим сведения о версии ядра:

``` zsh
uname -a
```

    Linux kali 6.1.0-kali7-amd64 #1 SMP PREEMPT_DYNAMIC Debian 6.1.20-1kali1 (2023-03-22) x86_64 GNU/Linux

2\. Выведем информацию о процессоре:

``` zsh
lscpu | grep -v Vulnerability
```

    Architecture:                    x86_64
    CPU op-mode(s):                  32-bit, 64-bit
    Address sizes:                   40 bits physical, 48 bits virtual
    Byte Order:                      Little Endian
    CPU(s):                          4
    On-line CPU(s) list:             0-3
    Vendor ID:                       AuthenticAMD
    Model name:                      AMD Ryzen 7 4700U with Radeon Graphics
    CPU family:                      23
    Model:                           96
    Thread(s) per core:              1
    Core(s) per socket:              2
    Socket(s):                       2
    Stepping:                        1
    BogoMIPS:                        3992.38
    Flags:                           fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush mmx fxsr sse sse2 ht syscall nx mmxext rdtscp lm constant_tsc rep_good nopl tsc_reliable nonstop_tsc cpuid extd_apicid tsc_known_freq pni pclmulqdq ssse3 fma cx16 sse4_1 sse4_2 movbe popcnt aes xsave avx hypervisor lahf_lm abm sse4a misalignsse 3dnowprefetch osvw ssbd vmmcall arat overflow_recov succor
    Hypervisor vendor:               VMware
    Virtualization type:             full
    L1d cache:                       128 KiB (4 instances)
    L1i cache:                       128 KiB (4 instances)
    L2 cache:                        2 MiB (4 instances)
    L3 cache:                        32 MiB (4 instances)
    NUMA node(s):                    1
    NUMA node0 CPU(s):               0-3

*- исключая строки об уязвимостях ядра*

Теперь об оперативной памяти:

``` zsh
free -h
```

                   total        used        free      shared  buff/cache   available
    Mem:           3.8Gi       2.5Gi       820Mi       144Mi       977Mi       1.3Gi
    Swap:          1.0Gi       825Mi       198Mi

*- show human-readable output*

Получим информацию о дисках:

``` zsh
df -ht ext4
```

    Filesystem      Size  Used Avail Use% Mounted on
    /dev/sda1        79G   16G   59G  22% /

*- вывод человекочитаемого вида указаной файловой системы*

3\. Выведем последние 30 строк логов:

``` zsh
journalctl | tail -n 30
```

    Apr 02 14:15:01 kali CRON[86178]: (root) CMD (command -v debian-sa1 > /dev/null && debian-sa1 1 1)
    Apr 02 14:15:01 kali CRON[86177]: pam_unix(cron:session): session closed for user root
    Apr 02 14:17:01 kali CRON[87166]: pam_unix(cron:session): session opened for user root(uid=0) by (uid=0)
    Apr 02 14:17:01 kali CRON[87167]: (root) CMD (cd / && run-parts --report /etc/cron.hourly)
    Apr 02 14:17:01 kali CRON[87166]: pam_unix(cron:session): session closed for user root
    Apr 02 14:20:06 kali dbus-daemon[1139]: [session uid=1000 pid=1139] Activating service name='org.xfce.Xfconf' requested by ':1.22' (uid=1000 pid=1286 comm="xfsettingsd")
    Apr 02 14:20:06 kali dbus-daemon[1139]: [session uid=1000 pid=1139] Successfully activated service 'org.xfce.Xfconf'
    Apr 02 14:20:37 kali dbus-daemon[637]: [system] Activating via systemd: service name='org.bluez' unit='dbus-org.bluez.service' requested by ':1.158' (uid=1000 pid=88953 comm="/usr/share/code/code --unity-launch --enable-crash")
    Apr 02 14:20:37 kali dbus-daemon[637]: [system] Activation via systemd failed for unit 'dbus-org.bluez.service': Unit dbus-org.bluez.service not found.
    Apr 02 14:20:43 kali dbus-daemon[637]: [system] Activating via systemd: service name='org.freedesktop.hostname1' unit='dbus-org.freedesktop.hostname1.service' requested by ':1.128' (uid=1000 pid=8151 comm="/usr/share/code/code --unity-launch --enable-crash")
    Apr 02 14:20:43 kali systemd[1]: Starting systemd-hostnamed.service - Hostname Service...
    Apr 02 14:20:43 kali dbus-daemon[637]: [system] Successfully activated service 'org.freedesktop.hostname1'
    Apr 02 14:20:43 kali systemd[1]: Started systemd-hostnamed.service - Hostname Service.
    Apr 02 14:21:13 kali systemd[1]: systemd-hostnamed.service: Deactivated successfully.
    Apr 02 14:25:01 kali CRON[91615]: pam_unix(cron:session): session opened for user root(uid=0) by (uid=0)
    Apr 02 14:25:01 kali CRON[91616]: (root) CMD (command -v debian-sa1 > /dev/null && debian-sa1 1 1)
    Apr 02 14:25:01 kali CRON[91615]: pam_unix(cron:session): session closed for user root
    Apr 02 14:25:23 kali NetworkManager[712]: <info>  [1680459923.4747] dhcp4 (eth0): state changed new lease, address=192.168.79.128
    Apr 02 14:31:10 kali dbus-daemon[1139]: [session uid=1000 pid=1139] Activating service name='org.xfce.Xfconf' requested by ':1.22' (uid=1000 pid=1286 comm="xfsettingsd")
    Apr 02 14:31:10 kali dbus-daemon[1139]: [session uid=1000 pid=1139] Successfully activated service 'org.xfce.Xfconf'
    Apr 02 14:35:01 kali CRON[98350]: pam_unix(cron:session): session opened for user root(uid=0) by (uid=0)
    Apr 02 14:35:01 kali CRON[98351]: (root) CMD (command -v debian-sa1 > /dev/null && debian-sa1 1 1)
    Apr 02 14:35:01 kali CRON[98350]: pam_unix(cron:session): session closed for user root
    Apr 02 14:39:01 kali CRON[100310]: pam_unix(cron:session): session opened for user root(uid=0) by (uid=0)
    Apr 02 14:39:01 kali CRON[100311]: (root) CMD (  [ -x /usr/lib/php/sessionclean ] && if [ ! -d /run/systemd/system ]; then /usr/lib/php/sessionclean; fi)
    Apr 02 14:39:01 kali CRON[100310]: pam_unix(cron:session): session closed for user root
    Apr 02 14:39:01 kali systemd[1]: Starting phpsessionclean.service - Clean php session files...
    Apr 02 14:39:01 kali systemd[1]: phpsessionclean.service: Deactivated successfully.
    Apr 02 14:39:01 kali systemd[1]: Finished phpsessionclean.service - Clean php session files.
    Apr 02 14:40:23 kali NetworkManager[712]: <info>  [1680460823.4753] dhcp4 (eth0): state changed new lease, address=192.168.79.128

## Оценка результата

В результате лабораторной работы была получена основная информация об
ОС, процессоре, оперативной памяти и логи используемой системы.

## Вывод

Таким образом. мы научились, используя команды Linux, получать сведения
о системе.
