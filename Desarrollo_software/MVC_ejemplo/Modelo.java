package pro;

public class Modelo {
	
	String frase = null;
	Controller controller;
	
	public Modelo(Controller con) {
		controller = con;
	}
	
	public void setFrase(String str) {
		frase = str;
	}
	
	public String getFrase() {
		return frase;
	}

}
