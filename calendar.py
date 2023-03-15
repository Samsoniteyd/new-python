import calendar

# y = int(input("Enter the Year :"))
# m = int(input("Enter the Month of Number :"))
# print(calendar.month(y,m))




print("Enter Year: ")
yy = input()
print("\nEnter Month Number (1-12): ")
mm = input()

y = int(yy)
m = int(mm)
print("\n", calendar.month(y, m))