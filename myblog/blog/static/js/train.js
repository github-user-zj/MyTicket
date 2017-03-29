/**
 * Created by Administrator on 2017/3/27.
 */
//日历
$(document).ready(function () {

    $('.form_date').datetimepicker({
        language: 'zh-CN',
        weekStart: 1,
        todayBtn: 1,
        autoclose: 1,
        todayHighlight: 1,
        startView: 2,
        minView: 2,
        forceParse: 0,
    });
    // 清空 输入框提示信息
    $('.form-control').click(function () {
        var inputdata = $(this).val()
        if (inputdata.indexOf("请") != -1) {
            $(this).val("")
        }
    });
    // 检查车站名称是否正确
    function cheakname(station_name){
        var from_station = $(station_name).val();
        if (from_station == "") {
            $(station_name).val("请填写地址");
            return false
        }else {
            //    检查车站名称
            $.ajax({
                type: "GET",
                url: "/blog/station/action" ,
                data: {station_name: $(station_name).val()},
                dataType: "text",
                success:function(data) {
                    if(data=="0"){
                        $(station_name).val("输入车站名错误，请重新输入！")
                    }
                },
                error:function(xhr) {
                    $(station_name).val("ajax 出错！！")
                }
            });
        }
    }

    $('#from_station').blur(function () {
            cheakname("#from_station");
        }
    );
    $('#to_station').blur(function () {
            cheakname("#to_station");
        }
    );

    // 提交前验证
    $('#submitbut').bind("click",function () {
        var from_station = $("#from_station").val();
        if (from_station == "") {
            $("#from_station").val("请填写出发地");
            return false
        }

        var to_station = $("#to_station").val();
        if (to_station == "") {
            $("#to_station").val("请填写目的地");
            return false
        }

        var train_date = $("#train_date").val();
        if (train_date == "") {
            // alert(train_date)
            $("#train_date02").val("请选择日期");
            return false
        }

         $.ajax({
                type: "GET",
                url: "/blog/query/action" ,
                data: {from_station: $("#from_station").val(),to_station:$("#to_station").val(),train_date:$("#train_date").val()},
                dataType: "text",
                success:function(data) {

                    var html= ''
                    html += '<thead><th>车次</th><th>商务座</th><th>一等座</th><th>二等座</th><th>软卧</th><th>硬卧</th>' +
                            '<th>软座</th><th>硬座</th><th>无座</th></thead>';
                    if (data != "[]") {
                        var obj = jQuery.parseJSON(data);
                        $.each(obj, function (i, item) {
                            // alert(item.station_train_code)
                            html += '<tr>';
                            html += '<td>' + item.station_train_code + '</td>';
                            html += '<td>' + item.swz_num + '</td>';
                            html += '<td>' + item.zy_num + '</td>';
                            html += '<td>' + item.ze_num + '</td>';
                            html += '<td>' + item.rw_num + '</td>';
                            html += '<td>' + item.yw_num + '</td>';
                            html += '<td>' + item.rz_num + '</td>';
                            html += '<td>' + item.yz_num + '</td>';
                            html += '<td>' + item.wz_num + '</td>';
                            html += "</tr>";
                        });
                    }else{
                        html += '<tr>';
                        html += '<td colspan="9" >未查到车票信息</td>';
                        html += '</tr>';
                    }
                    $("#float").html(html);
                    // alert(obj[0].station_train_code)
                },
                error:function(xhr) {
                    $("#from_station").val("ajax 出错！！")
                }
            });
        return false;
    });
    /* 日历的日期 */
    $("#train_date").val(getDate(1))
    function getDate(AddDayCount) {
        //获取当前日期
        var date_time = new Date();
        date_time.setDate(date_time.getDate() + AddDayCount);
        //年
        var year = date_time.getFullYear();
        //判断小于10，前面补0
        if (year < 10) {
            year = "0" + year;
        }

        //月
        var month = date_time.getMonth() + 1;
        //判断小于10，前面补0
        if (month < 10) {
            month = "0" + month;
        }

        //日
        var day = date_time.getDate();
        //判断小于10，前面补0
        if (day < 10) {
            day = "0" + day;
        }
        return year + "-" + month + "-" + day;
    }

})
