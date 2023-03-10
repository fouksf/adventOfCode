const fs = require('fs')
const input = fs.readFileSync('./input.txt').toString()

function surfaceArea(w, h, l) {
    return 2 * l * w + 2 * w * h + 2 * h * l
}

function findSlack(w, h, l) {
    const biggest = Math.max(w, h, l)
    return (w * h * l) / biggest
}

const lines = input.split('\n')

let sqFt = 0

for (const line of lines) {
    const [l, w, h] = line.split('x').map(dim => Number(dim))
    sqFt += surfaceArea(l, w, h) + findSlack(l, w, h)
}

console.log(sqFt)

function lowestPerimeter(w, h, l) {
    const longest = Math.max(w, h, l)
    return 2 * (w + h + l - longest)
}

let length = 0
for (const line of lines) {
    const [l, w, h] = line.split('x').map(dim => Number(dim))
    length += lowestPerimeter(l, w, h) + l * w * h
}
console.log(length)