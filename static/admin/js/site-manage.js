$('#siteSetting').submit(function (event) {
    event.preventDefault();

    let formData = $(this).serialize();
    $.ajax({
        url: '/api/set-setting/', type: 'POST', data: formData,

        success: (result) => {
            let liveToast = new bootstrap.Toast(document.getElementById('liveToast'));
            liveToast.show();
        }, error: (error) => {
            console.err(error);
        }
    });
});

$('#slogan-manage').submit(function (event) {
    event.preventDefault();

    let formData = $(this).serialize();
    $.ajax({
        url: '/api/set-slogan/', type: 'POST', data: formData,

        success: (result) => {
            let liveToast = new bootstrap.Toast(document.getElementById('liveToast'));
            liveToast.show();
        }, error: (error) => {
            console.error(error);
        }
    });
});
