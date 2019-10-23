class invoice(object):
    def __init__(self, days_to_invoice):
        self.invoice = days_to_invoice

    def makeString(self, entry):
        result = f"{entry[0]}:[{entry[1]}] Invoice for {entry[2]} for {entry[3]} dollars"
        return result


    def getInvoiceEmailList(self, member_list):
        email_list = []

        for member in member_list:
            now = member[0]
            name = member[1]
            amount = member[2]

            for entry in self.invoice:
                target_day = entry[0] + now
                target_message = entry[1]

                email_list.append((target_day, target_message, name, amount))

        email_list.sort(key=lambda t:t[0])
        result = []
        for entry in email_list:
            result.append(self.makeString(entry))
        return result

input = [(-10, "Upcoming"), (0, "New"), (20, "Reminder"), (30, "Due")]
inv = invoice(input)

for entry in inv.getInvoiceEmailList([(0, "Alice", 200), (0, "Bob", 100)]):
    print(entry)
