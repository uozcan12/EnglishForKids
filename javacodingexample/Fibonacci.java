package javacodingexample;

import java.util.Scanner;

public class Fibonacci {


	public static void main(String[] args) {
		Scanner sc= new Scanner(System.in) ;
		int prev,next,sum,n;
		System.out.println("Enter the number :");
		String val = sc.next();
		n=Integer.parseInt(val);
		prev=next=1;
		for(int i=1;i<=n;i++){
			System.out.println(prev);
			sum=prev+next;
			prev=next;
			next=sum;
		}
	}

}
