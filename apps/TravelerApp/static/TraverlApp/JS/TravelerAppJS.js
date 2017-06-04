$(document).ready(function(){
    // Variable currently_today creates the current time for the moment.
    // This information must be parased and reconstructed to fit the min value for input type of date.
    var currently_today = new Date();
    // Day displays with length of 1 number if possible, but we need a zero for numbers below 9.
    var current_day = currently_today.getDate();
    // Month displays with length of 1 number and starts at 0. We need to add a zero as we did for day.
    var current_month = currently_today.getMonth()+1;
    
    var yyyy = currently_today.getFullYear();

    // Go through the process of adding a zero if the day and month is less than 9.
    if(current_day < 10){
            current_day= '0' + current_day
        } 
        if(current_month < 10){
            current_month= '0' + current_month
        } 
    // remake the currently_today variable to have the new wanted format.
    currently_today = yyyy+'-' + current_month + '-'+current_day;
    console.log(currently_today)
    document.getElementById("current_day").setAttribute("min", currently_today)
})

