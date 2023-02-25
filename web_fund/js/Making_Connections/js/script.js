console.log("Javascript is connected")

let userName = document.querySelector("#userName")
let request1 = document.querySelector("#request1")
let request2 = document.querySelector("#request2")
let requestCount = document.querySelector("#requestCount")
let connectionCount = document.querySelector("#connectionCount")

let numRequests = 2
let numConnections = 418

function editProfile() {
    userName.innerText = "Wonder Woman"
}

function acceptRequest1() {
    request1.remove();
    numRequests--
    numConnections++
    updateCounts(numRequests, numConnections)
}

function acceptRequest2() {
    request2.remove();
    numRequests--
    numConnections++
    updateCounts(numRequests, numConnections)
}

function updateCounts(requests, connections) {
    requestCount.innerText = numRequests
    connectionCount.innerText = numConnections
}

function declineRequest1() {
    request1.remove();
    numRequests--
    updateCounts(numRequests, numConnections)
}

function declineRequest2() {
    request2.remove();
    numRequests--
    updateCounts(numRequests, numConnections)
}
