const fs = require('fs')
const strings = fs.readFileSync(__dirname + '/input.txt').toString().split('\n')
// const strings = ['ugknbfddgicrmopn', 'aaa', 'jchzalrnumimnmhp', 'haegwjzuvuyypxyu', 'dvszwmarrgswjxmb']
function hasAtLeastThreeVowels(str) {
    const replaced = str.replace(/[^aeiou]/ig,'')
    return replaced.length >= 3
}

function hasRepeatedChar(str) {
    for(let i = 0; i < str.length - 1; i++) {
        const a = str[i]
        const b = str[i + 1]

        if (a === b) {
            return true
        }
    }

    return false
}

function hasBadPairs(str) {
    const badPairs = new Set(['ab', 'cd', 'pq', 'xy'])

    for(let i = 0; i < str.length - 1; i++) {
        const a = str[i]
        const b = str[i + 1]
        const pair = a + b
        if (badPairs.has(pair)) {
            return true
        }
    }

    return false
}

function isNice(string) {
    return hasAtLeastThreeVowels(string) && hasRepeatedChar(string) && !hasBadPairs(string)
}

console.log(strings.filter(isNice).length)
