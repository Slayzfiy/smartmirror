// TAG FUNCTIONS
const searchWrapper = document.querySelector(".search-input");
const inputBox = searchWrapper.querySelector("input");
const suggestionBox = searchWrapper.querySelector(".autocom-box");
const icon = searchWrapper.querySelector(".icon");

inputBox.onkeyup = (e)=>{
    let userData = e.target.value;
    let emptyArray = [];
    if(userData){
        icon.onclick = ()=>{
            let firstSuggestion = suggestionBox.getElementsByTagName('li')[0].innerText;
            createStockTag(firstSuggestion, true);
            resetSuggestionBox()
        }

        $("#stockInput").keydown(function(event){
            if( (event.keyCode === 13)) {
                event.preventDefault();
            }
        });

        emptyArray = suggestions.filter((data)=>{
            return data.toLocaleLowerCase().startsWith(userData.toLocaleLowerCase());
        });
        emptyArray = emptyArray.map((data)=>{
            return data = `
                        <li>${data}
                            <button type="button" class="close stockClose" aria-label="Close">
                                   <span class="text-dark"><i class="fas fa-plus"></i></span>
                            </button>
                        </li>`;
        });
        // show autocomplete box and add suggestions
        searchWrapper.classList.add("active");
        showSuggestions(emptyArray);
        let allList = suggestionBox.querySelectorAll("li");
        //adding onclick attribute in all li tag
        for (let i = 0; i < allList.length; i++) {
            allList[i].setAttribute("onclick", "createStockTag(this.innerText, true)");
        }

    }else{
        searchWrapper.classList.remove("active"); //hide autocomplete box
    }
}
function showSuggestions(list){
    let listData;
    if(!list.length){
        listData = `<li>${userValue}</li>`;
    }else{
        listData = list.join('');
    }
    suggestionBox.innerHTML = listData;
}
function createStockTag(stockName, postData){
    let Tag = `
                            <span class="greenContainer">
                                <a class="text-white stockName" >`+stockName+`</a>
                                <button type="button" class="close stockClose" aria-label="Close" onclick="removeTag(this)">
                                    <span aria-hidden="true">&times;</span>
                                </button>
                            </span>
                           `

    document.querySelector('#stockTags').innerHTML += Tag;
    resetSuggestionBox()
    if(postData === true){
        $.ajax({
            type: "POST",
            url: "/stocks",
            data: {"stockToAdd": stockName},
            success:function (){
                notify('Added $' + stockName + ' Stock to watchlist!', 'success')
            }
        })
        e.preventDefault();
    }
}
function removeTag(e){
    $(e).closest('.greenContainer').fadeTo(500, 0.01, function(){
        $(e).slideDown(200, function() {
            $(e).closest('.greenContainer').remove();
            $.ajax({
                type: "POST",
                url: "/stocks",
                data: {"tagToRemove": $(e).siblings().text()},
                success:function (){
                    notify('Successfully removed stock from watchlist!', 'danger')
                }
            })
            e.preventDefault();
        });
    });
    // $(e).closest('.redContainer').fadeTo(500, 0.01, function(){
    //     $(e).slideDown(200, function() {
    //         $(e).closest('.redContainer').remove();
    //     });
    // });
}
function resetSuggestionBox(){
    inputBox.value = "";
    searchWrapper.classList.remove("active");
}
// END

function checkCurrency(currency){
    let $currencyBox = $('#currencySelection')
    let $currencyPlaceholder = $('#currency_placeholder')

    $currencyBox.val(currency);
    $currencyPlaceholder.text(currency);
    changeCurrencyPlaceholder()

    $currencyBox.change(function (e){
        changeCurrencyPlaceholder()
    })

    function changeCurrencyPlaceholder(){
        let $currentCurrency = $currencyBox.val();
        if ($currentCurrency === "EUR"){
            $currencyPlaceholder.text("€")
        }
        if ($currentCurrency === "USD"){
            $currencyPlaceholder.text("$")
        }
        if ($currentCurrency === "GBP"){
            $currencyPlaceholder.text("£")
        }
    }
}


// END


// MULTISELECT FUNCTION
$(document).ready(function() {
    $('#example-getting-started').multiselect({
        includeSelectAllOption: true,
        enableFiltering: true,
        selectedClass: "select"
    });
});
// END


