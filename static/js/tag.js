
$(function () {
    // let s = [];
    let s = "";  // 设置选择分类标签数据

    let $tag= $(".tag-widget .tagcloud a");  // 获取分类选择按钮

    let $tag_look = $(".comment-form-wrap .form-group .tag_look");
    // 标签解决方案
    $tag.click(function () {
        let tag_id = $(this).prop("id");
        let tag_name = $(this).html();


        // 查看是否选择了标签
        if (s){
            alert("标签已选择, 不能多选");
            return false;
        }
        s = tag_id;
        // 添加选者标签展示
        $tag_look.prepend(`<a href="#" class="tag-cloud-link" id="${tag_id}">${tag_name} </a>`)
    });

    // 图片上传解决方案
    let $img = $(".comment-form-wrap .form-group #image_file");  //获取图片元素
    let $title= $(".comment-form-wrap .form-group #title");  //获取图片元素
    let $content = $(".comment-form-wrap .form-group #content"); // 获取内容元素
    let $submit = $(".comment-form-wrap .form-group #submit"); // 获取提交按钮
    $submit.click(function () {
        // 获取图片文件
        let file = $img[0].files[0];
        if (!file){
            alter("请上传图片");
            return false
        }
        // 创建文件包
        let oFormData = new FormData();

        // 图片
        oFormData.append('image_file', file);

        // 添加令牌
        oFormData.append("_xsrf",getCookie("_xsrf"));

        // 获取标题
        let title = $title.val();
        if (!title){
            alter("标题未输入");
            return false
        }
        oFormData.append("title",title);

        // 获取内容
        let content = $content.val();
        if (!title){
            alter("内容介绍未输入");
            return false
        }
        oFormData.append("content",content);

        // 添加分类标签
        oFormData.append("tag",s);

        // let data = {
        //     "_xsrf": getCookie("_xsrf"),
        //     "image":file,
        // };
        
        // 发送请求
        $.ajax(url="/update",{
            method:'POST',
            data:oFormData,
            processData:false,
            contentType:false,  
        })
            .done(function (res) {
                alert(res.code)
            })
            .fail(function () {
                alert("服务器超时！")
            })

    });
         

function getCookie(name){
        var x = document.cookie.match("\\b" + name + "=([^;]*)\\b");
        return x ? x[1]:undefined;
}
    
});
