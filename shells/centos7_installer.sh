#!/bin/bash




function checkVirualKernel()
{
    cd /tmp
    wget –N —no–check–certificate https://raw.githubusercontent.com/91yun/code/master/vm_check.sh && bash vm_check.sh
}

function shadowsocksInstall()
{
    yum update
    yum install m2crypto gcc python-setuptools
    easy_install pip
    pip install shadowsocks
    cat /etc/ld.so.conf.d/usr_local_lib.conf
    if [ $? -ne 0 ]
        then
            cd /tmp
            wget https://download.libsodium.org/libsodium/releases/LATEST.tar.gz
            tar zxf LATEST.tar.gz
            cd libsodium*
            ./configure
            make && make install
            echo /etc/ld.so.conf.d/usr_local_lib.conf
            echo /usr/local/lib > /etc/ld.so.conf.d/usr_local_lib.conf
            ldconfig
    fi

    ### shadowsocks config file

    read -p "Input ss port[8080]:" port
    if [ "$port" = "" ]
        then
            port=8080
    fi

    read -p "Input ss password[lc4t]:" password
    if [ "$password" = "" ]
        then
            password="lc4t"
    fi


    read -p "Input ss filename[shadowsocks.json]:" filename
    if [ "$filename" = "" ]
        then
            filename="shadowsocks.json"
    fi
    mkdir /etc/shadowsocks
    cd /etc/shadowsocks
    echo '{'                                   >  $filename
    echo '"server":"0.0.0.0",'                  >> $filename
    echo '"server_port":'$port','              >> $filename
    echo '"local_address": "127.0.0.1",'       >> $filename
    echo '"local_port":1080,'                  >> $filename
    echo '"password":"'$password'",'           >> $filename
    echo '"timeout":300,'                      >> $filename
    echo '"method":"chacha20",'                >> $filename
    echo '"fast_open": true,'                  >> $filename
    echo '"workers": 1'                        >> $filename
    echo '}'                                   >> $filename
    ssserver -c /etc/shadowsocks/$filename -d start
}

function supervisorInstall()
{
    cat /etc/supervisord.conf
    if [ $? -ne 0 ]
        then
            easy_install pip
            pip install supervisor
    fi
    filename="shadowsocks.json"
    read -p "Input ss filename[shadowsocks.json]:" filename
    if [ "$filename" = "" ]
        then
            filename="shadowsocks.json"
    fi
    echo_supervisord_conf >/etc/supervisord.conf
    echo "[program:shadowsocks]"                            >> /etc/supervisord.conf
    echo "command = ssserver -c /etc/shadowsocks/$filename" >> /etc/supervisord.conf
    echo "user = root"                                      >> /etc/supervisord.conf
    echo "autostart = true"                                 >> /etc/supervisord.conf
    echo "autoresart = true"                                >> /etc/supervisord.conf
    echo "stderr_logfile = /root/ss.stderr.log"             >> /etc/supervisord.conf
    echo "stdout_logfile = /root/ss.stdout.log"             >> /etc/supervisord.conf
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
    cd /tmp
    wget -N --no-check-certificate https://raw.githubusercontent.com/91yun/serverspeeder/master/serverspeeder-all.sh && bash serverspeeder-all.sh
}

function setSSHD()
{
    read -p "no password and use rsa?[y/n]" noPassword
    if [ "$noPassword" = "" ] || [ "$noPassword" = "Y" ] || [ "$noPassword" = "y" ]
        then
            echo "set..."
            sed -i 's/^[[:space:]]*PasswordAuthentication[[:space:]].*$//g' /etc/ssh/sshd_config
            sed -i 's/^[[:space:]]*PubkeyAuthentication[[:space:]].*$//g' /etc/ssh/sshd_config
            sed -i 's/^[[:space:]]*ChallengeResponseAuthentication[[:space:]].*$//g' /etc/ssh/sshd_config

            echo "PasswordAuthentication no" >> /etc/ssh/sshd_config
            echo "PubkeyAuthentication yes" >> /etc/ssh/sshd_config
            echo "ChallengeResponseAuthentication no" >> /etc/ssh/sshd_config
    else
        echo "NO"
    fi


    read -p "set the ssh port:[22]" port
    if [ "$port" = "" ]
        then
            port=22
    fi
    sed -i 's/^[[:space:]]*Port[[:space:]][0-9]*$//g' /etc/ssh/sshd_config
    echo "Port $port" >> /etc/ssh/sshd_config
}

function setHostname()
{
    oldHostname=`cat /etc/hostname`

    read -p "new hostname[host]" newHostname
    if [ "$newHostname" = "" ]
        then
            newHostname = "host"
    fi
    echo $newHostname > /etc/hostname
    sed -i "s/$oldHostname/$newHostname/g" /etc/hosts
}

function nginxInstall()
{
    echo '[nginx]' > /etc/yum.repos.d/nginx.repo
    echo 'name=nginx repo' >> /etc/yum.repos.d/nginx.repo
    echo 'baseurl=http://nginx.org/packages/centos/7/$basearch/' >> /etc/yum.repos.d/nginx.repo
    echo 'gpgcheck=0' >> /etc/yum.repos.d/nginx.repo
    echo 'enabled=1' >> /etc/yum.repos.d/nginx.repo

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
    mariadbInstall
    phpInstall
}

function sqlmapInstall()
{
    cd /opt
    git clone https://github.com/sqlmapproject/sqlmap

    cd /usr/local/bin
    touch sqlmap
    echo '#!/bin/bash' > sqlmap
    echo 'cd /opt/sqlmap' >> sqlmap
    echo 'python sqlmap.py "$@"' >> sqlmap
    chmod a+x sqlmap
}

function nmapInstall()
{
    yum install nmap
}

function metasploitInstall()
{

    yum update
    yum upgrade


    curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall &&   chmod 755 msfinstall &&   ./msfinstall
    yum install postgresql
    yum install postgresql-server
    postgresql-setup initdb

    echo 'please set this>>>
            host    "msf_database"	"msf_user"      127.0.0.1/32          md5
            host     all             all            127.0.0.1/32          ident
        @/var/lib/pgsql/data/pg_hba.conf'
    read
    systemctl start postgresql.service
    echo 'DO THIS-->(password should \d\w, not !@#$%^&*())
            su postgres
            createuser msf_user -P
            createdb --owner=msf_user msf_database
        '
    read

    systemctl enable postgresql
    systemctl restart postgresql

    cd /opt
    cd metasploit-framework
    bash -c 'for MSF in $(ls meta*); do ln -s /opt/metasploit-framework/$MSF /usr/local/bin/$MSF;done'
    ln -s /opt/metasploit-framework/armitage /usr/local/bin/armitage

    echo 'DO THIS on msf-->
            db_status
            db_connect msf_user:yourmsfpassword@127.0.0.1:5432/msf_database
            db_status
        '


}

function crontabInstall()
{
    yum install cronie
}

function main()
{
    yum update
    yum upgrade
    yum install tmux wget git vim
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
            echo "9. sqlmapInstall"
            echo "10. nmapInstall"
            echo "11. metasploitInstall"
            echo "12. crontabInstall"
            read -p "-->:" userInput

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
                                8)
                                    lnmpInstall
                                    ;;
                                9)
                                    sqlmapInstall
                                    ;;
                                10)
                                    nmapInstall
                                    ;;
                                11)
                                    metasploitInstall
                                    ;;
                                12)
                                    crontabInstall
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
