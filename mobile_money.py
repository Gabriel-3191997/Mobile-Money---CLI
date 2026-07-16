import sys
import time


def simulate_loading():
    # application loading
    print("\nUSSD code running.", end="", flush=True)

    for _ in range(3):
        time.sleep(0.6)
        print(".", end="", flush=True)

    time.sleep(0.5)
    print()


def main():
    step = -1
    history = []

    # Stores the receiver's phone number
    phone = ""

    # Stores the transfer amount
    amount = ""

    # Menu options
    while True:
        dial_input = input("\n ").strip()

        if dial_input == "*144#":
            simulate_loading()
            step = 0

        elif dial_input.lower() == "exit":
            print("\nExiting dialer.")
            sys.exit()

        else:
            # Slight delay for failed codes
            print("\nUSSD code running.", end="", flush=True)
            for _ in range(3):
                time.sleep(0.4)
                print(".", end="", flush=True)
            time.sleep(0.5)
            print("\n[Error] Connection problem or invalid  code.")

        # STEP 0: MAIN MENU
        if step == 0:
            print(
                "\nWelcome to Orange Money\n"
                "1:Send Money\n"
                "2:Buy Airtime\n"
                "3:Buy Bundles\n"
                "4:Energy\n"
                "5:Pay Taxes and Fees\n"
                "6:Pay with Orange Money\n"
                "7:Cash Out\n"
                "8:Bank Services\n"
                "9:My Account\n"
                "10:Help\n"
                "---\n"
                "0:back"
            )

            choice = input("\nEnter choice: ").strip()

            # 'Send Money' is selected
            if choice == "1":
                history.append(0)
                step = 1

            # Go back to Dial Pad if they type 0
            elif choice == "0":
                print("\nDisconnecting USSD session...")
                time.sleep(0.5)
                step = -1

            else:
                print(f"\n[Info] Option {choice} is simulated successfully.")

        # CURRENCY SELECTION
        elif step == 1:
            print(
                "\n1:USD\n"
                "2:LRD\n"
                "3:My Status\n"
                "4:New Tariff\n"
                "5:OM Lifeline Bundle\n"
                "6:Buy bundle commison\n"
                "7:Reactivation Service\n"
                "8:Free 2 mins\n"
                "9:Self PIN Reset\n"
                "10:New Sim Offer\n"
                "---\n"
                "0:back"
            )

            choice = input("\nEnter choice: ").strip()

            # 'USD' is selected
            if choice == "1":
                history.append(1)
                step = 2

            # Go back to step 0
            elif choice == "0":
                step = history.pop()

            else:
                print("\n[Info] Option not simulated. Choose 1 or 0.")

        # TRANSFER
        elif step == 2:
            print(
                "\n1: To Orange Money\n"
                "2: To MTN Momo\n"
                "3: International transfer\n"
                "---\n"
                "0:back"
            )

            choice = input("\nEnter choice: ").strip()

            # 'To Orange Money' is selected
            if choice == "1":
                history.append(2)
                step = 3

            # Go back
            elif choice == "0":
                step = history.pop()

            else:
                print("\n[Info] Option not simulated. Choose 1 or 0.")

        # ENTER RECEIVER'S PHONE NUMBER
        elif step == 3:
            print("\nEnter receiver phone number\n---\n0:back")

            user_input = input("\nEnter phone: ").strip()

            # Go back
            if user_input == "0":
                step = history.pop()

            # If typed phone number, proceed
            elif user_input:
                phone = user_input
                history.append(3)
                step = 4

        # ENTER A SEND AMOUNT
        elif step == 4:
            print("\nEnter amount in USD\n---\n0:back")

            user_input = input("\nEnter amount: ").strip()

            # Go back
            if user_input == "0":
                step = history.pop()

            # If typed an amount, proceed
            elif user_input:
                amount = user_input
                history.append(4)
                step = 5

        # CONFIRMATION & PIN ENTRY
        elif step == 5:
            print(
                f"\nYou will transfer {amount} USD to {phone}\n"
                "Kun.\n"
                "Charge: 0.02\n"
                "Enter PIN to confirm.\n"
                "2.If you want Kun to received in LRD\n"
                "3.To Cancel\n"
                "---\n"
                "0:back"
            )

            choice = input("\nEnter PIN or option: ").strip()

            # Go back
            if choice == "0":
                step = history.pop()

            # Cancel and return to Main Menu
            elif choice == "3":
                print("\nTransaction cancelled.")
                history.clear()
                step = 0

            # Enter any 4-digit PIN
            elif len(choice) >= 4:
                print("\nSending request...", end="", flush=True)
                time.sleep(1.5)
                print(f"\nSuccess! You have sent {amount} USD to {phone}.")
                sys.exit()

            else:
                print("\n[Error] Invalid PIN or Choice.")


if __name__ == "__main__":
    main()

