#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include "AurickAnwarSummative.cpp"//include the header file

using namespace std;

struct Question {//struct for the question
    string question;//question
    string answer;//answer
};

vector<Question> readQuestionsFromFile(const string& filename) {//function to read the questions from the file
    vector<Question> questions;//vector to store the questions
    ifstream file(filename);//open the file

    if (file.is_open()) {//if the file is open
        string line;//string to store each line
        while (getline(file, line)) {//while there are lines to read
            stringstream ss(line);//stringstream to parse the line
            string question, answer;//strings to store the question and answer
            getline(ss, question, ',');//get the question
            getline(ss, answer);//get the answer
            questions.push_back({question, answer});//add the question and answer to the vector
        }
        file.close();//close the file
    }

    return questions;//return the vector of questions
}

int animals(int value) {//function to play the animals game
    int points = 0;//points to keep track of the player's score
    string userAnswer;//string to store the player's answer

    vector<Question> questions = readQuestionsFromFile("animals.txt");//read the questions from the file

    if (value >= 100 && value <= 500) {//if the value is between 100 and 500
        Question currentQuestion = questions[value / 100 - 1];//get the current question
        cout << currentQuestion.question << " ";//print the question
        getline(cin, userAnswer);//get the player's answer

        for(char &c : userAnswer) {
            c = tolower(c);//convert the answer to lowercase
        }
        for(char &c : currentQuestion.answer) {
            c = tolower(c);//convert the answer to lowercase
        }

        if (userAnswer == currentQuestion.answer) {//if the answer is correct
            cout << "Correct!" << endl;//print correct
            points += value;//add the value to the player's score
        } else {//if the answer is incorrect
            cout << "Incorrect!" << endl;//print incorrect
            points -= value;//subtract the value from the player's score
        }
    } 

    return points;//return the player's score
}

//the following functions are the same as the animals function except for the file name and the value range
int science(int value) {
    int points = 0;
    string userAnswer;

    vector<Question> questions = readQuestionsFromFile("science.txt");

    if (value >= 100 && value <= 500) {
        Question currentQuestion = questions[value / 100 - 1];
        cout << currentQuestion.question << " ";
        getline(cin, userAnswer);
        for(char &c : userAnswer) {
            c = tolower(c);
        }
        for(char &c : currentQuestion.answer) {
            c = tolower(c);
        }

        if (userAnswer == currentQuestion.answer) {
            cout << "Correct!" << endl;
            points += value;
        } else {
            cout << "Incorrect!" << endl;
            points -= value;
        }
    } 
    

    return points;
}
int music(int value) {
    int points = 0;
    string userAnswer;

    vector<Question> questions = readQuestionsFromFile("music.txt");

    if (value >= 100 && value <= 500) {
        Question currentQuestion = questions[value / 100 - 1];
        cout << currentQuestion.question << " ";
        getline(cin, userAnswer);
        for(char &c : userAnswer) {
          c = tolower(c);
        }
        for(char &c : currentQuestion.answer) {
          c = tolower(c);
        }

        if (userAnswer == currentQuestion.answer) {
            cout << "Correct!" << endl;
            points += value;
        } else {
            cout << "Incorrect!" << endl;
            points -= value;
        }
    } 

    return points;
}
int movies(int value) {
    int points = 0;
    string userAnswer;

    vector<Question> questions = readQuestionsFromFile("movies.txt");
  

    if (value >= 100 && value <= 500) {
        Question currentQuestion = questions[value / 100 - 1];
        cout << currentQuestion.question << " ";
        getline(cin, userAnswer);
        for(char &c : userAnswer) {
          c = tolower(c);
        }
        for(char &c : currentQuestion.answer) {
          c = tolower(c);
        }

        if (userAnswer == currentQuestion.answer) {
            cout << "Correct!" << endl;
            points += value;
        } else {
            cout << "Incorrect!" << endl;
            points -= value;
        }
    } 

    return points;
}
int sports(int value) {
    int points = 0;
    string userAnswer;

    vector<Question> questions = readQuestionsFromFile("sports.txt");

    if (value >= 100 && value <= 500) {
        Question currentQuestion = questions[value / 100 - 1];
        cout << currentQuestion.question << " ";
        getline(cin, userAnswer);
        for(char &c : userAnswer) {
            c = tolower(c);
        }
        for(char &c : currentQuestion.answer) {
            c = tolower(c);
        }

        if (userAnswer == currentQuestion.answer) {
            cout << "Correct!" << endl;
            points += value;
        } else {
            cout << "Incorrect!" << endl;
            points -= value;
        }
    } 

    return points;
}


