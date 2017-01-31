
var $chatsock = null;
var $username = null;

var $receiverdata = {};
var $senderdata = {}

$(document).ready(function() {

    $('#message').val("");
    $user_id = parseInt($("#user_id").val());
    $username = $("#username").val();

    $senderdata = {
            id:$user_id,
            username: $username,
        }

    connectChatServer();

    $("#message").keyup(function(e) {
        var code = e.which;
        if (code == 13) e.preventDefault();
        if (code == 13) {
            var message = {
                receiver: $("#message").attr("receiver"),
                message: $('#message').val(),
            }
            if (message.message === "") {
                return false;
            }
            $chatsock.send(JSON.stringify(message));
            $("#message").val('').focus();
            html = ' <div class="media">\
                        <div class="media-body">\
                          <h4 class="media-heading">Me</h4>\
                          <p class="message">' + message.message + '</p>\
                        </div>\
                      </div>';
            $(".chat-data").append(html);
            $(".chat-data").animate({
                scrollTop: 99999999
            }, 'fast');
        }
    });


    $(".user-list").click(function(){
        $(".chat-data").html("");
        var user_id = $(this).attr("data-pk");
        $("#message").attr("receiver", user_id);
        $(".user-list").removeClass("chat-active");
        $(this).removeClass("message-blink");
        $(this).addClass("chat-active");
        $receiverdata = {
            id:user_id,
            username: $(this).attr("username"),
        }
        getChatData(user_id);
    });

});

var connectChatServer = function() {
    $chatsock = new ReconnectingWebSocket('ws://' + window.location.host + "/ws/chat/" + $username + "/");

    $chatsock.onmessage = function(message) {

        var message_data = JSON.parse(message.data);
        console.log(message_data);
        if($(".users-div .chat-active").length){
            if(parseInt($(".users-div .chat-active").attr("data-pk"))==message_data.sender.id){
                printMessages(message_data);
            }else{
                $(".user-"+message_data.sender.id).addClass("message-blink");
            }
        }else{
            $(".user-"+message_data.sender.id).addClass("message-blink");
        }
        
    };

    $chatsock.onopen = function() {
        console.log("Connected to chat socket");
    }
}

var getChatData = function(user_id){
    $.get("/api/chat/get-messages/?receiver="+user_id,{},function(data,status){
        $.each(data, function(indexs, message) {
            printMessages(message);
        });
        
    });
}

var printMessages = function(data){
    user = null;
    if ($user_id == data.sender) {
        name = "Me";
        user = $senderdata;
    }else{
        user = $receiverdata;
        name = user.username;
    }
    html = ' <div class="media">\
                <div class="media-body">\
                  <h4 class="media-heading">' + name + '</h4>\
                  <p class="message">' + data.message + '</p>\
                </div>\
              </div>';
    $(".chat-data").append(html);
    $(".chat-data").animate({
                scrollTop: 99999999
            }, 'fast');
}


