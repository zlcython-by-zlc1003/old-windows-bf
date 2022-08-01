// Initialize button with user's preferred color
var isstoptf = false;
var now = 0;
var maxcolor = 16777215;
let changeColor = document.getElementById("changeColor");
let nnnn = document.getElementById("nnnn");
let rb = document.getElementById("rinble");
let stopbtn = document.getElementById("stop__");
chrome.storage.sync.get("color", ({ color }) => {
    changeColor.style.backgroundColor = color;
    nnnn.style.backgroundColor = "#F7F7F7"
});

function sleep(ms) {
    const d = new Date();
    time = d.getTime();
    while (true) {
        const ad = new Date();
        nowtime = ad.getTime();
        if (nowtime - time > ms) {
            break;
        }
    }
}

function stop(){isstoptf = true;console.log('stop');}
function runner() {
    try {
        var maxcolor = 16777215;
        now++;
        if (now == maxcolor) {
            now = 0;
        }
        now16 = now.toString(16);
        if (now16.length == 6) { }
        else if (now16.length == 5) { now16 = "0" + now16; }
        else if (now16.length == 4) { now16 = "00" + now16; }
        else if (now16.length == 3) { now16 = "000" + now16; }
        else if (now16.length == 2) { now16 = "0000" + now16; }
        else if (now16.length == 1) { now16 = "00000" + now16; }
        document.body.style.backgroundColor = "#" + now16;
    }
    catch (e) {alert('there is a error: ' + e);}
    if (isstoptf == false){setTimeout(runner, 100);};
    if (isstoptf == true){isstoptf = false;}
}
function setPageBackgroundColor() {
    chrome.storage.sync.get("color", ({ color }) => {
        try {
            document.body.style.backgroundColor = color;
        }
        catch (e) {
            alert('there is a error: ' + e);
        }
    });
}

function setn() {
    chrome.storage.sync.get("color", ({ color }) => {
        try {
            document.body.style.backgroundColor = "#FFFFFF";
        }
        catch (e) {
            alert('there is a error: ' + e);
        }
    });
}

changeColor.addEventListener("click", async () => {
    try {
        let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
        chrome.scripting.executeScript({
            target: { tabId: tab.id },
            function: setPageBackgroundColor,
        });
    }
    catch (e) {
        alert('there is a error: ' + e);
    }
});
nnnn.addEventListener("click", async () => {
    try {
        let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
        chrome.scripting.executeScript({
            target: { tabId: tab.id },
            function: setn,
        });
    }
    catch (e) {
        alert('there is a error: ' + e);
    }
});
rb.addEventListener("click", async () => {
    try {
        let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
        chrome.scripting.executeScript({
            target: { tabId: tab.id },
            function: runner,
        });
    }
    catch (e) {
        alert('there is a error: ' + e);
    }
});

stopbtn.addEventListener("click", async () => {
    try {
        let [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
        chrome.scripting.executeScript({
            target: { tabId: tab.id },
            function: stop,
        });
    }
    catch (e) {
        alert('there is a error: ' + e);
    }
});