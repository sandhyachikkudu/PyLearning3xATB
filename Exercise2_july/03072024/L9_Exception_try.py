class XYZ:
    def f1(self):
        try:
            a= int(input("Enter a number: "))

        except Exception as e:
            print("enter only a value")

        else:
            print(a)

        finally:
            print("anyhow i will execute")


q = XYZ()
q.f1()

