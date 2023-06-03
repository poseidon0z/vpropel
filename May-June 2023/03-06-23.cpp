/*
QUESTION:

Joined Number
A set of house numbers were formed using number tiles as shown below. During transportation, the numbers got joined. Vivek knows the sum of digits of his house number but do not know the exact house number and the number of digits in it.


Given the joined number ‘n’ and the sum of house number ‘h’, write a C++ program to find all possible consequent digits of ‘n’ whose sum of digits is ‘h’. For example, if the joined number ‘n’ is 7234198523322 and house number ‘h’ as 17, the answers are 72341, 3419, 98 and 523322

Hint:

This problem can be quickly solved with string in STL. STL is Standard Template Library that has got generic functions, classes and algorithms.

To use string, add #include<string>

We can create object and array of objects for string

length is a member function of string that gives the number of characters in it

You can access ith character of a string object s as s[i] – Subscript operator is overloaded

substr(i,n) – will return a substring from position ‘i’ and of length ‘n’

stol(s) – returns long integer of string s

Sample Code using String in STL

#include<iostream>

using namespace std;

#include<string>

int main()

{

string s1,s2;

int l,pos;

long int li;

cin>>s1;

//get length of s1

l=s1.length();

//substring of length 3 from position 2

s2 = s1.substr(2,3);

li = stol(s1);

}

Input Format

First line contains the joined number, n

Next line contains the sum of the house number, h

Output Format

Print the consequent digits that may be house number separated by a tab
*/

/*
Imports:
iostream for cin and cout
string to use string object, and string functions: length(), substr()
vector to use a vector object
*/
#include <iostream>
#include <string>
#include <vector>

// Setting the namespace used
using namespace std;

int main()
{
    vector<string> answers;

    // Initialising variables to hold joined number and house number
    string num;
    int house;

    // taking inputs
    cin >> num;
    cin >> house;

    // Checking for sum = house number
    // For each digit in string of numbers
    for (int i = 0; i < num.length(); i++)
    {
        int total = 0;

        // For each string following that number
        for (int j = i; j < num.length(); j++)
        {
            total += num[j] - 48;

            if (total == house)
            {
                answers.push_back(num.substr(i, j - i + 1));
            }
            else if (total > house)
            {
                break;
            }
        }
    }

    // Displaying answers
    for (string answer : answers)
    {
        cout << answer << "\t";
    }

    // 0 returned to show successful execution
    return 0;
}