import java.util.ArrayList;
import java.util.Scanner;
import java.util.Stack;

public class Baekjoon_4949_균형잡힌세상 {
    	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Stack<Character> stack1 = new Stack<>();
		ArrayList<String> result = new ArrayList<>();
		
		while(true) {
			String str = sc.nextLine();
			if (str.equals(".")) break;
			
			boolean isError = false;
			for(int i = 0; i<str.length();i++) {
				char now = str.charAt(i); 
				if (now == '(') { stack1.push('(');}
				else if (now == ')') { 
					if (stack1.isEmpty()) { isError = true; break;}
					if (stack1.peek() == '(') { stack1.pop(); continue; }
					else { isError = true; break; }
				}
				else if (now == '[') { stack1.push('[');}
				else if (now == ']') { 
					if (stack1.isEmpty()) { isError = true; break;}
					if (stack1.peek() == '[') { stack1.pop(); continue; }
					else { isError = true; break; }
				}
				else {continue;}
			}
			
			if (!isError && stack1.isEmpty()) { result.add("yes");}
			else {result.add("no");}
			
			stack1.clear();
			
		}
		
		for(int i = 0; i < result.size(); i++) {
			System.out.println(result.get(i));
		}
	}
}
