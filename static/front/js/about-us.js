$('#paramImg').click(function () {
    if ($(this).attr('id') === 'paramImg') {
        $(this).attr('id', 'paramImg-large');
        return;
    }
    $(this).attr('id', 'paramImg');
});