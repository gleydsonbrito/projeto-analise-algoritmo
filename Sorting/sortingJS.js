const arrayTest = [46, 68, 3, 40, 59, 20, 88, 12, 6, 86, 57, 47, 71, 92, 81, 95, 11, 4, 52, 35, 51]

const insertionSort = (A) => {
    for (let i = 1; i < A.length; i++) {
        const current = A[i]
        let j = i - 1
        while (j >= 0 && A[j] > current) {
            A[j + 1] = A[j]
            j--
        }
        A[j + 1] = current
    }
    return A
}
console.log(JSON.stringify(arrayTest))

// console.log(insertionSort(arrayTest))

const merge = (A, start, midle, end) => {
    let left = A.slice(start, midle)
    let right = A.slice(midle + 1, end)

    let left_top = 0
    let right_top = 0

    for (k = 0; k < A.length; k++) { 
        if (left_top >= left.length) {
            A[k] = right[right_top]
            right_top++
        } else if (right_top >= right.length) {
            A[k] = left[left_top]
            left_top++
        } else if (left[left_top] < right[right_top]) {
            A[k] = left[left_top]
            left_top++
        } else {
            A[k] = right[right_top]
            right_top++
        }
    }
}

const mergeSort = (A, start = 0, end = null) => {
    if (end == null){
        end = A.length - 1
    } 

    if ((end - start) >= 1) {
        let midle = Math.floor((start + end) / 2)
        mergeSort(A, start, midle)
        mergeSort(A, midle + 1, end)
        merge(A, start, midle, end)
    }
}

//mergeSort(arrayTest)

//console.log(JSON.stringify(arrayTest))

function selectionsort(A){
    let ret = [...A]
    for(let i = 0; i < ret.length; i++){
        minIndex = i
        for(let j = i + 1; j < ret.length; j++){
            if(ret[j] > ret[minIndex]){
                minIndex = j
            }
        }
        if(ret[i] > ret[minIndex]){
            let aux = ret[minIndex]
            ret[minIndex] = ret[i]
            ret[i] = aux
        } 
    }
    return ret
}

console.log(JSON.stringify(selectionsort(arrayTest)));
