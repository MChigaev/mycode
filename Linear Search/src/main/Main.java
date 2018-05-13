package main;

import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
		Person[] people = new Person[10]; // Person array
		String[] firstnames = { "Boris", "Yekanturinburg", "Tommy", "Bobby", "Yaroslav", "Yulelog", "Chochon","Person1", "PersonNine", "PersonTen" }; // firstnames
		String[] lastnames = { "Personlastname", "Patan", "Patan", "Putin", "Python", "Java", "C", "Cplusplus", "Nine","Ten" }; //lastnames
		String[] telephones = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "10"};
		for(int i = 0; i <= 9; i++) { // Initializes people
			people[i] = new Person(firstnames[i], lastnames[i], telephones[i]);
		}
		for(int i = 0; i <= 9; i++) { // Prints out unsorted names
			System.out.println(people[i].getFirstname() + " " + people[i].getLastname() + " " + people[i].getTelephone());
		}
		System.out.printf("\n");
		Scanner in = new Scanner(System.in); // Gets user input
		String select = "";
		while(!(select.equalsIgnoreCase("Firstname") || select.equalsIgnoreCase("Lastname") || select.equalsIgnoreCase("Telephone"))) { // Makes sure non-existant input is not entered
			System.out.println("Please input by what method to search for: Firstname, Lastname, or Telephone");
			select = in.nextLine().toLowerCase();
		}
		if(select.equalsIgnoreCase("Firstname")) { //The next 3 compare their respectives strings to the key
			System.out.println("Please input firstname to search for: ");
			String firstname = in.nextLine();
			in.close();
			for(int x = 0; x < people.length; x++) {
				if(people[x].getFirstname().toLowerCase().equals(firstname.toLowerCase())) {
					System.out.println("Position: " + x + ", " + "Firstname: " + people[x].getFirstname() + ", " + "Lastname: " + people[x].getLastname() + ", " + "Telephone: " + people[x].getTelephone());
					System.exit(0);
				}
			}
			System.out.println("Person not found");
		}
		else if(select.equalsIgnoreCase("Lastname")) {
			System.out.println("Please input lastname to search for: ");
			String lastname = in.nextLine();
			in.close();
			for(int x = 0; x < people.length; x++) {
				if(people[x].getLastname().toLowerCase().equals(lastname.toLowerCase())) {
					System.out.println("Position: " + x + ", " + "Firstname: " + people[x].getFirstname() + ", " + "Lastname: " + people[x].getLastname() + ", " + "Telephone: " + people[x].getTelephone());
					System.exit(0);
				}
			}
			System.out.println("Person not found");
		}
		else {
			System.out.println("Please input telephone to search for: ");
			String telephone = in.nextLine();
			in.close();
			for(int x = 0; x < people.length; x++) {
				if(people[x].getTelephone().equals(telephone)) {
					System.out.println("Position: " + x + ", " + "Firstname: " + people[x].getFirstname() + ", " + "Lastname: " + people[x].getLastname() + ", " + "Telephone: " + people[x].getTelephone());
					System.exit(0);
				}
			}
			System.out.println("Person not found"); //If person is not found, prints person is not found
		}
	}
}
