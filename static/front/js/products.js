$('.load-commodity').click(function () {
    let category = $(this).attr('value');
    let base64Text = btoa(encodeURIComponent(category));

    location.href = '?category=' + base64Text;
})