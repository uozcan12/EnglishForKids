package javacodingexample ;

import java.util.Scanner;

public class Factorial {

	public static void main(String[] args) {
		
		Scanner sc = new Scanner(System.in);  // got the number of the system.  
		System.out.println("Please, enter a number");
		String val = sc.next();  // val is string
		int num= Integer.parseInt(val); //val become parse and change integer.
		int fact=1 ;
		if(num==0){
			fact=1;
		}
		else {
			for(int i= num ; i>0 ; i--){
				fact=fact*i ;
				
			}
		System.out.println("Factorial of " + num + " is " + fact);
		}

	}

}
