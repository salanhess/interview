#!/usr/bin/env bash
kill_all ()
{
	kill 9 `ps aux |grep "[v]olumemgr.cfg" |awk -F " " '{print $2}'`
	sleep 1
	kill 9 `ps aux |grep "[c]hunknode0.cfg" |awk -F " " '{print $2}'`
	sleep 1
	kill 9 `ps aux |grep "[c]hunknode1.cfg" |awk -F " " '{print $2}'`
	sleep 1
	kill 9 `ps aux |grep "[m]onitor.cfg" |awk -F " " '{print $2}'`
	sleep 1
	kill 9 `ps aux |grep "[p]roxy" |awk -F " " '{print $2}'`
	sleep 1
	kill 9 `ps aux |grep "[r]ecoverynode.cfg" |awk -F " " '{print $2}'`
	sleep 1
	kill 9 `ps aux |grep "[w]eb.cfg" |awk -F " " '{print $2}'`
	sleep 1
	return 0
}
echo "start kill"
kill_all
kill_all
echo "finished kill"
echo "restart sequence: web > volumemgr > chunknodes > proxy > recovernode > monitor > gatewaymgr and serv"
cd /export/App/bhebs
nohup ./web -conf web.cfg >bh_web.out 2>&1 &
sleep 5
nohup ./ebs_volumemgr -c volumemgr.cfg >bhvm.out 2>&1 &
sleep 5
nohup ./ebs_chunknode -c chunknode0.cfg > bh_chunknode0.out 2>&1 &
sleep 5
nohup ./ebs_chunknode -c chunknode1.cfg > bh_chunknode1.out 2>&1 &
sleep 5
nohup ./proxy -h 192.168.171.48 -e ebs-root-bh -z 192.168.172.80:2181,192.168.172.80:2182,192.168.172.80:2183>proxy.out 2>&1 &
sleep 5
nohup ./ebs_recoverynode -c recoverynode.cfg > bh_recoverynode.out 2>&1 &
sleep 5
nohup ./ebs_monitor -c monitor.cfg >bh_monitor.out 2>&1 &
ps aux |grep [c]fg
ps aux |grep [p]roxy
