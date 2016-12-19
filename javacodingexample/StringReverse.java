package javacodingexample;

import java.util.Scanner;

public class StringReverse {
	
	public static void main(String args[]) {
	
		
		Scanner s= new Scanner(System.in);
		System.out.println("Lütfen kelimeyi giriniz :");
		String string =s.next(); 
		
		//String string = "abcdef" ;
		String reverse = new StringBuffer(string).reverse().toString() ;
		System.out.println("\n String before reverse " + string ) ;
		System.out.println("\n String after reverse " + reverse) ;	
	}

}
