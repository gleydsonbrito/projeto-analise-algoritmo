let set = [];

 function randonArray(){
     for(let i=0; i < 41; i++){
         set.push(Math.floor(Math.random() * 101))
     }
 }

randonArray()

const bubbleSort = vector => {
    if(vector.length === 0) return "Empty List"

    const n = vector.length;
    for(let j=0; j < n; j++){
        for(let i=0; i < n; i++){
            if(vector[i] > vector[i + 1]){
                let aux = vector[i];
                vector[i] = vector[i + 1];
                vector[i + 1] = aux            }
        }
    }
    return vector;
};

console.log(JSON.stringify(set));

console.log(JSON.stringify(bubbleSort(set)))