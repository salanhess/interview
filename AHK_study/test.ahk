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

#i::
Var =
(InvalidVolumeStatus   = -1
	CreatingVolume        = 0 
	AvailableVolume       = 1 
	InUseVolume           = 2 
	DeleteingVolume       = 3 
	DeletedVolume         = 4 
	ExtendingVolume       = 5 
	RestoringVolume       = 6 
	ErrorCreatingVolume   = 7 
	ErrorExtendingVolume  = 8 
	ErrorDeletingVolume   = 9 
	ErrorRestoringVolume  = 10
	RecycledVolume        = 11
	ErrorRecycledVolume   = 12
	CreatingSnapshot      = 20
	AvailableSnapshot     = 21
	InUseSnapshot         = 22
	DeleteingSnapshot     = 23
	DeletedSnapshot       = 24
	ErrorCreatingSnapshot = 25
	ErrorDeletingSnapshot = 26
	ErrorRecycledSnapshot = 27
	RecyclingSnapshot     = 28
	RecycledSnapshot      = 29
	VolumeAttaching       = 30
	VolumeDetaching       = 31
	VolumeAttached        = 32
	VolumeDetached        = 33
	ErrorVolumeAttach     = 34
	ErrorVolumeDetach     = 35
	DB_TASK_STATUS_BEGIN      = 1
	DB_TASK_STATUS_INPROGRESS = 2
	DB_TASK_STATUS_SUCCESS    = 3
	DB_TASK_STATUS_FAILED     = 4
    InvalidFileSystemStatus    = -1
    CreatingFileSystem         = 0  //The filesystem is being created.
    AvailableFileSystem        = 1  //The filesystem is ready to attach to an instance.
    InUseFileSystem            = 2  //The filesystem is attached to an instance.
    DeleteingFileSystem        = 3  //The filesystem is being deleted.
    DeletedFileSystem          = 4  //The filesystem has been deleted.
    ExtendingFileSystem        = 5  //The filesystem is being extended
    RestoringFileSystem        = 6  //A backup is being restored to the filesystem.
    ErrorCreatingFileSystem    = 7  //A filesystem creation error occurred.
    ErrorExtendingFileSystem   = 8  //An error occurred while attempting to extend a filesystem.
    ErrorDeletingFileSystem    = 9  //A filesystem deletion error occurred.
    ErrorRestoringFileSystem   = 10 //A backup restoration error occurred.
    RecycledFileSystem         = 11 // filesystem recycled
    ErrorRecycledFileSystem    = 12 // filesystem recycled error
    ErrorDescribeMdsFileSystem = 13
        //OpenAPI 订单状态码，3至20以下为中间状态，20以上为最终状态
	ORDER_INVALID        int = -1 //无效（已删除）
	ORDER_INIT           int = 1  //初始状态
	ORDER_START_CREATE   int = 3  //开始生产
	ORDER_START_CHECK    int = 4  //开始检查
	ORDER_PRE_SUCCESS    int = 5  //成功前处理
	ORDER_ROLLBACK       int = 10 //回滚
	ORDER_SUCCESS        int = 11 //成功
	ORDER_FAIL           int = 12 //失败
	ORDER_SUCCESS_FINISH int = 20 //成功终止
	ORDER_FAIL_FINISH    int = 21 //失败终止
	ORDER_EXPIRED_FINISH int = 30 //超时终止
)
MsgBox, %Var% `n
return

::gotest::>log1 && go test -v x.go |tee x.out && less x.out
::pause::read -n 1 -p "Press any key to continue..."
::2>::2>&1 &
::builderX::ansible-playbook -i inventories/hd_test_env1/hosts main.yml -e"component=builder,server,scheduler,gateway,storage build_flag=local version_flag=latest"
::|py::|python -mjson.tool
::|perl::|perl -pe 's/(Error)/\e[1;31m$1\e[0m/g'
::|awk::|awk '{{}print $1{}}'
::fiorw::fio -direct=1 -iodepth 1 -thread -rw=randrw -rwmixread=70 -ioengine=psync -bs=16k -size=10M -numjobs=10 -runtime=10 -group_reporting -name=mytest -filename=/dev/nbd22
::fiow::fio -direct=1 -iodepth 1 -thread -rw=randwrite -ioengine=psync -bs=16k -size=10M -numjobs=10 -runtime=10 -group_reporting -name=mytest -filename=/dev/nbd22
::fior::fio -direct=1 -iodepth 1 -thread -rw=randread -ioengine=psync -bs=16k -size=10M -numjobs=10 -runtime=10 -group_reporting -name=mytest -filename=/dev/nbd22
::ddw::dd if=/dev/zero bs=1M count=1 oflag=direct of=/dev/nbd22
::ddr::dd of=/dev/null bs=1M count=1 iflag=direct if=/dev/nbd22
::ddmd5::dd if=/dev/nbd201 bs=1M count=1 2>  /dev/null | md5sum  | awk '{{}print $1{}}'
::history::history |grep 
::./ebs::./ebs -h "192.168.172.80:2181" -root=ebs-root
::./cm::rm -f doneGroup.txt && ./cmpgroups -config volumemgr.cfg -volid 6 && tail -f /export/Logs/ebs/vmm/compgroup_warn.log
::ps::ps aux |grep -v grep|grep ebs
::.48::192.168.171.48
::select::select * from
::selectorder::select * from disk_open_api.order where request_id='xx' \G;
::selectvol::select id,volume_name,size,pool_id,az_name,action,tenant_id,status,cluster_name,created_at from volume where id in ('');
::selectattach::select * from volume_attachment where status in (32) and volume_id in ('');
::selectfile::select id,fs_name,status,action,created_at from filesystem where id in ('');
::selectsnap::select id,tenant_id,snapshot_name,size,volume_id,pool_id,az_name,created_at,status,snapshot_dst,share,percent,snapshot_type,cluster_name,created_at from snapshot where id='xxx';
::order::order by id DESC limit 10\G
::mysqlX::mysql -uroot -pJcloud00 volumemgr
::sp::set paste
::nu::set nu
::nonu::set nonu
::blkt::blktrace -d /dev/nbd50 -o - |blkparse -i-
::lsblk::lsblk -o NAME,PARTUUID
::myrm::myrm(){{} D=/tmp/$(date {+}%Y%m%d%H%M%S); mkdir -p $D; mv "$@" $D && echo "moved to $D ok"; {}} && alias rm='myrm'
::gitlog::git log --graph --pretty=oneline --abbrev-commit |head -n 5
::tmuxatt::tmux attach-session -t 
::fdisk1::fdisk -l |grep /dev |grep -v vda
::fdisk2::echo "Manually INPUT:n,p,1,enter,enter,wq.Then format fdisk /dev/vdc" && fdisk /dev/vdb
::fdisk3::mkfs -t ext4 /dev/vdb1
::fdisk4::echo "Then mkdir -p /mnt/vdc1 && mount -t ext4 /dev/vdc1 /mnt/vdc1 via fdisk4_1" && mkdir -p /mnt/vdb1 && mount -t ext4 /dev/vdb1 /mnt/vdb1
::fdisk4_1::mkdir -p /mnt/vdc1 && mount -t ext4 /dev/vdc1 /mnt/vdc1
::fdisk5::df -h |egrep "vdb|vdc"
::fdisk6::echo {`}date{`} > /mnt/vdb1/date.log && cat /mnt/vdb1/date.log && echo {`}date{`} > /mnt/vdc1/date.log && cat /mnt/vdc1/date.log
::fdisk7::echo "Writedata,newdisk via fdisk7_1" && dd if=/dev/urandom bs=100M count=1 oflag=direct of=/mnt/vdb1/test.data && sleep 1s && dd if=/mnt/vdb1/test.data  bs=100M count=1 2>  /dev/null | md5sum  | awk '{{}print $1{}}'
::fdisk7_1::dd if=/dev/urandom bs=200M count=1 oflag=direct of=/mnt/vdc1/test.data && sleep 1s && dd if=/mnt/vdc1/test.data  bs=200M count=1 2>  /dev/null | md5sum  | awk '{{}print $1{}}'
::fdisk8::echo "remount other disk via fdisk8_1" && mkdir -p /mnt/vdf1 && mount -t ext4 /dev/vdf1 /mnt/vdd1 && ls -lh /mnt/vdf1
::fdisk8_1::echo "fdisk8_1, mount old disk" && mkdir -p /mnt/vdj1 && mount -t ext4 /dev/vdj1 /mnt/vdj1 && ls -lh /mnt/vdj1
::fdisk9_1::echo "fdisk9_1,check md5" && dd if=/mnt/vdi1/test.data  bs=200M count=1 2>  /dev/null | md5sum
