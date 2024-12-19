#include <iostream>
#include <vector>
#include <memory>

class Detail {
protected:
    Detail() { std::cout << "Detail created\n"; }

public:
    virtual ~Detail() { std::cout << "Detail destroyed\n"; }
    virtual void show() const = 0;

    template <typename T, typename... Args>
    friend std::shared_ptr<T> create(Args&&... args);
};

class Assembly : public Detail {
protected:
    Assembly() { std::cout << "Assembly created\n"; }

public:
    ~Assembly() override { std::cout << "Assembly destroyed\n"; }
    void show() const override { std::cout << "This is an assembly.\n"; }

    template <typename T, typename... Args>
    friend std::shared_ptr<T> create(Args&&... args);
};

template <typename T, typename... Args>
std::shared_ptr<T> create(Args&&... args) {
    return std::shared_ptr<T>(new T(std::forward<Args>(args)...));
}

int main() {
    std::vector<std::shared_ptr<Detail>> details;

    details.push_back(create<Assembly>());

    for (const auto& detail : details) {
        detail->show();
    }

    return 0;
}
