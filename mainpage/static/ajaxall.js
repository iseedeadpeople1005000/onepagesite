 $(function() {
    $('.create_post').on('submit', function(event){
        event.preventDefault();
        console.log("form submited!")
        create_post();
    });
    function create_post() {
        console.log("create post is working!")
        var Comment_Author = $('#Comment_Author').val()
        var Comment_Text = $('#Comment_Text').val()
        $.ajax({
            url: '/create_post/',
            type: "POST",
            data: { 'Comment_Text': Comment_Text, 'Comment_Author': Comment_Author },
            success: function(json) {
                $('#Comment_Author').val('')
                $('#Comment_Text').val('')
                $('#results').html("<b>"+json.result+"</b>");
                console.log("success");
            },
            error: function(xhr,errmsg,err) {
                $('#results').html("<div>oops! error: "+errmsg+"</div>");
                console.log(xhr.status + ": " +xhr.responseText);
            }
        });
    };
});
jQuery("document").ready(function(){
    jQuery(".addcomm").on('click', function(){
        console.log("gogogo");
            var Comment_Author = $('input[name=Comment_Author]');
            var Comment_Text = $('input[name=Comment_Text]');
            jQuery.ajax({
                type: "POST",

                url: "/addcomm/ajax/",

                data:{'Comment_Author': Comment_Author.val(), 'Comment_Text': Comment_Text.val(),},

                catch: false,

                success: function(data){
                    console.log(data)
                    jQuery .html(data);
                }
            });
    });
});