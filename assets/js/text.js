const textArea = document.getElementById("text-area");
const saveButton = document.getElementById("save-button");
const loadButton = document.getElementById("load-button");

// Save the text to the server
saveButton.addEventListener("click", async () => {
    const content = textArea.value;
    await fetch("", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ content }),
    });
    alert("Text saved successfully.");
});
