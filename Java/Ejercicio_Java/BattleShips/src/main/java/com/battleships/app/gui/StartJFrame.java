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
package com.battleships.app.gui;

import com.battleships.app.controller.ClientBattleController;
import com.battleships.app.controller.ServerBattleController;
import com.battleships.app.netApp.ClientBattleShips;
import com.battleships.app.netApp.ServerBattleShips;

import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.GroupLayout.Alignment;
import javax.swing.JLabel;

import java.awt.Font;
import java.net.InetSocketAddress;

import javax.swing.GroupLayout;
import javax.swing.LayoutStyle.ComponentPlacement;

/**
*
* @author kurotom
* https://github.com/kurotom
* @version 1.0
* 
* 
* 
*/


/**
 *  Frame incial, este contiene campos: nombre del jugador, ip servidor, selección tamaño del mapa,
 *  selección cliente o servidor. 
 *  
 *  
 */
public class StartJFrame extends JFrame {
	
	
	private static final long serialVersionUID = 1L;
	private ServerBattleController serverBattleController;
	private ClientBattleController clientBattleController;


    /**
     * Creates new form NewJFrame
     */
    public StartJFrame() {
        System.out.println(serverBattleController);
        System.out.println(clientBattleController);
        System.out.println("-- Antes");
        
        initComponents();
        
        System.out.println(serverBattleController);
        System.out.println(clientBattleController);
        System.out.println("-- Despues");
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {
    	
    	serverBattleController = new ServerBattleController();
    	clientBattleController = new ClientBattleController();

        jLabel1 = new javax.swing.JLabel();
        jLabel2 = new javax.swing.JLabel();
        playerName = new javax.swing.JTextField();
        jPanel1 = new javax.swing.JPanel();
        clientRadio = new javax.swing.JRadioButton();
        jPanel2 = new javax.swing.JPanel();
        serverRadio = new javax.swing.JRadioButton();
        startBoton = new javax.swing.JButton();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);
        setResizable(false);
        
        playerName.setFocusable(true);
        

        jLabel1.setFont(new Font("Courier 10 Pitch", Font.BOLD, 24));
        jLabel1.setHorizontalAlignment(javax.swing.SwingConstants.CENTER);
        jLabel1.setText("BattleShips");
        jLabel1.setVerticalTextPosition(javax.swing.SwingConstants.TOP);

        jLabel2.setText("Player name");
        jLabel2.setFont(new Font("Courier 10 Pitch", Font.PLAIN, 16));

        playerName.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                playerNameActionPerformed(evt);
            }
        });

        jPanel1.setPreferredSize(new java.awt.Dimension(180, 120));

        clientRadio.setSelected(true);
        clientRadio.setText("Client");
        clientRadio.setFont(new Font("Courier 10 Pitch", Font.PLAIN, 16));
        clientRadio.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                clientRadioActionPerformed(evt);
            }
        });

        javax.swing.GroupLayout jPanel1Layout = new javax.swing.GroupLayout(jPanel1);
        jPanel1Layout.setHorizontalGroup(
        	jPanel1Layout.createParallelGroup(Alignment.TRAILING)
        		.addGroup(jPanel1Layout.createSequentialGroup()
        			.addContainerGap(36, Short.MAX_VALUE)
        			.addComponent(clientRadio)
        			.addGap(41))
        );
        jPanel1Layout.setVerticalGroup(
        	jPanel1Layout.createParallelGroup(Alignment.LEADING)
        		.addGroup(jPanel1Layout.createSequentialGroup()
        			.addComponent(clientRadio)
        			.addContainerGap(96, Short.MAX_VALUE))
        );
        jPanel1.setLayout(jPanel1Layout);

        jPanel2.setPreferredSize(new java.awt.Dimension(180, 120));

        serverRadio.setText("Server");
        serverRadio.setFont(new Font("Courier 10 Pitch", Font.PLAIN, 16));
        serverRadio.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                serverRadioMouseClicked(evt);
            }
        });

        javax.swing.GroupLayout jPanel2Layout = new javax.swing.GroupLayout(jPanel2);
        jPanel2Layout.setHorizontalGroup(
        	jPanel2Layout.createParallelGroup(Alignment.LEADING)
        		.addGroup(jPanel2Layout.createSequentialGroup()
        			.addGap(66)
        			.addComponent(serverRadio)
        			.addContainerGap(GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
        );
        jPanel2Layout.setVerticalGroup(
        	jPanel2Layout.createParallelGroup(Alignment.LEADING)
        		.addGroup(jPanel2Layout.createSequentialGroup()
        			.addComponent(serverRadio)
        			.addContainerGap(112, Short.MAX_VALUE))
        );
        jPanel2.setLayout(jPanel2Layout);

        startBoton.setFont(new Font("Courier 10 Pitch", Font.PLAIN, 16));
        startBoton.setText("Start");
        startBoton.addMouseListener(new java.awt.event.MouseAdapter() {
            public void mouseClicked(java.awt.event.MouseEvent evt) {
                startBotonMouseClicked(evt);
            }
        });
        startBoton.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                startBotonActionPerformed(evt);
            }
        });
        jPanel3 = new javax.swing.JPanel();
        jLabel3 = new javax.swing.JLabel();
        mapSizeBox = new javax.swing.JComboBox<>();
        jLabel5 = new javax.swing.JLabel();
        ipServer = new javax.swing.JTextField();
        
        jLabel3.setText("Ip");
        jLabel3.setFont(new Font("Courier 10 Pitch", Font.PLAIN, 16));
                
        mapSizeBox.setModel(new javax.swing.DefaultComboBoxModel<>(new String[] { "7x7", "10x10", "13x13" }));
        mapSizeBox.setFont(new Font("Courier 10 Pitch", Font.PLAIN, 16));
        mapSizeBox.setBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(0, 0, 0)));
        mapSizeBox.setCursor(new java.awt.Cursor(java.awt.Cursor.HAND_CURSOR));
        mapSizeBox.addActionListener(new java.awt.event.ActionListener() {

        public void actionPerformed(java.awt.event.ActionEvent evt) {
        		mapSizeBoxActionPerformed(evt);
	        }
        });
                        
        jLabel5.setText("Map Size");
        jLabel5.setFont(new Font("Courier 10 Pitch", Font.PLAIN, 16));
                                
        ipServer.setHorizontalAlignment(javax.swing.JTextField.CENTER);
//        ipServer.setText("localhost");
        ipServer.setBorder(javax.swing.BorderFactory.createLineBorder(new java.awt.Color(0, 0, 0)));
        ipServer.setPreferredSize(new java.awt.Dimension(74, 25));
//                                        ipServer.addMouseListener(new java.awt.event.MouseAdapter() {
//                                            public void mouseClicked(java.awt.event.MouseEvent evt) {
//                                                ipServerMouseClicked(evt);
//                                            }
//                                        });
//                                        ipServer.addActionListener(new java.awt.event.ActionListener() {
//                                            public void actionPerformed(java.awt.event.ActionEvent evt) {
//                                                ipServerActionPerformed(evt);
//                                            }
//                                        });
                                        
        javax.swing.GroupLayout jPanel3Layout = new javax.swing.GroupLayout(jPanel3);
        jPanel3Layout.setHorizontalGroup(
        		jPanel3Layout.createParallelGroup(Alignment.LEADING)
                .addGroup(jPanel3Layout.createSequentialGroup()
                .addContainerGap()
                .addGroup(jPanel3Layout.createParallelGroup(Alignment.LEADING)
                .addComponent(jLabel3)
                .addComponent(jLabel5))
                .addPreferredGap(ComponentPlacement.RELATED)
                .addGroup(jPanel3Layout.createParallelGroup(Alignment.LEADING)
                .addComponent(mapSizeBox, 0, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addComponent(ipServer, GroupLayout.PREFERRED_SIZE, 100, GroupLayout.PREFERRED_SIZE))
                .addGap(56, 56, Short.MAX_VALUE))
                );
        jPanel3Layout.setVerticalGroup(
        		jPanel3Layout.createParallelGroup(Alignment.TRAILING)
                .addGroup(jPanel3Layout.createSequentialGroup()
                .addContainerGap(GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addGroup(jPanel3Layout.createParallelGroup(Alignment.BASELINE)
                .addComponent(jLabel3)
                .addComponent(ipServer, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE))
                .addPreferredGap(ComponentPlacement.UNRELATED)
                .addGroup(jPanel3Layout.createParallelGroup(Alignment.BASELINE)
                .addComponent(mapSizeBox, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
                .addComponent(jLabel5))
                .addGap(17))
        		);
        jPanel3.setLayout(jPanel3Layout);

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        layout.setHorizontalGroup(
        	layout.createParallelGroup(Alignment.LEADING)
        		.addGroup(layout.createSequentialGroup()
        			.addGroup(layout.createParallelGroup(Alignment.LEADING)
        				.addComponent(jLabel1, Alignment.TRAILING, GroupLayout.DEFAULT_SIZE, 400, Short.MAX_VALUE)
        				.addGroup(Alignment.TRAILING, layout.createSequentialGroup()
        					.addGap(137)
        					.addComponent(startBoton, GroupLayout.PREFERRED_SIZE, 125, GroupLayout.PREFERRED_SIZE)
        					.addGap(0, 138, Short.MAX_VALUE))
        				.addGroup(Alignment.TRAILING, layout.createSequentialGroup()
        					.addContainerGap(43, Short.MAX_VALUE)
        					.addGroup(layout.createParallelGroup(Alignment.TRAILING)
        						.addComponent(jLabel2)
        						.addComponent(jPanel1, GroupLayout.PREFERRED_SIZE, 112, GroupLayout.PREFERRED_SIZE))
        					.addGap(14)
        					.addGroup(layout.createParallelGroup(Alignment.LEADING)
        						.addComponent(playerName, GroupLayout.PREFERRED_SIZE, 178, GroupLayout.PREFERRED_SIZE)
        						.addComponent(jPanel2, GroupLayout.PREFERRED_SIZE, 233, GroupLayout.PREFERRED_SIZE)))
        				.addGroup(layout.createSequentialGroup()
        					.addGap(84)
        					.addComponent(jPanel3, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)))
        			.addContainerGap())
        );
        layout.setVerticalGroup(
        	layout.createParallelGroup(Alignment.LEADING)
        		.addGroup(layout.createSequentialGroup()
        			.addGap(20)
        			.addComponent(jLabel1, GroupLayout.DEFAULT_SIZE, GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
        			.addGap(36)
        			.addGroup(layout.createParallelGroup(Alignment.BASELINE)
        				.addComponent(playerName, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
        				.addComponent(jLabel2))
        			.addGap(30)
        			.addGroup(layout.createParallelGroup(Alignment.LEADING, false)
        				.addComponent(jPanel1, 0, 0, Short.MAX_VALUE)
        				.addComponent(jPanel2, GroupLayout.PREFERRED_SIZE, 26, Short.MAX_VALUE))
        			.addPreferredGap(ComponentPlacement.RELATED)
        			.addComponent(jPanel3, GroupLayout.PREFERRED_SIZE, GroupLayout.DEFAULT_SIZE, GroupLayout.PREFERRED_SIZE)
        			.addGap(18)
        			.addComponent(startBoton)
        			.addGap(20))
        );
        getContentPane().setLayout(layout);

        pack();
        setLocationRelativeTo(null);
    }// </editor-fold>//GEN-END:initComponents

    private void playerNameActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_playerNameActionPerformed
    }//GEN-LAST:event_playerNameActionPerformed

    private void serverRadioMouseClicked(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_serverRadioMouseClicked
        if (serverRadio.isSelected()) {
            clientRadio.setSelected(false);
        } else {
            if (clientRadio.isSelected() == false) {
                clientRadio.setSelected(true);
            }
        }        
    }//GEN-LAST:event_serverRadioMouseClicked

    private void clientRadioActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_clientRadioActionPerformed
        if (clientRadio.isSelected()) {
            serverRadio.setSelected(false);
        } else {
            if (serverRadio.isSelected() == false) {
                serverRadio.setSelected(true);
            }
        }
    }//GEN-LAST:event_clientRadioActionPerformed

    private void startBotonActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_startBotonActionPerformed
    }//GEN-LAST:event_startBotonActionPerformed

    private void startBotonMouseClicked(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_startBotonMouseClicked
        int size = 0;
        switch (mapSizeBox.getSelectedIndex()) {
            case 0:
                size = 7;
                break;
            case 1:
                size = 10;
                break;
            case 2:
                size = 13;
                break;
            default:
                size = 7;
        }
        if (ipServer.getText().isBlank() == false && playerName.getText().isBlank() == false) {
            if (serverRadio.isSelected()) {
//            	System.out.println("Name: " + playerName.getText() + "|   IP  " + ipServer.getText());
            	
            	serverBattleController.setIp(ipServer.getText());
                serverBattleController.setName(playerName.getText());
                serverBattleController.runServer(serverBattleController);
                    
                mapa = new MapBattleJFrame(size, serverBattleController);
                mapa.setVisible(true);
                this.setVisible(false);
                
            } else if (clientRadio.isSelected()) {
//            	System.out.println("Name: " + playerName.getText() + "|   IP  " + ipServer.getText());
                
            	clientBattleController.setIp(ipServer.getText());
                clientBattleController.setName(playerName.getText());
                clientBattleController.runClient(clientBattleController);
                	
                mapa = new MapBattleJFrame(size, clientBattleController);
                mapa.setVisible(true);
                this.setVisible(false);
                
            }
        } else if (playerName.getText().isBlank()) {
        	JLabel label = new JLabel(
        				"<html>" +
        				"<p>You must enter a player name.</p>" +
        				"</html>"
        			);
        	label.setFont(new Font("Courier 10 Pitch", Font.PLAIN, 15));
        	JOptionPane.showMessageDialog(this, label, "Enter Player Name", JOptionPane.WARNING_MESSAGE);
        } else if (ipServer.getText().isBlank()) {
        	JLabel label = new JLabel(
        			"<html>" +
        			"<p>You must enter a server IP string</p>" + 
        			"<p>'localhost' or number address</p>" +
        			"<p>For example: 192.0.0.2</p>" +
        			"</html>"
        			);
        	label.setFont(new Font("Courier 10 Pitch", Font.PLAIN, 15));
        	JOptionPane.showMessageDialog(this, label, "No Ip Server", JOptionPane.WARNING_MESSAGE);
        }
    }//GEN-LAST:event_startBotonMouseClicked

    private void mapSizeBoxActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_mapSizeBoxActionPerformed
    }//GEN-LAST:event_mapSizeBoxActionPerformed

    private void ipServerMouseClicked(java.awt.event.MouseEvent evt) {//GEN-FIRST:event_ipServerMouseClicked
    }//GEN-LAST:event_ipServerMouseClicked

    private void ipServerActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_ipServerActionPerformed
    }//GEN-LAST:event_ipServerActionPerformed

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(StartJFrame.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(StartJFrame.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(StartJFrame.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(StartJFrame.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new StartJFrame().setVisible(true);
            }
        });
    }
    
    private MapBattleJFrame mapa;
    
    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JRadioButton clientRadio;
    private javax.swing.JTextField ipServer;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabel5;
    private javax.swing.JPanel jPanel1;
    private javax.swing.JPanel jPanel2;
    private javax.swing.JPanel jPanel3;
    private javax.swing.JComboBox<String> mapSizeBox;
    private javax.swing.JTextField playerName;
    private javax.swing.JRadioButton serverRadio;
    private javax.swing.JButton startBoton;
    // End of variables declaration//GEN-END:variables
}
