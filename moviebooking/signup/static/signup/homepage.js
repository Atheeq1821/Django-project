let popUp = document.getElementById("popup")
function openPopup(){
    popUp.classList.add("open-popup")
}
function closePopup(){
    popUp.classList.remove("open-popup")
}
const ticketDisplay = document.getElementById("ticket")
const totalPrice = document.getElementById("totalprice")
const addTicket = document.getElementById("add-btn")
let price = 120
let count=0
let rupees="₹"
addTicket.addEventListener("click",function(){
        currentPrice=parseInt(totalPrice.textContent)
        currentCount=parseInt(ticketDisplay.textContent)
        totalPrice.textContent=currentPrice+price
        ticketDisplay.textContent=currentCount+=1

})