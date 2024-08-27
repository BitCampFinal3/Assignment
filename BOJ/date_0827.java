package _group3_BOJ;

import java.util.Scanner;

public class date_0827 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		        Scanner sc = new Scanner(System.in);
		        
		        int D = sc.nextInt(); 
		        int N = sc.nextInt(); 
		        int V = sc.nextInt(); 
		     
		        int totalDistance = D - N;
		        int mustDistance = V - D;

		        int days = mustDistance / totalDistance;
		        if (mustDistance % totalDistance != 0) {
		            days++;
		        }
		       
		        days += 1; 

		        System.out.println(days);
		    }

}
