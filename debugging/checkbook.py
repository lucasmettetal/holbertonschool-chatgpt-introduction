class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        """
        Function description:
        Adds money to the account balance.

        Parameters:
        amount (float): The amount of money to add.

        Returns:
        None
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Function description:
        Withdraws money from the account if sufficient funds exist.

        Parameters:
        amount (float): The amount of money to withdraw.

        Returns:
        None
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Function description:
        Displays the current account balance.

        Parameters:
        None

        Returns:
        None
        """
        print("Current Balance: ${:.2f}".format(self.balance))


def get_valid_amount(prompt):
    """
    Function description:
    Safely asks the user for a numeric amount and prevents crashes.

    Parameters:
    prompt (str): Message shown to the user.

    Returns:
    float: A valid numeric amount entered by the user.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def main():
    cb = Checkbook()
    while True:
        action = input(
            "What would you like to do? (deposit, withdraw, balance, exit): "
        ).lower()

        if action == "exit":
            break

        elif action == "deposit":
            amount = get_valid_amount("Enter the amount to deposit: $")
            cb.deposit(amount)

        elif action == "withdraw":
            amount = get_valid_amount("Enter the amount to withdraw: $")
            cb.withdraw(amount)

        elif action == "balance":
            cb.get_balance()

        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
