console.log('connected')

let likes1 = document.querySelector('#likes1')
let likes2 = document.querySelector('#likes2')
let likes3 = document.querySelector('#likes3')

let likesArr = [9, 12, 9]

function addLike1() {
    likesArr[0]++
    likes1.innerText = likesArr[0]
}

function addLike2() {
    likesArr[1]++
    likes2.innerText = likesArr[1]
}

function addLike3() {
    likesArr[2]++
    likes3.innerText = likesArr[2]
}