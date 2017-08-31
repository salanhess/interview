; ! means Alt ,^  means Ctrl, + means shift ,# means Win

#n::
Run Notepad
return

#d::
Run D:\Study\ShutDown.bat
return

; redefine xShell for baoleiji reconnect
#c::
Send !c
sleep 2
Send ^+r
sleep 1
return

#k::
Run D:\Study\StartUP.bat
return

::2>::2>&1 &
::|py::|python -mjson.tool
::|awk::|awk '{{}print $1{}}'
::fiorw::fio -direct=1 -iodepth 1 -thread -rw=randrw -rwmixread=70 -ioengine=psync -bs=16k -size=10M -numjobs=10 -runtime=10 -group_reporting -name=mytest -filename=/dev/nbd22
::fiow::fio -direct=1 -iodepth 1 -thread -rw=randwrite -ioengine=psync -bs=16k -size=10M -numjobs=10 -runtime=10 -group_reporting -name=mytest -filename=/dev/nbd22
::fior::fio -direct=1 -iodepth 1 -thread -rw=randread -ioengine=psync -bs=16k -size=10M -numjobs=10 -runtime=10 -group_reporting -name=mytest -filename=/dev/nbd22
::ddw::dd if=/dev/zero bs=1M count=1 oflag=direct of=/dev/nbd22
::ddr::dd of=/dev/null bs=1M count=1 iflag=direct if=/dev/nbd22
::history::history |grep 
::./ebs::./ebs -h "192.168.XXX.80:2181" -root=ebs-root
::./cm::rm -f doneGroup.txt && ./cmpgroups -config volumemgr.cfg -volid 6 && tail -f /export/Logs/ebs/vmm/compgroup_warn.log
::ps::ps ax |grep -v grep|grep ebs
::.48::192.168.XXX.48
::select::select * from
::order::order by id DESC limit 10\G
::mysqlX::mysql -uroot -pXXXX
::sp::set paste
::blkt::blktrace -d /dev/nbd50 -o - |blkparse -i-
::myrm::myrm(){{} D=/tmp/$(date {+}%Y%m%d%H%M%S); mkdir -p $D; mv "$@" $D && echo "moved to $D ok"; {}} && alias rm='myrm'
