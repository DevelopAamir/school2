function uiInit(resultsSheet) {
    var subjectspace =  document.getElementById('subjects-space')
    var result_place = document.getElementById('resluts-place')
    subjectspace.innerHTML = '';
    result_place.innerHTML = '';
     resultsSheet.subjects.forEach(element => {
        subjectspace.innerHTML = subjectspace.innerHTML + element.widget()
     });
     document.getElementById('subject-count').innerHTML = resultsSheet.subjects.length;
     result_place.appendChild(resultsSheet.widget())
    var filter = document.getElementById('filter-by-section')
    onfilterbysection(filter)
}


function sendUpdate(resultsheet,token){
    var data = JSON.stringify(resultsheet)
    const urls = window. location. href 
    fetch(urls,{ method: "POST",
    
    headers: {
        "Content-Type": "application/json",
        "X-CSRFToken" : token
    },
    body: data
    
    })
    .then((response) => response.json())
    .then((data)=>{
        if(data.toString() == "Updated"){
            saveicon()
        }
        
    })
}


async function saveicon(){
    let player = document.querySelector("lottie-player");
    player.stop()
    player.play()
    await new Promise(r => setTimeout(r, 3000));
    player.stop();
}

