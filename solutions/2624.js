/*
    Question 2624: https://leetcode.com/problems/snail-traversal/
    Just do it.
*/


/**
 * @param {number} rowsCount
 * @param {number} colsCount
 * @return {Array<Array<number>>}
 */
 Array.prototype.snail = function(rowsCount, colsCount) {
    if (rowsCount * colsCount !== this.length) {
        return [];
    }

    const result = [];
    [...Array(rowsCount).keys()].forEach(() => {
        result.push([...Array(colsCount).keys()])
    });

    columnIndex = 0;
    rowIndex = 0;
    
    [...Array(this.length).keys()].forEach((index) => {
        result[rowIndex][columnIndex] = this[index];
        if (columnIndex % 2 === 0) {
            if (rowIndex < rowsCount - 1) {
                rowIndex = rowIndex + 1;
            } else {
                columnIndex = columnIndex + 1;
            }
        } else {
            if (rowIndex > 0) {
                rowIndex = rowIndex - 1;
            } else {
                columnIndex = columnIndex + 1
            }
        }
    });

    return result;
}

/**
 * const arr = [1,2,3,4];
 * arr.snail(1,4); // [[1,2,3,4]]
 */