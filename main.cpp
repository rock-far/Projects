#include <iostream>
#include <iomanip>
#include "Jeopardy.h"
#include "AurickAnwarSummative.cpp"

using namespace std;

string table[6][5] = {//table array
    {"Animals", "Science", "Music", "Movies", "Sports"},
    {"100", "100", "100", "100", "100"},
    {"200", "200", "200", "200", "200"},
    {"300", "300","300", "300", "300"},
    {"400", "400", "400", "400", "400"},
    {"500", "500", "500", "500", "500"}};

void displayTable(string table[6][5])
{
    for (int i = 0; i < 6; i++)
    {
        for (int j = 0; j < 5; j++)
        {
            cout << left << setw(10) << table[i][j] << " ";
        }
        cout << endl;
    }
  //couts the table of categories
}

int main()
{
    displayTable(table);//function to display table

    bool finish = true;

    int totalPoints = 0;//total points

    while (finish)//loop has started
    {
        int choice;
        cout << "Enter a category (1-5): ";
        cin >> choice;
      //user inputs a category

        int value;
        cout << "Enter a value (100-500): ";
        cin >> value;
        //user inputs a value
        cin.ignore();//cin.ignore

        if (choice < 1 || choice > 5)
        {
            cout << "Invalid choice" << endl;
        }//if the user inputs a number that is not 1-5, it will display invalid choice
        if (value < 100 || value > 500)
        {
            cout << "Invalid value" << endl;
        }//if the user inputs a number that is not 100-500, it will display invalid value

        else{

        int points = 0;//points
        

        switch (choice)//switch statement
        {
        case 1://Animals
            cout << "\nAnimals" << endl;
            points = animals(value);
            break;

         case 2://Science
          cout<<"\nScience"<<endl;
          points = science(value);
          break;
        case 3://Music
          cout<<"\nMusic"<<endl;
          points = music(value);
          break;
        case 4://Movies
          cout<<"\nMovies"<<endl;
          points = movies(value); 
          break;
        case 5://Sports
          cout<<"\nSports"<<endl;
          points = sports(value);
          break; 
        }
        
        totalPoints += points;//after each category, the total points will be added to the total points
        

        cout << "Your current score is: " << totalPoints << endl;//The current score will be updated after each guess
        }

        // Prompt for continuing
        char response;
        cout << "Do you want to continue? (Y/N): ";//asks the user if they want to continue
        cin >> response;

        // Update finish based on the user's response
        if(response == 'N' || response == 'n'){//if the user inputs N or n, the loop will end
           cout<<"\nYour final score: "<<totalPoints<<endl;
           cout << "Thank you for playing!" << endl;
         
          finish = false;
          
        }
        else if(response == 'Y' || response == 'y'){//if the user inputs Y or y, the loop will continue)
          finish = true;
        }
        else{
          cout<<"Invalid response"<<endl;
        }
              
    }
    return 0;
}

