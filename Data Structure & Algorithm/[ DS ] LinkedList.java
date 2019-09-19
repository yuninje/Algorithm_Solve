package LinkedList;

public class LinkedList {
    // https://opentutorials.org/module/1335/8857#entirecode
    // 첫번째 노드를 가리키는 필드
    private Node head;
    private Node tail;
    private int size = 0;
    private class Node{
        private Object data; // 데이터 필드
        private Node next;   // 다음 노드
        public Node(Object input){
            this.data = input;
            this.next = null;
        }
        public String toString(){
            return String.valueOf(this.data);
        }
    }

    public void addFirst(Object input){
        Node newNode = new Node(input); // 노드 생성
        newNode.next = head;            // add(0,object) >> (구)첫번째 노드를 생성한 노드의 다음노드로 지정
        head = newNode;                 // head 갱신
        size ++;
        if(head.next == null){
            tail = head;
        }
    }

    public void addLast(Object input){
        Node newNode = new Node(input); // 노드 생성
        if(size == 0){
            addFirst(input);            // 리스트에 노드가 없다면 첫번째 노드 추가
            return;
        }
        tail.next = newNode;            // (구)마지막 노드의 다음 노드로 생성한 노드를 지정
        tail = newNode;                 // 마지막 노드 갱신
        size ++;                        // 엘리먼트 개수 증가
    }

    Node node(int index){               // index번째의 노드 반환
        Node x = head;
        for(int i = 0; i<index; i++)
            x = x.next;
        return x;
    }

    public void add(int k, Object input){
        if(k == 0){
            addFirst(input);
            return;
        }
        Node temp1 = node(k-1);     // 새로 추가하는 노드의 이전 노드가 될 노드
        Node temp2 = temp1.next;           // 새로 추가하는 노드의 다음 노드가 될 노드
        Node newNode = new Node(input);
        temp1.next = newNode;
        newNode.next = temp2;
        size ++;
        if(newNode.next == null)            // 마지막 노드 갱신
            tail = newNode;
    }

    public String toString(){
//        opentutorial==========================================================
        if(head == null)        // 노드가 없다면 [] 를 리턴.
            return "[]";

        Node temp = head;
        String str = "[";
        while(temp.next != null){
            str += temp.data + ", ";
            temp = temp.next;
        }
        str += temp.data;                   // 마지막 노드를 출력 결과에 추가
        return str + "]";

//        이게 더 낫지 않나..? ====================================================
//        Node temp = head;
//        String str = "[";
//        while(temp != null){
//            str += temp.data + ", ";
//            temp = temp.next;
//        }
//        return str + "]";
    }

    public Object removeFirst(){
        Node temp = head;
        head = temp.next;                   // 처음 노드 갱신

        Object returnData = temp.data;      // 데이터를 삭제하기 전에 리턴할 값을 임시변수에 담음
        temp = null;
        size --;
        return returnData;
    }

    public Object remove(int k){
        if(k == 0)
            return removeFirst();

        Node temp = node(k-1);
        Node todoDeleted = temp.next;           // 삭제할 노드
        temp.next = todoDeleted.next;           // k-1 노드 next 갱신

        Object returnData = todoDeleted.data;   // 데이터를 삭제하기 전에 리턴할 값을 임시변수에 담음

        if(todoDeleted == tail)
            tail = temp;
        todoDeleted = null;
        size --;
        return returnData;
    }

    public Object removeLast(){
        return remove(size-1);
    }

    public int size(){
        return size;
    }

    public Object get(int k){
        Node temp = node(k);
        return temp.data;
    }

    class ListIterator{
        private Node lastReturned;
        private Node next;
        private int nextIndex;

        ListIterator(){
            next = head;
            nextIndex = 0;
        }

        // 본 메소드를 호출하면 next의 참조값이 기존 next.next로 변경됩니다.
        public Object next() {
            lastReturned = next;
            next = next.next;
            nextIndex++;
            return lastReturned.data;
        }

        public boolean hasNext() {
            return nextIndex < size();
        }

        public void add(Object input){
            Node newNode = new Node(input);
            if(lastReturned == null){
                head= newNode;
                newNode.next = next;
            } else {
                lastReturned.next = newNode;
                newNode.next = next;
            }
            lastReturned = newNode;
            nextIndex++;
            size++;
        }

        public void remove(){
            if(nextIndex == 0){
                throw new IllegalStateException();
            }
            LinkedList.this.remove(nextIndex-1);
            nextIndex--;
        }

    }
}
