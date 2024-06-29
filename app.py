##important imports
from pathlib import Path
import pickle
import os

## importing for type annotations
from io import BufferedReader, BufferedWriter

##File name Constants
MAIN_FILE_NAME = "Records.dat"
TEMP_FILE_NAME = "Temp_Records.dat"


## For clearing the terminal
def clear() -> None:
    os.system("cls")


## Delaying while loop
def stop() -> None:
    input("Press Enter to continue")


## Closing Files
def fileClose(file1: BufferedReader, file2: BufferedWriter) -> None:
    file1.close()
    file2.close()


## Replacing File
def replaceFile(file1: str, file2: str) -> None:
    Path.unlink(Path(file1))
    Path.rename(Path(file2), file1)


# Formating Records
def printRecord(record: dict[str, int | str | list[str]]) -> None:
    for key, value in record.items():
        print(f"{key} => {value}")


# Insert Data
def insert(file: BufferedWriter) -> None:
    clear()
    aadhar: int = getAadhar()
    age: int = getAge()
    name: str = input("Enter Name: ")
    vaccines: list[str] = getVaccineTypes()
    record: dict[str, int | str | list[str]] = {
        "Aadhar Number": aadhar,
        "Name": name,
        "Age": age,
        "Vaccine type": vaccines,
    }
    pickle.dump(record, file)
    print("__Data Recorded__")


# Displaying record
def display() -> None:
    clear()
    with open(MAIN_FILE_NAME, "rb") as file:
        aadhar: int = getAadhar("Enter Aadhar Number to search by: ")
        while True:
            try:
                records: dict[str, int | str | list[str]] = pickle.load(file)
                if records["Aadhar Number"] == aadhar:
                    print("Record Found\n")
                    printRecord(records)
                    input("\nPress Enter to continue")
                    break
            except EOFError:
                print("No Records Found\nCheck the details and try again.")
                input("Press Enter to continue")
                break
    # input("Press Enter to continue")


def findAndCopy(
    file1: BufferedReader, file2: BufferedWriter, aadhar: int
) -> dict[str, int | str | list[str]] | None:
    updateRecord = {}
    try:
        while True:
            vaccineData: dict[str, int | str | list[str]] = pickle.load(file1)
            if vaccineData["Aadhar Number"] != aadhar:
                pickle.dump(vaccineData, file2)
            else:
                updateRecord = vaccineData
    except:
        pass
    return None if updateRecord == {} else updateRecord


# updating records
def update() -> None:
    clear()
    # getting aadhar number to search
    aadhar: int = getAadhar("Enter Aadhar number to search by: ")
    updates: int = 0
    try:
        while True:
            # opening files
            mainfile = open(MAIN_FILE_NAME, "rb")
            tempfile = open(TEMP_FILE_NAME, "ab")
            data: dict[str, int | str | list[str]] | None = findAndCopy(
                mainfile, tempfile, aadhar
            )
            if data == None:
                print("No record found\nExiting programme")
                break
            else:
                # if record found
                currentUpdate = 0
                print("Record Found:")
                printRecord(data)
                c = input(
                    "Select Field to update:\n(1) Name\n(2) Age\n(3) Vaccine Type\n(4) Quit\nOption: "
                )
                clear()
                if c == "1":
                    # updating name
                    name: str = input("Enter New Name: ")
                    newData: dict[str, int | str | list[str]] = {
                        "Aadhar Number": aadhar,
                        "Name": name,
                        "Age": data["Age"],
                        "Vaccine type": data["Vaccine Type"],
                    }
                    print("'Name'parameter updated")
                    pickle.dump(newData, tempfile)
                    updates += 1
                    currentUpdate += 1
                    fileClose(mainfile, tempfile)
                    replaceFile(MAIN_FILE_NAME, TEMP_FILE_NAME)
                    stop()
                elif c == "2":
                    # updating age
                    age: int = getAge("Enter new age: ")
                    print("'Age'parameter updated")
                    newData: dict[str, int | str | list[str]] = {
                        "Aadhar Number": aadhar,
                        "Name": data["Name"],
                        "Age": age,
                        "Vaccine type": data["Vaccine Type"],
                    }
                    pickle.dump(newData, tempfile)
                    updates += 1
                    currentUpdate += 1
                    fileClose(mainfile, tempfile)
                    replaceFile(MAIN_FILE_NAME, TEMP_FILE_NAME)
                    stop()
                elif c == "3":
                    # updating vaccines
                    newData: dict[str, int | str | list[str]] = {
                        "Aadhar Number": aadhar,
                        "Name": data["Name"],
                        "Age": data["Age"],
                        "Vaccine type": getVaccineTypes("Enter Updated Vaccines: "),
                    }
                    print("'Vaccine'parameter updated")
                    pickle.dump(newData, tempfile)
                    updates += 1
                    currentUpdate += 1
                    fileClose(mainfile, tempfile)
                    replaceFile(MAIN_FILE_NAME, TEMP_FILE_NAME)
                    stop()
                elif c == "4":
                    # quiting update
                    if updates == 0:
                        # quitting without updating anything
                        print("No record was updated")
                        fileClose(mainfile, tempfile)
                        replaceFile(MAIN_FILE_NAME, TEMP_FILE_NAME)
                        stop()
                        break
                    else:
                        if currentUpdate == 0:
                            print(
                                f"{updates} {'parameters' if updates > 1 else 'parameter'} {'were' if updates > 1 else 'was'} updated!!"
                            )
                            fileClose(mainfile, tempfile)
                            stop()
                            break
                        else:
                            print(
                                f"{updates} {'parameters' if updates > 1 else 'parameter'} {'were' if updates > 1 else 'was' } updated"
                            )
                            fileClose(mainfile, tempfile)
                            replaceFile(MAIN_FILE_NAME, TEMP_FILE_NAME)
                            stop()
                            break
                else:
                    print("Invalid Choice!!\nRecord was not updated")
                    stop()
    except EOFError:
        print("No Records Found\nCheck the details and try again.")
        stop()


def delete() -> None:
    clear()
    with open(MAIN_FILE_NAME, "rb") as mainfile, open(TEMP_FILE_NAME, "wb") as tempfile:
        aadhar: int = getAadhar("Enter Aadhar number of record to delete: ")
        # recordDeleted: bool = False
        try:
            d = findAndCopy(mainfile, tempfile, aadhar)
            if d != None:
                print("Record Deleted")
            else:
                raise EOFError
        except EOFError:
            print(
                "End of File reached\nNo Records Found\nCheck the details and try again."
            )
    Path.unlink(Path(MAIN_FILE_NAME))
    Path.rename(Path(TEMP_FILE_NAME), MAIN_FILE_NAME)
    input("Press Enter to continue...")


def getAadhar(msg: str = "Enter Aadhar number: ") -> int:
    while True:
        try:
            aadhar: str = input(msg)
            if len(aadhar) != 4:
                raise ValueError
            elif aadhar.isnumeric() != True:
                raise TypeError
            elif int(aadhar) < 0:
                raise ValueError
            else:
                break
        except TypeError:
            print("Please enter valid Aadhar Number")
            continue
        except ValueError:
            print("Enter valid 4 digit Aadhar number")
            continue
        except EOFError:
            print("Please input something....")
            continue
    return int(aadhar)


def getAge(msg: str = "Enter Age: ") -> int:
    while True:
        try:
            age: str = input(msg)
            if age.isnumeric() != True:
                raise TypeError
            elif int(age) < 18:
                raise ValueError
            else:
                break
        except TypeError:
            print("Please enter valid Age")
            continue
        except ValueError:
            print("Age should be above 18 years old")
            continue
        except EOFError:
            print("Please input something....")
            continue
    return int(age)


def getVaccineTypes(msg: str = "Enter Vaccine Name: ") -> list[str]:
    vaccines: list[str] = []
    while True:
        clear()
        vaccines.append(input(msg))
        add: str = input("Do yo wish to add more Vaccines? (y/n): ")
        if add.lower() == "n":
            break
        elif add.lower() != "y":
            print("invalid choice\nNo more Vaccines will be added!")
            break
        else:
            pass
    return vaccines


def vaccineManagementMenu():
    while True:
        clear()
        choice = input(
            "\n---Vaccine Managemment System---\n\nMenu:\n(1) Insert Record\n(2) Display Record\n(3) Update Record\n(4) Delete Record\n(q) Quit programe\nOption:  "
        )
        if choice == "1":
            with open(MAIN_FILE_NAME, "ab") as records:
                insert(records)
                while True:
                    yn = input("Do you want to add more records? (y/n/Y/N): ")
                    if yn.lower() == "n":
                        break
                    elif yn.lower() != "y":
                        print("Invalid choice. Please give a y/n answer.")
                    else:
                        insert(records)
        elif choice == "2":
            display()
        elif choice == "3":
            update()
        elif choice == "4":
            delete()
        elif choice == "q" or choice == "Q":
            clear()
            print("Exiting programe")
            break
        else:
            print("invalid Choice")
            input("Press Enter to continue")


if __name__ == "__main__":
    vaccineManagementMenu()
    # pdconsec.vscode-print
