const merge = (array1, array2) => {
  const mergeSortArray = [];

  let i = 0;
  let j = 0;

  while (i < array1.length && j < array2.length) {
    if (array1[i] > array2[j]) {
      mergeSortArray.push(array2[j]);
      j++;
    } else {
      mergeSortArray.push(array1[i]);
      i++;
    }
  }

  while (j < array2.length) {
    mergeSortArray.push(array2[j]);
    j++;
  }

  while (i < array1.length) {
    mergeSortArray.push(array1[i]);
    i++;
  }

  return mergeSortArray;
};

const mergeSort = (array, start, end) => {
  if (start === end) return [array[end]];

  const mid = Math.floor((end + start) / 2);

  const mergeSortArray1 = mergeSort(array, start, mid);
  const mergeSortArray2 = mergeSort(array, mid + 1, end);

  return merge(mergeSortArray1, mergeSortArray2);
};

const array = [5, 4, 3, 2, 1];

const sortedArray = mergeSort(array, 0, array.length - 1);

console.log(array);
console.log(sortedArray);
