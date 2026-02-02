console.log("hello world...")

let btn = document.getElementById("btn")
let Employeesdiv = document.getElementById("Employeesdiv")
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
        
    }
    console.log(n,a,d,c);
    
    
    fetch("http://127.0.0.1:8000/add_employee/",{
        method : "POST",
        headers:{
            "Content-Type" : "application/json",
        },
        body: JSON.stringify(empData)
    })
    .then((res)=>res.json())
    .then((res)=>console.log(res))
    .catch(()=>console.log("error"))

})

//get employee
  fetch("http://127.0.0.1:8000/get_employee/")
    //     method : "POST",
    //     headers:{
    //         "Content-Type" : "application/json",
    //     },
    //     body: JSON.stringify(empData)    
    // })
    .then((res)=>res.json())
    .then((res)=>{
        for(let i=0;i<res.emp.length;i++){
            // console.log(res.emp[i])
            let empDiv = document.createElement('div')
            empDiv.style.backgroundColor = "yellow"
            empDiv.style.height = "200px"
            empDiv.style.textAlign ="center"
            empDiv.innerHTML = `
                        <p>${res.emp[i].name}</p>
                        <p>${res.emp[i].age}</p>
                        <p>${res.emp[i].dept}</p>
                        <p>${res.emp[i].city}</p>`
            
            Employeesdiv.append(empDiv)

        }

    })
    .catch((err)=>console.log(err))



