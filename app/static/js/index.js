function submit(e){
    e.preventDefault();
    const val = document.getElementById('code').value;
    const props = {
        method: "POST", credentials: "include",
        headers: {
            'Content-Type': 'application/json'
        }, 
        body: JSON.stringify({code: val})
    }
    console.log(val);
    fetch("/yuufoundyitwaw",props).then(response=>response.json()).then(data=>{
        console.log(data);
        if(data.success)
        {
            window.location.href = data.url;
        }
        else{
            alert("Wrong Code!")
        }
    });
}
document.getElementById('form').addEventListener("submit", submit);