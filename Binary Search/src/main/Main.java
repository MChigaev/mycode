package main;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		String[] names = {"Boris", "Yekanturinburg", "Tommy", "Bobby", "Yaroslav", "Yulelog", "Chochon","Person1", "PersonNine", "PersonTen" }; // names
		ArrayList<String> i = new ArrayList<String>(); // Makes list
		for(String s : names) {
			i.add(s); // Adds names to list
		}
		System.out.println(i.toString()); // Prints unsorted list
		Collections.sort(i); // Sorts the string
		System.out.println(i.toString()); // Prints sorted list
		Scanner in = new Scanner(System.in);
		System.out.println("Input name to search for: ");
		String key = in.nextLine(); // Gets key to search for
		in.close();
		int lower = 0;
		int higher = i.size() - 1;
		int mid = (lower + higher)/2;
		boolean exists = true;
		while(!(i.get(mid).compareTo(key) == 0 || exists != true)) { // Runs until key is found or it is found that it does not exist
			if(i.get(mid).compareTo(key) < 0) { // Key is less than the middle
				lower = mid;
				mid = (lower + higher)/2;
			}
			else { // Key is greater than the middle
				higher = mid;
				mid = (lower + higher)/2;
			}
			if(Math.abs(lower - higher) == 1 && i.get(lower).compareTo(key) != 0 && i.get(higher).compareTo(key) != 0) { // If there's two elements left, and both do not equal the key, the key does not exist
				exists = false;
			}
			else if(Math.abs(lower - higher) == 1) { //If there's 2 elements left, but one is equal to the key, this finds the key (prevents infinite looping)
				if(i.get(lower).compareTo(key) == 0) {
					mid = lower;
				}
				else {
					mid = higher;
				}
			}
		}
		if(exists == false) { // Prints out not found if not found
			System.out.println("Not in the list");
		}
		else { // Prints out data if found
			System.out.println("Position: " + mid + ", " + "Firstname: " + i.get(mid));
		}
	}
}