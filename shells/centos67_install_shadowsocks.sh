#! /bin/bash

echo 'install package ...'
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

read -p "Input ss port:" port
read -p "Input ss password:" passwd
echo '''SHADOWSOCKS
{
    "server":"0.0.0.0",
    "server_port":$port,
    "local_address": "127.0.0.1",
    "local_port":1080,
    "password":"$passwd",
    "timeout":300,
    "method":"chacha20",
    "fast_open": true,
    "workers": 1
}
SHADOWSOCKS'''
pip install supervisor

(
    cat <<SUPERVISORDCONF

[program:shadowsocks]
command = ssserver -c /etc/shadowsocks.json
user = root
autostart = true
autoresart = true
# stderr_logfile = /var/log/supervisor/ss.stderr.log
# stdout_logfile = /var/log/supervisor/ss.stdout.log

SUPERVISORDCONF
) >> /etc/supervisord.conf
supervisord -c /etc/supervisord.conf

(
    cat <<RCLOCAL
supervisord

RCLOCAL
) >> /etc/rc.local

chmod +x /etc/rc.local





(
    cat <<TCP
fs.file-max = 51200
#提高整个系统的文件限制
net.ipv4.tcp_syncookies = 1
#表示开启SYN Cookies。当出现SYN等待队列溢出时，启用cookies来处理，可防范少量SYN攻击，默认为0，表示关闭；
net.ipv4.tcp_tw_reuse = 1
#表示开启重用。允许将TIME-WAIT sockets重新用于新的TCP连接，默认为0，表示关闭；
net.ipv4.tcp_tw_recycle = 0
#表示开启TCP连接中TIME-WAIT sockets的快速回收，默认为0，表示关闭；
#为了对NAT设备更友好，建议设置为0。
net.ipv4.tcp_fin_timeout = 30
#修改系統默认的 TIMEOUT 时间。
net.ipv4.tcp_keepalive_time = 1200
#表示当keepalive起用的时候，TCP发送keepalive消息的频度。缺省是2小时，改为20分钟。
net.ipv4.ip_local_port_range = 10000 65000 #表示用于向外连接的端口范围。缺省情况下很小：32768到61000，改为10000到65000。（注意：这里不要将最低值设的太低，否则可能会占用掉正常的端口！）
net.ipv4.tcp_max_syn_backlog = 8192
#表示SYN队列的长度，默认为1024，加大队列长度为8192，可以容纳更多等待连接的网络连接数。
net.ipv4.tcp_max_tw_buckets = 5000
#表示系统同时保持TIME_WAIT的最大数量，如果超过这个数字，TIME_WAIT将立刻被清除并打印警告信息。
#额外的，对于内核版本新于**3.7.1**的，我们可以开启tcp_fastopen：
net.ipv4.tcp_fastopen = 3

# increase TCP max buffer size settable using setsockopt()
net.core.rmem_max = 67108864 
net.core.wmem_max = 67108864 
# increase Linux autotuning TCP buffer limit
net.ipv4.tcp_rmem = 4096 87380 67108864
net.ipv4.tcp_wmem = 4096 65536 67108864
# increase the length of the processor input queue
net.core.netdev_max_backlog = 250000
# recommended for hosts with jumbo frames enabled
net.ipv4.tcp_mtu_probing=1

TCP
) > /etc/sysctl.conf
sysctl -p

echo 'install serverspeeder'
wget -N --no-check-certificate https://raw.githubusercontent.com/91yun/serverspeeder/master/serverspeeder-all.sh && bash serverspeeder-all.sh

