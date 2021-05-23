document.addEventListener("DOMContentLoaded", function () {
    let detail_group = document.querySelectorAll('button');
    for (let i = 0; i < detail_group.length; i++) {
        let detail = detail_group[i];
        if (detail) {
            detail.addEventListener('click', function (e) {
                let detail_block = e.target.nextElementSibling
                detail_block.style.display = 'block';
                detail_block.innerHTML = 'some text';
                console.log(e)
            });
        }
    }
});
let detail_load = function () {
    console.log('click')
};

function get_detail() {
    $.ajax(
        {
            type: "GET",
            url: "/detail",
            data: {
                page: 'page_num',
            },

            success: function (data) {
                $("#div_sort").replaceWith(data);
            }
        })
};