import { getTotal } from "./solution";

describe("getTotal", () => {
  it("Returns the correct Total Distance", () => {
    const input = {
      sortedLeft: [1, 3, 5],
      sortedRight: [2, 4, 6],
    };
    const result = getTotal(input);
    expect(result).toBe(3);
  });
});
