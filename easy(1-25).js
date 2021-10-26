function twoNumberSum(array, targetSum) {
    
    let output= [];
    let sum = 0;
    for (let i = 0; i < array.length; i++) {
        for (let j = 0; j < array.length; j++){
            if (i !== j) {
                sum = array[i] + array[j];
                if (sum == targetSum) {
                    output.push(array[i]);
                    output.push(array[j]);
                    return output;
                }
            }
        }
    }
    return output;
}
// console.log(twoNumberSum([4, 6, 8], 14));

function isValidSubsequence(array, sequence) {
	let j = 0;
	for (let i = 0; i < array.length; i++) {
		if (array[i] == sequence[j]) {
			j+= 1;
		}
	}
	if (j == sequence.length) {
		return true;
	}
	return false;
}

function sortedSquaredArray(array) {
    let output= [];
    for (let i = 0; i < array.length; i++) {
        output.push(array[i]**2);
    }
    output.sort((a, b) => a-b);
    return output;
}
// console.log(sortedSquaredArray([-3, -2, -1]));

function tournamentWinner(competitions, results) {
    let points = {};
    for (let i = 0; i < competitions.length; i++) {
        if (results[i] == 0) {
            points[competitions[i][1]] = (points[competitions[i][1]] || 0) + 3;
        }
        if (results[i] == 1) {
            points[competitions[i][0]] = (points[competitions[i][0]] || 0) + 3;
        }
    }
    let maxPoints = 0;
    let winner = "";
    for (let key in points) {
        if (points[key] >= maxPoints) {
            maxPoints= points[key];
            winner= key;
        }
    }
    return winner;
}
let competitions= [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
]
let results = [0, 0, 1];
// console.log(tournamentWinner(competitions, results));

function nonConstructibleChange(coins) {
    let change = 0;
    let max = false;
    coins.sort((a, b) => a-b);
    if (coins[0] !== 1) {
        return 1;
    }
    for (let i = 0; i < coins.length; i++) {
        if ((change + 1) < coins[i]) {
            max = true;
            return change+= 1;
        }
        change+= coins[i];
    }
    if (!max) {
        return change + 1;
    }
    return change;
}

let coins = [5, 7, 1, 1, 2, 3, 22];
// let coins = [1, 1, 1, 1, 1];
// console.log(nonConstructibleChange(coins));

function findClosestValueInBst(tree, target) {
    let current = tree;
    let closest = tree.value;
    while (current) {
        if (Math.abs(target - closest) > Math.abs(target - current.value)) {
            closest= current.value;
        }
        if (target > current.value) {
            current = current.right;
    }
        else if (target < current.value) {
            current = current.left;
        }
        else {
            break;
        }
    }
    return closest;
}

  // This is the class of the input tree. Do not edit.
class BST {
    constructor(value) {
        this.value = value;
        this.left = null;
        this.right = null;
    }
}
