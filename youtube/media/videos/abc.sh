cd /home/sahaj-bamba/Desktop/webster3/Youtube2.0/youtube/media/videos
rm -rf ax.txt
for i in * 
do 
	cmp --silent $i $1
	if (( $? == 0 ))
	then
		echo $i >> ax.txt 
	fi
done
 
