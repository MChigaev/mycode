package main;

public class Person {
	private String firstname;
	private String lastname;
	private int telephone;
	private int[] numberLastName = new int[200];
	public Person(String firstname, String lastname, int telephone, int[] numberlastname) {
		this.firstname = firstname;
		this.lastname = lastname;
		this.telephone = telephone;
		this.numberLastName = numberlastname;
	}
	public String getFirstname() {
		return firstname;
	}
	public void setFirstname(String firstname) {
		this.firstname = firstname;
	}
	public String getLastname() {
		return lastname;
	}
	public void setLastname(String lastname) {
		this.lastname = lastname;
	}
	public int getTelephone() {
		return telephone;
	}
	public void setTelephone(int telephone) {
		this.telephone = telephone;
	}
	public int[] getNumberLastName() {
		return numberLastName;
	}
	public void setNumberLastName(int[] numberlastname) {
		this.numberLastName = numberlastname;
	}
	public String toString() {
		return "Firstname=" + firstname + ", \nlastname=" + lastname + ", \ntelephone=" + telephone;
	}
}
