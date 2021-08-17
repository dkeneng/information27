function getCookie(name) {
    var r = document.cookie.match("\\b" + name + "=([^;]*)\\b");
    return r ? r[1] : undefined;
}


$(function () {
    $(".pic_info").submit(function (e) {
        e.preventDefault()

        //上传头像
        // ajaxSubmit 代表使用 ajax 的方式去模拟点击提交按钮的操作

        //ajaxSubmit：利用ajax方式，对表单进行提交

        //ajaxSubmit :利用ajax方式， 再自动收集 带name的input标签 ， 将name:value 拼接之后作为ajax提交的数据提交到后台
        $(this).ajaxSubmit({
            url: "/user/pic_info",
            type: "POST",
            headers: {
                "X-CSRFToken": getCookie('csrf_token')
            },
            success: function (resp) {
                if (resp.errno == "0") {
                    $(".now_user_pic").attr("src", resp.data.avatar_url)
                    $(".user_center_pic>img", parent.document).attr("src", resp.data.avatar_url)
                    $(".user_login>img", parent.document).attr("src", resp.data.avatar_url)
                }else {
                    alert(resp.errmsg)
                }
            }
        })
    })
})