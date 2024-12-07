import { checkSafe } from "./solution";

describe("checkSafe", () => {
  it("Returns True for a Safe Report", () => {
    const input = [7, 6, 4, 2, 1];
    const result = checkSafe(input);
    expect(result).toBe(true);
  });
  it("Returns False for Unsafe Report", () => {
    const input = [1, 2, 7, 8, 9];
    const result = checkSafe(input);
    expect(result).toBe(false);
  });
  it("Returns False for Unsafe Report", () => {
    const input = [9, 7, 6, 2, 1];
    const result = checkSafe(input);
    expect(result).toBe(false);
  });
  it("Returns False for Unsafe Report", () => {
    const input = [1, 3, 2, 4, 5];
    const result = checkSafe(input);
    expect(result).toBe(false);
  });
  it("Returns False for Unsafe Report", () => {
    const input = [8, 6, 4, 4, 1];
    const result = checkSafe(input);
    expect(result).toBe(false);
  });
  it("Returns True for Unsafe Report", () => {
    const input = [1, 3, 6, 7, 9];
    const result = checkSafe(input);
    expect(result).toBe(true);
  });
});
