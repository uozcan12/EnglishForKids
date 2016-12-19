package javacodingexample;

import java.util.Scanner;
import java.lang.*;

public class Prime {

	public static void main(String[] args) {
	
		Scanner sc=new Scanner(System.in);
		System.out.println("Please, enter a starting number :");
		String val=sc.next();
		int x = Integer.parseInt(val);
		System.out.println("Please, enter a last number :");
		val=sc.next();
		int y=Integer.parseInt(val);
		System.out.println("Printing the prime number from : " + x +" to " + y);
		for(int i=x; i<=y; i++){
			if(isPrime(i)){
				System.out.println(i);
			}
		}

	}

	public static boolean isPrime(int i) {
	for(int j=2;j<i;j++){
		if(i % j == 0){
			return false ;
		}
		else {	
			return true; 
		}
	}

	}
	}
	


