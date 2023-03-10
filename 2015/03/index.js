const fs = require('fs')
const input = fs.readFileSync('./input.txt').toString().split('')

let sx = 0
let sy = 0

let rx = 0
let ry = 0

let isSanta = true

const visited = new Set([`0, 0`])
for (const instruction of input) {
    if (instruction === '^') {
        if (isSanta) {
            sy+=1
        } else {
            ry+=1
        }
    } else if (instruction === 'v') {
        if (isSanta) {
            sy-=1
        } else {
            ry-=1
        }
    } else if (instruction === '>') {
        if (isSanta) {
            sx+=1
        } else {
            rx+=1
        }
    } else if (instruction === '<') {
        if (isSanta) {
            sx-=1
        } else {
            rx-=1
        }
    } else {
        throw('bad things')
    }

    isSanta = !isSanta

    visited.add(`${sx}, ${sy}`)
    visited.add(`${rx}, ${ry}`)
}

console.log(visited.size)