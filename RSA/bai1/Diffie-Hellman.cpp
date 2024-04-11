#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

long long moduloPower(long long base, long long exponent, long long modulus) {
    long long result = 1;
    base = base % modulus;
    while (exponent > 0) {
        if (exponent % 2 == 1)
            result = (result * base) % modulus;
        exponent = exponent >> 1;
        base = (base * base) % modulus;
    }
    return result;
}

main() {
    ifstream inputFile("input.txt");
    if (!inputFile.is_open()) {
        cerr << "Loi: Khong the mo file input" << endl;
        return 1;
    }

    long long q, a, xA, xB;
    if (!(inputFile >> q >> a >> xA >> xB)) {
        cerr << "Loi: Input khong hop le" << endl;
        return 1;
    }

    inputFile.close();

    long long yA = moduloPower(a, xA, q);
    cout << "Khoa cong khai cua An (yA): " << yA << endl;

    long long K_A = moduloPower(yA, xB, q);
    cout << "Khoa phien cua An (K_A): " << K_A << endl;

    long long yB = moduloPower(a, xB, q);
    cout << "Khoa cong khai cua Ba (yB): " << yB << endl;

    long long K_B = moduloPower(yB, xA, q);
    cout << "Khoa phien cua Ba (K_B): " << K_B << endl;

    return 0;
}
