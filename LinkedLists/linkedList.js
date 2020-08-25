class Node {
    constructor(data) {
        this.data = data
        this.next = null
    }
}

class LinkedList {
    constructor() {
        this.head = null
    }

    add(data) {
        const nNode = new Node(data)

        if (this.head == null) {
            this.head = nNode;
        } else {
            let current = this.head;

            while (current.next != null) {
                current = current.next;
            }
            current.next = nNode;
        }
    }

    get(key) {
        let position = 0;

        if (this.head.data == key) {
            return position;
        } else {
            let current = this.head

            while (current != null) {
                position++;

                if (current.data === key) {
                    return position;
                }
                current = current.next;
            }
            return -1;
        }
    }

    delete(key) {
        if (this.head.data === key) {
            this.head = this.head.next
            return key;
        } else {
            let current = this.head;

            while (current != null) {
                if (current.next != null && current.next.data === key) {
                    current.next = current.next.next;
                    return key;
                } else {
                    current = current.next
                }
            }
            return -1;
        }
    }

    length() {
        if (this.head == null) return null;

        let current = this.head;
        let qt = 1;

        while (current.next != null) {
            qt++
            current = current.next;
        }
        return qt;
    }
}

let list = new LinkedList();

console.log("Instanciando a lista: ", JSON.stringify(list));

console.log(list.length());


list.add("Estudo de PAA");

list.add("Info Aplicada");
list.add("x");


console.log(list.length());
console.log(JSON.stringify(list))
console.log(JSON.stringify(list.delete("x")))
console.log(JSON.stringify(list))

console.log(list.length());



