package com.battleships.app.netApp;

import java.io.IOException;
import java.io.InputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.InetSocketAddress;
import java.nio.channels.SocketChannel;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

import com.battleships.app.controller.ClientBattleController;

/**
*
* @author kurotom
* https://github.com/kurotom
* 
*/


public class ClientBattleShips {
	
	public Boolean conectado = false;
	
	InetSocketAddress serverAddress;
	SocketChannel socketChannel;
	
	private ExecutorService hilos;
	
	ObjectInputStream inObjectList;
	ObjectOutputStream outObjectList;
	InputStream inReadMesage;
	
	ClientBattleController clientController;


	
	public ClientBattleShips(ClientBattleController controller) {
		hilos = Executors.newFixedThreadPool(4);
		clientController = controller;
	}
	
	
	public void close() {
		try {
			if (outObjectList != null && inObjectList != null) {
				System.out.println("Client - Forcing shutdown...");
				
				outObjectList.close();
				System.out.println("Cerrado -- outObjectList");
				
				inObjectList.close();
				System.out.println("Cerrado -- inObjectList");
				
				socketChannel.close();
				System.out.println("Cerrado -- socketChannel");
				
				serverAddress = null;
				System.out.println("Cerrado -- serverAddress");
				
				hilos.shutdownNow();
				System.out.println("Cerrado -- hilos");
			}
		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
		}
	}
	
	
	public void network(String ipServerAddress) {
		try {
			serverAddress = new InetSocketAddress(ipServerAddress, 8210);
			socketChannel = SocketChannel.open(serverAddress);
			
			inObjectList = new ObjectInputStream(socketChannel.socket().getInputStream());
			outObjectList = new ObjectOutputStream(socketChannel.socket().getOutputStream());
			
			hilos.submit(new ClienteRead(socketChannel, inObjectList));
//			hilos.submit(new ClienteWriter(socketChannel, outObjectList));
			
			conectado = true;
			System.out.println("servidor conectado");
		} catch (IOException e) {
			e.printStackTrace();
		}
	}
	
	
	public void sendCoords(List<Integer> lista) {
		try {
			outObjectList.writeObject(lista);
			outObjectList.flush();
		} catch (Exception e) {
			e.printStackTrace();
		}
	}
	
	public boolean getConectado() {
		return this.conectado;
	}
	
	
	public class ClienteRead implements Runnable  {
		SocketChannel socket;
		ObjectInputStream in;
		
		public ClienteRead(SocketChannel socketRead, ObjectInputStream entrada) {
			socket = socketRead;
			in = entrada;
		}
		
		public void close() {
			try {
				in.close();
				socket.close();
			} catch (Exception e) {
				// TODO: handle exception
			}
		}

		@Override
		public void run() {			
			try {
				List<Integer> lista = null;
				
				while ((lista = (List<Integer>) in.readObject()) != null) {
//					System.out.println("SERVER coords attack ===>  " + lista);
					if (lista.size() == 2) {
						clientController.coordsAtackOponent(lista);
					} else if (lista.size() == 4) {
						boolean confirm = lista.stream().allMatch(item -> item == 0);
						if (confirm) {
							clientController.statusAttack("Hit!!!");
							clientController.drawOponentMap("X");
						} else {
							clientController.statusAttack("Miss");
							clientController.drawOponentMap("0");
						}
					} else if (lista.size() == 1) {
// TODO  - recibe código de victoria - no tiene vidas el enemigo
						clientController.victoryMessage();
					}
					
				}
			} catch (Exception e) {
				e.printStackTrace();
			}
		}
	}

	
	
	
//	public class ClienteWriter implements Runnable {
//		
//		public PrintWriter writerCL;
//		public SocketChannel socketCL;
//		
//		ObjectOutputStream out;
//		
//		
//		public ClienteWriter(SocketChannel soc, ObjectOutputStream objectOut) {
//			socketCL = soc;
//			out = objectOut;
//		}
//		
//		public ClienteWriter(SocketChannel soc, PrintWriter writerClient) {
//			socketCL = soc;
//			writerCL = writerClient;
//		}
//		
//		public ClienteWriter(SocketChannel soc) {
//			socketCL = soc;
//			writerCL = new PrintWriter(Channels.newWriter(soc, StandardCharsets.UTF_8));
//		}
//		
//		
//		@Override
//		public void run() {
//			System.out.println("Preparado escribir Cliente");
//			try {
//				
//				List<String> lista = new ArrayList<>();
//				
//				lista.add("cliente");
//				lista.add("mensaje");
//				lista.add("1");
//				
//				out.writeObject(lista);
//				
//				hilos.shutdown();
//			} catch (Exception e) {
//				e.printStackTrace();
//			}
//		}
//	}
	
}
