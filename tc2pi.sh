#!/bin/sh

USER='username'
PASS='password'

prog='mount.cifs //10.0.1.1/Data /mnt/tc -o user='${USER}',pass='${PASS}',sec=ntlm,rw,uid=1000,iocharset=utf8'
uprog='umount /mnt/tc'

start() {
        $prog
}

stop() {
        $uprog
        return
}

# See how we were called.
case "$1" in
  start)
        start
        ;;
  stop)
        stop
        ;;
  *)
        echo $"Usage: $0 {start|stop}"
        exit 2
esac
