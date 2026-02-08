/* CHAT DATA */
const chats = {
    "User 1": [
        { type: "received", text: "Hello 👋" },
        { type: "sent", text: "Hi!" }
    ],
    "User 2": [
        { type: "received", text: "Hey there" },
        { type: "sent", text: "How are you?" }
    ]
};

const chatItems = document.querySelectorAll(".chat-item");
const messagesBox = document.getElementById("messages");
const chatUserName = document.getElementById("chatUserName");
let currentUser = "User 1";

/* LOAD CHAT */
function loadChat(user) {
    currentUser = user;
    chatUserName.textContent = user;
    messagesBox.innerHTML = "";

    chats[user].forEach(msg => {
        const div = document.createElement("div");
        div.className = `msg ${msg.type}`;
        div.textContent = msg.text;
        messagesBox.appendChild(div);
    });

    // 🔽 Auto scroll to bottom
    messagesBox.scrollTop = messagesBox.scrollHeight;
}


chatItems.forEach(item => {
    item.addEventListener("click", () => {
        chatItems.forEach(i => i.classList.remove("active"));
        item.classList.add("active");
        loadChat(item.textContent.trim());
    });
});

loadChat("User 1");

/* SEND MESSAGE */
document.getElementById("sendBtn").addEventListener("click", () => {
    const input = document.getElementById("msgInput");
    if (!input.value.trim()) return;

    chats[currentUser].push({ type: "sent", text: input.value });
    loadChat(currentUser);
    input.value = "";
});

/* LEFT MENU */
const leftMenu = document.getElementById("leftMenu");
const leftPopup = document.getElementById("leftPopup");

leftMenu.onclick = (e) => {
    leftPopup.style.display = "block";
    leftPopup.style.top = "50px";
    leftPopup.style.right = "10px";
    e.stopPropagation();
};

/* RIGHT MENU */
const rightMenu = document.getElementById("rightMenu");
const rightPopup = document.getElementById("rightPopup");

rightMenu.onclick = (e) => {
    rightPopup.style.display = "block";
    rightPopup.style.top = "50px";
    rightPopup.style.right = "10px";
    e.stopPropagation();
};

/* SEARCH */
const searchBtn = document.getElementById("searchBtn");
const chatSearch = document.getElementById("chatSearch");

searchBtn.onclick = () => {
    chatSearch.style.display =
        chatSearch.style.display === "block" ? "none" : "block";
};

/* IMAGE MODAL */
const profileImg = document.getElementById("myProfile");
const imageModal = document.getElementById("imageModal");

profileImg.onclick = () => imageModal.style.display = "flex";
imageModal.querySelector(".close").onclick = () => imageModal.style.display = "none";

/* CLOSE POPUPS */
document.addEventListener("click", () => {
    leftPopup.style.display = "none";
    rightPopup.style.display = "none";
});
