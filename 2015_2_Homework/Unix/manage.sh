#! /usr/bin/sh

function disk()
{
    du -ks $@ | sort -n  | awk '
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
                                    $2 = sprintf("%s%s%s%s", "\033[40;46m", $2, " use max", "\033[01m");
                                    print $2;
                                }'
}

# disk /home/*




function findLargeFile()
{
    du -a $@ | sort -n -r | awk '
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
                                            }'
}

# findLargeFile ~/Downloads

function cppRowCountSum()
{
    find $@ -name "*.cpp" -o -name "*.h" | xargs wc -l
}


# cppRowCountSum ~/Documents/git/WebServer