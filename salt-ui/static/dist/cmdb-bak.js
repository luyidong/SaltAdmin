$(document).ready( function () {
    var table = $('#datatables').DataTable({
                    "dom": '<"top"f >rt<"bottom"ilp><"clear">',//dom定位
                    "bServerSide": true,
                    "bJQueryUI": false,
                    "bLengthChange": true,
                    'iDisplayLength': 8,
                    "bFilter": true,
                    "bInfo": true,
                    "sAjaxSource": '/cmdb/listTable',
                    "bProcessing": false,
                    "bPaginate": true,
                    "bSort": true,
                    "bAutoWidth": false,
                    "asStripClasses": false,
                    "oLanguage": {
                    "oAria": {
                        "sSortAscending": ": 升序排列",
                        "sSortDescending": ": 降序排列"
                    },
                    "oPaginate": {
                        "sFirst": "首页",
                        "sLast": "末页",
                        "sNext": "下页",
                        "sPrevious": "上页"
                    },
                    "sEmptyTable": "没有相关记录",
                    "sInfo": "第 _START_ 到 _END_ 条记录，共 _TOTAL_ 条",
                    "sInfoEmpty": "第 0 到 0 条记录，共 0 条",
                    "sInfoFiltered": "(从 _MAX_ 条记录中检索)",
                    "sInfoPostFix": "",
                    "sDecimal": "",
                    "sThousands": ",",
                    "sLengthMenu": "每页显示: _MENU_",
                    "sLoadingRecords": "正在载入...",
                    "sProcessing": "正在载入...",
                    "sSearch": "搜索:",
                    "sSearchPlaceholder": "",
                    "sUrl": "",
                    "sZeroRecords": "没有相关记录",
                    "searching":false,
                    },
                "destory": true, //允许重新实例化Datatables
                "retrieve": true, //检索一个已存在的Datatables实例
                    "columns": [
                        {"mdata": "Server_name"}, 
                        {"mdata": "Server_ip"},
                        {"mdata": "Prom"},  
                        {"mdata": "Env"},  
                        {"mdata": "Status"},  
                        {"mdata": "Update"},  
                        {"mdata": "Modify"},  
                    ], 
                     "columnDefs":[ 
                          { 
                            "targets": [0], 
                            orderable:false,//禁用排序
                            //  "orderable": false,//关闭id的排序
                            //  "ordering":false,
                            //"mdata":"Server_ip", 
                            "render":function(data,type){ 
                                return "<input type='checkbox' name='checkList' class='deleteRow' value='"+data+"' />"; 
                            } 
                        },
                         { 
                            "targets": [7], 
                            //"orderData":[1,2], 
                            //"mdata":"UserId",  
                            "render":function(data,type,row){ 
                                return "<button data-names='"+row[0]+"' id='del-btn' type='button' class='btn btn-danger btn-sm'>删除</button>&nbsp;" +
                                        "<button data-serverip='"+row[0]+"' data-sname='"+row[1]+"' data-prom='"+row[3]+"' data-env='"+row[4]+"' data-status='"+row[5]+"' id='edit-btn' type='button' class='btn btn-success btn-sm'>编辑</button>&nbsp;" +
                                "<button id='info-btn' type='button' class='btn btn-info btn-sm'>详细</button>";
                            } 
                        } 

                    ] 

                });

            // DataTables 1.10.7   custom search
            $('#datatables_filters').on('keyup change', function(){
                    table.search($(this).val()).draw();
            });


            //submit update
            $("#submit-update-btn").on('click', function (data) { 
                var serverip = $("#front-data-serverip").val()
                var servername = $("#front-data-server-name").val()
                var prom = $("#front-data-prom").val()
                var env = $("#front-data-env").val()
                var status = $("#front-data-status").val()
                $.ajax({
                    type: "post",
                    url: "/cmdb/submit?action_type=server_list",
                    data: {"serverip":serverip,"servername":servername,"prom":prom,"env":env,"status":status},
                    success: function(result) {
                            $('#update-modal').modal('hide')
                            table.draw(false); // redrawing datatable
                    },
                    async:false
                });
            });


            ////addlist
            //
            //$("#addnodes").on('click', function (data) { 
            //    var serverip = ($("#edit-btn").attr("data-serverip"))
            //    var serverName = ($("#edit-btn").attr("data-sname"))
            //    var prom = ($("#edit-btn").attr("data-prom"))
            //    var env = ($("#edit-btn").attr("data-env"))
            //    var status = ($("#edit-btn").attr("data-status"))
            //
            //    //alert(status)
            //    //alert( data[1] +"'s salary is: "+ data[ 2 ] );
            //    $("#front-data-serverips").val(serverip)
            //    $("#front-data-server-names").val(serverName)
            //    $("#front-data-proms").val(prom)
            //    $("#front-data-envs").val(env)
            //    $("#front-data-statusss").val(status)
            //    //$("#user-role").val(selects)
            //    //$('#info').html(str)
            //    $.ajax({
            //        type: 'get',
            //        url: "/cmdb/addlist",
            //        //data: {"serverip":serverip},
            //        success: function(data) {
            //            eval("var data="+data)
            //            //alert(data['server_attr']['server_env_id'])
            //            //alert(data['server_attr']['server_fun_id'])
            //            var strs=''
            //            strs += '<label class="col-sm-2 control-label"  for="front-data-prom">应用名称：</label>'
            //            strs += '<div class="col-sm-4">'
            //            strs += '<input class="form-control" type="hidden" value=" '+data['server_attr']['server_fun_id']+' " />'
            //            strs += '<select class="form-control" name="front-data-prom" id="front-data-prom">'
            //
            //                $.each(data.server_fun, function (i, contents) {
            //                    if (data['server_attr']['server_fun_id'] == contents.id) {
            //                        strs += '<option selected="selected" value="' + contents.id + '">' + contents.fun_categ_name + '</option>'
            //                    } else {
            //                        strs += '<option value="' + contents.id + '">' + contents.fun_categ_name + '</option>'
            //                    }
            //                })
            //            strs += ' </select>'
            //            strs += '</div>'
            //            strs += '<div class="col-sm-6"></div>'
            //            $('#select-proms').html(strs)
            //
            //            var str=''
            //            str += '<label class="col-sm-2 control-label"  for="front-data-env">运行环境：</label>'
            //            str += '<div class="col-sm-4">'
            //            str += '<input class="form-control" type="hidden" value=" '+data['server_attr']['server_env_id']+' " />'
            //            str += '<select class="form-control" name="front-data-env" id="front-data-env" >'
            //
            //                $.each(data.server_env, function (i, content) {
            //                    if (data['server_attr']['server_env_id'] == content.id) {
            //                        str += '<option selected="selected" value="' + content.id + '">' + content.env_categ_name + '</option>'
            //                    } else {
            //                        str += '<option value="' + content.id + '">' + content.env_categ_name + '</option>'
            //                    }
            //                })
            //            str += ' </select>'
            //            str += '</div>'
            //            str += '<div class="col-sm-6"></div>'
            //            $('#select-envs').html(str)
            //
            //
            //            var str=''
            //            str += '<label class="col-sm-2 control-label"  for="front-data-status">服务状态：</label>'
            //            str += '<div class="col-sm-4">'
            //            str += '<input class="form-control" type="hidden" value=" '+data['server_attr']['server_status_id']+' " />'
            //            str += '<select class="form-control" name="front-data-status" id="front-data-status" >'
            //
            //                $.each(data.server_stat, function (i, content) {
            //                    if (data['server_attr']['server_status_id'] == content.ID) {
            //                        str += '<option selected="selected" value="' + content.ID + '">' + content.server_status_name + '</option>'
            //                    } else {
            //                        str += '<option value="' + content.ID + '">' + content.server_status_name + '</option>'
            //                    }
            //                })
            //            str += ' </select>'
            //            str += '</div>'
            //            str += '<div class="col-sm-6"></div>'
            //            $('#select-statuss').html(str)
            //
            //
            //
            //               //$("#update-modal").modal("show");//弹出框show
            //
            //        },
            //        async:false
            //    });
            //
            //});



            ////update
            $("#datatables tbody").on('click','button#edit-btn', function (data) { 
                var serverip = ($("#edit-btn").attr("data-serverip"))
                var serverName = ($("#edit-btn").attr("data-sname"))
                var prom = ($("#edit-btn").attr("data-prom"))
                var env = ($("#edit-btn").attr("data-env"))
                var status = ($("#edit-btn").attr("data-status"))

                //alert(status)
                //alert( data[1] +"'s salary is: "+ data[ 2 ] );
                $("#front-data-serverip").val(serverip)
                $("#front-data-server-name").val(serverName)
                $("#front-data-prom").val(prom)
                $("#front-data-env").val(env)
                $("#front-data-status").val(status)
                //$("#user-role").val(selects)
                //$('#info').html(str)
                $.ajax({
                    type: 'get',
                    url: "/cmdb/update",
                    data: {"serverip":serverip},
                    success: function(data) {
                        eval("var data="+data)
                        //alert(data['server_attr']['server_env_id'])
                        //alert(data['server_attr']['server_fun_id'])

                        var str=''
                        str += '<label class="col-sm-3 control-label"  for="front-data-status">服务状态：</label>'
                        str += '<div class="col-sm-6">'
                        str += '<input class="form-control" type="hidden" value=" '+data['server_attr']['server_status_id']+' " />'
                        str += '<select class="form-control" name="front-data-status" id="front-data-status" >'

                            $.each(data.server_stat, function (i, content) {
                                if (data['server_attr']['server_status_id'] == content.ID) {
                                    str += '<option selected="selected" value="' + content.ID + '">' + content.server_status_name + '</option>'
                                } else {
                                    str += '<option value="' + content.ID + '">' + content.server_status_name + '</option>'
                                }
                            })
                        str += ' </select>'
                        str += '</div>'
                        str += '<div class="col-sm-3"></div>'
                        $('#select-status').html(str)



                        var str=''
                        str += '<label class="col-sm-3 control-label"  for="front-data-env">运行环境：</label>'
                        str += '<div class="col-sm-6">'
                        str += '<input class="form-control" type="hidden" value=" '+data['server_attr']['server_env_id']+' " />'
                        str += '<select class="form-control" name="front-data-env" id="front-data-env" >'

                            $.each(data.server_env, function (i, content) {
                                if (data['server_attr']['server_env_id'] == content.id) {
                                    str += '<option selected="selected" value="' + content.id + '">' + content.env_categ_name + '</option>'
                                } else {
                                    str += '<option value="' + content.id + '">' + content.env_categ_name + '</option>'
                                }
                            })
                        str += ' </select>'
                        str += '</div>'
                        str += '<div class="col-sm-3"></div>'
                        $('#select-env').html(str)

                        var strs=''
                        strs += '<label class="col-sm-3 control-label"  for="front-data-prom">应用名称：</label>'
                        strs += '<div class="col-sm-6">'
                        strs += '<input class="form-control" type="hidden" value=" '+data['server_attr']['server_fun_id']+' " />'
                        strs += '<select class="form-control" name="front-data-prom" id="front-data-prom">'

                            $.each(data.server_fun, function (i, contents) {
                                if (data['server_attr']['server_fun_id'] == contents.id) {
                                    strs += '<option selected="selected" value="' + contents.id + '">' + contents.fun_categ_name + '</option>'
                                } else {
                                    strs += '<option value="' + contents.id + '">' + contents.fun_categ_name + '</option>'
                                }
                            })
                        strs += ' </select>'
                        strs += '</div>'
                        strs += '<div class="col-sm-3"></div>'
                        $('#select-prom').html(strs)


                           $("#update-modal").modal("show");//弹出框show

                    },
                    async:false
                });

            });
            //
            ////info
            //$("#datatables tbody").on('click','#info-btn', function () { 
            //    //http://datatables.club/example/ajax/null_data_source.html
            //    var data = table.row( $(this).parents('tr') ).data();
            //    //alert( data[1] +"'s salary is: "+ data[ 2 ] );
            //    var str = ''
            //    str += '<tr>'
            //    str += '<th>节点名称</th>'
            //    str += '<td>' + data[1] + '</td>'
            //    str += '</tr>'
            //    str += '<tr>'
            //    str += '<th>节点地址</th>'
            //    str += '<td>' + data[2] + '</td>'
            //    str += '</tr>'
            //    str += '<tr>'
            //    str += '<th>应用名称</th>'
            //    str += '<td>' + data[3] + '</td>'
            //    str += '</tr>'
            //    str += '<tr>'
            //    str += '<th>运行环境</th>'
            //    str += '<td>' + data[4] + '</td>'
            //    str += '</tr>'
            //    str += '<tr>'
            //    str += '<th>服务状态</th>'
            //    str += '<td>' + data[5] + '</td>'
            //    str += '</tr>'
            //    str += '<tr>'
            //    str += '<th>更新时间</th>'
            //    str += '<td>' + data[6] + '</td>'
            //    str += '</tr>'
            //    $('#info').html(str)
            //    $("#info-modal").modal("show");//弹出框show
            //});



            //delete
            $("#datatables tbody").on('click','#del-btn', function (data) { 
                var serverIP=$(this).attr('data-names')

                swal({   title: "请确认",
                    text: "删除后，将无法恢复!",
                    type: "warning",
                    showCancelButton: true,
                    confirmButtonColor: "#DD6B55",
                    confirmButtonText: "确认, 删除!",
                    closeOnConfirm: false },
                    function() {
                        $.ajax({
                            type: 'get',
                            url: "/cmdb/delTable",
                            data: {"server_ip": serverIP},
                            success: function (data) {
                                if (data == '0') {
                                    table.draw(false); // redrawing datatable 
                                    //alert("ok");
                                    swal("删除!", "文件已被删除.", "success");
                                }
                            },
                            async: false
                        });
                    });

            });

            //checkbox全选
            $("#bulkDelete").on('click',function() { // bulk checked
                var status = this.checked;
                $(".deleteRow").each( function() {
                    $(this).prop("checked",status);
                });
            });
                //delete checkall
            $('#deleteTriger').on("click", function(event){ // triggering delete one by one
                    if( $('.deleteRow:checked').length > 0 ){  // at-least one checkbox checked
                        var ids = [];
                        $('.deleteRow').each(function(){
                            if($(this).is(':checked')) {
                                ids.push($(this).val());
                            }
                        });
                        var ids_string = ids.toString();  // array to string conversion

                        swal({   title: "请确认",
                        text: "删除后，将无法恢复!",
                        type: "warning",
                        showCancelButton: true,
                        confirmButtonColor: "#DD6B55",
                        confirmButtonText: "确认, 删除!",
                        closeOnConfirm: false },
                        function() {
                            $.ajax({
                                type: "post",
                                url: "/cmdb/delTable",
                                data: {"server_ip": ids_string},
                                success: function (result) {
                                    table.draw(false); // redrawing datatable
                                    swal("删除!", "文件已被删除.", "success");
                                },
                                async: false
                            });
                        });
                    }

            });

} );
