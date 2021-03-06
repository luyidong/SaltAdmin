####Saltstack Config Api with Tornado
```C
--------------------------------------------------------------------------------------
UR                          结果类型          说明                                     
--------------------------------------------------------------------------------------
/salt/v1/creategroup        True/False        创建项目                                  
/salt/v1/createstate        True/False        项目组推送配置环境php，tomcat，zabbix等   
/salt/v1/addnodetate        True/False        单节点推送配置环境php，tomcat，zabbix等  
/salt/v1/checkgroup         True/False        验证项目组是否存在                        
/salt/v1/checknode          True/False        验证节点是否存在
/salt/v1/checkpillar        True/False        验证Pillar 节点角色
/salt/v1/checkphp           True/False        验证推送PHP是否成功
/salt/v1/checklogstash      True/False        验证推送Logstaths是否成功
/salt/v1/checkzabbix        True/False        验证推送Zabbix是否成功
```

######启动脚本
```Bash
python app.py -log_file_prefix=./test.log 
```

#####Ex.
######新建节点
```Bash
curl  http://saltmaster:9191/salt/v1/creategroup?program=community-view\&env=online\&node=community-view01.idc,community-view02.idc\&soft=java
curl  http://saltmaster:9191/salt/v1/createnode?program=community-view\&env=online\&node=community-view01.idc,community-view02.idc\&soft=java
curl  http://saltmaster:9191/salt/v1/createstate?program=community-view\&env=online\&node=community-view01.idc,community-view02.idc\&soft=java
curl  http://saltmaster:9191/salt/v1/createstate?program=community-view\&env=online\&node=community-view01.idc,community-view02.idc\&soft=logstash
curl  http://saltmaster:9191/salt/v1/createstate?program=community-view\&env=online\&node=community-view01.idc,community-view02.idc\&soft=zabbix
curl  http://saltmaster:9191/salt/v1/createstate?program=community-view\&env=online\&node=community-view01.idc,community-view02.idc\&soft=rundeck
curl  http://saltmaster:9191/salt/v1/createrundeck?program=community-view\&env=online\&node=community-view01.idc,community-view02.idc\&soft=rundeck
```
######扩容节点
```Bash
  curl  http://saltmaster:9191/salt/v1/creategroup?program=community-view\&env=online\&node=community-view03.idc\&soft=java
  curl  http://saltmaster:9191/salt/v1/createnode?program=community-view\&env=online\&node=community-view03.idc\&soft=java
  curl  http://saltmaster:9191/salt/v1/addnodestate?program=community-view\&env=online\&node=community-view03.idc\&soft=java
  curl  http://saltmaster:9191/salt/v1/addnodestate?program=community-view\&env=online\&node=community-view03.idc\&soft=logstash
  curl  http://saltmaster:9191/salt/v1/addnodestate?program=community-view\&env=online\&node=community-view03.idc\&soft=zabbix
  curl  http://saltmaster:9191/salt/v1/addnodestate?program=community-view\&env=online\&node=community-view03.idc\&soft=rundeck
```

######线上运行接口，部分关键数据已作调整，如需运行此脚本，请按需调整
