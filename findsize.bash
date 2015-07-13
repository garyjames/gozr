echo user,filecount,totalsize
for U in $(ls -d $*/*); do
    FCOUNT=0
    TOTALSIZE=0
    for FILE in $(find $U -type f 2>/dev/null); do
	FCOUNT=$((FCOUNT + 1))
        FSIZE=$(du -b $FILE 2>/dev/null |cut -f1)
	TOTALSIZE=$((TOTALSIZE + FSIZE))
    done
    echo $(basename $U),$FCOUNT,$TOTALSIZE 
done
