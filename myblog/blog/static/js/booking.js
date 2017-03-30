/**
 * Created by Administrator on 2017/3/29.
 */
//车票预订 js 代码

$(document).on('click',".yunding_class",function(){
   // alert($(this).val())


});
// 邮箱验证
$(document).ready(function () {

    function CheckMail(email) {
        var myreg = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
        if (!myreg.test(email)) {
            // myreg.focus();
            $("#tishi").val('请输入有效的E_mail！');
            return false;
        }else{
            $("#tishi").val("邮箱输入正确！");
        }
    };
    $("#email").blur(function () {
        var email = $("#email").val();
        //对电子邮件的验证
        CheckMail(email);
    });
    $("#savaemail").click(function () {

        var email = $("#email").val();
        if(email==""){
            $("#tishi").val("请输入邮箱！");
            return false;
        }
        CheckMail(email);
        $("#tishi").val("邮箱保存成功！");
    });

});


