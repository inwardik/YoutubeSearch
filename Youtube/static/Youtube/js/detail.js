document.addEventListener("DOMContentLoaded", function () {
    let detail_group = document.querySelectorAll('button');
    for (let i = 0; i < detail_group.length; i++) {
        let detail = detail_group[i];
        if (detail) {
            detail.addEventListener('click', function (e) {
                let detail_block = e.target.nextElementSibling;
                let videoId = e.target.previousElementSibling.innerText;
                if (detail_block.style.display === 'block') {
                    detail_block.style.display = 'none';
                } else detail_block.style.display = 'block';
                detail_block.innerHTML = "Loading...";
                get_detail2(detail_block, videoId)
            });
        }
    }
});
let detail_load = function () {
    console.log('click')
};

function get_detail2(detail_block, videoId) {
    let request = new XMLHttpRequest();
    let url_addr = '/Youtube/detail?q=' + videoId.toString();
    console.log(url_addr);
    request.open('GET', url_addr, true);

    request.onload = function () {
        if (this.status >= 200 && this.status < 400) {
            console.log('success')
            let resp = this.response;
            jresp = JSON.parse(resp)
            console.log(jresp);
            detail_block.innerHTML = "👍 " + jresp.likeCount + "\t   👎 " + jresp.dislikeCount +
                "\t   👀 " + jresp.viewCount + "\t   🦜 " + jresp.commentCount;
        } else {
            // We reached our target server, but it returned an error
            console.log("We reached our target server, but it returned an error")
        }
    };
    request.onerror = function () {
        // There was a connection error of some sort
        console.log("There was a connection error of some sort")
    };
    request.send();
}