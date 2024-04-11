#include <iostream>
#include <fstream>
#include <cmath>
using namespace std;

long long gcd(long long a, long long b) {
    if (b == 0)
        return a;
    return gcd(b, a % b);
}

long long modInverse(long long a, long long m) {
    a = a % m;
    for (long long x = 1; x < m; x++)
        if ((a * x) % m == 1)
            return x;
    return 1;
}

long long powerMod(long long base, long long exponent, long long modulus) {
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

    long long p, q, e, M;
    if (!(inputFile >> p >> q >> e >> M)) {
        cerr << "Loi: Input khong hop le" << endl;
        return 1;
    }

    inputFile.close();

    long long n = p * q;
    long long phi_n = (p - 1) * (q - 1);

    long long d = modInverse(e, phi_n);

    std::pair<long long, long long> PU = {e, n};
    std::cout << "Khoa cong khai cua An (PU): {" << PU.first << ", " << PU.second << "}" << std::endl;

    std::pair<long long, long long> PR = {d, n};
    std::cout << "Khoa rieng cua An (PR): {" << PR.first << ", " << PR.second << "}" << std::endl;

    long long C = powerMod(M, d, n);
    std::cout << "Ban ma hoa cua M = " << M << ": " << C << std::endl;

    long long decrypted_M = powerMod(C, e, n);
    std::cout << "Giai ma ban ma: " << decrypted_M << std::endl;

    std::cout << "Viec ma hoa o cau c la thuc hien nhiem vu chu ky so." << std::endl;

    return 0;
}
