#include <iostream>
#include <cstdlib>

class Person {
  public:
  char name[10];
  int age;
};

class student: public Person {
  public:
  int grad_year;
  int id;
};

class teacher : public Person {
  public:
  int teacher_id;
  char subject[20];
};

int main() {
  int i = 1;
  while(i != 0) {
    std::cout << "Are you a student or a teacher?\n";
    std::cout << "If you are a student, type 1. Otherwise, type 2. To quit, type 0.\n";
    std::cin >> i;
    if (i == 0) break;
    else if (i == 1) {
      student a;
      std::cout << "What's your name?\n";
      std::cin >> a.name;
      std::cout << "How old are you?\n";
      std::cin >> a.age;
      std::cout << "What's your student id?\n";
      std::cin >> a.id;
      std::cout << "What year will you graduate?\n";
      std::cin >> a.grad_year;

      std::cout << "Welcome, " << a.name << " " << a.id << ", Class of " << a.grad_year << "!\n";
      std::cout << std::endl;
    } else {
      teacher a;
      std::cout << "What's your name?\n";
      std::cin >> a.name;
      std::cout << "How old are you?\n";
      std::cin >> a.age;
      std::cout << "What's your teacher id?\n";
      std::cin >> a.teacher_id;
      std::cout << "What subject do you teach?\n";
      std::cin >> a.subject;

      std::cout << "Welcome, our new " << a.subject << " teacher, " << a.name << " " << a.teacher_id << "!\n";
      std::cout << std::endl;
    }
  }
}