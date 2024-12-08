import * as fs from "fs";
import * as path from "path";
import { fileURLToPath } from "url";

export function findMuls(text: string): number {
  let uncorrupted: number = 0;
  const regex = /mul\((\d+),(\d+)\)/g;
  const matches = text.matchAll(regex);
  for (const [, left, right] of matches) {
    uncorrupted += parseInt(left) * parseInt(right);
  }
  return uncorrupted;
}

function enabledMuls(text: string): number {
  const regex = /mul\((\d+),(\d+)\)|do\(\)|don't\(\)/g;
  let enabled = true;
  let uncorrupted = 0;
  const matches = [...text.matchAll(regex)];
  for (const match of matches) {
    if (match[0] === "do()") {
      enabled = true;
    } else if (match[0] === "don't()") {
      enabled = false;
    } else if (enabled && match[1] && match[2]) {
      const left = parseInt(match[1], 10);
      const right = parseInt(match[2], 10);
      uncorrupted += left * right;
    }
  }
  return uncorrupted;
}

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const filePath = path.join(__dirname, "input.txt");
const data = fs.readFileSync(filePath, "utf8");
console.log("Uncorrupted Total: ", findMuls(data));
console.log("Enabled Total: ", enabledMuls(data));
