#! /bin/bash
Server_create(){
    read -p '[Enter Your ip-address]--->' ip
    read -p '[Enter Port number]--->' port
    cp Data/Main/Server.py Data/tmp
    sed -i "s/ipaddress/$ip/g" Data/tmp/Server.py
    sed -i "s/number/$port/g" Data/tmp/Server.py
}
Server_join(){
    read -p '[Enter Server ip-adress]--->' ip_server
    read -p '[Enter Server port]--->' port_server
    cp Data/Main/Client.py Data/tmp
    sed -i "s/ipaddress/$ip_server/g" Data/tmp/Client.py
    sed -i "s/number/$port_server/g" Data/tmp/Client.py
}
Banner(){
    clear
    figlet "EvilMassage"
    echo "[@]##################################################[@]"
}
Question1(){
    echo "[1]---[Create Server]"
    echo "[2]---[Join Server]"
    read -p '[Enter the number]--->' ans1
    case $ans1 in 
       [1] ) clear
              echo "[@]---[You Selected number]-->[1]" | pv -qL 20;
               Server_create
               python Data/tmp/Server.py
        ;;
       [2] ) clear 
              echo "[@]---[You Selected number]-->[2]" | pv -qL 20;
              Server_join
              python Data/tmp/Client.py 
        ;;      
    esac              
}

Banner
Question1