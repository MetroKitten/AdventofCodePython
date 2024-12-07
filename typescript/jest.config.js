/** @type {import('ts-jest').JestConfigWithTsJest} */
export default {
  preset: "ts-jest",
  testEnvironment: "node",
  moduleNameMapper: {
    "^typescript/(.*)$": "<rootDir>/typescript/$1",
  },
  extensionsToTreatAsEsm: [".ts"], // Treat .ts files as ES modules
  globals: {
    "ts-jest": {
      useESM: true,
    },
  },
};

