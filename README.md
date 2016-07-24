####Saltstack with Tornado

######No.1  Salt Config Api
```Bash
https://github.com/luyidong/SaltAdmin/tree/master/salt-api
```
```C
--------------------------------------------------------------------------------------
UR                          结果类型          说明
--------------------------------------------------------------------------------------  /salt/v1/creategroup        True/False        创建项目
/salt/v1/createstate        True/False        项目组推送配置环境php，tomcat，zabbix等   /salt/v1/addnodetate        True/False        单节点推送配置环境php，tomcat，zabbix等
/salt/v1/checkgroup         True/False        验证项目组是否存在                        /salt/v1/checknode          True/False        验证节点是否存在
/salt/v1/checkpillar        True/False        验证Pillar 节点角色 
/salt/v1/checkphp           True/False        验证推送PHP是否成功
/salt/v1/checklogstash      True/False        验证推送Logstaths是否成功
/salt/v1/checkzabbix        True/False        验证推送Zabbix是否成功
```

######No.2  Salt Web UI
```Bash
https://github.com/luyidong/SaltAdmin/tree/master/salt-ui
```
######CMDB Demo
Home
![](https://github.com/luyidong/SaltAdmin/blob/master/salt-ui/screen/home-cmdb.png)
List
![](https://github.com/luyidong/SaltAdmin/blob/master/salt-ui/screen/list-cmdb.png)
Add
![](https://github.com/luyidong/SaltAdmin/blob/master/salt-ui/screen/add-cmdb.png)
Edit
![](https://github.com/luyidong/SaltAdmin/blob/master/salt-ui/screen/edit-cmdb.png)
Delete
![](https://github.com/luyidong/SaltAdmin/blob/master/salt-ui/screen/del-cmdb.png)

