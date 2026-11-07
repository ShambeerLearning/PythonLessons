#include <iostream>
#include <cmath>
using namespace std;
int main() {
	setlocale(LC_ALL, "ru");
	int I, N;
	cout << "Введите первое число промежутка - ";
	cin >> I;
	cout << "Введите второе число промежутка - ";
	cin >> N;
	while (I < N) {
		if (I % 2 != 0 && I % 3 != 0 && I % 5 != 0 && I % 7 != 0 && sqrt(I) != (int)I) {
			cout << I << endl;
			I++;
		}
		else {
			I++;
		}
	}
	system("pause");
}