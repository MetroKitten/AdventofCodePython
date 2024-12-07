import { getTotal, getSimilarityScore } from "./solution";
import { expect, test, describe } from "bun:test";

describe("getTotal", () => {
  test("Returns the correct Total Distance", () => {
    const input = {
      sortedLeft: [1, 3, 5],
      sortedRight: [2, 4, 6],
    };
    const result = getTotal(input);
    expect(result).toBe(3);
  });
});

describe("getSimilarityScore", () => {
  test("Returns the correct total Similarity Score", () => {
    const input = {
      sortedLeft: [1, 2, 3, 3, 3, 4],
      sortedRight: [3, 3, 3, 4, 5, 9],
    };
    const result = getSimilarityScore(input);
    expect(result).toBe(31);
  });
});
