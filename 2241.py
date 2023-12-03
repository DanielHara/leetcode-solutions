"""
Question 2241: https://leetcode.com/problems/design-an-atm-machine/

    Not a difficult question, just do it!
    Should actually be rated as easy, IMHO.
"""

class ATM:
    def __init__(self):
        # Bank notes of denominations: 20, 50, 100, 200, 500
        self.bank_notes = [{
            'value': 20,
            'count': 0
        },
        {
            'value': 50,
            'count': 0
        },
        {
            'value': 100,
            'count': 0
        },
        {
            'value': 200,
            'count': 0
        },
        {
            'value': 500,
            'count': 0
        }]

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(len(banknotesCount)):
            self.bank_notes[i]['count'] = self.bank_notes[i]['count'] + banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        rest = amount
        answer = [0 for i in range(len(self.bank_notes))]

        for i in range(len(self.bank_notes) - 1, -1, -1):
            answer[i] = min(rest // self.bank_notes[i]['value'], self.bank_notes[i]['count'])
            rest = rest - answer[i] * self.bank_notes[i]['value']
        
        if rest > 0:
            return [-1]

        for i in range(len(self.bank_notes)):
            self.bank_notes[i]['count'] = self.bank_notes[i]['count'] - answer[i]
        
        return answer


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)