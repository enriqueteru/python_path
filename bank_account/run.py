import bank_account

account: bank_account = bank_account.Bank_account("enrique", 0)

bank_account.Bank_account.processTransactions(account)
account.showBalance()