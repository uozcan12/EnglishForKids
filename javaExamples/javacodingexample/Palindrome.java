package javacodingexample;

import java.util.Scanner;

public class Palindrome { //right to left anf left to right is same
						  // 101,1331,636,..
	
	public static void main(String[] args) {
	
		int num,rev=0,r=0 ;
		Scanner sc=new Scanner(System.in);
		System.out.println("Please, enter a number :");
		String val=sc.next();
		num=Integer.parseInt(val);
		int n=num ;
		while (num!=0){
			r= num % 10 ;
			rev=rev*10+r ;
			num=num/10;
		}
		if(n==rev){
			System.out.println("Number is Palindrome.");
		}else{
			System.out.println("Number is not Palindrome.");
		}

	}

}
