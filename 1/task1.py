# -*- coding: 1251 -*-
#��� ������ �� 10 �����.������� ��������� ������� ������ ����� ��������, �.�. ����������� � ������������.
#������ � ��������� �������� �� �������������.

def calculate_number_of_elements_greater_neighbors(a):
  n=len(a);
  i=1;res=0;
  while i < n-1:
    if a[i] > a[i-1]:
     if a[i] > a[i+1]:
      res=res+1;
    i=i+i

  return res;

arr=[1,2,3,4,6,5,7,8,9,10]

print ("������:",arr);
print ("���������� ��������� ������� ������ ����� �������:",calculate_number_of_elements_greater_neighbors(arr));