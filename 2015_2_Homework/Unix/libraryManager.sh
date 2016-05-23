#! /bin/bash

function checkLibraryDatabase()
{
    if [ -f './library' ]
        then
            echo "Database exists."
    else
        touch library
    fi
}

checkLibraryDatabase


function view()
{
    echo "$1" | awk -F ':' 'BEGIN {                 print "\n"
                                                    print "Find---------->"
                                                }
                                                {
                                                    print "Title:"$1
                                                    print "Author:"$2
                                                    print "Category:"$3
                                                    print "Status:"$4
                                                    print "bname:"$5
                                                    print "date:"$6":"$7":"$8
                                                    print "--------------"
                                                }
                                            END{
                                                    print "\n"
                                               }'
}

function add()
{
    clear
    read -p "Title:" title
    read -p "Author:" author
    read -p "Category:" category
    status='in'
    bname='null'
    date="`date`"
    echo -e "$title:$author:$category:$status:$bname:$date" >> library
    read -n 1 -p "Do you want to add more[y/n]:" userAnswer
    # exit
    if [ "$userAnswer" = "y" ] || [ "$userAnswer" = "Y" ]
        then
            add
    fi
    return
}

function updateStatus()
{
    clear

    read -p "Book title:" title


    found=`grep "^$title:" library`
    # echo "$found"

    if [ "$?" = "0" ]
        then
            IFS=$'\n'
            for line in `echo "$found"`
                do
                    Title=`echo "$line" | cut -d ':' -f 1 `
                    Author=`echo "$line" | cut -d ':' -f 2`
                    Category=`echo "$line" | cut -d ':' -f 3`
                    status=`echo "$line" | cut -d ':' -f 4`
                    bname=`echo "$line" | cut -d ':' -f 5`
                    sed -i "/$line/d" library
                    date="`date`"

                    if [ "$status" = "in" ]
                        then
                            # echo $line
                            view $line

                            echo -e "Linux Library - \033[;;1m UPDATE STATUS MODE\033[0m"
                            read -p "Input bname:" bname
                            echo "Title: $Title"
                            echo "Author: $Author"
                            echo "Category: $Category"
                            echo "Status: $status"
                            echo "New Status: out"
                            status="out"
                            echo "Check out by:$bname"
                            echo "Date:$date"

                            read -n 1 -p "update?[y/n]" userAnswer
                            if [ "$userAnswer" = "y" ] || [ "$userAnswer" = "Y" ]
                                then
                                    echo "$Title:$Author:$Category:$status:$bname:$date" >> library
                                    clear
                            else
                                echo "$line" >> library
                            fi

                    elif [ "$status" = "out" ]   # out
                        then
                            echo "Title: $Title"
                            echo "Author: $Author"
                            echo "Category: $Category"
                            echo "Status: $status"
                            echo "Check out by:$bname"
                            echo "Date:$date"
                            echo ""
                            echo "New Status: in"
                            status="in"

                            read -n 1 -p  "update?[y/n]" userAnswer
                            if [ "$userAnswer" = "y" ] || [ "$userAnswer" = "Y" ]
                                then
                                    echo "$Title:$Author:$Category:$status:$bname:$date" >> library
                                    clear
                            else
                                echo "$line" >> library
                            fi

                    else
                        echo "No such book:)"
                    fi


                done
    else
        echo "No such book:)"
    fi

    read -n 1 -p  "Any more to update?[y/n]" userAnswer
    if [ "$userAnswer" = "y" ] || [ "$userAnswer" = "Y" ]
        then
            clear
            updateStatus
    fi
    clear

    return

}

function display()
{
    clear

    read -p "Enter the Author/Title>" userQuery
    found=`grep -E "(^$userQuery:.*)|(^[^:]*:$userQuery:.*)$" library`
    if [ "$?" = '0' ]
        then
            view $found
    else
        echo "No such book:)"
    fi
    read -n 1 -p "Any more to look for?[y/n]:" userAnswer
    if [ "$userAnswer" = "y" ] || [ "$userAnswer" = "Y" ]
        then
            display
    fi
    return
}

function delete()
{
    clear
    read -p "Book title:" title

    found=`grep "^$title:" library`
    if [ "$?" = '0' ]
        then
            view $found
            echo -n "Do you want to delete?"
            read -n 1 -p "[y/n]:" userAnswer
            if [ "$userAnswer" = "y" ] || [ "$userAnswer" = "Y" ]
                then
                    sed -i "/^$title:/d" library
            fi
            clear
    else
        echo "No such book:)"
    fi

    read -n 1 -p "Do you want to delete more[y/n]:" userAnswer
    if [ "$userAnswer" = "y" ] || [ "$userAnswer" = "Y" ]
        then
            delete
    fi
    return

}

function editMenu()
{

    while [ true ]
    do
        clear
        echo -e "Linux Library - \033[;;1m EDIT MENU\033[0m"
        echo -e "0: \033[;;1m RETURN\033[0m to the main menu"
        echo -e "1: \033[;;1m ADD\033[0m Menu"
        echo -e "2: \033[;;1m UPDATE STATUS\033[0m Menu"
        echo -e "3: \033[;;1m DISPLAY\033[0m this program"
        echo -e "4: \033[;;1m DELETE\033[0m Menu"

        echo -n "Enter your choice>_"
        echo -e -n "\033[1D\033[0m"
        read -n 1 userInput

        if [ "$userInput" = "0" ]
            then
                return
        elif [ "$userInput" = "1" ]
            then
                add
        elif [ "$userInput" = "2" ]
            then
                updateStatus
        elif [ "$userInput" = "3" ]
            then
                display
        elif [ "$userInput" = "4" ]
            then
                delete
        else
            error
        fi
    done

}




function reportsMenu()
{

    while [ true ]
    do
        clear
        echo -e "Linux Library - \033[;;1m REPORTS MENU\033[0m"
        echo -e "0: \033[;;1m RETURN\033[0m to the main menu"
        echo -e "1: sorted by \033[;;1m TITLE\033[0m"
        echo -e "2: sorted by \033[;;1m AUTHOR\033[0m Menu"
        echo -e "3: sorted by \033[;;1m CATEGORY\033[0m"

        echo -n "Enter your choice>_"
        echo -e -n "\033[1D\033[0m"
        read -n 1 userInput

        if [ "$userInput" = "0" ]
            then
                return
        elif [ "$userInput" = "1" ] || [ "$userInput" = "2" ] || [ "$userInput" = "3" ]
            then
                content=`cat library | sort -t ':' -k $userInput`
                IFS=$'\n'
                output=""
                for line in `echo "$content"`
                    do
                        output=${output}`view $line`
                    done
                echo "$output" | more
                pauseNotEnter
        else
            error
        fi
    done
}


function error()
{
    echo -e "\n Wrong Input. Try again.\nPress any key to continue...>_"
    read -n 1
    clear
}

function pause()
{
    echo -n "Please enter and key to continue..."
    read -n 1
}

function pauseNotEnter()
{
    ifs=$IFS
    IFS=
    while [ true ]
    do
        echo -n "Please enter and key(not \n) to continue..."
        read -n 1
        [[ -z $REPLY ]] && echo "Cannot use \n to kill" || break
    done
    IFS=$ifs
}

function LLIB()
{
    clear
    echo -e "\033[;33;1mLinux Library Manager\033[0m"
    echo -e "\n\n\n"
    echo "This is the Linux Library application"
    pause

    userInput="null"

    while [ true ]
    do
        clear
        echo -e "Linux Library - \033[;;1m MAIN MENU\033[0m"
        echo -e "0: \033[;;1m EXIT\033[0m this program"
        echo -e "1: \033[;;1m EDIT\033[0m Menu"
        echo -e "2: \033[;;1m REPORTS\033[0m Menu"

        echo -n "Enter your choice>_"
        echo -e -n "\033[1D\033[0m"
        read -n 1 userInput

        if [ "$userInput" = "0" ]
            then
                exit
        elif [ "$userInput" = "1" ]
            then
                editMenu
        elif [ "$userInput" = "2" ]
            then
                reportsMenu
        else
            error
        fi
    done
}

LLIB
