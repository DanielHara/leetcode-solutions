# Question 1169: https://leetcode.com/problems/invalid-transactions/submissions/

# https://leetcode.com/problems/invalid-transactions/

"""
    A found it a quite interesting question despite the fact that this question received so many dislikes.
    Good exercise of data structures: first group by name, and then sort by time, and use sequential search to get the
    transactions with same name, and different cities, which occur within a timespan of less or equal to 60 minutes.
"""

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        result = []
        
        name_2_transaction_dict = {}
        for transaction in transactions:
            [name, time, amount, city] = transaction.split(',')
            
            time = int(time)
            amount = int(amount)
            
            if name not in name_2_transaction_dict:
                name_2_transaction_dict[name] = []
                
            name_2_transaction_dict[name].append({
                'name': name,
                'time': time,
                'amount': amount,
                'city': city,
                'deleted': True if amount > 1000 else False,
            })
            
            if amount > 1000:
                result.append(transaction)
        
        for name in name_2_transaction_dict:
            name_2_transaction_dict[name].sort(key=lambda el: el['time'])
        
        for transactions in name_2_transaction_dict.values():
            end = False
            while not end:
                end = True
                
                i = 0
                while i < len(transactions):
                    foundInvalid = False
                    j = i + 1
                    while j < len(transactions):
                        if transactions[j]['time'] - transactions[i]['time'] <= 60 and transactions[j]['city'] != transactions[i]['city']:             
                            foundInvalid = True
            
                            
                            if not transactions[j]['deleted']:
                                transaction = ','.join([transactions[j]['name'], str(transactions[j]['time']), str(transactions[j]['amount']), str(transactions[j]['city'])])
                                result.append(transaction)
                                end = False

                            transactions[j]['deleted'] = True
                        
                        j = j + 1
                    
                    if foundInvalid:
                        if not transactions[i]['deleted']:
                            transactions[i]['deleted'] = True
                            transaction = ','.join([transactions[i]['name'], str(transactions[i]['time']), str(transactions[i]['amount']), str(transactions[i]['city'])])

                            result.append(transaction)
                    
                    i = i + 1
        
        return result
