#include <iostream>
#include <stdexcept>
#include <vector>
using namespace std;
class Transport {
public:
    virtual void info() const = 0;
    virtual ~Transport() = default;
};
class Bicycle : public Transport {
public:
    void info() const override {
        cout << "велосипед" << endl;
    }
};
class Car : public Transport {
public:
    void info() const override {
        cout << "автомобиль" << endl;
    }
};
class Truck : public Transport {
public:
    void info() const override {
        cout << "грузовик" << endl;
    }
};
template <typename T>
class PointerArray {
private:
    vector<T*> items;
public:
    void add(T* item) {
        items.push_back(item);
    }
    T* operator[](size_t index) {
        if (index >= items.size()) {
            throw out_of_range("индекс выходит за пределы списка");
        }
        return items[index];
    }
    ~PointerArray() {
        for (auto item : items) {
            delete item;
        }
    }
};
int main() {
    setlocale(LC_ALL, "Russian");
    try {
        PointerArray<Transport> transports;
        transports.add(new Bicycle());
        transports.add(new Car());
        transports.add(new Truck());
        for (size_t i = 0; i < 3; ++i) {
            transports[i]->info();
        }
        transports[10]->info();
    }
    catch (const out_of_range& e) {
        cerr << "исключение: " << e.what() << endl;
    }
    return 0;
}