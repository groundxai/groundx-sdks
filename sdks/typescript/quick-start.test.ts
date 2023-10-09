import { Groundx } from "./index";
import * as fs from "fs";

it.skip("quick start", async () => {
  // const groundx = new Groundx({
  //   apiKey: process.env.GROUNDX_API_KEY,
  // });
  // const project = await groundx.project.create({
  //   project: {
  //     name: "My Project",
  //   },
  // });
  // const bucket = await groundx.bucket.create({
  //   bucket: {
  //     name: "My Bucket",
  //   },
  // });
  // let ingest = await groundx.document.uploadRemote({
  //   documents: [
  //     {
  //       bucketId: bucket.data.bucket.bucketId,
  //       sourceUrl:
  //         "https://raw.githubusercontent.com/konfig-dev/groundx-sdks/main/document.txt",
  //     },
  //   ],
  // });
  // while (ingest.data.ingest.status !== "complete") {
  //   ingest = await groundx.document.getProcessingStatusById({
  //     processId: ingest.data.ingest.processId,
  //   });
  //   // sleep for 3 seconds
  //   await new Promise((resolve) => setTimeout(resolve, 3000));
  // }
  // const search = await groundx.search.content({
  //   id: project.data.project.projectId,
  //   search: {
  //     query: "hello",
  //   },
  // });
  // console.log(search.data);
});

it.skip("quick start - local", async () => {
  // const groundx = new Groundx({
  //   apiKey: process.env.GROUNDX_API_KEY,
  // });
  // const projects = await groundx.projects.list();
  // const project = projects.data.projects?.[0];
  // const buckets = await groundx.buckets.list();
  // const bucket = buckets.data.buckets?.[0];
  // if (project === undefined || bucket === undefined) {
  //   throw new Error("project or bucket is undefined");
  // }
  // let ingest = await groundx.documents.uploadLocal([
  //   {
  //     blob: fs.readFileSync("../../document.txt"),
  //     metadata: {
  //       bucketId: bucket.bucketId,
  //       fileName: "document-1.txt",
  //       fileType: "txt",
  //     },
  //   },
  //   {
  //     blob: fs.readFileSync("../../document.txt"),
  //     metadata: {
  //       bucketId: bucket.bucketId,
  //       fileName: "document-2.txt",
  //       fileType: "txt",
  //     },
  //   },
  // ]);
  // while (ingest.data.ingest.status !== "complete") {
  //   ingest = await groundx.documents.getProcessingStatusById({
  //     processId: ingest.data.ingest.processId,
  //   });
  //   // sleep for 3 seconds
  //   await new Promise((resolve) => setTimeout(resolve, 3000));
  // }
  // const search = await groundx.search.content({
  //   id: project.projectId,
  //   search: {
  //     query: "hello",
  //   },
  // });
  // console.log(search.data);
});
