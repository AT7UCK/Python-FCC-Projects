class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item.get("amount", 0) for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = ""
        for entry in self.ledger:
            desc = entry.get("description", "")[:23]
            amt = entry.get("amount", 0)
            items += f"{desc:<23}{amt:>7.2f}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    spends = []
    for cat in categories:
        spent = sum(-item.get("amount", 0) for item in cat.ledger if item.get("amount", 0) < 0)
        spends.append(spent)

    total_spent = sum(spends)
    percentages = [int((s / total_spent) * 100) // 10 * 10 if total_spent > 0 else 0 for s in spends]

    lines = ["Percentage spent by category"]

    for level in range(100, -1, -10):
        row = str(level).rjust(3) + "|"
        for p in percentages:
            row += " o " if p >= level else "   "
        row += " "
        lines.append(row)

    dashes = "    " + "-" * (len(categories) * 3 + 1)
    lines.append(dashes)

    max_len = max(len(cat.name) for cat in categories)
    for i in range(max_len):
        row = "    "
        for cat in categories:
            if i < len(cat.name):
                row += " " + cat.name[i] + " "
            else:
                row += "   "
        row += " "
        lines.append(row)

    return "\n".join(lines)