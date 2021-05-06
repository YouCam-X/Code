#include<iostream>
using namespace std;

int calculate();

int calculate() {
	
	int sum = 0;
	int i;
	char ch;

	cout << "请输入一些整数和空格，将帮你计算所有整数的和" << endl;

	if ((ch = getchar()) == '\n') {

		return 0;
	}

	while (scanf_s("%d", &i) == 1) {

		sum += i;

		if (ch = getchar() == '\n') {

			break;
		}

		while ((ch = getchar()) == ' '|| (ch = getchar()) > '9') {

			if (ch = getchar() == '\n') {

				return 0;
			}
		}
	}

	cout << "结果是：" << sum << endl;
	cout << "\n";
	system("pause");

	return 0;
}

void main() {
	
	int w;

	for (w = 0; w < 100; w++) {
		
		calculate();
	}
}