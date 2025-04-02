

function hotelCost() {
    let nights;
    while (isNaN(nights) || nights <= 0) {
        nights = prompt("How many nights would you like to stay at the hotel?");
    }
    return nights * 140;
}

function planeRideCost() {
    let destination;
    while (!destination || !isNaN(destination)) {
        destination = prompt("Where would you like to go? (London, Paris, or other)");
    }
    if (destination === "London") {
        return 183;
    } else if (destination === "Paris") {
        return 220;
    } else {
        return 300;
    }
}

function rentalCarCost() {
    let days;
    while (isNaN(days) || days <= 0) {
        days = prompt("How many days would you like to rent the car?");
    }
    let cost = days * 40;
    if (days > 10) {
        cost *= 0.95;
    }
    return cost;
}

function totalVacationCost() {
    let hotel = hotelCost();
    let plane = planeRideCost();
    let car = rentalCarCost();
    return hotel + plane + car;
}

console.log(totalVacationCost());
