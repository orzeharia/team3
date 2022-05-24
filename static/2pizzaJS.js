const activePage = window.location.pathname;
/* -------------- Home -------------- */
if (activePage.includes("home.html")){
document.querySelector("#homeOrderBtn").addEventListener("click",()=>{
     window.location.href = window.location.href.replace("home.html","Order_qestions.html")
})
}


/*...................................... */



document.querySelectorAll('header a').forEach(link => {
    if (link.href.includes(activePage))
        link.classList.add('active-nav');
})