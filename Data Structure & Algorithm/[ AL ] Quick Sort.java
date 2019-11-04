class QuickSort{
    public static void main(String[] args){
        int[] arr = {3,2,1,4,5,8,6,0};
        QuickSort.sort(arr);
        System.out.println(arr);
    }


    QuickSort(){}
    static void sort(int[] arr, int start, int end){
        if (end - start == 0 || end - start == 1){
            return
        }
        int pivot = start;
        int l_idx = start +1;
        int r_idx = end-1;

        while(true){
            if(!lFlag){
                if( l_idx <= end-1 && arr[pivot] > arr[l_idx])
                    l_idx ++;
                else:
                    lFlag = true;
            }
            if(!rFlag){
                if( r_idx > start && arr[pivot] < arr[r_idx])
                    r_idx ++;
                else:
                    rFlag = true;
            }
            if( lFlag && rFlag){
                if(l_idx < r_idx){
                    int temp = arr[l_idx];
                    arr[l_idx] = arr[r_idx];
                    arr[r_idx] = temp;
                    lFlag = false;
                    rFlag = false;
                }else{
                    int temp = arr[pivot];
                    arr[pivot] = arr[r_idx];
                    arr[r_idx] = temp;
                    break;
                }
            }
        }
        sort(start, r);
        sort(r+1, end);
    }

}