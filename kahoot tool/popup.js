let longbtn = document.getElementById("longbtn");
let blankbtn = document.getElementById("blankbtn");
let kahoot_nicknime_input = document.getElementById("nickname");
function long() {
    window.document.getElementById("nickname").maxLength = 999999;
}
function blank() {
    window.document.getElementById("nickname").value = "   ‍   ";
}
longbtn.addEventListener("click", async () => {
    try {
        let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
        chrome.scripting.executeScript({
            target: { tabId: tab.id },
            function: long,
        });
    }
    catch (e) {
        alert('there is a error: ' + e);
    }
});
blankbtn.addEventListener("click", async () => {
    try {
        let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
        chrome.scripting.executeScript({
            target: { tabId: tab.id },
            function: blank,
        });
    }
    catch (e) {
        alert('there is a error: ' + e);
    }
});