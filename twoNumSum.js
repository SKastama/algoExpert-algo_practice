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

function sortedSquaredArray(array) {
    let output= [];
    for (let i = 0; i < array.length; i++) {
        output.push(array[i]**2);
    }
    let position= 0;
    for (let j = 1; j < output.length; j++) {
        if (output[j - 1] > output[j]) {
            position= output[j];
            output[j] = output[j-1];
            output[j-1]= position;
        }
    }
    return output;
}
console.log(sortedSquaredArray([-3, -2, -1]));
