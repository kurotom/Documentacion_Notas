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

/**
 *
 * @author kurotom
 * https://github.com/kurotom
 * 
 */

package com.battleships.app.controller;

import java.util.List;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTable;

public abstract class AbstractController {
	
	public abstract void close();
	
	public abstract boolean isConnected();
	
	public abstract void sendCoords(List<Integer> lista);
	
	public abstract void setName(String name);
	
	public abstract String getName();
	
	public abstract void setCoords(List<List<List>> lista);
	
	public abstract List<List<List>> getCoords();

	public abstract void setIp(String str);

	public abstract void setFrame(JFrame thisFrame);

	public abstract Integer amountLive();

	public abstract boolean hitShip(List<Integer> coords);

	public abstract void setSurrenderButton(JButton btn);

	public abstract void setAttackButton(JButton btn);

	public abstract void setStatusAttackLabel(JLabel label);

	public abstract void setStatusPlayerLabel(JLabel label);

	public abstract void setTableMapOponent(JTable tabla);

	public abstract void setTableMapPlayer(JTable tabla);

	public abstract void setPlayeLifeLabel(JLabel label);

	public abstract Integer getPlayerLife();

	public abstract void statusAttack(String str);

	public abstract void coordsAtackOponent(List<Integer> coords);

	public abstract void drawOponentMap(String str);

	public abstract void sendSurrender();

	public abstract void victoryMessage();

	public abstract void defeatMessage();
	

}
