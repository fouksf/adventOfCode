const fs = require('fs')
const input = fs.readFileSync('./input.txt').toString().split('')

let x = 0
let y = 0

const visited = new Set([`${x}, ${y}`])
for (const instruction of input) {
    if (instruction === '^') {
        y += 1
    } else if (instruction === 'v') {
        y -= 1
    } else if (instruction === '>') {
        x += 1
    } else if (instruction === '<') {
        x -= 1
    } else {
        throw('bad things')
    }

    visited.add(`${x}, ${y}`)
}

console.log(visited.size)