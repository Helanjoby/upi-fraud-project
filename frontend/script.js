function checkTransaction(){

let upi=document.getElementById("upi_id").value;
let amount=document.getElementById("amount").value;
let note=document.getElementById("note").value;

let resultBox=document.getElementById("result");

resultBox.innerText="Checking...";
resultBox.className="";

fetch("http://127.0.0.1:5000/check_transaction",{

method:"POST",

headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({

upi_id:upi,
amount:amount,
note:note

})

})

.then(response=>response.json())

.then(data=>{

resultBox.innerText=data.result;

if(data.result.includes("Fraud")){

resultBox.classList.add("fraud");

}

else{

resultBox.classList.add("safe");

}

})

.catch(error=>{

resultBox.innerText="Server Error";

});

}