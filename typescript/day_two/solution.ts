import * as fs from "fs";

function cleanData(filePath: string): number[][] {
  const data = fs.readFileSync(filePath, "utf8");
  const reportList: number[][] = [];
  const lines: string[] = data.split("\n").filter((line) => line.trim() !== "");
  for (let line of lines) {
    const cleanedLines = line.trim().split(/\s+/);
    const numList: number[] = [];
    for (let num of cleanedLines) {
      numList.push(Number(num));
    }
    reportList.push(numList);
  }
  return reportList;
}

export function checkSafe(reportLine: number[]): boolean {
  const isAscending = reportLine.every((num, index, arr) => {
    if (index === arr.length - 1) return true;
    return num < arr[index + 1];
  });
  const isDescending = reportLine.every((num, index, arr) => {
    if (index === arr.length - 1) return true;
    return num > arr[index + 1];
  });
  const rightDiff = reportLine.every((num, index, arr) => {
    if (index === arr.length - 1) return true;
    return Math.abs(num - arr[index + 1]) <= 3;
  });
  return (isAscending || isDescending) && rightDiff;
}

const reportList: number[][] = cleanData("./input.txt");
var safeReports: number = 0;
for (let report of reportList) {
  if (checkSafe(report)) {
    safeReports += 1;
  } else {
    for (let i = 0; i < report.length; i++) {
      const choppedList: number[] = [
        ...report.slice(0, i),
        ...report.slice(i + 1),
      ];
      if (checkSafe(choppedList)) {
        safeReports += 1;
        break;
      }
    }
  }
}
console.log(safeReports);
