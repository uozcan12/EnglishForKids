package javacodingexample;

import java.util.Scanner;

public class ReverseNum {

	public static void main(String[] args) {
		
		Scanner sc=new Scanner(System.in);
		System.out.println("Please,enter a number :");
		String val=sc.next();
		int num=Integer.parseInt(val);
		int rev=0;
		int r;
		while(num!=0){
			r= num % 10 ;
			rev=rev*10+r;
			num=num/10;
					
		}
		System.out.println("Reverse of given number is: " + rev);
		
	}

}
