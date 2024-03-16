let load_commodity = $('.load-commodity');


load_commodity.click(function () {
    let category = $(this).attr('value');
    let base64Text = btoa(encodeURIComponent(category));

    location.href = '/products/?category=' + base64Text;
})

let label_high_light = $('.product-list').attr('data-high-light');

for (let i = 0; i < load_commodity.length; i++) {
    if (load_commodity[i].innerText === label_high_light) {
        load_commodity[i].classList.add('hover');
        break;
    }
}
