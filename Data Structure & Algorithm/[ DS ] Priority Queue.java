public class Main {
	public static int n = 100;
    public static int[] src={9,8,1,2,5,4,7,6,3};

    public static void main(String[] args) {
    	Heap heap = new Heap();
        for (int i=0;i<src.length;i++)
			heap.push(src[i]);

        for (int i=0;i<src.length;i++) {
			System.out.print(heap.pop()+" ");
		}
    }

    public static class Heap {
    	int[] heap = new int[n];
    	int hCnt=0;

    	public Heap() {}

    	public void push (int x) {
    		heap[++hCnt]=x;
    		int idx = hCnt;
    		while (idx>1 && heap[idx/2]>heap[idx]) {
    			if (idx==1 || heap[idx/2]<heap[idx])
    				break;
    			int tmp = heap[idx/2];
    			heap[idx/2]=heap[idx];
    			heap[idx]=tmp;
    			idx/=2;
    		}
    	}

    	public int pop() {
    		int pop = heap[1];
    		heap[1] = heap[hCnt--];
    		int idx =1;
    		int next;
    		while (true) {
    			next = idx*2;
    			if (next<hCnt && heap[next]>heap[next+1])
    				next++;
    			if (next>hCnt || heap[next]>heap[idx])
    				break;
    			int tmp = heap[idx];
    			heap[idx]=heap[next];
    			heap[next]=tmp;
    			idx=next;
    		}
    		return pop;
    	}
    }
}