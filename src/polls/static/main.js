const search_data = JSON.parse(document.getElementById('init-search-data').textContent);

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.autocomplete');
    let options = {
        data: search_data
    }
    var instances = M.Autocomplete.init(elems, options);
});

const redirect = () => {
    let input = document.getElementById("search-input");
    window.location.href = `${input.value}`;
    return false;
}