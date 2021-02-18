#include <iostream>
#include "../../headers/helpers/NumberGenerator.h"
#include "../../headers/tasks/Task_7_17.h"

void StartTask_7_17(int numberOfIterations, int numberOfButches, double percentOfSecondRate)
{
    int count1 = 0;
    int count2 = 0;
    int n = numberOfIterations;

    for (int i = 0; i < numberOfIterations; i++) {
        int butchWithSecondRate = GetRandomInt(1, numberOfButches);
        int chosenButch = GetRandomInt(1, numberOfButches);
        if (butchWithSecondRate == chosenButch) {
            if (GetRandomDouble(0, 1) > percentOfSecondRate) {
                count1++;
                if (GetRandomDouble(0, 1) > percentOfSecondRate)
                    count2++;
            }
            else
                n--;
        }
    }

    std::cout << "Task 7.17:" << std::endl;
    std::cout << "Result 1: " << (double)count1 / n << std::endl;
    std::cout << "Result 2: " << (double)count2 / n << std::endl;
}