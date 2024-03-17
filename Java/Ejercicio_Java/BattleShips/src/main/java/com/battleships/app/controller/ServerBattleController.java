/*
 * The MIT License
 *
 * Copyright 2023 tomas.
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
 */
package com.battleships.app.controller;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.Font;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JTable;

import com.battleships.app.gui.StartJFrame;
import com.battleships.app.netApp.ServerBattleShips;

/**
*
* @author kurotom
* https://github.com/kurotom
* 
*/

public class ServerBattleController extends AbstractController {
	
	private String playerName;
	private Integer playerLife = 0;
	
	private ExecutorService hilo = null;
	
	private List<List<List>> listaCoordenadas = new ArrayList<>();

	private ServerBattleShips server;
	
	private JTable tablaPlayer = null;
	
	private List<Integer> coordsOponent = null;

	private JLabel labelPlayerLife, playerStatusLabel, attackStatusLabel;
	private JTable tablaOponent;
	private JButton attackButton, btnSurrender;
	private JFrame frame;
	private JLabel labelOptionPane = new JLabel("");
	private String ipAddress;
	
	
	public ServerBattleController() {
		hilo = Executors.newSingleThreadExecutor();
		labelOptionPane.setFont(new Font("Arial", Font.BOLD, 20));
	}
	
	public void runServer(ServerBattleController controller) {
		server = new ServerBattleShips(controller);
		hilo.submit(() -> server.runServer(ipAddress));
	}
	
	public void closeHilo() {
		if (!hilo.isShutdown()) {
			hilo.shutdown();
			hilo = null;
		}
	}
	
// TODO	
/////////////////////////////////////////////////////////////////////
	@Override
	public void setFrame(JFrame thisFrame) {
		frame = thisFrame;
	}
	
	@Override
	public Integer amountLive() {
		int i = 0;
		for (int x = 0; x < listaCoordenadas.size(); x++) {
			i += listaCoordenadas.get(x).size();
		};
		playerLife = i;
		return i;
	}
	
	@Override
	public boolean hitShip(List<Integer> coords) {
		boolean contiene = listaCoordenadas.stream().anyMatch(item -> item.contains(coords));
		return contiene;
	}
	
	@Override
	public void setSurrenderButton(JButton btn) {
		btnSurrender = btn;
	}
	@Override
	public void setAttackButton(JButton btn) {
		attackButton = btn; 
	}
	
	@Override
	public void setStatusAttackLabel(JLabel label) {
		attackStatusLabel = label;
	}
	
	@Override
	public void setStatusPlayerLabel(JLabel label) {
		playerStatusLabel = label;
	}
	
	@Override
	public void setTableMapOponent(JTable tabla) {
		tablaOponent = tabla;
	}
	
	@Override
	public void setTableMapPlayer(JTable tabla) {
		tablaPlayer = tabla;
	}
	
	@Override
	public void setPlayeLifeLabel(JLabel label) {
		labelPlayerLife = label;
	}
	
	@Override
	public Integer getPlayerLife() {
		return playerLife;
	}
	
	@Override
	public void statusAttack(String str) {
		if (str.equals("Hit!!!")) {
			attackStatusLabel.setText(str);
			attackStatusLabel.setForeground(new Color(0, 222, 42));
		} else if (str.equals("Miss")) {
			attackStatusLabel.setText(str);
			attackStatusLabel.setForeground(Color.BLACK);			
		}
	}
	
	@Override
	public void coordsAtackOponent(List<Integer> coords) {
		coordsOponent = coords;
		List<Integer> listaResponse = new ArrayList<>();
		attackButton.setEnabled(true);
		
		if (hitShip(coords)) {
//			System.out.println("LE ACHUNTÓ = " + coords);
			tablaPlayer.setValueAt("X", coords.get(1), coords.get(0));
			playerLife--;
			labelPlayerLife.setText(String.valueOf(playerLife));
			listaResponse.add(0);
			listaResponse.add(0);
			listaResponse.add(0);
			listaResponse.add(0);
			server.sendCoords(listaResponse);
			playerStatusLabel.setText("Damaged!");
			playerStatusLabel.setForeground(Color.RED);
			if (playerLife == 0) {
				labelPlayerLife.setFont(new Font("Arial", Font.BOLD, 18));
				labelPlayerLife.setForeground(Color.RED);
				attackButton.setEnabled(false);
				sendSurrender();
				defeatMessage();
			}
		} else {
//			System.out.println("NO LE ACHUNTÓ");
			tablaPlayer.setValueAt("0", coords.get(1), coords.get(0));
			listaResponse.add(1);
			listaResponse.add(1);
			listaResponse.add(1);
			listaResponse.add(1);
			server.sendCoords(listaResponse);
			playerStatusLabel.setText("Safe");
			playerStatusLabel.setForeground(Color.BLUE);
		}
	}
	
	@Override
	public void drawOponentMap(String str) {
		tablaOponent.setValueAt(str, coordsOponent.get(1), coordsOponent.get(0));
	}
	
	@Override
	public void sendSurrender() {
		btnSurrender.setEnabled(false);
		attackButton.setEnabled(false);
		List<Integer> lista = new ArrayList<>();
		lista.add(1);
		server.sendCoords(lista);
	}
	
	@Override
	public void victoryMessage() {
		attackButton.setEnabled(false);
		btnSurrender.setEnabled(false);
		labelOptionPane.setText("You Win");
		JOptionPane.showMessageDialog(frame, labelOptionPane, "Win", JOptionPane.NO_OPTION);
		Integer opt = dialogContinue();
		if (opt == 0) {
			frame.setVisible(false);
			closeHilo();
			server.close();
			
	    	StartJFrame start = new StartJFrame();
	    	start.setVisible(true);
		}
//		return opt;
	}
	
	
	public void defeatMessage() {
		String[] confirmar = new String[] {"Accept"};
		labelOptionPane.setText("You Lost");
		labelOptionPane.setFont(new java.awt.Font("Courier 10 Pitch", Font.PLAIN, 22));
		Integer opcionEntregada = JOptionPane.showOptionDialog(
							frame,
							labelOptionPane,
							"Lost",
							JOptionPane.DEFAULT_OPTION,
							JOptionPane.INFORMATION_MESSAGE,
							null,
							confirmar,
							confirmar[0]
						);
		if (opcionEntregada == 0) {
			Integer opt = dialogContinue();
			frame.setVisible(false);
			if (opt == 0) {
				closeHilo();
				server.close();
				
		    	StartJFrame start = new StartJFrame();
		    	start.setVisible(true);
			}
		}

	}
	
	public Integer dialogContinue() {
		String[] options = new String[] {"Yes", "No"};
		Integer optionNewGame = JOptionPane.showOptionDialog(
					frame,
					"Try again?",
					"Continue?",
					JOptionPane.DEFAULT_OPTION,
					JOptionPane.INFORMATION_MESSAGE,
					null,
					options,
					options[0]
				);
		return optionNewGame;
	}
	
//////////////////////////////////////////
	
//TODO
	
	@Override
	public void setIp(String str) {
		ipAddress = str;
	}
	
	@Override
	public void sendCoords(List<Integer> lista) {
		server.sendCoords(lista);
		coordsOponent = lista;
		attackButton.setEnabled(false);
	}
	
	@Override
	public void close() {
		server.close();
	}
	
	@Override
	public boolean isConnected() {
		return server.getConectado();
	}
	
	@Override
	public void setName(String name) {
		playerName = name;
	}

	@Override
	public String getName() {
		return playerName;
	}
	
	@Override
	public void setCoords(List<List<List>> lista) {
		listaCoordenadas = lista;
	}

	@Override
	public List<List<List>> getCoords() {
		return listaCoordenadas;
	}
	
    
}
