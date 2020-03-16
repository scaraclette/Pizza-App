document.addEventListener('DOMContentLoaded', function() {
    pageOthers();
    console.log('test');
});

function pageOthers() {
    // Disable checkbox by default
    disableSteakTopping(true);

    document.querySelector('#subName').onchange = function() {
        let currentSub = document.getElementById('subName').value;
        console.log(currentSub)
        if (currentSub == 'Steak + Cheese') {
            console.log('yest')
            disableSteakTopping(false);
        } else {
            disableSteakTopping(true);
        }
    }
}

function disableSteakTopping(bool) {
    let steakToppings = document.getElementsByName('steakTopping');
    for (let i = 0; i < steakToppings.length; i++) {
        steakToppings[i].disabled = bool;
    }
}