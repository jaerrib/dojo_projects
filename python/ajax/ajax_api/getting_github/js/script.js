console.log("Javascript is connected")

let follower_info = document.querySelector("#follower_info")
let avatar = document.querySelector("#avatar")


async function getGitHub() {
    // The await keyword lets js know that it needs to wait until it gets a response back to continue.
    var response = await fetch("https://api.github.com/users/jaerrib");
    // We then need to convert the data into JSON format.
    var coderData = await response.json();
    follower_info.innerText = coderData.login + " has " + coderData.followers + " followers"
    document.getElementById("avatar").src = coderData.avatar_url;
    return coderData;
}