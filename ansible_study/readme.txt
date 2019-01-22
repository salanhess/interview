ansible 分别生成不同的模板文件
https://stackoverflow.com/questions/31142369/how-to-use-template-module-with-different-set-of-variables
var_a:
  -
    var_1: 'this is var_a1'
    var_2: 'this is var_a2'
var_b:
  -
    var_1: 'this is var_b1'
    var_2: 'this is var_b2'

{{ item.var_1 }}
{{ item.var_2 }}	

如何ansible playbook 模板化 循环生成节点
#kfstore node name and ip  list
 wos_node_num: 3
 wos_node_name_list: ["A04-R08-I245-133-BCSVLP2.JCLOUD.COM", "A04-R08-I245-164-BDDQLP2.JCLOUD.COM", "A04-R08-I245-200-BD0PLP2.JCLOUD.COM"]
 wos_node_ip_list: ["192.168.245.133","192.168.245.164","192.168.245.200"]

 
                {% for i in range(0, wos_node_num) %}
                {
                    "serviceName" : "{{ wos_node_name_list[i] }}",
                    "boundAddr" : ["{{ wos_node_ip_list[i] }}:{{ wos_node_port }}"],
                    "triggerUseDefaultNP" : true
                },
                {% endfor %}

对应config文件为：
#wos-node name and ip  list
 wos_node_num: 2
 wos_node_name_list: ["zbs-staging-api", "zbs-staging-datanode1"]
 wos_node_ip_list: ["10.226.139.66","10.226.139.67"]

 
2019年1月21日10:28:50
ansible 如何获取ip并进行校验配置
已知问题， ip必须从小到大，依次设定，否则会乱掉，失败

 24     - name: get role ip
 25       shell: "hostname -I | cut -d' ' -f1"
 26       register: roleip
 27       ignore_errors: False
 28
 29     - name: get ip check
 30       debug: var=roleip
 31
 32     - name: get ip check2
 33       debug: var=roleip.stdout_lines[0]
 34
 35     - name: get ip check3
 36       debug: var=roleip.stdout_lines[0]
 37       when: roleip.stdout_lines[0] ==  node1
 38
 39     - name: get ip check4
 40       debug: var=roleip.stdout_lines[0]
 41       when: roleip.stdout_lines[0] ==  node2

 75     - name: loop check ip map-hash
 76       debug:
 77         msg: "{{ item.ip }} use {{ item.vol }}"
 78       when: roleip.stdout_lines[0] == {{ item.ip }}
 79       with_items:
 80         - { ip: node1,vol: vol1 }
 81         - { ip: node2,vol: vol2 }
 82         - { ip: node3,vol: vol2 }
 83
 84     - name: Final loop-together ip and vol
 85       debug:
 86         msg: "{{ item.0 }} and {{ item.1 }}"
 87       when: roleip.stdout_lines[0] == item.0
 88       with_together:
 89         - "{{ ex_nodelist }}"
 90         - "{{ ex_vollist }}"

# ansible-playbook -i hosts test.yml --private-key=id_rsa --extra-vars '{"ex_nodelist":[ "192.168.xx","192.168.xx" ],"ex_vollist":[ "vol-66","vol-67" ]}'

2019年1月20日10:28:50
如何将Jenkins中的变量传给playbook并进行split等处理
http://jfactory.jcloud.com/job/iaas/view/disk/job/iaas_cloud-disk_cfs-kfstore_dist/configure
字符参数： CMPT_LIST  ==》 默认值  kfstore,wosAdmin
zbs-dist/build_zfs/Makefile:4:CMPT_LIST := ${CMPT_LIST}
zbs-dist/build_zfs/Makefile:25:   -e  bin_name_list_str=${CMPT_LIST} \
变量名变为bin_name_list_str

 20 - name: build zfs
 21   shell: |
 22     cd {{ zfs_repo_path }}/{{ cmpt_dir }}
 23     mkdir -p {{ bin_path }}
 24     make clean && make
 25     mv {{ item }} {{ bin_path }}/{{ item }}-{{ git_commitid.stdout }}
 26   environment:
 27     GOPATH: "{{ go_path }}"
 28   with_items:
 29     - "{{ bin_name_list_str.split(',') }}"


