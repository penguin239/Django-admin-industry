let wrapper = $('.wrapper');
let nav_link = $('.wrapper .nav-link')

let scrollFunc = function (e) {
    let scrollTop = document.body.scrollTop || document.documentElement.scrollTop;
    if (scrollTop === 0) {
        wrapper[0].style.backgroundColor = 'transparent';
        wrapper[0].style.boxShadow = '';
        for (let i = 0; i < nav_link.length; i++) {
            nav_link[i].style.color = '#fff';
        }
        $('.contact-us')[0].style.color = '#fff';
        $('.phone-num')[0].style.color = '#fff';
        $('._phone-icon')[0].style.fill = '#fff';
        $('#logo-view').attr('src', '/static/front/imgs/logo-light.png');
    } else {
        wrapper[0].style.backgroundColor = 'rgb(255, 255, 255)';
        wrapper[0].style.boxShadow = '0 0 15px rgb(0 0 0 / 20%)';
        for (let i = 0; i < nav_link.length; i++) {
            nav_link[i].style.color = '#000';
        }
        $('.contact-us')[0].style.color = '#000';
        $('.phone-num')[0].style.color = '#005BAC';
        $('._phone-icon')[0].style.fill = '#444';
        $('#logo-view').attr('src', '/static/front/imgs/logo-dark.png');
    }
}
window.addEventListener('scroll', scrollFunc);