def Hanoi(n, source, auxi, dest):
  if n == 1:
    print(f"Chuyển đĩa 1 từ cột {source} đến cột {dest}")
    return#Chỉ dừng lại và in ra nội dung trên
  #Giả sử hàm Hanoi đã hoạt động "ok" trên subproblem (n-1)
  Hanoi(n-1, source, dest, auxi)#Chuyển n-1 đĩa từ source đến auxi
  #Mỗi một lần chuyển thành công từ n-1 từ source đến auxi thì
  #ta đã chuyển thành công được một đĩa dưới lớn thì source đến dest, nên ta print ra
  print(f"Chuyển đĩa {n} từ cột {source} đến cột {dest}")
  Hanoi(n-1, auxi, source, dest)#chuyển n-1 đĩa từ auxi đến đích (sau khi đã chuyển xong đĩa lớn nhất đến dest)
Hanoi(3, 'A', 'B', 'C')