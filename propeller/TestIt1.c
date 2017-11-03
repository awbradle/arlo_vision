/*
  Welcome.c
  
  Welcome to SimpleIDE, the C programming environment that makes it easy to 
  get started with the multi-core Propeller microcontroller! 
  
  To run this program:
  
    - Is this the first Parallax software you've installed on your computer?  
      If so, install USB driver's now: www.parallax.com/usbdrivers
    - Connect your Propeller board to your computer's USB.  Also connect power
      to the board if needed, and if it has a power switch, turn it on.
    - Make sure to select your COM port from the toolbar dropdown menu in the
      upper-right corner.  If you are unsure which COM port your board is 
      connected to, disconnect it and click the dropdown to check the port 
      list, then reconnect it and check again.
    - Click Program and select Run with Terminal (or click the Run with Terminal 
      button).  The SimpleIDE Terminal should appear and display the "Hello!"
      message.
      
   Next, check the Help menu for new online tutorials, software manual, and 
   reference material.
   http://learn.parallax.com/propeller-c-tutorials
*/
#include "arlodrive.h"
#include "simpletools.h"                      // Include simple tools
#include "fdserial.h"

fdserial *xxx;

char LEFT=64;
char RIGHT=32;
char TURRET=16;
char NEGATIVE=8;
char c;
int left_motor;
int right_motor;


int main()                                    // Main function
{
  
  
  
  xxx=fdserial_open(3,4,0,9600);  //receive 3 send 4, mode 0??,baudrate
  // Add startup code here.
  while(1)
  {
    while((c=fdserial_rxChar(xxx))>128);
      print("%d\n",c);
      switch (c){
      case 72:
       forward();
        break;
      case 80:
        down();
         break;
       case 77:
          right();
          break;
       case 75:
        left();
        break;
        }          
        
//    decode(c);
//    drive_speed(left_motor,right_motor);
    print("Value is %d\n",c);
  }   
 
}  


void forward()
{
  
  drive_speed(64,64);
  pause(1000);
  drive_speed(0,0);

}

void down()
{
  
  drive_speed(-64,-64);
  pause(1000);
  drive_speed(0,0);

}

void right()
{
  
  drive_speed(64,-64);
  pause(1000);
  drive_speed(0,0);

}

void left()
{
  
  drive_speed(-64,64);
  pause(1000);
  drive_speed(0,0);

}


void decode(char x)
{
  int exponent;
  int speed=16;
  int j;
  left_motor=0;
  right_motor=0;
  exponent=(x & 7);
  for(j=0;j<exponent;j++)
    speed+=16;
  if(x & NEGATIVE)
    speed*=-1;  
  left_motor= (x & LEFT  ? speed : 0);
  right_motor=(x & RIGHT ? speed : 0);
  
}



