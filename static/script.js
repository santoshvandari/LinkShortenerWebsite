let copytext=document.getElementById("shortedurl");
let successPara=document.querySelector("p.success");
document.getElementById('copybtn').addEventListener('click',()=>{
    navigator.clipboard.writeText(copytext.value);
    successPara.textContent="URL Copied Successfully!!!";
})
