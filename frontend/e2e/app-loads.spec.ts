import { expect, test } from "@playwright/test";

test("app loads and shows title", async ({ page }) => {
  await page.goto("/");
  await expect(page.getByRole("heading", { name: "DriftdetectionAI" })).toBeVisible();
  await expect(page.getByText("Failure intelligence for AI systems")).toBeVisible();
});
