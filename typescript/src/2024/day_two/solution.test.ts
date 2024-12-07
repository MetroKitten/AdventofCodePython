import { checkSafe } from "./solution";
import { expect, test, describe } from "bun:test";
describe("checkSafe", () => {
  test("Returns True for a Safe Report", () => {
    const input = [7, 6, 4, 2, 1];
    const result = checkSafe(input);
    expect(result).toBe(true);
  });
  test("Returns False for Unsafe Report", () => {
    const input = [1, 2, 7, 8, 9];
    const result = checkSafe(input);
    expect(result).toBe(false);
  });
  test("Returns False for Unsafe Report", () => {
    const input = [9, 7, 6, 2, 1];
    const result = checkSafe(input);
    expect(result).toBe(false);
  });
  test("Returns False for Unsafe Report", () => {
    const input = [1, 3, 2, 4, 5];
    const result = checkSafe(input);
    expect(result).toBe(false);
  });
  test("Returns False for Unsafe Report", () => {
    const input = [8, 6, 4, 4, 1];
    const result = checkSafe(input);
    expect(result).toBe(false);
  });
  test("Returns True for Unsafe Report", () => {
    const input = [1, 3, 6, 7, 9];
    const result = checkSafe(input);
    expect(result).toBe(true);
  });
});
