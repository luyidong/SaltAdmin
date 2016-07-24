#!/usr/bin/env python
#coding=utf-8
#__author__  = louis,
# __date__   = 2016-07-14 20:30,
#  __email__ = yidongsky@gmail.com,
#   __name__ = cmdb_table.py

from libs.datatables import DataTablesServer


# # Indexed column (used for fast and accurate table cardinality)
# _indexColumn = "userid"
# #Tupple of database columns with their alias (for JOIN feature) which should be read and sent back to DataTables
# columns = [("UserId","user.userid"),("Username","user.username"),("Nickname","user.nickname"),("Email","user.email"),("Status","user_stat.userstat"),("Role","role.name"),("Login","user.last_login")]
# # DB table to use Or a join query if table is more than one.
# joinOrtable = "user inner join role on (role.roleid=user.role_id) inner join user_stat on (user.is_active=user_stat.statid)"


#listCMDB
_listCmdbColumn = "Server_ip"
listCmdbColumns = [("Server_ip","server_list.server_ip"),("Server_name","server_list.server_name"),("Server_ip","server_list.server_ip"),("Prom","server_fun_categ.fun_categ_name"),("Env","server_env_categ.env_categ_name"),("Status","server_status_categ.server_status_name"),("Server_last_time","server_list.server_last_time")]
listCmdbJoinOrtable = "server_list inner join server_env_categ  on (server_list.server_env_id=server_env_categ.id ) inner join  server_fun_categ on (server_list.server_fun_id=server_fun_categ.id) inner join server_status_categ on (server_list.server_status_id = server_status_categ.id)"

class listCmdbTable:

    dataTableData = None

    def __init__(self):
        self.dataTableData = DataTablesServer()
        self.dataTableData.setDatabaseInfo(listCmdbJoinOrtable,listCmdbColumns ,_listCmdbColumn)
        self.dataTableData.connect()

    def setDataTableOptions(self, echo, sortdirection, sortcolumn, displaystart="", search = "", sortingcolumns = 0, displaylength = -1):
        self.dataTableData.dataTablesOptions(echo, sortdirection, sortcolumn, displaystart, search, sortingcolumns, displaylength)

    def getDataTableData(self):
        if(self.dataTableData is not None):
            return self.dataTableData.getData()
        else:
            return None

#listProm
_listPromColumn = "server_group_id"
listPromColumns = [("Pid","server_fun_categ.server_group_id"),("fun_categ_name","server_fun_categ.fun_categ_name"),("soft_group_name","server_group_categ.soft_group_name"),("group_mobile","server_group_categ.group_mobile")]
listPromJoinOrtable = "server_fun_categ inner join server_group_categ on (server_fun_categ.server_group_id = server_group_categ.id)"

class listPromTable:

    dataTableData = None

    def __init__(self):
        self.dataTableData = DataTablesServer()
        self.dataTableData.setDatabaseInfo(listPromJoinOrtable,listPromColumns,_listPromColumn)
        self.dataTableData.connect()

    def setDataTableOptions(self, echo, sortdirection, sortcolumn, displaystart="", search = "", sortingcolumns = 0, displaylength = -1):
        self.dataTableData.dataTablesOptions(echo, sortdirection, sortcolumn, displaystart, search, sortingcolumns, displaylength)

    def getDataTableData(self):
        if(self.dataTableData is not None):
            return self.dataTableData.getData()
        else:
            return None


#listEnv
_listEnvColumn = "id"
listEnvColumns = [("id","server_env_categ.id"),("env_categ_name","server_env_categ.env_categ_name")]
listEnvJoinOrtable = "server_env_categ"

class listEnvTable:

    dataTableData = None

    def __init__(self):
        self.dataTableData = DataTablesServer()
        self.dataTableData.setDatabaseInfo(listEnvJoinOrtable,listEnvColumns,_listEnvColumn)
        self.dataTableData.connect()

    def setDataTableOptions(self, echo, sortdirection, sortcolumn, displaystart="", search = "", sortingcolumns = 0, displaylength = -1):
        self.dataTableData.dataTablesOptions(echo, sortdirection, sortcolumn, displaystart, search, sortingcolumns, displaylength)

    def getDataTableData(self):
        if(self.dataTableData is not None):
            return self.dataTableData.getData()
        else:
            return None