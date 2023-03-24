const fs = require('fs')
const strings = fs.readFileSync(__dirname + '/input.txt').toString().split('\n')
// const strings = ['qjhvhtzxzqqjkmpb', 'xxyxx', 'uurcxstgmygtbstg', 'ieodomkazucvgmuy']
function nice(str){
    const vowels = str.match(/(\w).\1/g);
    const doubles = str.match(/(\w\w).*\1/g);
    return (vowels !== undefined && vowels !== null && vowels.length > 0)
        && (doubles !== undefined && doubles !== null && doubles.length > 0)
}

// console.log(strings.filter(nice))
console.log(strings.filter(nice).length)
