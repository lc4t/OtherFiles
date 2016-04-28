#! /usr/bin/sh

function disk()
{
    echo 'Loading...'
    sudo du -ks $@ | sort -n  | awk '
                                BEGIN{
                                    FS="\t";
                                    OFS="\t";
                                    split("K,M,G,T",unit, ",");
                                    }
                                {
                                    count = 1;
                                    while ($1 > 1024)
                                    {
                                        $1 = $1 / 1024;
                                        count += 1;
                                    }
                                    $1 = sprintf("%.1f%s", $1, unit[count]);
                                    sub(/\.0/, "", $1);
                                    sub(/\/home\//, "", $2);
                                    print $0;
                                }
                                END{
                                    #$2 = sprintf("%s%s%s%s", "\033[40;01m", $2, " use max", "\033[01m");
                                    $2 = sprintf("%s%s", $2, " use max");
                                    print $2;
                                }' 2>/dev/null
    echo ''
}

# disk /home/*




function findLargeFile()
{   
    echo 'Loading...'
    # ls -alR $@ | grep ^- | sort -n -k 5 | tail -1     # no path to this file
    sudo du -a $@ | sort -n -r | awk '
                                BEGIN{
                                    FS="\t";
                                    OFS="\t";
                                }
                                {

                                    if (system(sprintf("%s%s", "test -d ", $2)))
                                    {
                                        print $0;
                                        exit;
                                    }
                                }' 2>/dev/null
    echo ''
}

# findLargeFile ~/Downloads

function cppRowCountSum()
{
    echo 'Loading...'
    sudo find $@ -name "*.cpp" -o -name "*.h" | xargs wc -l 2>/dev/null
    echo ''
}


# cppRowCountSum ~/Documents/git/WebServer


function checkOnline()
{
    count=`who | grep $@ | wc -l`
    if [ $count -eq 0 ]
        then
            echo $@ is Offline
        else
            echo $@ has $count Online
    fi
    echo ''
}


# checkOnline lc4t


function checkService()
{
    command service >/dev/null 2>/dev/null
    if [ $? -eq 1 ]
        then
            # echo 'service command is found'
            controller="service"
    else
            command systemctl >/dev/null 2>/dev/null
            if [ $? -eq 0 ]
                then
                    # echo 'systemctl command is found'
                    controller="systemctl"
            else
                    echo 'Not install service|systemctl'
            fi
    fi
    echo '[Usage]'
    echo '       [status|start|stop] {vsftpd|apache2|httpd|docker|shadowsocks...}'
    echo 'input error will return back'
    read option serviceName
    if [ $option ] && [ $serviceName ]
        then
            if [ $controller ]
                then
                    case $controller in
                        "service")
                            # echo "service enable"
                            sudo service $serviceName $option
                            ;;
                        "systemctl")
                            # echo "systemctl enable";
                            sudo systemctl $option $serviceName
                            ;;
                        "*")
                            echo "Ah ha?"
                            ;;
                    esac
            fi
            # echo 'input error, return back'
    fi
}



# checkService


function main()
{
    userInput='NULL' 
    while [ $userInput != 'exit' ] && [ $userInput != 'q' ]
        do
            echo '       Please input the NUM.'
            echo '<---------------- MENU ---------------->';
            echo '<--- 1. check disk use by user -------->';
            echo '<--- 2. find the largest file in user-->';
            echo '<--- 3. sum cpp/h file row count ------>';
            echo '<--- 4. check user online ------------->';
            echo '<--- 5. manage service ---------------->';
            echo '[input exit|q will exit me]';
            read userInput
            if [ $userInput ]
                then
                    case $userInput in
                                1)
                                    disk /home/*
                                    ;;
                                2)
                                    echo -n 'Input User:'
                                    read user
                                    if [ -d '/home/'$user ]
                                        then
                                            findLargeFile '/home/'$user
                                        else
                                            echo 'Not exists this user'
                                    fi
                                    ;;
                                3)
                                    echo -n 'Input User:'
                                    read user
                                    if [ -d '/home/'$user ]
                                        then
                                            cppRowCountSum '/home/'$user
                                        else
                                            echo 'Not exists this user'
                                    fi
                                    ;;
                                4)
                                    echo -n 'Input User:'
                                    read user
                                    if [ -d '/home/'$user ]
                                        then
                                            checkOnline $user
                                        else
                                            echo 'Not exists this user'
                                    fi
                                    ;;
                                5)
                                    checkService
                                    ;;
                                'exit')
                                    exit
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
