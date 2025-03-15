let RunSentimentAnalysis = () => {
    const textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            // Check if the status code is 200 (success)
            if (this.status == 200) {
                // If successful, display the system response
                let response = JSON.parse(xhttp.responseText);
                document.getElementById("system_response").innerHTML = response.response;
            } else if (this.status == 400) {
                // If the status is 400 (bad request), show the error message
                let response = JSON.parse(xhttp.responseText);
                document.getElementById("system_response").innerHTML = response.error;
            }
        }
    };

    // Send the request with the user input text
    xhttp.open("GET", "emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze), true);
    xhttp.send();
};
