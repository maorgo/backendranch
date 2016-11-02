import os
import sys


def generate_numbers():
    count = 1
    while True:
        yield count
        count += 1

tax = float(3) / 4

while True:
    os.system('cls')
    print ' ---------- Investment Calculator -----------'
    starting_amount = input('Enter the starting amount:\n')
    growth_percentage = input('Enter the predicted growth percentage:\n')
    management_percentage = input('Enter the management precentage:\n')
    years = input('How many years?\n')
    try:
        int(starting_amount)
        int(growth_percentage)
        int(management_percentage)
        int(years)
    except ValueError:
        print 'Not all values are integers. Exiting.'
        sys.exit()
    growth_percentage = 1 + float(growth_percentage) / 100
    management_percentage = float(100 - management_percentage) / 100

    data = []
    current_amount = starting_amount
    for i in xrange(years):
        last_amount = current_amount
        current_amount = current_amount * growth_percentage * management_percentage
        delta = current_amount - last_amount
        data.append([current_amount, delta, delta / 12])

    taxed_total = (current_amount - starting_amount) * float(tax)
    os.system('cls')
    print '-' * 49
    print '|\t\t\tSummary\t\t\t|'
    print '-' * 49
    print 'Total amount (without paying taxes): {0:,.2f}'.format(current_amount)
    print 'Tax paying: {0:,.2f}'.format((current_amount - starting_amount) * (1 - tax))
    print '* After tax: '
    print 'Clean revenue: {0:,.2f}'.format(taxed_total)
    print 'Yearly average revenue: {0:,.2f}'.format(taxed_total / years)
    print 'Monthly average revenue: {0:,.2f}'.format(taxed_total / years / 12)
    print '-' * 49
    print '|\t\t\tDetails\t\t\t|'
    print '-' * 49
    gen = generate_numbers()
    for i in data:
        current, delta, monthly = i
        print 'Year {0}: {1:,.2f}. Revenue: {2:,.2f}. Monthly: {3:,.2f}'.format(gen.next(), current, delta, monthly)
    command = raw_input('Enter a command to continue (q - quit, any key to continue).')
    if command == 'q':
        exit()
