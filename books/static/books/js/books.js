function optionUrl(option) {
    /** 
     * SORT - function to retrieve the URL from a selected option and redirect to the url
     * URL is stored from selected option
     * extracted URL is used to redirect the user to the selected option URL
     */
        let selectedOption = option.options[option.selectedIndex];
        let url = selectedOption.dataset.url;
        if (url) {
            window.location.href = url;
        }
        return false;
}

/*Functions to switch the bootstrap arrow icon depending on hover state*/
function fillSquare() {
    let arrowUp = document.getElementById("arrow-up");
    arrowUp.classList.remove("bi-arrow-up-square");
    arrowUp.classList.add("bi-arrow-up-square-fill");
}

    function emptySquare() {
    let arrowUp = document.getElementById("arrow-up");
    arrowUp.classList.remove("bi-arrow-up-square-fill");
    arrowUp.classList.add("bi-arrow-up-square");
}

/*Click event that takes the user back to the top of the page*/
function scrollToTop() {
    window.scrollTo(0,0);
}

/*Media query match event to determine mobile style of back to top button*/
function mobileFill(mQuery) {
    let arrowUp = document.getElementById("arrow-up");
    if (mQuery.matches) {
        arrowUp.classList.remove("bi-arrow-up-square");
        arrowUp.classList.add("bi-arrow-up-square-fill");
    } else {
        arrowUp.classList.remove("bi-arrow-up-square-fill");
        arrowUp.classList.add("bi-arrow-up-square");
    }
}

let mQuery = window.matchMedia("(max-width: 767px)");

mobileFill(mQuery);

mQuery.onchange = function() {
    mobileFill(mQuery);
};