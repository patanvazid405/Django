console.log("hello world...")

let btn = document.getElementById("btn")
btn.addEventListener("click",()=>{
    let n = document.getElementById("name").value 
    let a = document.getElementById("age").value 
    let d = document.getElementById("dept").value 
    let c = document.getElementById("city").value 
    let empData = {
        name :n,
        age : a,
        dept :d,
        city : c,
    };
    console.log(n,a,d,c)
    fetch("http://127.0.0.1:8000/add_employee/",{
        method : "POST",
        headers:{
            "Content-Type" : "application/json",
        },
        body: JSON.stringify(empData)
    })
    .then((res)=>res.json())
    .then((data)=>console.log(data))
    .catch(()=>console.log("error"))

})


