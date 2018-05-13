package main;

import java.util.Random;

public class Main {
	public static void main(String[] args) {
		Random ran = new Random();
		int[] intarray = new int[20];
		for(int i = 0; i <= 19; i++) {
			intarray[i] = 0;
			while(intarray[i] == 0) {
				intarray[i] = ran.nextInt(100);
			}
		}
		for(int i = 0; i <=19; i++) {
			System.out.println(intarray[i]);
		}
		System.out.println("---------");
		intarray = selectionsort(0, intarray);
		for(int i = 0; i <= 19; i++) {
			System.out.println(intarray[i]);
		}
	}
	public static int[] selectionsort(int swap, int[] intarray) {
		if(swap > intarray.length - 1) {
			return intarray;
		}
		int min = 19;
		for(int i = 0 + swap; i <= 19; i++) {
			if(intarray[i] < intarray[min]) {
				min = i;
			}
		}
		int temp = intarray[swap];
		intarray[swap] = intarray[min];
		intarray[min] = temp;
		return selectionsort(swap + 1, intarray);
	}
}