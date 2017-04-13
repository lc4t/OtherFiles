#! /bin/bash

function scan_dir()
{
	echo -e "\033[34m [*]start dir $1 \033[0m"
	if [ -d "$1" ]
	then
		echo -e "\033[32m [+]cd $1 \033[0m"
		`cd $1`
		`git pull 2>>/dev/null`
		for new_item in `ls $1`
		do
			if [ -d "$1/$new_item" ]
			then
				scan_dir "$1/$new_item"
				echo -e "\033[33m [-]cd .. \033[0m"
				`cd ..`
			fi
		done
	else
		echo -e "\033[31m $1 is not folder \033[0m"
	fi
}

path=`pwd`
echo -e "\033[34m [*]now here $path \033[0m"
echo -n ' input start path or enter for here:'
read input;

if [ -n "$input" ]
then
	path=$input
fi
echo -e "\033[34m [*]set path $path \033[0m"
scan_dir $path
