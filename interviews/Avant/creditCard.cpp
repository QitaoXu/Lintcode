#include <iostream>
#include <map>
#include <iostream>
#include <vector>

using namespace std;. From 1point 3acres bbs

/**
* At the end of each day, there will be a closing information
* A piece of information mainly contains 3 variables:
* 1. The day (how long from the opening account day). 1point3acres
* 2. Balance. If the balance > 0, meaning owing bank many and every day the balance cause interest
*             If the balance < 0, meaning we paid more than expected. The money can be used later
*             to purchase, or pay for the debt
* 3. Interest. Accumulated interest generated in the current 30 days.
*
* Key conception:
* 1. Base Day, the start day of each period, 0 day, 30 day, 60 day... At this day, interest become a part
*    of balance and reset to be 0. Day 1 ~ Day 30 's Base Day is 0. To calculate the closing information of a specific day, we should calculate the
*    previous Closing Day if it is not smaller than Base Day. Or we calculate the Base Day because we need to. 1point3acres
*    close last month.
* 2. Closing day, the program only record the transaction day as a Closing Day. Any other day's closing
*    information can be calculated.
*/
class DailyClosingInfo {
    /**
     * How long is it from the opening day
     */
    int day;

    /**-baidu 1point3acres
     * How much many owe. Can be negative
     */
    double outstanding_balance;

    /**
     * The total interest till now, generate in the 30 days
     */
    double accrued_interest;

public:
    /**
     *
     */
    DailyClosingInfo() : day(0), outstanding_balance(0), accrued_interest(0) {};

    /**
     *
     * @param d
     * @param o
     * @param a
     */
    DailyClosingInfo(int d, double o, double a) : day(d), outstanding_balance(o), accrued_interest(a) {};

    /**
     *
     * @return
     */
    inline int getDay() {
        return day;
    }

    /**
     *
     * @return
     */
    inline bool isBaseDay() {-baidu 1point3acres
        return day % 30 == 0;
    }

    /**
     * Before next closing day, this much money would generate interest
     * This is tightly related to balance but not balance
     * If the day is the Base Day, interest generated through the past 30 days
     * should be add to the balance

     * If the amount is smaller than 0, debt is 0
     * @return
     */
    double getDebt() {
        double balance = getBalance();
        return balance > 0 ? balance : 0;
    }

    /**
     *
     * @return
     */
    double getBalance() {
        if (isBaseDay())
            return outstanding_balance + accrued_interest;
        else
            return outstanding_balance;
    }

    /**
     *
     * @return
     */
    double getInterest() {
        return isBaseDay() ? 0 : accrued_interest;
    }

    /**
     *
     * @return
     */
    double getAccumulatedInterest() {
        return isBaseDay() ? 0 : accrued_interest;
    }

    /**
     *
     * @param debt
     */
    void setDebt(double debt) {
        outstanding_balance = debt;
    }

    /**
     *
     * @param _d
     */
    void setDay(int _d) {
        day = _d;
    }

    /**
     *
     * @param interest
     */
    void setInterest(double interest) {
        accrued_interest = interest;-baidu 1point3acres
    }

};

/**
* Toy transaction storage
*/
struct Transaction {
    int day;
    double amount;
    double balance;

    Transaction(int _day, int _amount, int _balance): day(_day), amount(_amount), balance(_balance){};
};

/**
*
*/
class CreditCard {
private:
    map<int, DailyClosingInfo> closing_history;
    vector<Transaction> charges_history;
    vector<Transaction> pays_history;

    /**
     *
     */
    double limit;

    /**
     *
     */
    double apr;

    /**
     *
     * @param day-baidu 1point3acres
     * @return
     */
    DailyClosingInfo getLastClosingInfo(int day) {
        return prev(closing_history.upper_bound(day))->second;
    }

    /**
     *
     * @return
    */
    DailyClosingInfo getLastClosingInfo() {
        return prev(closing_history.end())->second;
    }

    /**
     *
     * @param day
     * @return
     */
    int getBaseDay(int day) {
        return 30 * ((day - 1) / 30);
    }

    /**
     *
     * @param info
     */. 1point3acres
    void updateInfoHistory(DailyClosingInfo info) {
        closing_history[info.getDay()] = info;
    }

    /**
     * Last closing day or the base day
     * @param day
     * @return
     */
    DailyClosingInfo getReferenceInfo(int day) {
-baidu 1point3acres
        if (closing_history.find(day) != closing_history.end()) {
            return closing_history[day];
        }

        DailyClosingInfo last_closing_info = getLastClosingInfo(day);
        int base_day = getBaseDay(day);
        return last_closing_info.getDay() < base_day ? getClosingInfo(base_day) : last_closing_info;
    }

public:
    /**
     * Open an account by create a CreditCard object
     * @param _limit
     * @param _apr
     */
    CreditCard(double _limit, double _apr) : limit(_limit), apr(_apr) {
        closing_history[0] = DailyClosingInfo(0, 0, 0);
    };

    /**
     *. From 1point 3acres bbs
     * @param day
     * @param amount
     * @return If the transaction is successful. check 1point3acres for more.
     */
    bool transaction(int day, double amount) {
        // todo: record failed transaction_history
        // To make a successful transaction, the transaction day
        // must be at least the last closing day or after it
        DailyClosingInfo last_info = getLastClosingInfo();. check 1point3acres for more.
        if (last_info.getDay() > day) {
            cout << "Transaction failed, can not flow back." << endl;
            return false;
        }

        // Get the day's closing info and update the balance
        DailyClosingInfo info = getClosingInfo(day);
        if (info.getDebt() + amount > limit) {
            cout << "Transaction failed, exceeded limit." << endl;
            return false;
        }

        // update the transaction history and the closing history

        info.setDebt(info.getBalance() + amount);
        updateInfoHistory(info);
        if (amount > 0) {
            charges_history.push_back(Transaction(day, amount, info.getBalance()));
        } else {
            pays_history.push_back(Transaction(day, amount, info.getBalance()));. 1point3acres
        }

        cout << "[Transaction notice] ";
        cout << (amount > 0 ? "Swipe " : "Pay ") << (amount > 0 ? amount : -amount) << " at day " << day << ", balance is " << info.getBalance() << endl;

        return true;
    }

    /**
     *
     * @param day
     * @return
     */
    DailyClosingInfo getClosingInfo(int day) {

        if (closing_history.find(day) != closing_history.end())
            return closing_history[day];

        DailyClosingInfo reference_day_info = getReferenceInfo(day);

        return DailyClosingInfo(
            day,
            reference_day_info.getBalance(),
            reference_day_info.getInterest() + reference_day_info.getDebt() * ((day - reference_day_info.getDay()) * apr / 365.0). 1point3acres
        );

    }

    void showBalance(int day) {
        cout << "[Query for balance] At day " << day;
        if (day < 0)
            cout << " failed. Must bigger than 0" << endl;
        else
            cout << ", the balance is " << getClosingInfo(day).getBalance() << endl;
    }

    void showSwipeHistory() {
        cout << "[Query swiping history] " << endl;
        for (auto each:charges_history)-baidu 1point3acres
            cout << "At day " << each.day << ", swiped " << each.amount << ", balance was " << each.balance << endl;
        cout << "[Query end] " << endl;

    }

    void showPayHistory() {
        cout << "[Query paying history] " << endl;
        for (auto each:charges_history)
            cout << "At day " << each.day << ", paid " << -each.amount << ", balance was " << each.balance << endl;
        cout << "[Query end] " << endl;
    }

};

void test1() {
    // Open account
    CreditCard card(1000.0, 0.35);
    // Swipe 500. 1point3acres
    card.transaction(0, 500);
    // Show balance at day 30
    card.showBalance(30);
}

void test2() {
    CreditCard card(1000.0, 0.35);
    card.transaction(0, 500);
    card.transaction(15, -200);
    card.transaction(25, 100);

    card.showBalance(30);
}

void test3() {
    CreditCard card(1000.0, 0.35);
    card.transaction(0, 300);
    card.transaction(1, -300);
    card.transaction(2, 897);
    card.showBalance(-30);
}

int main() {
    test2();
    return 0;
}