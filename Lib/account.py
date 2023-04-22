class account:
    """
    A class cintaining a name and value, representing an account.
    """


    def __init__(self, name: str):
        """
        Constructor to create an initial state of a person object.
        :param name: Person's first name.
        """

        self.__account_name = name
        self.__account_balance = 0


        def deposit(self, amount: float) -> bool:
            """
            Function to add money to the account.
            :param amount: Amount to deposit.
            :return: Returns True/False. When True is returned, account balance has been updated, with amount added to it.
            """
            if amount > 0:
                self.__account_balance = self.__account_balance + amount
                return True
            else:
                return False


        def withdraw(self, amount: float) -> bool:
            """
            Function to withdraw money from the account.
            :param amount: Amount to withdraw.
            :return: Returns True/False. When True is returned, account balance has been updated, with amount removed from it.
            """
            if amount > 0:
                if amount <= self.__account_balance:
                    self.__account_balance = self.__account_balance - amount
                    return True
                else:
                    return False
            else:
                return False


        def getbalance(self) -> float:
            """
            Retrieves Account balance.
            :return: Returns the account balance.
            """
            return self.__account_balance


        def getname(self) -> float:
            """
            Retrieves account name.
            :return: Returns the account name.
            """
            return self.__account_name