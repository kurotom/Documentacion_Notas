package com.battleships.app.netApp;

import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.net.Inet4Address;
import java.net.InetAddress;
import java.net.InetSocketAddress;
import java.nio.channels.ServerSocketChannel;
import java.nio.channels.SocketChannel;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

import com.battleships.app.controller.ServerBattleController;

/**
*
* @author kurotom
* https://github.com/kurotom
* 
*/


/**
 * 
 * Código de envios
 * 
 * ArrayList
 * [EjeX, EjeY] = tamaño de 2
 * [0, 0, 0 ,0] = tamaño de 4 - ataque exitoso
 * [1, 1, 1 ,1] = tamaño de 4 - ataque fallido
 * [1] = tamaño 1 - surrender
 * 
 */


public class ServerBattleShips {
	
	public Boolean conectado = false;

	
	ExecutorService poolHilos;
	
	ObjectOutputStream outObjectList;
	ObjectInputStream inObjectList;
	
	ServerSocketChannel serverChannel;
	SocketChannel cliente;
	
	ServerBattleController serverController;
	
	
	public ServerBattleShips(ServerBattleController controller) {
		poolHilos = Executors.newFixedThreadPool(2);
		serverController = controller;
	}
	
	public void close() {
		try {
			if (outObjectList != null && inObjectList != null) {
				System.out.println("Server - Forcing shutdown...");

				outObjectList.close();
				System.out.println("Cerrado -- outObjectList");
				
				inObjectList.close();
				System.out.println("Cerrado -- inObjectList");
				
				cliente.close();
				System.out.println("Cerrado -- cliente");
				
				serverChannel.close();
				System.out.println("Cerrado -- serverChannel");
				
				poolHilos.shutdownNow();
				System.out.println("Cerrado -- poolHilos");
			}
		} catch (IOException e) {
			// TODO: handle exception
			e.printStackTrace();
		}
	}
	
	public void runServer(String ipServer) {
		try {
			serverChannel = ServerSocketChannel.open();
//			serverChannel.bind(new InetSocketAddress(ipServer ,5000));
			serverChannel.bind(new InetSocketAddress(InetAddress.getByName(ipServer), 8210), 100);
			System.out.println(serverChannel.getLocalAddress());
			
			
			
			while (serverChannel.isOpen()) {
				cliente = serverChannel.accept();
				
				outObjectList = new ObjectOutputStream(cliente.socket().getOutputStream());
				inObjectList = new ObjectInputStream(cliente.socket().getInputStream());
				
//				poolHilos.submit(new ClientWriter(cliente, outObjectList));
				poolHilos.submit(new ClientReader(cliente, inObjectList));
				
				conectado = true;
				System.out.println("Cliente conectado");
			}
			poolHilos.shutdown();
			
			
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
	
//	public class ClientWriter implements Runnable {
//		
//		PrintWriter writerServer;
//		SocketChannel socketCliente;
//		
//		ObjectOutputStream outObjectWriter;
//		
//		public ClientWriter(SocketChannel socket, ObjectOutputStream out) {
//			socketCliente = socket;
//			outObjectWriter = out;
//		};
//		
//		public ClientWriter(SocketChannel socket, PrintWriter writerCL) {
//			socketCliente = socket;
//			writerServer = writerCL;
////			writerServer = new PrintWriter(Channels.newWriter(socket, UTF_8));
//		}
//		
//		public void run() {
//			System.out.println("---> Enviar mensaje cliente");
//			
//			try {
//				List<String> lista = new ArrayList<>();
//				
//				lista.add("un");
//				lista.add("String");
//				lista.add("desde Server");
//				
//				System.out.println(lista.toString());
//				
//				outObjectWriter.writeObject(lista);
//				
//			} catch (Exception e) {
//				e.printStackTrace();
//			}
//			
//			
//			
//			
////			writerServer.println("init");
////			writerServer.flush();
//			
////			while (true) {
////				System.out.println(poolHilos.toString());
////				String msg = scan.nextLine();
////				writerServer.print(msg + "\n");
////				writerServer.flush();
////			}
//
//		}
//	}
//	
//	
//	
	public class ClientReader implements Runnable {
		SocketChannel socket;
		ObjectInputStream input;
		
		public ClientReader(SocketChannel cliente, ObjectInputStream inObj) {
			socket = cliente;
			input = inObj;
		}
		
		public void run() {
			try {
				List<Integer> lista = null;
				while ((lista = (List<Integer>) input.readObject()) != null) {
//					System.out.println("Cliente COords attack -->  " + lista);
					if (lista.size() == 2) {
						serverController.coordsAtackOponent(lista);
					} else if (lista.size() == 4) {
						boolean confirm = lista.stream().allMatch(item -> item == 0);
						if (confirm) {
							serverController.statusAttack("Hit!!!");
							serverController.drawOponentMap("X");
						} else {
							serverController.statusAttack("Miss");
							serverController.drawOponentMap("0");
						}
					} else if (lista.size() == 1) {
// TODO  - recibe código de victoria - no tiene vidas el enemigo						
						serverController.victoryMessage();
					}
					
				}
				poolHilos.shutdown();
			} catch (Exception e) {
				e.printStackTrace();
			}

		}		

	}
	
	

}
