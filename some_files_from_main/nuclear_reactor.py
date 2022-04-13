def is_criticality_balanced(temperature, neutrons_emitted):
    if temperature <= 800 and neutrons_emitted >= 500:
        print('\nReactor Is Balanced!')
        return True
    else:
        print("\nReactor Is Melting!")
        return False


is_criticality_balanced(800, 500)


def reactor_efficiency(voltage, current, max_power):
    print('Power Output:', end=" ")
    efficiency = ((voltage*current)/max_power)*100

    if efficiency >= 80:
        print('green')
    elif efficiency >= 60 and efficiency <= 80:
        print('orange')
    if efficiency >= 30 and efficiency <= 60:
        print('red')
    if efficiency < 30:
        print('black')


reactor_efficiency(200, 50, 15000)


def fail_safe(temperature=1000, neutrons_produced_per_second=30, threshold=5000):
    status_code = "DANGER"
    criticality = temperature * neutrons_produced_per_second
    if criticality < (threshold * .9):
        status_code = "LOW"
    elif (threshold * 0.9) <= criticality <= (threshold * 1.1):
        status_code = "NORMAL"
    print("Efficiency Level:", status_code, "\n")


fail_safe()
