#!/bin/bash

LOGFILE="system_log.txt"

pause(){
    read -p "Press Enter to continue..."
}

system_info(){
    clear
    echo "== SYSTEM INFO =="
    uname -a
    echo ""
    lsb_release -a
    echo ""
    date
    echo ""
    hostname
    echo ""
    whoami
    echo ""
    pause
}

disk_usage(){
    clear
    echo "== DISK USAGE =="
    df -h
    echo ""
    pause
}

memory_usage(){
    clear
    echo "== MEMORY USAGE =="
    free -h
    echo ""
    pause
}

cpu_info(){
    clear
    echo "== CPU INFO =="
    lscpu
    echo ""
    pause
}

network_info(){
    clear
    echo "== NETWORK INFO =="
    ifconfig
    echo ""
    pause
}

running_process(){
    clear
    echo "== RUNNING PROCESS =="
    ps aux | head -20
    echo ""
    pause
}

docker_status(){
    clear
    echo "== DOCKER STATUS =="
    systemctl status docker
    pause
}

current_users(){
    clear
    echo "== CURRENT USERS =="
    who
    echo ""
    pause
}

uptime_info(){
    clear
    echo "== SYSTEM UPTIME =="
    uptime
    echo ""
    pause
}

kernel_info(){
    clear
    echo "== KERNEL INFO =="
    uname -r
    echo ""
    pause
}

top_memory_process(){
    clear
    echo "== TOP MEMORY PROCESS =="
    ps aux --sort=-%mem | head
    echo ""
    pause
}

top_cpu_process(){
    clear
    echo "== TOP CPU PROCESS =="
    ps aux --sort=-%cpu | head
    echo ""
    pause
}

list_directory(){
    clear
    echo "== CURRENT DIRECTORY =="
    pwd
    echo ""
    ls -la
    echo ""
    pause
}

create_backup(){
    clear
    echo "== BACKUP =="
    tar -czf backup.tar.gz ~/shaktidb-work
    echo "Backup created."
    echo ""
    pause
}

write_log(){
    clear
    echo "== WRITING LOG =="
    echo "System log generated on $(date)" >> $LOGFILE
    uname -a >> $LOGFILE
    free -h >> $LOGFILE
    df -h >> $LOGFILE
    echo "Log written."
    echo ""
    pause
}

while true
do
    clear

    echo "====="
    echo "      Developer Setup Tool"
    echo "====="
    echo ""
    echo "1. System Information"
    echo "2. Disk Usage"
    echo "3. Memory Usage"
    echo "4. CPU Information"
    echo "5. Network Information"
    echo "6. Running Processes"
    echo "7. Docker Status"
    echo "8. Current Users"
    echo "9. Uptime Information"
    echo "10. Kernel Information"
    echo "11. Top Memory Processes"
    echo "12. Top CPU Processes"
    echo "13. List Current Directory"
    echo "14. Create Backup"
    echo "15. Write System Log"
    echo "16. Exit"
    echo ""

    read -p "Enter your choice: " choice

    case $choice in

        1)
            system_info
            ;;

        2)
            disk_usage
            ;;

        3)
            memory_usage
            ;;

        4)
            cpu_info
            ;;

        5)
            network_info
            ;;

        6)
            running_process
            ;;

        7)
            docker_status
            ;;

        8)
            current_users
            ;;

        9)
            uptime_info
            ;;

        10)
            kernel_info
            ;;

        11)
            top_memory_process
            ;;

        12)
            top_cpu_process
            ;;

        13)
            list_directory
            ;;

        14)
            create_backup
            ;;

        15)
            write_log
            ;;

        16)
            echo "Exiting..."
            exit
            ;;

        *)
            echo "Invalid Choice"
            pause
            ;;

    esac

done