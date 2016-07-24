#!/usr/bin/env python
#coding=utf-8
#__author__  = louis,
# __date__   = 2016-05-05 10:20,
#  __email__ = yidongsky@gmail.com,
#   __name__ = table.py


from libs.datatables import DataTablesServer


# Indexed column (used for fast and accurate table cardinality)
_indexColumn = "userid"

#Tupple of database columns with their alias (for JOIN feature) which should be read and sent back to DataTables
columns = [("UserId","user.userid"),("Username","user.username"),("Nickname","user.nickname"),("Email","user.email"),("Status","user_stat.userstat"),("Role","role.name"),("Login","user.last_login")]

# DB table to use Or a join query if table is more than one.
joinOrtable = "user inner join role on (role.roleid=user.role_id) inner join user_stat on (user.is_active=user_stat.statid)"


#role
_roleColumn = "roleid"
roleColumns = [("UserId","role.roleid"),("Name","role.name")]
rolejoinOrtable = "role"


#permission
_permissColumn = "id"
permissColumns = [("UserId","user_permission.id"),("Name","user_permission.name"),("Url","user_permission.url")]
permissjoinOrtable = "user_permission"


class UserlistTable:

    dataTableData = None

    def __init__(self):
        self.dataTableData = DataTablesServer()
        self.dataTableData.setDatabaseInfo(joinOrtable,columns,_indexColumn)
        self.dataTableData.connect()

    def setDataTableOptions(self, echo, sortdirection, sortcolumn, displaystart="", search = "", sortingcolumns = 0, displaylength = -1):
        self.dataTableData.dataTablesOptions(echo, sortdirection, sortcolumn, displaystart, search, sortingcolumns, displaylength)

    def getDataTableData(self):
        if(self.dataTableData is not None):
            return self.dataTableData.getData()
        else:
            return None

class RolelistTable:

    dataTableData = None

    def __init__(self):
        self.dataTableData = DataTablesServer()
        self.dataTableData.setServerInfo(_databaseInfo['host'], _databaseInfo['db'], _databaseInfo['user'], _databaseInfo['passwd'])
        self.dataTableData.setDatabaseInfo(rolejoinOrtable,roleColumns,_roleColumn)
        self.dataTableData.connect()

    def setDataTableOptions(self, echo, sortdirection, sortcolumn, displaystart="", search = "", sortingcolumns = 0, displaylength = -1):
        self.dataTableData.dataTablesOptions(echo, sortdirection, sortcolumn, displaystart, search, sortingcolumns, displaylength)

    def getDataTableData(self):
        if(self.dataTableData is not None):
            return self.dataTableData.getData()
        else:
            return None

class PermisslistTable:

    dataTableData = None

    def __init__(self):
        self.dataTableData = DataTablesServer()
        self.dataTableData.setServerInfo(_databaseInfo['host'], _databaseInfo['db'], _databaseInfo['user'], _databaseInfo['passwd'])
        self.dataTableData.setDatabaseInfo(permissjoinOrtable,permissColumns,_permissColumn)
        self.dataTableData.connect()

    def setDataTableOptions(self, echo, sortdirection, sortcolumn, displaystart="", search = "", sortingcolumns = 0, displaylength = -1):
        self.dataTableData.dataTablesOptions(echo, sortdirection, sortcolumn, displaystart, search, sortingcolumns, displaylength)

    def getDataTableData(self):
        if(self.dataTableData is not None):
            return self.dataTableData.getData()
        else:
            return None



#Sample Code#
################################################################
#data = ServerProcessing()
#data.setDataTableOptions( 3,"asc","1",0,"",1,10) #echo sortdir sortcol displaystart search sortingcolumns displaylength
#print(data.getDataTableData())