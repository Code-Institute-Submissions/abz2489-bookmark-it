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
            console.log(url)
        }
        return false;
    }

    function fillSquare(icon) {
        let arrowUp = document.getElementById("arrow-up");
        arrowUp.classList.remove("bi-arrow-up-square");
        arrowUp.classList.add("bi-arrow-up-square-fill");
    }

    function emptySquare(icon) {
        let arrowUp = document.getElementById("arrow-up");
        arrowUp.classList.remove("bi-arrow-up-square-fill");
        arrowUp.classList.add("bi-arrow-up-square");
    }

    function scrollToTop() {
        window.scrollTo(0,0);
    }