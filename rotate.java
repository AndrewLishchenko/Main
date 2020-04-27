import java.io.*;
import java.net.*;
import java.awt.*;
import java.awt.event.*;
import java.awt.image.*;
import javax.imageio.*;
import javax.swing.*;
import java.util.Random;


public class rotate extends JFrame implements ActionListener, KeyListener, Runnable{ 
  //Variable and GUIObject Declaration area 
  Thread th=new Thread(this);
  MyDrawPanel draw=new MyDrawPanel();
  
  int i=0;
  int code;
  int counter=0;
  int time;
  long s=0, f=100;
  boolean timez=true;
  public static void main(String[ ] args) 
  {
    new rotate();
  }  
  
  public rotate(){
    //Create object and your code goes here
    addKeyListener(this);
    this.add(draw);
    this.setSize(500,500);
    this.setVisible(true);
    
    
    while(true)
    {
      i++;
      try
      {
        th.sleep(10);      
      }
      catch(InterruptedException ex) 
      {
        System.out.print("how this happen?"); 
      }
      
      th.currentThread().setPriority(Thread.MAX_PRIORITY);
      repaint();
      
    }
  }
  public void actionPerformed(ActionEvent e){}
  public void run (){}
  public void keyReleased (KeyEvent e){}
  public void keyTyped(KeyEvent e){}  
  public void keyPressed (KeyEvent e){
    code=e.getKeyCode();
    if(code == KeyEvent.VK_LEFT)//MOVE LEFT
    {
      
      
      counter++;
      
      System.out.println(counter);
      repaint();
    }
  }
  
  class MyDrawPanel extends JPanel {//DRAW PANEL METHOD OTHERWISE KNOW AS "WHERE THE MAGIC HAPPENES"
    public void paintComponent(Graphics g) {
      
      Graphics2D g2 = (Graphics2D)g;
      
      g2.setRenderingHint(RenderingHints.KEY_ANTIALIASING,RenderingHints.VALUE_ANTIALIAS_ON);
      
      
//      AffineTransform at=AffineTransform.getTranslateInstance(100,100);
//
//      Rectangle rect= new Rectangle(200,200,100,50);
//
//     
//      g2.rotate(Math.toRadians(60),250,225);

      
      
      g2.rotate(Math.toRadians(i),250,225);
      
      g2.drawLine(200,200,300,300);
      
      g2.rotate(Math.toRadians(360-i),250,225);
      
      g2.rotate(Math.toRadians(2*i),45,45);
      
      g2.fillRect(20,20,50,50);
      
    }
  }
}




