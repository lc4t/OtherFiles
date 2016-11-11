#include <iostream>
#include <string>

void tree(std::string NLRstr, std::string LNRstr)
{
    if (NLRstr.size() < 1)
    {
        // return
    }
    else if (NLRstr.size() == 1)
    {
        std::cout << NLRstr[0];
    }
    else
    {
        // abcdefg NLR
        // cbdaegf LNR
        // cdbgfea LRN

        // use N(root) to split the NLRstr, get the NLR parts
        int index = LNRstr.find(NLRstr[0]);
        std::string leftNRL = NLRstr.substr(1, index);
        std::string rightNRL = NLRstr.substr(index + 1, NLRstr.size() - 1 - index);

        // use N(root) to split the LNRstr, get the LNR parts
        std::string leftLNR = LNRstr.substr(0, index);
        std::string rightLNR = LNRstr.substr(index + 1, LNRstr.size() - 1  - index);

        // recursion
        tree(leftNRL, leftLNR);
        tree(rightNRL, rightLNR);
        std::cout << NLRstr[0];

        return;
    }



}


int main(int argc, const char* argv[])
{
    std::string NLR, LNR;
    std::cin >> NLR >> LNR;
    tree(NLR, LNR);
    return 0;
}
