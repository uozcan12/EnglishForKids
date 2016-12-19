package javacodingexample;

import java.util.Scanner;

public class DetermineLeapYear {

	public static void main(String[] args) {
		
	// year we want to check
		Scanner sc= new Scanner(System.in);
		System.out.println("Please, enter the year: ");
		String val=sc.next();
		int year=Integer.parseInt(val);
		

		//int year=2004;
		
		// if year is divisible by 4, it is a leap year.
		if(year % 400==0 || (year % 4==0 && year % 100!=0)){
			System.out.println("Year " + year + " is a leap year."); 
		}
		else {
			System.out.println("Year " + year + " is NOT a leap year.");
		}

	}

}
