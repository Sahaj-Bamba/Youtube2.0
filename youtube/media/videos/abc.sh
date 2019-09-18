cd /home/sahaj-bamba/Desktop/webster3/Youtube2.0/youtube/media/videos
#pwd
rm -rf ax.txt
chk=0
for i in *
do
  #echo $i
	cmp --silent $i $1
	#echo "$?"
#	pk=$?
#	echo $pk
	if [ "$?" -eq "$chk" ]
	then
	  #echo "Not at all"
		echo $i >> ax.txt
	fi
done
 
