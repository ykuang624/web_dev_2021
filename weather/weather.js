
var wind_dict = {
    "NE": "Northeast",
    "SE": "Southeast",
    "SW": "Southwest",
    "NW": "Northwest",
    "NNE":"North-Northeast",
    "ENE": "East-Northeast",
    "ESE": "East-Southeast",
    "SSE": "South-Southeast",
    "SSW": "South-Southwest",
    "WSW": "West-Southwest",
    "WNW": "West-Northwest",
    "NNW": "North-Northwest"
  };

const BASE_URL = "http://api.weatherapi.com/v1";
APIKEY = "214aa59e5f274856927221106212702"
document.addEventListener("DOMContentLoaded", function(){
    // Zipcode Response
    var zipcodeSubmit= document.querySelector(".zipcode")
    zipcodeSubmit.addEventListener("click", function(e){
        var zipcode = document.querySelector(".form-control").value;
        var zip_url = BASE_URL+"/current.json?"+"key="+APIKEY+"&q="+zipcode.toString();
        updateContent(zip_url);
    })
    var currentSubmit = document.querySelector(".btn-primary")
    currentSubmit.addEventListener("click", function(e){
        e.preventDefault(); 
        if(navigator.geolocation) {
        var current_url= navigator.geolocation.getCurrentPosition(function(position){
            console.log("lala")
            let lat = position.coords.latitude;
            let long = position.coords.longitude;
            var loc_url = BASE_URL+"/current.json?"+"key="+APIKEY+"&q="+lat.toString()+","+long.toString();
            updateContent(loc_url);
        });
    }
    })
})



async function updateContent(url){
    var httpResponse = await fetch(url);

    var data = await httpResponse.json();
    if (httpResponse.ok){
        // get rid of the error message first
        var invalid = document.querySelector(".bla");
        console.log(invalid)
        if (typeof(invalid) != 'undefined' && invalid != null){
            invalid.remove();
        }
        document.querySelector("#name").textContent = `${data.location.name}`;
        document.querySelector("#region").textContent = `${data.location.region}`;
        var temp = `${data.current.temp_f}`;
        document.querySelector("#temp").textContent = Math.round(temp).toString();
        document.querySelector("#conditions").querySelector("img").src= "http:"+`${data.current.condition.icon}`;
        document.querySelector("#conditions").querySelector("strong").textContent= `${data.current.condition.text}`;
        var wind = `${data.current.wind_mph}`;
        document.querySelector("#wind_mph").textContent = Math.round(wind).toString();
        document.querySelector("#wind_direction").textContent = wind_dict[`${data.current.wind_dir}`]
    } else {
        document.querySelector("#name").textContent = "Invalid Zipcode";
        document.querySelector("#region").textContent = " ";
        // var newItem = document.createElement("p");
        // var textNode = ? 
    var textnode = document.createTextNode("Invalid Zipcode");  // Create a text node
    textnode.className = "bla";
    // newItem.appendChild(textnode);                    // Append the text to <li>

    var location = document.querySelector("#location");    // Get the <ul> element to insert a new node
    document.body.insertBefore(textnode, location); 
    }
    console.log(data)




    // console.log(httpresponse);
};