document.getElementById("shorten").onclick = () => {
  testFetch();
  document.getElementById("surl").innerHTML = "Hello"
}


function testFetch(){
  payload={
    name: "Manas",
    phone:7483728745
  };
  fetch("http://localhost:5000/t", {
    method: "POST",
    credentials: "include",
    body: JSON.stringify(payload),
    cache: "no-cache",
    headers: new Headers({
      "content-type": "application/json"
    })
  }).then((res) => {
    if(res.status != 200){
      console.log("Response status was not 200: " + res.status + "")
      return ;
    }
    res.json().then((data) => {
      console.log(data);
    })
  })
}