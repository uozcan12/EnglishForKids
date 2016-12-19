package javacodingexample;

import java.util.Scanner;

public class Sum {

	public static void main(String[] args) {
	int num,sum=0,r=0;
	Scanner sc=new Scanner(System.in);
	System.out.println("Please, enter the number :");
	String val=sc.next();
	num=Integer.parseInt(val);
	while(num!=0){
		r=num%10;
		num=num/10;
		sum=sum+r;
	}
	System.out.println("Sum of the digits :" + sum);

	
	}

}
