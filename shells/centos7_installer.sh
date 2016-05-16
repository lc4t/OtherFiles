#! /bin/bash




function checkVirualKernel()
{
    yum install wget
    cd /tmp
    wget –N —no–check–certificate https://raw.githubusercontent.com/91yun/code/master/vm_check.sh && bash vm_check.sh
}

function shadowsocksInstall()
{
    yum update
    yum install m2crypto vim gcc python-setuptools wget
    easy_install pip
    pip install shadowsocks
    cd /tmp
    wget https://download.libsodium.org/libsodium/releases/LATEST.tar.gz
    tar zxf LATEST.tar.gz
    cd libsodium*
    ./configure
    make && make install
    echo /usr/local/lib > /etc/ld.so.conf.d/usr_local_lib.conf
    ldconfig

    ### shadowsocks config file
    port=25
    read -p "Input ss port[25]:" port
    password="123456"
    read -p "Input ss password[123456]:" passwd
    filename="shadowsocks.json"
    read -p "Input ss filename[shadowsocks.json]:" filename
    mkdir /etc/shadowsocks
    cd /etc/shadowsocks
    echo "{" > $filename
    echo "\"server\":\"0.0.0.0\"," >> $filename
    echo "\"server_port\":$port," >> $filename
    echo "\"local_address\": \"127.0.0.1\"," >> $filename
    echo "\"local_port\":1080," >> $filename
    echo "\"password\":\"$passwd\"," >> $filename
    echo "\"timeout\":300," >> $filename
    echo "\"method\":\"chacha20\"," >> $filename
    echo "\"fast_open\": true," >> $filename
    echo "\"workers\": 1" >> $filename
    echo "}" >> $filename

}

function supervisorInstall()
{
    yum install pip
    pip install supervisor
    filename="shadowsocks.json"
    read -p "Input ss filename[shadowsocks.json]:" filename
    echo "[program:shadowsocks]" >> /etc/supervisord.conf
    echo "command = ssserver -c /etc/shadowsocks/$filename" >> /etc/supervisord.conf
    echo "user = root" >> /etc/supervisord.conf
    echo "autostart = true" >> /etc/supervisord.conf
    echo "autoresart = true" >> /etc/supervisord.conf
    echo "stderr_logfile = /root/ss.stderr.log" >> /etc/supervisord.conf
    echo "stdout_logfile = /root/ss.stdout.log" >> /etc/supervisord.conf
    supervisord -c /etc/supervisord.conf
    echo "supervisord" >> /etc/rc.local
    chmod +x /etc/rc.local
}

function tcpReset()
{
    echo "fs.file-max = 51200"  > /etc/sysctl.conf
    echo "net.ipv4.tcp_syncookies = 1" >> /etc/sysctl.conf
    echo "net.ipv4.tcp_tw_reuse = 1" >> /etc/sysctl.conf
    echo "net.ipv4.tcp_tw_recycle = 0" >> /etc/sysctl.conf
    echo "net.ipv4.tcp_fin_timeout = 30" >> /etc/sysctl.conf
    echo "net.ipv4.tcp_keepalive_time = 1200" >> /etc/sysctl.conf
    echo "net.ipv4.ip_local_port_range = 10000 65000" >> /etc/sysctl.conf
    echo "net.ipv4.tcp_max_syn_backlog = 8192" >> /etc/sysctl.conf
    echo "net.ipv4.tcp_max_tw_buckets = 5000" >> /etc/sysctl.conf
    echo "net.ipv4.tcp_fastopen = 3" >> /etc/sysctl.conf
    echo "net.core.rmem_max = 67108864" >> /etc/sysctl.conf
    echo "net.core.wmem_max = 67108864" >> /etc/sysctl.conf
    echo "net.ipv4.tcp_rmem = 4096 87380 67108864" >> /etc/sysctl.conf
    echo "net.ipv4.tcp_wmem = 4096 65536 67108864" >> /etc/sysctl.conf
    echo "net.core.netdev_max_backlog = 250000" >> /etc/sysctl.conf
    echo "net.ipv4.tcp_mtu_probing=1" >> /etc/sysctl.conf

    sysctl -p

}

function serverspeederInstall()
{
    yum install wget
    cd /tmp
    wget -N --no-check-certificate https://raw.githubusercontent.com/91yun/serverspeeder/master/serverspeeder-all.sh && bash serverspeeder-all.sh
}

function setSSHD()
{
    noPassword="y"
    read -p "no password and use rsa? y or n[y]" noPassword
    if [ noPassword = "y" ]
        then
            sed -i 's/^[[:space:]]*PasswordAuthentication[[:space:]].*$//g' /etc/ssh/sshd_config
            sed -i 's/^[[:space:]]*PubkeyAuthentication[[:space:]].*$//g' /etc/ssh/sshd_config
            sed -i 's/^[[:space:]]*ChallengeResponseAuthentication[[:space:]].*$//g' /etc/ssh/sshd_config

            echo "PasswordAuthentication no" >> /etc/ssh/sshd_config
            echo "PubkeyAuthentication yes" >> /etc/ssh/sshd_config
            echo "ChallengeResponseAuthentication no" >> /etc/ssh/sshd_config
    fi

    port="22"
    read -p "set the ssh port:[22]" port
    sed -i 's/^[[:space:]]*Port[[:space:]][0-9]*$//g' /etc/ssh/sshd_config
    echo "Port $port" >> /etc/ssh/sshd_config
}

function setHostname()
{
    oldHostname=`cat /etc/hostname`
    newHostname="host"
    read -p "new hostname[host]" newHostname
    sed -i "s/$oldHostname/$newHostname/g" /etc/hosts
}

function nginxInstall()
{
    echo '[nginx]' > /etc/yum.repo.d/nginx.repo
    echo 'name=nginx repo' >> /etc/yum.repo.d/nginx.repo
    echo 'baseurl=http://nginx.org/packages/centos/7/$basearch/' >> /etc/yum.repo.d/nginx.repo
    echo 'gpgcheck=0' >> /etc/yum.repo.d/nginx.repo
    echo 'enabled=1' >> /etc/yum.repo.d/nginx.repo

    yum install nginx
    systemctl start nginx
    systemctl enable nginx
    firewall-cmd --zone=public --add-port=80/tcp --permanent
    firewall-cmd --reload
}


function phpInstall()
{
    yum install php php-fpm php-mysql
    systemctl start php-fpm
    systemctl enable php-fpm
}

function mariadbInstall()
{
    yum install mariadb-server
    systemctl start mariadb
    systemctl enable mariadb
}

function lnmpInstall()
{
    nginxInstall
}

function sqlmapInstall()
{
    yum install git
    cd /opt
    git clone https://github.com/sqlmapproject/sqlmap

    cd /usr/bin
    echo '#!/bin/bash' > sqlmap
    echo 'cd /opt/sqlmap' >> sqlmap
    echo 'python sqlmap.py "$@"' >> sqlmap

}

function nmapInstall()
{
    yum install nmap
}

function metasploitInstall()
{

    yum update
    yum upgrade


    yum groupinstall 'Development Tools'
    yum install sqlite-devel libxslt-devel libxml2-devel java-1.7.0-openjdk libpcap-devel nano openssl-devel zlib-devel libffi-devel gdbm-devel readline-devel nano wget
    nmapInstall
    yum install postgresql-server postgresql-contrib
    postgresql-setup initdb
    systemctl start postgresql
    systemctl enable postgresql
    # exclude=postgresql*
    # cd /tmp
    # wget http://yum.postgresql.org/9.4/redhat/rhel-6-x86_64/pgdg-centos94-9.4-1.noarch.rpm
    # rpm -ivh pgdg-centos94-9.4-1.noarch.rpm
    # # yum update
    # yum install postgresql94-server postgresql94-devel postgresql94
    # postgresql-setup initdb
    # systemctl start postgresql-9.4.service
    # systemctl enable postgresql-9.4.service
    cd /tmp
    wget http://downloads.metasploit.com/data/releases/metasploit-latest-linux-installer.run
    chmod 777 metasploit-latest-linux-installer.run
    ./metasploit-latest-linux-installer.run
}

function main()
{
    userInput='NULL'
    while [ $userInput != 'exit' ] && [ $userInput != 'q' ]
        do
            echo "--------------Console--------------"
            echo "1. checkVirualKernel"
            echo "2. shadowsocksInstall"
            echo "3. supervisorInstall"
            echo "4. tcpReset"
            echo "5. serverspeederInstall"
            echo "6. setSSHD"
            echo "7. setHostname"
            echo "8. lnmpInstall"
            read -p "-->:" -n 5 userInput

            if [ $userInput ]
                then
                    case $userInput in
                                1)
                                    checkVirualKernel
                                    ;;
                                2)
                                    shadowsocksInstall
                                    ;;
                                3)
                                    supervisorInstall
                                    ;;
                                4)
                                    tcpReset
                                    ;;
                                5)
                                    serverspeederInstall
                                    ;;
                                6)
                                    setSSHD
                                    ;;
                                7)
                                    setHostname
                                    ;;

                                'q')
                                    exit
                                    ;;
                                "*")
                                    echo "Ah ha?"
                                    ;;
                    esac
                else
                    userInput='NULL'
                fi
        done
}


main
