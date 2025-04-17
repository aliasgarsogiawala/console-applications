import java.util.*;
public class rockpaperscrissors{
    public static void main(String[]args){
        Scanner sc=new Scanner(System.in);
        System.out.println("Welcome to Rock Paper Scissors!");
        System.out.println("First to 5 wins!");
        int playerscore=0;
        int computerscore=0;
        while(playerscore<5&&computerscore<5){
            System.out.println("Enter your choice:");
            System.out.println("1. Rock");
            System.out.println("2. Paper");
            System.out.println("3. Scissors");
            int playerchoice=sc.nextInt();
            int computerchoice=(int)(Math.random()*3)+1;
            System.out.println("Computer chose: "+computerchoice);
            if(playerchoice==computerchoice){
                System.out.println("Tie!");
            }
            else if(playerchoice==1&&computerchoice==2){
                System.out.println("Computer wins!");
                computerscore++;
            }
            else if(playerchoice==1&&computerchoice==3){
                System.out.println("Player wins!");
                playerscore++;
            }
            else if(playerchoice==2&&computerchoice==1){
                System.out.println("Player wins!");
                playerscore++;
            }
            else if(playerchoice==2&&computerchoice==3){
                System.out.println("Computer wins!");           
                computerscore++;    
            }
        }
    }
}