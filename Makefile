init:
	curl https://dlcdn.apache.org/logging/log4j/2.16.0/apache-log4j-2.17.0-bin.zip
	unzip apache-log4j-2.17.0-bin.zip
run:
	python3 patch_log4j.py
check:
	find /mnt/c/AnypointStudio -name "log4j*.jar" -type f
restore:
	cp -rpf /mnt/c/OriginalAnypointStudio /mnt/c/AnypointStudio
