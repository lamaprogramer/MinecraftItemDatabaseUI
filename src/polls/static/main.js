const search_data = JSON.parse(document.getElementById('init-search-data').textContent);

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.autocomplete');
    let options = {
        data: search_data
    }
    var instances = M.Autocomplete.init(elems, options);

    var sidenav_elems = document.querySelectorAll('.sidenav');
    var sidenav_instances = M.Sidenav.init(sidenav_elems, {});
});

const redirect = () => {
    let input = document.getElementById("search-input");
    window.location.href = `${input.value}`;
    return false;
}