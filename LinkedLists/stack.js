class Stack {

    constructor() {
        this.array = [];
        this.top = -1
    }

    push(data) {
        this.array.push(data);
        this.top++
    };

    pop() {
        if (this.top < 1) return -1

        return this.array[this.top];
    }

    unstack() {
        if (this.top < 0) return -1;

        this.array.splice(this.top, 1);
        return this.top--;
    }

    get(key){
        if(this.top < 0) return -1;

        while(this.array[this.top] != key){
            this.unstack()
            if(this.top < 0) return -1;
        }
        return this.array[this.top];
    }
}


let stack = new Stack();

stack.push("x");
stack.push("y");
stack.push('z');

// console.log(JSON.stringify(stack));

// console.log(JSON.stringify(stack.unstack()));

console.log(JSON.stringify(stack));

stack.get('a')
console.log(JSON.stringify(stack));

