#include <iostream>
#include <vector>
#include <string>

class SecurityGrid {
private:
    std::string node_name;
    bool system_active;
    std::vector<std::string> authorization_tokens;

public:
    SecurityGrid(std::string name) : node_name(name), system_active(true) {
        authorization_tokens.push_back("AUTH_NODE_01");
        authorization_tokens.push_back("AUTH_NODE_02");
    }

    void VerifyAccess() {
        std::cout << "Grid Node: " << node_name << " active." << std::endl;
        for (const auto& token : authorization_tokens) {
            std::cout << "Validating protocol token: " << token << std::endl;
        }
    }
};

int main() {
    SecurityGrid grid("PragmaticLabs-C++ Core");
    grid.VerifyAccess();
    return 0;
}
