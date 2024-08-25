import java.util.*;

public class Baekjoon_5525_IOIOI {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        Deque<Character> deque = new LinkedList<>();
        int count = 0;
        int deque_size = 0;

        int n = sc.nextInt();
        sc.nextLine();

        int length = sc.nextInt();
        sc.nextLine();

        String str = sc.nextLine();
        char c = 'i';
        for(int i = 0; i < length; i++){
            if(deque_size == 0) {
                if(str.charAt(i) == 'I') {deque.add('I'); deque_size++;}
                continue;
            }
            
            c = deque.peekLast();
            if(c != str.charAt(i)){deque.add(str.charAt(i)); deque_size++;}
            else {
                deque.clear();
                deque_size = 0;
                if(c == 'I') {deque.add('I');deque_size++;}
            }

            if(deque_size == 2*n+1){
                deque.pollFirst();
                deque.pollFirst();
                deque_size -= 2;    
                count += 1;
            }
        }

        System.out.println(count);

        sc.close();
    }
}
