package pro;

public class Controller {

	Modelo modelo;
	Vista vista;
	
	public Controller() {
		modelo = new Modelo(this);
		vista = new Vista(this);
	}
	
	public void setFrase(String str) {
		modelo.setFrase(str);
	}
	
	public String getFrase() {
		return modelo.getFrase();
	}

}
