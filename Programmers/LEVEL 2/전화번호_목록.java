public class 전화번호_목록 {
    public boolean solution(String[] phone_book) {

        for(int i = 0 ; i < phone_book.length; i++){
            for(int j = 0; j< phone_book.length ; j++){
                if(j == i)
                    continue;
                if(phone_book[i].indexOf(phone_book[j]) == 0)
                    return false;
            }
        }
        return true;
    }
}
