const API_URL = "http://127.0.0.1:8000";


async function getItem(amount, category) 
{
    // http://127.0.0.1:8000/getentries/?n=2&category=Cracking
    const response = await fetch(`${API_URL}/getentries/?n=${amount}&category=${category}`);

    if (!response.ok) {
        const body = await response.json().catch(() => null);
        throw new Error(
            `Request failed: ${response.status}\n` + JSON.stringify(body, null, 2)
        );
    }

    return await response.json();
}

document.getElementById("Go").addEventListener("click", async() => {
    const amount = Number(document.getElementById("amount").value);
    const category = document.getElementById("category").value;

    const output = document.getElementById("output");

    try {
        const data = await getItem(amount, category);
        console.log("data:", data);
        output.textContent = JSON.stringify(data, null, 2);
    } catch (err) {
        output.textContent = err.message;
    }
});
