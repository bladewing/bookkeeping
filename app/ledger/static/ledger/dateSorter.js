function dateSorter(a, b) {
    //alert(Date.parse(a.date));
    if (new Date(a.date) < new Date(b.date)) return 1;
    if (new Date(a.date) > new Date(b.date)) return -1;
    return 0;
}
