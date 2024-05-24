Файл предоставляет пошаговую инструкцию по повторной установке DPDK на стенд, замещению нужных файлов в DPDK и по запуску программы-балансировщика.

Шаг 1:
Запустить стенд с DPDK и проверить, установлен ли DPDK согласно инструкции:
Примечание: Данное описание установки написано для конкретного сервера с ОС Ubuntu. Для других машин или более подробно можно найти по https://doc.dpdk.org/guides/linux_gsg/sys_reqs.html#compilation-of-the-dpdk.

1.1) Установка зависимостей
- sudo apt install pkg-config
- sudo apt install build-essential
- sudo apt install python3-pip
- sudo pip3 install meson ninja
- sudo apt install python3-pyelftools
- sudo apt install libnuma-dev

1.2) Установка hugepages
- sudo mkdir /mnt/huge
- sudo mount -t hugetlbfs pagesize=1GB /mnt/huge

1.3) Установка и сборка dpdk
- git clone https://github.com/DPDK/dpdk.git

- cd dpdk
- meson setup -Dexamples=all build
- cd build
- ninja
- meson install
- sudo ldconfig
- cd ..

- sudo su
- echo 1 > /sys/module/vfio/parameters/enable_unsafe_noiommu_mode
- exit

Проверить существующие девайсы с помощью:
- ./usertools/dpdk-devbind.py --status

В моем случае это было:
Network devices using kernel driver
===================================
0000:06:00.0 'I350 Gigabit Network Connection 1521' if=eno2 drv=igb unused=vfio-pci *Active*
0000:06:00.1 'I350 Gigabit Network Connection 1521' if=eno3 drv=igb unused=vfio-pci *Active*
0000:06:00.2 'I350 Gigabit Network Connection 1521' if=eno4 drv=igb unused=vfio-pci 
0000:06:00.3 'I350 Gigabit Network Connection 1521' if=eno5 drv=igb unused=vfio-pci 
0000:11:00.0 'MT27500 Family [ConnectX-3] 1003' if=enp17s0d1,enp17s0 drv=mlx4_core unused=vfio-pci 

No 'Baseband' devices detected
==============================
...

1.4) Передача интерфейсов во владение dpdk, могут быть переданы только интерфейсы с незаданным ip
- sudo ./usertools/dpdk-devbind.py --bind=vfio-pci 06:00.2
- sudo ./usertools/dpdk-devbind.py --bind=vfio-pci 06:00.3 

1.5) Настройка hugepages в dpdk
- sudo modprobe vfio-pci
- sudo ./usertools/dpdk-hugepages.py -p 1G --setup 2G
- cd build

1.6) Тестовый запуск примера
- sudo ./examples/dpdk-helloworld -l 0-3 -n 4

1.7) (дополнительно) В случае перезагрузки машины требуется заново настроить hugepages и интерфейсы
// из директории dpdk/

- sudo su
- echo 1 > /sys/module/vfio/parameters/enable_unsafe_noiommu_mode
- exit

- sudo ./usertools/dpdk-hugepages.py -p 1G --setup 2G
- sudo ./usertools/dpdk-devbind.py --bind=vfio-pci 06:00.1
- sudo ./usertools/dpdk-devbind.py --bind=vfio-pci 06:00.2

1.8) (дополнительно) Запуск примеров
Cервер с DPDK (admsys@dpdk-flowlet-1, 172.21.253.4)

// из директории dpdk/build/
- sudo ./examples/dpdk-eventdev_pipeline -l 0,2,8-15 --vdev event_sw0 -- -r1 -t1 -e4 -w FF00 -s1 -n10 -c32
или
- sudo ./examples/dpdk-l2fwd -l 0-3 -n 4 -- -q 8 -p 7 --portmap="(0,1)"

Сервер для генерации пакетов (admsys@dpdk-flowlet-2, 172.21.253.13)

- sudo scapy
// посылка 1 пакета
- sendp(Ether()/IP(dst="172.21.253.13")/UDP(dport=999,sport=666)/"HELLO!",iface="enp4s0f1")

// посылка 256 пакетов
- sendp(Ether()/IP(dst="172.21.253.13", src="2.2.2.2/24")/UDP(dport=999,sport=666)/"HELLO!",iface="enp4s0f1")

Пример вывода для eventdev_pipeline (завершение по Сtrl + C):

Port Workload distribution:
worker 0 :      12.5 % (98 pkts)
worker 1 :      12.5 % (98 pkts)
worker 2 :      12.5 % (98 pkts)
worker 3 :      12.5 % (98 pkts)
worker 4 :      12.5 % (98 pkts)
worker 5 :      12.5 % (98 pkts)
worker 6 :      12.4 % (97 pkts)
worker 7 :      12.4 % (97 pkts)

Пример вывода для l2fd:

Port statistics ====================================
Statistics for port 0 ------------------------------
Packets sent:                     1542
Packets received:                    5
Packets dropped:                     0
Statistics for port 1 ------------------------------
Packets sent:                        5
Packets received:                 1542
Packets dropped:                     0
Aggregate statistics ===============================
Total packets sent:               1547
Total packets received:           1547
Total packets dropped:               0
====================================================

Шаг 2: 
Выбрав метод балансировки, начать замещение нужных файлов на стенде файлами из папки метода:
Папка rr соответствует методу балансировки сегментов Round Robin;
Папка lc соответствует методу балансировки сегментов Least Connections;
Папка rb соответствует методу балансировки сегментов Resource Based;
Папка hash соответствует методу балансировки сегментов Hash Scheduling;

Заместить файлы:
dpdk/lib/distributor/rte_distributor.c
dpdk/lib/distributor/rte_distributor.h
dpdk/examples/distributor/main.c

Шаг 3:
Прописать следующие команды:
- cd /home/admsys/dpdk/build
- meson install
(после этой команды придется один раз нажать согласие, а именно 'y')
- sudo ./examples/dpdk-distributor -l 1-9,22 -n 4 -- -p f
После выполнения этих команд запустится программа балансировщика и будет ожидать входящих пакетов.
Для выключения программы используйте Ctrl + C.

Шаг 4:
Для запуска пакетов на первый сервер необходимо зайти на второй сервер и прописать следующую команду:
- sudo python3 packet_sender.py
После этого на выбор пользователю будут предоставлены следующие команды:
1) rnd_send NUM - команда, засылающая 256 пакетов с разными ID флоулетов на
первый сервер NUM раз (ID встречаются повторно каждые 256 раз);
2) fix_send NUM - команда, отправляющая NUM пакетов с одинаковым id флоулета;
3) file_send PATH NUM - команда, отправляющая пакеты, содержащиеся в файле с
путем PATH NUM раз;
4) testing PATH NUM - команда, запускающая NUM экспериментов, используя файлы 
из директории PATH;
