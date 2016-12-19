package javacodingexample;

import java.util.Scanner;

public class Factorial2 {
	static int fact(int n){ //This is a static metod.
		if(n==1){
			return 1 ;
		}
		else {
			return n* fact(n-1);
		}
	}

	public static void main(String[] args) {
		int num ;
		String val ;
		Scanner sc = new Scanner(System.in); //got the value from the system.
		System.out.println("Please, enter a number : ");
		val = sc.next() ;
		num = Integer.parseInt(val) ; // val become parse and change integer.
		int result = fact(num);
		System.out.println("Factorial of " + num + " is " + result); 
	
	} // we used recursion in this example

}
