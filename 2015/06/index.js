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
const onLights = new Set()

for (let i = 0; i < actions.length; i++) {
    const { verb, start, end } = actions[i]
    const [ x1, y1 ] = start
    const [x2, y2 ] = end

    for (let x = x1; x <= x2; x++ ) {
        for (let y = y1; y <= y2; y++) {
            if (verb === 'on') {
                onLights.add(`${x},${y}`)
            } else if (verb === 'off') {
                onLights.delete(`${x},${y}`)
            } else if (verb === 'toggle') {
                if (onLights.has(`${x},${y}`)) {
                    onLights.delete(`${x},${y}`)
                } else {
                    onLights.add(`${x},${y}`)
                }
            } else {
                throw new Error(`This should not happen, verb was "${verb}"`)
            }
        }
    }


}

console.log(onLights.size)