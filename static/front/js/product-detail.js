$('#paramImg').click(function () {
    if ($(this).attr('id') === 'paramImg') {
        $(this).attr('id', 'paramImg-large');
        return;
    }
    $(this).attr('id', 'paramImg');
});

$('#leaveMessage').submit(function (event) {
    // 避免form提交后页面跳转
    event.preventDefault();

    const formData = $(this).serialize();

    $.ajax({
        url: '/leave-message/',
        type: 'POST',
        data: formData,

        success: (result) => {
            if (result.status_code === 200) {
                let liveToast = new bootstrap.Toast(document.getElementById('liveToast'));

                liveToast.show();
                document.getElementById('leaveMessage').reset();
            }
        },
        error: (error) => {
            console.log(error);
        }
    });
});
