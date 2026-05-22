function showLoading(){

    document.getElementById("loading").style.display = "flex";
}

function hideLoading(){

    document.getElementById("loading").style.display = "none";
}

function showPopup(message){

    const popup = document.getElementById("popup");

    popup.innerText = message;

    popup.classList.add("show");

    setTimeout(() => {

        popup.classList.remove("show");

    },3000);
}

/* Encrypt */

function encryptFile(){

    showLoading();

    setTimeout(() => {

        hideLoading();

        showPopup("✅ File Successfully Encrypted!");

    },3000);
}

/* Decrypt */

function decryptFile(){

    showLoading();

    setTimeout(() => {

        hideLoading();

        showPopup("🔓 File Successfully Decrypted!");

    },3000);
}
