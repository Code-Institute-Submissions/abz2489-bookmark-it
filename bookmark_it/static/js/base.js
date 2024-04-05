const tooltipTriggerList = document.querySelectorAll('[data-bs-toggle="tooltip"]')
const tooltipList = [...tooltipTriggerList].map(tooltipTriggerEl => new bootstrap.Tooltip(tooltipTriggerEl))


document.addEventListener('DOMContentLoaded', function () {
    const getToast = document.getElementById('toast');
    let toast = new bootstrap.Toast(getToast);
    toast.show();

    const closeToast = document.getElementById('toast-close');
    closeToast.addEventListener('click', () => {
    toast.hide();
})
});
    