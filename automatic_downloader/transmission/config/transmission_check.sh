#/bin/bash

PID=$(/bin/pidof transmission-daemon)

if [ "$PID" == "" ] ; then
	echo "Transmission daemon is not running"
	/bin/transmission-daemon -w /storage/videos -g /storage/.transmission-daemon --incomplete-dir /storage/incoming --watch-dir /storage/watch -a '*.*.*.*' -T
fi

