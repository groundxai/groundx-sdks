import { Groundx } from "./index";

it("quick start", async () => {
  const groundx = new Groundx({
    apiKey: process.env.GROUNDX_API_KEY,
  });

  const bucket = await groundx.bucket.create({
    bucket: { name: "sdk-test-bucket" },
  });

  const bucketId = bucket.data.bucket.bucketId;

  const ingestProcess = await groundx.document.upload({});
});
