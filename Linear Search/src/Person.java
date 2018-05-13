

public class Person {
	private String firstname;
	private String lastname;
	private String telephone;
	public Person(String firstname, String lastname, String telephone) {
		this.firstname = firstname;
		this.lastname = lastname;
		this.telephone = telephone;
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
	public String getTelephone() {
		return telephone;
	}
	public void setTelephone(String telephone) {
		this.telephone = telephone;
	}
	public String toString() {
		return "Firstname=" + firstname + ", \nlastname=" + lastname + ", \ntelephone=" + telephone;
	}
}
