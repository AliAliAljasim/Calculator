class Calculator:
    def __init__(self, Input):
        Input = Input.replace(" ", "")
        inputList = list(Input)  # Removed list comprehension for simplicity
        self.numList = []
        self.opList = []
        self.tempNum = ''
        self.N = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']

        # Splitting inputList into numList, opList
        self.formNumber(inputList)
        self.solve()

        while any(op in self.opList for op in ['+', '-', '*', '/', '^']):
            self.solve()

        self.result = self.numList[0]

    def solveBrackets(self, Input):
        inputList = list(Input)
        numList, opList = [], []
        tempNum = ''

        for x in inputList:  # Simplified using direct iteration
            if x in self.N:
                tempNum += x
            else:
                if tempNum:
                    numList.append(float(tempNum))
                    tempNum = ''
                opList.append(x)

        if tempNum:
            numList.append(float(tempNum))

        # Solve using operator precedence
        self.numList, self.opList = numList, opList
        self.solve()
        while any(op in self.opList for op in ['+', '-', '*', '/', '^']):
            self.solve()

        return self.numList[0]

    def formNumber(self, inputList):
        tempNum = ''
        brackets = False

        for x in inputList:
            if x == '(':
                brackets = True
                continue
            elif x == ')':
                brackets = False
                tempNum = str(self.solveBrackets(tempNum))
                self.numList.append(float(tempNum))
                tempNum = ''
                continue

            if brackets:
                tempNum += x
            else:
                if x in self.N:
                    tempNum += x
                else:
                    if tempNum:
                        self.numList.append(float(tempNum))
                        tempNum = ''
                    self.opList.append(x)

        if tempNum:
            self.numList.append(float(tempNum))

    def solve(self):
        for op in ['^', '/', '*', '+', '-']:
            while op in self.opList:
                idx = self.opList.index(op)
                if op == '^':
                    self.numList[idx] = float(self.numList[idx]) ** self.numList[idx + 1]
                elif op == '/':
                    self.numList[idx] = float(self.numList[idx]) / self.numList[idx + 1]
                elif op == '*':
                    self.numList[idx] = float(self.numList[idx]) * self.numList[idx + 1]
                elif op == '+':
                    self.numList[idx] = float(self.numList[idx]) + self.numList[idx + 1]
                elif op == '-':
                    self.numList[idx] = float(self.numList[idx]) - self.numList[idx + 1]

                self.numList.pop(idx + 1)
                self.opList.pop(idx)

try:
    while True:
        try:
            cal = Calculator(input("Enter An Equation: "))  # Use input for Python 3.x
            print(cal.result)
        except Exception as e:
            print("Sorry, there's an error:", e)
            break  # Exit the loop if an error occurs
except KeyboardInterrupt:
    print("\nExiting...")
