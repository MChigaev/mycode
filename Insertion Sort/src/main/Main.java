package main;

import java.util.Random;

public class Main {
	public static void main(String[] args) {
		int[] tempNumLastName = null; //Used for person initialization
		Random ran = new Random(); //Used for generating random numbers
		Person[] people = new Person[10]; //Person array
		String[] firstnames = {"Boris", "Yekanturinburg", "Tommy", "Bobby", "Yaroslav", "Yulelog", "Chochon", "Person1", "PersonNine", "PersonTen"}; //firstnames
		String[] lastnames = {"Personlastname", "Patan", "Patan", "Putin", "Python", "Java", "C", "Cplusplus", "Nine", "Ten"}; //lastnames
		for(int i = 0; i <= 9; i++) { //Initializes people
			people[i] = new Person(firstnames[i], lastnames[i], ran.nextInt(1000000), tempNumLastName);
		}
		for(int i = 0; i <= 9; i++) { //Prints out unsorted names
			System.out.println(people[i].getFirstname() + " " + people[i].getLastname() + " " + people[i].getTelephone());
		}
		System.out.printf("\n");
		for(int x = 0; x <= 9; x++) { //Sets the number last name(used for sorting)
			people[x].setNumberLastName(numberLastName(people[x].getLastname()));
		}
		for(int x = 0; x <= 8; x++) { //Goes through array
			int temp = x; //Used to reset x after moving value
			while(swap(people[x].getNumberLastName(), people[x + 1].getNumberLastName())) { //Checks if sort possible, if possible, moves value down, repeats
				Person tempPerson = people[x]; //Swap start
				people[x] = people[x + 1];
				people[x + 1] = tempPerson; //Swap end
				if(x - 1 >= 0) { //Move down by one value
					x = x - 1;
				}
			}
			x = temp;
		}	
		for(int i = 0; i <= 9; i++) { //Prints out sorted names
			System.out.println(people[i].getFirstname() + " " + people[i].getLastname() + " " + people[i].getTelephone());
		}
	}
	public static int[] numberLastName(String name) { //Changes lastnames into integer arrays
		int[] numberName = new int[name.length()]; //Number Name
		for(int c = 0; c <= name.length() - 1; c++) { //Converts letters to ascii
			numberName[c] = name.toLowerCase().charAt(c);
		}
		return numberName;
	}
	public static boolean swap(int[] name1, int[] name2) { //Checks if swapping is required
		try { //Try and catch statement used to keep name1 OR name2 from throwing exception(simpler than checking both arrays)
			for(int x = 0; x <= 199; x++) {
				if(name1[x] > name2[x]) { //If element on the left is greater switch
					return true;
				}
				if(name1[x] < name2[x]) { //Otherwise do not switch
					return false;
				}
			}
		}
		catch(IndexOutOfBoundsException e) {
			
		}
		return false; //If all the letters are the same, do not switch(no reason to)
	}
}
