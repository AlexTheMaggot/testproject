// Плавное отображение контента
$(window).on('load', function() {
    setTimeout(function() {
        $('.content').removeClass('invisible')
    }, 500)
})