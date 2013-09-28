#!/bin/sh
backupPath=~/backup/;
path=`pwd`/;
if [ "$path" != "$backupPath" ]; then
for file in $@; do
curdate=`date +%Y%m%d%H%M%S`;
cp $file $backupPath;
mv ~/backup/$file $backupPath$file.$curdate;
done
fi
rm $@
