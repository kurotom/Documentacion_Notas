package pro;

import javax.swing.JOptionPane;

public class Vista {
	
	static Controller controller;

	public Vista(Controller con) {
		controller = con;
	}
	
	public void setMensaje(String str) {
		controller.setFrase(str);
	}
	public String getMensaje() {
		return controller.getFrase();
	}
	
	public void mostrarMensaje(String msg) {
		JOptionPane.showMessageDialog(null, msg);
	}
	
	
	public static void main(String[] args) {
		Controller con = new Controller();
		Vista vista = new Vista(con);
		

		vista.setMensaje("Mensaje 1");
		vista.mostrarMensaje(vista.getMensaje());
		
		
		vista.setMensaje("Mensaje 2");
		vista.mostrarMensaje(vista.getMensaje());
	}
}
