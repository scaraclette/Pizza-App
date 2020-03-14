document.addEventListener('DOMContentLoaded', function() {
    // Limit the toppings on pizza menu
    limitTopping();
});

function limitTopping() {
    let toppingCheckbox = document.getElementsByTagName("input");
    let limit = 3;
    for (let i = 0; i < toppingCheckbox.length; i++) {
        toppingCheckbox[i].onclick = function() {
            let checkedcount = 0;
            for (let i = 0; i < toppingCheckbox.length; i++) {
                checkedcount += (toppingCheckbox[i].checked) ? 1 : 0;
            }
            if (checkedcount > limit) {
                console.log("here");
                alert("Choose a maximum of 3 toppings");
                this.checked = false;
            }
        }
    }
}