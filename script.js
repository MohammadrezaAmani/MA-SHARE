const textArea = document.getElementById("text-area");
const saveButton = document.getElementById("save-button");
const loadButton = document.getElementById("load-button");

// Save the text to the server
saveButton.addEventListener("click", async () => {
    const text = textArea.value;
    await fetch("/save", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ text }),
    });
    alert("Text saved successfully.");
});

// Load the text from the server
loadButton.addEventListener("click", async () => {
    const response = await fetch("/load");
    const data = await response.json();
    textArea.value = data.text;
});
