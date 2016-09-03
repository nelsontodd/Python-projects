def bubbleSort1 (a):
  idx = 0
  while (idx < len(a) - 1):
    jdx = len(a) - 1
    while (jdx > idx):
      if (a[jdx] < a[jdx - 1]):
        a[jdx], a[jdx - 1] = a[jdx - 1], a[jdx]
      jdx = jdx - 1
    print(str(a))
    idx = idx + 1


def selectionSort (d):
  for i in range (len(d) - 1):
    # find the minimum
    min = d[i]
    minIdx = i

    for j in range (i + 1, len(d)):
        if (d[j] < min):
            minIdx = j
            min = d[j]

    # Swap the minimum element with the element at the ith place
    d[minIdx] = d[i]
    d[i] = min
    print(str(d))

def insertion_sort1 (q):
  for i in range (1, len(q)):
    j = i
    while ((j > 0) and (q[j] < q[j - 1])):
      q[j], q[j - 1] = q[j - 1], q[j]
      j += -1
      print(str(q))

def mergeSort (a, left, right):
  print('in merge main: ' + str(a))
  if (left < right):
    center = (left + right) / 2
    mergeSort (a, left, center)
    mergeSort (a, center + 1, right)
    merge_sort (a, left, center, right)

def merge_sort (a, left, center, right):
  first1 = left
  last1 = center
  first2 = center + 1
  last2 = right
  b = []

  while ((first1 <= last1) and (first2 <= last2)):
    if (a[first1] < a[first2]):
      b.append(a[first1])
      first1 = first1 + 1
    else:
      b.append(a[first2])
      first2 = first2 + 1

  while (first1 <= last1):
    b.append(a[first1])
    first1 = first1 + 1

  while (first2 <= last2):
    b.append(a[first2])
    first2 = first2 + 1

  idxA = left
  for i in range (len(b)):
    a[idxA] = b[i]
    idxA = idxA + 1
  print(str(a))

def qsort1 (d, lo, hi):
  if (lo >= hi):
    return

  pivot = d[lo]
  m = lo;
  for i in range (lo, hi + 1):

    if (d[i] < pivot):
      m = m + 1
      print('m value: '+ str(d[m]) + ' '+ str(m))
      d[m], d[i] = d[i], d[m]
    print(str(d))
  d[lo], d[m] = d[m], d[lo]
  print(str(d)+ 'out of loop'+ str(d[m]) + ' '+ str(m))
  qsort1 (d, lo, m - 1)
  qsort1 (d, m + 1, hi)

def qsort2 (e, lo, hi):
  if (lo >= hi):
    return

  left = lo
  right = hi
  pivot = e[(lo + hi) / 2]

  while (left < right):
    while (e[left] < pivot):
      left = left + 1
    while (pivot < e[right]):
      right = right - 1

    if (left <= right):
      e[left], e[right] = e[right], e[left]
      print(str(e))
      left = left + 1
      right = right - 1

  qsort2 (e, lo, right)
  qsort2 (e, left, hi)


def main():
  b = [3,6,4,9,1,2,0,7]
  c = [7,9,2,6,3,8,5,4]
  q = [7,9,2,6,3,8,5,4]
  d = [7,9,2,6,3,8,5,4]
  e = [7,9,2,6,3,8,5,4]
  #bubbleSort1(b)
  print('selectionSort: ' + '\n' )
  selectionSort(c)
  print('insertionSort: ' + '\n' )
  insertion_sort1(q)
  print('mergeSort: ' + '\n' )
  mergeSort(b,0,len(b)-1)
  print('quickSort1: ' + '\n' )
  qsort1(d,0,len(d)-1)
  print('quickSort2: ' + '\n' )
  qsort2(e,0,len(e)-1)
main()
