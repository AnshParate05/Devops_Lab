function handleForm(event) {
    event.preventDefault();
    const name = document.getElementById('name').value;
    const status = document.getElementById('status');
    
    // This exact string is what Selenium will look for
    status.innerText = "Success! Test passed for: " + name;
    status.style.color = "#00ff88";
    status.style.fontWeight = "bold";
}
