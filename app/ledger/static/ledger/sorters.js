function dateSorter(a, b) {
    if (new Date(a.date) < new Date(b.date)) return 1;
    if (new Date(a.date) > new Date(b.date)) return -1;
    return 0;
}

function floatSorter(a, b) {
    if (parseFloat(a.price) < parseFloat(b.price)) return 1;
    if (parseFloat(a.price) > parseFloat(b.price)) return -1;
    return 0;
}

function stringCaseInsensitiveSorter(a, b) {
    return (a.name.toString().toLowerCase()).localeCompare(b.name.toString().toLowerCase())
}