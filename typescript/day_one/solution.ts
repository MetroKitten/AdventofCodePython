import * as fs from "fs";

type SortedArrays = {
  sortedLeft: number[];
  sortedRight: number[];
};

function cleanData(filePath: string): {
  sortedLeft: number[];
  sortedRight: number[];
} {
  const data = fs.readFileSync(filePath, "utf8");
  const lines: string[] = data.split("\n").filter((line) => line.trim() !== "");
  let leftNum: number[] = [];
  let rightNum: number[] = [];
  for (let line of lines) {
    const [left, right] = line.trim().split(/\s+/);
    leftNum.push(Number(left));
    rightNum.push(Number(right));
  }
  const sortedLeft: number[] = leftNum.sort((a, b) => a - b);
  const sortedRight: number[] = rightNum.sort((a, b) => a - b);
  return { sortedLeft, sortedRight };
}

export function getTotal(args: SortedArrays): number {
  let total: number = 0;

  for (let i = 0; i < args.sortedLeft.length; i++) {
    const leftItem = args.sortedLeft[i];
    const rightItem = args.sortedRight[i];
    total += Math.abs(leftItem - rightItem);
  }
  return total;
}

export function getSimilarityScore(args: SortedArrays): number {
  let total: number = 0;
  const rightMap = args.sortedRight.reduce((map, item) => {
    map.set(item, (map.get(item) || 0) + 1);
    return map;
  }, new Map<number, number>());

  for (const leftItem of args.sortedLeft) {
    const occurances = rightMap.get(leftItem) || 0;
    total += leftItem * occurances;
  }
  return total;
}

const { sortedLeft, sortedRight } = cleanData("./input.txt");
const total = getTotal({ sortedLeft, sortedRight });
const simTotal = getSimilarityScore({ sortedLeft, sortedRight });
console.log("Total Distance:", total);
console.log("Total Similarity Score:", simTotal);
