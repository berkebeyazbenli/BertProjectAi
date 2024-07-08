// web/script.js
async function loadPDF() {
    let filePath = document.getElementById('file_path').value;
    let response = await fetch(`/load-pdf?file_path=${filePath}`);
    let data = await response.text();
    document.getElementById('context').value = data.substring(0, 1000);
}

async function askQuestion() {
    let question = document.getElementById('question').value;
    let context = document.getElementById('context').value;
    let response = await fetch(`/ask?question=${question}&context=${context}`);
    let data = await response.text();
    document.getElementById('answer').innerText = data;
}
