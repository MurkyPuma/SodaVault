// Initial fetch
let start = 0;
let limit = 20;  // How many items you want to fetch in each request
let debounceTimeout;
let isDataLoading = false;
let isSearchActive = false;  // Indicates whether a search is currently active
let searchQuery = '';


document.addEventListener('DOMContentLoaded', function () {
    const currentPath = window.location.pathname;
    const regex = /^\/drinks\/\d+$/;

    // Check if the current path is a drink detail page
    if (regex.test(currentPath)) {
        likeButtonFunctionality();
        // generateImage();
    }

    // Check if the current path is the drinks list page
    if (currentPath === '/drinks/') {
        fetchMainDrinks();  // Load initial drinks

        const searchInput = document.getElementById('search-input');
        const filterRadios = document.querySelectorAll('input[name="filter"]');


        searchInput.addEventListener('input', function () {
            clearTimeout(debounceTimeout);
            debounceTimeout = setTimeout(function () {
                start = 0;
                isSearchActive = true;
                searchQuery = searchInput.value.trim().toLowerCase();
                searchDrinks();
            }, 200);
        });

        filterRadios.forEach(radio => {
            radio.addEventListener('change', function () {
                if (isSearchActive && searchQuery) {
                    start = 0; // Reset start index for a new search
                    searchDrinks(); // Trigger search with the new filter
                }
            });
        });

        window.onscroll = function () {
            if (window.innerHeight + window.scrollY >= document.body.offsetHeight - 1000 && !isDataLoading) {
                isDataLoading = true;
                if (isSearchActive && searchQuery) { // Check if a search is active and searchQuery is not empty
                    searchDrinks();
                } else {
                    fetchMainDrinks();
                }
            }
        };
    }
});

function likeButtonFunctionality() {
    var likeButton = document.getElementById('like-button');
    if (likeButton) { // Check if the likeButton exists
        likeButton.addEventListener('click', function () {
            this.classList.toggle('liked'); // Use 'this' to refer to the likeButton within the event listener
        });
    } else {
        console.log('Like button not found.'); // Helpful for debugging
    }
}

function displayDrinks(drinks, append = true) {
    const drinksGrid = document.getElementById('random-results');
    if (!append) drinksGrid.innerHTML = ''; // Clear the existing content if not appending

    drinks.forEach(function (drink) {
        const drinkElement = `
            <a href="/drinks/${drink.id}" class="drink-block">
                <img src="${drink.thumbnail}" alt="${drink.name}" class="drink-image"/>
                <h2 class="drink-name">${drink.name}</h2>
            </a>
        `;
        drinksGrid.innerHTML += drinkElement;
    });
}

function fetchMainDrinks() {
    console.log(start, limit);
    axios.get(`/api/random/?start=${start}&limit=${limit}`)
        .then(function (response) {
            displayDrinks(response.data, true); // Append new drinks
            start += limit; // Prepare start for the next batch of results
            isDataLoading = false; // Clear the flag after the data is appended
        })
        .catch(function (error) {
            console.error('Error fetching drinks:', error);
            isDataLoading = false; // Ensure to clear the flag even if there is an error
        });
}

async function searchDrinks() {
    if (!searchQuery) {
        displayDrinks([], false); // Clear existing results if searchQuery is empty
        isSearchActive = false; // Reset search state if query is cleared
        if (start === 0) fetchMainDrinks(); // Reload main drinks if at the beginning and no search query
        return; // Exit if no search query
    }

    let filterValue = document.querySelector('input[name="filter"]:checked').value;

    try {
        const endpoint = filterValue === 'name' ? '/api/search/name' : '/api/search/ingredient';
        const response = await axios.get(`${endpoint}?q=${encodeURIComponent(searchQuery)}&start=${start}&limit=${limit}`);
        displayDrinks(response.data, start > 0); // Append if not the first set
        start += limit;
    } catch (error) {
        console.error('Error fetching search results:', error);
    } finally {
        isDataLoading = false; // Ensure isDataLoading is reset after operation
    }
}

// Add this to your existing JavaScript
function toggleAlcohol() {
    var toggleLeft = document.getElementById('toggle-left');
    var toggleRight = document.getElementById('toggle-right');
    // Assuming you're using a class "active" to highlight the selection
    toggleLeft.classList.toggle('active');
    toggleRight.classList.toggle('active');

    // Your logic to filter drinks goes here
    var showAlcoholic = toggleRight.classList.contains('active');
    // Redirect or AJAX call to update the drinks list
    // For example, using a URL parameter to filter drinks on the server:
    window.location.href = '?show_alcoholic=' + showAlcoholic;
}






// function getDrinkDetails() {
//     // Get the drink ID from the data-drink-id attribute of the like button
//     let drinkId = document.getElementById('like-button').getAttribute('data-drink-id');
//     // Fetch the drink details from the server
//     axios.get(`/api/${drinkId}`)
//         .then(response => {
//             // Extract the drink details from the response
//             let drink = response.data;

//             // Prepare the HTML content to display the drink details
//             let htmlContent = `
//                 <div class="drink-detail-image">
//                     <img src="${drink.thumbnail}" alt="${drink.name}" />
//                 </div>
//                 <div class="drink-detail-name">${drink.name}</div>
//                 <div class="drink-info">
//                     <div class="glass-type">Glass: ${drink.glass}</div>
//                     <div class="ingredients">
//                         <h3>Ingredients</h3>
//                         <ul>
//                             ${generateIngredientList(drink)}
//                         </ul>
//                     </div>
//                     <div class="instructions">
//                         <h3>Instructions</h3>
//                         <p>${drink.instructions}</p>
//                     </div>
//                 </div>
//             `;

//             // Display the drink details in the drink-details div
//             document.getElementById('drink-details').innerHTML = htmlContent;
//         })
//         .catch(error => {
//             console.error('Error fetching drink details:', error);
//         });
// }


// function generateIngredientList(drink) {
//     // Generate the HTML for the ingredient list
//     var ingredientList = '';
//     for (var i = 1; i <= 9; i++) {
//         var ingredient = drink[`ingredient${i}`];
//         var measurement = drink[`measurement${i}`];
//         if (ingredient && measurement) {
//             ingredientList += `<li>${ingredient} ${measurement}</li>`;
//         }
//     }
//     return ingredientList;
// }
// function generateImage() {
//     // Get the drink ID from the data-drink-id attribute of the like button
//     let drinkId = document.getElementById('like-button').getAttribute('data-drink-id');
//     // Fetch the drink details from the server
//     axios.get(`/api/${drinkId}`)
//         .then(response => {
//             // Extract the drink details from the response
//             let drink = response.data;
//             if (drink.thumbnail === '/media/default.png' && drink.instructions && drink.author === null) {
//                 console.log('No image available');

//             }


//         })

//         .catch(error => {
//             console.error('Error fetching drink details:', error);
//         });
// }