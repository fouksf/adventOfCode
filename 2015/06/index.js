const fs = require('fs')
const strings = fs.readFileSync(__dirname + '/input.txt').toString().split('\n')

function parseLine(line) {
    const parts = line.split(' ')
    if (parts.length === 4) {
        return {
            verb: parts[0],
            start: parts[1].split(',').map(str => Number(str)),
            end: parts[3].split(',').map(str => Number(str)),
        }
    }

    return {
        verb: parts[1],
        start: parts[2].split(',').map(str => Number(str)),
        end: parts[4].split(',').map(str => Number(str)),
    }
}

const actions = strings.map(parseLine)
const lights = {}

for (let i = 0; i < actions.length; i++) {
    const { verb, start, end } = actions[i]
    const [ x1, y1 ] = start
    const [x2, y2 ] = end

    for (let x = x1; x <= x2; x++ ) {
        for (let y = y1; y <= y2; y++) {
            if (lights[`${x},${y}`] === undefined) {
                lights[`${x},${y}`] = 0
            }
            if (verb === 'on') {
                lights[`${x},${y}`] += 1
            } else if (verb === 'off') {
                lights[`${x},${y}`] -= 1
                if (lights[`${x},${y}`] < 0) {
                    lights[`${x},${y}`] = 0
                }
            } else if (verb === 'toggle') {
                lights[`${x},${y}`] += 2
            } else {
                throw new Error(`This should not happen, verb was "${verb}"`)
            }
        }
    }
}

let count = 0
for (const point in lights) {
    count += lights[point]
}

console.log(count)
