package javacodingexample;
import java.util.Scanner;


public class Armstrong {

	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		System.out.println("Please enter the number :");
		String val=sc.next();
		int num=Integer.parseInt(val);
		
		
		//int num = 371 ;
		int n=num;
		int check=0,rem;
		while(num>0){
			rem=num%10;
			check=check+(int)Math.pow(rem,3);
			num=num/10;
		}
		if(check==n){
			System.out.println(n+ " is an Armstrong number.");
		}
		else{
			System.out.println(n+ " is NOT an Armstrong number.");
		}
				
	}

}
